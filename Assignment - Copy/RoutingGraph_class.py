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


def main():

    map_str = """\
    +-------+
    |  9  XG|
    |X XXX P|
    | S  0FG|
    |XX P XX|
    +-------+
    """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(s)
        for arc in graph.outgoing_arcs(s):
            print ("  " + str(arc))

    node = (1,1,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (1,7,2)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (3, 7, 0)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 7, math.inf)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 6, 5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (3, 6, 9)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (2, 7, 4)  # at a location with a portal
    print("\nOutgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
if __name__ == "__main__":
    main()
