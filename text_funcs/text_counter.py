"""
Count the frequency of each char / word in a string
"""

from typing import Mapping
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter


def char_count(text: str) -> Mapping[str, int]:
    '''Returns counter object
    '''
    text = text.lower()
    text = ''.join(text.split())  # remove all spaces
    text = text.translate(str.maketrans('', '', punctuation))  # remvoe punctuations
    return Counter(text.lower())


def word_count(text: str, filter_stopwords: bool = False) -> Mapping[str, int]:
    '''Returns counter object
    '''
    text = text.lower()
    text = text.translate(str.maketrans('', '', punctuation))  # remvoe punctuations
    words = word_tokenize(text)

    if filter_stopwords:
        stop_words = set(stopwords.words("english"))
        words = [word for word in words if word not in stop_words]

    return Counter(words)


if __name__ == "__main__":
    with open('pap.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    # with open('hamlet.txt', 'r', encoding='utf-8') as f:
    #     text = f.read()
    print(char_count(text))
    print()
    print(word_count(text))
    print()
    print(word_count(text, filter_stopwords=True))
