
var = input("Enter sequence of comma-separated numbers : ")
lists = list(map(int,var.split(',')))
tuples = tuple(map(int,var.split(',')))

print('list = '+str(lists))
print('tuple = '+str(tuples))
