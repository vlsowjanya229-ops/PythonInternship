#Random Password Generator
print('Enter length of the password')
N=int(input())
import string
import random
password = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
print("The generated random string: " ,password)
