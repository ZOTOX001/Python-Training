# 2. Check if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]
a =input("enter a string:")
result = is_palindrome(a)
if result == True:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")