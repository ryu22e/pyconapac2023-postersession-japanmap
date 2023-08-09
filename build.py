#!/usr/bin/env python
import argparse
from typing import TypeAlias

import matplotlib.pyplot as plt
from japanmap import picture

from postersession.pyconjp import get_prefs

Color: TypeAlias = tuple[int, int, int]
COLOR_HELD_PREF: Color = (119, 197, 228)
ImageSize: TypeAlias = float
DPI: ImageSize = 300.0


def main(output: str) -> None:
    prefs = get_prefs()
    pct = picture({pref: COLOR_HELD_PREF for pref in prefs})
    plt.imshow(pct)
    plt.savefig(output, dpi=DPI)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="pyconapac2023-postersession-japanmap",
        description="The map shows the provinces where the Python Boot Camp was held",
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Image Output Destination"
    )
    args = parser.parse_args()
    main(output=args.output)
