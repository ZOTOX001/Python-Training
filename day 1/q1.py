#palindrome check:
n = input("Enter a word: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
