"""
test_bst_structure_example.py

Test the foundational mental model of a Binary Search Tree (BST).

These tests ensure that the structural rules we teach in the example module
hold true programmatically. We test manually constructed relationships,
empty branches, and explicit ordering comparisons without relying on
traversal algorithms (which belong in later modules).
"""

from algorithms.binary_search_tree.bst_structure_example import Node

# --- Initialization & Structure Tests ---


def test_node_initializes_with_value_and_empty_branches() -> None:
    """A new node should store its value and default to having no children."""
    test_value = 42
    node = Node(test_value)

    assert node.value == test_value
    assert node.left is None
    assert node.right is None


def test_node_can_be_explicitly_linked_to_children() -> None:
    """Nodes should retain the exact references we assign to their left and right."""
    parent = Node(10)
    left_child = Node(5)
    right_child = Node(15)

    parent.left = left_child
    parent.right = right_child

    # We use 'is' to verify it points to the exact same object in memory,
    # not just another node that happens to have the same value.
    assert parent.left is left_child
    assert parent.right is right_child


# --- Ordering Rule Tests ---


def test_manual_bst_satisfies_ordering_comparisons() -> None:
    """Directly verify the relationships and ordering of a manual BST."""
    # This tree matches 'demonstrate_ordering_rule' from the main module.
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)

    # We assert they are not None to satisfy type checkers before accessing .left/.right
    assert root.left is not None
    assert root.right is not None

    # Verify empty branches (leaves)
    assert root.right.left is None
    assert root.right.right is None

    # Verify the manually constructed relationships and values
    expected_root = 20
    expected_left = 10
    expected_right = 30
    assert root.value == expected_root
    assert root.left.value == expected_left
    assert root.right.value == expected_right

    # Directly verify the ordering comparisons (the rule)
    assert root.left.value < root.value
    assert root.right.value > root.value

    # Check the left child's children
    assert root.left.left is not None
    assert root.left.right is not None
    assert root.left.left.value < root.left.value
    assert root.left.right.value > root.left.value

    # Directly compare 5 and 15 with the root value of 20 to prove the
    # full subtree invariant.
    assert root.left.left.value < expected_root
    assert root.left.right.value < expected_root
