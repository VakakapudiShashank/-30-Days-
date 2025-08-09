# Day 1 - Hello Python Interactive Greeting App

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! 👋")

from datetime import datetime
current_year = datetime.now().year
hundred_year = current_year + (100 - age)

print(f"You will turn 100 years old in the year {hundred_year}.")
