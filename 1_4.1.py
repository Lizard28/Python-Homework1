ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
shipLower = ship.lower()

while True:  
    typed = input("Ваш ход (буква и цифра): ")

    if len(typed) == 2:
        break
    print("Введите ровно 2 символа")

typedLower = typed.lower()

if typedLower[0].isalpha() and typedLower[1].isdigit() :
    hit = shipLower.replace(" ", "").find(typedLower)
    print("Промах" if hit == -1 else "Попадание")
else:
    print("Введенные значения не соответствуют условиям")

