import random

def getdata():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid. Try Again!!")

def condition(choice, choice1):
    towin = {
        'rock': {'scissors': 'you win!', 'paper': 'computer wins!', 'rock': 'it\'s a tie!!'},
        'paper': {'scissors': 'computer wins', 'paper': 'it\'s a tie!', 'rock': 'you win'},
        'scissors': {'scissors': 'it\'s a tie!', 'paper': 'computer wins!', 'rock': 'you win!!'}
    }
    return towin[choice][choice1]

def display(choice, choice1):
    print(f"You chose: {choice}")
    print(f"Computer chose: {choice1}")

def game():
    print("Welcome to rock, paper, scissors game!!\n")
    while True:
        choice = getdata()
        choice1 = random.choice(['rock', 'paper', 'scissors'])
        display(choice, choice1)
        res = condition(choice, choice1)
        print(res)
        oncemore = input("Do you want to play again? (yes/no)").lower()
        if oncemore != 'yes':
            print("\nThank you!")
            break

game()
