"""
Count the frequency of each charecter in a string and return the sorted dict
"""
from typing import Mapping
from collections import Counter


def char_count(text: str) -> Mapping[str, int]:
    return Counter(text)


if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog."
    print(char_count(text))
