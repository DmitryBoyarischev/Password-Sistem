password = input("Create password: ")
while True:
    for i in range(3):
        input_password = input("Enter your password: ")
        if password == input_password:
            print("Login successful")
            exit()
        else:
            if i<2:
                print("Wrong password. Try again.")
            else:
                print(f"Hey, password is: <{password}>")
