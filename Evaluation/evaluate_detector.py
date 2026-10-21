from detector import detect_sensitive_information

# Test cases containing expected sensitive information.
test_cases = [
    {
        "text": "Contact me at rahul@example.com",
        "expected": ["Email Address"]
    },
    {
        "text": "My phone number is 9876543210",
        "expected": ["Phone Number"]
    },
    {
        "text": "Employee ID: EMP1042",
        "expected": ["Employee ID"]
    },
    {
        "text": "Account ID: AC123456",
        "expected": ["Account ID"]
    },
    {
        "text": "PAN: ABCDE1234F",
        "expected": ["PAN-like Identifier"]
    },
    {
        "text": "Server IP: 192.168.1.10",
        "expected": ["IPv4 Address"]
    },
    {
        "text": "Hello, have a nice day!",
        "expected": []
    }
]

total_cases = len(test_cases)
passed_cases = 0

print("\n===== PRIVACYGUARD AI EVALUATION =====")

for index, case in enumerate(test_cases, start=1):

    findings = detect_sensitive_information(case["text"])

    detected = {
        item["category"]
        for item in findings
    }

    expected = set(case["expected"])

    passed = expected.issubset(detected)

    if not expected and detected:
        passed = False

    if passed:
        passed_cases += 1

    print(f"\nTest {index}: {case['text']}")
    print(f"Expected: {sorted(expected)}")
    print(f"Detected: {sorted(detected)}")
    print(f"Result: {'PASS' if passed else 'FAIL'}")

print("\n===== SUMMARY =====")
print(f"Total test cases: {total_cases}")
print(f"Passed: {passed_cases}")
print(f"Failed: {total_cases - passed_cases}")
print(f"Test pass rate: {passed_cases / total_cases * 100:.2f}%")