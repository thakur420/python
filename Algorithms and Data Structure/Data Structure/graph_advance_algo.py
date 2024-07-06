from priority_queue import PriorityQueue
from disjoint_set import DisjointSet

class Edge:
    def __init__(self,src,dest,wt) -> None:
        self.src = src
        self.dest = dest
        self.wt = wt

class Graph:
    def __init__(self,size) -> None:
        self.adj_list = [set() for _ in range(size)]

    def add_edge(self,edge:Edge):
        self.adj_list[edge.src].add((edge.dest,edge.wt))
        self.adj_list[edge.dest].add((edge.src,edge.wt))
    
    def print(self):
        for u, edges in enumerate(self.adj_list):
            for v, wt in edges:
                print(f"{u} -> {v} = {wt}")
    
    def dijkstra_sp(self,src):
        dist = [float('inf') for _ in range(len(self.adj_list))]
        dist[src] = 0
        pq = PriorityQueue()
        pq.insert(src,0)
        while not pq.empty():
            prev_dist, u = pq.get()
            for v, wt in self.adj_list[u]:
                if prev_dist + wt < dist[v]:
                    dist[v] = prev_dist + wt
                    pq.decrease_key(v,dist[v])
        return dist
    
    def prim_mst(self,src):
        dist = [float('inf') for _ in range(len(self.adj_list))]
        visited = [0 for _ in range(len(self.adj_list))]
        dist[src] = 0
        pq = PriorityQueue()
        pq.insert(src,0)
        while not pq.empty():
            _, u = pq.get()
            visited[u] = 1
            for v, wt in self.adj_list[u]:
                if not visited[v] and wt < dist[v]:
                    dist[v] = wt
                    pq.decrease_key(v,dist[v])
        return dist
    
    def kruskal_mst(self):
        pq = PriorityQueue()
        ds = DisjointSet()
        mst = 0
        for u, edges in enumerate(self.adj_list):
            for v, wt in edges:
                pq.insert((u,v),wt)
            ds.makeset(u)

        while not pq.empty():
            wt, (u, v) =  pq.get()
            if ds.findset(u) != ds.findset(v):
                mst += wt
                ds.unionset(u,v)
        return mst
    
if __name__ == "__main__":
    g = Graph(9)
    edges = [Edge(0, 1, 4),Edge(0, 7, 8),Edge(1, 2, 8),Edge(1, 7, 11),Edge(2, 3, 7),Edge(2, 8, 2),
             Edge(2, 5, 4),Edge(3, 4, 9),Edge(3, 5, 14),Edge(4, 5, 10),Edge(5, 6, 2),Edge(6, 7, 1),
             Edge(6, 8, 6),Edge(7, 8, 7)]
    for edge in edges:
        g.add_edge(edge)
    print(g.dijkstra_sp(0))
    print(g.dijkstra_sp(6))
    print(g.dijkstra_sp(2))
    dist = g.prim_mst(0)
    print(f"{dist} => {sum(dist)}")
    print(g.kruskal_mst())