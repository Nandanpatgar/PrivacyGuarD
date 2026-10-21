from privacy_utils import mask_sensitive_value


test_cases = [
    ("rahul@example.com", "Email Address"),
    ("9876543210", "Phone Number"),
    ("EMP1042", "Employee ID"),
    ("AC123456", "Account ID"),
    ("ABCDE1234F", "PAN-like Identifier"),
    ("192.168.1.10", "IPv4 Address"),
    ("Rahul Sharma", "Person Name")
]

print("\n===== PRIVACY MASKING TESTS =====")

for value, category in test_cases:

    masked = mask_sensitive_value(value, category)

    print(f"\nCategory: {category}")
    print(f"Original: {value}")
    print(f"Masked:   {masked}")