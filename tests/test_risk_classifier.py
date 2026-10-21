from detector import detect_sensitive_information
from context_analyzer import analyze_context
from risk_classifier import classify_risk


text = """
Publish the customer report publicly.
Customer email: rahul@example.com
Employee ID: EMP1042
"""

destination = "Public publication"

# Step 1: Detect sensitive information.
findings = detect_sensitive_information(text)

# Step 2: Analyse the sharing context.
context_results = analyze_context(
    text,
    findings,
    destination
)

# Step 3: Classify the overall risk.
risk_result = classify_risk(context_results)

# Step 4: Display the decision.
print("\n===== PRIVACY RISK REPORT =====")

print("Overall Risk:", risk_result["overall_risk"])
print("Decision:", risk_result["decision"])
print("Reason:", risk_result["reason"])