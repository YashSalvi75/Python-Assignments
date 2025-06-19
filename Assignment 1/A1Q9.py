def sum_of_digits(num):
    total = sum(int(d) for d in str(abs(num)))
    print(f"Sum of digits in {num} = {total}")
 
 
sum_of_digits(1234)
