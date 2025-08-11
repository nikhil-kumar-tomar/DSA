"""
Binary Search Tree based Set Implementation using AVL-TREE 

Log N insertions, deletions, searches
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
    
    def __repr__(self):
        return f"{self.value}"

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def _insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        if balance > 1 and value < root.left.value:
            return self._right_rotate(root)

        if balance < -1 and value > root.right.value:
            return self._left_rotate(root)

        if balance > 1 and value > root.left.value:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        if balance < -1 and value < root.right.value:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            if not root.left:
                temp_node = root.right
                root = None
                return temp_node
            elif not root.right:
                temp_node = root.left
                root = None
                return temp_node

            temp_node = self._min_value_node(root.right)
            root.value = temp_node.value
            root.right = self._delete(root.right, temp_node.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >= 0:
            return self._right_rotate(root)

        if balance < -1 and self.balance(root.right) <= 0:
            return self._left_rotate(root)

        if balance > 1 and self.balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _left_rotate(self, z):
        y = z.right
        a = y.left

        y.left = z
        z.right = a

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        b = y.right

        y.right = z
        z.left = b

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def _min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def _search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self._search(root.right, value)
        return self._search(root.left, value)

    def insert(self, value):
        if self.index(value) == None:
            self.root = self._insert(self.root, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def index(self, value):
        return self._search(self.root, value)
    
    def _lower_search(self, root, value, answer):
        if not root:
            return answer
        
        if root.value <= value:
            answer = root
            return self._lower_search(root.right, value, answer)
        return self._lower_search(root.left, value, answer)
    
    def _higher_search(self, root, value, answer):
        if not root:
            return answer
        
        if root.value >= value:
            answer = root
            return self._higher_search(root.left, value, answer)

        return self._higher_search(root.right, value, answer)
    
    def lower_bound(self, value):
        return self._lower_search(self.root, value, None)
    
    def upper_bound(self, value):
        return self._higher_search(self.root, value, None)
    
    def _inorder(self, root, array):
        if not root:
            return
        
        self._inorder(root.left, array)
        array.append(root)
        self._inorder(root.right, array)


    def __repr__(self):
        array = []
        self._inorder(self.root, array)

        return f"SortedSet({array})"


sortedset = AVLTree()

sortedset.insert(1)
sortedset.insert(2)
sortedset.insert(3)
# sortedset.insert(4)
sortedset.insert(5)
sortedset.insert(5)
sortedset.insert(5)
# sortedset.delete_value(5)
# sortedset.delete_value(9)
print(sortedset)
print(sortedset.lower_bound(4))
print(sortedset.upper_bound(4))