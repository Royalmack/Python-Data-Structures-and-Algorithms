#Unorganised List
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, value):
        self.data = value

    def setNext(self, newNext):
        self.next = newNext

class UnorganisedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addNode(self, value):
        temp = Node(value)
        temp.setNext(self.head)
        self.head = temp
        print('Added node with value ' + str(value) + ' to the list')

    def sizeOfList(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, searchItem):
        current = self.head

        while current != None:
            if current.getData() == searchItem:
                return 'Item is in the list'
            current = current.getNext()

        return 'Item not in list'

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def printList(self):
        current = self.head

        while current != None:
            print(current.getData())
            current = current.getNext()               
                

ul = UnorganisedList()
