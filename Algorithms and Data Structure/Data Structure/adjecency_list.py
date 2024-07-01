class Graph:
    def __init__(self,size) -> None:
        self.adj_list = [ set() for _ in range(size)]

    def add_edge(self,src,dest):
        self.adj_list[src].add(dest)
        self.adj_list[dest].add(src) # undirected graph

    def remove_edge(self,src,dest):
        self.adj_list[src].remove(dest)
        self.adj_list[dest].remove(src) # undirected graph

    def print(self):
        for src,adj_list in enumerate(self.adj_list):
            print(src," => ",adj_list)

if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(2,3)
    graph.add_edge(1,4)
    graph.add_edge(0,3)
    graph.print()
    graph.remove_edge(0,3)
    graph.add_edge(1,2)
    graph.print()