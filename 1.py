lst = [1, 2, 3, 4, 5, 2, 6]
def myfunc(x):
    for i in x: #перебераем список
        if i % 2 == 0:
            x.remove(i) #удаляем позицию из списка
        print(x)

myfunc(lst)
