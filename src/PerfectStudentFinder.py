# src/PerfectStudentFinder.py
from Types import DataType


class PerfectStudentFinder:
    def __init__(self, data: DataType):
        self.data = data

    def find(self) -> str:
        for student, scores in self.data.items():
            if all(score == 90 for _, score in scores):
                return student
        return "Студентов с 90 баллами по всем предметам нет."
