
user_string = input("Enter a string: ")


target_char = input("Enter the character to find: ")


count = 0

for char in user_string:
    if char == target_char:
        count += 1


print(f"The character '{target_char}' appears {count} time(s) in the string.")