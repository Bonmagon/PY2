class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, _name: str, _author: str, pages: int):
        super().__init__(_name, _author)
        self.pages = pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}"

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages < 0:
            raise ValueError("Количество страниц должно быть положительным числом")


class AudioBook(Book):
    def __init__(self, _name, _author, duration: float):
        super().__init__(_name, _author)
        self.duration = duration

    def __str__(self):
        return f"Электронная нига {self.name}. Автор {self.author}"

    @property
    def duration(self) -> int:
        return self.duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration < 0:
            raise ValueError("Продолжительность должна быть положительным числом")


