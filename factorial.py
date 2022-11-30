# To find the  factorial of a number,
# the number is multiplied with all the integers that lie
#  between 1 and the number itself.

def factorial(n):
    fact= 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

print(factorial(5))

def factorial2(n):
    if n ==1:
        return n
    else:
        return n*factorial2(n-1)

print(factorial2(5))



