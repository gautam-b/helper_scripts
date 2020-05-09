"""
Count the frequency of each word in a string and return the sorted dict
"""

from typing import Dict
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation


def word_count(sent: str, filter_stopwords: bool = False) -> Dict[str, int]:
    words = word_tokenize(sent.lower())
    if filter_stopwords:
        stop_words = set(stopwords.words("english") + list(punctuation))
        words = [word for word in words if word not in stop_words]

    word_count = dict()
    for word in words:
        if word not in word_count.keys():
            word_count[word] = 0

        word_count[word] += 1

    return {k: v for k, v in sorted(word_count.items(), key=lambda item: item[1], reverse=True)}


if __name__ == "__main__":
    sent = "The quick brown fox jumps over the lazy dog."
    print(word_count(sent))
    print(word_count(sent, filter_stopwords=True))
