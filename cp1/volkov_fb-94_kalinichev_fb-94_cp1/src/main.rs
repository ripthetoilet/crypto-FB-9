use anyhow::{Context, Result};
use regex::Regex;
use std::fs;
use std::path::{Path, PathBuf};
use std::collections::HashMap;

fn filter_file<P: AsRef<Path>>(path: P) -> Result<String> {
    let file_name = path
        .as_ref()
        .file_name()
        .context("Failed to get file name from path")?
        .to_str()
        .context("Path include non UTF-8 symbols")?
        .to_string();

    let filtered_file = PathBuf::from(format!("filtered_{}", file_name));
    if filtered_file.exists() {
        println!("File already filtered!");
        Ok(fs::read_to_string(filtered_file)?)
    } else {
        let lowercase_text = fs::read_to_string(path)?.to_lowercase();
        let russian_letters = Regex::new("[^а-я-ё ]+")?;
        let text = russian_letters.replace_all(&lowercase_text, " ");
        let multiple_whitespaces = Regex::new(r"\s+")?;
        let filtered_text = multiple_whitespaces.replace_all(text.as_ref(), " ");
        fs::write(filtered_file, filtered_text.as_bytes())?;
        Ok(filtered_text.to_string())
    }
}

fn count_bigram_frequency(text: &str) -> HashMap<String, u32> {
    let mut frequency = HashMap::new();

    let mut chars = text.chars();
    let mut last_char = chars.next().unwrap();
    while let Some(char) = chars.next() {
        *frequency.entry(format!("{}{}", last_char, char)).or_insert(0) += 1;
        last_char = char;
    }
    frequency
}

fn count_monogram_frequency(text: &str) -> HashMap<char, u32> {
    let mut frequency = HashMap::new();

    let mut chars = text.chars();
    while let Some(char) = chars.next() {
        *frequency.entry(char).or_insert(0) += 1;
    }
    frequency
}

fn main() {
    let text = filter_file("text.txt").unwrap();
    dbg!(count_monogram_frequency(&text));
    dbg!(count_bigram_frequency(&text));
}
