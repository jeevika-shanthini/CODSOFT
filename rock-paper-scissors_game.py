import random

print("\n========== Rock Paper Scissors Game ==========")

while True:
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    users_choice=int(input("type 0 for rock, 1 for paper or 2 for scissors:\n"))
    choices=["rock","paper","scissors"]

    if users_choice>=0 and users_choice<=2:
        print(choices[users_choice])

    computers_choice=random.randint(0,2)
    print("\nComputer chose:")
    print(choices[computers_choice])

    if users_choice>=3 or users_choice<0:
        print("\nInvalid number,you lose")

    elif users_choice==computers_choice:
        print("\nGame is draw")

    elif users_choice>computers_choice:
        print("\nYou win !")

    elif computers_choice>users_choice:
        print("\nComputer Wins !")

    elif users_choice==0 and computers_choice==2:
        print("\nYou win !")

    else:
        print("\nComputer Wins !")
    play = input("\nDo you want to play again? (yes/no): ").lower()

    if play != "yes":
        print("\nThank you for playing!")
        break