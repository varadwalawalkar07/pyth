import random
print("WARNING! Write only integers")
n= int(input("Enter the range : "))
# n = int(n)
number = random.randint(0,n)
guesses = 0
# print(number)
#
# guess = input("Guess a number between 1 and 10: ")
# if guess == number:
#     print("Congratulations you have guessed the number!")
# else :
#     print("Wrong ! Try again !")
# print(f"The number was {number}")
while True:
    guesses += 1
    guess = int(input("Enter your guess : "))
    if guess == number:
        print("Correct !")
        break
    else:
        if guess < number:
            print("The number is greater than your guess.")
        elif guess >number:
            print("The number is smaller than your guess.")
print(f"You guessed {guesses} times")