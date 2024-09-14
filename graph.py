import random
import itertools

class Graph:
    def __init__(self, nodes: int):
        self._v = [set() for _ in range(nodes)]
        self.numVertices = nodes
        self.numEdges = 0
    
    def __repr__(self):
        graphstr = str()
        for v in range(len(self._v)):
            graphstr +=  "v["+str(v)+"] = "+str(self._v[v])+"\n"
        return graphstr
    
    def addEdge(self, u: int, v: int) -> None:
        self._v[u].add(v)
        self._v[v].add(u)
        self.numEdges +=1

    def addDiEdge(self, u: int, v: int) -> None:
        self._v[u].add(v)
        self.numEdges +=1

    def delDiEdge(self, u: int, v: int) -> None:
        if v in self._v[u]: 
            self._v[u].remove(v)
            self.numEdges -=1

    def delEdge(self, u: int, v: int) -> None:
        if v in self._v[u] and u in self._v[v]: 
            self._v[u].remove(v)
            self._v[v].remove(u)
            self.numEdges -=1

    def randomUndirectedGraph(self) -> None:
        # vertex set
        vset = list([i for i in range(0,self.numVertices)])
        
        # generate possible edge set
        eset = set()
        for u in vset: 
            for v in vset:
                if u!=v and frozenset((u,v)) not in eset:
                    eset.add(frozenset((u,v)))
        maxEdges = len(eset)

        # how connected should the graph be?
        connectivity = random.randint(0,maxEdges-1)

        # generate #(connectivity) random edges
        for _ in range(connectivity):
            remaining_edges = len(eset)
            index_edge = random.randint(0,remaining_edges-1)
            edges = list(eset)

            new_edge = edges[index_edge]
            u, v = tuple(new_edge)
            
            self.addEdge(u,v) 
            
            eset.remove(new_edge)

    def randomDirectedGraph(self) -> None:
        # vertex set
        vset = list([i for i in range(0,self.numVertices)])
        
        # generate possible edge set
        eset = set()
        for u in vset: 
            for v in vset:
                if u!=v:
                    eset.add((u,v))
        maxEdges = len(eset)

        # how connected should the graph be?
        connectivity = random.randint(0,maxEdges-1)

        # generate #(connectivity) random edges
        for _ in range(connectivity):
            remaining_edges = len(eset)
            index_edge = random.randint(0,remaining_edges-1)
            edges = list(eset)

            new_edge = edges[index_edge]
            u, v = tuple(new_edge)
            
            self.addDiEdge(u,v) 
            
            eset.remove(new_edge)


if __name__=="__main__":
    di = Graph(6)
    di.randomDirectedGraph()

    un = Graph(4)
    un.randomUndirectedGraph()
    print(di)
    print(un)


