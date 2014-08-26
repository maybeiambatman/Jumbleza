#!/usr/bin/env python

def check_word_jumble(word, dictionary, result_list):
    # Method that checks for all jumbled words and prints them out.
    if word in dictionary:
        results = dictionary[word]
        for item in results:
            result_list.append(item)

def find_all_combinations(word):
    # This method finds all the combinations of the given string
    word_list = []
    for i in range(len(word)):
        new_word = ''.join(sorted(word[i]))
        if new_word not in word_list:
            word_list.append(new_word)
        for j in find_all_combinations(word[:i]+word[i+1:]):
            new_word = ''.join(sorted(word[i]+j))
            if new_word not in word_list:
                word_list.append(new_word)
    word_list.sort()
    return word_list

def build_dictionary():
    file = open("words.txt", "r")
    dictionary = {}

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
    return dictionary


def main():
    dictionary = build_dictionary()
    print dictionary['ader']

    play = True

    while(play):
        result_list = []

        input_word = raw_input("Enter your word or hit 'q' to quit: ")
        input_word = input_word.lower()
        if(input_word == "q"):
            play = False
            break
        else:
            combinations = find_all_combinations(input_word)
            for combination in combinations:
                check_word_jumble(combination, dictionary, result_list)

        for item in result_list:
            print item
        print ("Total words found: %s") % (len(result_list))

if __name__ == '__main__':
    main()
