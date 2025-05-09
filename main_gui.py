from PyQt6.QtWidgets import *
from final import StartScreen, GradeApp, EndScreen
import sys


def main():
    app = QApplication(sys.argv)

    stacked = QStackedWidget()

    start_screen = StartScreen(stacked)
    grade_app = GradeApp()
    end_screen = EndScreen(stacked)

    stacked.addWidget(start_screen)
    stacked.addWidget(grade_app)
    stacked.addWidget(end_screen)

    stacked.setCurrentWidget(start_screen)
    stacked.setFixedSize(500, 400)
    stacked.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
