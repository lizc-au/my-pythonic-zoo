"""
bst_structure_example.py

Introduce the underlying structure of a Binary Search Tree (BST) and its core
ordering rule, without hiding the mechanics behind automated algorithms.

While an ordinary Binary Search Tree is primarily a foundational teaching
tool (because it can become unbalanced and lose its speed advantage), its
concepts form the core basis for more advanced, self-balancing trees (like
AVL or Red-Black trees). Those advanced trees are used in real-world
operating system memory management and in-memory database engines.

Before learning how a BST automatically inserts, searches, or deletes data, a
learner must first understand two things:
1. How individual pieces of data (``Node`` objects) are linked together.
2. The mathematical rule (the Invariant) that dictates where a ``Node`` belongs.

Because this module focuses only on the manual structure, we do not need
to handle duplicate values yet. When we introduce automatic insertion
algorithms in later modules, those examples will handle duplicates by
simply ignoring them.
"""

from __future__ import annotations


class Node:
    """
    Represent a single piece of data within the tree.

    A tree is built by linking these nodes together. Each node holds its own
    value and maintains references (pointers) to its left and right children.

    The ``left`` and ``right`` attributes are object references. To understand
    more deeply how Python handles names and objects in memory, see the exhibit
    at ``pythonic_thinking/mental_model/names_and_objects_example.py``.
    """

    def __init__(self, value: int) -> None:
        """
        Create a new node.

        When a node is first created, it has no children. In Python, we use the
        special keyword ``None`` to indicate the absence of a value. The type hint
        ``Node | None`` indicates the intended type to readers and static-analysis
        tools. It means this attribute will either point to another ``Node`` object,
        or it will be ``None`` (a dead end).

        Note that type hints like ``Node | None`` are not enforced by Python at
        runtime. They exist to help human readers and static-analysis tools. For
        more on this, see ``pythonic_thinking/type_system/type_annotations_example.py``.
        """
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


def demonstrate_nodes_and_links() -> None:
    """
    Show how individual Node objects are manually linked to form a tree shape.
    """
    print("=== Demonstration 1: Nodes and Links ===")

    # We create three independent, disconnected nodes.
    root_node = Node(10)
    left_child = Node(5)
    right_child = Node(15)

    print("Created three independent nodes: 10, 5, and 15.")

    # We link them together by assigning the child nodes to the references
    # inside the root node. This manual linking is exactly what automated
    # tree algorithms do behind the scenes.
    root_node.left = left_child
    root_node.right = right_child

    print("Linked 5 to the left of 10, and 15 to the right of 10.\n")

    print("Let's observe the actual Python references in memory:")
    print(f"  root_node.value       = {root_node.value}")
    # We prove the link exists by accessing the left child's value through the root.
    print(f"  root_node.left.value  = {root_node.left.value}")
    print(f"  root_node.right.value = {root_node.right.value}\n")


def demonstrate_ordering_rule() -> None:
    """
    Explain and manually apply the Binary Search Tree Ordering Rule.

    The Rule (Invariant):
    - Every value in a node's left subtree must be smaller than that node.
    - Every value in its right subtree must be larger.
    """
    print("=== Demonstration 2: The Ordering Rule ===")
    print("Building a valid BST manually to satisfy the ordering rule...")

    # We choose 20 as the root of our tree.
    root = Node(20)

    # We want to add 10 to the tree. Because 10 < 20, the rule dictates it
    # must go to the left.
    node_10 = Node(10)
    root.left = node_10
    print("- Added 10 to the left of 20 (because 10 < 20)")

    # We want to add 30. Because 30 > 20, it must go to the right.
    node_30 = Node(30)
    root.right = node_30
    print("- Added 30 to the right of 20 (because 30 > 20)")

    # We want to add 5. Starting from the root (20), 5 < 20 (go left).
    # The left spot is taken by 10. We compare 5 to 10. 5 < 10, so it goes
    # to the left of 10.
    node_5 = Node(5)
    node_10.left = node_5
    print("- Added 5 to the left of 10 (because 5 < 10)")

    # We want to add 15. Start at root (20). 15 < 20 (go left).
    # The left spot is taken by 10. Compare 15 to 10. 15 > 10, so it goes
    # to the right of 10.
    node_15 = Node(15)
    node_10.right = node_15
    print("- Added 15 to the right of 10 (because 15 > 10)\n")

    print(
        "The mental model is now complete: we have nodes linked together,\n"
        "and they are arranged according to a strict mathematical rule.\n\n"
        "A Note on Duplicates:\n"
        "Because this module focuses only on structure, we don't handle\n"
        "duplicates yet. When we introduce insertion algorithms later,\n"
        "those examples will handle duplicates by simply ignoring them.\n"
    )

    print("Let's trace the objects to prove the structure exists in memory:")

    # We must prove these links aren't 'None' before accessing them.
    # These assertions confirm the expected links at runtime and narrow
    # their types for the static type checker.
    assert root.left is not None
    assert root.left.left is not None
    assert root.left.right is not None

    print(f"  root.value            = {root.value}")
    print(f"  root.left.value       = {root.left.value}  (10 < 20)")
    print(f"  root.left.left.value  = {root.left.left.value}   (5 < 10)")
    print(f"  root.left.right.value = {root.left.right.value}  (15 > 10)\n")


def main() -> None:
    """Execute the module's demonstrations."""
    print("--- Binary Search Tree: Structure & Invariant ---\n")
    demonstrate_nodes_and_links()
    demonstrate_ordering_rule()


# In Python, this special block ensures that the main() function is only called
# if this file is run directly (e.g., 'python bst_structure_example.py').
# If another file imports this module, this code will safely do nothing.
if __name__ == "__main__":
    main()
