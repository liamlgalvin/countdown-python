import word_game as wg
import number_game as ng
import sys


print("Welcome to Countdown!!!")
while True:
    print("1. Word Game")
    print("2. Number Game")
    print("3. Exit")
    selection = input("pick 1, 2 or 3: ")
    if int(selection) in range(1,3):
        break
    elif int(selection) == 3:
        sys.exit()

if int(selection) == 1:
    wg.play_game()
if int(selection) == 2:   
    ng.play_game()
