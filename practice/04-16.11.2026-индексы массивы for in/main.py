
#  Маршрут с остановками

stops = [input("Остановка 1: "), input("Остановка 2: "), input("Остановка 3: "), input("Остановка 2: ")]

for number, name in enumerate(stops, start =1):
    if number == len(stops):
        print(f"{number}. {name} (конечная)")
    else:
        print(f"{number}. {name}")


# Дни похолодания


temperatures = [int(input("День 1: ")),int(input("День 2: ")),int(input("День 3: ")),
                int(input("День 4: ")),int(input("День 5: ")),int(input("День 6: ")),]

count = 0
for index in range(1, len(temperatures)):
    drop = temperatures[index - 1] - temperatures[index]
    if drop >= 5:
        print("Похолодание в день", index + 1)
        count += 1
print("Всего дней:", count)

# Снижение цен

prices = [int(input("Цена 1: ")),int(input("Цена 2: ")),int(input("Цена 3: ")),int(input("Цена 4: ")),int(input("Цена 5: ")),]


for index in range(len(prices)):
    if prices[index] > 500:
        prices[index] -= 50
print(prices)





# Общие свободные часы

first = [int(input("Первый, час 1: ")),int(input("Первый, час 2: ")),int(input("Первый, час 3: ")),]
second = [int(input("Второй, час 1: ")),int(input("Второй, час 2: ")),int(input("Второй, час 3: ")),]

common = 0
for left in first:
    for right in second:
        if left == right:
            print("Общий час:",left)
            common += 1
print("Всего общих часов:", common)
