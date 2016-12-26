#!/usr/bin/env python

"""Represent a small bilingual lexicon as a Python dictionary
in the following fashion
{"merry":"god","christmas":"jul", "and":"och", "happy":gott", "new":"nytt",
"year":"år"} and use it to translate your Christmas
cards from English into Swedish. That is, write a function translate()
that takes a list of English words and returns a list of Swedish words."""

def translate(greeting):
    "this function translates the words in greeting to swedish"""
    word_dict = {"merry":"god",
                 "christmas":"jul",
                 "and":"och",
                 "happy":"gott",
                 "new":"nytt",
                 "year":"år"}
    for word in greeting:
        return [word_dict[word] for word in greeting]

if __name__ == '__main__':
    print(translate(["merry","christmas"]))
    
