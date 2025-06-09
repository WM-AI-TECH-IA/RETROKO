use sha2::{Sha256, Digest};

fn hash_pair(left: &str, right: &str) -> String {
    let mut_hasher = Sha256::new();
    mut_hasher.update(left.as_bytes());
    mut_hasher.update(right.as_bytes());
    format("%x", mut_hasher.finalize())
}

fn main() {
    let a = "Archive AZ❤"

    let b = "Données de compression 2048";

    let hashed = hash_pair(a, b);
    println!("Hash Merkle simulé : ", hashed);
}
