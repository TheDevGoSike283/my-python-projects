import os
import random
print("Welcome to the Python3 version of Wordle! To play, you have to type a word that contains only 5 letters and all caps. Letter backgrounds: \n\033[0;42mgreen = in right place, \n\033[0;43myellow = is in the word but not in the right place, \n\033[0;mand black means that the letter is not in the word. \nStarting in 5 seconds..")
os.system("sleep 5; clear")
words = ["HAPPY", "METAL", "QUEEN", "GAMES", "TRADE", "TRAPS", "TRAIN", "TRICK", "ALTER", "SHIFT", "SPACE", "SEVEN", "CARET", "MARKS", "CLOSE", "FRESH", "COLON", "KNEES", "MOUTH"]
word = random.choice(words)
splword = list(word)
k = 0
print("Type in a word: ")
os.system("sleep 1; clear")
for i in range(0, 5):
    print("Try " + str(i + 1) + ":")
    inp = input().upper()
    splinp = list(inp)
    if len(splinp) == 5:
        for j in splinp:
            if inp == word:
                print("\033[0;32mGood job! You guessed it!")
                quit()
            elif j == splword[k]:
                splinp[k] = "\033[0;42m" + splinp[k]
            elif j in word:
                splinp[k] = "\033[0;43m" + splinp[k]
            else:
                splinp[k] = "\033[0;m" + splinp[k]
            k = k + 1
        print(splinp[0] + splinp[1] + splinp[2] + splinp[3] + splinp[4] + "\033[0;m")
        k = 0
    else:
        print("\033[33;31mWord must contain 5 letters. \033[0;m") 
print("\033[33;31mAw man! The real word was " + word + "! Better luck next time!")
