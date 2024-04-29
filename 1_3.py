typed = input("Введите число, которое:\n1) Должно быть положительным\n2) Должно быть трёхзначным\n3) Иметь неповторящиеся цифры\n> ")

typedInteger = int(typed)

typedIntegerUniqueDigits = []
for i in str(typedInteger):
    if i not in typedIntegerUniqueDigits:
        typedIntegerUniqueDigits += i

if typedInteger < 0 or len(str(typedInteger)) != 3 or len(typedIntegerUniqueDigits) != 3:
    print(f"{typedInteger} не подходит по условиям.")
    exit(0)
else:
    typedInteger = str(typedInteger)
    print("")

indexCombinations = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [1, 2, 0],
    [2, 0, 1],
    [2, 1, 0],
]

for i, j, k in indexCombinations:
    print(f"{typedInteger[i]}{typedInteger[j]}{typedInteger[k]}")
