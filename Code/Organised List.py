#Organised List
class Node:
    def __init__(self, value = 0):
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

class OrganisedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addNode(self, value):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() < value:
                previous = current
                current = current.getNext()
            else:
                stop = True

        temp = Node(value)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            previous.setNext(temp)
            temp.setNext(current)

    def search(self, item):
        current = self.head

        while current != None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
            
        return False

    def remove(self, value):
        current = self.head
        previous = None
        deleted = False

        while current != None and deleted is False:
            if current.getData() == value:
                deleted = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = self.head.getNext()
        else:
            previous.setNext(current.getNext())                

    def printList(self):
        current = self.head

        while current != None:
            print(current.getData())
            current = current.getNext()

    def size(self):
        count = 0
        current = self.head

        while current != None:
            count += 1
            current = current.getNext()

        return count

myList = OrganisedList()

myList.addNode(5)
myList.addNode(2)
myList.addNode(7)
myList.addNode(1)
myList.addNode(71)
myList.addNode(18)

print(myList.search(7))
print(myList.search(23))


myList.printList()
print(myList.size())

myList.remove(18)
myList.remove(1)

myList.printList()
print(myList.size())



                
                
