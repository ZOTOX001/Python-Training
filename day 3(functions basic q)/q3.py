#create a palindrome checker function:
def palindrome(word):
    rev=""
    for i in range(len(word)-1,-1,-1):
        rev += word[i]

    if rev ==word:
            print("Palindrome")
    else:
            print("Not Palindrome")
            
palindrome("Aniket")
palindrome("naman")
