#!/usr/bin/env python
import argparse
from pathlib import Path

from postersession.japanmap import save_image
from postersession.pyconjp import get_prefs


def main(output: str, cache_directory: str | None) -> None:
    prefs = get_prefs(cache_directory)
    save_image(prefs, Path(output))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="pyconapac2023-postersession-japanmap",
        description="The map shows the provinces where the Python Boot Camp was held",
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Image Output Destination"
    )
    parser.add_argument(
        "-c", "--cache", default=None, required=False, help="Cache Directory"
    )
    args = parser.parse_args()
    main(output=args.output, cache_directory=args.cache)
