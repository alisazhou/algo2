import heapq
from collections import defaultdict


class AdjList(object):
    """Parses txt into an adjacency list, represented as a dict

    """

    def __init__(self, txt):
        self.alist = defaultdict(list)
        with open(txt) as f:
            self.n, self.m = (int(i) for i in f.readline().strip().split(" "))
            for edge in f.readlines():
                n1, n2, w = (int(i) for i in edge.strip().split(" "))
                self.alist[n1].append((w, n2))
                self.alist[n2].append((w, n1))
        self.s = n1
        self.processed = [self.s]
        self.crossing = []
        self.get_crossing_edges(self.s)

    def get_crossing_edges(self, new_node):
        adj_edges = self.alist[new_node]
        self.crossing += adj_edges
        heapq.heapify(self.crossing)

    def add_processed(self, new_node):
        self.processed.append(new_node)


def mst(graph):
    tree = []
    cost = 0
    # n1: [ (w, n2), ...]
    while len(graph.processed) != graph.n:
        new_cost, new_node = heapq.heappop(graph.crossing)
        if new_node in graph.processed:
            continue
        else:
            cost += new_cost
            graph.add_processed(new_node)
            graph.get_crossing_edges(new_node)
    return cost


if __name__ == "__main__":
    import sys
    txt = sys.argv[1]
    graph = AdjList(txt)
    cost = mst(graph)
    print(cost)


# answers to testcases:
# t131 - 2624
# t132 - -684
# ass13 - -3612829