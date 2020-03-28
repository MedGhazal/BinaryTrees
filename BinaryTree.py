from Queue import Queue
from Stack import Stack


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root)
        elif traversal_type == "reverse levelorder":
            return self.reverse_levelorder_print(self.root)
        else:
            print("Traversal type " + traversal_type + " is not supported.")

    def preorder_print(self, start, traversal):
        """root -> Left -> right"""
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left -> root -> right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left -> right -> root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + " ")
        return traversal

    @staticmethod
    def levelorder_print(start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            traversal += str(queue.peek().value) + " "
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    @staticmethod
    def reverse_levelorder_print(start):
        if start is None:
            return

        q = Queue()
        s = Stack()
        q.enqueue(start)
        traversal = ""

        while len(q) > 0:
            node = q.dequeue()
            s.push(node)
            if node.right:
                q.enqueue(node.right)
            if node.left:
                q.enqueue(node.left)

        while len(s) > 0:
            node = s.pop()
            traversal += str(node.value) + " "

        return traversal

    def height(self, node):
        if node is None:
            return -1
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.left) + self.size(node.right) + 1