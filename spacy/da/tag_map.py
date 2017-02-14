# encoding: utf8
from __future__ import unicode_literals

from ..symbols import *

# Imported from https://github.com/slavpetrov/universal-pos-tags

TAG_MAP = {
    "AC": {POS: NUM},
    "AN": {POS: ADJ},
    "AO": {POS: NUM},
    "CC": {POS: CONJ},
    "CS": {POS: CONJ},
    "I":  {POS: X},
    "NC": {POS: NOUN},
    "NP": {POS: NOUN},
    "PC": {POS: PRON},
    "PD": {POS: PRON},
    "PI": {POS: PRON},
    "PO": {POS: PRON},
    "PP": {POS: PRON},
    "PT": {POS: PRON},
    "RG": {POS: ADV},
    "SP": {POS: ADP},
    "VA": {POS: VERB},
    "VE": {POS: VERB},
    "XA": {POS: X},
    "XF": {POS: X},
    "XR": {POS: X},
    "XX": {POS: X}
}
