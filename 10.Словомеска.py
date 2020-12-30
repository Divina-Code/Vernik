
from random import choice, shuffle

word = choice().lower()

words = ['антарктида, локомотив, драйвер, процессор, видюха']

word = choice(words).lower()
print(word)
shuffle_word = list(word)
shuffle(shuffle_word)




game = True

while game:
    user_word = input("Угадай слово: "+ ''.join(shuffle_word) )
    if user_word == word:
        print("Угадал")
        game = False
    else:
        print("Не угадал")
