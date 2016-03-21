from itertools import combinations_with_replacement

class HamNodes(object):

    def __init__(self, txt):
        self.clusters = {}
        with open(txt) as f:
            _, self.nbits = tuple(int(i) for i in f.readline().strip().split(" "))
            for raw_str in f.readlines():
                node_int = int("".join(raw_str.strip().split(" ")), 2)
                self.clusters[node_int] = node_int

    def __find_leader(self, node):
        orig_node = node
        while True:
            parent = self.clusters[node]
            if parent == node:
                self.clusters[orig_node] = parent
                break
            else:
                node = parent
        return parent


    def k_clusters(self):
        checked_neighbors = {}
        nodes = list(self.clusters.keys())
        k = len(nodes)
        while nodes:
            int_n = nodes.pop()
            leader_n = self.__find_leader(int_n)

            for i, j in combinations_with_replacement(range(self.nbits), 2):
                if i == j:
                    neighbor = int_n ^ (1 << i)
                else:
                    neighbor = int_n ^ ((1 << i) | (1 << j))
                if neighbor >= int_n or neighbor not in self.clusters:
                    continue

                elif neighbor in self.clusters:
                    leader_nei = self.__find_leader(neighbor)

                    if leader_nei != leader_n:
                        k -= 1
                        self.clusters[leader_n] = leader_nei
                        leader_n = leader_nei

        return k

if __name__ == "__main__":
    g = HamNodes("ass22.txt")
    g.k_clusters()



# t21 - 1
# t22 - 3
# t23 - 4
# t24 - 11