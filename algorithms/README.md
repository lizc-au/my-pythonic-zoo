# Algorithms

Explore algorithms through small, runnable demonstrations of the structures and decisions behind them. The longer paths introduce each prerequisite before assembling the complete technique.

## Choose a Learning Path

| Path | Start with | Build toward |
| :--- | :--- | :--- |
| [Binary Search Trees](#binary-search-trees) | Nodes and the ordering invariant | Traversal, updates, and an interactive visualizer |
| [Dancing Links](#dancing-links) | Exact Cover and Algorithm X | A linked matrix with reversible cover and uncover |

## Binary Search Trees

A binary search tree (BST) stores values in linked nodes. Every value in a node's left subtree is smaller than that node, and every value in its right subtree is larger.

| Stage | Exhibit or plan | What it teaches |
| :--- | :--- | :--- |
| 1 · Available | [Structure and Ordering](./binary_search_tree/bst_structure_example.py) | Nodes, empty branches, manual links, and the full subtree ordering rule. |
| 2 · Planned | [Traversal, Insertion and Searching](https://github.com/lizc-au/my-pythonic-zoo/issues/52) | In-order traversal and operations guided by the invariant. |
| 3 · Planned | [Deletion](https://github.com/lizc-au/my-pythonic-zoo/issues/53) | Leaf, one-child, and two-child cases. |
| 4 · Planned | [Rendering and Interactive Terminal Visualizer](https://github.com/lizc-au/my-pythonic-zoo/issues/54) | Draw the tree and interact with its completed operations. |

Run the first stage from the repository root with `python algorithms/binary_search_tree/bst_structure_example.py`. Stage 1 was contributed by [@Reh1t in PR #55](https://github.com/lizc-au/my-pythonic-zoo/pull/55).

<details>
<summary>Why this path uses an ordinary BST</summary>

The examples use an unbalanced BST so its structure and ordering decisions remain visible. Operations can be efficient when the tree is reasonably balanced, while a skewed tree can degrade to linear behaviour.

Production systems commonly use balanced or storage-oriented tree variants supplied by libraries, runtimes, or databases. A later Native GUI exhibit may reuse the completed operations to teach Tkinter Canvas drawing and event handling.

Each stage is intended to remain runnable on its own. Some repetition helps a learner study one stage without reconstructing earlier modules.

</details>

## Dancing Links

Dancing Links (DLX) is Donald Knuth's linked-structure technique for implementing Algorithm X, a search algorithm for Exact Cover problems. Its circular, doubly linked matrix lets the search remove possibilities and restore them when it backtracks.

| Stage | Exhibit | What it teaches |
| :--- | :--- | :--- |
| 1 | [Exact Cover](./dancing_links/exact_cover_example.py) | Choose rows that cover every required column exactly once. |
| 2 | [Algorithm X](./dancing_links/algorithm_x_example.py) | Search recursively and backtrack through possible covers. |
| 3 | [Linked Nodes](./dancing_links/linked_nodes_example.py) | Unlink and restore a node using retained references. |
| 4 | [Circular Links](./dancing_links/circular_links_example.py) | Make horizontal and vertical links wrap around. |
| 5 | [Toroidal Matrix](./dancing_links/toroidal_matrix_example.py) | Combine both circular directions in one structure. |
| 6 | [Cover and Uncover](./dancing_links/cover_uncover_example.py) | Remove and restore linked possibilities reversibly. |
| 7 | [Exact Cover Matrix](./dancing_links/exact_cover_matrix_example.py) | Translate requirements and choices into linked nodes. |
| 8 | [Dancing Links](./dancing_links/dancing_links_example.py) | Run Algorithm X over the linked matrix. |

Run the first stage from the repository root with `python algorithms/dancing_links/exact_cover_example.py`. Follow the rows in order, as later exhibits build on concepts introduced earlier.

<details>
<summary>Why Exact Cover and Algorithm X appear in this folder</summary>

Exact Cover is the problem, Algorithm X is the search algorithm, and Dancing Links is one way to implement that search. The first two work independently, but these exhibits introduce them as prerequisites to the DLX progression.

Broader treatments of Exact Cover or Algorithm X could later live elsewhere. The versions here stay focused on preparing the reader for Dancing Links.

</details>

<details>
<summary>Why the exhibits repeat some code</summary>

These are self-contained teaching exhibits, so later stages repeat familiar classes and links while adding one new idea. After studying the full sequence, refactoring it into reusable components is a useful follow-on exercise.

A separate modular example could sit alongside this progression. To propose one, open an [issue](https://github.com/lizc-au/my-pythonic-zoo/issues) and follow the [contribution guide](../CONTRIBUTING.md).

</details>

<details>
<summary>Where Dancing Links may lead</summary>

The current Exact Cover example starts with a small problem so the mechanics are easy to see. Planned puzzle exhibits will increase the scale before tackling a logic puzzle:

| Planned stage | Grid |
| :--- | :--- |
| Shi Doku | 4×4 |
| Go Doku | 5×5 |
| Roku Doku | 6×6 |
| Sudoku | 9×9 |
| Logic puzzle solver | Varies by puzzle |

Each stage will translate its constraints into Exact Cover and solve them with Algorithm X and Dancing Links.

</details>

---

[Return to the Zoo map](../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
