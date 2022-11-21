"""Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""

a,b,c=int(input("Enter a Number:- ")),int(input("Enter second Number:- ")),int(input("enter a third Number:- "))
if(a==b==c):{
  print(a," Number is same")
}
elif(a>b and a>c):{
    print(a,"is greater")
}
elif(b>a and b>c):{
  print(b,"is greater")
}
else:{
  print(c,"is grater")
}