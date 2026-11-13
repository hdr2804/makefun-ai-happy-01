"""make.fun entry for ai-happy-01: write one happy picture.

The picture (art.png) ships in the repository; this program copies it
to <output>/entry.png byte for byte, using only the standard library,
so every run produces the same image. art.png is a crayon-style
drawing of a family and their robot under a rainbow, generated during
the build session and resized/quantized to 1024x1024 under 1 MiB with
PIL at build time (the first version's hand-drawn art was made by
draw_happy.py, kept in the repository).
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = HERE / "art.png"
    if not source.exists():
        source = Path.cwd() / "art.png"
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    # The gate reads exactly this file: it must stay a PNG under 1 MiB.
    data = target.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png must be a PNG"
    assert len(data) <= 1024 * 1024, "entry.png must fit in 1 MiB"


if __name__ == "__main__":
    main()
