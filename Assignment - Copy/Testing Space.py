from search import *
import math


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
        
        options = [("N", -1, 0), ("E", 0, 1), ("S", 1, 0), ("W", 0, -1), ("N/A", 0, 0)]
        blockades = ["+", "-", "|", "X"]
        arcs = []
        row, col, fuel = tail_node[0], tail_node[1], tail_node[2]

        for directions in options:
            dir_str, edit_row, edit_col = directions[0], directions[1], directions[2]
            testing = self.routing_map[row + edit_row][col + edit_col]
            if testing not in blockades:
                if type(fuel) == int:  # If they have limited fuel:
                    if fuel == 0:  # If they have no fuel
                        None
                    else:
                        movement = (row + edit_row, col + edit_col, fuel - 1)
                        if testing == " " or testing == "G" or testing == "0":  # If they move into a empty spot
                            if  dir_str != "N/A":
                                arcs.append(
                                    Arc(tail_node, head=movement, action=dir_str, cost=5)
                                )
                        elif testing == "F":  # If they move into a fueling station
                            movement = (row + edit_row, col + edit_col, 9)
                            arcs.append(
                                Arc(tail_node, head=movement, action="fuel up", cost=15)
                            )
                        elif testing == "P": # move to a teleport station
                            movement = (row + edit_row, col + edit_col, 9)
                            arcs.append(
                                Arc(tail_node, head=movement, action="Teleport to (change movement)", cost=10)
                            )
                else:  # If they have unlimited fuel:
                    movement = (row + edit_row, col + edit_col, math.inf)
                    if testing == " " or testing == "G" or testing == "0":  # If they move into a empty spot
                        if dir_str != "N/A":
                            arcs.append(
                                Arc(tail_node, head=movement, action=dir_str, cost=5)
                            )
                    elif testing == "F":  # If they move into a fueling station
                        arcs.append(
                            Arc(tail_node, head=movement, action="fuel up", cost=15)
                        )
                    elif testing == "P": # move to a teleport station
                        arcs.append(
                            Arc(tail_node, head=movement, action="Teleport to (change movement)", cost=10)
                        )
        return arcs

    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""
        None

    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        for goal in self.goal_node:
            if (node[0], node[1]) == goal:
                return True
        return False 

class AStarFrontier(RoutingGraph):
    def __init__(self, map_str):
        self.container = []
        self.count = 0
        self.routing_graph = map_str

    def add(self, path):
        cost = 0
        for arc in path:
            cost += arc[-1]
        estimated_cost = 
        

    def __iter__(self):
        return self
    
    def __next__(self):
        None

def main():

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

if __name__ == "__main__":
    main()
