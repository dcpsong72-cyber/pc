#!/usr/bin/env python3
"""PixelForge — entry point.

Usage:
    python3 main.py                 # empty start
    python3 main.py image.psd       # open a file
    QT_QPA_PLATFORM=offscreen python3 main.py   # headless (screenshots)
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.qt_boot import create_app  # noqa: E402  (must set up libs before Qt)


def main() -> int:
    app = create_app(sys.argv)
    from pf.engine import Session
    from ui.main_window import MainWindow

    session = Session()
    win = MainWindow(session)
    win.show()

    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            win.load_path(os.path.abspath(arg))
            break

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
