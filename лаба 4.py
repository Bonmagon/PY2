if __name__ == "__main__":


class Auto:

    def __init__(self, color: str, model: str, weight: float, number_of_wheels: int):
        """
        Инициализируем объект "Авто"
        :param color: цвет авто
        :param model: модель авто
        :param weight: вес авто
        :param number_of_wheels: колечиство колес у авто
        Далее эти атрибуты наследуются
        """
        self.color = color
        self.model = model
        self.weight = weight
        self.number_of_wheels = number_of_wheels

    def change_color(self, new_color:str) -> None:
        """
        Перекраска авто в другой цвет
        :param new_color: новый цвет
        """
        self.color = new_color

    def category(self) -> str:
        """
        Возвращает категорию, к которой относится авто
        """
        return "Unknown"

    def __str__(self) -> str:
        """
        Магический метод __str__
        """
        return f'Auto "{self.model}"'

    def __repr__(self) -> str:
        """
        Магический метод __repr__
        """
        return f'Auto(color={self.color!r}, model={self.model!r}, weight={self.weight!r}, number_of_wheels={self.number_of_wheels!r})'


class Car(Auto):

    def __init__(self, color: str, model: str, weight: float, number_of_wheels: int, passengers: int):
        """
        Инициализируем объект "Лекговая машина"
        :param passengers: количество пассажиров, помещающихся в лекговую машину
        """
        super().__init__(color, model, weight, number_of_wheels)
        self.passengers = passengers

    def category(self) -> str:
        return "B"

    def __str__(self) -> str:
        return f'Car "{self.model}"'

    def __repr__(self) -> str:
        return f'Car (color={self.color!r}, model={self.model!r}, weight={self.weight!r}, number_of_wheels={self.number_of_wheels!r}), passengers={self.passengers!r}'


class Truck(Auto):

    def __init__(self, color: str, model: str, weight: float, number_of_wheels: int, cargo: str):
        """
        Инициализируем объект "Грузовик"
        :param cargo: тип перевозимого грузовиком груза
        """
        super().__init__(color, model, weight, number_of_wheels)
        self.cargo = cargo

    def category(self) -> str:
        return "C"

    def __str__(self) -> str:
        return f'Truck "{self.model}"'

    def __repr__(self) -> str:
        return f'Truck (color={self.color!r}, model={self.model!r}, weight={self.weight!r}, number_of_wheels={self.number_of_wheels!r}), cargo={self.cargo!r}'
