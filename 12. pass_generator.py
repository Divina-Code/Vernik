
import random
letters = list('abcdefgAEWFGFBJHWYDEWBFWGYWEBEWGYWE')
symb = list('!@#178%*$@$343264238y12355')
length = int(input("длина пароля?"))


password =''
for i in range(length):
    password += random.choice(letters)
print(password)
