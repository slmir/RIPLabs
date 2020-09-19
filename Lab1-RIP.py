import math
import sys

my_args = sys.argv
print(my_args)

#Объявление переменных
D,x1,x2,temp,flag,NotNumberA,NotNumberB,NotNumberC = 0,0,0,0,False,True,True,True

#Функция, проверяющая,является ли передаваемая строка числом
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

#Функция, выводящая решения биквадратного уравнения
def printKorni(bx1,bx2):
    print("Корни уравнения равны: ",bx1," и ",bx2)

print("Мирсонов Вячеслав Александрович, группа РТ5-51Б\n")

#Ввод коэффициента А и проверка на то, является ли он числом
#str1 = input("Введите коэффициент А: ")
while is_number(my_args[1]) == False:
    my_args[1] = input("Введенный вами коэффициент A некорректен. Введите коэффициент повторно: ")
    is_number(my_args[1])
if is_number(my_args[1]) == True:
    A = float(my_args[1])
    
#Ввод коэффициента B и проверка на то, является ли он числом
#str2 = input("Введите коэффициент В: ")
while is_number(my_args[2]) == False:
    my_args[2] = input("Введенный вами коэффициент B некорректен. Введите коэффициент повторно: ")
    is_number(my_args[2])
if is_number(my_args[2]) == True:
    B = float(my_args[2])

#Ввод коэффициента C и проверка на то, является ли он числом
#str3 = input("Введите коэффициент C: ")
while is_number(my_args[3]) == False:
    my_args[3] = input("Введенный вами коэффициент C некорректен. Введите коэффициент повторно: ")
    is_number(my_args[3])
if is_number(my_args[3]) == True:
    C = float(my_args[3])

if A == 0:
    if B !=0:
        temp = (-C)/B
        print("Корень уравнения равен: ",temp)
        flag = True
    elif C==0:
        print("Корень уравнения - любое число ")
        flag = True
else:
    if C<0 and B == 0:
        if A < 0:
            print("Уравнение не имеет действительных корней")
            flag = True
        else:
            temp = (-C)/A
            x1 = math.sqrt(temp)
            x2 = -x1
            printKorni(x1,x2)
            flag = True
    if flag == False:
        D = B*B - 4*A*C;
        if D<0:
            print("Уравнение не имеет действительных корней")
            flag = True
        if flag == False:
            x1 = (-B + math.sqrt(D))/(2*A)
            if abs(x1) == float(0):
                x1 = 0
            x2 = (-B - math.sqrt(D))/(2*A)
            if abs(x2) == float(0):
                x2 = 0
            if x1 == x2:
               print("Корень уравнения равен: ",x1)
               flag = True
            if flag ==False:
               printKorni(x1,x2)        

