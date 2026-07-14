class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def add(self, node):
        temp=self.head.next
        node.next=temp
        node.prev=self.head
        self.head.next=node
        temp.prev=node
    
    def delete(self, node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p

    def get(self, key: int) -> int:
        if key in self.cache:
            r=self.cache[key]
            a=r.value
            self.delete(r)
            self.add(r)
            return a
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            c=self.cache[key]
            del self.cache[key]
            self.delete(c)
        if len(self.cache)==self.capacity:
            del self.cache[self.tail.prev.key]
            self.delete(self.tail.prev)
        self.add(Node(key, value))
        self.cache[key]=self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)