#!/usr/bin/env python3
"""Pigeon Pitch, One Line -- make.fun bounty u-donrulezz-pigeon-pitch-one-line-af06c6cf.

Writes a single-line elevator pitch, spoken by a city pigeon to investors
for its startup, to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt).

Standard library only. Deterministic: the output is a fixed string.
"""

import os
import sys

PITCH = (
    "We\u2019re raising a seed round \u2014 literally, we eat the seed \u2014 "
    "to franchise the city\u2019s only zero-payroll delivery network: "
    "ten thousand couriers, every rooftop a warehouse, paid in crumbs."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
