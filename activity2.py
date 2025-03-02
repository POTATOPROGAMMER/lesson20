import random
options = ('rock', 'paper' , 'scissor')
user_choice = input("choose rock, paper, or scissors : ")
computer_choice= random.choice(options)
print("you chose :  " ,  user_choice)
print("computer chose:  " ,  computer_choice)
if computer_choice==user_choice:
    print("it is a tie")
elif user_choice == "rock" and computer_choice=="scissors":
    print("rock smashes paper ! you win")
elif user_choice == "paper" and computer_choice=="rock":
    print("paper beats rock  ! you win")
elif user_choice == "scissors" and computer_choice=="paper":
    print("scissors cuts paper ! you win")
else:
    print("you lose")

