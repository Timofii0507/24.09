num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
min_num = min(num1, num2)
max_num = max(num1, num2)
sum_of_numbers = 0
count_of_numbers = 0
for number in range(int(min_num), int(max_num) + 1):
    sum_of_numbers += number
    count_of_numbers += 1
average = sum_of_numbers / count_of_numbers
print(f"Сума чисел у діапазоні від {min_num} до {max_num} = {sum_of_numbers}")
print(f"Середнє арифметичне чисел у цьому діапазоні = {average}")
