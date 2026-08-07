user_string = input("Enter a string: ")


print("\n--- Character and ASCII Values ---")

for char in user_string:
    
    ascii_val = ord(char)
    print(f"Character: '{char}' \t ASCII Value: {ascii_val}")