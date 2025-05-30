class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if not root:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
    
bst_root = None
for val in [50, 30, 20, 40, 70, 60, 80]:
    bst_root = insert(bst_root, val)
    
print("Inorder of BST: ", end="")
inorder(bst_root)  # Should print in sorted order

print("\nSearch 60:", search(bst_root, 60))  # True
print("Search 25:", search(bst_root, 25))    # False