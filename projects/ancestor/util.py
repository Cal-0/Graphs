
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def __str__(self):
        return f'{self.queue}'
    def peek(self):
        return self.queue[-1]
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def __str__(self):
        return f'{self.stack}'
    def peek(self):
        return self.stack[-1]
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # def add_vertex(self, vertex, edges=()):
        """
        Add a new vertex to the graph, with edges to other vertices.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            vert = q.dequeue()
            if vert not in visited:
                print(vert)
                visited.add(vert)
                for next_vert in self.get_neighbors(vert):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            vert = s.pop()
            if vert not in visited:
                print(vert)
                visited.add(vert)
                for next_vert in self.get_neighbors(vert):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        path = self.get_neighbors(starting_vertex)
        visited.add(starting_vertex)
        print(starting_vertex)
        for next_vert in path - visited:
            self.dft_recursive(next_vert, visited)
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            vert = path[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    return path
                    visited.add(vert)
                for neighbors in self.get_neighbors(vert):
                    new_path = list(path)
                    new_path.append(neighbors)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        pass  # TODO