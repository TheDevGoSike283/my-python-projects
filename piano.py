import os
print("Welcome to Python Piano but it's input-based! The keys are C, D, E, F, G, A, B, HC, which means higher C, and each space represents a wait period of 0.25 seconds. It is case-sensitive. Happy playing!")
play = input()
for i in [*play]:
    if i != " ":
        os.system("mpg123 -q " + i + ".mp3")
    os.system("sleep 0.25")

