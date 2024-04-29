
while True:
        typed = input("Введите число или exit: ")

        if typed == "exit":
            break

        try:
            typeConverted = int(typed)
        except ValueError:
            try:
                typeConverted = float(typed)
            except ValueError:
                print(f'"{typed}" не число и не exit.')
                continue

        typeStripped = str(abs(typeConverted))

        typeStripped = typeStripped.replace(".", "").replace(",", "")

        typedLength = len(typeStripped)

        print(f"Длина числа {typed}: {typedLength}")
