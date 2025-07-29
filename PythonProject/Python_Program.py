# from numpy import int256
#
# x=8.7
# print(x)
# y = "Madhu"
# print(y)
# print("Hello world")
# print(type(2.6))
#
# a = "apple"
# print("I love",a)
#
# b = 25
# print(2+5)
#
# # C = Madhu
# # print(Madhu)
#
# # c = 10
# # d= 20
# # e =40
# c,d,e = 10,20,40
# print(c,d,e)
#
# f = 10
# f= f&7
# print(f)
#
# ##############################
# # print()
# h = input("Enter the name ")
# print(h)
# i =int(input("Enter the number "))
# print(i)
#
#
#
# num1_int
# num2_int
# add(num1+num2)
# print(input("enter the number: "))
from itertools import count

from selenium.common import ElementNotSelectableException

# name=(input("Enter your name: "))
# score=int(input("Enter your score: "))
# department=(input())
# print("My name is ",name)
# print("Enter your score: ",score)
# print("Enter your department: ",department)




# Input:
# Enter your name:
# Enter your id:
# Enter your score:
# Enter your Dept:
#
#
# Condition :
# score = 100
# divide /10 ex: 100/10
#
# output:
# My name is
# My id is
# My score is " " /10
# My dept is
#
#
#
# My name is Madhu
# My id is 101
# My score is 8 /10
# My dept is BSC




score = 30
if score>=70:
    print("Topper")

elif score<=30:
    print("Poor")


# status=input(Died)
# meghna_status = input("Enter the meghna status: ")
# meghna_status = "Died"
# if meghna_status=="Died":
#     print("Suriya meets priya")
# else:
#     print("Suriya weds Meghna")


a= "sangeetha vani madhu madhu madhu"
print(a[0:9])
print(a[:])
print(a[::-1])
print(a[0:9:2])
print(a[5:9])
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip())
print(a.capitalize())
print(a.title())
print(a.split(" "))
print(a.count("madhu"))
print(a.replace("madhu", "Python"))
# print(a[13])
# print(a[-1])
#
for i in range(1,11):
    j = i * 2
    print(i,"* 2 = ",j)

# a= int(input("Enter the number a:"))
# b = int(input("Enter the number b:"))
# for i in range(a+1,b):
#     print(i)

# for i in range(1,11):
#     if i%2== 0:
#         print(i)
e_count=0
o_count=0
for i in range (1,10):
    if i%2== 0:
        e_count= e_count+1
    else:
        o_count =o_count + 1
print("Even ", e_count)
print("Odd", o_count)

# count=0
# for i in range(1,100):
#     if i%3 ==0 and i%5==0:
#         count = count+1
# print(count)


sum = 0
for i in range(1,6):
    sum = sum+i
print(sum)

# sum =0
# for i in range(1,11):
#     value = int(input("Enter the value"))
#     sum = sum+value
#     print(sum)
#
# print("sum:",sum)
# print("avg",sum/10)

# a=[]
# for i in range(1,4):
#     int(input("Enter the value"))
#     a.append(i)
# print(a)
#
# i=10
# while(i>0):
#     print(i, end=",")
#     i=i-1


# i=3
# fact = 1
# while(i>0):
#     fact = fact*i
#     i = i-1
# print(fact)
#
# total = 0
# # loop will run at least once
# while True:
#     # ask the user to enter a number
#     num = int(input("Enter a number (or 0 to exit): "))
#
#     # exit the loop if the user enters 0
#     if num == 0:
#         break
#     total += num
#
# # print the total
# print("Total:", total)

count_ev =0
count_od =0
for madhu in range(1,10):
    if (madhu %2==0):
        count_ev= count_ev+1
    elif(madhu %2!=0):
        count_od= count_od+1
print("even=",count_ev)
print("odd=",count_od)

# sum=0
# for madhu in range(10):
#     if(madhu %2==0):
#         sum=sum+1
# print("sum= ",sum)
#
# for i in range(1,5):
#     print()
#     for j in range(i):
#         print(j+1, end="")


# for i in range(1,6):
#     print(i, "Mango")
#     for j in range(1,4):
#         print(j,"Apple")




# i = 1
# while(i<6):
#     print(i)
#     i = i+1



# i = 5
# fact = 1
# while(i>0):
#     fact = fact*i
#     i = i-1
#
# print(fact)

# i = int(input())
# for i in range(i):
#      print()
#      for j in range(i):
#         print(j)





fruits = ["apple", "orange", "cherry", "apple", "mango"]
print(fruits)
print(fruits[-1])
print(fruits[0:3])
# fruits[0] = "blueberry"
# print(fruits)
fruits.append("bed")
print(fruits)
fruits.remove("apple")
print(fruits)

#
a = [1,2,3,4]
b= set(a)
print(b)
print(type(b))


# fruits = {"apple", "orange", "cherry", "apple"}
# print(fruits)
# fruits.remove("banana")
# print(fruits)
# fruits.discard("banana")
# print(fruits)

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5}
# difference_set = set_b.difference(set_a)
# print(difference_set)


# student = {
# 1: "Class-X",
# "name": "Madhav",
# "age": 20
# }
# student["name"] = "Madhu"
# print(student)

# a = "Sangeethavani Subramanian"
# print(a[::-1])

# b = "madam"
# print(b)
# b1 = b[::-1]
# print(b1)
# if b == b1:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# a = ["apple","orange","mango",8,86]
# for i in a:
#     print(i)
#
# a = ["apple","orange","mango",8,86]
#
# for i in range (len(a)):
#     if i ==3:
#         continue
#     print(a[i])


# a = ["apple","orange","mango",8,86]
#
# i =0
# while(i<len(a)):
#     print(a[i])
#     i=i+1


# a = {'a': 1, 'b': 2, 'c': 3}
# print("\nDictionary elements (key and value):")
# for i in a:
#     print(f"Key: {i}, Value: {a[i]}")

# a = ["apple","orange","mango",8,86]
# if "apple1" not in a:
#     print("apple")


# def addition(a,b):
#     print(a+b)
#
#
# addition(5,7)
# addition(8,7)
# addition(9,7)
# addition(54,7)
#
# def sub(a,b):
#     print(a-b)
# sub(2,7)


# def greet(name= "bob"):
#     print("Hello,", name)
#
# greet("Alice")
# greet()
#
#
# def add(a, b):
#     return a*b
#
# result = add(9, 3)
# result1 = add(7,9)
# print(result)
# print(result1)




# class Car:
#     # properties
#     brand = "BMW"
#     color = ""
#
#     # method
#     def start(self):
#         print("Car started")

    # create an object of Car class
# my_car = Car()
# my_car.brand = ""
# my_car.color = "Red"
#
# print(my_car.brand)  # Output: Toyota
# my_car.start()


# Parent class
# class Vehicle:
#     def move(self):
#         print("Vehicle is moving")
#
# # Child class
# class Car(Vehicle):
#     def start(self):
#         print("Car started")
#
# my_car = Car()
# # my_car.move()   # Output: Vehicle is moving
# my_car.start()



# class Vehicle:
#     def fuel_type(self):
#         print("Some fuel")
#
# class Car(Vehicle):
#     def fuel_type(self):
#         print("Petrol or Diesel")
#
# class ElectricCar(Vehicle):
#     def fuel_type(self):
#         print("Electric Battery")
#
# vehicles = [Car(), ElectricCar(), Vehicle()]
#
# for v in vehicles:
#     v.fuel_type()


from abc import ABC, abstractmethod

# class Vehicle(ABC):  # Abstract class
#     @abstractmethod
#     def start(self):
#         print("Car Start")
#
#     @abstractmethod
#     def stop(self):
#         print("Car stop")
#
# class Car(Vehicle):
#     def start(self):
#         print("Car started with key")
#
#     def stop(self):
#         print("Car stopped using brake")
#
# # Usage
# my_car = Car()
# my_car.start()
# my_car.stop()
#
#

# n = int(input())
# list_values = map(int, input().split())
# L1 = list(set(list_values))
# L1.sort(reverse = True)
# l2 = L1[1]
#
# print(l2)


# n = int(input())
# l1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# l1.sort(reverse = False)
# print(l1)
# if l1[0][1]>l1[1][1] and l1[1][1] == l1[2][1]:
#     print(l1[1][0])
#     print(l1[2][0])
# elif l1[1][1] == l1[2][1]:
#             print(l1[1][0])


# a =6
# b =''
# print(a/b)
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2  # Might raise ZeroDivisionError
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Please enter valid numbers!")
# finally:
#     print("This block always runs. Clean up done.")

# import pandas as pd
#
# # Read input Excel file
# input_file = 'C:/Users/YourName/Documents/input.xlsx'
# # input_file = 'input.xlsx'   # your source Excel file
# df = pd.read_excel(input_file)
#
# # Do any processing here (optional)
# # For now, just returning same data
#
# # Write to output Excel file
# output_file = 'C:/Users/YourName/Documents/output.xlsx'
# # output_file = 'output.xlsx'
# df.to_excel(output_file, index=False)
#
# print(f"Data copied from {input_file} to {output_file} successfully.")


# class Student:
#     def __init__(self, name, age):
#         self.name = name  # instance variable
#         self.age = age    # instance variable
#
#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
# name = input()
# age = int(input())
# # Create an object of Student
# student1 = Student(name,age)
#
# # Call the method to display details
# student1.display_details()

# file = open("sample.txt", 'r')
# content = file.read()
# print(file.tell())
# # file.seek(0)
# content1 = file.readline()
#
# # content2 = file.readlines()
# print(content)
# print(content1)
# # print(content2)
# file.close()


# with open("sample.txt", "w+") as file:
#     file.writelines("Hi Hi Hi I like apple orange mango")
#
#     file.seek(0)
#     content = file.readlines()
#     print(content)

# Open the file in write mode
# with open("sample.txt", "w") as file:
#     file.write("This is line one.\n")
#     file.write("This is line two.\n")
#     file.write("This is line three.\n")
#
# # Read it back to see the output
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print("Output using write():")
#     print(content)

# Open the file in write mode
# with open("sample.txt", "w") as file:
#     lines = [
#         "Apple is red.\n",
#         "Banana is yellow.\n",
#         "Mango is sweet.\n"
#     ]
#     file.writelines(lines)
#
# # Read it back to see the output
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print("Output using writelines():")
#     print(content)



