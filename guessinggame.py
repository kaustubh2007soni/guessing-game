import random
print("number guessingGame")
number=random.randint(1,9)
chances=0
print("guess the numbers between 1 and 9")
while chances<5:
    guess=int(input("enteryourguess"))
    if guess ==number:
        print("congrtulations you won!!!!!")
        break
    elif guess<number:
        print("your guess was low:guess number higher than",guess)
    else:
        print("guess this to high guess lower number",guess)

    chances+=1
if not chances<5:
    print("congrtulations you lose!!the number is",number)