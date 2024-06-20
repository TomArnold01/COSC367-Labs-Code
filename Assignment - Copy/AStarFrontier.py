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
        # this is what the question asked me to return 
        return 0  

class AStarFrontier(RoutingGraph):
    def __init__(self, map_str):
        self.container = []
        self.count = 0
        self.pruned = set()
        self.routing_graph = map_str

    def add(self, path):
        if path[-1][1] in self.pruned:
            return

        cost = 0
        for arc in path:
            cost += arc[-1]
        to_add = (cost, self.count, path)
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

    def estimated_cost_to_goal(self, node):        
        agnt_row, agnt_col, fuel = node
        
        if (agnt_row, agnt_col) in self.goal_node:
            return 0
        
        results = []
        
        for goal_row, goal_col in self.goal_node:
            results.append(abs(agnt_row - goal_row) + abs(agnt_col - goal_col))
        
        return min(results) * 5

    
def main():
    print('\nTest number 1')
    map_str = """\
    +-------+
    |   G   |
    |       |
    |   S   |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print('\nTest number 2')
    map_str = """\
    +-------+
    |  GG   |
    |S    G |
    |  S    |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print('\nTest number 3')
    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print('\nTest number 4')
    
    map_str = """\
    +-------+
    |  F  X |
    |X XXXXG|
    | 3     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print('\nTest number 5')
    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print('\nTest number 6')
    map_str = """\
    +---+
    |GF2|
    +---+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print('\nTest number 7')

    map_str = """\
    +----+
    | S  |
    | SX |
    |GX G|
    +----+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print('\nTest number 8')

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
    print_actions(solution)

if __name__ == "__main__":
    main()
