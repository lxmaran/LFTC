from BinaryTree import *


def main():
    testTree = Tree()
    testTree.addNode(testTree.root, 1, "w")
    testTree.addNode(testTree.root, 2, "b")
    testTree.addNode(testTree.root, 3, "a")
    testTree.addNode(testTree.root, 4, "f")
    testTree.printInorder(testTree.root)

    b = testTree.getByKey(testTree.root, 4)
    print(b.data)


main()
