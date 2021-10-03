use std::fmt::Debug;

use crate::calculation::{Frequency, EntropyExt, RedundancyExt};

mod calculation;
mod filter;

fn print_info<T: Debug>(frequency: Frequency<T>, n_gram: f32, letters_num: f32) {
    println!("Frequency \
    {:?}", frequency);
    let entropy = frequency.calc_entropy(n_gram);
    println!("Entropy: {}", entropy);
    println!("Redundancy: {}", entropy.calc_redundancy(letters_num));
}

fn main() {
    let spaces_text = filter::filter_file("text.txt").unwrap();
    let no_spaces_text: String = spaces_text.chars().filter(|c| !c.is_whitespace()).collect();

    println!("Text monogram with spaces: ");
    print_info(calculation::count_monogram_frequency(&spaces_text), 1f32, 34f32);
    println!("Text bigram with spaces: ");
    print_info(calculation::count_bigram_frequency(&spaces_text), 2f32, 34f32);
    println!("Text monogram without spaces: ");
    print_info(calculation::count_monogram_frequency(&no_spaces_text), 1f32, 33f32);
    println!("Text bigram without spaces: ");
    print_info(calculation::count_bigram_frequency(&no_spaces_text), 2f32, 33f32);
}
