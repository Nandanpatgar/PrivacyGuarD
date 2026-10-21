def redact_sensitive_information(text, findings):
    """
    Replace detected sensitive information with
    category-specific placeholders.

    The original text is not modified.
    A new sanitised string is returned.
    """

    # Work from the end of the text towards the beginning.
    # This prevents earlier replacements from changing
    # the positions of later detections.

    redacted_text = text

    # Process detections in descending order of start position.
    sorted_findings = sorted(
        findings,
        key=lambda item: item["start"],
        reverse=True
    )

    for item in sorted_findings:

        start = item["start"]
        end = item["end"]
        category = item["category"]

        # Map detection categories to readable placeholders.
        placeholder_map = {
    "Email Address": "[EMAIL ADDRESS]",
    "Phone Number": "[PHONE NUMBER]",
    "Employee ID": "[EMPLOYEE ID]",
    "Account ID": "[ACCOUNT ID]",
    "Person Name": "[PERSON]",
    "PAN-like Identifier": "[PAN IDENTIFIER]",
    "IPv4 Address": "[IP ADDRESS]"
}

        placeholder = placeholder_map.get(
            category,
            "[SENSITIVE INFORMATION]"
        )

        # Replace the detected text using its positions.
        redacted_text = (
            redacted_text[:start]
            + placeholder
            + redacted_text[end:]
        )

    return redacted_text