# Day 19: Email & Phone Extractor
import re

text = """
Hello, contact me at john.doe@example.com or jane123@gmail.com.
You can also reach me at +91-9876543210 or (123) 456-7890.
"""

# Regex patterns
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
phones = re.findall(r"(\+?\d{1,3}?[-.\s]?\(?\d{2,3}\)?[-.\s]?\d{3,4}[-.\s]?\d{4})", text)

print("📧 Emails:", emails)
print("📞 Phone Numbers:", phones)
