#  File: ExpressionTree.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        stck= Stack()
        self.root=Node()
        current_node=self.root

        lst=[]
        i=0
        while i<len(expr)-1:
            str=''
            if expr[i]!=' ':
                while expr[i]!=' ':
                    str=str+expr[i]
                    i+=1
                lst.append(str)
            else:
                i+=1
        





        for item in lst:

            if item== '(':
                current_node.lChild=Node()
                stck.push(current_node)
                current_node=current_node.lChild
            elif item in operators:
                current_node.data=item
                stck.push(current_node)
                current_node.rChild=Node()
                current_node=current_node.rChild
            elif item==')' and stck.is_empty()==False:
                current_node=stck.pop()
            else:
                current_node.data=item
                current_node=stck.pop()

    def opp(self,x,y,z):
        if z== '+':
            return x + y
        if z== '-':
            return x - y
        if z== '*':
            return x * y
        if z== '/':
            return x / y
        if z== '%':
            return x % y
        if z== '**':
            return x ** y
        if z== '//':
            return x // y
        



    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode.lChild==None and aNode.rChild ==None:
            return aNode.data
        
        x= self.evaluate(aNode.lChild)
        y=self.evaluate(aNode.rChild)
        z=aNode.data

        return self.opp(float(x),float(y),z)
        












    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        stck= Stack()
        stck.push(aNode)
        str=''
        while stck.is_empty()==False:
            node=stck.pop()
            str=str+node.data+' '
            if node.rChild!= None:
                stck.push(node.rChild)
            if node.lChild!= None:
                stck.push(node.lChild)
        return str


       

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation

    def post_order (self, aNode,str=''):
        stck= Stack()
        stck.push(aNode)
        fin=[]
        
        while stck.is_empty()==False:
            node=stck.pop()
            fin.append(node.data+' ')
            if node.lChild!= None:
                stck.push(node.lChild)
            if node.rChild!= None:
                stck.push(node.rChild)
        
        str=''
        for thing in fin:
            str=thing+str

        return str
        

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
