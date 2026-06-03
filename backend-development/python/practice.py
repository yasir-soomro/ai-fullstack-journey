

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