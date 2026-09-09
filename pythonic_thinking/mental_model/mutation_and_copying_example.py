"""
mutation_and_copying_example.py

Demonstrate the difference between rebinding, mutation, and copying.

Rebinding changes which object a name refers to. Mutation changes an existing
mutable object. Copying creates another object, which may be independent or may
still share nested objects depending on the kind of copy performed.

Python's `copy.deepcopy()` function can create a deep copy by recursively
copying contained objects rather than leaving nested mutable objects shared.

A shallow copy is useful when a new outer container is needed but sharing its
contained objects is acceptable. A deep copy is useful when nested mutable
objects must also be changed independently of the original.

This exhibit builds on `names_and_objects_example.py`, where multiple names
were shown to refer to the same object.

Real-world analogue:
Two workflow labels may refer to the same document object. Editing that shared
document changes what both labels reveal, while assigning one label to a
different document changes only that label.

A document may itself contain nested mutable objects such as customer details,
approval details, or line items. A shallow copy can create a new document
container while some of those nested objects remain shared with the original.
A deep copy can instead create independent copies of the nested objects, which
is useful when the copied document must be changed without affecting the
original.

This exhibit comments individual assignments more heavily than normal Python
code because the mechanics of assignment are themselves the subject being
demonstrated.
"""

from copy import deepcopy


def demonstrate_rebinding() -> None:
    """Demonstrate rebinding a name to a different object."""

    print("\n=== DEMONSTRATION 1: Rebinding changes a name ===")

    animals = ["lion", "panda"]
    first_name = animals

    print("\n    Before rebinding:")
    print(f"        animals = {animals}")
    print(f"        first_name = {first_name} ")
    print(f"        animals is first_name: {animals is first_name}")

    # Rebind `first_name` to a new list object.
    first_name = ["elephant"]

    print("\n    After rebinding:")
    print(f"        animals = {animals}")
    print(f"        first_name = {first_name} ")
    print(f"        animals is first_name: {animals is first_name}")


def demonstrate_mutation() -> None:
    """Demonstrate mutation of an object shared by multiple names."""

    print("\n=== DEMONSTRATION 2: Mutation changes the object ===")

    animals = ["lion", "panda"]
    first_name = animals

    print("\n    Before mutation:")
    print(f"        animals = {animals}")
    print(f"        first_name = {first_name}")
    print(f"        animals is first_name: {animals is first_name}")

    # `list.append()` mutates the existing list rather than creating a new one.
    first_name.append("elephant")

    print("\n    After mutation:")
    print(f"        animals = {animals}")
    print(f"        first_name = {first_name}")
    print(f"        animals is first_name: {animals is first_name}")


def show_copy_state(
    animals: list[list[str]],
    shallow_copy: list[list[str]],
    deep_copy: list[list[str]],
) -> None:
    """Show value equality and object identity for copied nested lists."""
    print(f"        animals = {animals}")
    print(f"        shallow_copy = {shallow_copy}")
    print(f"        deep_copy = {deep_copy}")

    print()
    print(f"        animals[0] == shallow_copy[0] = {animals[0] == shallow_copy[0]}")
    print(f"        animals[0] is shallow_copy[0] = {animals[0] is shallow_copy[0]}")
    print("             note - shallow_copy shares this inner list object")

    print()
    print(f"        animals[0] == deep_copy[0] = {animals[0] == deep_copy[0]}")
    print(f"        animals[0] is deep_copy[0] = {animals[0] is deep_copy[0]}")
    print("             note - deep_copy has its own independent inner list object")


def demonstrate_copying() -> None:
    """Demonstrate the difference between shallow and deep copying."""

    print("\n=== DEMONSTRATION 3: Shallow and deep copying ===")
    animals = [["lion"], ["panda"]]  # deliberately nested object

    # A shallow copy creates a new outer list, but its nested lists are still
    # shared, i.e. the same objects referenced by the original outer list.
    shallow_copy = animals.copy()

    # A deep copy recursively creates new nested list objects as well.
    deep_copy = deepcopy(animals)

    print("\n    Before mutation:")
    show_copy_state(animals, shallow_copy, deep_copy)

    # Mutate the first inner list. The shallow copy refers to this same inner
    # list object, while the deep copy contains its own independent inner list.
    animals[0].append("python")

    print("\n    After mutation: (to the inner list only)")
    show_copy_state(animals, shallow_copy, deep_copy)

    print()


def main() -> None:
    """Run the rebinding, mutation, and copying demonstrations."""
    demonstrate_rebinding()
    demonstrate_mutation()
    demonstrate_copying()


if __name__ == "__main__":
    main()
