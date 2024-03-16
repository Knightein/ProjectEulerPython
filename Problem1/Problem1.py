def problem1_solution(number):
    sum = 0

    for i in range(number):
        # Check modular of 3 or 5, and add to sum
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum
