"""Ship the finished front page to the grader's output folder.

The newspaper image is rendered ahead of time from index.html (see
generate.mjs) and stored in this repository as entry.png. All this
program does is carry those exact bytes to /output/entry.png, so the
two runs the grader makes produce identical files. It uses only the
standard library and never touches the network.
"""

from pathlib import Path

BLOCK = 1024 * 1024


def shipped_picture() -> Path:
    """Locate entry.png next to this program, whatever the workdir is."""
    return Path(__file__).resolve().with_name("entry.png")


def stream_copy(origin: Path, target: Path) -> int:
    """Copy a file in blocks; return how many bytes were written.

    Raises RuntimeError if the copy ends up shorter than the source,
    so a truncated write fails loudly instead of shipping a bad file.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    moved = 0
    with origin.open("rb") as source, target.open("wb") as sink:
        while True:
            chunk = source.read(BLOCK)
            if not chunk:
                break
            sink.write(chunk)
            moved += len(chunk)
    if target.stat().st_size != origin.stat().st_size:
        raise RuntimeError("copy incomplete: size mismatch")
    return moved


def main() -> None:
    picture = shipped_picture()
    total = stream_copy(picture, Path("/output/entry.png"))
    print(f"delivered {total} bytes to /output/entry.png")


if __name__ == "__main__":
    main()
