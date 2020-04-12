secret = 19

guess=int(input("Can you guess the number?(Choose between 1 and 21)"))

if guess== secret:
    print("Congratulations! Your number is correct!")
else:
    print("Sorry, the number is not "+ str(guess) + " :(")

