# Number Guessing Game:
secret = 7

while True:
    guess = int(input("Guess number: "))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Try Again")