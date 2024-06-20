from search import *
import math
from heapq import *

class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.routing_map, self.goal_node, self.agents, self.teleport_stations = self.process_text_map(map_str)

    def process_text_map(self, map_str):
        goal_node = []
        agents = []
        map_list = []  # holds a version of the map as a list
        teleport_stations = []

        map_list_temp = map_str.splitlines()

        for row, line in enumerate(map_list_temp):
            line = line.strip()
            map_line = []  # each line of the map will be a list
            for col, char in enumerate(line):
                if char == "G":
                    goal_node.append((row, col))
                elif char == "S":
                    agents.append((row, col, math.inf))  # 'S' have inf fuel
                elif char == "P":
                    teleport_stations.append((row, col))
                elif char.isdigit():
                    agents.append((row, col, int(char)))  # digits have limited fuel
                map_line.append(char)
            map_list.append(map_line)

        return map_list, goal_node, agents, teleport_stations

    def starting_nodes(self):
        return self.agents

    def outgoing_arcs(self, tail_node):
        directions = [("N", -1, 0), ("E", 0, 1), ("S", 1, 0), ("W", 0, -1)]
        row, col, fuel = tail_node
        if fuel > 0:
            for label, move_x, move_y in directions:
                edit_row = row + move_x
                edit_col = col + move_y
                eidt_pos = self.routing_map[edit_row][edit_col]
                if not eidt_pos in ["+", "-", "|", "X"]:
                    head = (edit_row, edit_col, fuel - 1)
                    yield Arc(tail_node, head, label, 5)
                    
        
        if self.routing_map[row][col] == "F" and fuel < 9:
            head = (row, col, 9)
            yield Arc(tail_node, head, "Fuel up", 15)
        
        if self.routing_map[row][col] == "P":
            head = (row, col, fuel-1)
            for target in self.teleport_stations:
                if (row, col) != target:
                    new_head = (target[0], target[1], tail_node[2])
                    yield Arc(tail_node, new_head, f"Teleport to {target}", 10)

    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        for goal in self.goal_node:
            if (node[0], node[1]) == goal:
                return True
        return False 
    
    def estimated_cost_to_goal(self, node):
        agnt_row, agnt_col, _ = node

        min_distance = float('inf')

        for goal_row, goal_col in self.goal_node:
            distance = abs(agnt_row - goal_row) + abs(agnt_col - goal_col)
            min_distance = min(min_distance, distance)
            
        return min_distance * 5


class AStarFrontier(RoutingGraph):
    def __init__(self, map_str):
        self.container = []
        self.count = 0
        self.pruned = set()
        self.routing_graph = map_str

    def add(self, path):
        if path[-1][1] in self.pruned:
            return
        path_cost = sum(arc.cost for arc in path)
        estimated_cost = self.routing_graph.estimated_cost_to_goal(path[-1].head)
        total_cost = path_cost + estimated_cost

        to_add = (total_cost, self.count, path)
        self.count += 1
        heappush(self.container, to_add)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while len(self.container) > 0:
            next = heappop(self.container)[-1]
            if next[-1] not in self.pruned:
                self.pruned.add(next[-1])
                return next
        raise StopIteration
        
def print_map(routing_graph, frontier, solution):
    map = routing_graph.routing_map

    if solution:
        for arc in solution:
            row, col, _ = arc.head
            if map[row][col] == " ":
                map[row][col] = "*"
    
    for arc in frontier.pruned:
        row, col, _ = arc.head
        if map[row][col] == " ":
            map[row][col] = "."
    
    for line in map:
        printable = ""
        for char in line:
            printable += char
        if printable:
            print(printable)



def main():

    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    # +----------------+
    # |                |
    # |                |
    # |                |
    # |                |
    # |                |
    # |                |
    # |     ...S       |
    # |     ...*       |
    # |     ...*       |
    # |     G***       |
    # |                |
    # |                |
    # |                |
    # +----------------+


    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """


    map_graph = RoutingGraph(map_str)
    # changing the heuristic so the search behaves like LCFS
    map_graph.estimated_cost_to_goal = lambda node: 0

    frontier = AStarFrontier(map_graph)

    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    # +----------------+
    # |        .       |
    # |       ...      |
    # |      .....     |
    # |     .......    |
    # |    .........   |
    # |   ...........  |
    # |   .....S...... |
    # |    ....*.....  |
    # |     ...*....   |
    # |     G***...    |
    # |      .....     |
    # |       ...      |
    # |        .       |
    # +----------------+


    map_str = """\
    +-------------+
    | G         G |
    |      S      |
    | G         G |
    +-------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    # +-------------+
    # | G....*****G |
    # | .....S..... |
    # | G.........G |
    # +-------------+


    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    |  S    |
    +-------+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    # +-------+
    # |     XG|
    # |X XXX**|
    # |  S***.|
    # +-------+
 

    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    # +--+
    # |GS|
    # +--+


    map_str = """\
    +----+
    |    |
    | SX |
    | X G|
    +----+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    # +----+
    # | ***|
    # |.SX*|
    # |.X G|
    # +----+

    map_str = """\
    +---------------+
    |    G          |
    |XXXXXXXXXXXX   |
    |           X   |
    |  XXXXXX   X   |
    |  X S  X   X   |
    |  X        X   |
    |  XXXXXXXXXX   |
    |               |
    +---------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    # +---------------+
    # |    G********  |
    # |XXXXXXXXXXXX*  |
    # |.********..X*  |
    # |.*XXXXXX*..X*  |
    # |.*X.S**X*..X*  |
    # |.*X...***..X*  |
    # |.*XXXXXXXXXX*  |
    # |.************  |
    # +---------------+

    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

if __name__ == "__main__":
    main()
