#print hello world
print("hello world ")

#print youe name ,age ,city
name="John"
age= 50
city="Serbia"
print(name,age,city)

#Take user input and print it
user1=input("enter the number")
user2=input("enter your data")
print(user1,user2)

#Add two numbers entered by user
num1=int(input("enter your  first number"))
num2=int(input("enter you second number"))
sum= num1+num2
print(sum)

# Print multiple lines using single print statement
print("My name is John\nI live in Serbia\nI love to read chili mili")
# Print data type of a variable

a=12
b="4"
print(type(a))
print(type(b))

# Assign multiple variables in one line
a,b,c=1,2,3
print(a,b,c)

#Swap two variables
a=10
b=20
a,b=b,a
print("after swapping a",a)
print("b is",b)

#check python version 
import sys
print("python version\n",sys.version)
