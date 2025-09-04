def powers_of_two(N):
    result = []
    k = 1
    while 2 ** k <= N:
        result.append(2 ** k)
        k += 1
    return result

print(powers_of_two(10))    
