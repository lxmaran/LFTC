class TreeNode:
    def __init__(self, key, value):
        self.left = None
        self.key = key
        self.right = None
        self.data = value


class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, key, value):
        if node is None:
            self.root = TreeNode(key, value)
        else:
            if value < node.data:
                if node.left is None:
                    node.left = TreeNode(key, value)
                else:
                    self.addNode(node.left, key, value)
            else:
                if node.right is None:
                    node.right = TreeNode(key, value)
                else:
                    self.addNode(node.right, key, value)

    def printInorder(self, node):
        if node is not None:
            self.printInorder(node.left)
            print(node.data, node.key)
            self.printInorder(node.right)

    def getByKey(self, node, key):
        if node is not None:
            if node.key == key:
                return node
            left = self.getByKey(node.left, key)
            right = self.getByKey(node.right, key)
            if left:
                return left
            if right:
                return right

    def search(self, k):
        node = self.root
        while node is not None:
            if node.data == k:
                return node
            if node.data > k:
                node = node.left
            else:
                node = node.right
        return None

