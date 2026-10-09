# Цикл for
x = "Привет!"

# print(list(range(10)))
# quit()

x = [1, 5, 10, 15, 150]

# [0, 1, 2, 3, 4]
summ = 0

for i in range(len(x)):
    y: int = x[i]
    summ += y

# print(summ)
#
#
# for i in range(10):
#     print("hello")


# Условия
x = 5
if x > 0:
    print("X положительный")
else:
    print("X открицательный")


# Логические операторы

# больше
x > 5
# больше, или равно
x >= 5
# меньше
x < 5
# меньше, или равно
x <= 5
# равно
x == 5
# не равно
x != 5

# and or

x = 5
y = -5
x > 0 and y < 0  # True
x > 0 and y > 0  # False

x = 0
while x < 10:
    print("hello")
    x = x + 1
