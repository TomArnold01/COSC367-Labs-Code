from math import sqrt
from search import *
import heapq as heap


class LCFSFrontier(Frontier):
    """Implements a frontier container appropriate for Lowest-cost-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initializes the
        container to an empty heapq."""
        self.container = []
        self.count = 0

    def add(self, path):
        total_cost = sum(arc.cost for arc in path)
        self.count += 1
        # Use the total_cost as priority to ensure proper ordering
        heap.heappush(self.container, (total_cost, self.count, path))

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if self.container:
            _, _, path = heap.heappop(self.container)
            return path
        else:
            raise StopIteration


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
                distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if distance <= self.radius:
                    arcs.append(
                        Arc(tail, node, action=tail + "->" + node, cost=distance)
                    )
        sorted_arcs = sorted(arcs, key=lambda arc: arc.head[0])
        return sorted_arcs


def main():
    frontier = LCFSFrontier()
    frontier.add((Arc(None, None, None, 17),))
    frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
    frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))

    for path in frontier:
        print(path)

    graph = LocationGraph(
        location={"A": (25, 7), "B": (1, 7), "C": (13, 2), "D": (37, 2)},
        radius=15,
        starting_nodes=["B"],
        goal_nodes={"D"},
    )

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

    graph = ExplicitGraph(
        nodes=set("ABCD"),
        edge_list=[("A", "D", 7), ("A", "B", 2), ("B", "C", 3), ("C", "D", 1)],
        starting_nodes=["A"],
        goal_nodes={"D"},
    )

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)


if __name__ == "__main__":
    main()
