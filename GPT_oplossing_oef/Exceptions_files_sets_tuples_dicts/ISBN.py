def overview(codes):
    # Registration groups in required order
    groups = [
        ("English speaking countries", {'0', '1'}),
        ("French speaking countries", {'2'}),
        ("German speaking countries", {'3'}),
        ("Japan", {'4'}),
        ("Russian speaking countries", {'5'}),
        ("China", {'7'}),
        ("Other countries", {'6', '8', '9'})
    ]

    # Counters for each group + errors
    counts = {name: 0 for name, _ in groups}
    counts["Errors"] = 0

    def valid_isbn13(code):
        # must be 13 digits
        if len(code) != 13 or not code.isdigit():
            return False
        # prefix must be 978 or 979
        if not (code.startswith("978") or code.startswith("979")):
            return False

        # Validate checksum:
        total = 0
        for i in range(12):
            digit = int(code[i])
            total += digit if i % 2 == 0 else 3 * digit

        check_digit = (10 - (total % 10)) % 10
        return check_digit == int(code[12])

    # Process each code
    for code in codes:
        if not valid_isbn13(code):
            counts["Errors"] += 1
            continue

        # valid → determine group by the 4th digit
        group_digit = code[3]
        placed = False

        for name, digits in groups:
            if group_digit in digits:
                counts[name] += 1
                placed = True
                break

        if not placed:
            # should never happen because the table covers 0–9,
            # but safety fallback:
            counts["Errors"] += 1

    # Print the overview IN ORDER
    for name, _ in groups:
        print(f"{name}: {counts[name]}")
    print(f"Errors: {counts['Errors']}")