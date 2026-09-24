# Type System

Python objects have types, while names can be rebound to objects of different types as a program runs. Type annotations describe intended contracts for readers and static checkers; they do not enforce those contracts at runtime by themselves.

## Available Exhibit

| Exhibit | What to look for |
| :--- | :--- |
| [Type Annotations](./type_annotations_example.py) | Class attributes and `ClassVar`; framework-style overrides; forward references; `X | None` and `Optional[X]`; interpreting checker diagnostics. |

Run it from the repository root with `python pythonic_thinking/type_system/type_annotations_example.py`. The exhibit shows why an annotation should describe the real contract, rather than merely silence a warning.

<details>
<summary>What the type system includes</summary>

A type system describes kinds of values, how they can be used, and how they relate. Python's runtime behaviour and the contracts checked by tools such as mypy are related parts of this picture.

| Future topic | Question it may answer |
| :--- | :--- |
| Dynamic typing | What has a type at runtime: a name, an object, or both? |
| Unions, optional values, and narrowing | How can a checker know which type a value has at a particular point? |
| Structural typing and `Protocol` | When is matching behaviour enough without explicit inheritance? |
| Generics and `Any` | How can a type relationship be reused, and where does checking become less precise? |
| Equality and hashability | Which operations can an object support, and how do they affect collections? |

These topics are planned directions, not exhibits that are already present.

</details>

---

[Return to Pythonic Thinking](../README.md) for other topics.

[Return to the Zoo map](../../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
