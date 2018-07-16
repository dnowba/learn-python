from random import randrange
b=randrange(1,10,2)
print("Welcome")
a = input("Guess:")
guess = int(a)
while guess != b:
    if guess > b:
        print("Too big")
    else:
        print("Too small")
    a = input("Guess again:")
    guess = int(a)
print("Correct")
print("Game over")