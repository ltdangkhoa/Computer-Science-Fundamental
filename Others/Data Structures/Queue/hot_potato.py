"""
hot_potato.py
"""
class Queue:
    """
    class Queue
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """isEmpty"""
        return self.items == []

    def enqueue(self, item):
        """enqueue"""
        self.items.insert(0, item)

    def dequeue(self):
        """dequeue"""
        return self.items.pop()

    def size(self):
        """size"""
        return len(self.items)

def hot_potato(namelist, num):
    """
    hotPotato
    """
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for _ in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
