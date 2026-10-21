from detector import detect_sensitive_information
from redactor import redact_sensitive_information


sample_text = """
Contact Rahul at rahul@example.com.
Phone: 9876543210.
Employee ID: EMP1042.
Account ID: AC782914.
"""

# Step 1: Detect sensitive information.
findings = detect_sensitive_information(sample_text)

# Step 2: Redact the detected information.
sanitised_text = redact_sensitive_information(
    sample_text,
    findings
)

# Step 3: Display the results.
print("===== ORIGINAL TEXT =====")
print(sample_text)

print("\n===== SANITISED TEXT =====")
print(sanitised_text)