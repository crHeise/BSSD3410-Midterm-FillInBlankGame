# Programmer: Chris Heise (crheise@icloud.com)
# School: New Mexico Highlands University
# Course: BSSD 3410 Applied Algorithms & Architecture
# Instructor: Jonathan Lee
# Date: 9 March 2023
#
# Program: Midterm Project
# Purpose: Use Text Analysis and Dynamic Programming to create a fill-in-the-blank game.
# File: text_functions.py

# split_into_sentences function from
# URL: https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences
# Author: D Greenberg
# License: None listed

import re
import random

alphabets = "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|edu|me)"
digits = "([0-9])"


def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n", " ")

    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)

    text = re.sub(digits + "[.]" + digits, "\\1<prd>\\2", text)
    if "..." in text: text = text.replace("...", "<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.", "Ph<prd>D<prd>")

    text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
    text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
    text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)

    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")

    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]

    return sentences


def process_text(fname, enc):
    """
    Function for getting sentences from a text file.
    :param fname: the name of the text file to process.
    :param enc: the encoding of the text file.
    :return: a list of sentences from the text file.
    """
    with open(fname, 'r', encoding=enc) as file:
        data = file.read()
    return split_into_sentences(data)


def get_random_sentence(text_sentences, min_length=5):
    """
    Function for selecting a random sentence from a list of sentences.
    :param text_sentences: a list of sentences.
    :param min_length: the minimum number of words desired in random sentence.
    :return: a single sentence as a string.
    """
    sentence = []
    while len(sentence) < min_length:
        index = random.randint(0, len(text_sentences))
        sentence = text_sentences[index-1].split()
    return ' '.join(sentence)


def get_random_word(sentence, min_length=4):
    """
    Function for selecting a random word from a sentence.
    :param sentence: the sentence to select a word from.
    :param min_length: the minimum number of characters desired in the random word.
    :return: a single word as a string.
    """
    words = sentence.split()
    word = ""
    while len(word) < min_length:
        index = random.randint(0, len(words))
        word = words[index-1]
    return word
