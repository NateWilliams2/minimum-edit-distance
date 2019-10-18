import string
from collections import defaultdict
import re


def edit_distance(str1, str2, print_grid=False):
    w = len(str1) + 1
    h = len(str2) + 1
    my_table = [[0 for x in range(w)] for y in range(h)]

    for i in range(0, h):
        my_table[i][0] = i

    for j in range(0, w):
        my_table[0][j] = j

    for x in range(1, w):
        for y in range(1, h):
            if str1[x-1] == str2[y-1]:
                my_table[y][x] = my_table[y-1][x-1]
            else:
                my_table[y][x] = 1 + min(my_table[y][x-1],
                                         my_table[y-1][x], my_table[y-1][x-1])

    if print_grid:
        print_table(my_table, str1, str2)

    return my_table[y][x]


def print_table(arr, str1, str2):
    print("   epi ", end='')
    for i in str1:
        print(i + "  ", end='')
    print("")
    c = -1
    for j in arr:
        if c == -1:
            print("epi", end='')
        else:
            print(str2[c], end='')
        print(j)
        print("  ", end='')
        c += 1


def load_words():
    with open('./words_alpha.txt') as word_file:
        valid_words = word_file.read().split()
        word_dict = defaultdict(list)
        for w in valid_words:
            word_dict[len(w)].append(w)
    return word_dict


def correct_string(my_string):
    eng_dictionary = load_words()

    # split into list, punctuation strings are their own words
    words = re.findall(r"[a-zA-Z]+|[\W_0-9]+", my_string)

    for word in words:
        # test if word or punctuation, only include lower or title-case words (we do not want to correct
        # all-caps or other weirdly capitalized words)
        if re.match("^[a-zA-Z][a-z]*$", word):
            title_case = False
            min_dist_word = None
            min_dist = -999
            if word[0].isupper():
                title_case = True
            word = word.lower()
            # check list of words with same length as input word
            i = 0
            word_len = len(word)
            while i < min_dist or min_dist == -999:
                if word_len - i > 0:
                    for valid_word in eng_dictionary[word_len-i]:
                        dist = edit_distance(word, valid_word)
                        if dist == 0:
                            min_dist_word = word
                            min_dist = 0
                            break
                        elif min_dist == -999 or dist < min_dist:
                            min_dist = dist
                            min_dist_word = valid_word
                if word_len + i <= len(eng_dictionary) and i != 0:
                    for valid_word in eng_dictionary[word_len+i]:
                        dist = edit_distance(word, valid_word)
                        if dist == 0:
                            min_dist_word = word
                            min_dist = 0
                            break
                        elif min_dist == -999 or dist < min_dist:
                            min_dist = dist
                            min_dist_word = valid_word
                i += 1
            if title_case:
                ch = min_dist_word[0].upper()
                min_dist_word = ch + min_dist_word[1:]
            print(min_dist_word, end='')
        else:
            print(word, end='')
    print()


def run_program():
    user_input = input(
        "Enter 'a' for minimum edit distance, 'b' for string word correction\n")
    if user_input == "a":
        min_strings = input("enter two words separated by a space\n")
        min_strings_arr = min_strings.split()
        print("edit distance is: " +
              str(edit_distance(min_strings_arr[0], min_strings_arr[1], True)))
    if user_input == "b":
        user_string = input("enter a string to correct\n")
        correct_string(user_string)

run_program()
