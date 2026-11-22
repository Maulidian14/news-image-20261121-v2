#!/usr/bin/env python3
"""Entrypoint for "The World Today: 47 Stories", one image summing up
Saturday 21 November 2026's world news (make.fun news-image-20261121).

The newspaper page is designed in index.html and rendered to entry.png by
generate.mjs; this program copies that image into the output directory.
Deterministic: every run writes identical bytes. No network.
"""
import os
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    source = REPO_ROOT / "entry.png"
    if not source.is_file():
        raise SystemExit(f"missing source image: {source}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT_DIR / "entry.png"
    shutil.copyfile(source, destination)
    print("wrote", destination)


if __name__ == "__main__":
    main()
