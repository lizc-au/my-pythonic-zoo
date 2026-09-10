# 🖥️ Native GUI

Python's built-in `tkinter` module provides access to the Tk graphical user interface toolkit. These exhibits introduce native desktop GUI programming by building small applications that demonstrate one concept at a time.

GUI applications are **event-driven**. Instead of simply executing from top to bottom and finishing, they create an interface, enter an event loop, and respond to actions such as button clicks and user input.

---

## 🗺️ Exhibits

### [Basic Window Viewer](./basic_window_viewer.py)

Create a native window and display formatted text using Tkinter widgets and text tags.

On Windows, [`launch_basic_window_viewer.pyw`](./launch_basic_window_viewer.pyw) provides a GUI-only entry point that can run through `pythonw.exe` without displaying a console window.

### [Button & Event Handling](./button_event_handling.py)

Introduce event-driven interaction using buttons, callbacks, widget updates, and simple interface state changes.

The exhibit also demonstrates passing function objects to Tkinter and using a `lambda` expression as a callback adapter. See [Functions as Objects](../pythonic_thinking/mental_model/functions_as_objects_example.py) for the underlying Python mental model.

On Windows, [`launch_button_event_handling.pyw`](./launch_button_event_handling.pyw) provides the corresponding no-console entry point.

---

## 🌱 Where This Leads

Later exhibits can build on these foundations with user input, validation, layout management, richer `ttk` widgets, dialogs, and increasingly application-like desktop interfaces.

For a comprehensive reference to Tkinter's classes and API, see the [Python tkinter documentation](https://docs.python.org/3/library/tkinter.html).

[← Back to the Zoo Map](../README.md)

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _native_gui/README.md_ | _11 September 2026_ | _lizc-au_ |

---