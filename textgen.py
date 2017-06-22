import random, string

letter_input_1 = input("What letters do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")

def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3
    return(name)

print(generator())