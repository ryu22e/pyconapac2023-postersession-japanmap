from pathlib import Path
from typing import Iterable, TypeAlias

import matplotlib.pyplot as plt
from japanmap import picture

Color: TypeAlias = tuple[int, int, int]
COLOR_HELD_PREF: Color = (119, 197, 228)
ImageSize: TypeAlias = float
DPI: ImageSize = 300.0


def save_image(prefs: Iterable, output: Path) -> Path:
    pct = picture({pref: COLOR_HELD_PREF for pref in prefs})
    plt.axis("off")
    plt.imshow(pct)
    plt.savefig(output, dpi=DPI, facecolor="azure", bbox_inches="tight", pad_inches=0)
    return output
