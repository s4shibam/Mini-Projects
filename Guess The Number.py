import random

print("\n---- !! Guess the Number !! ----\n")
sr = int(input("Enter your desired \"Starting Range\" : "))
er = int(input("Enter your desired \"Ending Range\" : "))

if (er<sr):
    print("Game Crashed!!!")
    print("\"Starting Range\" can't be lesser than \"Ending Range\"!!")
    exit(0)
else:
    num = random.randint(sr, er)  # Random number selected

print(f"So..... The Number is Between {sr} to {er}")
print("Lets start the game.....")

if((er-sr)<=50):
    g = 5
elif((er-sr)>50 and (er-sr)<=100):
    g = 10
elif((er-sr)>100):
    g = 15

mg = g
print(f"You will get only {g} Guesses.")

while (1):
    if (g > 0):
        ui = int(input("\nGuess Number = "))
        if (ui > num):
            print("Alas!!! Hint: Decrease the number.")
            g -= 1
            print("Guesses Left : ", g)
        elif (ui < num):
            print("Alas!!! Hint: Increase the number.")
            g -= 1
            print("Guesses Left : ", g)
        elif (ui == num):
            print("Congrats!!! You guessed it Right!\n")
            print(f"Guessing ability = {(g * 100 / mg)} %")
            break
    elif (g == 0):
        print("\nGame Over!!!")
        print(f"Correct Number is = {num}.\nSorry!!! Better luck next time!!!")
        break
