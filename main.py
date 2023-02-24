#Ввод значень:
a = float(input("Введіть значення першого числа: "))
b = float(input("Введіть значення другого числа: "))
c = float(input("Введіть значення третього числа: "))
d = float(input("Введіть значення четвертого числа: "))

#Створення списку
mathList = [a + b, b - a, c * d, d / c, a ** b, b // a, c % d]

lengthMath = len(mathList)
print("Кількість елементів списку: ", lengthMath)

print("Парні елементи списку:")
index = 0
for i in mathList:
    if index % 2 != 0:
        print(i)
    index += 1

#Функція для виведення списку
def printList(arr):
    for i in arr:
        print(i)


print("Список до змін місцями 2го та 5го елементу:")
printList(mathList)

tmp = mathList[1]
mathList[1] = mathList[4]
mathList[4] = tmp

print("Після:")
printList(mathList)

name = input("Введіть прізвище та ім'я: ")
conclusions = "В цій роботі ми познайомились із основами мови Python"
print(f"Прізвище та ім'я: {name} \nВисновки: {conclusions}")
