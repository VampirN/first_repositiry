import json

import pytest
from src.class_vacancy_storage import JSONVacancyStorage


@pytest.fixture
def vacancy_storage(tmp_path):
    file_path = tmp_path / "test_vacancies.json"
    return JSONVacancyStorage(file_path)


def test_add_vacancy(vacancy_storage):
    vacancy_data = {"title": "Software Engineer", "company": "Example Inc."}
    vacancy_storage.add_vacancy(vacancy_data)
    assert len(vacancy_storage.vacancies) == 1
    assert vacancy_storage.vacancies[0] == vacancy_data


def test_save_to_file(vacancy_storage):
    vacancy_data = {"title": "Data Scientist", "company": "Test Corp."}
    vacancy_storage.add_vacancy(vacancy_data)
    vacancy_storage._save_to_file()

    with open(vacancy_storage.file_path, "r") as file:
        saved_data = json.load(file)

    assert len(saved_data) == 1
    assert saved_data[0] == vacancy_data


@pytest.fixture
def vacancies(self):
    return [
        {'id': 1, 'title': 'Software Engineer', 'location': 'New York'},
        {'id': 2, 'title': 'Data Analyst', 'location': 'San Francisco'},
        {'id': 3, 'title': 'Product Manager', 'location': 'Seattle'}]


def test_get_vacancies(self, vacancies):
    criteria = {'location': 'New York'}
    expected_result = [{'id': 1, 'title': 'Software Engineer', 'location': 'New York'}]

    instance = JSONVacancyStorage(vacancies)
    result = instance.get_vacancies(criteria)

    assert result == expected_result


def test_delete_vacancy(self, vacancies):
    vacancy_id = 2
    expected_vacancies = [
        {'id': 1, 'title': 'Software Engineer', 'location': 'New York'},
        {'id': 3, 'title': 'Product Manager', 'location': 'Seattle'}
    ]

    instance = JSONVacancyStorage(vacancies)
    instance.delete_vacancy(vacancy_id)

    assert instance.vacancies == expected_vacancies





