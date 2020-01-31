class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare value with root node
        if value < self.value:
            # If lesser go left child
            if self.left is None:
                self.left = BinarySearchTree(value)
            # If something is already there, recurse
            else:
                self.left.insert(value)

        else:  # value is >= root node
            # If greater or equal go right child
            if self.right is None:
                self.right = BinarySearchTree(value)
            # If something is already there, recurse
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
