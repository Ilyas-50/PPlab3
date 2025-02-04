import random

success = False
print("Hello! What is your name?")
name = input()
print("Well,",name ,", I am thinking of a number between 1 and 20.")
print("Take a guess.")
rand_num = random.randint(0,20)
counter = 0
while(not success):
    inp = int(input())
    if inp < rand_num:
        print("Your guess is too low.")
        print("Take a guess.")
        counter +=1
    elif inp > rand_num:
        print("Your guess is too high.")
        print("Take a guess.")
        counter +=1
    elif(inp == rand_num):
        print(f"Good job, {name}! You guessed my number in {counter} guesses!")

