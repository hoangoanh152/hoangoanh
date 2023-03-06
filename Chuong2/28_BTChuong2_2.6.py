a=str(input("Ho ten: "))
b=int(input("So ngay cong: "))
c=int(input("Don gia ngay cong:"))
d=float(input("He so phu cap: "))
e=int(input("Tam ung: "))
luong=c*b*d
thuclinh=luong - e 
print("Nhan vien",a, end=",")
print(" Co ten luong=",luong,sep="",end=",")
print("Tam ung=",e,sep="",end=" va ")
print("Thuc linh=",thuclinh,sep="")