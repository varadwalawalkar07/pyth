start = input("Type Start to enter the game : ")
if start.lower() == "start":
    game = input("You are now on a dead end, you can go left or right.")
    if game.lower() == "left":
        answer = input("You jumped of a cliff now you are in water. Type swim to swim ")
        if answer.lower()== "swim":
            print("Congratulations you have reached the coast.")
        else:
            print("Not a valid option you lose.")
    elif game.lower() == "right":
        print("You are now in the jungle. Woah a lion caught you. Sorry you died")
    else:
        print("Not a valid option you lose.")

else:
    print("Not a valid option but thanks for playing")