user_string = input("Enter a string: ")
seen = set()
duplicates = []
for char in user_string:
    if char in seen and char not in duplicates:
        duplicates.append(char)
    seen.add(char)
print(f"Duplicate characters: {duplicates}")