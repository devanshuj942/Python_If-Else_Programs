# 1)Find Maximum Out Of 2 Numbers.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1>num2:
  print(num1,"is Greater than",num2)
else:
  print(num2,"is Greater than",num1)
  
  
# 2)Find Minimum Out Of 2 Numbers.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1<num2:
  print(num1,"is Smaller than",num2)
else:
  print(num2,"is Smaller than",num1)
  
  
  # 3)Find Leap Year From Given Year.
  
  year=int(input("Enter the year: "))
if year%4==0:
  print(year,"is a leap year")
else:
  print(year,"is not a leap year")


# 4)Find Odd/Even Number.

num=int(input("Enter a Number:"))
if num%2==0:
  print(num,"is an even number")
else:
  print(num,"is an odd number")
  
  
# 5)Find Positive/Negative Number.

num=int(input("Enter a Number:"))
if num>0:
  print(num,"is a positive number")
elif num==0:
  print(num,"is neither positive nor negative")
else:
  print(num,"is a negative number")
  
  
# 6) Find Maximum Among 3 Numbers.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if num1>num2 and num1>num3:
  print(num1,"is the greatest number")
elif num2>num1 and num2>num3:
  print(num2,"is the greatest number")
elif num3>num1 and num3>num2:
  print(num3,"is the greatest number")
else:
  print("All the numbers are equal or invalid! Please try again")
  
  
# 7)Find Interest Rate Based On Given Age.


age=int(input("Enter your age: "))
balance=int(input("Enter your bank balance: "))

if age>60 and balance>50000:
  print("The Interest Rate is 10%.")
elif age>=60 and balance<50000:
  print("The Interest Rate is 7%.")
elif age<60:
  print("The Interest Rate is 5%.")
else:
  print("Invalid Input! Please try again.")   
  
  
# 8)Find If Student Is Pass Or Fail?  

marks=float(input("Enter your marks: "))

if marks>80 or marks<0:
  print("Invalid Input! Please try again.")
elif marks>=70:
  print("You got Distinction.")
elif marks>=60 and marks<=69:
  print("You got First Class.")
elif marks>=45 and marks<=59:
  print("You got Second Class.")
elif marks>=35 and marks<=44:
  print("You Passed.")
else:
  print("You Failed.")

  