
import doctest


class Car:
    def __init__(self, engine_state: str, fuel_volume: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param engine_state: Состояние двигателя()
        :param fuel_volume: Объем оставшегося топлива
        Примеры:
        >>> car = Car('turn on', 100)  # инициализация экземпляра класса
        """
        if not isinstance(engine_state, str):
            raise TypeError("Состояние описывается строкой")
        if engine_state != 'turn on' or 'turn off' or 'broken':
            raise ValueError("Двигатель может быть только включен(turn on), выключен(turn off) или сломан(broken)")
        self.engine_state = engine_state

        if not isinstance(fuel_volume, (int, float)):
            raise TypeError("Количество топлива должно быть int или float")
        if fuel_volume < 0:
            raise ValueError("Количество топлива не может быть отрицательным числом")
        self.fuel_volume = fuel_volume

    def is_empty_car(self) -> bool:
        """
        Функция которая проверяет есть ли топливо в машине
        :return: Есть ли топливо в машине
        Примеры:
        >>> car = Car('turn on', 100)
        >>> car.is_empty_car()
        """
        ...

    def add_fuel_to_car(self, fuel: float) -> None:
        """
        Заправка машины.
        :param fuel: Объем добавляемой жидкости
        :raise ValueError: добавляемое топливо - это положительное число
        Примеры:
        >>> car = Car('turn on', 100)
        >>> car.add_water_to_glass(200)
        """
        if not isinstance(fuel, (int, float)):
            raise TypeError("Добавляемое топливо должно быть типа int или float")
        if fuel < 0:
            raise ValueError("Добавляемое топливо должна положительным числом")
        ...

    def repair_engine(self) -> None:
        """
        Починка двигателя.
        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: нельзя починить работающую машину
        Примеры:
        >>> car = Car('broken', 100)
        >>> car.repair_engine()
        """
        if self.engine_state != "broken":
            raise ValueError('Двигатель не сломан');
        ...


class Tree:

    def __init__(self, height: float, sort: str, number_of_fruits: int):
        """
        Описываю Дерево
        :param height: высота дерева
        :param sort: тип дерева
        :param number_of_fruits: количество фруктов на дереве
        >>> tree1.Tree(300, "apple", 40)
        """
        if not isinstance(sort, str):
            raise TypeError("Сорт дерева описывается строкой")
        self.sort = sort
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть int или float")
        if height < 0:
            raise ValueError("Высота не может быть отрицательным числом")
        self.height = height
        if not isinstance(number_of_fruits, int):
            raise TypeError("Количество фруктов должно быть int")
        if number_of_fruits < 0:
            raise ValueError("Количество фруктов не может быть отрицательным числом")
        self.number_of_fruits = number_of_fruits

    def collect_fruits(self, n: int) -> None:
        """
        Собрать фрукты с дерева
        :param n: количество собираемых фруктов
        :return:Ничего
        >>>tree1.Tree(300, "apple", 40)
        >>>tree1.collect_fruits(10)
        """
        if n > self.number_of_fruits:
            raise ValueError("Нельзя собрать больше, чем имеешь")

    def grow_up(self, m: float) -> int:
        """
        Рост дерева
        :param m: на сколько сантиметров дерево выросло
        :return: высота дерева после роста
        >>>tree1.Tree(300, "apple", 40)
        >>>tree1.grow_up(100)
        """
        if not isinstance(m, (float, int)):
            raise TypeError("На сколько дерево растет должно быть числом")
        if m < 0:
            raise ValueError("Вырасти в отрицательную сторону нельзя")

    def how_many_fruits(self) -> int:
        """
        Проверить сколько на дереве фруктов
        :return: количество фруктов на дереве
         >>>tree1.Tree(300, "apple", 40)
         >>>tree1.how_many_fruits
        """


class Washer:
    def __init__(self, speed: float, load: float, color: str):
        """
        Описываю Стиральную машину
        :param speed: количество оборотов в стиральной машине
        :param load: загрузка стиральной машины (сколько килограммов внутри)
        :param color: цвет стиральной машины
        >>>washer_machine1.Washer(3000, 3, "white")
        """
        if not isinstance(speed, (float, int)):
            raise TypeError('Количество оборотов должно быть float, int')
        if speed < 0:
            raise ValueError('Количество оборотов не может быть отрицательным')
        self.speed = speed
        if not isinstance(load, (float, int)):
            raise TypeError('Загрузка вещами должна быть float, int')
        if load < 0:
            raise ValueError('Загрузка вещами не может быть отрицательной')
        self.load = load
        if not isinstance(color, str):
            raise TypeError('Цвет должн быть str')
        self.color = color

    def load_clothes(self, n: float) -> float:
        """
        Загрузка машины вещами
        :param n: сколько килограммов еще догружаем в машину
        :return: сколько теперь в машине(после догрузки)
        >>>washer_machine1.Washer(3000, 3, "white")
        >>>washer_machine1.load_clothes(1.2)
        """
        if not isinstance(n, (float, int)):
            raise TypeError('Загрузка вещами должна быть float, int')
        if n < 0:
            raise ValueError('Загрузка вещами не может быть отрицательной')

    def unload_clothes(self, n: float) -> float:
        """
        Разгрузка вещей из машины
        :param n: сколько килограммов выгружаем
        :return: сколько в машине осталось
        >>>washer_machine1.Washer(3000, 3, "white")
        >>>washer_machine1.unload_clothes(2.6)
        """
        if not isinstance(n, (float, int)):
            raise TypeError('Разгрузка вещей должна быть float, int')
        if n < 0:
            raise ValueError('Разгрузка вещей не может быть отрицательной')
        if n > self.load:
            raise ValueError('Нельзя выгрузить больше, чем сейчас есть')

    def set_speed(self, n) -> None:
        """
        Устанавливаем количество оборотов в минуту
        :param n: количество оборотов
        :return: Ничего
        >>>washer_machine1.Washer(3000, 3, "white")
        >>>washer_machine1.set_speed(4000)
        """
        if not isinstance(n, (float, int)):
            raise TypeError('Количество оборотов должно быть float, int')
        if n < 0:
            raise ValueError('Количество оборотов не может быть отрицательным')


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
