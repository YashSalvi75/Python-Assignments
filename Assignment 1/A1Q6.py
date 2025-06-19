def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        print(f"{num} is a Palindrome")
    else:
        print(f"{num} is not a Palindrome")

 
is_palindrome(121)
