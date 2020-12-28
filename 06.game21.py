while inGame1:


if ingame1:
    take_card = input('Будешь брать карту? [ДА\НЕТ]')
    if take_card == "ДА":
        player1 +=3
        print("Теперь у тебя очков", player1)
    elif take_card =="НЕТ":
        inGame1 = False
    else:
        print("Я тебя не понял")

    if player1>=21:
        inGame1 = False
print("Игра окончена")

    if player1<=21:
        print("Ты победил! Ура!")
    else:
        print("Ты проиграл! Увы!")





