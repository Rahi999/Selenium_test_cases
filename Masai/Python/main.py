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