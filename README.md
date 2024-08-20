# Graph Coloring Problem - ScoreMe

## Overview
This project provides a sophisticated solution to the graph coloring problem, incorporating a range of constraints that add complexity and realism to the challenge. The goal is to color the vertices of a graph such that no two adjacent vertices share the same color, all while adhering to additional constraints such as minimizing the number of colors used, respecting pre-assigned colors, handling color exclusions, and dynamically adapting to graph changes.

## Features
- **Minimum Colors Constraint**: Ensures the graph is colored using the minimum number of colors possible.
- **Pre-Assigned Colors**: Accommodates vertices that have been pre-colored, which cannot be changed during the process.
- **Color Exclusion**: Efficiently handles situations where certain colors are not allowed on specific vertices.
- **Dynamic Graph Changes**: Adapts to modifications in the graph (e.g., adding/removing vertices or edges) without the need to completely redo the coloring.
- **Heuristic Optimization**: Utilizes heuristic approaches to improve performance, such as greedy algorithms and metaheuristic methods.
- **Performance-Optimized**: Designed to efficiently handle large graphs with up to 10,000 vertices and 50,000 edges.

## Design and Architecture

### Graph Class
- **Purpose**: Manages the graph structure, including adding or removing vertices and edges.
- **Key Functions**:
  - `add_edge(u, v)`: Connects vertices `u` and `v`.
  - `remove_edge(u, v)`: Removes the connection between `u` and `v`.
  - `set_pre_assigned_color(vertex, color)`: Sets a fixed color for a vertex.
  - `set_color_exclusion(vertex, color)`: Prevents a vertex from using a specific color.

### ColoringSolver Class
- **Purpose**: Handles the graph coloring using the DSATUR algorithm.
- **Key Functions**:
  - `dsatur()`: Colors the graph while meeting all constraints.
  - `apply_color(vertex, color)`: Colors a vertex with the specified color.

### ConstraintManager Class
- **Purpose**: Manages and applies constraints during the coloring process.
- **Key Function**:
  - `enforce_constraints()`: Ensures all constraints are applied during coloring.

## Performance Analysis
- **Time Complexity**: DSATUR algorithm is efficient, with a complexity of O(V^2 log V), where V is the number of vertices.
- **Space Complexity**: Uses O(V + E) space, where E is the number of edges.
- **Practical Performance**: Handles large graphs efficiently and remains responsive with up to 10,000 vertices and 50,000 edges.

## Code Readability
- **Modular Design**: Clear separation of different components.
- **Documentation**: Comments and explanations are provided for clarity.
- **Best Practices**: Follows Python conventions for maintainability.

## How to Run

### Installation
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-repo/graph_coloring.git
    cd graph_coloring
    ```
2. **Install Dependencies:**
    No extra packages needed, just Python 3.x.

### Running the Implementation
- Import the classes from `graph_coloring.py` in your project.
- Use them as shown in `test_graph_coloring.py`.

### Running the Tests
To test the solution:
```bash
python test_graph_coloring.py
```
The tests cover:
- **Basic Coloring**: Simple graph tests.
- **Pre-Assigned Colors**: Checks respect for pre-colored vertices.
- **Color Exclusion**: Tests color restrictions.
- **Dynamic Changes**: Evaluates adaptability to graph modifications.
- **Large Graphs**: Performance and correctness on big graphs.
