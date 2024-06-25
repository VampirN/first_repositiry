import pytest
from src.class_vacancy import Vacancy


def test_vacancy_initialization():
    vacancy = Vacancy("Software Developer", "https://example.com", {"from": 50000}, "Job description")
    assert vacancy.name == "Software Developer"
    assert vacancy.url == "https://example.com"
    assert vacancy.salary == 50000
    assert vacancy.description == "Job description"


def test_default_salary():
    vacancy = Vacancy("Data Analyst", "https://example.com")

    assert vacancy.salary == 0


def test_no_salary():
    vacancy = Vacancy("Project Manager", "https://example.com")

    assert vacancy.salary == 0






