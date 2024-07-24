'''calculator'''


def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def substract(a,b):
    return a-b

operation={
 "+":add ,
 "*":multiply,
 "/":division,
 "-":substract
}

a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))

for n in operation:
    print(n)

op=input("take a operation from above: ")

operation_symbol=operation[op]

answer=operation_symbol(a,b)

print(f"a{str(op)}b = {answer}")