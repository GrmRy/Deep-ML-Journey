def add_two_numbers(l1, l2):
    result = []
    carry = 0
    i = 0

    while i < len(l1) or i < len(l2) or carry != 0:
        digit1 = 0
        if i < len(l1):
            digit1 = l1[i]

        digit2 = 0
        if i < len(l2):
            digit2 = l2[i]

        total = digit1 + digit2 + carry

        digit_out = total % 10

        carry = total // 10

        result.append(digit_out)
        i += 1

    return result
