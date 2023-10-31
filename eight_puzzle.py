#
# eight_puzzle.py (Final Project)
#

from searcher import *
from timer import *

def create_searcher(algorithm, depth_limit = -1, heuristic = None):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
            
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    # question 6
    if algorithm == 'random':
        searcher = Searcher(depth_limit)
    elif algorithm == 'BFS':
        searcher = BFSearcher(depth_limit)
    elif algorithm == 'DFS':
        searcher = DFSearcher(depth_limit)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(depth_limit, heuristic)
    elif algorithm == 'A*':
        searcher = AStarSearcher(depth_limit, heuristic)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher



def eight_puzzle(init_boardstr, algorithm, depth_limit = -1, heuristic = None):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, depth_limit, heuristic)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            


# question 1 V

def process_file(filename, algorithm, depth_limit=-1, heuristic=None):
    """Process a file containing puzzles, solve each one and print statistics."""
    total_moves = 0
    total_states = 0
    solved_puzzles = 0
    
    
    with open(filename, 'r') as f:
        for line in f:
            # Strip newline characters and whitespace
            digit_str = line.strip()
            
            # Initialize Board and State
            init_board = Board(digit_str)
            init_state = State(init_board, None, 'init')

            # Create searcher
            searcher = create_searcher(algorithm, depth_limit, heuristic)
            if searcher == None:
                return

            # Find solution
            soln = None
            print(f"{digit_str}: ",end = '')
            try:
                soln = searcher.find_solution(init_state)
            except KeyboardInterrupt:
                print('Search terminated, ', end='')

            if soln != None:
                solved_puzzles += 1
                total_moves += soln.num_moves
                total_states += searcher.num_tested
                print(f"{soln.num_moves} moves, {searcher.num_tested} states tested")
            else:
                print("no solution")

    # Print summary statistics
    print(f"\nsolved {solved_puzzles} puzzles")
    if solved_puzzles > 0:
        print(f"averages: {total_moves/solved_puzzles} moves, {total_states/solved_puzzles} states tested")

#process_file('10_moves.txt', 'BFS')
#process_file('10_moves.txt', 'Greedy', -1, h1)
#process_file('10_moves.txt', 'DFS', 5)

#process_file('15_moves.txt', 'A*', -1, h2)  # no depth limit, heuristic h2


if __name__ == '__main__':

    print('\n\nGreedyh1 :')
    process_file('18_moves.txt', 'Greedy', -1, h1)
    print('\n\nGreedyh2 :')
    process_file('18_moves.txt', 'Greedy', -1, h2)
    print('\n\nA*h1 :')
    process_file('18_moves.txt', 'A*', -1, h1)
    print('\n\nA*h2 :')
    process_file('18_moves.txt', 'A*', -1, h2)
    print('\n 18 moves Ends\n\n')


    print('\n 21 moves Test\n\n')

    print('\n\nGreedyh1 :')
    process_file('21_moves.txt', 'Greedy', -1, h1)
    print('\n\nGreedyh2 :')
    process_file('21_moves.txt', 'Greedy', -1, h2)
    print('\n\nA*h1 :')
    process_file('21_moves.txt', 'A*', -1, h1)
    print('\n\nA*h2 :')
    process_file('21_moves.txt', 'A*', -1, h2)
    print('\n 21 moves Ends\n\n')
    
    print('\n 24 moves Test\n\n')
    
    print('\n\nGreedyh1 :')
    process_file('24_moves.txt', 'Greedy', -1, h1)
    print('\n\nGreedyh2 :')
    process_file('24_moves.txt', 'Greedy', -1, h2)
    print('\n\nA*h1 :')
    process_file('24_moves.txt', 'A*', -1, h1)
    print('\n\nA*h2 :')
    process_file('24_moves.txt', 'A*', -1, h2)
    print('\n 24 moves Ends\n\n')
    
    print('\n 27 moves Test\n\n')
    
    print('\n\nGreedyh1 :')
    process_file('27_moves.txt', 'Greedy', -1, h1)
    print('\n\nGreedyh2 :')
    process_file('27_moves.txt', 'Greedy', -1, h2)
    print('\n\nA*h1 :')
    process_file('27_moves.txt', 'A*', -1, h1)
    print('\n\nA*h2 :')
    process_file('27_moves.txt', 'A*', -1, h2)
    print('\n 27 moves Ends\n\n')
