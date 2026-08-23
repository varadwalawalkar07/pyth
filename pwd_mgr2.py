import os
import hashlib
import getpass
from cryptography.fernet import Fernet

KEY_FILE = "key.key"
MASTER_FILE = "master.key"
PASSWORD_FILE = "password.txt"


# ---------- Fernet key ----------

def write_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)


def load_key():
    if not os.path.exists(KEY_FILE):
        write_key()

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


key = load_key()
fer = Fernet(key)


# ---------- Master password ----------

def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000
    )


def setup_master_password():
    print("No master password found.")
    print("Let's create one.")

    while True:
        password = input("Create master password: ")
        confirm = input("Confirm master password: ")

        if password != confirm:
            print("Passwords do not match. Try again.\n")
            continue

        if len(password) < 8:
            print("Master password must be at least 8 characters.\n")
            continue

        salt = os.urandom(16)
        password_hash = hash_password(password, salt)

        with open(MASTER_FILE, "wb") as f:
            f.write(salt + password_hash)

        print("Master password created successfully!\n")
        return True



def authenticate():
    if not os.path.exists(MASTER_FILE):
        setup_master_password()
        return True

    with open(MASTER_FILE, "rb") as f:
        data = f.read()

    salt = data[:16]
    stored_hash = data[16:]

    for attempt in range(3):
        master_pwd = input("Enter master password: ")


        entered_hash = hash_password(master_pwd, salt)

        if entered_hash == stored_hash:
            print("\nAuthentication successful!\n")
            return True

        remaining = 2 - attempt
        print("Incorrect master password.")

        if remaining > 0:
            print("Attempts remaining:", remaining)

    print("Too many failed attempts.")
    return False


# ---------- Password manager ----------

def view():
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords saved yet.")
        return

    with open(PASSWORD_FILE, "r") as f:
        for line in f.readlines():
            data = line.rstrip()

            if " - " not in data:
                continue

            user, passw = data.split(" - ", 1)

            try:
                password = fer.decrypt(passw.encode()).decode()
                print("User:", user, "| Password:", password)
            except Exception:
                print("Could not decrypt this password.")


def add():
    name = input("Enter Account Name: ")
    pwd = input("Enter Account Password: ")


    encrypted_password = fer.encrypt(pwd.encode()).decode()

    with open(PASSWORD_FILE, "a") as f:
        f.write(name + " - " + encrypted_password + "\n")

    print("Password saved successfully.")


# ---------- Main program ----------

if not authenticate():
    quit()

while True:
    mode = input(
        "\nWhich mode would you like? "
        "(view/add) [Press q to quit]: "
    ).lower()

    if mode == "q":
        print("Thank you for your time!")
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid choice. Please choose view, add, or q.")
