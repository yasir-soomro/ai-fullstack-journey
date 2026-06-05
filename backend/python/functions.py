

# functions are reusable blocks of code that perform a specific task. They allow us to break down our code into smaller, more manageable pieces, and they can be called multiple times throughout our program. In Python, we define a function using the `def` keyword, followed by the function name and parentheses. Inside the parentheses, we can specify any parameters that the function will take. The code block that performs the task is indented below the function definition. We can also return a value from a function using the `return` statement. Functions can be called by their name followed by parentheses, and we can pass arguments to the function if it takes parameters. Functions are an essential part of programming and help us write cleaner, more efficient code.


def welcome (name ) :
    print(f"welcome {name}")

welcome("ALI")

# function scope 

count = 0

def increment ():
    global count 
    count += 1

def numbers (*prime_numbers) :
    print(prime_numbers)

numbers(1,2,3,4,5)

# this *args used when we don't know how many positional arguments will come 

def login (**logins):
    print(logins)

login(
    name = " afzal soomro",
    passowrd = " soomro0311",
    age = 21,
)

# used when we have need multiple keword arguments or we don't know how many kewargs will come 

def register (username, *args , **kewargs) :
    print(username)
    print(args)
    print(kewargs)

register (
    "Afzal Soomro",
    "pakistan",
    "soomro",
    "mazarjo",
    email = "soomro@info.com",
    age = 23

)


# lambda funtion 

def fun (x) :
    return x * x

res1 = fun (5)
print(5)

squ = lambda  x : x * x

print(squ(6))


people = [
    ("Ali", 25),
    ("Ahmed", 18),
    ("Sara", 30)
]

people.sort(
    key=lambda peopl: peopl[1]
)

print (people)

# Find the student with highest marks.

# students = [
#     ("Ali", 80),
#     ("Ahmed", 95),
#     ("Sara", 88)
# ]

# students (
#     key= lambda stu : max(stu)
# )
# print(students)

numbers1 = [1,2,3,4,5,6,7,8,9]

odd_numbers = filter(
    lambda num : num % 2  != 0 ,
    numbers1
)

print(list(odd_numbers)) 

def cat () :
    print("meow")


def dog () :
    print("woof")

def animal_sound (animal) :
    animal()

xa = animal_sound
xa(dog)
xa(cat)
