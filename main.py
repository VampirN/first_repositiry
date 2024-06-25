from src.api_hh import HeadHunterAPI
from src.class_vacancy_storage import JSONVacancyStorage
from src.utils import get_vacancies_with_keyword, get_top_salaries_vacancies
from src.class_vacancy import Vacancy


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    hh_api = HeadHunterAPI()
    v1 = JSONVacancyStorage("data/my_vacancies.json")
    hh_vacancies = hh_api.get_vacancies(search_query)
    for vacancy in hh_vacancies:
        v1.add_vacancy(vacancy)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancies = [
        Vacancy(
            name=vacancy["name"],
            url=vacancy["url"],
            salary=vacancy["salary"],
            description=vacancy["snippet"]["requirement"]
        ) for vacancy in hh_vacancies]
    top_vacancies = get_top_salaries_vacancies(vacancies, top_n)
    print(top_vacancies)
    keyword = input("Введите ключевые слова для фильтрации вакансий: ")
    filtered_vacancies = get_vacancies_with_keyword(vacancies, keyword)
    print(filtered_vacancies)


if __name__ == "__main__":
    user_interaction()

