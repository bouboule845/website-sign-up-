#intro 
Print("welcome to Boost Tv!... please sign up here. ")
# List of usernames that are already taken
take_usernames = ['admin', 'admin123', 'user1', 'superuser']

# Special characters allowed in the password
special_chars = "!@?#$^&*_-"

# This will tell you whether the user has signed up successfully
signed_up = False

# These will save the final username and password
username = ""
password = ""

# One while loop to handle the whole process
while True:
    # Step 1: Signup process
    if not signed_up:
        username = input("Create a username: ")

        # Username must start with a lowercase letter
        # and can only have letters, numbers, or underscores
        if not username[0].islower():
            print("Invalid username")
            continue

        valid_chars = True
        for char in username:
            if not (char.isalnum() or char == "_"):
                valid_chars = False
                break

        if not valid_chars:
            print("Invalid username")
            continue

        # Check if the username is already taken
        if username in taken_usernames:
            print("Username taken")
            continue

        password = input("Create a password: ")

        # Check all password rules
        if len(password) < 8:
            print("invalid password ")
            continue

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        has_space = "" in password

        for char in password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True
            if char in special_chars:
                has_special = True

        if not (has_upper and has_lower and has_digit and has_special) or has_space:
            print("Invalid password")
            continue

        # If everything works and valid
        print("Sign up successful")
        signed_up = True

    # Step 2: Try to login
    else:
        login_username = input("Enter username: ")
        login_password = input("Enter password: ")

        if login_username != username or login_password != password:
            print("Incorrect username or password,")
            continue

        print("Login successful")
        break

