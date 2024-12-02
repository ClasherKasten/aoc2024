from __future__ import annotations

import argparse
import os.path
from itertools import pairwise

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    safe = 0
    for line in lines:
        levels = support.parse_numbers_split(line)
        found = False
        for idx, _ in enumerate(levels):
            cleaned_levels = levels.copy()
            _ = cleaned_levels.pop(idx)
            zipped_levels = pairwise(cleaned_levels)
            direction = cleaned_levels[0] - cleaned_levels[1]
            for previous_level, current_level in zipped_levels:
                diff = previous_level - current_level
                if (direction * diff) < 0 or not (1 <= abs(diff) <= 3):
                    break
            else:
                found = True
                break
        if found:
            safe += 1

    return safe


INPUT_S = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 4


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
