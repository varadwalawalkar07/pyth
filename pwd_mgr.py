from os import write
from cryptography.fernet import Fernet

master_pwd= input("What is the master password? ")
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)
# write_key()
def load_key():
    return open("key.key","rb").read()
key = "B5qHErXiMAm9ZMCxXnKXH60K2fc9FB5ABkTzHmoS6qw="
fer = Fernet(key.encode())

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            #rstrip strips(erases) the \n
            if " - " not in data:
                continue
            user , passw = data.split(" - ")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Enter Account Name : ")
    pwd = input("Enter Account Password : ")
    # file = open('passwords.txt', 'a')
    # file.close()
    with open('password.txt','a') as f:
        f.write(name + " - " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Which mode would you like to prefer (view/add)? [Press q to quit] ")
    if mode.lower()== "q":
        print("Thankyou for you time")
        break
    if mode.lower()== "view":
        view()
    elif mode.lower()=="add":
        add()
    else:
        print("Invalid choice")
        continue