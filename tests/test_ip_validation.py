from detector import detect_sensitive_information


test_cases = [
    "Server IP: 192.168.1.10",
    "Router IP: 10.0.0.1",
    "Invalid IP: 999.999.999.999",
    "Invalid IP: 192.168.300.10"
]

for text in test_cases:

    findings = detect_sensitive_information(text)

    ip_addresses = [
        item["value"]
        for item in findings
        if item["category"] == "IPv4 Address"
    ]

    print(f"\nInput: {text}")
    print(f"Detected IP addresses: {ip_addresses}")