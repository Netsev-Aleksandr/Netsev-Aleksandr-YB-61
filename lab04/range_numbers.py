a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
if a < b:
    step = 1
else:
    step = -1
for num in range(a, b + step, step):
    print(num)
