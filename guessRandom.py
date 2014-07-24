from random import randint
myvar = randint(0, 100)
print("random integer number generated between 0 and 100, try to guess this number.")
guess = -1

while guess != myvar:
    guess = int(input("try: "))
    if guess > myvar:
        print("random number is lower")
    elif guess < myvar:
        print("random number is higher")
    else:
        print("congratulations, you found the random number!")
