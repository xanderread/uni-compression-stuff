from graphviz import Digraph

class Node (object):
    def __init__(self, left=None, right=None, value = None, parent = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.left_value = 0
        self.right = right
        self.right_value = 1

    def children(self):
        return (self.left, self.right)
    
    def is_leaf(self):
        return not self.left and not self.right

    def nodes(self):
        return (self.left, self.right)

def add_edges(graph, node, parent_id=None):
    if node:
        node_id = str(id(node))
        if parent_id:
            edge_label = '0' if parent_id.endswith('L') else '1'
            graph.edge(parent_id[:-1], node_id, label=edge_label)
        
        if node.is_leaf():
            graph.node(node_id, str(node.value))
        else:
            graph.node(node_id, height="0", width="0", shape='point')
        
        if node.left:
            add_edges(graph, node.left, node_id + 'L')
        if node.right:
            add_edges(graph, node.right, node_id + 'R')

# Huffman from scratch
def frequencies(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def visualize_tree(root):
    dot = Digraph(comment='Huffman Tree')
    add_edges(dot, root)
    dot.render('huffman_tree', format='pdf')


if __name__ == "__main__":
    text = "aababccabdabbdec"

    # Put all to lower case
    text = text.lower()

    # Replace spaces with _
    text = text.replace(" ", "_")

    freq = frequencies(text)

    # Stores the nodes that don't have parents
    open_nodes = []

    while len(freq) > 1:
        # Find the two least frequent characters in the frequency dictionary
        sorted_freq = sorted(freq.items(), key=lambda x: x[1])

        print("\n\n")
        print(" ---------------------------  ")
        print("\n\n")

        # Print the frequency values in a pretty way
        for [key, value] in reversed(sorted_freq):
            print(f'{key}: {value}')

        char_1 = sorted_freq[0][0]
        char_2 = sorted_freq[1][0]

        # Find index of open_node with the same character as the value for each
        node_1 = next((node for node in open_nodes if node.value == char_1), None)
        if node_1:
            open_nodes.remove(node_1)
        else:
            node_1 = Node(value = char_1)

        node_2 = next((node for node in open_nodes if node.value == char_2), None)
        if node_2:
            open_nodes.remove(node_2)
        else:
            node_2 = Node(value = char_2)


        # Create a parent node for the two least frequent characters
        parent = Node(left = node_1, right = node_2, value = node_1.value + ", " + node_2.value)
        node_1.parent = parent
        node_2.parent = parent

        # Add the new parent node to the open_nodes list
        open_nodes.append(parent)

        del freq[char_1]
        del freq[char_2]
        freq[parent.value] = sorted_freq[0][1] + sorted_freq[1][1]
    
    root = open_nodes[0]
    current_node = root

    visualize_tree(root)

    # Encode the text using this huffman tree
    encoding = ""

    for char in text:
        while not current_node.is_leaf():
            if char in current_node.left.value:
                encoding += "0"
                current_node = current_node.left
            else:
                encoding += "1"
                current_node = current_node.right
        current_node = root
        encoding += " "
    
    print("\n\n")
    print(" ---------------------------  ")
    print("\n\n")

    print(f"Original text: {text}")
    print(f"Encoded text: {encoding}")