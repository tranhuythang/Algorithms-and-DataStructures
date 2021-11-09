class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, obj):
        self.children.append(obj)

n8 = Node("8")
n4 = Node("4")
n6 = Node("6")
n10 = Node("10")
n2 = Node("2")
n1 = Node("1")
n20 = Node("20")
n8.add(n4)
n8.add(n6)
n8.add(n10)
n4.add(n2)
n4.add(n1)
n4.add(n20)