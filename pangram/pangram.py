letters = "abcdefghijklmnopqrstuvwxyz"


def is_pangram(sentence):
    for i in letters:
        if i not in sentence.lower():
            return False
        
    return True
