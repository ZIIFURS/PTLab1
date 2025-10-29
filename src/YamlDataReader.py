# src/YamlDataReader.py
import yaml
from typing import Dict, List, Tuple
from DataReader import DataReader
from Types import DataType


class YamlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            raw_data = yaml.safe_load(file)

        students: DataType = {}
        for student_name, subjects in raw_data.items():
            student_scores: List[Tuple[str, int]] = []
            for subject, score in subjects.items():
                student_scores.append((subject.strip(), int(score)))
            students[student_name.strip()] = student_scores
        return students
