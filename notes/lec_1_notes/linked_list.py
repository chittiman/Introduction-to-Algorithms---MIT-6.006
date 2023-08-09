class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def build(self,X):
        prev_node = None
        for item in reversed(X):
            pres_node = LinkedListNode(item)
            pres_node.next = prev_node
            self.size += 1
            prev_node = pres_node
        self.head = prev_node

        # Alt implementation
        # for a in reversed(X):
        #     self.insert_first(a)

    def __iter__(self):
        node = self.head
        for _ in range(len(self)):
            item = node.item
            node = node.next
            yield item
        # Alt implementation
        # node = self.head
        # while node:
        #     yield node.item
        #     node = node.next

    def __getitem__(self,i):
        if 0<=i<len(self):
            return self.head.later_node(i).item
        else:
            raise Exception('Index is out of range')
        
    def __setitem__(self,i,x):
        if 0<=i<len(self):
            self.head.later_node(i).item = x
        else:
            raise Exception('Index is out of range')
        
    def insert_first(self,x):
        node = LinkedListNode(x)
        node.next = self.head
        self.head = node
        self.size += 1

    def delete_first(self):
        if len(self) > 0:
            del_node = self.head
            new_first_node = del_node.next
            self.head = new_first_node
            self.size -= 1 
            return del_node.item
        else:
            raise Exception('Index is out of range')
        
    def insert_at(self,i,x):
        if i==0:
            self.insert_first(x)
        elif i<=len(self):
            prev_node = self.head.later_node(i-1)
            new_node = LinkedListNode(x)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
        else:
            raise Exception('Index is out of range')
        
    def delete_at(self,i):
        if i==0:
            return self.delete_first()
        elif i<len(self):
            prev_node = self.head.later_node(i-1)
            del_node = prev_node.next
            prev_node.next = del_node.next
            self.size -= 1
            return del_node.item
        else:
            raise Exception('Index is out of range')
    #len iter build get_at set_at insert_delet at first last

class LinkedListNode:
    def __init__(self,item):
        self.item = item
        self.next = None

    def later_node(self,i):
        if i==0:
            return self
        else:
            next_node = self.next
            if next_node:
                return next_node.later_node(i-1)
            else:
                raise Exception(f'Later Node is None for {self}')
    
    def __repr__(self) -> str:
        return f'Node(item = {self.item})'

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.build([1, 2, 3])
    deleted_item = linked_list.delete_at(0)
    assert len(linked_list) == 2
    assert deleted_item == 1
    assert linked_list.head.item == 2

    