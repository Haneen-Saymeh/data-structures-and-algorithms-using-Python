class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
 
def insert(root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = insert(root.right, key)
            else:
                root.left = insert(root.left, key)
        return root
 

def inorder(root):
        if root:
            inorder(root.left)
            print(root.val)
            inorder(root.right)

def preorder(root):
        if root:
            print(root.val)
            preorder(root.left)
            preorder(root.right)

def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.val)

def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
            
 
 


 
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
# Print inoder traversal of the BST
inorder(r)
print("---------")
preorder(r)
print("---------")
postorder(r)
print(search(r,20))
