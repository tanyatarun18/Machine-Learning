import random

number = random.randint(1,50)
guess = int(input("Enter your guess: "))

count = 1
while guess != number:
    if(guess < number):
        print("Wrong! Think higher")
    else:
        print("Wrong! Think lower")

    guess = int(input("Enter your guess: "))
    count += 1
else :
    print("Sahi Jawab!")
    print("Attempts: ", count)