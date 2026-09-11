user_input = input("Enter a string: ")
origional = user_input
reverse_string = origional[::-1]
if origional == reverse_string:
    print("the string is palindrome")
else:
    print("the string is not palindrome")
