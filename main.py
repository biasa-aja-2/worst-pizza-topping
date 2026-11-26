#!/usr/bin/env python3
"""The Worst Pizza Topping.

Writes one original funny line (<=200 chars, single line, no trailing
newline) pitching a terrible pizza topping to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib only. The pitch sells the topping by naming it plainly,
then the free tetanus shot lands the joke on the last words.
"""

import os

JOKE = "Try our laundry-day pizza: soggy socks, dryer lint, and one lost earring on a crust of pure regret, with a free tetanus shot on the side."


def main():
    # Gate: /output/entry.txt must hold UTF-8 text of 1 to 200 chars.
    if not (1 <= len(JOKE) <= 200) or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke violates the competition gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
