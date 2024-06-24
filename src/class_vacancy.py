class Vacancy:
    """Класс описание вакансии"""

    def __init__(self, title, link, salary=None, description=None):
        self.title = title
        self.link = link
        if salary is not None:
            self.salary = salary
        else:
            self.salary = 0  # Если зарплата не указана, устанавливаем значение 0
        self.description = description

    def __str__(self):
        return f"Vacancy: {self.title}\nLink: {self.link}\nSalary: {self.salary}\nDescription: {self.description}"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def validate_salary(self):
        """Валидация данных"""
        if self.salary is None:
            self.salary = "Зарплата не указана"

    def to_dict(self):
        """Возвращает вакансию в виде словаря"""
        return {
            'title': self.title,
            'link': self.link,
            'salary': self.salary,
            'description': self.description,
        }



