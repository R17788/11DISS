from collections import defaultdict, Counter
word = input("Enter a word: ")
my_dict = {}  # Create a dictionary object
for letter in word:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)


for key, val in my_dict.items():
    print(f'Letter: {key}, Count: {val}')
print(f'There are {len(word)} total letters in the word {word}')
print(f'There are {len(my_dict)} unique letters in the word {word}')

