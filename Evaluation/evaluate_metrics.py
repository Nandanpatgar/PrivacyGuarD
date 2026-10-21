from detector import detect_sensitive_information


# --------------------------------------------------
# TEST DATASET
# --------------------------------------------------

test_cases = [
    {
    "text": "Rahul Sharma works at Infosys. Contact him at rahul@example.com",
    "expected": [
        ("Person Name", "Rahul Sharma"),
        ("Email Address", "rahul@example.com")
    ]
},
    {
        "text": "My phone number is 9876543210",
        "expected": [
            ("Phone Number", "9876543210")
        ]
    },
    {
        "text": "Employee ID: EMP1042",
        "expected": [
            ("Employee ID", "EMP1042")
        ]
    },
    {
        "text": "Account ID: AC123456",
        "expected": [
            ("Account ID", "AC123456")
        ]
    },
    {
        "text": "PAN: ABCDE1234F",
        "expected": [
            ("PAN-like Identifier", "ABCDE1234F")
        ]
    },
    {
        "text": "Server IP: 192.168.1.10",
        "expected": [
            ("IPv4 Address", "192.168.1.10")
        ]
    },
    {
        "text": "Hello, have a nice day!",
        "expected": []
    },
    {
        "text": "Call me tomorrow",
        "expected": []
    },
    {
        "text": "Email: rahul@example.com, ID: EMP1042",
        "expected": [
            ("Email Address", "rahul@example.com"),
            ("Employee ID", "EMP1042")
        ]
    },
    {
        "text": "Invalid IP: 999.999.999.999",
        "expected": []
    }
]


# --------------------------------------------------
# EVALUATION
# --------------------------------------------------

true_positives = 0
false_positives = 0
false_negatives = 0

category_metrics = {}


for case in test_cases:

    text = case["text"]

    expected = {
        (category, value)
        for category, value in case["expected"]
    }

    findings = detect_sensitive_information(text)

    detected = {
        (item["category"], item["value"])
        for item in findings
    }

    # Compare expected and detected items.
    tp = expected & detected
    fp = detected - expected
    fn = expected - detected
    if fp or fn:
        print("\n===== MISMATCH FOUND =====")
        print("Input:", text)

        if fp:
            print("False positives:", fp)

        if fn:
            print("False negatives:", fn)

    true_positives += len(tp)
    false_positives += len(fp)
    false_negatives += len(fn)

    # Maintain counts for each category.
    categories = {
        category
        for category, _ in expected | detected
    }

    for category in categories:

        if category not in category_metrics:
            category_metrics[category] = {
                "TP": 0,
                "FP": 0,
                "FN": 0
            }

        category_metrics[category]["TP"] += sum(
            1 for item in tp if item[0] == category
        )

        category_metrics[category]["FP"] += sum(
            1 for item in fp if item[0] == category
        )

        category_metrics[category]["FN"] += sum(
            1 for item in fn if item[0] == category
        )


# --------------------------------------------------
# METRIC CALCULATION
# --------------------------------------------------

def calculate_metrics(tp, fp, fn):

    precision = (
        tp / (tp + fp)
        if tp + fp > 0
        else 0.0
    )

    recall = (
        tp / (tp + fn)
        if tp + fn > 0
        else 0.0
    )

    f1_score = (
        2 * precision * recall / (precision + recall)
        if precision + recall > 0
        else 0.0
    )

    return precision, recall, f1_score


# --------------------------------------------------
# OVERALL RESULTS
# --------------------------------------------------

precision, recall, f1 = calculate_metrics(
    true_positives,
    false_positives,
    false_negatives
)

print("\n===== OVERALL EVALUATION =====")
print(f"True Positives:  {true_positives}")
print(f"False Positives: {false_positives}")
print(f"False Negatives: {false_negatives}")
print(f"Precision:       {precision:.2%}")
print(f"Recall:          {recall:.2%}")
print(f"F1-score:        {f1:.2%}")


# --------------------------------------------------
# CATEGORY-WISE RESULTS
# --------------------------------------------------

print("\n===== CATEGORY-WISE METRICS =====")

for category, counts in sorted(category_metrics.items()):

    p, r, f = calculate_metrics(
        counts["TP"],
        counts["FP"],
        counts["FN"]
    )

    print(f"\nCategory: {category}")
    print(f"Precision: {p:.2%}")
    print(f"Recall:    {r:.2%}")
    print(f"F1-score:  {f:.2%}")