class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = list() #Using a list for people with same first name


def addGuest(root, guest):
    if guest < root.data[0]:
        if root.left is None:
            root.left = Node()
            root.left.data.append(guest)
        else:
            addGuest(root.left, guest)
    else:
        if guest > root.data[0]:
            if root.right is None:
                root.right = Node()
                root.right.data.append(guest)
            else:
                addGuest(root.right, guest)
        else:
            root.data.append(guest)


def printGuest(root):
    if root is None:
        return
    print(root.data)
    printGuest(root.left)
    printGuest(root.right)


root = Node()
root.data.append('M')

for i in range(0, 5):
    addGuest(root, raw_input('Add guest: '))

print("Left Side:")
printGuest(root.left)
print("Right Side:")
printGuest(root.right)
