

from random import randint


random_number = randint(100, 999)

code = str(random_number)



game = True
while game:
    user_number = input("Введи трёхзначное число:")
    if len(user_number)!= 3:
        print("Это не трёхзначное число")
    elif user_number == code:
        print("Ты угадал")
        game = False
    else:
        for d in user_number:
            if d in code:
                right_number += 1
    print("Ты угадал вот столько цифр:", right_number)
