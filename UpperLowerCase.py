
user_string = input("Enter a string: ")



for char in user_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1


print("\n--- Case Count Results ---")
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")