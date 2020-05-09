"""
Count the frequency of each charecter in a string and return the sorted dict
"""
from typing import Dict


def char_count(text: str) -> Dict[str, int]:
    chars = dict()
    for c in text.lower():
        if c not in chars.keys():
            chars[c] = 0

        chars[c] += 1

    # sorting and returning
    return {k: v for k, v in sorted(chars.items(), key=lambda item: item[1], reverse=True)}


if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog."
    print(char_count(text))
