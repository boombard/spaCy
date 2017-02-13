from __future__ import unicode_literals, print_function
import codecs
import pathlib


class Stemmer(object):
    @classmethod
    def load(cls, path='/Users/ge2/software/spacy/corpora/da/stemwords.txt', rules=None):
        with open(path) as file_:
            cls.stem_map = read_stemwords(file_)

    def __call__(self, string, univ_pos, morphology=None):
        stem = stem_search(string, self.stem_map)
        return [stem]


def stem_search(string, stem_map):
    return stem_map.get(string, string)


def read_stemwords(fileobj):
    mapper = {}
    for line in fileobj:
        items = line.strip().split()
        if len(items) == 2:
            mapper[items[0]] = items[1]
    return mapper


if __name__ == "__main__":

    stemmer = Stemmer()
    stemmer.load()
    print(stemmer('ønskje', None, None))

