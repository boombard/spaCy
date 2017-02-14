# encoding: utf8
from __future__ import unicode_literals

from ..symbols import *
from ..language_data import PRON_LEMMA

# Months of the year
# Source http://web.library.yale.edu/cataloging/months.htm
TOKENIZER_EXCEPTIONS = {
    "jan.": [
        {ORTH: "jan.", LEMMA: "Januar"}
    ],
    "febr.": [
        {ORTH: "febr.", LEMMA: "Februar"}
    ],
    "aug.": [
        {ORTH: "aug.", LEMMA: "August"}
    ],
    "sept.": [
        {ORTH: "sept.", LEMMA: "September"}
    ],
    "okt.": [
        {ORTH: "okt.", LEMMA: "Oktober"}
    ],
    "nov.": [
        {ORTH: "nov.", LEMMA: "November"}
    ],
    "dec.": [
        {ORTH: "dec.", LEMMA: "December"}
    ]
}


# Source: https://en.wiktionary.org/wiki/Category:Danish_abbreviations
TOKENIZER_EXCEPTIONS.update({
    "beg.": [
        {ORTH: 'beg.', LEMMA: 'begyndelse'}
    ],
    "bl.a.": [
        {ORTH: 'bl.', LEMMA: 'blandt'},
        {ORTH: 'a.', LEMMA: 'andet'}
    ],
    "ca.": [
        {ORTH: 'ca.', LEMMA: 'circa'}
    ],
    "d.s.s.": [
        {ORTH: 'd.', LEMMA: 'det'},
        {ORTH: 's.', LEMMA: 'samme'},
        {ORTH: 's.', LEMMA: 'som'}
    ],
    "f.eks.": [
        {ORTH: 'for.', LEMMA: 'for'},
        {ORTH: 'eks.', LEMMA: 'eksempel'}
    ]
})


# exceptions mapped to a single token containing only ORTH property
# example: {"string": [{ORTH: "string"}]}
# converted using strings_to_exc() util

# Source: https://en.wikipedia.org/wiki/Danish_orthography#Alphabet
ORTH_ONLY = [
    "a.",
    "b.",
    "c.",
    "d.",
    "e.",
    "f.",
    "g.",
    "h.",
    "i.",
    "j.",
    "k.",
    "l.",
    "m.",
    "n.",
    "o.",
    "p.",
    "q.",
    "r.",
    "s.",
    "t.",
    "u.",
    "v.",
    "w.",
    "x.",
    "y.",
    "z.",
    "æ.",
    "ø.",
    "å.",
]
