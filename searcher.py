#
# searcher.py (Final project)
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
# question 1
    def __init__(self, depth_limit):
        self.states = []            # list of untested states
        self.num_tested = 0         # number of states tested
        self.depth_limit = depth_limit

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
# question 2    
    def should_add(self, state):
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        if state.creates_cycle():
            return False
        return True
    
# question 3
    def add_state(self, new_state):
        """
            adds takes a single State object called new_state and adds it to the Searcher‘s list of untested states.
        """
        self.states.append(new_state)

# question 4
    def add_states(self, new_states):
        """takes a list State objects called new_states, and that processes 
           the elements of new_states one at a time as follows
        """
        for state in new_states:
            if self.should_add(state):
                self.add_state(state)

# question 5

    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
# question 6

    def find_solution(self, init_state):
        """performs a full random state-space search, stopping when the goal state is found or 
        when the Searcher runs out of untested states.
        """
        self.add_state(init_state)
        while len(self.states) > 0:
            next_state = self.next_state()
            candidate_states = next_state.generate_successors()
            # filter candidate_states using should_add before adding them
            candidate_states = [s for s in candidate_states if self.should_add(s)]
            self.add_states(candidate_states)
            self.num_tested += 1
            if next_state.is_goal():
                return next_state
        return None
'''
    def find_solution(self, init_state):
        """performs a full random state-space search, stopping when the goal state is found or 
           when the Searcher runs out of untested states.
        """
        self.add_state(init_state)
        while len(self.states) > 0:
            next_state = self.next_state()
            candidate_states = next_state.generate_successors()
            self.add_states(candidate_states)
            self.num_tested += 1
            if next_state.is_goal():
                return next_state
        return None
'''



### Add your BFSeacher and DFSearcher class definitions below. ###
# question 1
class BFSearcher(Searcher):
    """ A class for objects that perform breadth-first
        state-space search method.
    """
    def __init__(self, depth_limit):
        super().__init__(depth_limit)
        self.current_state_index = 0

    def next_state(self):
        """ overrides the next_state method that is inherited from Searcher.
        """
        next_state = self.states[self.current_state_index]
        del self.states[self.current_state_index]
        return next_state

# question 2
class DFSearcher(Searcher):
    """ A class for objects that perform depth-first
        state-space search method.
    """
    def __init__(self, depth_limit):
        super().__init__(depth_limit)
        self.current_state_index = -1  # index for the last state

    def add_state(self, new_state):
        """
            adds takes a single State object called new_state and adds it to the Searcher‘s list of untested states.
        """
        self.states.append(new_state)
        self.current_state_index += 1

    def next_state(self):
        """ overrides the next_state method that is inherited from Searcher.
        """
        next_state = self.states[self.current_state_index]
        del self.states[self.current_state_index]
        self.current_state_index -= 1
        return next_state


# heuristic functions

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    """ a heuristic function returns mistaken tiles """
    return state.board.num_misplaced()

def h2(state):
    """a heuristic function that returns the total Manhattan distance of the misplaced tiles"""
    total_distance = 0
    for row in range(3):
        for col in range(3):
            value = state.board.tiles[row][col] 
            if value != 0: 
                goal_row, goal_col = value // 3 , value % 3 # get the goal position of this value
                total_distance += abs(row - goal_row) + abs(col - goal_col) # accumulate the Manhattan distance
    return total_distance


### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def __init__(self, depth_limit, heuristic):
        super().__init__(depth_limit)
        self.heuristic = heuristic
    
    def priority(self, state):
        """ takes a State object called state, and that computes and returns the priority of that state.
        """
        heuristic_value = self.heuristic(state)
        priority = -1 * heuristic_value
        return priority

#    def add_state(self, new_state):
#       """ overrides the add_state method that is inherited from Searcher..
#        """
#        state_priority = self.priority(new_state)
#        self.states.append([state_priority, new_state])
#        
#    def next_state(self):
#        """ Coverrides the next_state method that is inherited from Searcher.
#        """
#        max_priority_state = max(self.states, key=lambda x: x[0])
#        self.states.remove(max_priority_state)
#        return max_priority_state[1]
    def add_state(self, new_state):
        """ Adds a single State object called new_state to the Searcher‘s list of untested states.
        """
        priority = self.priority(new_state)
        self.states.append([priority, new_state])

    def next_state(self):
        """ Chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it.
            This overrides the inherited method to return the state with the highest priority.
            """
        max_priority_state = max(self.states, key=lambda x: x[0])
        self.states.remove(max_priority_state)
        return max_priority_state[1]


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """ performs A* search.
    """
    def priority(self, state):
        """ compute and return the priority of a state
        """
        heuristic_value = self.heuristic(state)
        priority = -1 * (heuristic_value + state.num_moves)
        return priority
    
    def __repr__(self):
        """ returns a string representation of the AStarSearcher object
            referred.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

if __name__ == '__main__':

    b = Board('214360758')       
    s = State(b, None, 'init')
    g = GreedySearcher(-1, h1)
    g.add_state(s)
    print(g.states)
    #[[-5, 142358607-init-0]]
    succ = s.generate_successors()
    g.add_state(succ[0])
    print(g.states)
    #[[-5, 142358607-init-0], [-5, 142308657-up-1]]
    g.add_state(succ[1])
    print(g.states)
    #[[-5, 142358607-init-0], [-5, 142308657-up-1], [-6, 142358067-left-1]]