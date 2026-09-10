"""
iteration_example.py

Demonstrate Python's iterable and iterator model.

An iterable is an object that can provide an iterator. An iterator produces
values one at a time and remembers its current position. Once an iterator is
exhausted, it does not automatically restart.

Python's `for` loop uses this model internally: it obtains an iterator from an
iterable and repeatedly asks that iterator for the next value until no values
remain.

For normal iteration, a `for` loop is usually the Pythonic choice. Working with
`iter()` and `next()` directly can be useful when values need to be consumed
manually or incrementally, when coordinating multiple iterators, or when
implementing custom iteration behaviour. The underlying protocol is
demonstrated here primarily to explain how Python iteration works.

Other languages also support iterators, but Python's `for` statement is built
directly around its iteration protocol rather than being inherently a numeric
counter loop. This is particularly important for programmers familiar with
C-style `for` loops: Python normally iterates over values produced by an
iterable rather than managing an index explicitly.

Because the `for` statement works with a common iteration protocol, it does not
need to know the concrete type of object producing the values. The same loop
syntax can therefore operate over lists, strings, dictionaries, files,
generators, and user-defined iterables. Values can also be produced
incrementally rather than requiring an entire collection to exist in memory.

list ─────────┐
string ───────┤
file ─────────┤
dictionary ───┼──► iteration protocol ──► for loop
generator ────┤
your class ───┘

Real-world analogue:
A workflow queue can provide a sequence of pending items. Processing the queue
one item at a time is similar to advancing an iterator. Once all items in one
traversal have been consumed, that traversal is finished; processing the
collection again requires starting a new traversal over it.
"""


def demonstrate_iterable_and_iterator() -> None:
    """Demonstrate the relationship between an iterable and its iterator."""

    print("\n=== DEMONSTRATION 1: Iterable and iterator are different roles ===")

    animals = ["python", "panda", "lion", "elephant"]
    animal_iterator = iter(animals)

    print(f"\n    animals list: {animals}")
    print(f"\n    animals iterable type: {type(animals).__name__}")
    print(f"    animal_iterator type: {type(animal_iterator).__name__}")
    print(f"    iterable is iterator: {animals is animal_iterator}")

    # Introduce the built-in `next()`.
    # It asks the iterator for its next value and advances its position.
    print(f"\n    next(animal_iterator) first value: {next(animal_iterator)}")
    print(f"    next(animal_iterator) second value: {next(animal_iterator)}")

    # Show that the iterator remembers its position
    print(f"    next(animal_iterator) third value: {next(animal_iterator)}")
    print(f"    next(animal_iterator) fourth value: {next(animal_iterator)}")

    # Demonstrate exhaustion explicitly through the `StopIteration` exception.
    try:
        next(animal_iterator)
    except StopIteration:
        print("\n    another `next()` raises StopIteration: iterator exhausted")

    # Iterators are not generally resettable. Ask the iterable for a new
    # iterator when another traversal is required.
    fresh_iterator = iter(animals)

    print(f"\n    original animals list: {animals}")
    print(f"    first value from a fresh iterator: {next(fresh_iterator)}")


def demonstrate_for_loop() -> None:
    """Demonstrate how a `for` loop uses the iteration protocol."""

    print("\n=== DEMONSTRATION 2: Python `for` loops use the iteration protocol ===")

    print("\n    For normal iteration, prefer a `for` loop.")
    print("    It handles the iterator protocol for you.\n")

    animals = ["python", "panda", "lion", "elephant"]

    # The recommended Pythonic interface for normal iteration is the `for` loop.
    for animal in animals:
        print(f"    {animal}")


def main() -> None:
    """Run the iteration demonstrations."""
    demonstrate_iterable_and_iterator()
    demonstrate_for_loop()
    print()


if __name__ == "__main__":
    main()
