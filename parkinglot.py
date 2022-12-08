# noOfCars=0
# noOfBikes=0
# totalPayment=0
# noOfCars=int(input("No of cars"))
# noOfBike=int(input("No of Bikes"))
# totalPayment=noOfBikes*20+noOfCars*40
# print("total payment would be",totalPayment)
# students=['rahul','ram','raj','ravi']
# print('the student names are:')
# for i in students:
#     print(i)

# using the list
# l=[1,2,3.5,4.5,'aditya',True]
# print(l)
# print(l[4])
# print(l[1:3])# include 1 and exclude 3
# print(l[1:5])
# print(l[2:])
# print(l*2)
# l1=['srujan','sai kumar']
# print(l+l1)
# print(l1+l)

# t=(1,2,3.5,4.5,'aditya',True)
# print(t[0])
# print(t[1:4])
# # print(t[2:1])
# details={'ram':90,'rahul':80}
# print(details)
# print(details.values())
# print(details.keys())
# details[4]="test"
# print(details[4])
# print(details)
# dict={
#     "college":"aditya",
#     "location":"andhra pradesh",
#     "Stream":"ECE"
# }
# for info in dict:
#     print(info)
# for info1 in dict:
#     print(dict[info1])
# name=input("enter the college:")
# rollno=input("enter the rollno:")
# college1={name:rollno}
# print(college1)
import functools
def comp(x,y):
    if(x[1]>y[1]):return 1
    else:return -1
A=[[1,2],[5,6]]