import json

from abc import ABC, abstractmethod


class VacancyStorage(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy_data):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass


class JSONVacancyStorage(VacancyStorage):
    """Класс, который реализовывает методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях,
    сохранение информации о вакансиях в JSON-файл"""
    def __init__(self, file_path):
        self.file_path = file_path

        self.vacancies = []

    def add_vacancy(self, vacancy_data):
        self.vacancies.append(vacancy_data)

        self._save_to_file()

    def get_vacancies(self, criteria):
        result = []
        for vacancy in self.vacancies:
            if all(key in vacancy and vacancy[key] == criteria[key] for key in criteria):
                result.append(vacancy)
                return result

    def delete_vacancy(self, vacancy_id):
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy.get('id') != vacancy_id]

        self._save_to_file()

    def _save_to_file(self):
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(self.vacancies, file, indent=4, ensure_ascii=False)
