

# prcatice of python functions  

# Task 1

# Create a function named welcome() that prints

def greet (name) : 
    return f"welcome mr {name}"

res = greet( "Yasir Afzal Soomro")
print(res)

# Task 2

# Create a function named about_me() that prints:

def about_me (**details) :
    return details

my_info = about_me (
    Name = "Afzal Soomro" , 
    Learning = "Python ", 
    Goal = " AI Engieer"
)

print(my_info)

def total_numbers(*numbers):
    return sum(numbers)

res_sum =total_numbers (1,2,3,4,5,5)
print (res_sum)

def find_max(*numbers):
    return max(numbers)

max = find_max(3,5,4,6,9,7,8,11,10)
print(max)

# Student Management System

# Build a simple console-based Student Management System.


students = [] 

def show_welcome():
    print("welcome to student management system")

show_welcome()

def calculate_average(*marks):
    sum = 0
    for mark in marks :
        sum += mark
 
    return sum / len(marks)

total_avg = calculate_average(80 , 99 , 91)
print(total_avg)

def register_student(name, role="Student"):
    if not name:
        raise ValueError ("please Enter Name")
    r = name , role
    return r

reg = register_student ("Afzal")
print (reg)

# Print numbers 1 → 10

def numb (n):
    if n == 0:
        return 
    numb(n - 1)
    print(n)

numb(10)

numbers2 = [5, 2, 8, 1, 9]

large = numbers2[0]
for nu in numbers2 :
    if nu > large :
        large = nu

print(large)

