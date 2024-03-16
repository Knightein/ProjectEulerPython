def problem4_solution():
    """
    This method finds the greatest palindrome from the multiplication of two 3-digit numbers.
    :return: The highest palindrome from a product of two 3-digit numbers.
    """
    x = 100
    y = 100
    possible_palindromes = [0]

    for i in range(899):
        while y < 999:
            result = x * y
            # If the length of the integer is not even, it cannot be a palindrome
            if len(str(result)) % 2 == 0:
                digits = list(str(result))
                if digits[0] == digits[5] and digits[1] == digits[4] and digits[2] == digits[3]:
                    if result > possible_palindromes[0]:
                        possible_palindromes.clear()
                        possible_palindromes.append(result)
            else:
                # Ignore result if it is odd
                pass
            y += 1
        x += 1
        y = 100

    return possible_palindromes.pop()
