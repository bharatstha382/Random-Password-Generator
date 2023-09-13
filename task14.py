import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_letters = []
for letter in range(1, nr_letters+1):
    letter = random.choice(letters) 
    password_letters.append(letters)
    
password_symbol = []
for symbol in range(1,nr_symbols+1):
    symbol = random.choice(symbols)
    password_symbol.append(symbol)

password_numbers = []
for number in range(1,nr_numbers+1):
    number = random.choice(numbers)
    password_numbers.append(number)

password_letters.extend(password_symbol)
password_letters.extend(password_numbers)
print(password_numbers)
password = []
for password_ in range(1, nr_letters+nr_symbols+nr_numbers+1):
    password_ = random.choice(password_letters)
    password.append(password_)
print("test", password)
password__ = ""
for a in range (len(password)):
    print(password[a])
    password__ += random.choice(password[a])
print(password__)