class DisjointSetSize:
    def __init__(self, V):
        self.size = [1] * V
        self.parent = [x for x in range(V)]
        
    def _path_compression(self, u):
        if u == self.parent[u]:
            return u
        else:
            self.parent[u] = self.find_parent(self.parent[u])
            return self.parent[u]

    def find_parent(self, u):
        return self._path_compression(u)
    
    def union_find(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        
    def is_same(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if pu == pv:
            return True
        return False

disjointsetsize = DisjointSetSize(7)
edges = [(1,2),(2,3),(4,5),(6,7),(5,6),(3,7)]
for edge in edges:
    disjointsetsize.union_find(edge[0]-1, edge[1]-1)

print(disjointsetsize.parent)
print(disjointsetsize.size)
disjointsetsize.is_same(1, 3) # On demand path compression happening here
print(disjointsetsize.parent)
print(disjointsetsize.size)
