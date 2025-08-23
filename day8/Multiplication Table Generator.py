# Day 8: Multiplication Table Generator
# Topic: Loops (for, while)
# Project: Multiplication Table Generator (CLI)

def multiplication_table(number, upto):
    """Generates multiplication table for the given number."""
    table = []
    for i in range(1, upto + 1):
        table.append(f"{number} x {i} = {number * i}")
    return table

def main():
    print("=== Multiplication Table Generator ===")
    num = int(input("Enter a number: "))
    limit = int(input("Enter the limit (e.g., 10): "))

    table = multiplication_table(num, limit)
    print("\n--- Multiplication Table ---")
    for row in table:
        print(row)

if __name__ == "__main__":
    # Uncomment below line to run interactively
    # main()

    # --- Sample Test Cases ---
    print("=== Sample Test Cases ===")
    # Test Case 1
    print("\nTest Case 1: num=2, limit=5")
    for row in multiplication_table(2, 5):
        print(row)

    # Test Case 2
    print("\nTest Case 2: num=7, limit=10")
    for row in multiplication_table(7, 10):
        print(row)

    # Test Case 3
    print("\nTest Case 3: num=12, limit=12")
    for row in multiplication_table(12, 12):
        print(row)
