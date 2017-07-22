age=int(input("Enter Age :"))
if(age<20):
    if(age>11):
        print("Teen")
    else:
        print("Not Teen")
elif (age>20 and age<60):
    print("Adult")

else:
    print("Old")