def vowel_or_not(var):
    if var in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False


if __name__ == "__main__":
    var = input("Enter any Alphabet : ")
    l = vowel_or_not(var.lower())
    if len(var) > 1:
        print("Please, Enter only one Character")
        exit()
    if l:
        print(var + ' is vowel')
    else:
        print(var + ' is not vowel')
