# test/test_YamlDataReader.py
import pytest
import yaml
from src.Types import DataType
from src.YamlDataReader import YamlDataReader
from pathlib import Path


class TestYamlDataReader:

    @pytest.fixture
    def sample_yaml_content(self) -> str:
        return """
Иванов Иван Иванович:
  математика: 80
  программирование: 90
  литература: 76
Петров Петр Петрович:
  математика: 100
  социология: 90
  химия: 61
Андрей Андреев Андреевич:
  математика: 90
  физика: 90
  информатика: 90
  химия: 90
""".strip()

    @pytest.fixture
    def yaml_file(self, sample_yaml_content, tmp_path) -> str:
        file_path = tmp_path / "data.yaml"
        file_path.write_text(sample_yaml_content, encoding='utf-8')
        return str(file_path)

    @pytest.fixture
    def expected_data(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("социология", 90),
                ("химия", 61)
            ],
            "Андрей Андреев Андреевич": [
                ("математика", 90),
                ("физика", 90),
                ("информатика", 90),
                ("химия", 90),
            ]
        }

    def test_read_valid_yaml(self, yaml_file, expected_data):
        reader = YamlDataReader()
        result = reader.read(yaml_file)
        assert result == expected_data

    def test_read_empty_file(self, tmp_path):
        empty_file = tmp_path / "empty.yaml"
        empty_file.write_text("{}", encoding='utf-8')
        reader = YamlDataReader()
        assert reader.read(str(empty_file)) == {}

    def test_read_invalid_yaml(self, tmp_path):
        invalid_file = tmp_path / "invalid.yaml"
        invalid_file.write_text("not: yaml: [", encoding='utf-8')
        reader = YamlDataReader()
        with pytest.raises(yaml.YAMLError):
            reader.read(str(invalid_file))