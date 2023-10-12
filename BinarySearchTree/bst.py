from queue3 import *
class bst:
    class _Node:
        def __init__(self,ele):
            self.data=ele
            self.left=None
            self.right=None
    def __init__(self):
        self.root=None
        self.count=0
    def isEmpty(self):
        return self.count==0
    def getNodecount(self):
        return self.count
#  Design data structure for Binary Search Tree. Write methods for adding node into BST.
    def addNode(self,ele):
        cur=parent=self.root
        while cur!=None and cur.data!=ele:
            parent=cur
            if ele<cur.data:
                cur=cur.left
            else:
                cur=cur.right
        if cur==None:
            new_node=self._Node(ele)
            if parent==None:
                self.root=new_node
            elif ele<parent.data:
                parent.left=new_node
            elif ele>parent.data:
                parent.right=new_node
            self.count+=1

#  Implement following tree traversals
# a. Inorder
# b. Preorder
# c. Postorder
# d. Levelorder

    #inorder traversal
    def inorder(self):
        a=[]
        if not self.isEmpty():
            self._inOrder(self.root,a)
        return a
    def _inOrder(self,node,l):
        if node!=None:
            self._inOrder(node.left,l)
            l.append(node.data)
            self._inOrder(node.right,l)
    
    
    #Preorder Traversal
    def preorder(self):
        a=[]
        if not self.isEmpty():
            self._preOrder(self.root,a)
        return a
    def _preOrder(self,node,l):
        if node!=None:
            l.append(node.data)
            self._preOrder(node.left,l)
            self._preOrder(node.right,l)
        
    
    #Postorder Traversal
    def postorder(self):
        a=[]
        if not self.isEmpty():
            self._postOrder(self.root,a)
        return a
    def _postOrder(self,node,l):
        if node!=None:
            self._postOrder(node.left,l)
            self._postOrder(node.right,l)
            l.append(node.data)
        
        
    #Levelorder Traversal
    def LevelOrder(self):
        if not self.isEmpty():
            l=[]
            q1=flexiQueue()
            q1.enqueue(self.root)
            while not q1.isEmpty():
                node=q1.dequeue()
                l.append(node.data)
                if node.left:
                    q1.enqueue(node.left)
                if node.right:
                    q1.enqueue(node.right)
            return l
        else:
            return None
    # Write method to find the height of BST 
    def findHeight(self):
        return self._findHeight(self.root)

    def _findHeight(self, node):
        if node is None:
            return -1
        left_height = self._findHeight(node.left)
        right_height = self._findHeight(node.right)
        return max(left_height, right_height) + 1

# Write method to count number of terminal nodes
    def getLeafCount(self):
        if not self.isEmpty():
            return (self._leaf_count_(self.root))
        else:
            return 0
    def _leaf_count_(self,node):
        if node:
            if self._isLeafNode_(node):
                return 1
            else:
                return (self._leaf_count_(node.left)+self._leaf_count(node.right))
        else:
            return 0
    def _isLeafNode_(node):
        if node.left==None and node.right==None:
            return True
        else:
            return False
# Write method to delete specified node from BST
    def deleteNode(self,key):
        if not self.isEmpty():
            self.root=self._nodeDelete(self.root,key)
            return self.count
        else:
            return None
    def _nodeDelete(self,node,key):
        if node==None:
            return None
        elif key<node.data:
            node.left=self._nodeDelete(node.left,key)
        elif key>node.data:
            node.right=self._nodeDelete(node.right,key)
        else:
            if node.left and node.right:
                temp=self._findMin(node.right)
                node.data=temp.data
                node.right=self._nodeDelete(node.right,temp.data)
            else:
                if node.right==None:
                    node=node.left
                else:
                    node=node.left
            self.count-=1
    def _findMin(self,node):
        if node.left==None:
            return node
        else:
            return self._findMin(node.left)

# Write method to traverse the BST in descending order
    def descendingOrder(self):
        result = []
        self._descendingOrder(self.root, result)
        return result

    def _descendingOrder(self, node, result):
        if node is not None:
            self._descendingOrder(node.right, result)
            result.append(node.data)
            self._descendingOrder(node.left, result)


b1=bst()
assert(b1.isEmpty()==True)
assert(b1.getNodecount()==0)
b1.addNode(45)
b1.addNode(30)
b1.addNode(50)
assert(b1.getNodecount()==3)
assert(b1.inorder()==([30,45,50]))
assert(b1.preorder()==([45,30,50]))
assert(b1.postorder()==([30,50,45]))
assert(b1.LevelOrder()==([45,30,50]))
b1.addNode(25)
b1.addNode(40)
b1.addNode(60)
b1.addNode(55)
assert(b1.findHeight()==3)
assert(b1.getNodecount()==7)
assert(b1.deleteNode(55)==6)
assert(b1.getLeafCount()==3)
assert(b1.descendingOrder()==([60,50,45,40,30,25])) 