class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

    def insertAfter(self, node):
        node.next = self.next
        self.next = node

    def deleteAfter(self):
        if self.next is None:
            return
        else:
            pp = self.next
            self.next = pp.next
            pp.next = None
            del pp


if __name__ == '__main__':
    head = Node(0)
    p = head
    for i in range(1, 10):
        n = Node(i)
        p.insertAfter(n)
        p = n

    p = head

    while True:
        if p.data == 3:
            p.insertAfter(Node(3.5))
            break
        else:
            p = p.next

    p = head

    while True:
        if p.data == 7:
            p.deleteAfter()
            break
        if p.next is None:
            break

    p = head
    while True:
        print(p.data)
        if p.next is None:
            break
        p = p.next
