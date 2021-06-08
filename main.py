# Red Black Tree implementation in Python 2.7
# Author: Algorithm Tutor
# Tutorial URL: https://algorithmtutor.com/Data-Structures/Tree/Red-Black-Trees/

import sys


# data structure that represents a node in the tree
class Node():
    def __init__(self, data):
        self.data = data  # holds the key
        self.parent = None  # pointer to the parent
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child
        self.color = 1  # 1 . Red, 0 . Black


# class RedBlackTree implements the operations in Red Black Tree
class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # def __pre_order_helper(self, node):
    #     if node != self.TNULL:
    #         sys.stdout.write(node.data + " ")
    #         self.__pre_order_helper(node.left)
    #         self.__pre_order_helper(node.right)
    #
    # def __in_order_helper(self, node):
    #     if node != TNULL:
    #         self.__in_order_helper(node.left)
    #         sys.stdout.write(node.data + " ")
    #         self.__in_order_helper(node.right)
    #
    # def __post_order_helper(self, node):
    #     if node != TNULL:
    #         self.__post_order_helper(node.left)
    #         self.__post_order_helper(node.right)
    #         sys.stdout.write(node.data + " ")

    def __search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)



    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # fix the red-black tree
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 1:
                    # case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # case 3.2.2
                        k = k.parent
                        self.right_rotate(k)
                    # case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 1:
                    # mirror case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # mirror case 3.2.2
                        k = k.parent
                        self.left_rotate(k)
                    # mirror case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print
            str(node.data) + "(" + s_color + ")"
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)




    def searchTree(self, k):
        return self.__search_tree_helper(self.root, k)

    # find the node with the minimum key
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    # find the node with the maximum key
    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node




    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # insert the key to the tree in its appropriate position
    # and fix the tree
    def insert(self, key):
        # Ordinary Binary Search Insertion
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  # new node must be red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent == None:
            node.color = 0
            return

        # if the grandparent is None, simply return
        if node.parent.parent == None:
            return
        self.fix_insert(node)

    def get_root(self):
        return self.root






if __name__ == "__main__":

   rbt = RedBlackTree()
   dictf = open('EN-US-Dictionary.txt', 'r')
   dictionary = dictf.readlines()
   for key in dictionary:
       rbt.insert(key)
   while True:
       print("1-Search\n2-Insert\n3-Tree Height\n4-Tree Size\n5-Exit")
       choice = input(">")
       if choice.lower() == 'search':
           key = input("Search for Key: ")
       elif choice.lower() == 'insert':
           key = input("Insert Key: ")
       elif choice.lower() == 'tree height':
           print("Tree Height:")
       elif choice.lower() == 'tree size':
           print("Tree Size:")

       elif choice.lower() == 'exit':
           print("------Terminating Program------")
           break
       else:
           print("Not a Valid Choice!")
