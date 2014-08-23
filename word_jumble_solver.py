#!/usr/bin/env python

def check_word_jumble(word, dictionary, result_list):
    # Method that checks for all jumbled words and prints them out.
    word = ''.join(sorted(word))
    if word in dictionary:
        results = dictionary[word]
        for result in results:
            if result not in result_list:
                result_list.append(result)

def find_all_permuatations(word):
    # This method finds all the permutations of the given string
    for i in range(len(word)):
        yield (word[i])
        for j in find_all_permuatations(word[:i]+word[i+1:]):
            yield(word[i]+j)

def main():
    dictionary = {}
    file = open("words.txt", "r")

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
        result_list = []

        input_word = raw_input("Enter your word or hit 'q' to quit: ")
        input_word = input_word.lower()
        if(input_word == "q"):
            play = False
            break
        else:
            permutations = list(find_all_permuatations(input_word))
            for permutation in permutations:
                check_word_jumble(permutation, dictionary, result_list)

        for item in result_list:
            print item
        print ("Total words found: %s") % (len(result_list))

if __name__ == '__main__':
    main()
