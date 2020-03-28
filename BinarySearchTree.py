from BinaryTree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            def helper(node):
                if node.value < value:
                    if node.left is None:
                        node.left = Node(value)
                    else:
                        helper(node.left)
                elif node.value > value:
                    if node.right is None:
                        node.right = Node(value)
                    else:
                        helper(node.right)
                else:
                    print("Already in BST.")
            helper(self.root)

    def find(self, value):
        if self.root is None:
            print("Not found.")
        else:
            def helper(node):
                if node.value < value:
                    if node.left is None:
                        print("Not found.")
                    else:
                        helper(node.left)
                elif node.value > value:
                    if node.right is None:
                        print("Not found.")
                    else:
                        helper(node.right)
                else:
                    print("found")
            helper(self.root)

    def delete(self, value):
        if self.root is None:
            print("Empty tree")
        else:
            def helper(node):
                if node is not None:
                    if node.value == value:
                        node = BinarySearchTree.merge(node.left, node.right)
                        return node
                    elif node.left is not None and node.value > value:
                        helper(node.left)
                    elif node.left is not None and node.value < value:
                        helper(node.right)
            helper(self.root)

    def is_bst(self):
        if self.root is None:
            return True
        else:
            def helper(node):
                if node.left is None and node.right is None:
                    return True
                elif node.left is not None:
                    if node.left.value < node.value:
                        helper(node.left)
                    else:
                        return False
                elif node.right is not None:
                    if node.right.value > node.value:
                        helper(node.right)
                    else:
                        return False
            helper(self.root)

    @staticmethod
    def merge(node1, node2):
        node = Node(None)
        if node1 is None:
            return node2
        elif node2 is None:
            return node1
        else:
            if node1.value < node2.value:
                node = Node(node1.value)
                node.left = node1.left
                node.right = BinarySearchTree.merge(node2, node1.right)
            elif node1.value > node2.value:
                node = Node(node2.value)
                node.left = node2.left
                node.right = BinarySearchTree.merge(node1, node2.right)
            else:
                print("No duplicates.")
        return node

    def from_list(self, items):
        for item in items:
            self.insert(item)


binarySearchTree1 = BinarySearchTree()
binarySearchTree2 = BinarySearchTree()
binarySearchTree2.from_list([2, 3, 1, 4, 5])
binarySearchTree1.insert(1)
binarySearchTree1.insert(2)
binarySearchTree1.insert(3)
binarySearchTree1.find(2)
binarySearchTree1.find(4)
binarySearchTree2.find(4)
binarySearchTree2.delete(4)
print(binarySearchTree1.print_tree("postorder"))
print(binarySearchTree2.print_tree("postorder"))
binarySearchTree3 = BinarySearchTree()
binarySearchTree3.root = BinarySearchTree.merge(binarySearchTree1.root, binarySearchTree2.root)
print(binarySearchTree3.print_tree("postorder"))





