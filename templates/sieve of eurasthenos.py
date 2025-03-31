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


# Find Prime Factors
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
        factors.append([]) # <- convert to set() for unique prime factors
    
    for num in range(2, n + 1):
        copy = num
        while copy != 1:
            if type(factors[num]) == list:
                factors[num].append(spf[copy])
            else:
                factors[num].add(spf[copy])
            copy = copy // spf[copy]

    return factors


prime_factors(10**5)
