import math
import random
def is_number(n):
    try:
        int(n)
    except ValueError:
        print('n must be a int')
        return False
    return True

def MAE(n,a,b):
    k=0
    for i in range(n):
        k = k + abs(a-b)
    return k/n
def MSE(n,a,b):
    k = 0
    for i in range(n):
        k = k + (a-b)**2
    return k/n

def exercise3(n):
    is_number(n)
    funct = input('Input loss Name ')
    if funct =="MAE":
        for i in range(n):
            a = random.uniform(0,10)
            b = random.uniform(0,10)
            print(f"loss name: {funct}, sample: {i}, pre : {a}, target: {b}, loss: {MAE(n,a,b)}")
    elif funct =="MSE":
        for i in range(n):
            a = random.uniform(0,10)
            b = random.uniform(0,10)
            print(f"loss name: {funct}, sample: {i}, pre : {a}, target: {b}, loss: {MSE(n,a,b)}")
    else:
        print(f"{funct} is not support")
exercise3(15)

