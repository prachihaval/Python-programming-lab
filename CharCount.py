
user_string = input("Enter a string: ")

consonants = 0
digits = 0
spaces = 0
special_chars = 0


vowel_set = "aeiouAEIOU"


for char in user_string:
    if char.isspace():
        spaces += 1
    elif char.isdigit():
        digits += 1
    elif char.isalpha():
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
    else:
        special_chars += 1


print("\n--- Character Count Results ---")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special Characters: {special_chars}")