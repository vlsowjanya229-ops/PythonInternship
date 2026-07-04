#Calculator
print('Enter the first number')
a=int(input())
print('Enter second number')
b=int(input())
print('Enter the operation you want to perform(+,-,*,/,%)')
c=input()
if c=='+':
    print('The addition is',a+b)
elif c=='-':
    print('The subtraction is ',a-b)
elif c=='*':
    print('The multiplication is',a*b)
elif c=='/':
    print('The division is ',a/b)
elif c=='%':
    print('The modulo division is',a%b)
else:
    print('Please select one of the options among +,-,*,%,/')
