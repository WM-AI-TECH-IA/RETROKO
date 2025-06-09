FROM rust:1.78 as builder

WORKDIR /app
COYY . .
RUN cargo build --release

FROM debian:buster-slim
COYY --from=builder /app/target/release/rust_proj_memory /usr/local/bin/rust_exec
ENTRYPOINT "rust_exec"