import heapq
from graphviz import Digraph
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        # Priority queue needs to know how to compare Node objects. Lower frequency has higher priority.
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    # Create a priority queue to hold the nodes
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    # Combine nodes until there is only one node remaining (the root)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0] if priority_queue else None

def generate_huffman_codes(root, code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = code

    generate_huffman_codes(root.left, code + "0", codes)
    generate_huffman_codes(root.right, code + "1", codes)

    return codes



def visualize_huffman_tree(root):
    def add_nodes_edges(node, graph, node_id):
        # Non-leaf nodes use frequency only as label
        if node.char is None:
            node_label = f"{node.freq}"
        else:
            # Leaf nodes use char:frequency as label
            node_label = f"{node.char}"

        # Add the current node to the graph
        graph.node(node_id, label=node_label)

        # Recursively add left and right children
        if node.left is not None:
            left_id = f"{node_id}l"
            graph.edge(node_id, left_id, label="0")
            add_nodes_edges(node.left, graph, left_id)
        
        if node.right is not None:
            right_id = f"{node_id}r"
            graph.edge(node_id, right_id, label="1")
            add_nodes_edges(node.right, graph, right_id)

    # Initialize graph and add nodes and edges
    graph = Digraph()
    add_nodes_edges(root, graph, "root")
    # Render the graph to a file and open it
    graph.render('huffman_tree', view=True)

# Build Huffman Tree


# Visualize Huffman Tree


inp = input("Enter the string to encode: ")

# Calculate frequencies
frequencies = {}
# t : 5, r : 4, a : 2, d : 2, o : 2, e : 2, u : 1, = : 1, i : 1
frequencies = {'t': 5, 'r': 4, 'a': 2, 'd': 2, 'o': 2, 'e': 2, 'u': 1, '=': 1, 'i': 1}
for char in inp:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

# Sort the frequencies (not necessarily needed for encoding but useful for understanding)
frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1]))

# Build Huffman Tree
root = build_huffman_tree(frequencies)

# Generate Huffman Codes
huffman_codes = generate_huffman_codes(root)


# print the frequencies
print("The frequencies are:", frequencies)


# Print Huffman Tree
print("We build a huffman tree:")
visualize_huffman_tree(root)

# Print Huffman Codes
print("This gives us the huffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")


encoded_string = ' '.join(huffman_codes[char] for char in inp)

print("which means the final encoding is:")
print(encoded_string)
print("we added spaces to make it more readable")






