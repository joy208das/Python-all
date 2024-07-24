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

def calculator():
    a=float(input("enter 1st number: "))

    for n in operation:
        print(n)
    end=True

    while end:
        op=input("take a operation from above: ")
        b=float(input("enter 2nd number: "))

        operation_symbol=operation[op]

        answer=operation_symbol(a,b)

        print(f"a{str(op)}b = {answer}")

        if input("type yes to continue calculating with answer,or type no to for new calculation: ") == "yes":
            a=answer
        else :
            end =False        
            calculator()

calculator()        