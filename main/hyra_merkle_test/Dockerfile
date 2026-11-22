FROM rust:1-bookworm AS builder

WORKDIR /app
COPY Cargo.toml main.rs ./
RUN cargo build --release

FROM debian:bookworm-slim
COPY --from=builder /app/target/release/rust_proj_memory /usr/local/bin/rust_exec
ENTRYPOINT ["/usr/local/bin/rust_exec"]
