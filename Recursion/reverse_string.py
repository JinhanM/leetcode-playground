def reverseString(s):
    if len(s) == 0:
        return s
    return reverseString(s[1:]) + s[0]


print(reverseString("test"))
