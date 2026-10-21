from detector import detect_sensitive_information
from context_analyzer import analyze_context
from risk_classifier import classify_risk
from redactor import redact_sensitive_information
from report_generator import generate_report


# Sample input
text = """
Contact Rahul at rahul@example.com.
Phone: 9876543210.
Employee ID: EMP1042.
"""

destination = "Public publication"


# STEP 1: Detect sensitive information
findings = detect_sensitive_information(text)


# STEP 2: Analyse the sharing context
context_results = analyze_context(
    text,
    findings,
    destination
)


# STEP 3: Classify the overall risk
risk_result = classify_risk(context_results)


# STEP 4: Redact sensitive information
redacted_text = redact_sensitive_information(
    text,
    findings
)


# STEP 5: Generate the report
report = generate_report(
    findings,
    context_results,
    risk_result,
    redacted_text
)


# STEP 6: Display the report
print("\n===== PRIVACYGUARD AI REPORT =====")

print("Detected items:", report["total_detected"])

print("Overall risk:", report["overall_risk"])

print("Decision:", report["decision"])

print("Reason:", report["reason"])

print("\nSanitised text:")
print(report["redacted_text"])