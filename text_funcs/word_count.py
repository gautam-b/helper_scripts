"""
Count the frequency of each word in a string and return the sorted dict
"""

from typing import Mapping
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter


def word_count(sent: str, filter_stopwords: bool = False) -> Mapping[str, int]:
    words = word_tokenize(sent.lower())
    if filter_stopwords:
        stop_words = set(stopwords.words("english") + list(punctuation))
        words = [word for word in words if word not in stop_words]

    return Counter(words)


if __name__ == "__main__":
    sent = "The quick brown fox jumps over the lazy dog."
    print(word_count(sent))
    print(word_count(sent, filter_stopwords=True))
