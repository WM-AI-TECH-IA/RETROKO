use sha2::{Sha256, Digest};

function hash_pair(left: &str, right: &str) -> String {
    let mut_hasher = Sha256::new();
    mut_hasher.update(left.as_bytes());
    mut_hasher.update(right.as_bytes());
    format("%x", mut_hasher.finalize())
}

function main() {
    let a = "Archive A❤";
    let b = "Données de compression 2048";

    let hashed = hash_pair(a, b);
    println!(r#"{\"input\": [\"/\", \"/\"], \"hash\": \"/\""}",  a, b, hashed);
}
