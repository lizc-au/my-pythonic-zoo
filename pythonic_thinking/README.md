# Pythonic Thinking

Learn the mental models behind Python's behaviour, from names and objects to types and execution. These exhibits explain why code works as it does and when a familiar approach from another language may behave differently.

## Explore the Topics

| Topic | What it explores | Status |
| :--- | :--- | :--- |
| [Mental Model](./mental_model/README.md) | Names and objects, mutation and copying, iteration, and functions as objects | Available |
| [Type System](./type_system/README.md) | Dynamic typing, annotations, static checking, protocols, equality, and hashability | Growing |
| [Context Managers](./context_managers/README.md) | `with`, enter and exit, managed resources, and exception behaviour | Growing |
| Pythonic Idioms | Unpacking, comprehensions, `enumerate()`, and `zip()` | Planned |
| Classic Pitfalls | Mutable defaults, copying, closures, shared attributes, identity, and exhausted iterators | Planned |
| Familiar but Different | Truthiness, operators, division, slicing, scope, `None`, and strings | Planned |
| Object Model | Attributes, binding, properties, special methods, dataclasses, descriptors, and method resolution | Planned |
| Runtime and Imports | Module execution, caching, packages, imports, and object lifetime | Planned |
| Advanced Execution | Generators, threads, processes, the GIL, `async`/`await`, and event loops | Planned |

The linked topics have guides and runnable exhibits today. The other rows describe directions for future exhibits, not empty folders to navigate.

## Start Here

Begin with [Mental Model](./mental_model/README.md) if these ideas are new to you. Its explanations of objects, mutation, and iteration provide a foundation for the other topics.

| Next interest | Suggested direction |
| :--- | :--- |
| What do type hints mean? | [Type System](./type_system/README.md) |
| What happens around a `with` block? | [Context Managers](./context_managers/README.md) |
| Why did familiar code surprise me? | Return to Mental Model, then follow the planned Classic Pitfalls and Familiar but Different topics. |
| How does Python's class machinery work? | Explore [Object-Oriented Python](../object_oriented/README.md) while the Object Model exhibits are planned. |

From the repository root, try `python pythonic_thinking/mental_model/names_and_objects_example.py`. The example is self-contained and shows the distinction between names and the objects they reference.

<details>
<summary>What does "Pythonic" mean?</summary>

*Pythonic* describes approaches that work naturally with Python's language features, semantics, and conventions. It favours clear intent and appropriate use of the language over clever brevity.

| Reference | Why read it |
| :--- | :--- |
| [PEP 20 - The Zen of Python](https://peps.python.org/pep-0020/) | Guiding principles for readable Python. |
| [PEP 8 - Style Guide](https://peps.python.org/pep-0008/) | Widely used code style conventions. |
| [Python Language Reference](https://docs.python.org/3/reference/) | Technical definition of language behaviour. |

These references provide useful principles and precise definitions. The exhibits connect those ideas to small examples you can run and inspect.

</details>

<details>
<summary>How the topics fit together</summary>

Mental Model is the first completed area; Type System and Context Managers have initial exhibits and can grow further. The remaining topics are a roadmap, so follow your interests rather than waiting for every section to be filled.

The planned Object Model topic focuses on Python's class machinery and behaviour. [Object-Oriented Python](../object_oriented/README.md) instead explores design decisions and how objects collaborate.

Advanced Execution will begin with generators before moving into concurrency, parallelism, threads, processes, and asynchronous programming.

</details>

Suggestions, corrections, and contributions are welcome through the [Issues page](https://github.com/lizc-au/my-pythonic-zoo/issues).

---

[Return to the Zoo map](../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
