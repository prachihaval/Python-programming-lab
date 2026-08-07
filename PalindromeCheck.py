# Input a string from the user
user_string = input("Enter a string: ")

# Initialize an empty string to store the reversed version
reversed_string = ""

# Reverse the string manually
for i in range(len(user_string) - 1, -1, -1):
    reversed_string += user_string[i]

# Compare the original string with the reversed string
if user_string == reversed_string:
    print(f"'{user_string}' is a palindrome!")
else:
    print(f"'{user_string}' is not a palindrome.")