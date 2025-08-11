class FenwickTree:
    """
    Range query and point update | 1-based indexing acceptable(pad array with a 0 at beginning if 0 based indexing).
    
    """
    def __init__(self, n, array = []):
        self.n = n + 1
        self.FT = [0] * (n + 1)
        if array:
            for i in range(1, len(array)):
                self.FT[i] +=  array[i]
                r = i + (i & -i)
                if r < len(self.FT):
                    self.FT[r] += self.FT[i]
    
    def sum(self, r):
        sums = 0
        while (r > 0):
            sums += self.FT[r]
            r -= r & -r  
        return sums
    
    def sum_rng(self, l, r):
        return self.sum(r) - self.sum(l - 1)
    
    def update(self, i, val):
        while (i < self.n):
            self.FT[i] += val
            i += i & -i


FT = FenwickTree(4)
arr = [0,1,2,3,4]
for i in range(1, len(arr)):
    FT.update(i, arr[i])

print(FT.sum(4))

class FenwickTree:
    """
    Range update and point query | 1 based indexing, Convert to 1 based index
    """
    def __init__(self, n):
        self.n = n + 1
        self.FT = [0] * (n + 1)

    def sum(self, r):
        sums = 0
        while (r > 0):
            sums += self.FT[r]
            r -= r & -r  
        return sums

    def update(self, i, val):
        while (i < self.n):
            self.FT[i] += val
            i += i & -i
    
    def range_update(self, l, r, val):
        self.update(l, val)
        self.update(r + 1, -val)

FT = FenwickTree(5)
FT.range_update(1, 3, 5)
FT.range_update(2, 5, 3)
