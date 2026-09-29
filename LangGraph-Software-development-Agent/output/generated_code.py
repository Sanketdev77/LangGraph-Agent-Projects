```python
#!/usr/bin/env python3
"""
Utility module for working with even numbers.

Provides:
- `is_even(value)`: Return ``True`` if *value* is an even integer.
- `filter_even(iterable)`: Return a list of even integers from *iterable*.
- Simple CLI to check numbers supplied as command‑line arguments or via STDIN.
"""

from __future__ import annotations

import sys
from typing import Iterable, List, Sequence


def is_even(value: int) -> bool:
    """
    Determine whether *value* is an even integer.

    Parameters
    ----------
    value: int
        The integer to test.

    Returns
    -------
    bool
        ``True`` if *value* is even, ``False`` otherwise.

    Raises
    ------
    TypeError
        If *value* is not an ``int`` (bool is a subclass of int and is allowed;
        ``True`` is considered odd, ``False`` even).
    """
    if not isinstance(value, int):
        raise TypeError(f"Expected int, got {type(value).__name__}")
    # ``bool`` is a subclass of ``int`` – treat it according to its numeric value.
    return value % 2 == 0


def filter_even(iterable: Iterable[int]) -> List[int]:
    """
    Return a list containing only the even integers from *iterable*.

    Parameters
    ----------
    iterable: Iterable[int]
        An iterable yielding integers.

    Returns
    -------
    List[int]
        All even numbers found in the input, preserving order.

    Raises
    ------
    TypeError
        If any element of *iterable* is not an ``int``.
    """
    evens: List[int] = []
    for idx, item in enumerate(iterable):
        if not isinstance(item, int):
            raise TypeError(
                f"Element at position {idx} is not an int (got {type(item).__name__})"
            )
        if is_even(item):
            evens.append(item)
    return evens


def _parse_numbers(args: Sequence[str]) -> List[int]:
    """
    Convert a sequence of strings to integers, handling conversion errors.

    Parameters
    ----------
    args: Sequence[str]

    Returns
    -------
    List[int]

    Raises
    ------
    ValueError
        If any string cannot be parsed as an integer.
    """
    numbers: List[int] = []
    for s in args:
        s = s.strip()
        if not s:
            continue
        try:
            numbers.append(int(s))
        except ValueError as exc:
            raise ValueError(f"Unable to parse '{s}' as an integer") from exc
    return numbers


def _cli() -> None:
    """
    Command‑line interface.

    Usage examples:
        $ python even_utils.py 2 3 4
        2 is even
        3 is odd
        4 is even

        $ echo "5\n6\nseven" | python even_utils.py
        5 is odd
        6 is even
        Error: Unable to parse 'seven' as an integer
    """
    if len(sys.argv) > 1:
        # Numbers supplied as command‑line arguments.
        raw_inputs = sys.argv[1:]
    else:
        # Read from STDIN, one number per line.
        raw_inputs = [line for line in sys.stdin]

    try:
        numbers = _parse_numbers(raw_inputs)
    except ValueError as err:
        sys.stderr.write(f"Error: {err}\n")
        sys.exit(1)

    for n in numbers:
        parity = "even" if is_even(n) else "odd"
        print(f"{n} is {parity}")


if __name__ == "__main__":
    _cli()
```