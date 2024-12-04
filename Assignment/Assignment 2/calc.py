def add(n1,n2):
    return n1+n2
def sub (n1,n2):
    return n1-n2
def mult (n1,n2):
    return n1*n2
def div (n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        return "divisor cannot be zero"
    