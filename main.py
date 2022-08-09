import random

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senha em Python!")
nr_lowers = int(input("Quantas letras MINÚSCULAS você gostaria na sua senha?\n"))
nr_upper = int(input("Quantas letras MAIÚSCULAS você gostaria na sua senha??\n"))
nr_symbols = int(input(f"Quantos símbolos você gostaria na sua senha?\n"))
nr_numbers = int(input(f"Quantos números você gostaria na sua senha?\n"))

password_list = []

for char in range(0, nr_lowers):
	password_list += random.choice(lower)

for char in range(0, nr_upper):
	password_list += random.choice(upper)

for number in range(0, nr_numbers):
	password_list += random.choice(numbers)

for symbol in range(0, nr_symbols):
	password_list += random.choice(symbols)
random.shuffle(password_list)

password = ""
for char in password_list:
	password += char

print(f"Sua senha pode ser ==> {password} <==")

input("Pressione ENTER")
