import random
import time

operators = [" + "," - "," * "]
number1 = 3
number2 = 9
total_problems = 10

def solution():

    left = random.randint(number1,number2)
    right = random.randint(number1,number2)
    operator = random.choice(operators)

    expr = str(left) +" "+ operator + "" + str(right)
    answer = eval(expr)
    return expr, answer

correct = 0
input("Press Enter to Start!")
print("---------------------")

start_time = time.time()

for i in range (total_problems):
    expr,answer = solution()
    guess = input ( "Problem #"+ str(i+1)+ " : "+ expr + " = ")
    if guess == str(answer):
        correct +=1

end_time = time.time()
total_time = round(end_time - start_time,2)

print("-----------------------")
print("You finished in ",total_time)
print("You got",correct,"questions correct!")