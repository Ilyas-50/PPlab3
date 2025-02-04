def check(word):
    rever = word[::-1]
    if word == rever:
        print("this word is palindrome")
    else:
        print("this word is not palindrome")

check("pop")