# Write a python script to check whether a given year is a leap year or not.

a=int(input("Enter any Year:- "))
if(a%400==0):{
  print(a,"is leap Year")
}
elif(a%4==0 and a%100!=0):{
  print(a,"is leap Year")
}
else:{
  print(a,"is not leap Year")
}