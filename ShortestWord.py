sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
    shortest_word = min(words, key=len)
    print(f"The shortest word is: {shortest_word}")
else:
    print("No words entered.")
    
