import pytest
from BinarySearchTree import BinarySearchTree
from HashTable import HashTable
def test_bst_insert_and_search():
    bst = BinarySearchTree()
    bst.insert(15, "ItemA")
    bst.insert(10, "ItemB")
    bst.insert(20, "ItemC")
    assert bst.search(10) == "ItemB"
    assert bst.search(99) is None

def test_bst_inorder_traversal():
    bst = BinarySearchTree()
    for k in [15, 10, 20]:
        bst.insert(k)
    assert bst.inorder_traversal() == [10, 15, 20]

def test_hash_table_insert_and_search():
    ht = HashTable(size=5)
    ht.insert("user1", "ItemA")
    ht.insert("user2", "ItemB")
    assert ht.search("user1") == "ItemA"
    assert ht.search("userX") is None

def test_hash_table_remove():
    ht = HashTable(size=5)
    ht.insert("user1", "ItemA")
    ht.remove("user1")
    assert ht.search("user1") is None
