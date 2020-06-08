texts = [
    '''Situated about 10 miles west of Kemmerer, Fossil Butte 
is a ruggedly impressive topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley to an elevation of more 
than 7500 feet above sea level. The butte is located just north 
of US 30N and the Union Pacific Railroad, which traverse the valley.''',

    '''At the base of Fossil Butte are the bright red, purple, 
yellow and gray beds of the Wasatch Formation. Eroded portions 
of these horizontal beds slope gradually upward from the valley 
floor and steepen abruptly. Overlying them and extending to the 
top of the butte are the much steeper buff-to-white beds 
of the Green River Formation, which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects a portion 
of the largest deposit of freshwater fish fossils in the world. 
The richest fossil fish deposits are found in multiple limestone 
layers, which lie some 100 feet below the top of the butte. 
The fossils represent several varieties of perch, as well as other 
freshwater genera and herring similar to those in modern oceans.
Other fish such as paddlefish, garpike and stingray are also present.'''
]

registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}
text_id = {'1', '2', '3'}
line = '=' * 70

# User input

print(line)
print('Welcome to our Text Analyzer!')
print(line)

print('Please log in.')
username = input('Enter your username: ')
if username not in registered_users.keys():
    print('Login failed (invalid username)!')
    exit()
password = input('Enter your password: ')
if registered_users.get(username) == password:
    print('Login successful!')
    print(line)
else:
    print('Login failed (invalid password)!')
    exit()

print('We have 3 texts to be analyzed.')
user_choice = ''
while user_choice not in text_id:
    user_choice = input('''Please enter a number from 1 to 3 to select the text 
or type exit to end the application: ''')
    if user_choice == 'exit':
        print('See you later!')
        exit()
else:
    print(line)
    text = texts[int(user_choice)-1]
    print(f'Selected text: \n{text}')
    print(line)

# Text analysis

text_length = len(text.split())
title_words = 0
upper_words = 0
lower_words = 0
numbers = []
word_count = {}

for raw_word in text.split():
    word = raw_word.strip(' ,.!')
    if word.istitle():
        title_words += 1
    if word.isupper():
        upper_words += 1
    if word.islower():
        lower_words += 1
    if word.isnumeric():
        numbers.append(int(word))
    word_count[len(word)] = word_count.setdefault(len(word), 0) + 1

# Output

print(f'There are {text_length} words in the selected text.')
print(f'There are {title_words} titlecase word(s) in the text.')
print(f'There are {upper_words} uppercase word(s) in the text.')
print(f'There are {lower_words} lowercase word(s) in the text.')
print(f'There are {len(numbers)} numeric string(s) in the text.')
print(line)

for length in sorted(word_count.keys()):
    print(f'{length}-letter words: \t {"*" * word_count[length]} ({word_count[length]}x)')
print(line)

print(f'If we summed all the numbers in this text we would get: {sum(numbers)}.')
print(line)