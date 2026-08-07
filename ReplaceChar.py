
user_string = input("Enter a string: ")


old_char = input("Enter the character to replace: ")


new_char = input("Enter the replacement character: ")


modified_string = ""


for char in user_string:
    if char == old_char:
        modified_string += new_char
    else:
        modified_string += char


print(f"The modified string is: {modified_string}")