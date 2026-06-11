"""
Functions Learning Module

Functions are reusable blocks of code that perform specific tasks. They help break down
programs into smaller, manageable pieces and promote code reusability and maintainability.
"""

# =============================================================================
# BASIC FUNCTION DEFINITION AND CALLING
# =============================================================================


def welcome(name):
    """Print a welcome message."""
    print(f"welcome {name}")


welcome("ALI")


# =============================================================================
# FUNCTION SCOPE AND GLOBAL VARIABLES
# =============================================================================

count = 0


def increment():
    """Increment global counter."""
    global count
    count += 1


# =============================================================================
# *ARGS: VARIABLE-LENGTH POSITIONAL ARGUMENTS
# =============================================================================


def numbers(*prime_numbers):
    """Print all positional arguments passed to the function."""
    print(prime_numbers)


numbers(1, 2, 3, 4, 5)


# =============================================================================
# **KWARGS: VARIABLE-LENGTH KEYWORD ARGUMENTS
# =============================================================================


def login(**credentials):
    """Print all keyword arguments passed to the function."""
    print(credentials)


login(
    name="afzal soomro",
    password="soomro0311",
    age=21,
)


# =============================================================================
# COMBINING *ARGS AND **KWARGS
# =============================================================================


def register(username, *args, **kwargs):
    """Process user registration with positional and keyword arguments."""
    print(username)
    print(args)
    print(kwargs)


register(
    "Afzal Soomro",
    "pakistan",
    "soomro",
    "mazarjo",
    email="soomro@info.com",
    age=23
)


# =============================================================================
# LAMBDA FUNCTIONS
# =============================================================================

# Anonymous function for simple operations
def square(x):
    """Calculate square of x."""
    return x * x


square_lambda = lambda x: x * x
print(square_lambda(6))


# Sorting with lambda
people = [
    ("Ali", 25),
    ("Ahmed", 18),
    ("Sara", 30)
]

people.sort(key=lambda person: person[1])
print(people)


# =============================================================================
# FILTER WITH LAMBDA
# =============================================================================

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = filter(lambda num: num % 2 != 0, numbers_list)
print(list(odd_numbers))


# =============================================================================
# HIGHER-ORDER FUNCTIONS
# =============================================================================

def cat():
    """Make cat sound."""
    print("meow")


def dog():
    """Make dog sound."""
    print("woof")


def animal_sound(animal):
    """Call animal function to produce sound."""
    animal()


sound_handler = animal_sound
sound_handler(dog)
sound_handler(cat)
