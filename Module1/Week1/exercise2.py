import math
def is_number(n):
    try:
        float(n)
    except ValueError:
        print('n must be a number')
        return False
    return True

def sigmoid(n):
    return 1/(1+(math.e)**(-n))
def ReLU(n):
    if n <=0:
        return 0
    else:
        return n
def ELU(n):
    if n<=0:
        return 0.01*((math.e)**n-1)
    else:
        return n

def exercise2(n):
    while is_number(n):
        func = input("Input activation Function (sigmoid|Relu|elu)")
        if func == "sigmoid":
            print(f"sigmoid:f({n}) = {sigmoid(n)}")
            break
        elif func == "Relu":
            print(f"Relu:f({n}) = {ReLU(n)}")
            break
        elif func == "ELU":
            print(f"elu:f({n}) = {ELU(n)}")
            break
        else:
            print(f"{func} is not supportted")
            break
exercise2(1.5)

