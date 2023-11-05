start = int(input("Введіть початок діапазону: "))
finish = int(input("Введіть кінець діапазону: "))
print("Всі числа в діапазоні:")
for число in range(start, finish + 1):
    print(число, end=" ")
print("\nВсі числа в діапазоні в спадному порядку:")
if start > finish:
    print("Помилка: Початок діапазону більший за кінець.")
else:
    for число in range(start, finish - 1, -1):
        print(число)
for число in range(start, finish - 1, -1):
    print(число, end=" ")
print("\nВсі числа, кратні 7:")
for число in range(start, finish + 1):
    if число % 7 == 0:
        print(число, end=" ")
print("\nКількість чисел, кратних 5:")
for число in range(start, finish + 1):
    if число % 5 == 0:
        print(число, end=" ")