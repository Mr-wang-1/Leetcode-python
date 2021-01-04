class ListNode:
    def __init__(self, key, val):
        self.key, self.val, self.prev, self.next = key, val, None, None

class MyOrderedDict:
    """ 哈希表 + 双向链表实现有序字典
    - 双向链表，记录键值插入顺序
    - 哈希表，记录键与节点映射关系，以O(1)复杂度查找、删除节点
    """
    def __init__(self):
        self.head, self.tail = ListNode(0, 0), ListNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.lookup = {} # 记录键与节点映射关系

    def delete(self, node): # 删除节点
        self.lookup.pop(node.key)
        node.prev.next, node.next.prev = node.next, node.prev

    def append(self, node): # 插入节点
        self.lookup[node.key] = node
        cur, pre = self.tail, self.tail.prev
        node.next, node.prev = cur, pre
        pre.next, cur.prev = node, node

    def move_to_end(self, key):
        node = self.lookup[key]
        self.delete(node)
        self.append(node)

    def pop(self, key):
        if len(self.lookup) == 0:
            raise Exception('Empty dict')
        node = self.lookup[key]
        self.delete(node)
        return node.val

    def popitem(self, last=True):
        if len(self.lookup) == 0:
            raise Exception('Empty dict')

        if last:
            node = self.tail.prev
        else:
            node = self.head.next
        self.delete(node)
        return node.val

    def __len__(self):
        return len(self.lookup)

    def __contains__(self, key) -> bool:
        return key in self.lookup

    def __setitem__(self, key: int, value: int) -> None:
        """ 存在更新，不存在则插入 """
        if key in self.lookup:
            self.lookup[key].val = value
        else:
            self.append(ListNode(key, value))

    def __getitem__(self, key: int) -> int:
        """ 存在返回键对应值，否则返回 -1 """
        if key in self.lookup:
            return self.lookup[key].val
        else:
            return -1

    def get(self, key: int, default=None):
        if key in self.lookup:
            return self.lookup[key].val
        return default

    def __iter__(self):
        cur = self.head.next
        while cur != self.tail:
            yield cur
            cur = cur.next

    def __str__(self):
        res = []
        for node in self:
            res.append((node.key, node.val))
        return "MyOrderedDict({})".format(str(res))

class LRUCache:
    """ 有序字典实现LruCache """
    def __init__(self, capacity: int):
        self.lru_cache = MyOrderedDict()
        self.maxsize = capacity

    def get(self, key: int) -> int:
        """ 存在key 移动到末尾并返回对应值， 否则返回-1"""
        if key in self.lru_cache:
            self.lru_cache.move_to_end(key)
        return self.lru_cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
            self.lru_cache.pop(key)
        if len(self.lru_cache) == self.maxsize: # 缓存满
            self.lru_cache.popitem(last=False)
        self.lru_cache[key] = value
