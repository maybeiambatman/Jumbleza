#!/usr/bin/env python

from sets import Set

def check_word_jumble(word, dictionary):
    # Method that checks for all jumbled words and prints them out.
    word_sorted = ''.join(sorted(word))
    if word_sorted in dictionary:
        results = dictionary[word_sorted]
        for result in results:
            print result

def find_all_substrings(word):
    # This method finds all the substrings (with length greater than one) of the given string
    temp_list = []
    for i in range (0, len(word)):
        for j in range (i+1, len(word)+1):
            substring = word[i:j]
            if len(substring) > 1:
                temp_list.append(substring)

    # This returns the list of unique substrings in new_list
    return list(Set(temp_list))

def main():
    dictionary = {}
    file = open("/Users/mohdirteza/Jumbleza/words.txt", "r")

    print "Preparing ..."
    for word in file:
        word = word.strip().lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in dictionary:
            if word not in dictionary[sorted_word]:
                dictionary[sorted_word].append(word)
        else:
            dictionary[sorted_word] = [word]
    print "Preparation complete"

    play = True

    while(play):
        input_word = raw_input("Enter your word or hit 'q' to quit: ")
        input_word = input_word.lower()
        if(input_word == "q"):
            play = False
            break
        else:
            substrings = find_all_substrings(input_word)
            for substring in substrings:
                check_word_jumble(sorted(substring), dictionary)

if __name__ == '__main__':
    main()
