import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    
    print("Welcome to 'Guess the Number'!")
    print("I have picked a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        
    print("Thanks for playing!")

if __name__ == "__main__":
    guess_the_number()

