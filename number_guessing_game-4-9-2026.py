from random import randint
ans = randint(1,100)
print("Guess a number from one to a hundred")
guess = int(input("Guess the number:"))
while guess !=ans:  
    if guess > ans:
        print("number is lower than", guess)
    elif guess<ans:
        print("number is higher than", guess)
    guess = int(input("Guess the number"))

print("Thats right")