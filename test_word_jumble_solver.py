#!/usr/bin/env python

from word_jumble_solver import *

def test_find_all_combinations_dog():
    assert find_all_combinations('dog') == ['d', 'dg', 'dgo', 'do', 'g', 'go', 'o']

def test_find_all_combinations_food():
    assert find_all_combinations('food') == ['d', 'df', 'dfo', 'dfoo', 'do', 'doo', 'f', 'fo', 'foo', 'o', 'oo']

def test_build_dictionary():
    dictionary = build_dictionary()
    assert dictionary['dgo'] == ['dog', 'god']
    assert dictionary['ader'] == ['ared', 'dare', 'dear', 'read']

if __name__ == '__main__':
    test_find_all_combinations_dog()
    test_find_all_combinations_food()
    test_build_dictionary()