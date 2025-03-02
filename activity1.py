import random #import module
playing = True #inisialise
number = str(random.randint(1,10))
print("i wil generate a number from 1 to 10 and you have to guess the number one digit at a time")
#iterate loop until the condition is true
while playing:
    guess = input("give me your best guess:  " )
    if number == guess:
        print("you win the game")
        print("the number was",  number)
        break
    else:
        print("your guess is not quite right")