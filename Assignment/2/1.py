def length(var):
    count = 0
    for x in var:
        count += 1
    return count


if __name__ == "__main__":
    var = input("Enter any String : ")
    var1 = input("Enter List elements followed by space : ")
    try:
       var1 = list(map(int, var1.split()))
    except ValueError:
        print("\nInput Error")
        print("\nGood Bye")
        exit(1)

    l = length(var)
    l1 = length(var1)

    print("\nLength of "+var+" is " + str(l)+"\n")
    print("Length of "+str(var1)+" is " + str(l1))
