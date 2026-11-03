CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"

# Get user input
username = input("Enter username: ")

# Check the username first
if username == CORRECT_USERNAME:
    # If username is correct, check the password
    password = input("Enter password: ")

    if password == CORRECT_PASSWORD:
        print("Login Successful")
    else:
        print("Error: Incorrect password.")
else:
    print("Error: Username not found.")