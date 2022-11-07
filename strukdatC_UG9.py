class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority 

class PriorityQueueSortedList:
    def __init__(self):
        self._data =[]
        self._size = 0

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def peek(self):
        print(self._data[0])
    
    def add(self,data,priority):
        baru = Node(data,priority)
        self._data.append(list([baru._data,baru._priority]))
        self._data.sort(key=lambda a: a[1])

    def removePriority(prio):
        pass

    def printIsiQueue(self):
        for i in range(0,len(self._data)):
            print(self._data[i], end=" ")
        print()

sortedList = PriorityQueueSortedList() 
sortedList.add("Shalom", 5) 
sortedList.add("Beatrix", 1) 
sortedList.add("Sindu", 3) 
sortedList.add("Hanif", 2) 
sortedList.add("Dedi", 4) 
# sortedList.update(4, "Karin") 
# sortedList.update(3, "Rafi") 
# sortedList.remove() 
# sortedList.removePriority(4) 
sortedList.peek() 
sortedList.printIsiQueue()