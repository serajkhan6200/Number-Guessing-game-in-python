import random
num = random.randint(1,100)
tries = 0
while True:
    guess = int(input("Please Guess Your Number Between 1 to 100 :- "))
    if num == guess:
        tries+=1
        print(f"You are Right ✅, You Guessed The Number in {tries} tries")
        break
    elif num < guess:
        print("Go a Little Lower ↓")
        tries+=1
    elif num > guess:
        print("Go a Little Higher ⬆")
        tries+=1
    else:
        tries+=1
        print("Sorry You are Wrong X")