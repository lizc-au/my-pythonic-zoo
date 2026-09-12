# 🏷️ Type System

A **type system** is the collection of rules and concepts a programming language uses to describe different kinds of values, how those values can be used, and how types relate to one another.

Python is dynamically typed at runtime: objects have types, while names can be rebound to objects of different types as a program runs. Python also supports type annotations, which let developers describe expected types and contracts that static analysis tools can check without changing Python's fundamentally dynamic runtime behaviour.

This category explores both sides of Python's type system. Topics can include type annotations, dynamic typing, unions and optional values, `ClassVar`, forward references, type narrowing, structural typing with `Protocol`, generics, `Any`, equality, hashability, and other concepts that help explain how Python represents and reasons about types.

---

## 🗺️ Exhibits

### [Type Annotations](./type_annotations_example.py)

Understand what type annotations communicate and why stricter-looking annotations are not automatically more accurate. The exhibit explores ordinary class attributes versus `ClassVar`, framework-style attribute overrides, forward references, `X | None` versus `Optional[X]`, and how to interpret static type-checker diagnostics without distorting working code merely to silence warnings.

---

## 🔗 Where These Ideas Lead

Later exhibits can build on these foundations with Python's dynamic typing model, structural typing and `Protocol`, type narrowing, generics, equality, hashability, and other parts of Python's type system.

[← Back to Pythonic Thinking](../README.md)

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _pythonic_thinking/type_system/README.md_ | _12 September 2026_ | _lizc-au_ |

---