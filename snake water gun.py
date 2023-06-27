
import random

list=["Snake","Gun","Water"]
# comp=random.choice(list)
num=random.randint(0,2)
comp=list[num]

print('''Snake , Water , Gun''')
Per = input("Enter any word from the above :- ")

if Per=="Snake":
    if comp == "Water":
        print("You Won The Match")
    elif comp=="Gun":
        print("Computer Won The Match")
    else:
        print("Match Draw")
elif Per=="Water":
    if comp == "Snake":
        print("Computer Won the match")
    elif comp == "Gun":
        print("You won the match")
    else:
        print("Match Draw")
elif Per == "Gun":
    if comp == "Water":
        print("Computer won the match")
    elif comp=="Snake":
        print("You won the match")
    else:
        print("Match Draw")
else:
    print("Enter only those words which are display to you on the screen")

print(f"{comp} had selected by computer ")



