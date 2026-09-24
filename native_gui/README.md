# Native GUI

Build small desktop applications with Python's built-in `tkinter` toolkit. Each exhibit focuses on one part of an event-driven interface: the program creates a window, enters an event loop, and responds to actions such as clicks and typing.

## Follow the Learning Path

| Step | Exhibit | Main idea |
| :--- | :--- | :--- |
| 1 | [Basic Window Viewer](./basic_window_viewer.py) | Create a window and display formatted text with widgets and tags. |
| 2 | [Button & Event Handling](./button_event_handling.py) | Use callbacks, button events, and widget updates to change interface state. |
| 3 | [User Input & Validation](./user_input_validation.py) | Read, normalise, validate, and clear an entry; submit by button or Enter key. |
| 4 | [Layout & Resizing](./layout_resizing.py) | Arrange widgets with `Frame` and `grid`, then let selected areas expand. |
| 5 | [Dialogs & Multi-step Interaction](./dialogs_multistep.py) | Use a modal Yes, No, or Cancel decision to control a workflow. |

Start from the repository root with `python native_gui/exhibit_launcher.py` to choose an exhibit. The launcher opens one exhibit in a separate Python process, hides while it is open, and returns when it closes.

## Bring the Pieces Together

The [Comprehensive Tkinter Showcase](./tkinter_showcase.py) combines navigation, responsive layout, validation, keyboard events, and dialogs in one application-style example. Its shorter comments and reusable view helpers make it a starting point for studying a more finished structure.

Run it from the repository root with `python native_gui/tkinter_showcase.py`.

<details>
<summary>Windows launchers without a console</summary>

Each `.pyw` file starts its corresponding GUI without a console window when launched through `pythonw.exe`.

| Application | Windows entry point |
| :--- | :--- |
| Exhibit menu | [`launch_exhibit_launcher.pyw`](./launch_exhibit_launcher.pyw) |
| Comprehensive showcase | [`launch_tkinter_showcase.pyw`](./launch_tkinter_showcase.pyw) |
| Basic window | [`launch_basic_window_viewer.pyw`](./launch_basic_window_viewer.pyw) |
| Button events | [`launch_button_event_handling.pyw`](./launch_button_event_handling.pyw) |
| User input | [`launch_user_input_validation.pyw`](./launch_user_input_validation.pyw) |
| Layout and resizing | [`launch_layout_resizing.pyw`](./launch_layout_resizing.pyw) |
| Dialogs | [`launch_dialogs_multistep.pyw`](./launch_dialogs_multistep.pyw) |

</details>

<details>
<summary>Concepts to notice as you work through the exhibits</summary>

| Exhibit | Detail to inspect |
| :--- | :--- |
| Button events | A function object is passed as a callback; a `lambda` adapts a callback when needed. See [Functions as Objects](../pythonic_thinking/mental_model/functions_as_objects_example.py). |
| User input | `.bind()` handles Enter, `.focus_set()` sets initial focus, and `strip()` with `casefold()` supports forgiving text comparison. |
| Layout | `rowconfigure()` and `columnconfigure()` set relative weights; `sticky="nsew"` stretches a widget in its grid cell. |
| Dialogs | A parented `askyesnocancel()` dialog returns `True`, `False`, or `None`. See the [Python messagebox documentation](https://docs.python.org/3/library/tkinter.messagebox.html). |

</details>

For the broader API, see the [Python tkinter documentation](https://docs.python.org/3/library/tkinter.html).

---

[Return to the Zoo map](../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
