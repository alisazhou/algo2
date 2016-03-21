from itertools import combinations_with_replacement
from collections import defaultdict
import time

class HamNodes(object):

    def __init__(self, txt):
        self.nodes = set()
        with open(txt) as f:
            _, self.nbits = tuple(int(i) for i in f.readline().strip().split(" "))
            for raw_str in f.readlines():
                node_int = int("".join(raw_str.strip().split(" ")), 2)
                self.nodes.add(node_int)
        self.nodes = list(self.nodes)
        self.nodes.sort()
        self.leader = defaultdict(int)

    def __find_leader(self, node):
        orig_node = node
        while True:
            parent = self.leader[node]
            if not parent:
                self.leader[node] = node
                parent = node
                self.leader[orig_node] = parent
                break
            elif parent == node:
                self.leader[orig_node] = parent
                break
            else:
                node = parent
        return parent


    def k_clusters(self):
        start_time = time.time()
        count_time = 0
        k = len(self.nodes)
        while self.nodes:
            count_time += 1
            if not count_time % 100:
                print("{} time: {}".format(count_time, time.time() - start_time))
            int_n = self.nodes.pop()
            leader_n = self.__find_leader(int_n)
            if not leader_n:
                leader_n = int_n
                self.leader[int_n] = int_n

            for i, j in combinations_with_replacement(range(self.nbits), 2):
                if i == j:
                    neighbor = int_n ^ (1 << i)
                else:
                    neighbor = int_n ^ ((1 << i) | (1 << j))
                if neighbor >= int_n:
                    continue

                if neighbor in self.nodes:
                    leader_nei = self.__find_leader(neighbor)

                    if leader_nei != leader_n:
                        k -= 1
                        self.leader[leader_n] = leader_nei
                        leader_n = leader_nei

        return k

if __name__ == "__main__":
    g = HamNodes("ass22.txt")
    g.k_clusters()



# t21 - 1
# t22 - 3
# t23 - 4
# t24 - 11