class LRUCache:
    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cacheMap = {}
    
    def addNode(self,newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode
    
    def deleteNode(self,delNode):
        temp = delNode.prev
        nextt = delNode.next
        temp.next = nextt
        nextt.prev = temp

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            resNode = self.cacheMap[key]
            res = resNode.val
            del self.cacheMap[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.cacheMap[key] = self.head.next
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            curr = self.cacheMap[key]
            del self.cacheMap[key]
            self.deleteNode(curr)

        if len(self.cacheMap) == self.cap:
            del self.cacheMap[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key, value))
        self.cacheMap[key] = self.head.next 




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)