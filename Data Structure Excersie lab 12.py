class Graph:
    def __init__(self, V):
        # Constructor initializes a graph with V vertices
        self.V = V  # Number of vertices
        self.adj = {}  # Dictionary to store adjacency list for each vertex
        # Initialize adjacency lists for all vertices
        for i in range(V):
            self.adj[i] = []

    def add_edge(self, v, w):
        # Adds an edge to the directed graph; edge from v to w.
        if v not in self.adj:
            self.adj[v] = []
        self.adj[v].append(w)

    def dfs_iterative(self, start):
        """
        Performs an iterative DFS traversal using an explicit stack
        starting from the given start vertex.
        
        :param start: The start vertex from where DFS starts.
        :return: List representing the DFS traversal order.
        """
        # Stack to store the vertices for DFS traversal
        stack = [start]
        # List to keep track of visited vertices to avoid cycles
        visited = []
        
        # DFS as long as there are vertices to process
        while stack:
            # Pop a vertex from the stack
            v = stack.pop()
            
            # If not visited, process it
            if v not in visited:
                # Mark the vertex as visited
                visited.append(v)
                # Add all unvisited neighbors to the stack for future processing
                # Reversed to maintain the correct traversal order
                for neighbor in reversed(self.adj[v]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return visited

# Create the graph with given vertices and edges
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 3)
g.add_edge(3, 5)

# Perform DFS traversal
dfs_order = g.dfs_iterative(0)

# Test cases written as code comments:

# Test Case 1: Ensure the DFS traversal starts from the correct vertex (0)
assert dfs_order[0] == 0, "DFS did not start from vertex 0."

# Test Case 2: Ensure all vertices are visited in the traversal.
assert len(dfs_order) == g.V, "Not all vertices were visited in DFS."

# Test Case 3: Ensure there are no duplicates in the traversal.
assert len(dfs_order) == len(set(dfs_order)), "There are duplicates in DFS traversal."

# Test Case 4: Test the graph with a cycle to ensure it doesn't get stuck in an infinite loop.
g.add_edge(5, 2)  # Create a cycle: 2 -> 4 -> 5 -> 2
dfs_order_cycle = g.dfs_iterative(0)
assert len(dfs_order_cycle) == len(set(dfs_order_cycle)), "DFS got stuck in a cycle."

# Test Case 5: Ensure the function works for a graph with no edges.
g_no_edges = Graph(6)
dfs_order_no_edges = g_no_edges.dfs_iterative(0)
assert dfs_order_no_edges == [0], "DFS failed for graph with no edges."

# Test Case 6: Ensure the function works for disconnected graphs.
g_disconnected = Graph(6)
g_disconnected.add_edge(0, 1)
g_disconnected.add_edge(2, 3)
dfs_order_disconnected = g_disconnected.dfs_iterative(0)
assert dfs_order_disconnected == [0, 1], "DFS failed for disconnected graph."

# End of test cases

print(dfs_order)  # The result of the DFS traversal for the given graph.
