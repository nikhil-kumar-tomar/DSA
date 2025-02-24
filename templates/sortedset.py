from bisect import bisect_left, bisect_right, insort

class SortedSet:
    def __init__(self, iterable=None):
        self._list = []
        if iterable:
            for value in iterable:
                self.add(value)

    def add(self, value):
        
        idx = bisect_left(self._list, value)
        if idx == len(self._list) or self._list[idx] != value:
            self._list.insert(idx, value)

    def remove(self, value):
        
        idx = bisect_left(self._list, value)
        if idx == len(self._list) or self._list[idx] != value:
            raise KeyError(f"{value} not in SortedSet")
        self._list.pop(idx)

    def discard(self, value):
        
        idx = bisect_left(self._list, value)
        if idx < len(self._list) and self._list[idx] == value:
            self._list.pop(idx)

    def bisect_left(self, value):
        
        return bisect_left(self._list, value)

    def bisect_right(self, value):
        
        return bisect_right(self._list, value)

    def __contains__(self, value):
        
        idx = bisect_left(self._list, value)
        return idx < len(self._list) and self._list[idx] == value

    def __len__(self):
        
        return len(self._list)

    def __iter__(self):
        
        return iter(self._list)

    def __getitem__(self, index):
        
        return self._list[index]

    def __repr__(self):
        return f"SortedSet({self._list})"

a = SortedSet([3,2,1,5,4,2,1])
