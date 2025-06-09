#!/bin/bash
echo "[I] Build et ex%c3%a8cution du conteneur Rust"
docker build -t hyra_merkle_test .
docker run hyra_merkle_test