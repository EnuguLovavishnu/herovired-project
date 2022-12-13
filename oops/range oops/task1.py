number=int(input("enter the number:"))
sum=0
# x=range(6)
for i in range(number+1):
    sum+=i
    #sum=sum+i

print(f"sum of{number} numbers are:{sum}")
print(f"average of {number}numbers :{sum/number}")