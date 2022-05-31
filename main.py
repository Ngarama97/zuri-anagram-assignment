# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    #Change the inputs to lowercase & set them into lists
    First_word = sorted(list(word.lower()))
    Second_word = sorted(list(anagram.lower())) 

    # Loop through the words to compare them
    if First_word == Second_word:
        return True
    


