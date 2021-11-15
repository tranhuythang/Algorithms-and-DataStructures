"""
Kruskal's greedy algorithm to find minimum spanning tree of a weighted connected graph:
    1. Idea (Greedy algorithm): Repeatedly add next lightest edge that does not make cycle
    2. Data structure: Union-Find
    Kruskal algorithm starts with all vertices but no edge, so each vertex is a acyclic connected component (trees),
    and gradually join those connected components by adding edges to eventually have only one connected component.
    Kruskal's algorithm uses data structure Union-Find for acyclic connected components (= trees) with 2 operations:
          find(node): find the root of the tree containing node
          union(node1, node2): union the two trees that contain node1, node2)

    Each acyclic connected component, i.e. a tree, is determined by a root node. Each node points to its parent; the root
    node points to itself; one uses an array list to describe the tree structure. Also for optimizing union operator,
    one uses rank - the height of nodes, to compare two acyclic connected component.

    3. Pseudocode for Kruskal algorithm:
    for each vertex u create a tree: maketree(u)
    sort edges by their length non-decreasing
    mst = []
    for each edge (u, v) in the sorted edges:
        if find(u) != find(v):
            mst.append((u, v))
            union(u, v)
"""

"""
    Assume that vertices are labeled from 0 to n; edges are a list, like [[0, 2], [1, 4], [2, 4]].
    A graph is given by two parameter: number of vertices, list of edges
"""
class Graph:
    def __init__(self, vertices_num, edges):
        self.vertices_num = vertices_num
        self.edges = edges[::]

class UnionFind:
    def __init__(self, graph):
        self.rank = [0 for i in range(graph.vertices_num)]
        self.pi = [i for i in range(graph.vertices_num)]

    def find(self, node):
        while self.pi[node] != node:
            node = self.pi[node]
        return node

    def union(self, node_a, node_b):
        root_a = self.find(node_a)
        root_b = self.find(node_b)
        if root_a == root_b:
            return
        if self.rank[root_a] > self.rank[root_b]:
            self.pi[root_b] = root_a
        else:
            self.pi[root_a] = root_b
            if self.rank[root_a] == self.rank[root_b]:
                self.rank[root_b] += 1



def Kruskal(graph):
    mst = []
    uf = UnionFind(graph)
    sorted_edges = sorted(graph.edges, key = lambda x : x[2])
    for e in sorted_edges:
        start_root = uf.find(e[0])
        end_root = uf.find(e[1])
        if start_root != end_root:
            mst.append(e)
            uf.union(start_root, end_root)
    return sum(map(lambda x:x[2], mst)), mst

def main():
    graph = Graph(6, [[0, 1, 2], [0, 2, 1], [1, 2, 2], [1, 3, 1], [2, 3, 2], [2, 4, 3], [3, 4, 3], [3, 5, 4], [4, 5, 1]])
    print(Kruskal(graph))

if __name__ == '__main__':
    main()