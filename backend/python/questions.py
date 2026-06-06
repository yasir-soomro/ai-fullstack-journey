

# Find Largest Number

# Hint: Start with the first number as largest.

numbers = [1,23,2,43,11,12,10]

largest = numbers[0]
# sec_largeset = numbers[0]

for num in numbers :
    if num > largest :
        largest = num
print(f"here is largest number {largest}")

# Find Smallest Number
# Hint: Start with the first number as smallest.

smallest = numbers[0]

for n in numbers :
    if n < smallest :
        smallest = n

print(f"here is smallest number {smallest}")

# Find Second Largest

# Hint: Track both largest and second_largest.

numbers = [1, 23, 2, 43, 11, 12, 10]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(f"Largest number: {largest}")
print(f"Second largest number: {second_largest}")

# Sum of List

# Hint: Keep adding each number to a variable.

list_num = [1,4,7,5,8,9]

sum = 0

for li in list_num :
    sum += li
    avg = sum / len(list_num)

print(f"sum of list {sum} and avg of it {avg:.2f}")


# Average of List
# Hint: sum ÷ count.

# Count Even Numbers and Odd numbers 

# Hint: Check num % 2 == 0.

nums = [2,3,4,12,13,15,16,8,9]

even_numbers = 0
odd_numbers = 0
for num in nums :
    if num % 2 == 0 :
        even_numbers += 1
    else : 
        odd_numbers +=1

print (f"even numbers {even_numbers} \nodd numbers {odd_numbers}")

# Remove Duplicates

# Hint: Use a set or check before adding.

uni_num = [1,1,2,3,4,3,2,4,2,23,22,1,22,1]
unique_numbers = set()
for num in uni_num :
    unique_numbers.add(num)
print(f"unique numbers {unique_numbers}")

# Reverse List

# Hint: Start from the last index.

rev_list = [1,2,3,4,5,6,7]

rev = rev_list[:: -1 ]
rev_list.reverse()
print(rev)
print(rev_list)