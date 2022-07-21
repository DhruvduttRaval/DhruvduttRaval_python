import random
num = random.randint(1,20)
while True :
    guess = int(input("Guess A Number Between 1 to 20 :"))
    if guess == num:
        print("You Guessed A Correct Number")
    elif guess > num:
        print("You Guessed A Greatest Number")
    elif guess < num:
        print("You Guessed A Smallest Number")
