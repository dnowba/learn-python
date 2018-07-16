print("Welcome")
g = input("數字:")
guess = int(g)
if guess == 6:
    print("You win")
else :
    if guess < 6:
     print("Bigger")
    if guess > 6:
     print("Smaller")
print("Game over")