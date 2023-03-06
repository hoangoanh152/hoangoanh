n=int(input("n="))
i=1
while n<1 or n>50:
    print("Nhap lai")
    n=int(input("n="))
while i<=n:
    if i%10==0:
        print(i,end="\n")
    else:
        print(i,end=' ')
    i=i+1