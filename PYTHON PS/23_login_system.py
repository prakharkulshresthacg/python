correct_username = "admin"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username != correct_username:
    print("User not found")
elif password != correct_password:
    print("Wrong password")
else:
    print("Login successful")
