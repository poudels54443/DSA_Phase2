class Node:
    def __init__(self, key, value=None):
        self.key = key              # Node's key
        self.value = value          # Optional value associated with the key
        self.left = None            # Left child
        self.right = None           # Right child

class BinarySearchTree:
    def __init__(self):
        self.root = None            # Initialize an empty tree

    def insert(self, key, value=None):
        if self.root is None:
            self.root = Node(key, value)  # Insert at root if tree is empty
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, current_node, key, value):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key, value)
            else:
                self._insert_recursive(current_node.left, key, value)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key, value)
            else:
                self._insert_recursive(current_node.right, key, value)
        else:
            current_node.value = value  # Update value if key already exists

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None:
            return None  # Key not found
        if key == current_node.key:
            return current_node.value if current_node.value is not None else True
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result_list):
        if current_node:
            self._inorder_recursive(current_node.left, result_list)
            result_list.append(current_node.key)  # Add key in sorted order
            self._inorder_recursive(current_node.right, result_list)
