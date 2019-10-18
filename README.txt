Homework 4
Nate Williams and Govind Brahmanyapura
10/17


﻿1. Problem Description
This problem has two parts. First is the minimum edit-distance algorithm and second is the spelling correction program. The minimum edit-distance algorithm must take two strings of any length as input and return the minimum number of operations required to produce one string from the other. These operations include insertion of a character, deletion of a character, or substitution of a character. In many variants of this problem substitution should be counted as two operations (one deletion followed by one deletion) but in this case, substitution of one letter for another counts as one operation. The algorithm must also print the table which it populates using dynamic programming to produce the result. This table begins with one column and one row representing a blank character, and then one table or row for each character in each of the strings. Each entry in the table should represent the minimum number of operations required to convert one string to the other only including the characters at that index and lower.


The spelling correction program should use the minimum edit-distance algorithm to correct any misspelled words in a given string to some word in the english dictionary which has the smallest edit distance compared to the original misspelled word. If many words share the same minimum edit-distance, any of them can be chosen. The program should use https://github.com/dwyl/english-words as its english dictionary, and should not alter punctuation or correctly spelled words. The program’s behavior with regard to capitalized letters is unspecified, so we set the specification that title-case words (ones where only the first letter is capitalized) should be corrected if misspelled but should retain their title-case property. Any words capitalized beyond title-case should be treated, like capitalized words in most commercial autocorrect programs, as non-correctable.


2. Analysis and Description of the major functions/classes
Our program includes the following functions:
        edit_distance(str1, str2, print_grid)
This function takes two strings and a boolean as input and returns the minimum edit distance between those two strings. If the boolean print_grid is set to true, the function also prints the table used to construct the edit distance between the two words. The function allocates a table with O(n*m) entries, where n is the length of str1 and m is the length of str2, and it performs a constant-time operation on each of these entries. So the function is O(n*m).


        print_table(arr, str1, str2)
This function takes an array (which represents a 2d table of characters) and two strings and prints the table with the strings’ characters as headers for the x and y axes of the tables. It performs one constant-time print operation on each entry in the table, which is size O(n*m) where where n is the length of str1 and m is the length of str2. Therefore this function is running time O(n*m).


        load_words()
This function opens the file of words in the english dictionary and returns them as a dictionary which has one list entry for each word-length (eg. one entry in the dictionary is a list containing all 3-letter words). The algorithm first splits the file into an array of words, which performs a constant-time array value assignment operation on each word and therefore takes O(n) time where n is the number of words. It then creates the dictionary and populates it, which performs one dictionary access and one list append operation on each word, so is also O(n). The function is therefore running-time O(n).


        correct_string(my_string)
This function takes a string as input and prints a new string in which every previously misspelled word is corrected to a word in the english dictionary with minimum edit-distance from the original misspelled word. The function first performs an O(n) operation, where n is the number of words in the string, to split it up into an array of words. (here strings of punctuation and numbers are counted as their own words). The function then compares this word to each word in the dictionary with the same length as that word. If it finds an identical word, it prints the word and moves on to the next word in the array. If it finds no word with an edit distance less than 2 away from the original word, it then compares the original word to words of length one greater or one less than the original. It repeats this pattern until either all words in the dictionary are compared to the original word or an edit distance sufficiently small is found so that increasing or decreasing the size of dictionary words cannot find a better result. In the worst case, this loop compares each original word to each of d words in the dictionary. Even in the best case, however, each original word will be compared to some fraction of d words in the dictionary. So there will be O(d) comparisons per original word, or O(n*d) comparisons done on the original string of n words. Furthermore, each comparison calls the edit_distance function, which we have identified as being O(x*y) where x and y are the lengths of the strings being compared. So the total running time for this function is O(n*d*x*y) where x is the average length of words in the original string and y is the average length of words in the dictionary that word is being compared to.


        run_program()
This function calls either the edit_distance or correct_string function, depending on user input. It therefore takes O(x*y) time where x and y are the lengths of user-input strings, or O(n*d*x*y) where n is the number of words in a user-input string, d is the number of words in the english dictionary, and x and y are the average lengths of words in those sets, respectively.


3. Instruction to execute your code
Set up an environment which can run python code, and then simply run the file homework4.py, ensuring it is in a folder along with words_alpha.txt. The command line will prompt you to input either ‘a’ for edit-distance or ‘b’ for spelling correction.


4. Some sample input and corresponding output


MacBook-Air:homework4 natewilliams$ python3 homework4.py
Enter 'a' for minimum edit distance, 'b' for string word correction
a
enter two words separated by a space
beef modality
   epi b  e  e  f
epi[0, 1, 2, 3, 4]
  m[1, 1, 2, 3, 4]
  o[2, 2, 2, 3, 4]
  d[3, 3, 3, 3, 4]
  a[4, 4, 4, 4, 4]
  l[5, 5, 5, 5, 5]
  i[6, 6, 6, 6, 6]
  t[7, 7, 7, 7, 7]
  y[8, 8, 8, 8, 8]
  edit distance is: 8
MacBook-Air:homework4 natewilliams$ python3 homework4.py
Enter 'a' for minimum edit distance, 'b' for string word correction
a
enter two words separated by a space
hi bi
   epi h  i
epi[0, 1, 2]
  b[1, 1, 2]
  i[2, 2, 1]
  edit distance is: 1
MacBook-Air:homework4 natewilliams$ python3 homework4.py
Enter 'a' for minimum edit distance, 'b' for string word correction
a
enter two words separated by a space
hello yellow
   epi h  e  l  l  o
epi[0, 1, 2, 3, 4, 5]
  y[1, 1, 2, 3, 4, 5]
  e[2, 2, 1, 2, 3, 4]
  l[3, 3, 2, 1, 2, 3]
  l[4, 4, 3, 2, 1, 2]
  o[5, 5, 4, 3, 2, 1]
  w[6, 6, 5, 4, 3, 2]
  edit distance is: 2
MacBook-Air:homework4 natewilliams$ python3 homework4.py
Enter 'a' for minimum edit distance, 'b' for string word correction
b
enter a string to correct
Henlo, my old freind!
Hello, my old freend!
MacBook-Air:homework4 natewilliams$ python3 homework4.py
Enter 'a' for minimum edit distance, 'b' for string word correction
b
enter a string to correct
Whattadkle is your nmae?
Chattable is your mae?
MacBook-Air:homework4 natewilliams$ python3 homework4.py
Enter 'a' for minimum edit distance, 'b' for string word correction
b
enter a string to correct
aaa bcd fgtifhdk
aaa bcd fecifork


5. Discussion of your experience on this assignment
In reflection, we both feel that we worked really efficiently on this assignment. We sat down and sketched out possible pseudocode for each problem before digging in and both had a clear conceptual understanding of the task at hand. This helped us to write code efficiently and effectively. The harder part for us was considering edge cases like punctuation and capitalization, as well as optimizing by searching for similar word-lengths first while ensuring the mathematically correct solution would still be found.
The edit-distance problem is a really interesting one which helped us to understand dynamic programming. The spelling correction program was more difficult, but largely due to its messiness as a problem rather than its intrinsic difficulty.
