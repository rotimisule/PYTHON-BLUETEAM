sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    word=input("Enter a word in English or EXIT: ")
    
    if word == "EXIT":
        break  # Exit the loop if the user enters "EXIT"
    
    if word in sample_dict:
        print("Translation:", sample_dict[word])  # Prints the translation if the word exists in the dictionary
    else: 
        print("No match!")  # Prints "No match!" if the word doesn't exist in the dictionary

print('Bye!')  # Prints "Bye!" after exiting the loop

