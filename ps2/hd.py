from itertools import combinations_with_replacement
from collections import defaultdict
import time

class HamNodes(object):

    def __init__(self, txt):
        self.nodes = set()
        with open(txt) as f:
            _, self.nbits = tuple(int(i) for i in f.readline().strip().split(" "))
            for raw_str in f.readlines():
                bit_str = "".join(raw_str.strip().split(" "))
                self.nodes.add(bit_str)
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
            n = self.nodes.pop()

            count_time += 1
            if not count_time % 100:
                print("----time: {}----".format(time.time() - start_time))

            int_n = int(n, 2)
            leader_n = self.leader[int_n]
            if not leader_n:
                leader_n = int_n
                self.leader[int_n] = int_n
            count = 0
            for i, j in combinations_with_replacement(range(self.nbits), 2):
                count += 1
                if n[i] == "0":
                    # only look at smaller nodes
                    continue
                else:
                    diff = "0"

                if i == j:
                    neighbor = n[:i] + diff + n[i + 1:]
                else:
                    if n[j] == "0":
                        diff2 = "1"
                    else:
                        diff2 = "0"
                    neighbor = n[:i] + diff + n[i + 1:j] + diff2 + n[j + 1:]
                if neighbor in self.nodes:
                    int_nei = int(neighbor, 2)
                    leader_nei = self.__find_leader(int_nei)

                    if leader_nei != leader_n:
                        k -= 1
                        self.leader[leader_n] = leader_nei
                        leader_n = leader_nei


        return k





# t21 - 1
# t22 - 3
# t23 - 4
# t24 - 11