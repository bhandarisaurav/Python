# while True:
#     try :
#         x = int(input("Enter a number"))
#         break
#     except ValueError:
#         print("Oops ! That was not a valid number")
#
#
#
# try :
#     x = int(input("Enter a number"))
# except ValueError:
#     print("Oops ! That was not a valid number")
# finally:
#     print("Last Block")

num = input("Enter a Number : ")

try:
    if int(num) < 12:
        raise Exception("Number less than 12")
    a = int(num) / 0

except ZeroDivisionError:
    print("Cannot Divide by zero")
except TypeError:
    print("Type Mismatch")
except Exception:
    print("Custom Exception Caught")
else:
    print("Result is %f" % (a))
finally:
    print("Executes Always")
print("This Program Executed Successfully")
