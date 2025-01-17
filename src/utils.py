import json


def get_top_salaries_vacancies(vacancies, top_n):
    """Сортировка по зарплате"""
    sorted_vacancies = sorted(vacancies, reverse=True)
    return sorted_vacancies[:top_n]


def get_vacancies_with_keyword(vacancies, keyword):
    """Сортировка по критерию (ключевому слову)"""
    return [vacancy for vacancy in vacancies if keyword.lower() in vacancy.description.lower()]


def save_vacancies_to_json(vacancies, filename):
    """Запись результатов сортировки в файл"""
    with open(filename, 'w') as file:
        json.dump(vacancies, file, indent=4)




