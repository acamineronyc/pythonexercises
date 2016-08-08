secret_number = 8

while True:
    guess = int(input("Guess the number between 1 and 15: "))

    if guess == secret_number:
        print("Congratulations! you guess the number.")
        break
    else:
        print("Enter another number")

