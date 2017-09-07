def _ispalindrome(p):
    reverse = ""
    # for i in range(len(p) - 1, -1, -1):
    #     reverse += p[i]
    # if p == reverse:
    #     return True
    # else:
    #     return False
    index = len(p)
    while index:
        index -= 1
        print(index)
        reverse = reverse+p[index]
    if p == reverse:
        return True
    else:
        return False


if __name__ == "__main__":
    p = input("Enter a String")
    if _ispalindrome(p):
        print(p + " is Palindrome")
    else:
        print(p + " is not Palindrome")
