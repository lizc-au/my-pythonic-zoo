# 🐍 Pythonic Thinking

Knowing Python syntax is not quite the same as understanding **how Python works**.

Many Python behaviours become much easier to understand once you know the underlying object, iteration, type, and execution models. The same understanding also explains why some approaches are considered more *Pythonic* than others.

This collection explores those mental models, common surprises, and characteristic Python idioms. Each topic focuses on **why Python behaves as it does**, rather than presenting rules that simply need to be memorised.

The exhibits are useful both for new Python learners and for experienced programmers whose expectations may have been shaped by other languages.

---

## What Does *Pythonic* Mean?

*Pythonic* describes code and approaches that work naturally with Python's language features, semantics, and established conventions. Pythonic code is not simply the shortest or cleverest solution; it aims to express intent clearly while making appropriate use of the way Python is designed to work.

Three essential references for every Python programmer are:

* [PEP 20 - The Zen of Python](https://peps.python.org/pep-0020/)
* [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [Python Language Reference](https://docs.python.org/3/reference/)

PEP 20 and PEP 8 are not a complete rulebook for Pythonic programming, but they provide important principles and conventions that underpin much of modern Python practice. The Python Language Reference provides the authoritative technical foundation for many of the behaviours explored in these exhibits.

---

## 🗺️ Exhibit Map

### 🧠 Mental Model

Build the foundations for reasoning about Python: names and objects, mutation and copying, iteration, and functions as first-class objects.

### 🌟 Pythonic Idioms

Explore expressive Python features and established idioms such as unpacking, comprehensions, context managers, `enumerate()`, and `zip()` - including when not to use them.

### ⚠️ Classic Pitfalls

Understand common sources of surprising behaviour, including mutable defaults, shallow copying, late-binding closures, shared class attributes, identity comparisons, and exhausted iterators.

### 🔀 Familiar but Different

Examine features that may look familiar from other languages but behave differently in Python, including truthiness, Boolean operators, division, slicing, scope, `None`, and strings.

### 🏷️ Type System

Explore Python's dynamic type system, type annotations, static checking, protocols, optional values, equality, and hashability.

### 🧱 Object Model

Look beneath Python's class syntax to understand instance and class attributes, method binding, properties, special methods, dataclasses, descriptors, and method resolution. Some of these concepts also appear in the [Object-Oriented](../object_oriented/) exhibits; here the focus is specifically on understanding Python's object model and its characteristic behaviours.

### 📦 Runtime and Imports

Explore module execution and caching, packages, imports, object lifetime, resource management, and other behaviours that become important as programs grow.

### ⚙️ Advanced Execution

Introduce generators, concurrency, threads, processes, the GIL, `async`/`await`, event loops, and the distinction between concurrency and parallelism.

---

## 🐾 Suggested Path

If these concepts are new to you, begin with **Mental Model**. Its foundational ideas help explain many of the behaviours encountered elsewhere in the collection.

From there, **Classic Pitfalls** shows what can happen when those behaviours are misunderstood, while **Pythonic Idioms** demonstrates how the same understanding can be used deliberately to write clearer, more natural Python.

The remaining sections can then be explored according to interest or as particular concepts arise in your own Python work.

---

## 🌱 Growing Exhibit

**Pythonic Thinking is under active development.**

The **Mental Model** collection is the first area being developed. The remaining sections describe planned exhibits and provide a roadmap for future additions.

Suggestions, corrections, and contributions from Python programmers of all experience levels are welcome.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _pythonic_thinking/README.md_ | _9 September 2026_ | _lizc-au_ |

---
