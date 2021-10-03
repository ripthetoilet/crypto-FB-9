use std::collections::HashMap;

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

pub fn count_bigram_frequency(text: &str) -> Frequency<String> {
    let mut frequency = HashMap::new();

    let mut chars = text.chars();
    let mut last_char = chars.next().unwrap();
    while let Some(char) = chars.next() {
        *frequency
            .entry(format!("{}{}", last_char, char))
            .or_insert(0f32) += 1f32;
        last_char = char;
    }
    let len: f32 = frequency.values().sum();

    for (_, v) in frequency.iter_mut() {
        *v = *v / len;
    }
    frequency
}

pub fn count_monogram_frequency(text: &str) -> Frequency<char> {
    let mut frequency = HashMap::new();

    let mut chars = text.chars();
    while let Some(char) = chars.next() {
        *frequency.entry(char).or_insert(0f32) += 1f32;
    }
    for (_, v) in frequency.iter_mut() {
        *v = *v / text.len() as f32;
    }
    frequency
}
