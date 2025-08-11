class SegmentTree:
    def __init__(self, n, array):
        self.st = [0] * (4 * n)
        self.array = array
        self.build(0, 0, n - 1)

    def build(self, current, tl, tr):
        if tl == tr:
            self.st[current] = self.array[tl]
            return
        else:
            tm = (tl + tr) // 2

            self.build(2 * current + 1, tl, tm)
            self.build(2 * current + 2, tm + 1, tr)
            self.st[current] = self.st[2 * current + 1] + self.st[2 * current + 2] # <- Change operation here
            return
    
    def query(self, current, tl, tr, l, r):
        if l > r:
            return 0

        if tl == l and tr == r:
            return self.st[current]
        else:
            tm = (tl + tr) // 2
            ans1 = self.query(2 * current + 1, tl, tm, l, min(r, tm))
            ans2 = self.query(2 * current + 2, tm + 1, tr, max(l, tm + 1), r)
            return ans1 + ans2 # <- Change operation here
    
    # Point Update only
    def update(self, current, tl, tr, pos, value): 
        if tl == tr == pos:
            self.st[current] = value
            return
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2 * current + 1, tl, tm, pos, value)
            else:
                self.update(2 * current + 2, tm + 1, tr, pos, value)
            
            self.st[current] = self.st[2 * current + 1] + self.st[2 * current + 2]
            return

array = [1, 3, -2, 8, -7]
st = SegmentTree(len(array), array)

print(st.st)

print(st.query(0, 0, len(array) -1, 2,2))

st.update(0, 0, len(array) -  1, 2, 4)

print(st.query(0, 0, len(array) -1, 2,2))
            
