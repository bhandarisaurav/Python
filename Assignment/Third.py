import os


def add():
    os.system('cls')
    print("Enter Your Academic Details")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    address = input("Enter Address: ")
    college = input("Enter College Name: ")
    level = input("Enter Study Level: ")
    course = input("Enter Course: ")


def view():
    pass


def update():
    pass


def delete():
    pass


def main():
    print("What Do You want to do")
    print("1 : Add Records")
    print("2 : View Records")
    print("3 : Update Records")
    print("4 : Delete Records")


if __name__ == "__main__":
    main()
    x = int(input("Enter:"))
    if x == 1:
        add()
    elif x == 2:
        view()
    elif x == 3:
        update()
    elif x == 4:
        delete()
    else:
        print("Error")
