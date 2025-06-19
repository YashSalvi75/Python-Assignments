def natural_sum_pattern(n):
    total = 0
    for i in range(1, n+1):
        total += i
        print(" + ".join(str(x) for x in range(1, i+1)), "=", total)

 
natural_sum_pattern(5)
