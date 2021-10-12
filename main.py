
# Program: Music Lyrics
# Author: Tom Alexa

import sys
from PyQt5.QtWidgets import QApplication
from src.gui.window import Window


def main():
    app = QApplication(sys.argv)
    win = Window()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
