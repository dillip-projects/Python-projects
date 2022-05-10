import random
# declaring a function


def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    # using if statement to check whether my number is high low or exact the same guessed

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x} :"))

        if guess < random_number:
            print("Try again ! It's too low %d" % guess)

        elif(guess > random_number):
            print(f"Try again ! It's too high {guess} ")

    print("Yay , you have exactly guessed the same number {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = int(random.randint(low, high))

        else:
            guess = low
        feedback = input(
            f"Is {guess} too low (l),too high (h) or correct (c)??")

        if feedback == 'l':
            guess = low+1

        elif feedback == 'h':
            guess = high-1

    print(f"Yay! The computer guessed the correct number {guess}")


computer_guess(100)
# guess_number(15)  # calling the function to execute
