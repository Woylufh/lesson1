x = 38

print("Здравствуйте!")
if x < 0:
    print("Меньше нуля")# вывод игнорирует, так как x > 0
print("Досвидания!")


a, b = 10, 5

if a>b:
    print("a>b")# все команды выполнены, так как удовлетворяет всем нормам и правилом.

if a > b and a > 0:
    print("успех")# все команды выполнены, так как удовлетворяет всем нормам и правилом.
if (a > b) and (a > 0 or b < 1000):
    print("успех")# все команды выполнены, так как удовлетворяет всем нормам и правилом.
if 5<b and b<10:
    print("успех")# вывод игнорирует, так как b=5.


if "34" > "123":
    print("успех")# все команды выполнены, так как удовлетворяет всем нормам и правилом.

if "123" > "12":
    print("успех")# все команды выполнены, так как удовлетворяет всем нормам и правилом.

if [1, 2] > [1, 1]:
    print("успех")# все команды выполнены, так как удовлетворяет всем нормам и правилом.


if "6" > 5:
    print("успех")# ошибка, так как "6" это str ,а 5 это int несоизмеримы.

if [5, 6] > 5:
    print("успех")# ошибка, так как list и int несоизмеримы.

if "6" != 5:
    print("успех")# выполняется не смотря что разный тип данных ,но факт, что они неравны по типу и равенству!
