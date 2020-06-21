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
line = '=' * 70


def main():
    intro()
    user_login()
    text = choose_text()
    analyze_text(text)


def intro() -> None:
    print(line)
    print("Welcome to our Text Analyzer!")
    print(line)


def user_login() -> None:
    print("Please log in.")
    username = input("Enter your username: ")
    while username not in registered_users.keys():
        print("\nLogin failed (invalid username)! ")
        username = input("Enter you username again or type 'exit' to end the application: ")
        if username == "exit":
            print("Thank you for using our application. See you later!")
            exit()
    password = input("Enter your password: ")
    while registered_users.get(username) != password:
        print("\nLogin failed (wrong password)! ")
        password = input("Enter your password again or type 'exit' to end the application: ")
        if password == "exit":
            print("Thank you for using our application. See you later!")
            exit()
    print('Login successful!')
    print(line)


def choose_text() -> str():
    print(f"We have {len(texts)} texts to be analyzed.")
    message = f"Please enter a number from 1 to {len(texts)} to select the text " \
              f"\nor type 'exit' to end the application: "
    while True:
        choice = (input(message))
        if choice == "exit":
            print("Thank you for using our application. See you later!")
            exit()
        try:
            text = texts[int(choice)-1]
            print(f"{line}\nSelected text: \n{text}\n{line}")
            return text
        except (ValueError, IndexError):
            print(f"\nInvalid input. Please try again!")


def analyze_text(my_text: str) -> None:
    word_list = [word.strip(' ,.!') for word in my_text.split()]
    title_words, upper_words, lower_words, numbers_count, numbers_sum = 0, 0, 0, 0, 0
    word_count = {}

    for word in word_list:
        if word.istitle():
            title_words += 1
        if word.isupper():
            upper_words += 1
        if word.islower():
            lower_words += 1
        if word.isnumeric():
            numbers_count += 1
            numbers_sum += (int(word))
        word_count[len(word)] = word_count.setdefault(len(word), 0) + 1

    print(f"There are {len(word_list)} words in the selected text.")
    print(f"There are {title_words} titlecase words in the text.")
    print(f"There are {upper_words} uppercase words in the text.")
    print(f"There are {lower_words} lowercase words in the text.")
    print(f"There are {numbers_count} numeric strings in the text.")
    print(line)

    for length in sorted(word_count.keys()):
        print(f'{length}-letter words: \t {"*" * word_count[length]} ({word_count[length]}x)')
    print(line)

    print(f'If we summed all the numbers in this text we would get: {numbers_sum}.')
    print(line)


main()