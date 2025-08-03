import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']
print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
letters_pass = random.sample(letters, nr_letters)
symbols_pass = random.sample(symbols, nr_symbols)
numbers_pass = random.sample(numbers, nr_numbers)
password = letters_pass + symbols_pass + numbers_pass
print(password)
random.shuffle(password)
password_string = ""
for n in range(0, len(password)):
    password_string += password[n]
print(password_string)
