WORD JUMBLE SOLVER
==================

This is a script that accepts any combination of letters as input and generates words for all possible permutations of those letters. Any combinatorics modules have been left out intentionally as a part of the design decisions. User can hit 'q' to quit the script at any moment.

Implementation
--------------

The program has two key functions:

1. check_word_jumble: This function accepts a string as input and goes through the dictionary built by the program to yields all words key-ed to the sorted word.

For example: if input is 'dog'.

It yields key: dgo, value: [dog, god]

2. find_all_permutations: This function outputs all possible permutations possible for the combination of letters it takes as input.

Contact Info
------------

Author: Mohd Irteza
Email: irteza1@illinois.edu