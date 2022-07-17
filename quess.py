import random


answer = []
test_string = []
test_n = 10 # длина тестовой строки
train_n = 20 # длина тренировочной строки
kekeys = ("000", "001", "010", "011", "100", "101", "110", "111") # сочетания 3 символов, состоящих из 0 и 1
counting_zeros = {"000": 0, "001": 0, "010": 0, "011": 0, "100": 0, "101": 0, "110": 0, "111": 0}
counting_ones = {"000": 0, "001": 0, "010": 0, "011": 0, "100": 0, "101": 0, "110": 0, "111": 0}
counting_prob_one = counting_ones.copy()
while len(answer) < train_n: # пользователь вводит данные, пока длина строки не будет равна n(20)
    print("\nВведите случайную строку, содержащую 0 или 1:")
    answer.extend(x for x in input() if x in "01") # выбираем из введенной строки только 0 и 1
    if len(answer) < train_n:
        print("Текущая длина данных равна {}, осталось {} символов".format(len(answer), train_n - len(answer)))
for x in range(len(answer)-3):
    current_three = "".join(answer[x:x+3])
    if answer[x+3] == "0":
        counting_zeros[current_three] += 1
    elif answer[x+3] == "1":
        counting_ones[current_three] += 1
ones_count = counting_ones.keys()
print("\nИтоговая строка:")
print("".join(answer))
for x in ones_count:
    zo_count = (counting_zeros[x] + counting_ones[x])
    if zo_count == 0:
        counting_prob_one[x] = counting_ones[x]
    else:
        counting_prob_one[x] = round(counting_ones[x] / zo_count, 2)
while len(test_string) < test_n:
    print("\nВведите тестовую строку, содержащую 0 или 1:")
    test_string.extend(x for x in input() if x in "01")
    if len(test_string) < test_n:
        print("Текущая длина данных равна {}, осталось {} символов".format(len(test_string), test_n - len(test_string)))
print("\nТестовая строка:")
print("".join(test_string))
print("\nПредсказание:")
prediction_string = random.choice(kekeys) # выбираем первые три символа случайно
for x in range(len(test_string) - 3):
    prediction_string += str(int(bool(round(counting_prob_one[prediction_string[x:x+3]]))))
print(prediction_string)
count_check = 0 # счетчик правильно угаданных символов
for x in range(len(test_string)):
    if test_string[x] == prediction_string[x]:
        count_check += 1
accuracy = round(count_check / len(test_string), 2) * 100 # считаем точность предсказанных символов
print("\nКомпьютер правильно угадал {} из {} символов ({} %)".format(count_check, len(test_string), accuracy))

