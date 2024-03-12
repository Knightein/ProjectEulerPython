def problem2_solution():
    # Since 2 is part of the starting sequence, just start sum at 2 since it is even
    sum = 2
    # Temp value to store the addition of the sequence
    temp = 0
    # Simple counter
    counter = 0
    # Starting sequence
    seq = [1, 2]
    while temp < 4000000:
        temp = seq[counter] + seq[counter + 1]
        counter += 1
        seq.append(temp)
        # Check if the result of the Fibonacci is even
        if temp % 2 == 0:
            sum += temp
    return sum
