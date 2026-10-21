# -----------------------------------------
# MASK SENSITIVE INFORMATION
# -----------------------------------------

def mask_sensitive_value(value, category):
    """
    Mask sensitive values before displaying them
    in the application interface.
    """

    value = str(value)

    # Mask email addresses.
    if category == "Email Address":

        if "@" in value:
            username, domain = value.split("@", 1)

            if len(username) <= 1:
                masked_username = "*"
            else:
                masked_username = (
                    username[0]
                    + "*" * (len(username) - 1)
                )

            return masked_username + "@" + domain

    # Mask phone numbers.
    if category == "Phone Number":

        if len(value) > 4:
            return "*" * (len(value) - 4) + value[-4:]

    # Mask employee and account identifiers.
    if category in ["Employee ID", "Account ID"]:

        if len(value) > 2:
            return value[:2] + "*" * (len(value) - 2)

    # Mask PAN-like identifiers.
    if category == "PAN-like Identifier":

        if len(value) > 4:
            return value[:2] + "*" * (len(value) - 4) + value[-2:]

    # Mask IPv4 addresses.
    if category == "IPv4 Address":
        return "[IP ADDRESS HIDDEN]"

    # Mask person names.
    if category == "Person Name":

        parts = value.split()

        masked_parts = []

        for part in parts:

            if len(part) == 1:
                masked_parts.append("*")
            else:
                masked_parts.append(
                    part[0] + "*" * (len(part) - 1)
                )

        return " ".join(masked_parts)

    # Default fallback.
    return "[SENSITIVE INFORMATION HIDDEN]"