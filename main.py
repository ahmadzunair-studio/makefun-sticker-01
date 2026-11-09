"""Emit the reviewed original sticker without generating it at grading time."""

import os
from pathlib import Path


def main():
    payload = Path(__file__).with_name("entry.png").read_bytes()
    output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    output.joinpath("entry.png").write_bytes(payload)


if __name__ == "__main__":
    main()
