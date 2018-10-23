# Uses Breadth-first search		 
class BFS(Solver):
    """
     Concrete solver: must implement abstract methods from abstract class Solver
     uses a Queue
    """
    def __init__(self):
        self.queue=Queue()
    def get(self):
        return self.queue.get()
    def add(self,state):
        self.queue.add(state)

# Uses Depth-first search		
class DFS(Solver):
    """
     Concrete solver: must implement abstract methods from abstract class Solver
     Uses a Stack
    """
    def __init__(self):
        self.stack=Stack()
    def get(self):
        return self.stack.pop()
    def add(self,state):
        self.stack.push(state)

# Uses Greedy Best First Heuristic search
class GBFS(Solver):
    """
     Concrete solver 3: must implement abstract methods from abstract class Solver
     Uses the Python built-in Priority Queue
    """
    def __init__(self, goal,numOfJug): # constructor
        self.pq=Q.PriorityQueue() #Q is from the module Queue, the Priority means that the queue is sorted  , w
        self.goal=goal
        self.Jug=numOfJug # essentially the width of the array

    def get(self):
        if not self.pq.empty(): # if the queue aint empty
             (val,state)=self.pq.get() # this retrieves the entries which are of value and board in one set
             return state # returns the board from the queue
        else:
             return None # if the queue is empty, return nothing

    def add(self, state):
        value=self.heuristic(state) # calls the heuristics function below
        self.pq.put((value,state)) # puts the value and the board into the queue

    def heuristic(self,state):
        count=0 # starts with a count of 0
        for x in range(self.Jug): # for loop for the range of how many jugs
                  if self.goal[x]!=state[x]: # if the goal state aint the same as the current board state
                      count += 1 # increment
        return count # return the count
     
#  Game Class (Model): keep track on the abstract game state data. No animation or drawing
#                       methods.

class AstarSearch(Solver):
    """
     Concrete solver 4: must implement abstract methods from abstract class Solver
     Uses the Python built-in Priority Queue
     This utilizes not only the goal state, but the common patterns/states that come BEFORE the goal
    """
    def __init__(self, goal,numOfJug): # constructor
        self.pq=Q.PriorityQueue() #Q is from the module Queue, the Priority means that the queue is sorted  , w
        self.goal=goal
        self.Jug=numOfJug # essentially the width of the array
        self.pq.put((0, start))

    def get(self):
        if not self.pq.empty(): # if the queue aint empty
             (val,state)=self.pq.get() # this retrieves the entries which are of value and board in one set
             return state # returns the board from the queue
        else:
             return None # if the queue is empty, return nothing

    def add(self, state):
        self.pq.put(state)

    def addAstar(self, state, value):
        self.pq.put((value,state)) # puts the value and the board into the queue

    def heuristic(self,state): #Is this a A star search?
        count=0 # starts with a count of 0
        for x in range(self.Jug): # for loop for the range of how many jugs
                  if self.goal[x]!=state[x]: # if the goal state aint the same as the current board state
                      count += 1 # increment
        return count # return the count

class Game:
    """Model class for the game that stores states about the game state.
       This class also include all the necessary operators.
       Does not handle Animation or screen processses.
    """
    
   
    def __init__(self):
        self.initialstate = start
        self.goal = [8,8,8,0]
        self.numOfJug = 4
        
        #### CHANGE THE SOLVER METHOD HERE ##
        #self.Solver=BFS() #Breath-first search
        self.Solver=DFS() #Depth-first search
        #self.Solver=GBFS(self.goal,self.numOfJug) # Heuristic search (greedy best first search)
        #####################################
               
    def solve(self): 
        #get state
        #get valid moves
        #put new state state in a data structure
        #repeat

        self.used=[]
        self.i = 0
        self.Solver.add(self.initialstate)
        state=self.Solver.get()
        #pdb.set_trace()

        found=False
        while not(found or (state is None)):
            moves=self.getMoves(state)
            self.i += 1
            #print("moves=",moves)
            for move in moves:
                #print("--->trying ...",move)
                temp=self.makeMove(state,move)
                self.used.append(state)                
                if not (temp in self.used):
                     self.printstate(temp,"--->moved ")
                     self.Solver.add(temp)
                     
                     if (temp==self.goal):
                          print("Found answer")
                          print("Number of moves made", self.i - 1)
                          found=True
                          break
            state=self.Solver.get()

    def solveAstar(self):

        self.SolverAstar = AstarSearch(self.goal, self.numOfJug)
        # when initialized, SolverAstar will add the start with a value of 0 to the priority queue
        current= self.SolverAstar.get() # gets the start

        self.i = 0
        came_from = {} # these two are dictionaries which, came_from holds all optimal path
        cost_so_far = {} # this holds all the child moves explored

        came_from[tuple(start)] = None # we first put the start state as a key (as a tuple) for the dictionary, set to None
        cost_so_far[tuple(start)] = 0 # Cost from the start is 0 duh

        Found=False
        while not(Found or (current is None)):
            moves=self.getMoves(current) # get all the possible moves
            self.i += 1

            if current == self.goal: # if the goal is reached
                print("Found  answer")
                print("Number of moves explored: ", self.i) # prints out how many moves are checked
                self.i=0 # reset
                current = self.goal
                path = [current] # path will be a list, that starts with the goal
                while current != start: # until it reaches back to the start
                    self.i += 1
                    current = came_from[tuple(current)] # take up the previous move from that current state
                    path.append(current) # append to the path
                path.reverse() # reverse for viewing from start to goal
                for x in path: print(x)
                print("Number of moves in optimal path: ", self.i )
                break #break the while loop

            for move in moves: # for every possible move
                temp=self.makeMove(current, move) # get the move
                new_cost = cost_so_far[tuple(current)] + 1
                # the new cost will hold the cost so far from the start to the current, plus 1 path cost (since you pour only once)
                # This is then later used as it is the new cost to go to the next state, which the next is temp

                if tuple(temp) not in cost_so_far or new_cost < cost_so_far[tuple(temp)]:
                    # if the key of state temp, is not in the dictionary,
                    # OR if the new_cost is less than the cost_so_far of that temp state (from start to temp)
                    # We added that OR condition because we may travese the temp state again later on as we search for the optimal path
                    # which may actually have a lower path cost value than previously seen before
                    self.printstate(temp, "--->moved ")
                    cost_so_far[tuple(temp)] = new_cost # the cost to get to temp from the current so far will be the new cost
                    fCost = new_cost + self.SolverAstar.heuristic(temp) # f(n) = g(n) + h(n), A* search formula
                    # g(n) is the cost from the start to n, h(n) is our Solver3's heuristics, estimate cost to the goal
                    self.SolverAstar.addAstar(temp,fCost) # add that new state in the priority queue
                    came_from[tuple(temp)] = current # add the current state to the key of temp (for each state) in the dictionary came_from

            current = self.SolverAstar.get()

    def printstate(self, state, msg=None):
        print(msg, state)
        return

    def makeMove(self,state, move):
        """make a valid move and update the state """
        # This function does not check if the move is valid.
        A, B, C, D = state
        
        #Get the values of the From and To containers
        From=state[named[move[0]]]
        To=state[named[move[1]]]
        Pour = MAX[named[move[1]]] - To # Pour till filled unless From has less
        Pour = From if (From<Pour) else Pour

        #Update the state now as a new object
        state1=state[:]
        state1[named[move[0]]]=state[named[move[0]]]-Pour
        state1[named[move[1]]]=state[named[move[1]]]+Pour
        
        return state1
            
    
    def isValidMove(self, state, move):
        A, B, C, D = state

        # move e.g. = ('A','D') means pour from A to D
        # valid if condition is meet
        # 1. From (move[0]) is not empty
        # 2. To (move[1]) is not filled
        
        From=state[named[move[0]]]
        To=state[named[move[1]]]
        Max_To=MAX[named[move[1]]]
        
        #Valid to pour as long as there is empty space in To and From is not empty
        Pour = abs(From - Max_To - To) if From >0 else 0

        if(From > 0 and (Max_To-To)>0 and Pour>0):
             return True
        else:
             return False
        
        
    
    def getMoves(self,state, lastMove=None):
        """get all possible combination of moves """         
        self.printstate(state,"getMoves for .. ")
        
        moves=[]
        name=['A','B','C','D']
        
        #get the filled container names as A,B,C,D
        #generate all combinations -- not so smart ..
        filled=[]
        for i,j in enumerate(state):
            filled.append(name[i])

        #generate possible permutations of moves
        possible_moves=list(itertools.permutations(filled,2))
        #you could use a static list that has all combinations instead
        
        #check if moves are valid, if they are add it to moves
        for m in possible_moves:
             #print(m)
             if (self.isValidMove(state, m)):
                 moves.append(m)

        # return a list of remaining moves
        return moves
    
    
def main():
    game = Game()

    #### CHANGE THE SEARCH METHOD HERE ##
    game.solve() #for BFS, DFS, and GreedyBest
    #game.solveAstar() #For A* search

if __name__ == '__main__':
    main()
