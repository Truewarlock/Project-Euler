def factorial(num):
    rez=1
    dif=0
    for i in range(num):
        rez= rez*(num-dif)
        dif=dif+1
    return rez

def sum_of_digits(num):
    suma=0
    string=str(num)
    for i in range(len(string)):
        suma=suma+int(string[i])
    return suma


number=int(input("What is your number?"))
print("Factorial is:"+str(factorial(number)))
print("Sum of digits is:"+str(sum_of_digits(factorial(number))))
