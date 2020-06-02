#Método 1
lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
print(lambda_factorial(5))

#Método 2
print((lambda a: lambda v: a(a,v))(lambda s,x: 1 if x ==0 else x*s(s,x-1))(5))