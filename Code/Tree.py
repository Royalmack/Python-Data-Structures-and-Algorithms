#Tree
class Node:
    def __init__(self, value, left = None, right = None):
        self.key = value
        self.left = left
        self.right = right

    def getKey(self):
        return self.key

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right
    
class Tree:
    def __init__(self):
        self.root = None

    def generateTree(self):
        self.root = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))

    def getLeftChild(self):
        return self.root.getLeftChild()

    def getRightChild(self):
        return self.root.getRightChild()

    def depthFirst(self ,n = None):
        if n == None:
            temp = self.root
        else:
            temp = n

        print(temp.getKey())
        
        if temp.getLeftChild() != None:
            self.depthFirst(temp.getLeftChild())
        if temp.getRightChild() != None:
            self.depthFirst(temp.getRightChild())

    def breadthFirst(self):
        currentLevel = [self.root]

        while currentLevel:
            nextLevel = []
            for n in currentLevel:
                print(n.getKey())

                if n.getLeftChild():
                    nextLevel.append(n.getLeftChild())
                if n.getRightChild():
                    nextLevel.append(n.getRightChild())
            currentLevel = nextLevel
                
        
r = Tree()

r.generateTree()
r.depthFirst()
r.breadthFirst()
