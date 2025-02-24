#sieve of eurathenous

def sieve(n):
    array = [0,0]
    for x in range(1, n + 1):
        array.append(1)
    
    for i in range(2, int(n ** (1/2)) + 1):
        if array[i] == 1:
            for j in range(i * i, n+1, i):
                array[j] = 0
    
    return array

print(len(sieve(31)))
