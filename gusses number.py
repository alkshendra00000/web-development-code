import random

print("🎯 Welcome to Number Guessing Game 🎯")
print("I have selected a number between 1 to 100.")
print("Try to guess it!\n")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too Low! Try again.\n")
    elif guess > secret_number:
        print("📈 Too High! Try again.\n")
    else:
        print(f"🎉 Congratulations jaanu! You guessed it right 🎉")
        print(f"✅ The number was: {secret_number}")
        print(f"🔢 Total attempts: {attempts}")
        break
