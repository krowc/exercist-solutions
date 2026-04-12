"""A pangram is a sentence that contains at least one of every letter in the
English alphabet. Here's a function that checks that."""

def is_pangram(sentence):
    """Checks if a sentence is a pangram.

    :param sentence: str - sentence to check.
    :return: bool - is the sentence a pangram.
    """
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    potential_pangram = []
    for char in sentence.lower():
        if char.isalpha():
            potential_pangram.append(char)

    potential_pangram = set(potential_pangram)
    
    return potential_pangram == alphabet