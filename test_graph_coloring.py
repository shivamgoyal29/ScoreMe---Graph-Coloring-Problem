import random
import time
from graph_coloring import Graph, ColoringSolver, ConstraintManager, GreedyColoringSolver


def test_basic_coloring():
    """Test basic graph coloring without constraints."""
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    solver = ColoringSolver(g)
    result = solver.dsatur()

    # Check that the number of colors used is within expected bounds
    num_colors_used = len(set(result))
    assert num_colors_used <= 3, f"Expected <= 3 colors, but got {
        num_colors_used}"


def test_pre_assigned_colors():
    """Test graph coloring with pre-assigned colors."""
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.set_pre_assigned_color(0, 0)
    g.set_pre_assigned_color(1, 1)

    solver = ColoringSolver(g)
    result = solver.dsatur()

    assert result[0] == 0, "Vertex 0 should be colored with color 0"
    assert result[1] == 1, "Vertex 1 should be colored with color 1"


def test_color_exclusion():
    """Test graph coloring with color exclusions."""
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.set_color_exclusion(1, 0)  # Exclude color 0 for vertex 1

    solver = ColoringSolver(g)
    result = solver.dsatur()

    assert result[1] != 0, "Vertex 1 should not be colored with color 0"


def test_dynamic_changes():
    """Test graph coloring with dynamic graph changes."""
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    solver = ColoringSolver(g)
    manager = ConstraintManager(g, solver)

    # Apply dynamic changes
    g.add_edge(4, 0)
    g.remove_edge(0, 2)

    result = manager.enforce_constraints()

    num_colors_used = len(set(result))
    assert num_colors_used <= 4, f"Expected <= 4 colors after dynamic changes, but got {
        num_colors_used}"


def test_large_graph():
    """Stress test with a large graph."""
    num_vertices = 10000
    num_edges = 50000

    g = Graph(num_vertices)
    edges_added = set()

    while len(edges_added) < num_edges:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v and (u, v) not in edges_added and (v, u) not in edges_added:
            g.add_edge(u, v)
            edges_added.add((u, v))

    solver = GreedyColoringSolver(g)

    start_time = time.time()
    result = solver.greedy_coloring()  # Call the correct method
    end_time = time.time()

    # Count the number of unique colors used
    num_colors_used = len(set(result))
    print(f"Number of colors used in large graph: {num_colors_used}")

    print(f"Time taken for large graph: {end_time - start_time} seconds")

    assert result is not None, "Coloring result should not be None"
    # Optionally, check if the number of colors is within an expected range
    assert num_colors_used <= num_vertices, "More colors used than vertices available"

    return num_colors_used


def test_edge_cases():
    """Test edge cases including empty graphs and single vertex graphs."""
    # Empty graph
    g_empty = Graph(0)
    solver_empty = ColoringSolver(g_empty)
    result_empty = solver_empty.dsatur()
    assert result_empty == [], "Empty graph should result in an empty coloring list"

    # Single vertex graph
    g_single = Graph(1)
    solver_single = ColoringSolver(g_single)
    result_single = solver_single.dsatur()
    assert len(
        result_single) == 1, "Single vertex graph should have exactly one color assigned"
    assert result_single[0] == 0, "Single vertex should be colored with color 0"


if __name__ == '__main__':
    test_basic_coloring()
    test_pre_assigned_colors()
    test_color_exclusion()
    test_dynamic_changes()
    test_large_graph()
    test_edge_cases()
    print("All tests passed!")
