from search import *
from collections import deque

class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = deque([])

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration   # don't change this one

def main():    
    
    graph = ExplicitGraph(nodes=set('SAG'),
                      edge_list = [('S','A'), ('S', 'G'), ('A', 'G')],
                      starting_nodes = ['S'],
                      goal_nodes = {'G'})

    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    


if __name__ == "__main__":
    main()