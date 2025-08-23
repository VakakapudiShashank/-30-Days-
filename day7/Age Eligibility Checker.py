# Day 7 - Age Eligibility Checker
# Topic: Conditional Statements

print("🧾 Age Eligibility Checker 🧾")

# Take user input for name and age
name = input("Enter your name: ")
age_input = input("Enter your age: ")

# Validate input
if not age_input.isdigit():
    print("⚠️ Invalid age entered. Please enter a number.")
else:
    age = int(age_input)

    print(f"\nHello {name}!")

    # Check eligibility for various categories
    if age < 0:
        print("❌ Age cannot be negative!")
    elif age < 5:
        print("🚼 You are too young for school.")
    elif 5 <= age < 18:
        print("🎒 You are eligible for school education.")
    elif 18 <= age < 60:
        print("💼 You are eligible to vote and work.")
    elif age >= 60:
        print("🎉 You are eligible for senior citizen benefits.")

    # Special condition for voting
    if age >= 18:
        print("🗳️ You are eligible to vote!")
    else:
        print("🕒 You are not eligible to vote yet.")
