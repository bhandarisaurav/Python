# Python

Python Training Files
# counter = 0
# while counter < 3:
#     print("loop #%d" % counter)
#     counter += 1
#
# for i in range(0, 3):
#     print("First Loop:%d" % i)
#     for j in range(0, 3):
#         print("Second Loop:%d" % j)
#         for i in range(0, 3):
#             print("Third Loop:%d" % i)


# l= [1,2,3,4,5,6]
#
# for i  in l:
#     print(l)
#     pass

# for item in [1,2,3,4,5]:
#     # if item == 3:
#     pass
#     print(item)

# for i in range(0,999999999999999999):
#     print(i,end='\t')
#
# def test():
#     return "Hello"
#
# x = test()
#
# print(x)
# -----------------------------------------------
# def test(x = 99):
#     print(x*x)
#
# test()
# -----------------------------------------------
# def test(*args, msg="Hello"):
#     print(args)
#     print("args " + str(args))
#     print("msg " + msg)
# test()
# test("a")
# test(1, 2, 3, 4, msg= "Message")
# -----------------------------------------------


# def greet_me(**kwargs):
#     if kwargs is not None:
#         for key, value in kwargs.items():
#             print("%s == %s" % (key,value))
#
# greet_me(name="Saurav" ,age =18, add = "KTM")


# def greet_me(**pair):
#     if pair is not None:
#         for key, value in pair.items():
#             print("%s == %s" % (key,value))
#
# greet_me(name="Saurav" ,age =18, add = "KTM")
# d = {"name" : "ram", "age" : 18}
#
# for value in d.values():
#     print("value" + "," +str(value))






# for item in [1,2,3,4,5]:
#     if item == 3:
#         break
#     print(item)

#####################################################################

# def test(msg="hello"):
#     print(msg)
#
# test("world")

#####################################################################
#
# def test(*args):
#     print(args)
#
#
# test()
# test("a")
# test(1, 2, 3, 4)

#####################################################################

# def greet_me(**pair):
#     if pair is not None:
#         for key, value in pair.items():
#             print("%s = %s"%(key,value))
#
# greet_me(name="ram", age =12)

#####################################################################

# d = {"name": "ram", "age": 18}
#
# print("---------------------------------------")
#
# for key, value in d.items():
#     print(key + "," + str(value))
#
# print("---------------------------------------")

#####################################################################

# def modifyList(l):
#     l.append("newVal")
#
# def modifyString(s):
#     s.upper()
#     print("inside function:" + s.upper())
#
# ls = [1,2,3]
# ms = "Hello"
#
# print(ls)
# print(ms)
#
# modifyList(ls)
# modifyString(ms)
#
# print(ls)
# print(ms)

#####################################################################

# def modifyList(l):
#     l.append("newVal")
#
# def modifyString(s):
#     s.upper()
#     print("inside function:" + s.upper())
#
# def modifyDict(d):
#     d.update({"f":6})
#    # d={}
#
# ls = [1,2,3]
# ms = "Hello"
# d={"a":1, "b":2, "c":3}
#
# print(ls)
# print(ms)
#
# modifyList(ls)
# modifyString(ms)
#
# print(ls)
# print(ms)
# print(d)

#####################################################################


