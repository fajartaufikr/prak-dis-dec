se litesvm::LiteSVM;
use solana_sdk::{
    signature::{read_keypair_file, Signer},
};

#[test]
fn test_hello_solana() {
    let mut svm = LiteSVM::new();

    let solana_keypair_path = "target/deploy/hello_solana-keypair.json";
    let solana_so_path = "target/deploy/hello_solana.so";

    let program_keypair = read_keypair_file(solana_keypair_path).unwrap();
    let program_id = program_keypair.pubkey();

    svm.add_program_from_file(program_id, solana_so_path)
        .expect("Failed to deploy program");

    assert!(svm.get_account(&program_id).unwrap().executable);
}
