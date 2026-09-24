# Mental Model

Build a clearer picture of how Python works beneath its familiar syntax. These four exhibits explain names, mutation, iteration, and functions as objects.

## Follow the Exhibits

| Step | Exhibit | Main idea | Helps explain |
| :--- | :--- | :--- | :--- |
| 1 | [Names and Objects](./names_and_objects_example.py) | A name refers to an object; assignment does not inherently copy it. | Identity, arguments, and shared references |
| 2 | [Mutation and Copying](./mutation_and_copying_example.py) | Rebinding a name differs from changing an object. | Shared mutable state, shallow copies, and deep copies |
| 3 | [Iteration](./iteration_example.py) | A `for` loop requests values from an iterable through an iterator. | Generators, comprehensions, `enumerate()`, and `zip()` |
| 4 | [Functions as Objects](./functions_as_objects_example.py) | Functions can be stored, passed, and returned like other objects. | Callbacks, adapters, decorators, `lambda`, and `functools.partial()` |

Start from the repository root with `python pythonic_thinking/mental_model/names_and_objects_example.py`. Each exhibit runs independently, though the table gives a useful study order.

<details>
<summary>How these ideas connect</summary>

| Foundation | Later questions it helps answer |
| :--- | :--- |
| Names and objects | Why can two names refer to the same list? What does passing an object to a function do? |
| Mutation and copying | Why did a change appear elsewhere? When is a shallow copy insufficient? |
| Iteration | How do generators supply values? Why can an iterator be exhausted? |
| Functions as objects | How can a button receive a callback? What do `lambda` and `partial()` provide? |

These ideas recur throughout [Pythonic Thinking](../README.md). Later exhibits build on them instead of treating each behaviour as an isolated rule.

</details>

---

[Return to Pythonic Thinking](../README.md) for other topics.

[Return to the Zoo map](../../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
