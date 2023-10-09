# Задача "Ряд - 1"
#a = 10
#b = 29
#for i in range(a, b+1):
#    print(i)





#Задача "Ряд - 2"
#a = int(input("a = "))
#b = int(input("b = "))
#if(a < b):
#    for i in range(a, b+1):
#        print(i)
#elif(a > b):
#    for i in range(a, b - 1, -1):
#        print(i)





# Задача "Сумма N чисел"
#n_digits = int(input("Введите количество чисел: "))
#sum = 0
#for i in range(n_digits):
#    sum += int(input("Введите число: "))
#print(sum)





#Задача "Факториал"
#userDigit = int(input("Введите число: "))
#factorial = 1
#for i in range(1, userDigit+1):
#    factorial *= i
#print(f'Факториал числа {userDigit} = {factorial}')






#Задача "Лесенка"











# Задача "Список квадратов"
# userDigit = int(input("Введите целое натуральное число: "))
# for i in range(2, userDigit):
#    if(i ** 2 < userDigit):
#       print(i ** 2)





# Задача "Степень двойки"
#userDigit = int(input("Введите число: "))
#degree = 0
#degreeValue = 2
#pastValue = 0
#while(degreeValue < userDigit):
#    pastValue = degreeValue
#    degreeValue *= 2
#    degree += 1
#else:
#    print(f'Показатель степени: {pastValue}, Степень: {degree}')





#Задача "Утренняя пробежка"
#x = int(input("Введите x километров в первый день: "))
#y = int(input("Введите у километры: "))
#days = 0
#while(x < y):
#    x += x * 0.1
#    days +=1
#else:
#    print(f'День, на который пробег спортсмена составляет не менее у километров: {days}')





#Задача "Длина последовательности"
#userDigit = int(input("Введите целое неотрицательное число: "))
#count = 0
#while(userDigit != 0):
#    userDigit = int(input("Введите целое неотрицательное число: "))
#    count += 1
#else:
#    print(f'Количество членов последовательности: {count}')





#Задача "Количество элементов, которые больше предыдущего"






#Задача "Второй максимум"






#Задача "Числа Фибоначчи"





#Задача "Максимальное число идущих подряд равных элементов"





#Задача "Четные индексы"
#array = ["a", "b", "c", "d", "e", "f"]
#for i in range(len(array)):
#    if(i % 2 == 0):
#        print(array[i])





#Задача "Больше предыдущего"
#array = [1,5,1,43,2,3,44,6,1,2,5,23,5]
#for i in range(len(array)):
#    if(i < len(array) - 1):
#        if(array[i] < array[i+1]):
#            print(array[i+1])





#Задача "Наибольший элемент"
#array = [4,12,5,1,2,5,4,32,2,45,65,1,2,43,4,5,31,2]
#currentMaxDigit = 0
#for i in range(len(array)):
#    if(array[i] > currentMaxDigit):
#        currentMaxDigit = array[i]
#print(f'Наибольший элемент под индексом {array.index(currentMaxDigit)}')





#Задача "Шеренга"






#Задача "Переставить соседние"
# array = ["a", "b", "c", "d", "e", "f", "g", "h"]
# fresh_array = []
# i = 0
# while(i < len(array)):
#     if(len(array) % 2 != 0):
#         if(i == len(array) - 1):
#             fresh_array.append(array[i])
#             break
#         else:
#             fresh_array.append(array[i+1])
#             fresh_array.append(array[i])
#         i += 2
#     else:
#         if(i == len(array) - 1):
#            break
#         else:
#             fresh_array.append(array[i+1])
#             fresh_array.append(array[i])
#         i += 2
    
# print(array)
# print(fresh_array)





#Задача "Переставить min и max"
# array = [45,4,212,5,42,313,5325,3,52,0]
# print(f'Изначальный массив: {array}')
# minDigit = min(array)
# maxDigit = max(array)
# minDigitIndex = array.index(minDigit)
# maxDigitIndex = array.index(maxDigit)
# array[minDigitIndex] = maxDigit
# array[maxDigitIndex] = minDigit
# print(f'Новый массив: {array}')





#Задача "Удалить элемент"
# array = [1,2,3,4,5,6,7,8]
# print(array)
# k = 3
# array.pop(k)
# array.pop()
# print(array)






#Задача "Вставить элемент"
# array = [1,5,32,1224,2]
# k = 3
# c = "ABBA"
# array.insert(k,c)
# array.append(952)
# print(array)





#Задача "Ферзи"
# arrayOfCorrectLocation = [
#     {
#         "Diagonal": 2,
#         "Horizontal": 2
#     },
#     {
#         "Diagonal": 1,
#         "Horizontal": 4
#     },
#     {
#         "Diagonal": 4,
#         "Horizontal": 5
#     },
#     {
#         "Diagonal": 3,
#         "Horizontal": 8
#     },
#     {
#         "Diagonal": 6,
#         "Horizontal": 1
#     },
#     {
#         "Diagonal": 7,
#         "Horizontal": 3
#     },
#     {
#         "Diagonal": 5,
#         "Horizontal": 7
#     },
#     {
#         "Diagonal": 8,
#         "Horizontal": 6
#     }
# ]
# print(arrayOfCorrectLocation)
# count = 0
# for i in range(8):
#     userDiagonal = int(input("Введите номер по ДИАГОНАЛИ: "))
#     userHorizontal = int(input("Введите номер по ГОРИЗОНТАЛИ: "))
#     for a in range(8):
#         if((arrayOfCorrectLocation[a].get("Diagonal")) == userDiagonal) and ((arrayOfCorrectLocation[a].get("Horizontal")) == userHorizontal):
#             print("DA")
#             count += 1
# if(count == 8):
#     print("NO")
# else:
#     print("YES")
