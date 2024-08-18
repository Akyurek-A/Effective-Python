import math
import random

minbound = int(input("Enter the lower bound number: "))
maxbound = int(input("Enter the upper bound number: "))

x = random.randint(minbound, maxbound)
total_chances = math.ceil(math.log(maxbound-minbound + 1, 2))
print("You only have ", total_chances, " chances to guess the number")

count = 0
flag = False

while count < total_chances:
    count += 1

    guess = int(input("Guess a number: "))
    if x == guess:
        print("Well done! You found the number in ", count, " try")
        flag = True
        break
    elif x > guess:
        print("Your number is so small!")
    elif x < guess:
        print("Your number is so high!")

if not flag:
    print("\nThe number was %d" % x)
    print("Nice try.")