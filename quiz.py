print("Welcome to the game")
question = input("What would you like play? (Y/N) : ")
# print(question)

if question.upper() =="N":
    print("Thankyou for playing")
    quit()
print("Welcome to the game")

score=0

answer = input("What is the full form of PC? ")
if answer.upper() == "PERSONAL COMPUTER":
    print("Correct !")
    score += 1
else:
    print("Wrong !")

answer = input("What is the full form of RAM? ")
if answer.upper() == "RANDOM ACCESS MEMORY":
    print("Correct !")
    score += 1
else:
    print("Wrong !")

answer = input("What is the full form of CPU? ")
if answer.upper() == "CENTRAL PROCESSING UNIT":
    print("Correct !")
    score += 1
else:
    print("Wrong !")
if score == 1:
    print("You got " + str(score) + " question correct")
else:
    print("You got " + str(score) + " questions correct")
print("Your score is "+ str((score/4)*100)+"%")