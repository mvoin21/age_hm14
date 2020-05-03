age = input('Введите Ваш возраст: ')
b = []
if int(age) % 2 == 0:
    for item in range(0, int(age)+1, 2):
        b.append(item)
    print(b)
else:
    for item in range(1, int(age)+1, 2):
        b.append(item)
    print(b)