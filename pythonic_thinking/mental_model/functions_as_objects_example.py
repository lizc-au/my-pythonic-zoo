"""
functions_as_objects_example.py

Demonstrate that Python functions are objects.

Defining a function creates a function object and binds its name to that object.
Because functions are first-class objects, they can be assigned to other names,
stored in collections, passed to other functions, and returned from functions.

This is an important Python mental model because a function name does not
represent a special kind of command. Like other names, it refers to an object.
Calling the function with `()` is a separate operation that invokes that object.

Many languages support function-like values in some form, but Python makes
functions ordinary runtime objects that participate naturally in the same name
binding and object model explored elsewhere in Pythonic Thinking.

These capabilities provide the foundation for callbacks, decorators, strategy
selection, and other techniques explored in more specialised exhibits.

Real-world analogue:
A workflow can treat an approval rule as an object that can be selected, stored,
passed to another part of the application, or returned by a rule-selection
function. The workflow does not need to know which rule was chosen in advance;
it can receive the appropriate function and call it when an approval decision
is required.
"""

from collections.abc import Callable


def python_sound() -> str:
    """Return the sound made by a python."""
    return "Hiss!"


def lion_sound() -> str:
    """Return the sound made by a lion."""
    return "Roar!"


def panda_sound() -> str:
    """Return the sound made by a panda."""
    return "Bleat!"


def demonstrate_function_object() -> None:
    """Demonstrate the distinction between a function object and calling it."""

    print("\n=== DEMONSTRATION 1: A function is an object ===")

    print(f"\n    lion_sound function type: {type(lion_sound).__name__}")
    print(f"    lion_sound function object: {lion_sound}")
    print(f"    lion_sound() call result: {lion_sound()}")

    # Bind `same_function` to the function object
    # already bound to `lion_sound`.
    same_function = lion_sound

    print(f"\n    lion_sound is same_function: {lion_sound is same_function}")

    print(f"\n    same_function function type: {type(same_function).__name__}")
    print(f"    same_function function object: {same_function}")
    print(f"    same_function() call result: {same_function()}")

    print("\n    Note: both names display the same function object.")
    print("       The function object still identifies itself as `lion_sound`")
    print("       because `same_function` is only another name bound to that object.")

    print()


def demonstrate_stored_functions() -> None:
    """Demonstrate storing function objects in a collection."""

    print("\n=== DEMONSTRATION 2: Functions can be stored ===")

    sound_functions = [python_sound, panda_sound, lion_sound]

    print("\n    Stored functions:")
    for sound_function in sound_functions:
        print(f"    {sound_function}")

    print("\n    Calling each by iterating over the sound_functions list:")
    for sound_function in sound_functions:
        print(f"    {sound_function.__name__}(): {sound_function()}")

    print()


def announce_sound(sound_function: Callable[[], str]) -> None:
    """Call a supplied sound function and display its result."""
    print(f"    {sound_function.__name__}(): {sound_function()}")


def demonstrate_passed_function() -> None:
    """Demonstrate passing a function object to another function."""

    print("\n=== DEMONSTRATION 3: Functions can be passed to other functions ===")

    print("\n    Passing lion_sound function object to announce_sound:")
    announce_sound(lion_sound)


def choose_sound(animal: str) -> Callable[[], str]:
    """Return the sound function associated with an animal."""
    sound_functions = {
        "python": python_sound,
        "panda": panda_sound,
        "lion": lion_sound,
    }

    return sound_functions[animal]


def demonstrate_returned_function() -> None:
    """Demonstrate returning a function object from another function."""

    print("\n=== DEMONSTRATION 4: Functions can be returned from functions ===")

    selected_sound = choose_sound("panda")

    print(f"\n    selected function object: {selected_sound}")
    print(f"    selected_sound is panda_sound: {selected_sound is panda_sound}")
    print(f"    selected_sound(): {selected_sound()}")


def main() -> None:
    """Run the function-object demonstrations."""
    demonstrate_function_object()
    demonstrate_stored_functions()
    demonstrate_passed_function()
    demonstrate_returned_function()
    print()


if __name__ == "__main__":
    main()
