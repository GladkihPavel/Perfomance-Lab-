hkab = input()
xy = input()
with open(hkab, 'r', encoding='utf-8') as first:
    with open(xy, 'r', encoding='utf-8') as second:
        alllines = second.readlines()
        hk = first.readline()
        ab = first.readline()
        h = float(hk[0])   #координата центра
        k = float(hk[2])   #координата центра
        a = float(ab[0])   #координата радиуса
        b = float(ab[2])   #координата радиуса
        x = []  #пустой массив 1
        y = []  #пустой массив 2
        for i in range(len(alllines)):  #заполнение пустых масиивов значениями x и y для каждой точки
            x.append(float(alllines[i][0]))
            y.append(float(alllines[i][2]))
        for i in range(len(x)):
            if ((x[i] - h) ** 2) / (a ** 2) + ((y[i] - k) ** 2) / (b ** 2) == 1: # формула эллипса
                print(i, "- точка лежит на окружности")
            elif ((x[i] - h) ** 2) / (a ** 2) + ((y[i] - k) ** 2) / (b ** 2) > 1:
                print(i, "- точка снаружи")
            else:
                print(i, "- точка внутри")
