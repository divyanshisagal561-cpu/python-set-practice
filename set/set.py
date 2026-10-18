# 1. Create and Display a Set
# Create a set containing 5 different numbers. Print the set and its type.

numbers_1 = {1, 2, 3, 4, 5}

print(numbers_1)
print(type(numbers_1))

# 2. Add Elements
# Create a set {10, 20, 30}. Add:

# 40 using add()
# 50 using update()

# Print the final set.

numbers_2 = {10, 20, 30}

numbers_2.add(40)
print(numbers_2)

numbers_2.update([50])
print(numbers_2)

# 3. Remove Elements
# Create a set {10, 20, 30, 40, 50}. Remove 30 using:

# discard()
# remove()

# What is the difference between these two methods?

number_3 = {10, 20, 30, 40, 50}
number_3.discard(30) 
print(number_3)

number_3 = {10, 20, 30, 40, 50}
number_3.remove(30) 
print(number_3)

# remove() gives an error if the element is not present.
# discard() does not give an error if the element is not present.

# 4. Set Length and Membership
# Create a set of 6 numbers. Find:

# Number of elements using len()
# Whether 25 exists using in
# Whether 100 does not exist using not in

numbers_4 = {1, 2, 3, 4, 5, 6}

print(len(numbers_4))

print(25 in numbers_4)

print(100 not in numbers_4)

# 5. Remove Duplicates
# Given:

numbers_5 = [10, 20, 10, 30, 20, 40, 30, 50]

# Convert the list into a set to remove duplicate values.

new_set = set(numbers_5)

print(new_set)

# 6. Union of Sets
# Given:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Find the union using:
# |
# union()

set_union_1 = A.union(B)
print(set_union_1)

set_union_2 = A | B
print(set_union_2)

# 7. Intersection of Sets
# Using the same sets A and B, find the common elements using:

# &
# intersection()

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

set_inter_1 = A.intersection(B)
print(set_inter_1)

set_inter_2 = A & B
print(set_inter_2)

# 8. Difference of Sets
# Using:

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

# Find:

# Elements present in A but not in B
# Elements present in B but not in A

# Use the - operator.

set_diff_1 = A - B
print(set_diff_1)

set_diff_2 = B - A
print(set_diff_2)

# 9. Symmetric Difference
# Using the sets:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Find elements that are present in either set but not in both.

# Use:

# ^
# symmetric_difference()

set_sym_1 = A.symmetric_difference(B)
print(set_sym_1)

set_sym_2 = A ^ B
print(set_sym_2)

# 10. Set Comparison
# Given:

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

# Check:

# Whether A is a subset of B
# Whether B is a superset of A
# Whether A and C are equal

subset_1 = A.issubset(B)
print(subset_1)

ss = B.issuperset(A)
print(ss)

print(A == C)

# 11. . Disjoint Sets
# Create:

# A = {1, 2, 3}
# B = {4, 5, 6}

# Check whether the two sets are disjoint using isdisjoint().

A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))

# 12. Copy a Set
# Create a set:

# numbers = {10, 20, 30, 40}

# Create a copy using copy(). Add 50 to the copied set and show that the original set is unchanged.


numbers_6 = {10, 20, 30, 40}
print(numbers_6)

copy_set = numbers_6.copy()
copy_set.add(50)

print(numbers_6)
print(copy_set)

# 13. Clear a Set
# Create a set containing 5 elements. Remove all elements using clear() and print the resulting set.

numbers_7 = {1, 2, 3, 4, 5}

numbers_7.clear()
print(numbers_7)

# 14. MINI PROJECT - Set Based Student Analysis ⭐
# Given:

# python_students = {"Aman", "Riya", "Rahul", "Priya", "Neha"}
# sql_students = {"Riya", "Rahul", "Karan", "Neha", "Vikas"}

# Find:

# Students learning both Python and SQL
# Students learning only Python
# Students learning only SQL
# Students learning either Python or SQL but not both
# All unique students learning Python or SQL

# This question covers union, intersection, difference, and symmetric difference together.

python_students = {"Aman", "Riya", "Rahul", "Priya", "Neha"}
sql_students = {"Riya", "Rahul", "Karan", "Neha", "Vikas"}

print(python_students.intersection(sql_students))
print(python_students.difference(sql_students))
print(sql_students.difference(python_students))
print(python_students.symmetric_difference(sql_students))
print(python_students.union(sql_students))






























