# fp = open("New_text.ext","a")
# print(fp)
#
# fp.write("\nHello World")
# fp.write("\nNew Line")
#
# fp.close()

# f = open("New_text.ext", "r+")
# print(f)
#
# print(f.read())
#
# f.close()
#
# print(f)
f = open("New_text.ext", "a+")

print(f.tell())
print(f.seek(4,0))
print(f.read())

f.write("\nHello World")
f.close()

f = open("New_text.ext", "a+")
print(f.read())
