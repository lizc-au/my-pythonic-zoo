"""
launch_basic_window_viewer.pyw

Provide a Windows no-console entry point for the Basic Window Viewer.

The application itself lives in `basic_window_viewer.py`, where its logic can
be imported, tested, and reused normally. On Windows, the `.pyw` extension can
be associated with `pythonw.exe`, allowing this launcher to start the GUI
without opening or retaining a terminal console window.

Keeping this launcher deliberately small also means other entry points can
reuse `basic_window_viewer.main()` without duplicating application setup.
"""

from basic_window_viewer import main

if __name__ == "__main__":
    main()
