from search import Arc, Graph
from math import sqrt

class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        return node in self.goal_nodes


    def outgoing_arcs(self, tail):

        x1, y1 = self.location[tail] if tail in self.location else (None, None)
        arcs = []
        for node in self.location:
            if node != tail:
                x2, y2 = self.location[node]
                distance = sqrt((x2 - x1)**2 +(y2-y1)**2)
                if distance <= self.radius:
                    arcs.append(Arc(tail, node, action = tail + "->" + node, cost = distance)) 
        sorted_arcs = sorted(arcs, key=lambda arc: arc.head[0])
        return sorted_arcs


def main():
    graph = LocationGraph(
    location={'SW': (-2, -2),
              'NW': (-2, 2),
              'NE': (2, 2),
              'SE': (2, -2)},
    radius = 5,
    starting_nodes=['NE'],
    goal_nodes={'SW'}
)

    for arc in graph.outgoing_arcs('NE'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('NW'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('SW'):
        print(arc)

    print()


    for arc in graph.outgoing_arcs('SE'):
        print(arc)

if __name__ == "__main__":
    main()