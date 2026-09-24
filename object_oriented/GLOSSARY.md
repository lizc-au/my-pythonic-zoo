# Object-Oriented Python Glossary

Practical definitions for terms used throughout the Object-Oriented Python exhibits. The examples use animals, but the same ideas apply to documents, orders, reports, storage, and other domains.

| Term | Meaning | Example or distinction |
| :--- | :--- | :--- |
| <a name="abstraction"></a>**Abstraction** | Exposes what other code needs while hiding unnecessary details. | Code can call `animal.speak()` without knowing how that animal implements it. |
| <a name="abstract-base-class-abc"></a>**Abstract Base Class (ABC)** | A common base that can require subclasses to implement methods. | Unlike a `Protocol`, an ABC normally establishes an explicit inheritance relationship and can share state or implementation. |
| <a name="attribute"></a>**Attribute** | Data or behaviour associated with an object or class. | An animal's `name` is an instance attribute; methods are attributes too. |
| <a name="behaviour"></a>**Behaviour** | Something an object can do. | A concrete animal provides `speak()`; a movement behaviour can instead be a separate collaborating object. |
| <a name="class"></a>**Class** | Defines a type of object and the data and behaviour its instances can provide. | `Lion` is a class; individual lions are objects created from it. |
| <a name="client-code"></a>**Client Code** | Code that uses another component through its public interface. | `factory_example.py` asks `AnimalFactory` for an animal without managing construction; "client" does not necessarily mean a person or browser. |
| <a name="cohesion"></a>**Cohesion** | How closely a component's responsibilities belong together. | A focused `Animal` has higher cohesion than one that also handles reports, storage, notifications, and scheduling. |
| <a name="collaboration"></a>**Collaboration** | Components working together while retaining their own responsibilities. | `KeeperReport` works with `FeedingGuide` and `CareSchedule`; collaboration alone does not guarantee good boundaries. |
| <a name="composition"></a>**Composition** | Building an object from other objects that supply parts of its functionality. | An animal *has a* movement behaviour instead of *being a* movement-based subclass. |
| <a name="concrete-class"></a>**Concrete Class** | A class that can be instantiated to create usable objects. | `Python`, `Panda`, `Lion`, and `Elephant` supply the `speak()` behaviour required by the `Animal` contract. |
| <a name="contract"></a>**Contract** | The operations and guarantees other code can rely on. | The `Animal` Protocol requires a compatible `speak()` method; contracts can also specify inputs, results, or exceptions. |
| <a name="coupling"></a>**Coupling** | How strongly one component depends on another's details. | Depending on the `Animal` contract instead of every concrete class reduces coupling; useful collaboration still requires dependencies. |
| <a name="delegation"></a>**Delegation** | Asking another component to perform work it owns. | `KeeperReport` delegates feeding guidance to `FeedingGuide`, then formats the returned information itself. |
| <a name="dependency"></a>**Dependency** | Something a component needs to perform its job. | A report may depend on a repository for data; dependencies can also be functions, configuration, services, or other objects. |
| <a name="dependency-injection"></a>**Dependency Injection** | Supplying a dependency from outside rather than constructing it inside the component. | `Animal(species="Python", movement=Slither())` receives its movement object; composition describes the parts, while injection describes how one part is supplied. |
| <a name="domain-modelling"></a>**Domain Modelling** | Representing the concepts, rules, relationships, and responsibilities that matter to an application. | Species may remain data on one `Animal` type until distinct rules or behaviour justify separate types. |
| <a name="encapsulation"></a>**Encapsulation** | Keeping related state and behaviour together behind a deliberate public interface. | Methods or properties can protect invariants; underscores and name mangling express boundaries in Python, not security guarantees. |
| <a name="factory"></a>**Factory** | A function, method, or object responsible for constructing other objects. | `AnimalFactory.create("lion")` chooses `Lion`; use direct construction when it is already the clearest choice. |
| <a name="inheritance"></a>**Inheritance** | Defining a class based on another class, usually to express genuine specialisation. | A subtype should honour the base contract; similar code alone does not justify an *is-a* relationship. |
| <a name="instance"></a>**Instance** | A particular object created from a class. | With `lion = Lion()`, `Lion` is the class and `lion` refers to an instance. |
| <a name="interface"></a>**Interface** | The operations through which other code interacts with a component. | Python interfaces can be expressed through public methods, functions, ABCs, or protocols; there is no required `interface` keyword. |
| <a name="invariant"></a>**Invariant** | A condition that must remain true throughout an object's valid lifetime. | An animal's weight must stay above zero even after updates, not only when the object is created. |
| <a name="liskov-substitution-principle-lsp"></a>**Liskov Substitution Principle (LSP)** | A subtype should work wherever its base type is expected without breaking the base contract. | Passing `isinstance()` is insufficient if client code needs special cases for a subtype's behaviour. |
| <a name="method"></a>**Method** | A function associated with a class. | An instance method such as `animal.speak()` receives its object as `self`; class and static methods relate to instances differently. |
| <a name="nominal-typing"></a>**Nominal Typing** | Compatibility based on an explicitly declared type relationship. | `class Lion(Animal): ...` declares inheritance, unlike structural typing based on supplied behaviour. |
| <a name="object"></a>**Object** | A runtime value with identity, state, behaviour, or a combination of these. | `lion = Lion()` binds a name to an object; classes themselves are also Python objects. |
| <a name="polymorphism"></a>**Polymorphism** | Using different kinds of objects through one interface or contract. | A client can call `animal.speak()` on different animals without branching by species; inheritance is not required. |
| <a name="protocol"></a>**Protocol** | A type contract describing required behaviour without requiring explicit inheritance. | A class with a compatible `speak()` method can satisfy an `Animal` Protocol through structural typing. |
| <a name="public-api"></a>**Public API** | The interface a component deliberately exposes for other code to use. | An API can belong to a Python module or package, not only a web service. |
| <a name="registry"></a>**Registry** | A mapping from identifiers to objects, classes, functions, or other selectable values. | A factory can map `"lion"` to `Lion` instead of growing a long conditional chain. |
| <a name="responsibility"></a>**Responsibility** | A job owned by a class, object, function, module, or other component. | `AnimalFactory` selects and constructs an animal; client code uses the returned object. |
| <a name="single-responsibility-principle-srp"></a>**Single Responsibility Principle (SRP)** | A component should have one coherent responsibility, often described as one reason to change. | Several methods may serve one job; report formatting and feeding rules change for different reasons and can have different owners. |
| <a name="state"></a>**State** | Data describing an object's condition at a given time. | An animal's name, age, or status may be state; not every difference needs its own class. |
| <a name="structural-typing"></a>**Structural Typing** | Compatibility based on provided structure or behaviour rather than declared ancestry. | A `Lion` with a compatible `speak()` can satisfy an `Animal` Protocol without inheriting from it. |

<details>
<summary>A closer look at related terms</summary>

| Terms | Distinction |
| :--- | :--- |
| Composition, collaboration, delegation | Composition assembles objects; collaboration describes their interaction; delegation hands a specific piece of work to another component. |
| Composition, dependency injection | Composition describes the parts of an object; dependency injection describes how a required part is supplied. |
| Nominal typing, structural typing | Nominal typing checks declared relationships; structural typing checks the required shape or behaviour. |
| SRP, cohesion | SRP asks whether a component owns one coherent job; cohesion describes how closely its responsibilities fit together. |

Structural typing formalises an idea related to Python's duck typing and lets static type checkers verify a contract. Separating responsibilities can improve cohesion, but adding classes before the requirements justify them can also make a design harder to understand.

</details>

---

[Return to the OO landing page](README.md)

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_