
from random import randrange


userChoice= str.lower(input(" Enter R , P, or S:   "))




choices = ["Rock","Paper", "Sciscors"]

computerChoice=choices[randrange(0,3)]

print("The computer chose", computerChoice)

if userChoice == "r":
    if computerChoice == "Sciscors":
        outcome = "You Win"
    elif computerChoice == "Paper":
        outcome = "You Lose"
    elif computerChoice == "Rock":
        outcome = "Tie"
elif userChoice == "p":
    if computerChoice == "Sciscors":
        outcome = "You Lose"
    elif computerChoice == "Paper":
        outcome = "Tie"
    elif computerChoice == "Rock":
        outcome = "You Win"
elif userChoice == "s":
    if computerChoice == "Sciscors":
        outcome = "Tie"
    elif computerChoice == "Paper":
        outcome = "You Win"
    elif computerChoice == "Rock":
        outcome = "You Lose"

print(outcome)
