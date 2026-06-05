# 1. Find Maximum Element

nums = [3, 7, 2, 9, 5]

def find_maximum(nums):
    if not nums:
        return None  # Return None for an empty list
    
    max_num = nums[0]  # Initialize max_num to the first element
    if len(nums) == 1:
        return max_num  # Return the only element if the list has one element

    for num in nums[1:]:
        if num > max_num:
            max_num = num
    return max_num
print(find_maximum(nums))  # Output: 9
