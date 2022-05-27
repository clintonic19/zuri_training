# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()

    if (sorted(word) == sorted(anagram)):
        return True
    elif (sorted(anagram) != sorted(word)):
        return False
    else:
        print("All the characters are anagram")


print(find_anagram("MASTER", "learn"))
print(find_anagram("MASTER", "master"))
