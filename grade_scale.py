from typing import List, Tuple
import csv
from typing import List

def get_grade(score: int, best_score: int) -> str:
    if score >= best_score - 10:
        return 'A'
    elif score >= best_score - 20:
        return 'B'
    elif score >= best_score - 30:
        return 'C'
    elif score >= best_score - 40:
        return 'D'
    else:
        return 'F'


def calculate_grades(scores: List[int]) -> Tuple[List[str], str]:
    best_score = max(scores)
    results = []
    total = 0

    for i, score in enumerate(scores, start=1):
        grade = get_grade(score, best_score)
        results.append(f"Student {i} score is {score} and grade is {grade}")
        total += score

    avg = total / len(scores)
    avg_grade = get_grade(int(avg), best_score)
    average_summary = f"The average score is {avg:.2f}, a grade of {avg_grade}"

    return results, average_summary


def save_grades_to_csv(scores: List[int], results: List[str], average_summary: str, filename: str = "data/grades.csv") -> None:
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student #", "Score", "Grade"])

        for i, line in enumerate(results, start=1):
            parts = line.split()
            writer.writerow([i, parts[3], parts[-1]])

        writer.writerow([])
        writer.writerow(["Average Summary:", average_summary])

class InputValidationError(Exception):
    """Raised when user input is invalid."""
    pass