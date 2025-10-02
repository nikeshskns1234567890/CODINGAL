import random

# Football legends list (icons of football history)
football_legends = ["Pele", "Diego Maradona", "Zinedine Zidane", "Ronaldinho", "Thierry Henry", "David Beckham", "Roberto Carlos"]

# Dictionary for player info
player = {'name': '', 'favorite_icon': ''}

print("🏆 Welcome to the Football Legends Guessing Game ⚽")
print("I’m thinking of a number between 1 and 20.")
print("If you guess it right, you’ll be matched with a football legend! 🔥")

# Secret number chosen by computer
secret_number = random.randint(1, 20)

# Get player info
player['name'] = input("Enter your name, young footballer: ")

# Game loop
attempts = 0
while True:
    guess = int(input("⚽ Take your shot! Guess a number (1-20): "))
    attempts += 1

    if guess == secret_number:
        # Match with a random football legend
        player['favorite_icon'] = random.choice(football_legends)
        print(f"\n🥳 GOAL!!! {player['name']} has scored! 🏆")
        print(f"You guessed the number in {attempts} attempts.")
        print(f"🔥 Your football icon is: {player['favorite_icon']}")
        break
    elif guess < secret_number:
        print("👉 Shot was too weak... Aim higher! ⬆️")
    else:
        print("👆 Shot went over the crossbar... Aim lower! ⬇️")
