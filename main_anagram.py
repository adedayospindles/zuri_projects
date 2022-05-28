# Check if two words are anagrams 
# Example:
# find_anagram("hello", "check") --> False
# find_anagram("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    # check if length is same
    if(len(word) == len(anagram)):
        # sort the strings
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)
        
        # if sorted char arrays are same
        if(sorted_word == sorted_anagram):
            print(word + " and " + anagram + " are anagram.")
            return True
        else:
            print(word + " and " + anagram + " are not anagram.")
            return False
    else:
        print(word + " and " + anagram + " are not anagram.")
        return False
        
# find_anagram("below", "elbow")