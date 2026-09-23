n1 = int(input())  
list1 = [] #создание пустого списка
for i in range(n1): #создание списка от 1 до n
    list1.append(i + 1)
m1 = int(input())
list1 *= m1 #продление списка до максимальной мужной длинны
way1 = list1[::m1 - 1] #срез каждого (m - 1) члена списка
ball1 = 0 #номер порядка каждого члена массива
ballList1 = [] #создание второго пустого списка
for i in way1: #номерной порядок всех членов списка равных первому
    ball1 += 1
    if i == way1[0]:
        ballList1.append(ball1)
way1 = way1[:ballList1[1] - 1] #срез первого списка по второму повторному члену списка
n2 = int(input()) #повторегие всего того же самого, но со вторым массивом
list2 = []
for i in range(n2):
    list2.append(i + 1)
m2 = int(input())
list2 *= m2
way2 = list2[::m2 - 1]
ball2 = 0
ballList2 = []
for i in way2:
    ball2 += 1
    if i == way2[0]:
        ballList2.append(ball2)
way2 = way2[:ballList2[1] - 1]
print(way1 + way2)
