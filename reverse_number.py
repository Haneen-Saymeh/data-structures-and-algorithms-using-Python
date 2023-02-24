def reverse_num(num):
    reversed_number = 0
    while num != 0:
        digit = num % 10
        reversed_number= reversed_number* 10 + digit
        num = num//10
    return reversed_number

print(reverse_num(679))
