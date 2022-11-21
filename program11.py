""" Write a python script to take the month value in numeric format and display the
number of days in it."""

a=int(input("Enter a Month in numeric format:- "))

if a in (1,3,5,7,8,10,12):
    print("31 days")
elif(a==4 or a==6 or a==9 or a==11):
    print("30 days")
elif(a==2):
    print("28 days")