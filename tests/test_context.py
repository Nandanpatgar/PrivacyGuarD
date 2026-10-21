from detector import detect_sensitive_information
from context_analyzer import analyze_context


text = """
Publish the customer report publicly.
Customer email: rahul@example.com
Employee ID: EMP1042
"""

destination = "Public publication"

# Step 1: Detect sensitive information.
findings = detect_sensitive_information(text)

# Step 2: Analyse the context.
results = analyze_context(
    text,
    findings,
    destination
)

# Step 3: Display the results.
for result in results:

    print("\nCategory:", result["category"])
    print("Value:", result["value"])
    print("Risk:", result["risk"])
    print("Action:", result["action"])
    print("Reason:", result["reason"])