"""
Data Structures & Algorithms - Arrays Practice

Practice problems for array manipulation and algorithms.
"""

# =============================================================================
# PROBLEM 1: FIND MAXIMUM ELEMENT
# =============================================================================

def find_maximum(numbers):
    """Find the maximum element in an array."""
    if not numbers:
        return None  # Return None for an empty list

    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num


nums = [3, 7, 2, 9, 5]
print(f"Maximum element: {find_maximum(nums)}")  # Output: 9
