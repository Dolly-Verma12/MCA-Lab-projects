secret_number = 25
attempts = 0

print("Welcome to the Number Guessing Game!")

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < secret_number:
        print("Try a larger number.")
    elif guess > secret_number:
        print("Try a smaller number.")
    else:
        print("Congratulations! You guessed correctly.")
        print("Number of attempts:", attempts)
        break