x=float(input("x="))
y=float(input("y="))
ch=str(input("Phep toan:"))
if ch=="+":
    a=x+y 
    print(x,"+",y,"=",x+y,sep="")
elif ch=="-":
    a=x-y
    print(x,"-",y,"=",x-y,sep="")
elif ch=="*":
    a=x*y
    print(x,"*",y,"=",x*y,sep="")
elif ch=="/" and y!=0:
    a=x/y
    print(x,"/",y,"=",x/y,sep="")
else:
    print("Khong hop le ")