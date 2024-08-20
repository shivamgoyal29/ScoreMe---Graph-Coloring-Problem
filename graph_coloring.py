import heapq
from collections import defaultdict


class Graph:
    # Initialize a graph with a given number of vertices
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = defaultdict(list)
        self.colors = [-1] * num_vertices
        self.pre_assigned_colors = {}
        self.exclusions = defaultdict(set)

    # Add an undirected edge between vertices u and v
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    # Remove an undirected edge between vertices u and v
    def remove_edge(self, u, v):
        if v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v)
        if u in self.adjacency_list[v]:
            self.adjacency_list[v].remove(u)

    # Set a pre-assigned color for a specific vertex
    def set_pre_assigned_color(self, vertex, color):
        self.pre_assigned_colors[vertex] = color
        self.colors[vertex] = color

    # Exclude a specific color from being used on a vertex
    def set_color_exclusion(self, vertex, color):
        self.exclusions[vertex].add(color)

# Initialize the solver with the given graph
class ColoringSolver:
    def __init__(self, graph):
        self.graph = graph

   # Implement the DSATUR algorithm for graph coloring
    def dsatur(self):
        degrees = [len(self.graph.adjacency_list[v])
                   for v in range(self.graph.num_vertices)]
        saturation = [0] * self.graph.num_vertices
        available_colors = [set(range(self.graph.num_vertices)) - self.graph.exclusions[v]
                            for v in range(self.graph.num_vertices)]
        max_heap = [(-degrees[v], v)
                    for v in range(self.graph.num_vertices) if self.graph.colors[v] == -1]
        heapq.heapify(max_heap)

        for vertex, color in self.graph.pre_assigned_colors.items():
            self._assign_color(vertex, color, degrees,
                               saturation, available_colors)

        while max_heap:
            _, u = heapq.heappop(max_heap)
            if self.graph.colors[u] == -1:
                best_color = self._choose_color(u, available_colors)
                self._assign_color(u, best_color, degrees,
                                   saturation, available_colors)
                for neighbor in self.graph.adjacency_list[u]:
                    if self.graph.colors[neighbor] == -1:
                        saturation[neighbor] += 1
                        heapq.heappush(
                            max_heap, (-saturation[neighbor], neighbor))

        return self.graph.colors

     # Choose the best color for the vertex based on constraints
    def _choose_color(self, vertex, available_colors):
        return min(available_colors[vertex], key=lambda x: (self._color_degree(vertex, x), x))

      # Assign the chosen color to the vertex and update constraints
    def _assign_color(self, vertex, color, degrees, saturation, available_colors):
        self.graph.colors[vertex] = color
        for neighbor in self.graph.adjacency_list[vertex]:
            if color in available_colors[neighbor]:
                available_colors[neighbor].remove(color)

            # Calculate the number of neighbors with the specified color
    def _color_degree(self, vertex, color):
        return sum(1 for neighbor in self.graph.adjacency_list[vertex] if self.graph.colors[neighbor] == color)


# Initialize with the graph and a solver to enforce constraints
class ConstraintManager:
    def __init__(self, graph, solver):
        self.graph = graph
        self.solver = solver

    # Enforce all constraints and return the result of the coloring algorithm
    def enforce_constraints(self):
        return self.solver.dsatur()

 # Initialize the greedy solver with the given graph
class GreedyColoringSolver:
    def __init__(self, graph):
        self.graph = graph

     # Implement a greedy algorithm for graph coloring
    def greedy_coloring(self):
        for vertex in range(self.graph.num_vertices):
            if self.graph.colors[vertex] == -1:
                forbidden_colors = set(self.graph.colors[neighbor] for neighbor in self.graph.adjacency_list[vertex]
                                       if self.graph.colors[neighbor] != -1)
                for color in range(self.graph.num_vertices):
                    if color not in forbidden_colors:
                        self.graph.colors[vertex] = color
                        break
        return self.graph.colors
