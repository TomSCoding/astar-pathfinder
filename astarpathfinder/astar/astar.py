from queue import PriorityQueue

# G Cost - how far away a node is from its starting point.
# H Cost - how far the node is from the end node.
# F Cost - combination of G + H Cost.

# HOW IT WORKS
# 1. Algorithm Choses node with lowest F Cost continiously
# 2. If two nodes have same F Cost it goes for the one with the lowest H cost.
# 3. When algorithm reaches target it traces back to starting Node.

# Gets the first start state
class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent: 
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
    
    def GetDist(self):
        pass
    def CreateChildren(self):
        pass


class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        # Init state class
        super(State_String, self).__init__(value, parent, start, goal)
        # Override distance var using get distance method - distance to goal
        self.dist = self.GetDist()

    # Gets distance to goal
    def GetDist(self):
        # Checks if we have reached goal
        if self.value == self.goal:
            return 0
        dist = 0
        # Goes through every letter of the goal 
        for i in range(len(self.goal)):
            # Get current letter
            letter = self.goal[i]
            # Gets the current index of that letter in the current value
            dist += abs(i - self.value.index(letter))
        return dist

    #Generates Children
    def CreateChildren(self):
        # Checks if children exist
        if not self.children:
            # Going through every possible arrangement of letters
            for i in range(len(self.goal)-1):
                val = self.value
                # Switching every second letter with every first letter of every pair of letters
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                # Create child / pass in every value generated into child + pass self to store parent of child
                child = State_String(val, self)
                # Add child to children method
                self.children.append(child)


class AStar_Solver:
    def __init__(self, start , goal):
        # Stores solution to getting from start state to goal state
        self.path          = []
        # Keeps track of children visited / prevent 2nd visit
        self.visitedQueue  = []
        self.priorityQueue = PriorityQueue()
        self.start         = start
        self.goal          = goal

    def Solve(self):
        # Create start state
        startState = State_String(self.start,
                                  0,
                                  self.start,
                                  self.goal)
        # Id for keeping track of children                          
        count = 0
        self.priorityQueue.put((0,count,startState))
        # While path is empty
        # While priority queue has size 
        # 

        while(not self.path and self.priorityQueue.qsize()):
            # Gets the top most value in priority queue
            closestChild = self.priorityQueue.get()[2]
            # Creates children for the state
            closestChild.CreateChildren()
            # Add child to visisted queue
            self.visitedQueue.append(closestChild.value)
            # Go through every child in created state
            for child in closestChild.children:
                #If this child has not been visited or in visite queue
                if child.value not in self.visitedQueue:
                    # Add id of nodes
                    count +=1
                    # If childs distance is at 0 and does not exist
                    if not child.dist:
                        # Set self path to child path
                        self.path = child.path
                        # Breaks out of if
                        break
                    self.priorityQueue.put((child.dist,count,child))
        # (Error Handler)If once finished searching not found path yet - no more children
        if not self.path:
            print("Goal of %s is not possible!" % (self.goal))
        # Return path
        return self.path


if __name__ == "__main__":
    start1 = "135764"
    goal1  = "645731"
    print("Starting...")

    a = AStar_Solver(start1, goal1)
    a.Solve()

    for i in range(len(a.path)):
        print("{0}) {1}".format(i, a.path[i]))

