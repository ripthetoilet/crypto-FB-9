use std::fmt;

use crate::calculation::{Frequency, RedundancyExt};

mod calculation;
mod filter;

fn print_info<T: fmt::Display>(frequency: Frequency<T>, n_gram: f32, letters_num: f32) {
    println!(
        "Frequency:\n\
        {}",
        frequency
    );
    let entropy = frequency.calc_entropy(n_gram);
    println!("Entropy: {}", entropy);
    println!("Redundancy: {}", entropy.calc_redundancy(letters_num));
}

fn main() {
    let spaces_text = filter::filter_file("text.txt").unwrap();
    let no_spaces_text: String = spaces_text.chars().filter(|c| !c.is_whitespace()).collect();

    println!("Text monograms with spaces: ");
    print_info(
        calculation::count_monogram_frequency(&spaces_text),
        1f32,
        32f32,
    );
    println!("Text bigrams with spaces: ");
    print_info(
        calculation::count_bigram_frequency(&spaces_text),
        2f32,
        32f32,
    );
    println!("Text intersection bigrams with spaces: ");
    print_info(
        calculation::count_bigram_intersection_frequency(&spaces_text),
        2f32,
        32f32,
    );
    println!("Text monograms without spaces: ");
    print_info(
        calculation::count_monogram_frequency(&no_spaces_text),
        1f32,
        31f32,
    );
    println!("Text bigrams without spaces: ");
    print_info(
        calculation::count_bigram_frequency(&no_spaces_text),
        2f32,
        31f32,
    );
    println!("Text intersection bigrams without spaces: ");
    print_info(
        calculation::count_bigram_intersection_frequency(&no_spaces_text),
        2f32,
        31f32,
    );
}
