use serde_json::json;
use sha2::{Digest, Sha256};

fn hash_pair(left: &str, right: &str) -> String {
    let mut hasher = Sha256::new();
    hasher.update(left.as_bytes());
    hasher.update(right.as_bytes());
    format!("{:x}", hasher.finalize())
}

fn main() {
    let left = "Archive A❤";
    let right = "Données de compression 2048";
    println!(
        "{}",
        json!({"input": [left, right], "hash": hash_pair(left, right)})
    );
}
