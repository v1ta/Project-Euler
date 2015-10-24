sum = 0
fibb = [0,1]
i = 1
while fibb[i] <= 4000000:
    if fibb[i] % 2 == 0:
        sum += fibb[i]
    i += 1
    fibb.append(fibb[i-1] + fibb[i-2])
print sum
    
