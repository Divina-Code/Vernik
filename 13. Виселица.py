

word = 'Локомотив'

letters = []
for a in range(len(word)):
    letters.append("_")


print(''.join(letters))

stop = False
lives = 9

while stop == False:
    answer = input("Скажите букву или слово")

if answer == word:
    for a in range(len(word)):
        letters[a] = word[a]
print('Вы угадали слово или букву')
if answer != word:
    for i in range(len(word)):
        if answer == word[i]:
            letters[i] = word[i]
        if lives == 1:
            stop = True
            print("Вы потерпели поражение!")

        lives += -1

        print(''.join(letters))

        if stop == False:
            if lives > 1:
                print("У вас осталось", lives, 'попыток\n')
            else:
                print("У вас осталось",lives,'попытки\n')

            print("Благодарю за игру")





