# Swap values with temp

def swap_temp(a,b):
    temp = a
    a= b
    b= temp
    print("value of a after swaping:", a)
    print("value of b after swaping:", b)
swap_temp(5,10)

# Swap values without temp

def swap_it(a,b):
    a,b = b,a
    print("value of a after swaping:", a)
    print("value of b after swaping:", b)

swap_it(5,10)

# swap values with Addition and Subtraction

def swap_this(a,b):
    a= a+b
    b= a-b
    a= a-b
    print("value of a after swaping:", a)
    print("value of b after swaping:", b)
swap_this(5,10)


# swap values with Multiplication and Division

def swap_multi(a,b):
    a= a*b
    b= a/b
    a= a/b
    print("value of a after swaping:", a)
    print("value of b after swaping:", b)
swap_multi(5,10)


# XOR swap

def swap_xor(a,b):
    a= a^b
    b= a^b
    a= a^b
    print("value of a after swaping:", a)
    print("value of b after swaping:", b)
swap_xor(5,10)




