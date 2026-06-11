print("Welcome to Chatbot Adventure Game!")
print("You will make choices and the bot will respond.\n")

name = input("What is your name? ")
print("Hello", name, "let's start!\n")

print("Choose your path:")
print("1. Go to the forest 🌲")
print("2. Go to the city 🏙️")

choice = input("Enter 1 or 2: ")

if choice == "1":
    print("\nYou entered the forest...")
    print("A wild animal appears!")

    action = input("Do you 'run' or 'fight'? ")

    if action == "run":
        print("You escaped safely!")
    else:
        print("You fought bravely, but it was dangerous!")

elif choice == "2":
    print("\nYou went to the city...")
    print("You meet a friendly stranger.")

    talk = input("Do you 'talk' or 'ignore'? ")

    if talk == "talk":
        print("They give you a secret mission!")
    else:
        print("You walk away and miss an opportunity.")

else:
    print("Invalid choice. Game over.")