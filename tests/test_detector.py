from detector import detect_sensitive_information
from redactor import redact_sensitive_information


sample_text = (
    "Rahul Sharma works at Infosys in Bengaluru. "
    "His email is rahul@example.com. "
    "His phone number is 9876543210. "
    "His employee ID is EMP1042."
)


# STEP 1: DETECT SENSITIVE INFORMATION

findings = detect_sensitive_information(sample_text)

print("\n===== DETECTION RESULTS =====")

for item in findings:

    print(
        f"Category: {item['category']} | "
        f"Value: {item['value']} | "
        f"Method: {item['method']}"
    )


# STEP 2: REDACT DETECTED INFORMATION

redacted_text = redact_sensitive_information(
    sample_text,
    findings
)

print("\n===== SANITISED TEXT =====")
print(redacted_text)