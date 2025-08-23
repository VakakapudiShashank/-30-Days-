# Day 13: Quick Data Cleaner using List Comprehension

raw_data = [" Alice  ", "BOB", "  ", "ChArLiE ", "   dave", "EVE  "]

# Clean data: strip spaces, convert to lowercase, and ignore empty strings
cleaned_data = [name.strip().lower() for name in raw_data if name.strip()]

print("Raw Data:", raw_data)
print("Cleaned Data:", cleaned_data)
