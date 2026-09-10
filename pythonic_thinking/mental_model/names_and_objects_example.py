"""
names_and_objects_example.py

Demonstrate the relationship between Python names, objects, and types.

A name is bound to an object; it is not the object itself. The object has a
type, and multiple names can be bound to the same object.

The terminology used in this exhibit is:

* `=` is assignment: bind a name to an object.
* `==` is an equality comparison: do two objects have equal values?
* `is` is an identity comparison: are they the same object?

This distinction provides a foundation for understanding mutation, copying,
function arguments, and other behaviours explored in later exhibits.

Real-world analogue:
Several workflow labels can refer to the same document object without creating
copies of that document. A separate document can contain identical information
while still being a different object.

This exhibit comments individual assignments more heavily than normal Python
code because the mechanics of assignment are themselves the subject being
demonstrated.
"""


def main() -> None:
    """Show three names bound to the same list object."""

    # Create a list object and bind the name `animal` to that object.
    animal = ["lion"]

    # Bind `first_name` to the object currently bound to `animal`.
    # This does not create another list object.
    first_name = animal

    # Bind `second_name` to that same object.
    # There is still only one list object.
    second_name = animal

    # Create a separate list object containing the same value.
    other_animal = ["lion"]

    # Demonstrate that three different names are bound to the same list object.
    print("\n=== DEMONSTRATION 1: Three names, one list object ===")

    # Show the value accessed through each name.
    print(f"    animal = {animal}")
    print(f"    first_name = {first_name}")
    print(f"    second_name = {second_name}")

    # Show that the object accessed through each name has type `list`.
    print(f"\n    animal object type: {type(animal).__name__}")
    print(f"    first_name object type: {type(first_name).__name__}")
    print(f"    second_name object type: {type(second_name).__name__}")

    # `is` checks object identity: all three names refer to the same object.
    print(f"\n    animal is first_name:  {animal is first_name}")
    print(f"    animal is second_name: {animal is second_name}")
    print(f"    first_name is second_name: {first_name is second_name}")

    # Contrast value equality with object identity.
    print("\n=== DEMONSTRATION 2: Equality versus identity ===")

    # `==` compares values; `is` compares object identity.
    print(f"    animal == other_animal: {animal == other_animal}")
    print(f"    animal is other_animal: {animal is other_animal}")
    print(f"    first_name is other_animal: {first_name is other_animal}")
    print(f"    second_name is other_animal: {second_name is other_animal}\n")


if __name__ == "__main__":
    main()
