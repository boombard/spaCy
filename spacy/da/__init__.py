# encoding: utf8
from __future__ import unicode_literals, print_function

from os import path
from pathlib import Path

from ..language import Language
from ..attrs import LANG
from ..stemmer import Stemmer



# Import language-specific data
from .language_data import *


# create Language subclass
class Danish(Language):
    lang = 'da' # ISO code

    class Defaults(Language.Defaults):
        lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
        lex_attr_getters[LANG] = lambda text: 'da'

        # override defaults
        tokenizer_exceptions = TOKENIZER_EXCEPTIONS
        tag_map = TAG_MAP
        stop_words = STOP_WORDS

        @classmethod
        def create_lemmatizer(cls, nlp=None):
            stemword_path = Path(path.dirname(path.realpath(__file__)))
            stemword_path = stemword_path / '..' / '..' / 'corpora' / 'da' \
                            / 'stemwords.txt'

            return Stemmer.load(path=stemword_path)
