import string
from random import choice, randint

letters = string.ascii_letters 
digits = string.digits 
symbols = string.punctuation
chars = letters + digits + symbols

min_length = 15
max_length = 21
password = "".join(choice(chars) for x in range(randint(min_length, max_length)))
print(password)
