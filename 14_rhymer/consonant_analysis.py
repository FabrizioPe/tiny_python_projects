#!/usr/bin/env python3
"""
Author: FabrizioPe
Date: 2021-02-17
Purpose: A program that can analyse a set of words (a 'dictionary') and
    extract all the consonant sounds.
"""

import re
import string


# ------------------------------------------
def dictionary_consonants(diction: set):
    """Find all the consonants in a set of words.
       Return a set with all the consonant sounds."""
    
    consonant_clusters = {cluster for word in diction
                          for cluster in consonant_sounds(word)}

    return consonant_clusters


# ------------------------------------------
def test_dictionary_consonants():
    assert dictionary_consonants({'Actress', 'attinium', 'sine', 'actor',
                                  'abattoir'}) == {'ctr', 's', 't', 'n', 'm',
                                                   'r', 'b', 'ct'}


# ------------------------------------------
def consonant_sounds(word: str):
    """Return a set with all the consonant sounds in word.
       Ex: chatting -> {'ch', 't', 'ng'}. Note that 'tt' becomes 't'."""

    consonants = ''.join([c for c in string.ascii_lowercase if c not in 'aeiou'])
    pattern = f'[aeiou]*([{consonants}]+)'
    match = set(re.findall(pattern, word.lower()))
    for cluster in match.copy():  # substitute 'tt' with 't'
        if len(cluster) > 1 and len(set(cluster)) == 1:
            match.update(cluster[0])
            match.remove(cluster)
    return match


# ------------------------------------------
def test_consonant_sounds():
    assert consonant_sounds('aardvark') == {'rdv', 'rk'}
    assert consonant_sounds('Ababdehobd') == {'b', 'bd', 'h'}
    assert consonant_sounds('attenzionett') == {'t', 'nz', 'n'}
    assert consonant_sounds('Chairiottich') == {'ch', 'r', 't'}
    assert consonant_sounds('bbbbbbbabb') == {'b'}
    
    
# ------------------------------------------
if __name__ == '__main__':
    with open('../inputs/words.txt') as fh:
        dictionary = set(fh.read().split('\n'))
        consonants = sorted(list(dictionary_consonants(dictionary)))
        # just print a preview
        print(f'There are {len(consonants)} consonant sounds in the given'
              f' dictionary with {len(dictionary)} words.')
        for i in range(30):
            print(consonants[i])
