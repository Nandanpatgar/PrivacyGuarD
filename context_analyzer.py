def analyze_context(text, findings, destination):
    """
    Evaluate sensitive information using simple,
    predefined sharing policies.

    This is a rule-based prototype, not a complete
    natural-language understanding system.
    """

    context_results = []
    text_lower = text.lower()

    # STEP 1: Check for simple protective instructions.
    protective_words = [
        "redact",
        "remove",
        "mask",
        "hide",
        "anonymize",
        "anonymise"
    ]

    protective_intent = any(
        word in text_lower.split()
        for word in protective_words
    )

    # STEP 2: Check whether the text mentions public sharing.
    public_sharing_phrases = [
        "publish publicly",
        "public publication",
        "public report",
        "publicly available",
        "publish the report",
        "publish this"
    ]

    mentions_public_sharing = any(
        phrase in text_lower
        for phrase in public_sharing_phrases
    )

    # STEP 3: Evaluate every detected sensitive item.
    for item in findings:

        category = item["category"]

        # PUBLICATION POLICY
        if destination == "Public publication":

            if protective_intent:
                reason = (
                    "A possible protective instruction was "
                    "detected. Sensitive information must still "
                    "be redacted before public publication."
                )
            else:
                reason = (
                    "Sensitive information was detected in "
                    "content intended for public publication."
                )

            context_results.append({
                "category": category,
                "value": item["value"],
                "risk": "HIGH",
                "action": "REDACT",
                "reason": reason
            })

        # EXTERNAL SHARING POLICY
        elif destination == "External sharing":

            if protective_intent:
                reason = (
                    "A possible protective instruction was "
                    "detected. Verify that sensitive information "
                    "is removed before external sharing."
                )
            else:
                reason = (
                    "Check whether sharing this information "
                    "externally is permitted by policy."
                )

            context_results.append({
                "category": category,
                "value": item["value"],
                "risk": "MEDIUM",
                "action": "REVIEW",
                "reason": reason
            })

        # INTERNAL USE POLICY
        else:

            context_results.append({
                "category": category,
                "value": item["value"],
                "risk": "REVIEW",
                "action": "CHECK_POLICY",
                "reason": (
                    "Internal use does not automatically "
                    "authorise access to sensitive information."
                )
            })

    # STEP 4: Handle public-sharing text when no sensitive
    # information was detected.
    if mentions_public_sharing and not findings:

        context_results.append({
            "category": "Sharing Context",
            "value": destination,
            "risk": "REVIEW",
            "action": "CHECK_CONTENT",
            "reason": (
                "The text mentions public sharing, but the "
                "current detector found no sensitive items. "
                "This does not guarantee that the content "
                "is free of sensitive information."
            )
        })

    return context_results