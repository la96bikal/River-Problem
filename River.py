import queue

class State:
    sShore=[]
    nShore=[]

    # contructor initializes to the given state
    def __init__(self,southShore, northShore, parent=None):
        #The south and the north shore
        # I am converting all the list to sets to remove duplicates
        # after that i am converting a set back to list to fit the other functions that require list as a parameter
        toSetS = list(set(southShore))
        toSetN = list(set(northShore))
        toSetS.sort()
        toSetN.sort()
        self.sShore = toSetS
        self.sShore.sort()
        self.nShore = toSetN
        self.nShore.sort()
        self.parent=parent

    # To check if the node is the goal state
    def goal(self):
        if self.sShore == [''] and self.nShore == ['C','D','F','W']:
            return True
    # To check if the node is the initial state
    def initial(self):
        if self.sShore == ['C','D','F','W'] and self.nShore==['','','','']:
            return True

    #To Print the state of the node
    def showState(self):
        print("In the south Shore::", end='')
        print(self.sShore, end='')
        print("\t\t\t\t\t\t\t",end='')
        print("In the North Shore::", end='')
        print(self.nShore)


    # function to check whether a state is valid
    def isValid(self):
        if(self.sShore == ['','D','W'] or self.sShore == ['','C','D'] or self.sShore==['','C','D','W'] or self.sShore == ['D','W'] or self.sShore==['C','D']):
            fCondition = False
        else:
            fCondition = True

        if (self.nShore == ['','D', 'W'] or self.nShore == ['','C', 'D'] or self.nShore == ['','C', 'D', 'W']
        or self.nShore == ['D','W'] or self.nShore == ['C','D']):
            sCondition = False
        else:
            sCondition = True

        if (fCondition and sCondition):
            return True
        else:
            return False

    #overloading the equality operator for comparing the nodes later on
    def __eq__(self, other):
	    if (self.sShore == other.sShore and self.nShore == other.nShore):
                return True




#function to evaluate children of a state. Here while evaluating the children, only valid children were chosen. All the invalid
# ones are filtered out before Breadth first is implemented. This way, redundancy in the tree is avoided and traversal cost is minimized
def rowBoat(cState):
    children = []
    south = cState.sShore[:]
    north = cState.nShore[:]
    # either the boat is in south or north. That is determined by the position of Farmer
    # Using the Position of the farmer, I row the boat accordingly
    # This function can find all the successor nodes of a current random state
    if 'F' in south:
        south.remove('F')
        north.append('F')
        child = State(south,north,cState)
        if(child.isValid()):
            children.append(child)
        for i in range(0,len(south)):
            stemp = south[:]
            ntemp = north[:]
            temp = stemp[i]
            ntemp.append(temp)
            del stemp[i]
            child = State(stemp,ntemp,cState)
            if (child.isValid()):
                children.append(child)
        return children
    # if the boat is in north, row south
    if 'F' in north:
        north.remove('F')
        south.append('F')
        child = State(south,north,cState)
        if(child.isValid()):
            children.append(child)
        for i in range(0,len(north)):
            stemp = south[:]
            ntemp = north[:]
            temp = ntemp[i]
            stemp.append(temp)
            del ntemp[i]
            child = State(stemp,ntemp,cState)
            if (child.isValid()):
                children.append(child)
        return children


# Hello this is just a commit
# breadth first search to find the goal state
def BFS(riverP):
    if(riverP.goal()):
        print("Solution Found!")
    discovered = []
    fringe = queue.Queue()
    fringe.put(riverP)
    discovered.append(riverP)
    while (not(fringe.empty())):
        trav = fringe.get()
        if (trav.goal()):
            return trav
        kids=rowBoat(trav)
        for kid in kids:
                if (kid not in discovered):
                    fringe.put(kid)
                    discovered.append(kid)






