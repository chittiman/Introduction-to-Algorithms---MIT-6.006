class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        first_node = Doubly_Linked_List_Node(x)
        next_node = self.head
        first_node.next = next_node
        self.head = first_node
        if next_node:
            next_node.prev = first_node
        else:
            self.tail = self.head
        ###########################
        return None

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        last_node = Doubly_Linked_List_Node(x)
        prev_node = self.tail
        last_node.prev = prev_node
        self.tail = last_node
        if prev_node:
            prev_node.next = last_node
        else:
            self.head = self.tail
        ###########################
        return None

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        if self.head:
            del_node = self.head
            next_node = del_node.next
            self.head = next_node
            if next_node:
                next_node.prev = None
            else:
                self.tail = self.head
            x = del_node.item    
        ###########################
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        if self.tail:
            del_node = self.tail
            prev_node = del_node.prev
            self.tail = prev_node
            if prev_node:
                prev_node.next = None
            else:
                self.head = self.tail
            x = del_node.item
        ###########################
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! #
        prev_node = x1.prev
        next_node = x2.next

        if  prev_node:
            prev_node.next = x2.next
        else:
            self.head = x2.next

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        L2.head = x1
        x1.prev = None
        L2.tail = x2
        x2.next = None
        ###########################
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 

        if L2.head is None:
            return None

        L2.tail.next = x.next
        if x.next:
            x.next.prev = L2.tail
        else:
            self.tail = L2.tail

        x.next = L2.head
        L2.head.prev = x

        L2.head = L2.tail = None

        # next_node = x.next
        # L2.next = next_node
        # if next_node:
        #     next_node.prev = L2.tail
        # else:
        #     self.tail = L2.tail

        # x.next = L2.head
        # L2.head.prev = x

        ###########################
        return None
