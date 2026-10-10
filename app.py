"""Entry point: python3 app.py [image|psd]
Theme is remembered in QSettings; default Pro Medium (their default)."""

import os
import sys

# Re-exec through the vendored Qt runtime libs (libxkbcommon et al.) if needed.
_LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runtime", "lib")
if os.path.isdir(_LIB) and _LIB not in os.environ.get("LD_LIBRARY_PATH", ""):
    os.environ["LD_LIBRARY_PATH"] = _LIB
    os.execv(sys.executable, [sys.executable] + sys.argv)

from PySide6.QtWidgets import QApplication

from pf.engine import Session
from ui.main_window import MainWindow
from ui.theme import apply_theme, current as T


def main():
    QApplication.setStyle("Fusion")
    app = QApplication(sys.argv)
    from PySide6.QtCore import QSettings
    theme = QSettings("PixelForge", "PixelForge").value("theme", "amoled")
    from ui.theme import set_theme, qss, THEMES
    t = set_theme(theme if theme in THEMES else "amoled")
    apply_theme(app, t)

    win = MainWindow(Session())
    for path in sys.argv[1:]:
        if os.path.exists(path):
            win.load_path(path)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
