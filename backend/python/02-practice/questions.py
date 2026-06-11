"""
Array Practice Problems

Common array manipulation problems to build programming fundamentals.
"""

# =============================================================================
# PROBLEM 1: FIND LARGEST NUMBER
# =============================================================================

def find_largest(numbers):
    """Find the largest number in a list."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


numbers = [1, 23, 2, 43, 11, 12, 10]
print(f"Largest number: {find_largest(numbers)}")


# =============================================================================
# PROBLEM 2: FIND SMALLEST NUMBER
# =============================================================================

def find_smallest(numbers):
    """Find the smallest number in a list."""
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest


print(f"Smallest number: {find_smallest(numbers)}")


# =============================================================================
# PROBLEM 3: FIND SECOND LARGEST
# =============================================================================

def find_second_largest(numbers):
    """Find the second largest number in a list."""
    largest = numbers[0]
    second_largest = numbers[0]

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return largest, second_largest


numbers = [1, 23, 2, 43, 11, 12, 10]
largest, second_largest = find_second_largest(numbers)
print(f"Largest number: {largest}")
print(f"Second largest number: {second_largest}")


# =============================================================================
# PROBLEM 4: SUM AND AVERAGE OF LIST
# =============================================================================

def calculate_sum_and_average(numbers):
    """Calculate sum and average of a list."""
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return total, average


list_num = [1, 4, 7, 5, 8, 9]
total, avg = calculate_sum_and_average(list_num)
print(f"Sum: {total}, Average: {avg:.2f}")


# =============================================================================
# PROBLEM 5: COUNT EVEN AND ODD NUMBERS
# =============================================================================

def count_even_odd(numbers):
    """Count even and odd numbers in a list."""
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


nums = [2, 3, 4, 12, 13, 15, 16, 8, 9]
even, odd = count_even_odd(nums)
print(f"Even numbers: {even}\nOdd numbers: {odd}")


# =============================================================================
# PROBLEM 6: REMOVE DUPLICATES
# =============================================================================

def remove_duplicates(numbers):
    """Remove duplicate numbers from a list."""
    return set(numbers)


uni_num = [1, 1, 2, 3, 4, 3, 2, 4, 2, 23, 22, 1, 22, 1]
unique_numbers = remove_duplicates(uni_num)
print(f"Unique numbers: {unique_numbers}")


# =============================================================================
# PROBLEM 7: REVERSE LIST
# =============================================================================

def reverse_list_slicing(numbers):
    """Reverse a list using slicing."""
    return numbers[::-1]


def reverse_list_method(numbers):
    """Reverse a list using the reverse method."""
    numbers.reverse()
    return numbers


rev_list = [1, 2, 3, 4, 5, 6, 7]
print(f"Reversed (slicing): {reverse_list_slicing(rev_list)}")
print(f"Reversed (method): {reverse_list_method(rev_list)}")
