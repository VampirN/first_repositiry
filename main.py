from src.api_hh import HeadHunterAPI
from src.utils import Vacancy
from src.class_vacancy_storage import JSONVacancyStorage
from src.utils import get_vacancies_with_keyword, get_top_salaries_vacancies
from src.class_vacancy_storage import VacancyStorage
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.to_dict(hh_vacancies)


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = get_vacancies_with_keyword(vacancies_list, filter_words)

    ranged_vacancies = get_top_salaries_vacancies(filtered_vacancies, salary_range)

    sorted_vacancies = get_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()

