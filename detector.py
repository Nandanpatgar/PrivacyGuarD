import re
import spacy


# -----------------------------------------
# LOAD THE PRETRAINED NLP MODEL
# -----------------------------------------

nlp = spacy.load("en_core_web_sm")


# -----------------------------------------
# REGEX PATTERNS
# -----------------------------------------

PATTERNS = {
    "Email Address": (
        r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"
    ),

    "Phone Number": (
        r"(?<!\d)(?:\+91[- ]?)?[6-9]\d{9}(?!\d)"
    ),

    "Employee ID": (
        r"\bEMP\d{4,}\b"
    ),

    "Account ID": (
        r"\bAC\d{6,}\b"
    ),

    "PAN-like Identifier": (
        r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"
    ),

    "IPv4 Address": (
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    )
}


# -----------------------------------------
# SENSITIVE INFORMATION DETECTOR
# -----------------------------------------

def detect_sensitive_information(text):

    findings = []

    # -------------------------------------
    # STEP 1: REGEX DETECTION
    # -------------------------------------

    for category, pattern in PATTERNS.items():

        matches = re.finditer(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        for match in matches:

            value = match.group()

            # Validate IPv4 address octets.
            if category == "IPv4 Address":

                octets = value.split(".")

                if not all(
                    0 <= int(octet) <= 255
                    for octet in octets
                ):
                    continue

            findings.append({
                "category": category,
                "value": value,
                "start": match.start(),
                "end": match.end(),
                "method": "Regex"
            })

    # -------------------------------------
    # STEP 2: NLP-BASED ENTITY DETECTION
    # -------------------------------------

    doc = nlp(text)

    # Technical labels that should not be
    # treated as person names.
    excluded_name_phrases = {
        "invalid ip",
        "valid ip",
        "ip address",
        "email address",
        "employee id",
        "account id",
        "phone number",
        "pan identifier"
    }

    for entity in doc.ents:

        if entity.label_ == "PERSON":

            entity_name = entity.text.strip()
            normalized_name = entity_name.casefold()

            # Skip known technical labels.
            if normalized_name in excluded_name_phrases:
                continue

            findings.append({
                "category": "Person Name",
                "value": entity_name,
                "start": entity.start_char,
                "end": entity.end_char,
                "method": "spaCy NER"
            })

    # -------------------------------------
    # STEP 3: REMOVE DUPLICATE FINDINGS
    # -------------------------------------

    unique_findings = []
    seen = set()

    for item in findings:

        key = (
            item["start"],
            item["end"],
            item["category"]
        )

        if key not in seen:

            unique_findings.append(item)
            seen.add(key)

    # -------------------------------------
    # STEP 4: SORT BY TEXT POSITION
    # -------------------------------------

    unique_findings.sort(
        key=lambda item: item["start"]
    )

    return unique_findings