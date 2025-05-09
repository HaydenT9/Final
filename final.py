from PyQt6.QtWidgets import *

from grade_scale import calculate_grades
from grade_scale import save_grades_to_csv
from grade_scale import InputValidationError


class StartScreen(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.stacked = stacked
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("🎓 Welcome to the Student Grading System")
        label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(label)

        start_btn = QPushButton("Start Grading")
        start_btn.clicked.connect(self.go_to_grading)
        layout.addWidget(start_btn)

    def go_to_grading(self):
        self.stacked.setCurrentIndex(1)

class GradeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grading System")
        self.setMinimumWidth(400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Student count
        self.student_label = QLabel("Enter number of students:")
        self.student_input = QLineEdit()
        self.layout.addWidget(self.student_label)
        self.layout.addWidget(self.student_input)

        # Score
        self.score_label = QLabel("Enter scores separated by spaces:")
        self.score_input = QLineEdit()
        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.score_input)

        # Submit
        self.submit_button = QPushButton("Calculate Grades")
        self.submit_button.clicked.connect(self.process_input)
        self.layout.addWidget(self.submit_button)

        # Output
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.layout.addWidget(self.output)

    def process_input(self):
        try:
            count = int(self.student_input.text())
            scores_str = self.score_input.text().split()
            if len(scores_str) != count:
                raise InputValidationError("Score count doesn't match number of students.")
            scores = list(map(int, scores_str))

            results, average_summary = calculate_grades(scores)
            self.output.setText("\n".join(results + [average_summary]))

            save_grades_to_csv(scores, results, average_summary)

        except ValueError:
            self.show_error("Scores and student count must be valid integers.")
        except InputValidationError as e:
            self.show_error(str(e))
        except Exception as e:
            self.show_error(f"Unexpected error: {str(e)}")


    def show_error(self, message: str):
        QMessageBox.critical(self, "Input Error", message)

class EndScreen(QWidget):
        def __init__(self, stacked):
            super().__init__()
            self.stacked = stacked
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)

            self.result_label = QTextEdit()
            self.result_label.setReadOnly(True)
            self.layout.addWidget(self.result_label)

            restart_btn = QPushButton("Restart")
            restart_btn.clicked.connect(self.restart)
            self.layout.addWidget(restart_btn)

            exit_btn = QPushButton("Exit")
            exit_btn.clicked.connect(self.close_app)
            self.layout.addWidget(exit_btn)

        def set_summary(self, text: str):
            self.result_label.setText("Grading Complete!" + text)

        def restart(self):
            self.stacked.setCurrentIndex(0)  # Back to StartScreen

        def close_app(self):
            self.close()
            self.stacked.close()