from types import NoneType

# Числа
# Целые "Integer"

x: int = 5
x1: int = -5

# С плавающей точкой (дробные)
y: float = 4.5
y1: float = -4.5

# Логическое значения
zt: bool = True
zf: bool = False

# Строка "String"
s: str = "Привет!"


# Компонентные типы:
# Список
lst: list = [5, 4.5, True, "Hello, world!"]
print(lst[3])
print(lst[-1])  # Считаем с конца

# Кортеж
tup: tuple = (5, 4.5, True)  # То же, что список, но нельзя менять

# Словарь
dct: dict = {"hello": "привет", "bye": "пока"}
dct1: dict = {"Один точка двадцать пять": 1.25}
# {ключ: значение}, по ключу получаем значение
print(dct["hello"])  # -> привет

# Множество
st: set = {1, 1, 1, 2, 2, 3, 4, 5}  # -> Только уникальные значения
print(st)

# Пустой тип
nothing: NoneType = None
