import heapq
from collections import defaultdict


class AdjList(object):

    def __init__(self, txt):
        self.edges = []
        self.clusters = defaultdict(int)
        self.leaders = defaultdict(list)
        with open(txt) as f:
            self.n = int(f.readline().strip())
            for line in f.readlines():
                n1, n2, d = (int(i) for i in line.strip().split(" "))
                edge = (d, n1, n2)
                heapq.heappush(self.edges, edge)

    def merge_closest(self):
        while True:
            d, n1, n2 = heapq.heappop(self.edges)
            cluster1 = self.clusters[n1]
            cluster2 = self.clusters[n2]
            if not (cluster1 and cluster2):
                # at least one node is in its own cluster
                if cluster1:
                    self.clusters[n2] = cluster1
                    self.leaders[cluster1].append(n2)
                else:
                    if cluster2:
                        self.clusters[n1] = cluster2
                        self.leaders[cluster2].append(n1)
                    else:
                        self.clusters[n1] = n1
                        self.clusters[n2] = n1
                        self.leaders[n1].extend([n1, n2])
                break
            elif cluster1 != cluster2:
                # both have been previously merged into clusters
                self.clusters[cluster2] = cluster1
                for node in self.leaders[cluster2]:
                    self.clusters[node] = cluster1
                self.leaders[cluster1].extend(self.leaders[cluster2])
                self.leaders[cluster2] = []
                break




def k_cluster(k, graph):
    no_clusters = graph.n
    while no_clusters > k:
        graph.merge_closest()
        no_clusters -= 1
    while True:
        spacing, n1, n2 = heapq.heappop(graph.edges)
        cluster1 = graph.clusters[n1]
        cluster2 = graph.clusters[n2]
        if not (cluster1 and cluster2):
            # at least one node is in its own cluster
            break
        elif cluster1 != cluster2:
            break

    return spacing



# testcase answers:
# t11 - 134365
    # 2 and 7 get merged with cost 2107
    # 6 and (2,7) get merged with cost 21490
    # 3 and (2,6,7) get merged with cost 25446
    # 4 and (2,3,6,7) get merged with cost 29041
    # 1 and 10 get merged with cost 93860
    # 8 and 9 get merged with cost 120890
    # This gets us to 4 clusters.
    # remaining edge is between (1,10) and (2,3,4,6,7) with cost 134365
# t12 - 7
# t13 - 2
    # cluster 1:  1
    # cluster 2:  2,  4
    # cluster 3:  3
    # cluster 5:  5
    # Max-Spacing is 2, between clusters  2 and 5
# t14 - 5
# t15 - 27
# t16 - 131
