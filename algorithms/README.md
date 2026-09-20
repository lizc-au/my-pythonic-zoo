# Algorithms

This category explores algorithms by building the mental model behind them,
not just presenting a finished implementation.

The examples favour small, runnable demonstrations that expose the decisions,
data structures, and transformations involved. Where an algorithm depends on
less familiar foundations, those foundations may be taught as part of a
deliberate progression before the complete algorithm is assembled.

## Binary Search Trees

A Binary Search Tree (BST) stores values in linked nodes while maintaining an
ordering rule: every value in a node's left subtree is smaller than that node,
and every value in its right subtree is larger.

This progression introduces the structure and its operations in stages before
combining them into an interactive terminal visualizer. The examples use an
ordinary, unbalanced BST as a teaching structure. Its operations can be
efficient when the tree is reasonably balanced, but a skewed tree can degrade
to linear behaviour.

### Study Sequence

Follow the exhibits in this order:

1. **[Structure and Ordering](./binary_search_tree/bst_structure_example.py)**
   introduces nodes, child references, empty branches, and the full BST ordering
   invariant by constructing trees manually.
   *(Contributed by [@Reh1t](https://github.com/Reh1t) via
   [#55](https://github.com/lizc-au/my-pythonic-zoo/pull/55))*

2. **[Traversal, Insertion and Searching](https://github.com/lizc-au/my-pythonic-zoo/issues/52)**
   will introduce recursive in-order traversal, automate the ordering decisions,
   and use the invariant to guide searches.

3. **[Deletion](https://github.com/lizc-au/my-pythonic-zoo/issues/53)**
   will explain the leaf, one-child, and two-child deletion cases.

4. **[Rendering and Interactive Terminal Visualizer](https://github.com/lizc-au/my-pythonic-zoo/issues/54)**
   will render the tree without changing it, then combine the completed
   operations in an interactive terminal application.

Each module is intended to remain directly runnable and understandable on its
own. A small amount of repetition is deliberate so learners can study one stage
without first reconstructing its foundations from several other files.

### Where this leads

In production systems, developers usually rely on balanced structures such as
AVL or Red-Black trees, or storage-oriented B-tree variants supplied by
libraries, language runtimes, and databases, rather than implementing an
ordinary Binary Search Tree directly. For that reason, this progression
culminates in visualizers that make the underlying structure and algorithms
observable instead of inventing a contrived business application.

The interactive terminal visualizer will complete this algorithmic progression.
A later Native GUI exhibit may reuse the completed BST operations in a Tkinter
visualizer, focusing on Canvas drawing, event handling, and responsive layout
while cross-referencing these modules for the underlying tree algorithms.

---

## Dancing Links

### What is Dancing Links?

Dancing Links (DLX) is Donald Knuth's technique for implementing Algorithm X,
a backtracking algorithm for Exact Cover problems. It represents the problem as
a circular, doubly linked matrix whose nodes can be temporarily removed and
restored very efficiently as the search explores different possibilities.

The name comes from those reversible link changes: as Algorithm X moves forward
and backtracks, links disappear from and return to the active structure. The
individual exhibits below explain each part of that mechanism in detail, so this
README provides only the overview rather than repeating their teaching material.

Dancing Links can look surprisingly opaque when encountered as a finished
implementation. This progression therefore separates the ideas that make it
work, introducing each one before combining them.

### Study Sequence

Follow the exhibits in this order:

1. **[Exact Cover](./dancing_links/exact_cover_example.py)** introduces the
   problem: choose rows so every required column is covered exactly once.

2. **[Algorithm X](./dancing_links/algorithm_x_example.py)** introduces the
   recursive search and backtracking algorithm used to solve Exact Cover
   problems.

3. **[Linked Nodes](./dancing_links/linked_nodes_example.py)** demonstrates how
   a node can be temporarily unlinked without being destroyed, then restored
   using the references it retained.

4. **[Circular Links](./dancing_links/circular_links_example.py)** removes the
   special end cases of a linear chain by making horizontal and vertical links
   wrap around.

5. **[Toroidal Matrix](./dancing_links/toroidal_matrix_example.py)** combines
   the horizontal and vertical circles so every node participates in both at
   once.

6. **[Cover and Uncover](./dancing_links/cover_uncover_example.py)** demonstrates
   the reversible structural changes that allow a search to remove possibilities
   temporarily and restore them during backtracking.

7. **[Exact Cover Matrix](./dancing_links/exact_cover_matrix_example.py)**
   translates the original Exact Cover requirements and choices into the linked
   matrix representation that Dancing Links operates on.

8. **[Dancing Links](./dancing_links/dancing_links_example.py)** combines the
   complete progression: Algorithm X searches the Exact Cover matrix while
   cover and uncover modify its linked structure reversibly.

Each exhibit is intended to be understood before moving to the next. The later
examples deliberately assume familiarity with the concepts introduced earlier
rather than attempting to explain the entire technique again in every file.

### Why are Exact Cover and Algorithm X in the Dancing Links folder?

Exact Cover and Algorithm X are not themselves Dancing Links. Exact Cover is the
problem being solved, while Algorithm X is the search algorithm. Both can be
studied and implemented without DLX.

These particular exhibits live in `dancing_links` because they were written as
the opening stages of this teaching progression. Moving them elsewhere would
separate the prerequisites from the sequence that depends on them.

If the Algorithms category later develops broader treatments of Exact Cover or
Algorithm X, those can exist independently. The versions here can remain focused
on preparing the reader for Dancing Links.

### Why do the examples repeat some code?

The exhibits in this section form a teaching progression, not a production
application split across modules. Each example is intentionally self-contained
so it can be opened, run, and studied independently. Later exhibits therefore
repeat some familiar classes and linking operations while adding the next
concept, rather than importing their implementation from earlier teaching
examples.

Once you understand the complete progression, you may prefer to refactor the
implementation into reusable components. That is a worthwhile next exercise:
the individual responsibilities and their relationships should now be familiar
enough to decide where the module boundaries belong.

If you take that challenge on, consider opening an Issue and working on a
branch, then contribute the result back as a separate, fully modularised example
in its own sub-folder. The teaching progression can remain intact alongside it,
giving visitors both a step-by-step explanation and an example of how the same
design might be structured for reuse and maintenance.

### Where this leads

The small Exact Cover problem used throughout this study sequence keeps the
mechanics visible while the technique is being learned. A future exhibit is
planned to apply the completed Dancing Links implementation to a more substantial
Sudoku or logic-puzzle problem, showing how a real constraint problem can first
be translated into Exact Cover and then solved using Algorithm X with DLX.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _algorithms/README.md_ | _20 September 2026_ | _lizc-au_ |

---
