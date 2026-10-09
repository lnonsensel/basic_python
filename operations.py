# Числа
# Арифметика
x: int = 5
xnegative: int = -5

summ = 10 + 5  # 15
subt = 10 - 5  # 5
x = int("5") + 5  # 10

multiplication = 10 * 5  # 50
dell: float = 10 / 3  # 3.333333
dell_full = 10 // 3  # 3

ostatok = 10 % 3  # 1
# 3 + 3 + 3 = 9, до 10 не хватает 1, 1 = остаток от деления

power = 10**5  # 100000

# Bool
# or Или
# and И

true = False or True  # True
# ЛОЖНО или ПРАВДА -> ПРАВДА
# ПРАВДА или ЛОЖНО -> ПРАВДА
# ПРАВДА или ПРАВДА -> ПРАВДА
# ЛОЖНО или ЛОЖНО -> ЛОЖНО
# True -> 1
# False -> 0
#
# or -> сумма
#
# 0 + 1 = 1
# 1 + 0 = 1
# 1 + 1 = 1
# 0 + 0 = 0

false = False and True  # False

# and -> умножение
# 0 * 1 = 0
# 1 * 0 = 0
# 1 * 1 = 1
# 0 * 0 = 0

# Строка
string: str = "Привет!"
# str_list = ["П", "р", "и", "в", "е", "т", "!"]
print(string[0])  # Строка имеет индексы

# Стрез
print(string[0:6])  # Возьми от 0 до 5-1 (4)
print(string[:6])  # [0:6]
print(string[1:])  # ривет!
print(string[::-1])  # print(reversed(string))

# Конкатенация (сложение строк)
print("Привет," + " мир!" + " и не только мир!")

print("Привет! " * 3)

print(len("abcde"))
# length

# Функции регистра
# A - верхний регистр
# а - нижний регистр

print("abcde".upper())
print("ABCDE".lower())


# Поиск и проверка строк

# "abcde" -> "bcd", "cde"
print("bcd" in "abcde")
print("bcddddddddddddd" in "abcde")
print("abcddde".count("d"))
print("abcde".startswith("ab"))
print("abcde".endswith("de"))

# Списки
lst = ["a", "b", "c", "d"]
print(lst[1])  # b
print(lst[-1])  # d
print(len(lst))  # len -> length, 4
print(lst[1:3])  # b, c
print("b" in lst)  # True
print("f" in lst)  # False

# Изменение списка
# Добавление элементов
lst.append("e")
print(lst)
lst.insert(1, "aa")
print(lst)  # [a aa b c d e]
lst.extend(["f", "g"])  # [a aa b c d e f g]
lst = lst + ["f", "g"]
print("Объединение списков")
print(["a", "b"] + ["c", "d"])

print(lst)
new_lst = lst * 3
print(new_lst)

# Удаление элементов
lst.remove("aa")
print(lst)  #
lst.pop(0)
print(lst)
lst.pop()
print(lst)
lst.clear()
print(lst)


# Изменение элементов
lst = [10, 100, 1000, 10000]
lst[0] = lst[0] + 5
# x = 10
# x = x + 5
# x += 5
# x == 15
print(lst)
lst[0] = "Hello"
print(lst)
lst[1:3] = ["Привет", "мир"]
print(lst)
lst.reverse()
print(lst)


somelst = [1, 2, 3]
print(3 in somelst)
lst = [6, 4, 2, 10, 100]
print(lst)
lst.sort(reverse=True)
print(lst)

print(lst.index(10))
lst.append(10)
print(lst)
print(lst.count(10))

print(min(lst))
print(max(lst))
print(sum(lst))


# Словари
dct = {"hi": "hello", "bye": "goodbye"}

dct["u"] = "you"
print(dct)
dct.pop("u")
print(dct)

print(dct.keys())
print(dct.values())
print(dct.items())

dct1 = dict(name="Ivan", surname="Karpochev")
print(dct1)

name = dct1["name"]  # Выдаст ошибку, если ключа нет
name_new = dct1.get("name", None)  # Может вернуть None
print(name, name_new)

dct_quiz = {"a": 1}
print(dct_quiz.get("b", 0))
quit()

dct.popitem()
dct.clear()
print(dct)
# dct.pop()

st = {1, 2, 3, 4, 5}
st1 = {4, 3, 2}
print(st.difference(st1))

st.add(7)
st.pop()
print(st)


print(len((1, 2, 3)))


# bool(0) = False
# bool(-1, 2, 100, ) = True

# bool("") = False
# bool(" ", "abc", "asdasd") = True

# bool([]) = False
# bool([1.2]) = True


x = 1
# 3 == 3.0  # True
# 3 == 4  # False

# True | True == True
# True + True == 2
