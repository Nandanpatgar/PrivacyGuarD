def generate_report(
    findings,
    context_results,
    risk_result,
    redacted_text
):
    """
    Combine the detection, contextual analysis,
    risk classification, and redaction results.
    """

    report = {
        "total_detected": len(findings),

        "detected_items": findings,

        "context_analysis": context_results,

        "overall_risk": risk_result["overall_risk"],

        "decision": risk_result["decision"],

        "reason": risk_result["reason"],

        "redacted_text": redacted_text
    }

    return report