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

if __name__ == "__main__":
    g = Graph(5)
    edges = [Edge(0, 1,2), Edge(0,2,4), Edge(1,3,5), Edge(2,3,7), Edge(2,4,9), Edge(3,4,10)]
    for edge in edges:
        g.add_edge(edge)
    g.print()