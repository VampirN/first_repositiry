import requests
from abc import ABC, abstractmethod


class GetVacancies(ABC):
    """Абстрактный класс для метода получения вакансий"""

    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HeadHunterAPI(GetVacancies):
    """Класс для подключения к сайту HH.ru"""

    def get_vacancies(self, search_query):
        url = f'http://api.hh.ru/vacancies?text={search_query}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return None




