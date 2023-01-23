#Выполнить обработку элементов квадратной матрицы А, имеющецй N строк и N столбцов. 
#Найти сумму элементов, расположенных выше главной диагонали, и произведение элементов, 
#расположенных выше побочной диагонали.

import random

n = int(input ("Введите размер квадратной матрицы: "))

a = []
print("Матрица А :")

for i in range (n):
    temp = []
    for j in range (n):
        temp.append(random.randrange (1,5,1))
        print(temp[j] , end=' ')
    print()
    a.append(temp)

sUp = 0

for i in range (n):
    for j in range (n):
        if i<j:
            sUp += a[i][j]


mDown = 1
m=n-1
for i in range (n-1):
    for j in range (m):
        mDown = mDown * a[i][j]
    m -= 1

print ("Сумма элементов выше главной диагонали = ", sUp)
print ("произведение элементов ниже главной диагонали = ", mDown)
