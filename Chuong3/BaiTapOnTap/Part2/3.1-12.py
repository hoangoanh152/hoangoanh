yrsOfService=int(input("yrsOfService ="))
Salary=int(input("Salary ="))
Bonus=int(input("Bonus ="))
if yrsOfService < 5:
    if Salary < 500:
        bonus =100
    else:
        bonus = 200
else: 
    bonus =700
print("Bonus amount: ", bonus)