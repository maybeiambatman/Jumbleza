WORD JUMBLE SOLVER
==================

This is a script that accepts any group of letters as a string input and generates words for all possible combinations of those letters. Any combinatorics modules have been left out intentionally as a part of the design decisions. User can hit 'q' to quit the script at any moment.

Note: This is the official problem statement - 'The program should accept a string as input, and then return a list of words that can be created using the submitted letters. For example, on the input "dog", the program should return a set of words including "god", "do", and "go".'

Implementation
--------------

The program has two key functions:

- At first it builds an anagram dictionary for more efficient lookup.

- check_word_jumble: This function accepts a string as input and goes through the dictionary built by the program to yields all words key-ed to the sorted word.

For example: if input is 'dog'.

It yields, {key: dgo, value: [dog, god]}

-  find_all_combinations: This function outputs all possible combinations possible for the letters of the string it takes as input.

NOTE: I have decided to use the EOWL word list as my dictionary. To learn more click [here](http://dreamsteep.com/projects/the-english-open-word-list.html). Or, see words.txt for a copy of the full word list provided by EOWL.

Contact Info
------------

Author: Mohd Irteza

Email: irteza1@illinois.edu
