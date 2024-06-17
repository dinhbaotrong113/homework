import math
import random
def Factorial(n):
    f = 1
    for i in range(n):
        f = f*(i+1)
    return f
print(Factorial(3))
def sin(x,n):
    k=0
    for i in range(n):
        k = k + (((-1)**i))*(((x**(2*i+1)))/(Factorial(2*i+1)))
    return k
print(sin(3.14,10))
def cos(x,n):
    k=0
    for i in range(n):
        k = k + (((-1)**i)*(x**(2*i)))/(Factorial(2*i))
    return k
print(cos(3.14,10))
def sinh(x,n):
    k=0
    for i in range(n):
        k = k + (x**(2*i+1))/(Factorial(2*i+1))
    return k
print(sinh(3.14,10))
def cosh(x,n):
    k=0
    for i in range(n):
        k = k + (x**(2*i))/(Factorial(2*i))
    return k
print(cosh(3.14,10))

