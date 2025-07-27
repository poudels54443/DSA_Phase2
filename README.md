# Recommendation System Proof of Concept

This project implements a basic recommendation system using custom data structures, including a **Binary Search Tree (BST)** and a **Hash Table**. It demonstrates key functionalities such as insertion, search, traversal, and collision handling, along with automated unit tests using `pytest`.

## Features

- **Binary Search Tree (BST)**  
  - Insert key-value pairs  
  - Search for keys  
  - In-order traversal for sorted output  

- **Hash Table**  
  - Insert, search, and remove operations  
  - Separate chaining to handle collisions  

- **Unit Tests**  
  - Implemented with `pytest`  
  - Tests edge cases including duplicate insertion, removal, and collision handling  

## Project Structure

```
├── BinarySearchTree.py               # Contains the Node and BinarySearchTree classes
├── HashTable.py         # Contains the HashTable class
├── tests.py   # Pytest test cases for both BST and HashTable
└── README.md            # Project overview and usage instructions
```

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Install Dependencies

Install `pytest` if not already installed:

```bash
pip install pytest
```

### Running the Project

You can manually run the classes using any Python script or open a Python shell and test them like:

```python
from bst import BinarySearchTree
from hashtable import HashTable

# BST example
bst = BinarySearchTree()
bst.insert(15, "Item15")
bst.insert(10, "Item10")
bst.insert(20, "Item20")
print(bst.search(10))  # Output: Item10
print(bst.inorder_traversal())  # Output: [10, 15, 20]

# HashTable example
ht = HashTable()
ht.insert("user1", "ItemA")
ht.insert("user2", "ItemB")
print(ht.search("user1"))  # Output: ItemA
ht.remove("user1")
print(ht.search("user1"))  # Output: None
```

### Running Tests

To run all tests:

```bash
pytest tests.py
```

You should see output confirming that all test cases pass.

## Future Work

- Upgrade BST to AVL Tree for balancing
- Add dynamic resizing to the Hash Table
- Implement collaborative filtering for recommendations