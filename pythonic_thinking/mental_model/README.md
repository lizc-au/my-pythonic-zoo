# 🧠 Mental Model

Python becomes easier to reason about when **your mental model matches its underlying behaviour**.

This collection explores several foundational ideas that influence how Python programs behave: how names relate to objects, what mutation means, how iteration works, and why functions can be treated like other objects.

Understanding these concepts provides a foundation for many of the pitfalls, idioms, and design choices explored elsewhere in **Pythonic Thinking**.

---

## 🗺️ Exhibits

### [Names and Objects](./names_and_objects_example.py)

Understand that Python variables are names bound to objects rather than containers that inherently store or copy values. This foundation helps explain assignment, identity, function arguments, and many apparently surprising Python behaviours.

### [Mutation and Copying](./mutation_and_copying_example.py)

Explore the difference between rebinding a name and changing an existing object, why multiple names can refer to the same mutable object, and why shallow and deep copying are importantly different operations.

### [Iteration](./iteration_example.py)

Understand Python's iterable and iterator model, why `for` loops operate on objects that produce values rather than acting primarily as counting loops, and how this model supports many Pythonic constructs.

### [Functions as Objects](./functions_as_objects_example.py)

Explore what it means for functions to be first-class objects: they can be assigned to names, stored, passed to other functions, and returned like other Python objects. The exhibit also introduces `lambda` expressions for creating short function objects at the point of use, and `functools.partial()` for creating callables with selected arguments already supplied. These techniques are especially useful for callbacks, adapters, decorators, and other patterns that pass behaviour around as data.

---

## 🔗 Where These Ideas Lead

These foundations recur throughout **Pythonic Thinking**. Names and mutation help explain shared state and mutable defaults; the iteration model leads naturally to generators, comprehensions, `enumerate()`, and `zip()`; and treating functions as objects provides the foundation for callbacks and decorators.

Later exhibits build on these ideas rather than treating each Python behaviour as an isolated rule to memorise.

[← Back to Pythonic Thinking](../README.md)

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _pythonic_thinking/mental_model/README.md_ | _11 September 2026_ | _lizc-au_ |

---
