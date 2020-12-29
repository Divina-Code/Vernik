words = input("Введи слова:").lower().split()

print("палиндромы")

for word in words:
    if word == word[::-1]:
        palindroms.append(word)






