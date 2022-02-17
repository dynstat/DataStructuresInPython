class student:
    def __init__(self, name, rollno, age):
        self.name = name
        self.rollno = rollno
        self.age = age

    def viewinfo(self):
        print(
            f"student name = {self.name}, rollno = {self.rollno}, age = {self.age}")

    @staticmethod
    def printAge(any_age):
        print(f"The age is {any_age}")

    @classmethod
    def changeinfo(cls, new_name, new_rollno, new_age):
        return cls(new_name, new_rollno, new_age)


# st1 = student('kanchan', 5, 24)
# st2 = student('Vivek', 6, 28)

# st1.viewinfo()
# new_st1 = st1.changeinfo('Bubbly', 5, 25)
# new_st1.viewinfo()


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# L->r->R


def traversal(rootnode):
    if rootnode is None:
        return
    traversal(rootnode.left)
    print(rootnode.data, end=' ')
    traversal(rootnode.right)


def add_new(rootnode, value):
    if rootnode is None:
        rootnode = Node(value)
        return
    store = []
    store.append(rootnode)
    while(len(store)):
        rootnode = store.pop(0)
        if rootnode.left is None:
            rootnode.left = Node(value)
            break
        else:
            store.append(rootnode.left)

        if rootnode.right is None:
            rootnode.right = Node(value)
            break
        else:
            store.append(rootnode.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(5)

    root.right = Node(12)
    root.right.left = Node(7)
    root.right.right = Node(4)

    add_new(root, 9)
    traversal(root)
