mod calculation;
mod filter;

fn main() {
    let text = filter::filter_file("text.txt").unwrap();
    dbg!(calculation::count_monogram_frequency(&text));
    dbg!(calculation::count_bigram_frequency(&text));
}
