t = int(input())

inputs = [t]
primes = []
for i in range(t):
    inputs.append(int(input())*2)

for num in range(3, 1000):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           primes.append(int(num))  

sets = [t]
for item in inputs:
    br = False
    for prime in primes:
        if prime > item:
            break
        if primes.count(item - prime) > 0:
            sets.append([prime, item - prime])
            break
        

for item in sets:
    print(item)




    





