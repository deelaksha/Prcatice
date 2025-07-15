class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
 

class LinkedList:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self.insert_helper(self.root,data)
    
    def insert_helper(self,root,data):
        if root is None:
            return Node(data)
        elif data<root.data:
            root.left=self.insert_helper(root.left,data)
        elif data>root.data:
            root.right=self.insert_helper(root.right,data)
        return root
    def inorder(self):
        self.inorder_helper(self.root)
    def inorder_helper(self,temp):
        if temp==None:
            return
        print(temp.data)
        self.inorder_helper(temp.left)
        self.inorder_helper(temp.right)    

list=LinkedList()
list.insert(40)        
list.inorder()
    

   
