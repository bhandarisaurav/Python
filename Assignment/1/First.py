import os

os.system('cls')


def menu():
    print("Enter Your Academic Details")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    add = input("Enter Address: ")
    address = list(map(str, add.split()))
    x = int(address[3])
    address[3] = x
    print(address)
    college = input("Enter College Name: ")
    level = input("Enter Study Level: ")
    course = input("Enter Course: ")
    course = tuple(map(str, course.split()))
    dictionary = {'name': name, 'age': age, 'address': address, 'college': college, 'level': level, 'course': course}
    x = 1
    data = {x: dictionary}
    x += 1
    return data


def display_data(data):
    print(data)


if __name__ == "__main__":
    n = int(input("How Many Data you want to Insert : "))
    os.system("cls")
    for i in range(0, n):
        os.system("cls")
        x = menu()
    display_data(x)