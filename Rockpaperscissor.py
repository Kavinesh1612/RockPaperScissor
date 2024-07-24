import random
def determine_winner(user,computer):
    if user== computer:
        return "It is a tie"

    elif user == 'R':
        if computer == 'P':
            return "Computer wins!"
        else:
            return "You win!"

    elif user == 'P':
        if computer == 'S':
            return "Computer wins!"
        else:
            return "You win!"

    elif user == 'S':
        if computer == 'R':
            return "Computer wins!"
        else:
            return "You win!"

    else:
        return "Invalid enter 'Rock = R', 'Paper = P', or 'Scissors = S'."

def play():
    print("Welcome to Rock, Paper, Scissors")
    print("R = Rock \nP = Papper \nS = Scissors")
    print("Enter your choice: R, P, or S")

    choices = ['R', 'P', 'S']
    user = input("Your choice: ")
    computer = random.choice(choices)
    print("\nResult:")
    print("You chose:",user)
    print("Computer chose:",computer)

    result = determine_winner(user, computer)
    print(result)
play()
