text = input("Please type your text here: ")

all_vowels = "aeiou"
vowel_count = 0

for char in text.lower():
    if char in all_vowels:
        vowel_count += 1
        
print("There are {} vowels in your inputed text!".format(vowel_count))