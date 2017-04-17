#Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, value):
        self.value = value

    def setNext(self, newNext):
        self.next = newNext

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def addToQueue(self, value):
        if self.head == None:
            temp = Node(value)
            self.head = temp
            self.size += 1
        else:
            self.size += 1
            current = self.head
            previous = None
            tail = False

            while current != None and tail is False:
                if current.getNext() != None:
                    previous = current
                    current = current.getNext()
                else:
                    tail = True

            temp = Node(value)

            if previous == None:
                self.head.setNext(temp)
            else:
                current.setNext(temp)

    def pop(self):
        if self.head.getNext() != None:
            print(str(self.head.getValue()) + ' Popped')
            self.head = self.head.getNext()
            self.size -= 1
        else:
            print('Queue is empty')

    def printQueue(self):
        current = self.head

        while current != None:
            print(current.getValue())
            current = current.getNext()

    def sizeOfQueue(self):
        print('size of queue is: ' + str(self.size))

    def search(self, item):
        current = self.head

        while current != None:
            if current.getValue() == item:
                print(str(item) + ' is in the queue')
                return
            else:
                current = current.getNext()
            
        print(str(item) + ' is not in the queue')

    def remove(self, value):
        current = self.head
        previous = None
        found = False

        while current != None and found is False:
            if current.getValue() == value:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = self.head.getNext()
            self.size -= 1
        else:
            previous.setNext(current.getNext())
            self.size -= 1

    def clearQueue(self):
        self.head = None
        self.size = 0

q = Queue()
q.addToQueue(1)
q.addToQueue(2)
q.addToQueue(31)
q.addToQueue(17)

q.printQueue()
q.sizeOfQueue()

q.pop()
q.pop()
q.printQueue()
q.sizeOfQueue()

q.search(31)
q.search(12)

q.addToQueue(20)
q.addToQueue(23)

q.sizeOfQueue()
q.printQueue()

q.remove(20)
q.sizeOfQueue()

q.printQueue()

q.clearQueue()
q.sizeOfQueue()
q.printQueue()
