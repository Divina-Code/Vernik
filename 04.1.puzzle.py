isGuessed = False
while isGuessed != True:
    puzzle = "4+10+12*20"
    answer = input(puzzle)
if answer == "254":
    print("Да,совершенно правильно!")
    isGuessed = True

else:
    print("нет, не верно")
