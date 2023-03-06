M1=float(input("M1="))
M2=float(input("M2="))
M3=float(input("M3="))
S=float(input("S="))
if 1<=S<=100:
    giatien=S*M1
elif S<=150:
    giatien=100*M1+(S-100)*M2
if 151<=S:
    giatien=100*M1+50*M2+(S-150)*M3
print("Phai tra=",round(giatien),sep="")