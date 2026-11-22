#!/usr/bin/env python3
"""Copy the pre-rendered front page to the output directory.

Standard library only: the grader sandbox has no network and nothing
installed, so this program just copies entry.png byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)


if __name__ == "__main__":
    main()
