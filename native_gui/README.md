# 🖥️ Native GUI

Python's built-in `tkinter` module provides access to the Tk graphical user interface toolkit. These exhibits introduce native desktop GUI programming by building small applications that demonstrate one concept at a time.

GUI applications are **event-driven**. Instead of simply executing from top to bottom and finishing, they create an interface, enter an event loop, and respond to actions such as button clicks and user input.

---

## 🗺️ Exhibits

### [Native GUI Exhibit Launcher](./exhibit_launcher.py)

Open the Native GUI category from a single Tkinter menu and launch each exhibit in its own Python process.

The launcher deliberately shows one exhibit at a time: it hides while the selected exhibit is open, then returns when that exhibit closes. Choosing another exhibit starts it fresh, and closing the launcher cleans up any active child exhibit.

On Windows, [`launch_exhibit_launcher.pyw`](./launch_exhibit_launcher.pyw) provides the corresponding no-console entry point.

### [Basic Window Viewer](./basic_window_viewer.py)

Create a native window and display formatted text using Tkinter widgets and text tags.

On Windows, [`launch_basic_window_viewer.pyw`](./launch_basic_window_viewer.pyw) provides a GUI-only entry point that can run through `pythonw.exe` without displaying a console window.

### [Button & Event Handling](./button_event_handling.py)

Introduce event-driven interaction using buttons, callbacks, widget updates, and simple interface state changes.

The exhibit also demonstrates passing function objects to Tkinter and using a `lambda` expression as a callback adapter. See [Functions as Objects](../pythonic_thinking/mental_model/functions_as_objects_example.py) for the underlying Python mental model.

On Windows, [`launch_button_event_handling.pyw`](./launch_button_event_handling.pyw) provides the corresponding no-console entry point.

### [User Input & Validation](./user_input_validation.py)

Collect text with a Tkinter `Entry`, normalise and validate user input, update interface feedback, and clear successful input ready for the next entry.

The exhibit also demonstrates binding the Enter key to an action with `.bind()`, setting initial keyboard focus with `.focus_set()`, and using `strip()` with `casefold()` for case-insensitive input comparison.

On Windows, [`launch_user_input_validation.pyw`](./launch_user_input_validation.pyw) provides the corresponding no-console entry point.

### [Layout & Resizing](./layout_resizing.py)

Organise widgets with Tkinter `Frame` containers and the `grid` geometry manager, then make selected rows and columns expand when the window is resized.

The exhibit demonstrates `rowconfigure()`, `columnconfigure()`, relative grid `weight` values, and `sticky="nsew"` for responsive widget stretching.

On Windows, [`launch_layout_resizing.pyw`](./launch_layout_resizing.pyw) provides the corresponding no-console entry point.

### [Dialogs & Multi-step Interaction](./dialogs_multistep.py)

Use Tkinter message boxes to pause a workflow, collect a user decision, and continue differently for Yes, No, or Cancel.

The exhibit demonstrates an explicitly parented modal dialog, a small wrapper around Tkinter's `askyesnocancel()` API, and three distinct return values: `True`, `False`, and `None`.

On Windows, [`launch_dialogs_multistep.pyw`](./launch_dialogs_multistep.pyw) provides the corresponding no-console entry point.

See the [Python `tkinter.messagebox` documentation](https://docs.python.org/3/library/tkinter.messagebox.html) for the standard message-box functions and return values.

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