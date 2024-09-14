import random
import itertools
from collections import deque

class Graph:
    def __init__(self, nodes: int):
        self._v = [set() for _ in range(nodes)]
        self._vset = [node for node in range(nodes)]
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
    
    def BFS(self, node: int) -> list[int]:
        if node not in self._vset: 
            raise ValueError(f"Node {node} is not in graph")

        visited = set()
        nodeQueue = deque()
        # start with root node
        visited.add(node)
        nodeQueue.append(node)
        
        bfs = list()
        while len(nodeQueue) != 0:
            node = nodeQueue.popleft()
            bfs.append(node)

            # build in a new level set
            for adj in self._v[node]:
                if adj in visited: continue

                visited.add(adj)
                nodeQueue.append(adj)

        return bfs
    
    def DFS(self, node: int) -> list[int]:
        if node not in self._vset:
            raise ValueError(f"Node {node} is not in graph")


if __name__=="__main__":
    di = Graph(6)
    di.randomDirectedGraph()
    
    print(di)
    print(di.BFS(0))

