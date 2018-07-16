print("Welcome")
a = input("Guess:")
guess = int(a)
while guess != 5:
    if guess > 5:
        print("Too big")
    else:
        print("Too small")
    a = input("Guess again:")
    guess = int(a)
print("Correct")
print("Game over")