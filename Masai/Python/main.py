# Printing string(Hello world);
# print("Hello, World!")

# Defining Variables;
# name = "Rahim Ansari"
# age = 19
# is_Maried = False

# Changing value of same variable's name
# name = "Ahil"
# age = 19.0

# print(name,age,is_Maried)

# Task 
# Add a person with name "Tony Stark", Tony's age is 51 years old, Tony is a genius

# name = str("Tony Stark")
# tony_age = 51
# is_genius = True

# print(name,tony_age,is_genius)


# Taking input from user

# name = input("What is your name? :")
# print("Hello " + name)


# Task
# Tony is Secretly a superhero. Ask him for his superhero name & show it on the terminal

# superhero_name = input("Who is your Superhero? :")
# print(superhero_name)


# Type conversion
# int() -->> integer

# old_age = input("Enter your old age :")
# new_age = int(old_age) + 2
# print("Your new age is: ", new_age)


# Printing sum of 2 numbers

# first_number = input("Enter first number : ")
# second_number = input("Enter Second number : ")
# sum = int(first_number) + int(second_number)
# print("Sum of numbers is : ", sum)


# ------------>>>>>   STRING    -------->>>>>>>>

# name = "Tony Stark"
# print(name.upper())
# print(name.lower())
# print(name.find("Stark"))  # Will return index(5) of S in the "Tony Stark"
# print(name.replace("Tony Stark", "Ironmane")) # Will replace the value of name("TOny Stark") with "Ironman";
# print(name.replace("Stark", "Ironman"))
# print(name.replace("T","M"))
# print(name)

# print("T" in name) #will check if T is available inside the name if yes then it will return True else False
# print("Stark" in name)
# print("s" in name)





# ------->>>>>>>>    Arithmetic operators      -------->>>>>>>>>>>>>

# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2)
# print(5//2)  # this is print only those number which are before .(point), 5/2=2.5 -> it will print 2 only

# print( 5 % 2)
# print( 5 ** 2)

# i = 5
# i = i + 2
# i += 2
# i -= 2
# i *= 2
# i /= 2




#  ------------->>>>>   Comparison Operators   --------->>>>>>>>>>>>>>>


# print(3 > 2)
# print( 3 < 2)
# print( 3 <= 2)
# print(3 == 2)
# print(3 == 3)
# print(3 != 2)



# --------->>>>>> Logical Operators   ------------>>>>>>>>>>

# # or operator
# print(2 > 3 or 2 > 1)

# # and operator
# print(3 > 2 and 2 < 1)

# # not operator
# print(3 > 2)
# print(not 3 > 2)



#   if-else statement

# age = 16
# if age >= 18:
#     print("You are an adult")
#     print("You can drive")
# elif age < 18 and age > 3:
#     print("You are in school")
# else: 
#     print("You are a child")    



# print("Thank You")    


# Mini project

# first_number = input("Enter First number: ")
# operator = input("Enter operator(+,-,*,/,%) : ")
# second_number = input("Enter second number : ")

# first_number = int(first_number)
# second_number = int(second_number)

# if operator == "+":
#     print(first_number+second_number)
# elif operator == "-":
#     print(first_number-second_number)
# elif operator == "*":
#     print(first_number*second_number)
# elif operator == "/":
#     print(first_number/second_number)
# elif operator == "%":
#     print(first_number%second_number)
# else : 
#     print("Invalid Operations")        





#   ------------>>>>>>>>   Range   ------------>>>>>>

# numbers = range(5) # 0,1,2,3,4,5
# print(numbers)




# ------------->>>>>>>>>   LOOPS   ------------------>>>>>>>>>

# WHILE LOOP
# i = 1
# while i <= 5:
#     print(i)
#     i+=1


# j = 1
# while j <= 5:
#     print(j* "*")
#     j+=1


# k = 1
# while k <= 10:
#     if k%2 == 0:
#         print(k)
#     elif k == 10:
#         print(k)    
#     k+=1        




#  FOR LOOP

# for items in range(5):
#     print(items)



# ----------->>>>>>>>>  ARRAY   ----------->>>>>>>>>>

# marks = [95,78,77, "maths"]
# print(marks)
# print(marks[0],marks[2])
# print(marks[-1])  # Print the last item
# print(marks[-2]) # Print the secod last item
# print(marks[0:2]) # 0:2 is the indexes from 0 to 1, it will print all the items between 0 to 1 indexes
# print(marks[1:3])

# for score in marks:
#     print("Score is :",score)


# # push function --->>>> append function
# marks.append(99)
# print(marks)

# # shift function --->>>>  insert(index, value)

# marks.insert(0,  19)
# marks.insert(2, 17)
# print(marks) 

# print(99 in marks) # True


# print(len(marks))  # return the length of the array


# # Printing all the value of array using while loop
# i = 0
# while i < len(marks):
#     print(marks[i])
#     i+=1

# # Printing all the value of array using FOR loop
# for i in range(len(marks)):
#     print("FOR loop:",marks[i])


# # Clear the array

# marks.clear()
# print(marks)    #--->>>  []

#------------------->>>>>>> Break and Continue keywords     -------------->>>>>>>>>>>

# students = ["name1","name2","name3","name4","name5"]

# for i in students:
#     if i == "name4":
#         break;
#     print(i)

# for i in range(len(students)):
#     if students[i] == "name4":
#         continue;
#     print(students[i])





# ------------>>>>>>>>>>   Tupple   -------------------->>>>>>>>>>>>

# Tupples are immutable we cant do such operation like insertion, append and those kinds of operation
# marks = (71,78,98,89,90,90,990,90)

# #  2 operation that can done on tupples

# print(marks.count(90))  # will count how many times 90 appears in marsk

# print(marks.index(98)) # will print the index of 98



#--------->>>>>>>>> SETS   ------------>>>>>>

# marks = {9,8,4,5,3,2,00,1,9,9,9}
# print(marks)

# for score in marks:
#     print(score)
 

# --------------->>>>>>>>   OBJECTS  --------------->>>>>>>>>>>>>
# marks = {"english":90,"Math" : 91, "Chemistry" : 92}
# print(marks["Chemistry"])
# marks["Physics"] = 97
# print(marks)

# marks["Physics"] = 99
# print(marks)



#   --------->>>>>>>>>>>  FUNCTION   ------------->>>>>>>>>>>
#  Module Functions
# from math import sqrt
# from math import *
# print(sqrt(4))
# print(sqrt(16))


# Self Created Functions

def function_name(a,b,c):
    if(a == b == c):
        print(a+b)

function_name(1,1,1)


def printSum(first,second) : 
    print(first+second)

    

def printNames(name1, name2 = "Rahim Ansari"):
    print(name1,name2)
    
printSum(1, 3)  
printNames("Md") 