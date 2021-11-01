use anyhow::{Context, Result};
use regex::Regex;
use std::fs;
use std::path::{Path, PathBuf};

pub fn filter_file<P: AsRef<Path>>(path: P) -> Result<String> {
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
        let russian_letters = Regex::new("[^а-яё ]+")?;
        let text = russian_letters.replace_all(&lowercase_text, " ");
        let multiple_whitespaces = Regex::new(r"\s+")?;
        let filtered_text = multiple_whitespaces.replace_all(text.as_ref(), " ");
        let final_text = filtered_text.replace("ё", "е").replace("ъ", "ь");
        fs::write(filtered_file, final_text.as_bytes())?;
        Ok(final_text)
    }
}
