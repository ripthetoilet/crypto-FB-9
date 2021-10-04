use itertools::Itertools;
use std::collections::HashMap;
use std::hash::Hash;
use std::iter::Iterator;

pub type Frequency<T> = HashMap<T, f32>;
pub type Redundancy = f32;

pub trait EntropyExt<T> {
    fn calc_entropy(&self, n: f32) -> f32;
}

pub trait RedundancyExt {
    fn calc_redundancy(&self, n: f32) -> f32;
}

impl<T> EntropyExt<T> for Frequency<T> {
    fn calc_entropy(&self, n: f32) -> f32 {
        let mut entropy = 0f32;
        for frequency in self.values() {
            entropy += -frequency * frequency.log2()
        }
        entropy *= 1f32 / n;
        entropy
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
    let mut frequency = HashMap::new();

    for item in iter {
        *frequency.entry(item).or_insert(0f32) += 1f32;
    }

    let len: f32 = frequency.values().sum();
    for (_, v) in frequency.iter_mut() {
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
