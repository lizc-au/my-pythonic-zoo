# Context Managers

A context manager handles the lifecycle around a block of work: entering, exiting, and responding to failures. Python's `with` statement calls that lifecycle at the appropriate points; the context manager does not have to perform the work inside the block.

## Try the Exhibit

Run `python pythonic_thinking/context_managers/context_manager_example.py` from the repository root. The script demonstrates six outcomes in sequence:

| Demonstration | What to observe |
| :--- | :--- |
| Successful context | `__enter__()` runs before the block and `__exit__()` runs afterward. |
| Work fails | `__exit__()` receives exception details, then the error continues outward unless suppressed. |
| Enter fails | The block never begins and this manager's `__exit__()` is not called. |
| Exit fails | Cleanup code can itself raise an exception. |
| Exception suppressed | Returning `True` from `__exit__()` deliberately prevents the managed exception from propagating. |
| `with ... as ...` | The name after `as` receives the value returned by `__enter__()`. |

Suppress errors deliberately; hiding unexpected failures can make bugs difficult to diagnose.

## Where the Pattern Helps

| Managed lifecycle | Example |
| :--- | :--- |
| Acquire and release | Files, database connections, network connections, and locks |
| Begin and finish | Database transactions and timers |
| Temporarily change and restore | Output redirection or application state |
| Create and clean up | Temporary files and directories |

A `with` block is useful when there is a meaningful enter and exit lifecycle. It is not a general wrapper that makes arbitrary work safe.

<details>
<summary>How the protocol works</summary>

A regular context manager implements Python's `__enter__()` and `__exit__()` methods. After a successful enter, Python calls `__exit__()` when the block ends, including when the block raises an exception.

| Method or result | Meaning |
| :--- | :--- |
| `__enter__()` | Prepare the context and optionally return a value for `as`. |
| `__exit__(exc_type, exc_value, traceback)` | Handle exit with information about any exception from the block. |
| `__exit__()` returns `True` | Suppress the exception from the managed block intentionally. |
| `__exit__()` does not return `True` | Let the exception continue after exit handling. |

If entering raises, the block does not run and that manager's exit method is not called. If exit handling raises, it can replace the error that would otherwise continue outward.

</details>

<details>
<summary>Related Python concepts</summary>

| Concept | Connection |
| :--- | :--- |
| [Names and Objects](../mental_model/names_and_objects_example.py) | `as` binds a name to the value returned by `__enter__()`. |
| Generators | `contextlib.contextmanager` uses a generator function and `yield`; that approach can follow a generators exhibit. |
| Asynchronous context managers | `async with` uses `__aenter__()` and `__aexit__()`, outside this introductory exhibit. |

</details>

---

[Return to Pythonic Thinking](../README.md) for other topics.

[Return to the Zoo map](../../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
