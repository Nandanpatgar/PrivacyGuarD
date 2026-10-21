def classify_risk(context_results):
    """
    Determine the overall risk and recommended action
    from the contextual analysis results.
    """

    if not context_results:
        return {
            "overall_risk": "LOW",
            "decision": "ALLOW",
            "reason": (
                "No policy issues were identified by the "
                "current checks. This does not guarantee "
                "that the content is safe."
            )
        }

    risks = [
        result["risk"]
        for result in context_results
    ]

    actions = [
        result["action"]
        for result in context_results
    ]

    # Highest priority: redaction is required.
    if "REDACT" in actions:
        return {
            "overall_risk": "HIGH",
            "decision": "REDACT",
            "reason": (
                "One or more detected items require "
                "redaction under the configured policy."
            )
        }

    # Next priority: policy review is required.
    if (
        "REVIEW" in actions
        or "CHECK_POLICY" in actions
        or "CHECK_CONTENT" in actions
    ):
        return {
            "overall_risk": "MEDIUM",
            "decision": "REVIEW",
            "reason": (
                "The request requires further review "
                "before proceeding."
            )
        }

    # Fallback for other explicitly classified findings.
    if "HIGH" in risks:
        return {
            "overall_risk": "HIGH",
            "decision": "BLOCK",
            "reason": (
                "A high-risk condition requires the "
                "request to be held."
            )
        }

    if "MEDIUM" in risks or "REVIEW" in risks:
        return {
            "overall_risk": "MEDIUM",
            "decision": "REVIEW",
            "reason": (
                "A potential privacy risk requires review."
            )
        }

    return {
        "overall_risk": "LOW",
        "decision": "ALLOW",
        "reason": (
            "No blocking condition was identified by "
            "the configured rules."
        )
    }