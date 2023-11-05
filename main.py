start = int(input("Введіть початок діапазону: "))
finish = int(input("Введіть кінець діапазону: "))
for число in range(start, finish + 1):
    if число % 7 == 0:
        print(число)