#Simple Calculator using function

def add(a, b):
    result=a+b
    print('a+b=', result)

def sub(a, b):
    result=a-b
    print('a-b=', result)

def mul(a, b):
        result=a*b
        print('a*b=', result)

def div(a, b):
    result=a/b
    print('a/b=', result)

def mod(a,b):
    result=a%b
    print('a%b=', result)

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
op= input('Enter operator:')

if op=='+':
    add(a,b)
elif op=='-':
    sub(a,b)
elif op=='*':
    mul(a,b)
elif op=='/':
    div(a,b)
elif op=='%':
    mod(a,b)
else:
    print('Invalid')