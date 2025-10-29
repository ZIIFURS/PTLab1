# test/test_PerfectStudentFinder.py
import pytest
from src.Types import DataType
from src.PerfectStudentFinder import PerfectStudentFinder


class TestPerfectStudentFinder:

    @pytest.fixture
    def data_with_perfect(self) -> DataType:
        return {
            "Иванов Иван Иванович": [("математика", 90), ("физика", 90)],
            "Петров Петр Петрович": [("химия", 85), ("биология", 90)]
        }

    @pytest.fixture
    def data_without_perfect(self) -> DataType:
        return {
            "Сидоров": [("математика", 89), ("физика", 90)],
            "Козлов": [("химия", 90), ("биология", 90), ("история", 91)]
        }

    @pytest.fixture
    def empty_data(self) -> DataType:
        return {}

    def test_find_perfect_student(self, data_with_perfect):
        finder = PerfectStudentFinder(data_with_perfect)
        assert finder.find() == "Иванов Иван Иванович"

    def test_no_perfect_student(self, data_without_perfect):
        finder = PerfectStudentFinder(data_without_perfect)
        assert finder.find() == "Студентов с 90 баллами по всем предметам нет."

    def test_empty_data(self, empty_data):
        finder = PerfectStudentFinder(empty_data)
        assert finder.find() == "Студентов с 90 баллами по всем предметам нет."
