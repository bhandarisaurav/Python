from math import sin,radians
def sin_function(n):
    return sin(radians(n))


x = input("Enter The values separated by space")
x = list(map(int,x.split()))


result = list(map(sin_function,x))
result = [ round(elem, 2) for elem in result ]
print(*result,sep='\n')