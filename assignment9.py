# Benjamin Lemery
# 4/2/20
# This program checks whether a string is Palindrome or not

def PalindromeCheck(user_string):
    user_string = user_string.strip()
    user_string = user_string.lower()

    if len(user_string) < 2:
        print("The string you entered is a palindrome string.")
        call_user_input()
    if user_string[0] != user_string[-1]:
        print("The string you entered is not a palindrome string.")
        call_user_input()
    else:
         print(PalindromeCheck(user_string[1: -1]))

def call_user_input():
    user_string = input('Enter a string. This program will check if the string is a palindrome.')
    PalindromeCheck(user_string)

call_user_input()