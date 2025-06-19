def is_armstrong(num):
    digits = list(map(int, str(num)))
    power = len(digits)
    total = sum(d ** power for d in digits)
    if total == num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

 
is_armstrong(153)
