def count_digits(num):
    count = 0
    n = abs(num)
    while n > 0:
        n //= 10
        count += 1
    print(f"Total digits in {num} = {count}")


count_digits(12345)
