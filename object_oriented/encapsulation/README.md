# Encapsulation & Invariants

Encapsulation is often introduced as "hiding data inside a class."

That description is incomplete, especially in Python.

A more useful design question is:

> How can an object own its state and rules so that normal client code uses a
> deliberate public interface rather than manipulating implementation details
> directly?

This exhibit focuses on **invariants**: conditions that should remain true for
every valid instance of an object.

For the zoo example, the invariant is simple:

> An animal's recorded weight must be greater than zero.

The rule is deliberately simple so that the examples can focus on
encapsulation rather than animal-specific behaviour.

---

## 1. Validation at construction is not enough

[`unprotected_state_example.py`](unprotected_state_example.py) defines an
`Animal` with a public `weight_kg` attribute.

The constructor rejects an invalid initial weight:

```python
Animal(
    name="Leo",
    species="Lion",
    weight_kg=-25.0,
)
```

raises `ValueError`.

That might initially look sufficient. The object cannot be created with an
invalid weight.

However, after valid construction, client code can simply do this:

```python
animal.weight_kg = -25.0
```

The object is now in a state that its own construction rule says is invalid.

The problem is not that public attributes are inherently wrong. Public
attributes are often entirely appropriate in Python.

The problem is that this particular attribute represents state governed by an
invariant, while callers can change that state without going through the rule
that owns it.

---

## 2. Protecting the public interface

[`protected_state_example.py`](protected_state_example.py) gives `Animal` a
more deliberate interface.

Normal client code reads the weight through:

```python
animal.weight_kg
```

and requests a change through:

```python
animal.record_weight(195.0)
```

`record_weight()` validates the requested value before changing the stored
state.

An invalid request:

```python
animal.record_weight(-25.0)
```

raises `ValueError`, leaving the existing valid weight unchanged.

The object therefore owns both:

- the state
- the rule governing valid changes to that state

That is the important encapsulation boundary in this example.

---

## A read-only property protects normal assignment

The protected example exposes `weight_kg` as a property with no setter.

Therefore this normal-looking attempt to bypass `record_weight()`:

```python
animal.weight_kg = -25.0
```

raises:

```text
AttributeError: property 'weight_kg' of 'Animal' object has no setter
```

This makes accidental misuse substantially harder.

It also communicates something useful through the public API:

- callers may inspect `weight_kg`
- callers should request changes through `record_weight()`

However, this still does not make the underlying state truly private.

---

## What does a single underscore mean?

Python code commonly uses a single leading underscore for implementation
details:

```python
_weight_kg
```

This is a **convention**.

It tells another developer:

> This belongs to the object's internal implementation. Do not depend on or
> manipulate it directly unless you have a very specific reason.

Python does not normally prevent this:

```python
animal._weight_kg = -25.0
```

If `_weight_kg` were the actual storage attribute, that assignment would still
be possible.

A single underscore is therefore valuable communication, but it is not access
control.

---

## What does a double underscore mean?

The protected example instead stores the value using:

```python
__weight_kg
```

A double leading underscore triggers Python's **name mangling**.

Inside an `Animal` class, Python transforms that attribute name to something
similar to:

```text
_Animal__weight_kg
```

This makes accidental external access harder. A caller cannot simply manipulate
`animal.__weight_kg` and reach the internal attribute used by the class.

But name mangling is **not true privacy**.

A caller who deliberately uses the mangled name can still do this:

```python
animal._Animal__weight_kg = -25.0
```

and bypass the validation performed by `record_weight()`.

That is important enough to state plainly:

> Python's double underscore does not create an impenetrable private field.

It makes accidental interference more difficult and helps communicate and
manage implementation details, but Python still allows a sufficiently
determined caller to reach the mangled attribute.

---

## See the deliberate bypass in the tests

The test suite deliberately demonstrates this misuse rather than merely
describing it.

See
[`test_protected_state_example.py`](../../tests/test_protected_state_example.py),
particularly
`test_name_mangled_storage_can_still_be_bypassed_deliberately()`.

That test assigns directly to:

```python
animal._Animal__weight_kg
```

and proves that the invalid value can still be reached through the public
property afterwards.

The test is intentionally breaking the object's contract. Application code
should not access the mangled attribute directly.

Keeping this behaviour in an executable test also prevents the teaching
material from implying stronger protection than Python actually provides.

---

## So what does encapsulation mean in Python?

For these examples, encapsulation is not:

> Make an attribute impossible for other code to reach.

Instead, it is:

> Give an object ownership of its state and rules, expose a deliberate public
> interface, and make normal client code use that interface.

Python relies heavily on conventions and cooperation between developers.

The language gives us useful mechanisms such as:

- properties
- methods
- underscore conventions
- name mangling
- dataclasses
- immutable objects where appropriate

But those mechanisms support the design. They are not the definition of
encapsulation themselves.

---

## Encapsulation is not always mutation

Several earlier Object-Oriented Python examples use:

```python
@dataclass(slots=True, frozen=True)
```

Those objects deliberately cannot have their fields reassigned normally after
construction.

That can be an excellent way to protect state when the domain concept should
be immutable.

This example is different because changing an animal's recorded weight is a
legitimate use case.

The design therefore permits mutation, but attempts to make that mutation
controlled:

```text
read current weight
        |
        v
   weight_kg property

request a change
        |
        v
 record_weight()
        |
        v
 validate invariant
        |
        v
 update internal state
```

The right choice depends on the domain:

- if state should not change, immutability may be appropriate
- if state must change, controlled operations can preserve its rules

Encapsulation is about controlling the object's valid behaviour, not blindly
making every object immutable or mutable.

---

## Why not use `__setattr__` to block everything?

Python provides lower-level mechanisms that could intercept attribute
assignment more aggressively.

For example, a class can customise `__setattr__`.

That would make this starter example more complicated without improving its
main lesson. It could also create the misleading impression that good
encapsulation requires defensive tricks to stop determined callers.

The goal here is a clear, Pythonic public interface rather than an
uncircumventable security boundary.

---

## Why only one animal?

Only one animal is used because animal type is not the design question here.

Repeating Python, Panda, Lion, and Elephant would add construction code without
helping to explain state ownership, invariants, properties, or name mangling.

Other exhibits explore meaningful differences between animal types.

---

## Beyond the zoo

The same design problem appears frequently in business applications.

An `Order` might require:

```text
quantity > 0
```

An `InsuranceClaim` might permit only certain status transitions:

```text
Submitted -> Assessed -> Approved
```

but not:

```text
Submitted -> Paid
```

A bank account might require a withdrawal operation to check available funds
rather than allowing arbitrary code to replace its balance.

In each case, the important question is not simply whether the data is visible.

The question is:

> Which object owns the rule, and can normal client code change the relevant
> state without going through that rule?

An object that owns a domain invariant should normally expose operations that
preserve it.

---

## Relationship to Responsibilities & Collaboration

[Responsibilities & Collaboration](../responsibilities/README.md) asks which
object should own a piece of work.

Encapsulation continues that idea inside an object:

> Once an object owns a rule, how should other code interact with the state
> governed by that rule?

Giving `Animal` responsibility for its valid recorded weight is only useful if
client code has a clear way to respect that responsibility.

The public interface establishes that boundary.

---

## Relationship to Domain Modelling

[Domain Modelling](../domain_modelling/README.md) asks which concepts and rules
matter enough to represent in software.

An invariant is one such rule.

If the application genuinely requires an animal's recorded weight to remain
positive, that rule belongs in the model somewhere. Encapsulation helps the
chosen owner preserve it.

This is another reason not to reproduce every real-world fact in a software
model: invariants should represent rules that matter to the application's
actual requirements.

---

## Choosing an encapsulation approach

When designing an object's state, ask:

- Does this value have rules that must remain true?
- Which object should own those rules?
- Should callers be allowed to replace the value directly?
- Would a method better express the meaning of a state change?
- Should the object be immutable instead?
- Does a property provide a useful read-only public view?
- Am I using `_name` as a convention or `__name` for name mangling?
- Am I accidentally describing either mechanism as true privacy?
- Is the public API making correct use easier than incorrect use?

The objective is not maximum restriction.

The objective is a clear object boundary that expresses and preserves the
requirements of the application during normal use.

---

## Related concepts

The [Object-Oriented Python Glossary](../GLOSSARY.md) explains terminology used
throughout this example, including: Attribute, Behaviour, Class, Contract,
Encapsulation, Invariant, Method, Object, Public API, Responsibility, and State.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _object_oriented/encapsulation/README.md_ | _4 September 2026_ | _lizc-au_ |
