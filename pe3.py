def isPrime(n):
    for i in range (2,int(n**(1/2.0))):
        if n % i == 0:
            return False
    return True

print "Enter a prime:"
prime = input() 
largest = 0
i = 2
while i < prime:
    if prime % i == 0:
        n = prime / i
        if isPrime(n) and n > largest:
                largest = n
        prime /= i
        i = 2
    else:
        i += 1

print "Largest prime factor: "
print largest if largest > prime else prime 
