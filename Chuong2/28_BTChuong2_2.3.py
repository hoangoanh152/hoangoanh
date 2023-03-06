import math
print("Nhap hai canh ke cua tam giac vuong:")
a=int(input("Canh ke thu nhat la: "))
b=int(input("Canh ke thu hai: "))
x=math.sqrt(a**2+b**2)
print("Canh thu nhat la:",a,end=",")
print(" canh ke thu hai:",b,end=",")
print(" co canh huyen=",round(x,2))