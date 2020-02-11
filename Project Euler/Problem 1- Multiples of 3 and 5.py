a=int(input("What is your number?"))
sum=0
for i in range(a):
    if (i%3==0) or( i%5==0):
        sum=sum+i
    
    
    
print(sum)
