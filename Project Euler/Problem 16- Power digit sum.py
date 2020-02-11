
def Power(number):
    power= 2**number
    print(power)

def SumDigit(number):
    sum=0
    while number:
        sum+=number%10
        number//=10
    print(sum)
variable=int(input("What number?"))
number=Power(variable)
SumDigit(number)
