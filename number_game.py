from random import shuffle, randrange, randint
import numpy
import time
import sys

# --------------- GENERATE LISTS OF NUMBERS - GLOBALS ----------------------
numbers = []
big = [25,50,75,100] 
little=[]
for i in [1,2]:
    for j in range(1,10):
        little.append(j)
# array to save all solutions
master=[]

# --------------- FUNCTIONS ----------------------
def add_big():
    global big
    shuffle(big)
    numbers.append(big[0])
    big.pop(0)

def add_little():
    global little
    shuffle(little)
    numbers.append(little[0])
    little.pop(0)

def add_random():
    options = randint(0,2)
    if options == 0:
        add_big()
    else:
        add_little()
    
def random_numbers():
    for i in range(0,6):
        add_random()

def goal():
    return randrange(100,1000)

def calculate(current, numbers, goal, sol):
        if current == goal:
            master.append(sol)
            return None
        else:
            for i,number in enumerate(numbers):
                list2 = numbers.copy()
                list2.pop(i) 
                plus(current, number, list2.copy(), goal, sol.copy())
                sub(current, number, list2.copy(), goal, sol.copy())
                div(current, number, list2.copy(), goal, sol.copy())
                mult(current, number, list2.copy(), goal, sol.copy())

def plus(num1,num2,numbers,goal,sol):
    current = num1 + num2
    sol.append(str(num1) + " + " + str(num2) + " = " + str(current))
    calculate(current, numbers, goal, sol)

def sub(num1,num2,numbers,goal,sol):
    current = num1 - num2
    sol.append(str(num1) + " - " + str(num2)+ " = " + str(current))
    calculate(current, numbers, goal, sol)

def mult(num1,num2,numbers,goal,sol):
    current = num1 * num2
    sol.append(str(num1) + " x " + str(num2)+ " = " + str(current))
    calculate(current, numbers, goal, sol)

def div(num1,num2,numbers,goal,sol):
    current = num1 / num2
    if (current % 2 == 0): 
        sol.append(str(num1) + " / " + str(num2)+ " = " + str(int(current)))
        calculate(int(current), numbers, goal, sol)
    else:
        return None

def calculate_aux(numbers, goal):
    for i, number in enumerate(numbers):
        list2 = numbers.copy()
        list2.pop(i)
        for j, number2 in enumerate(list2):
            list3 = list2.copy()
            list3.pop(j)
            sol = []
            plus(number, number2, list3.copy(), goal, sol.copy())
            sub(number, number2, list3.copy(), goal, sol.copy())
            div(number, number2, list3.copy(), goal, sol.copy())
            mult(number, number2, list3.copy(), goal, sol.copy())

   
#------------------- START GAME -----------------------

def number_game():
    global goal
    while True:
        print("1. Normal")
        print("2. Random")
        print("3. Solve")
        print("4. Exit")
        selection = input("pick 1, 2 or 3: ")
        try:
            if int(selection) in range(1,4):
                break
            elif int(selection) == 4:
                sys.exit()
            else:
                print("selection not in range")
        except ValueError:
            print("selection not a number")



    if int(selection) == 1:
        print("Choose your numbers:")
        for i in range (0,6):
            num = input("enter b (big) or l (little)")
            if num == "b":
                add_big()
            elif num == "l":
                add_little()
            else:
                add_random()
            print(numbers[-1])
    elif int(selection) == 2:
        random_numbers()
    elif int(selection) == 3:
        print("input your numbers 1 by one:")
        for i in range (0,6):
            num = input("enter number and press enter: ")
            numbers.append(int(num))

    if int(selection) == 3:
        goal = int(input("enter goal and press enter: "))
    else: 
        goal = goal()

    print()
    print(numbers)
    print()
    print(goal)
    print()

    input('When ready hit enter')

    # for sec in range(0,31):
    #     print("{0}".format(30-sec), end="\r")
    #     time.sleep(1)

    calculate_aux(numbers, goal)

    print("there are ", len(master), " solutions")
    master.sort()
    if len(master) > 0:
       return master[0]
    else:
        return "no solutions!"


def play_game():
    solution = number_game()
    print(solution)