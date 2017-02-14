# coding: utf-8
"""Test that longer and mixed texts are tokenized correctly."""


from __future__ import unicode_literals

import pytest


def test_tokenizer_handles_long_text(da_tokenizer):
    text = """
        Malaysia er en forholdsvis ung stat. Sin endelige udstrækning fik den
        først i 1965 efter, at Singapore trak sig ud. Staten blev grundlagt ved
        en sammenslutning af flere tidligere britiske besiddelser, foreløbigt i
        1957 og endeligt i 1963. Formelt er Malaysia et monarki sammensat af 13
        delstater, der er baserede på historiske, malaysiske kongedømmer.
        Kongemagten indehaves af de ledende fyrstefamilier efter et
        rotationsprincip. Befolkningen er meget sammensat og består af både
        hjemmehørende folkeslag og indvandrere, især fra Kina og Indien.
        Kulturen præges af befolkningens etniske og religiøse sammensætning.
    """

    tokens = da_tokenizer(text)
    assert len(tokens) == 110


def test_tokenizer_handles_exception_cases(da_tokenizer):
    text = """
        beg. Malaysia er en forholdsvis ung stat ca. jan. Kulturen
        præges af befolkningens etniske og religiøse sammensætning
        """
    tokens = da_tokenizer(text)
    result = [token.text for token in tokens if not token.is_space]
    assert result == text.split()


def test_stemmer(da_tokenizer, da_lemmatizer):
    text = """
        aabakken
        aabakkens
        aarbakke
        aarum
        aase
    """
    expected_stems = ["aabakk", "aabakk", "aarbakk", "aarum", "aas"]
    tokens = da_tokenizer(text)
    stemmed_tokens = [next(iter(da_lemmatizer(token.text))) for token in tokens
                      if not token.is_space]
    assert expected_stems == stemmed_tokens
