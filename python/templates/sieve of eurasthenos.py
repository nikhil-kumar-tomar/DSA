#sieve of eurathenous
def sieve(n):
    array = [0,0]
    for x in range(1, n):
        array.append(1)
    
    for i in range(2, int(n ** (1/2)) + 1):
        if array[i] == 1:
            for j in range(i * i, n+1, i):
                array[j] = 0
    
    return array



def prime_factors(n):
    """
    SPF calculation, Let primes have spf 1 and composite have different numbers. 
    below as we encounter any prime that hasn't been affected by primes before it yet. We are changing its factor to itself as well.
    """
    # SPF calculation
    spf = [1] * (n + 1)
    spf[0] = 0
    for i in range(2, n + 1):
        if spf[i] == 1:
            for j in range(i, n+1, i):
                if spf[j] == 1:
                    spf[j] = i
    
    # Prime Factorization, This part can be seperated to only do for numbers in the problem's list, Currently we are finding for all n nums
    factors = []
    for _ in range(n + 1):
        factors.append(set()) # <- convert to set() for unique prime factors
    
    for num in range(2, n + 1):
        copy = num
        while copy != 1:
            if type(factors[num]) == list:
                factors[num].append(spf[copy])
            else:
                factors[num].add(spf[copy])
            copy = copy // spf[copy]

    return factors

print(prime_factors(1000))
def segmented_sieve(left, right):
    prime = sieve(int(right ** (1/2)) + 1)
    segmented = [1] * (right - left + 1)

    for i in range(2, len(prime)):
        if prime[i] != 1:
            continue
        
        for j in range(max(i * i, ((left + i - 1) // (i)) * i), right + 1, i):
            segmented[j - left] = 0
    

    if left == 0:
        segmented[0] = 0
        if right >= 1:
            segmented[1] = 0
    
    if left == 1:
        segmented[0] = 0

    return segmented

# print(segmented_sieve(19990000000, 20000000000))

# Segmented Sieve to calculate in bigger ranges, Upto 10**12 as Right.

