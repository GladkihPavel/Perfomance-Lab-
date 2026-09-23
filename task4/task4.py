with open("tusk4.txt") as t:
    whitelist = t.readlines() #чтение файла
    list = [] #оздание списка
    for i in range(len(whitelist)): #запосление списка числами
        list.append(int(whitelist[i][0]))
max = max(list)
min = min(list)
torns = [] #лист с разными решениями
for i in range(min, max + 1): #перебор всех возможных решений
    torns.append(0)
    for u in range(len(list)):
        if list[u] > i: #сравнение числа из списка с приведенным
            torns[i - min] += list[u] - i #добавление ходов
        else:
            torns[i-min] += i - list[u] #добавление ходов(в случае с i = list[u] добавления не происходит)
    if torns[i - min] < torns[0]:  #замена первого члена листа с решениями на наименьшее значение
        torns[0] = torns[i - min]
print(torns[0])
