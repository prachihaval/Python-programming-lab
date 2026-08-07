
user_string = input("Enter a string: ")

reversed_string = ""

for i in range(len(user_string) - 1, -1, -1):
    reversed_string += user_string[i]

print(f"The reversed string is: {reversed_string}")