import re


def is_isogram(string):
    string = re.sub(r"[^a-z]", "", string.lower())
    return len(set(string)) == len(string)
