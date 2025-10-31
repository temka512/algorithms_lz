import random
l = []
d = []
k=0
while len(l)<100: #заполняем список 100 элементами без дублей
    a= random.randint(0,1000000)
    if a not in l : 
        l.append(a)
d=sorted(l)
print(d)
n=int(input('Введите искомое число: ')) #запрашиваем ввод числа
for i in range(len(d)): #выполняем линейный поиск
    if n == d[i]:
        print('Количество сравнений в линейном поиске: ',i)
        print('Индекс искомого элемента: ', i)
        
low = 0
high = len(d) - 1
mid = len(d) // 2
while d[mid] != n and low <= high: #выполняем бинарный поиск
    if n > d[mid]:
        low = mid + 1
    else:
        high = mid - 1
    k += 1
    mid = (low + high) // 2

if low > high:
    print('Введенного элемента в списке нет')
else:
    print('Количество сравнений в бинарном поиске: ', k)    

