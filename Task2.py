#Выполнить обработку элементов прямоугольной матрицы А, имеющий N строк и M столбцов. 
#Разделить элементы матрицы на элемент матрицы с наибольшим значением 

import random

m = int(input ("Введите число строк: "))
n = int(input ("Введите число столбцов: "))

a = []
print("Матрица А :")

for i in range (m):
    temp = []
    for j in range (n):
        temp.append(random.randrange (-20,20,1))
        print(temp[j] , end=' ')
    print()
    a.append(temp)


imax = 0
jmax = 0

for i in range (m):
    for j in range (n):
        if a[i][j]>a[imax][jmax]:
            imax = i
            jmax = j

print("Максимальный элемент - a(",imax+1,",",jmax+1,") = ", a[imax][jmax])

print()
print("Измененная матрица:")
for i in range (m):
    for j in range (n):
        a[i][j]=a[i][j]/a[imax][jmax]
        print(a[i][j], end = " ")
    print()
