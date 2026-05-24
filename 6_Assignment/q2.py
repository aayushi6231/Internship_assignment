import random

items = ["snake", "water", "gun"]
comp = random.choice(items)
user = input("Enter from snake,water,gun: ").lower()

print("Computer chose:", comp)

if user == comp:
    print("Match Draw")
elif (
    (user == "snake" and comp == "water") or
    (user == "water" and comp == "gun") or
    (user == "gun" and comp == "snake")
):
    print("user Win")
else:
    print("Computer Wins")