class Vacancy:

    """Класс описание вакансии"""

    def __init__(self, name: str, url: str, salary=None, description=None):
        self.name = name
        self.url = url
        if salary is not None:
            if salary["from"] is not None:
                self.salary = salary["from"]
            else:
                self.salary = 0  # Если зарплата не указана, устанавливаем значение 0
        else:
            self.salary = 0  # Если зарплата не указана, устанавливаем значение 0
        self.description = description

    def __repr__(self) -> str:
        return f"Vacancy: {self.name}\nUrl: {self.url}\nSalary: {self.salary}\nDescription: {self.description}"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def validate_salary(self):
        """Валидация данных"""
        if self.salary is None:
            self.salary = "Зарплата не указана"

    def to_dict(self) -> dict:
        """Возвращает вакансию в виде словаря"""
        return {
            'name': self.name,
            'url': self.url,
            'salary': self.salary,
            'description': self.description,
        }


