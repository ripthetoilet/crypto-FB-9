use itertools::Itertools;
use std::cmp::Ordering;
use std::collections::HashMap;
use std::fmt;
use std::fmt::Display;
use std::hash::Hash;
use std::iter::Iterator;

pub type Redundancy = f32;
pub struct Frequency<T>(HashMap<T, f32>);

pub trait RedundancyExt {
    fn calc_redundancy(&self, n: f32) -> f32;
}

impl<T> Frequency<T> {
    fn new() -> Self {
        Frequency(HashMap::new())
    }

    pub fn calc_entropy(&self, n: f32) -> f32 {
        let mut entropy = 0f32;
        for frequency in self.0.values() {
            entropy += -frequency * frequency.log2()
        }
        entropy *= 1f32 / n;
        entropy
    }
}

impl<T: Display> fmt::Display for Frequency<T> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        self.0
            .iter()
            .sorted_by(|(_, a), (_, b)| b.partial_cmp(a).unwrap_or(Ordering::Equal))
            .fold(Ok(()), |result, (key, value)| {
                result.and_then(|_| writeln!(f, "'{}': {}", key, value))
            })
    }
}

impl RedundancyExt for Redundancy {
    fn calc_redundancy(&self, n: f32) -> f32 {
        1f32 - (self / n.log2())
    }
}

fn count_frequency<T, I>(iter: I) -> Frequency<T>
where
    T: Eq + Hash,
    I: Iterator<Item = T>,
{
    let mut frequency = Frequency::new();

    for item in iter {
        *frequency.0.entry(item).or_insert(0f32) += 1f32;
    }

    let len: f32 = frequency.0.values().sum();
    for (_, v) in frequency.0.iter_mut() {
        *v = *v / len;
    }

    frequency
}

pub fn count_bigram_frequency(text: &str) -> Frequency<String> {
    let chunks = text.chars().chunks(2);
    let iter = chunks
        .into_iter()
        .map(|item| item.collect::<String>())
        .filter(|n| n.chars().count() == 2);
    count_frequency(iter)
}

pub fn count_bigram_intersection_frequency(text: &str) -> Frequency<String> {
    let iter = text
        .chars()
        .tuple_windows()
        .map(|(a, b)| format!("{}{}", a, b));
    count_frequency(iter)
}

pub fn count_monogram_frequency(text: &str) -> Frequency<char> {
    count_frequency(text.chars())
}
