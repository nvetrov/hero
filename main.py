import collections
import os
import json
from pprint import pprint
from collections import Counter


def read_json(file_path, max_len_word=6, top_words=3):
    with open(file_path, encoding='utf-8') as new_file:
        news = json.load(new_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend(description)
            counter_words = collections.Counter(description_words)
        pprint(counter_words.most_common(top_words))


if __name__ == '__main__':
    read_json('newsafr.json')

# read_json(file)
