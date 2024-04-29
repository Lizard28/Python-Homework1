typed = abs(int(input("Введите число: ")))

print(f"\n[{-typed}", end="")
for i in range(-typed + 1, typed + 1):
    print(f", {i}", end="")
print("]\n")

negativeSum = 0
for i in range(-typed, 0):
    negativeSum += i

positiveSum = 0
for i in range(0, typed + 1):
    positiveSum += i

print(f"Сумма отрицательных чисел: {negativeSum}")
print(f"Сумма положительных чисел: {positiveSum}")
