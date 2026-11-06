#Q1 Write a Python program to check if a number is positive----------->
num=int(input("Enter a number: "))
if num>0 :
    print("number is positive")
elif num <0 :
        print("number is negative")
else :
    print("number is Zero")

#Q2 Print "Eligible to vote" if age is 18 or above--------------->
age=int(input("Enter your age: "))
if age>=18 :
    print("You Eligible to vote")
else :
        print("not eligible for vote")

# Q3Check if a number is divisible by 7------------------------------->
num = int(input("Enter a number: "))

if num % 7 == 0:
    print(num, "is divisible by 7")
else:
    print(num, "is not divisible by 7")

#Q4 Print "Pass" if marks are greater than 40--------------------------->
marks = int(input("Enter marks: "))
if marks >=40 :
    print("Pass")
else :
    print("Fail")

#Q5 Check if a number is greater than 100--------------------------------->
num = int(input("Enter a number: "))
if num > 100 :
 print("A number is greater than 100")
else :
    print("A number is less than 100")

#Q6 Print "Logged In" if password matches "admin123"---------------------->
password=input("Enter a password: ")
if password == "admin123" :
    print("Logged in ")
else :
    print("Logged in failed ")

#Q7 Print a warning if balance is below minimum limit--------------->
balance=int(input("Enter balance :"))
if (balance<=2000) :
    print("balance is below minimum limit")
else :
    print("balance is above minimum limit")

#Q8 Check whether a number is even or odd--------------------->
num=int(input("Enter a number: "))
if num%2==0 :
    print("The number is even")
else:
    print("The number is odd")

#Q9 Find the largest of two numbers--------------------->
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
if a>b :
    print(a,"largest of two number")
else :
    print(b,"largest of two number")

#Q9 Check whether a number is positive or negative--------------->
number=int(input("Enter a number: "))
if number>0 :
    print("The number is positive")
else :
    print("The number is negative")

#Q10 Check whether a character is a vowel or consonant---------------->
alphabets=(input("Enter the alphabets: "))
if alphabets=="a":
    print("vowel: ")
elif alphabets=="e" :
    print("vowel: ")
elif alphabets=="i" :
    print("vowel: ")
elif alphabets=="o" :
    print("vowel: ")
elif alphabets=="u" :
    print("vowel: ")
else :
   print("Consonant")

#Q11 Check if a year is leap or not------------->
year =int(input("Enter a year :"))
if (year % 100==0) :
    print("leap year :")
elif (year % 4==0) :
    print("leap year :")
elif (year % 400==0) :
    print("leap year :")
else :
    print("not leap year :")

#Q12 Print "Valid Password" or "Invalid Password---------->
password=(input("Enter password : "))

if password == "abcde" :
    print("Valid Password")
else:
    print("Invalid Password")

#Q13 Check whether a number is greater than 50 or not--------->
number=int(input("Enter a number: "))
if number>50 :
    print("The number is greater than 50")
else :
    print("The number is less than 50")

#Q14 Find the largest of three numbers------------>
a=int(input("Enter a number: "))
b=int(input("Enter b number: "))
c=int(input("Enter c number: "))

if a>b:
    print(a," is greater of three number :")
elif b>c:
    print(b," is greater of three number :")
else:
    print(c," is greater of three number :")

#Q15 Find the largest of three numbers------------>
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

if a >= b and a >= c:
    print(a, "is greater of three numbers")

elif b >= a and b >= c:
    print(b, "is greater of three numbers")

else:
    print(c, "is greater of three numbers")

#Q16 Check whether a number is positive, negative, or zero------------------------->
numbers = int(input("Enter a number: "))

if numbers>0 :
    print("The number is positive :")
elif numbers<0 :
    print("The number is negative :")
else :
    print("The number is zero :")

#Q17  Check whether a character is a vowel or consonant----------->
ch=str(input("Enter a character:"))

if ch=="a" or ch=="A":
    print("This is a vowel :")
elif ch=="e" or ch=="E" :
    print("This is a vowel  :")
elif ch=="i" or ch=="I" :
    print("This is a vowel  :")
elif ch=="o" or ch=="O" :
    print("This is a vowel  :")
elif ch=="u" or ch=="U" :
    print("This is a vowel")

else :
 print("This is a consonent")

#Q18  Check if a year is leap or not---------->
year=int(input("Enter Year :"))

if year%4==0 and year%100!=0 or year%400==0 :
    print("Leap year :",year )
else :
    print("Not Leap year :",year)

#Q18 Print "Valid Password" or "Invalid Password---------->
password=str(input("Enter Password:"))
if password=="abcd":
    print("Password is correct")
else :
    print("Password is incorrect")

#Q19 Determine whether salary is taxable or not---------->
tax=int(input("Enter your Tax :"))

if tax <= 700000 :
    print("Salary is not taxable :",tax)
else :
    print("Salary is taxable:",tax)

#Q20 Check whether a number is greater than 50 or not-------->
n=int(input("Enter Number:"))

if n<=50 :
    print("The number is less than 50")
else :
    print("The number is greater than 50")

