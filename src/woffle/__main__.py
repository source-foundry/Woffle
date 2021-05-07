# This file is part of Woffle.
#
#    Slice is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Slice is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Slice.  If not, see <https://www.gnu.org/licenses/>.

import sys

from PyQt5.QtCore import (
    QSequentialAnimationGroup,
    Qt,
    QPropertyAnimation,
    QPoint,
    QEasingCurve,
)

from PyQt5.QtGui import QFont, QFontDatabase, QPalette, QColor

from PyQt5.QtWidgets import (
    QMainWindow,
    QDesktopWidget,
    QApplication,
    QLabel,
    QVBoxLayout,
    QWidget,
    QStyleFactory,
)

from .fontresources import *

# from .imageresources import *

__VERSION__ = "0.10.0"


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # get the user screen dimensions for UI layout
        self.screen_dimensions = QDesktopWidget().screenGeometry(0)
        print(
            f"Screen dimensions: {self.screen_dimensions.width()}, "
            f"{self.screen_dimensions.height()}"
        )

        self.setWindowTitle("Woffle")

        self.main_layout = QVBoxLayout()

        luckiestguy_id = QFontDatabase.addApplicationFont(":/font/LuckiestGuy.ttf")
        font_family = QFontDatabase.applicationFontFamilies(luckiestguy_id)[0]
        luckiest_guy = QFont(font_family)
        self.titleLabel = QLabel("DROP!")
        self.titleLabel.setStyleSheet(
            "QLabel { font-size: 144px;"
            "height: 400px; width: 600px;"
            "color: white;"
            "border: 10px solid #cd0200;"
            "margin-top:15px;}"
        )
        self.titleLabel.setFont(luckiest_guy)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.titleLabel)

        self.child = QWidget(self)
        self.child.setContentsMargins(0, 0, 0, 0)
        self.child.setStyleSheet("background-color:#cd0200;border-radius:15px;")
        self.child.setFixedHeight(5)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setStartValue(QPoint(-600, 367))
        self.anim.setEndValue(QPoint(600, 367))
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.setDuration(2000)

        self.anim2 = QPropertyAnimation(self.child, b"pos")
        self.anim2.setStartValue(QPoint(600, 367))
        self.anim2.setEndValue(QPoint(-600, 367))
        self.anim2.setEasingCurve(QEasingCurve.OutCubic)
        self.anim2.setDuration(2000)

        self.animgroup = QSequentialAnimationGroup()
        self.animgroup.addAnimation(self.anim)
        self.animgroup.addAnimation(self.anim2)
        self.animgroup.setLoopCount(1000)
        self.animgroup.start()
        self.main_layout.addWidget(self.child)

        w = QWidget()
        w.setLayout(self.main_layout)
        self.setCentralWidget(w)

        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready")

        # Version info
        status_version_label = QLabel(f"v{__VERSION__}")
        self.statusbar.addPermanentWidget(status_version_label)
        self.statusbar.update()

        self.setGeometry(0, 0, 600, 400)
        rect = self.frameGeometry()
        centerCoord = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(centerCoord)
        self.move(rect.topLeft())


def main():
    app = QApplication(sys.argv)
    # fusion_style = QStyleFactory.create("Fusion")
    # app.setStyle(fusion_style)
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(24, 24, 24))
    app.setPalette(palette)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
