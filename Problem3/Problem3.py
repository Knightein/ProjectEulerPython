def problem3_solution(factor):
    """
    This method uses prime factorisation based on trial division to find the prime factors.

    :param factor: The number to find the prime factors of.
    :return: List of prime factors.
    """
    i = 2
    factors = []

    # While the square of i is less than the factor
    while i * i <= factor:
        # If the remainder of the factor and i is non-zero, increment i
        if factor % i:
            i += 1
        # If it is zero, this means i is a factor of the factor,
        # we divide the factor by i and add i to the list of factors
        else:
            factor //= i
            factors.append(i)

    if factor > 1:
        factors.append(factor)

    return factors
