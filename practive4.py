length = int(input("Введіть довжину лінії: "))
symbol = input("Введіть символ для заповнення лінії: ")
if length <= 0:
    print("Довжина повинна бути додатньою!")
else:
    line = symbol * length
    print(line)
