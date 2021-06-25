def login(name, password):
    print("logged in")


def register(name, password):
    print("registered")


def access(option):
    if (option == "login"):
        name = input("Enter your name:")
        password = input("Enter your password:")
        login(name, password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your name:")
        password = input("Enter your password :")
        register(name, password)


def begin():
    global option
    print("Welcome to Felix Osmond Programming Club")
    option = input("Login or Register(login,reg):")
    if (option != "login" and option != "reg"):
        begin()


begin()
