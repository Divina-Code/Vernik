import random
i = False
num = random.randit(1, 10)
while i != True:
    op = int(input("я загадал число от одного до десяти, угадай его"))
    if num == op:
        print("ты красавчик")
        i = True
    elif num < op:
        print("мое число больше")
    elif op == 0:
        print("жаль ты не смог угадать моё число, я загадал число", num)
        i = True

    else:
        print("число меньше")

print("спасибо за игру, друг")
