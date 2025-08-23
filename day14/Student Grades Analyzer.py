# Day 14: Student Grades Analyzer
from functools import reduce

grades = [55, 67, 89, 45, 76, 92, 38, 80]

# Curve grades using lambda + map (add 5 marks to each)
curved = list(map(lambda x: x + 5, grades))

# Filter passing students (>= 50)
passed = list(filter(lambda x: x >= 50, curved))

# Find total and average using reduce
total = reduce(lambda a, b: a + b, passed)
average = total / len(passed)

print("Original Grades:", grades)
print("Curved Grades:", curved)
print("Passed Students:", passed)
print("Total Marks (Passed):", total)
print("Average Marks (Passed):", average)
