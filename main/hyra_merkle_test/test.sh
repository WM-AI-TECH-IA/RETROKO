#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
docker build -t hyra_merkle_test .
docker run --rm hyra_merkle_test
