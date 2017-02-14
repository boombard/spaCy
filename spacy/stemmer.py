from __future__ import unicode_literals, print_function
import codecs
import pathlib


class Stemmer(object):
    @classmethod
    def load(cls, path=None, rules=None):
        with path.open() as file_:
            stem_map = read_stemwords(file_)

        if rules is None:
            rules = {}

        return cls(stem_map, rules)

    def __init__(self, stem_map, rules):
        self.stem_map = stem_map
        self.rules = rules

    def __call__(self, string, univ_pos=None, morphology=None):
        stem = stem_search(string, self.stem_map)
        return stem


def stem_search(string, stem_map):
    string = string.lower()
    stem = stem_map.get(string, string)

    return set([stem])


def read_stemwords(fileobj):
    mapper = {}
    for line in fileobj:
        items = line.strip().split()
        if len(items) == 2:
            mapper[items[0]] = items[1]
    return mapper
