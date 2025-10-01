import random
Num=random.randint(1,100)
chances=0
print("Guess the lucky number between 1 and 100")
print("You have 7 chances")
while chances < 7:
    chances+=1
    print(f"Attempt Number {chances}")
    Guess=int(input("What is the lucky number? "))
    if Guess == Num:
        print(f"Congratulations, you found the lucky number in {chances} attempts")
        break
    if Guess > Num:
        print("Too high")
        continue
    if Guess < Num:
        print("Too low")
        continue
else:
    print("You failed to guess the lucky number in 7 attempts")
    print(f"{Num} is the lucky number")