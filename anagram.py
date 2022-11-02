from collections import defaultdict
from colorama import Fore as color
print(color.GREEN + "This is a program that sorts words in anagram collections. Type in the words to sort:")

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

words = []
i = 0
x = "nothing"
while x != "":
    print(color.YELLOW + "Word " + str(i + 1) + " to sort: ")
    x = input()
    words.append(x)
    i = i + 1
words.remove("")
print(color.BLUE + "Here is the sorted version of the words: \n" + str(group_anagrams(words)))
