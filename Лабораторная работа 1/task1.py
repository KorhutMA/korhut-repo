import doctest


class Book:
    def __init__(self, total_pages: int, current_page: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param total_pages: Общее количество страниц в книге
        :param current_page: Текущая страница, на которой остановился читатель

        Примеры:
        >>> book = Book(300, 0)  # инициализация экземпляра класса
        """
        if not isinstance(total_pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if total_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.total_pages = total_pages

        if not isinstance(current_page, int):
            raise TypeError("Текущая страница должна быть целым числом")
        if current_page < 0:
            raise ValueError("Текущая страница не может быть отрицательной")
        self.current_page = current_page

    def is_book_read(self) -> bool:
        """
        Проверка, прочитана ли книга полностью

        :return: Прочитана ли книга

        Примеры:
        >>> book = Book(300, 0)
        >>> book.is_book_read()
        False
        """
        return self.current_page == self.total_pages

    def read_pages(self, pages: int) -> None:
        """
        Чтение определенного количества страниц

        :param pages: Количество страниц для чтения
        :raise ValueError: Если количество страниц превышает оставшиеся страницы

        Примеры:
        >>> book = Book(300, 0)
        >>> book.read_pages(50)
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным")

        if self.current_page + pages > self.total_pages:
            raise ValueError("Количество страниц превышает общее число страниц в книге")

        self.current_page += pages

    def reset_book(self) -> None:
        """
        Сброс книги к началу

        Примеры:
        >>> book = Book(300, 100)
        >>> book.reset_book()
        >>> book.current_page
        0
        """
        self.current_page = 0


if __name__ == "main":
    doctest.testmod()


class Battery:
    def __init__(self, total_capacity: float, current_charge: float):
        """
        Создание и подготовка к работе объекта "Аккумулятор"

        :param total_capacity: Полная емкость аккумулятора
        :param current_charge: Текущий заряд аккумулятора

        Примеры:
        >>> battery = Battery(5000, 0)  # инициализация экземпляра класса
        """
        if not isinstance(total_capacity, (int, float)):
            raise TypeError("Емкость аккумулятора должна быть числом")
        if total_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительной")
        self.total_capacity = total_capacity

        if not isinstance(current_charge, (int, float)):
            raise TypeError("Текущий заряд должен быть числом")
        if current_charge < 0:
            raise ValueError("Текущий заряд не может быть отрицательным")
        self.current_charge = current_charge

    def is_battery_empty(self) -> bool:
        """
        Проверка, разряжен ли аккумулятор

        :return: Разряжен ли аккумулятор

        Примеры:
        >>> battery = Battery(5000, 0)
        >>> battery.is_battery_empty()
        True
        """
        return self.current_charge == 0

    def charge_battery(self, charge_amount: float) -> None:
        """
        Зарядка аккумулятора

        :param charge_amount: Количество заряда для пополнения
        :raise ValueError: Если заряд превышает оставшееся место

        Примеры:
        >>> battery = Battery(5000, 0)
        >>> battery.charge_battery(2000)
        """
        if not isinstance(charge_amount, (int, float)):
            raise TypeError("Количество заряда должно быть числом")
        if charge_amount < 0:
            raise ValueError("Количество заряда должно быть положительным")

        if self.current_charge + charge_amount > self.total_capacity:
            raise ValueError("Заряд превышает полную емкость аккумулятора")

        self.current_charge += charge_amount

    def use_battery(self, consumption: float) -> None:
        """
        Использование заряда аккумулятора

        :param consumption: Количество расходуемого заряда
        :raise ValueError: Если расход превышает текущий заряд

        Примеры:
        >>> battery = Battery(5000, 3000)
        >>> battery.use_battery(1000)
        """
        if not isinstance(consumption, (int, float)):
            raise TypeError("Количество расхода должно быть числом")
        if consumption < 0:
            raise ValueError("Количество расхода должно быть положительным")

        if consumption > self.current_charge:
            raise ValueError("Расход превышает текущий заряд")

        self.current_charge -= consumption


if __name__ == "main":
    doctest.testmod()


class Bucket:
    def __init__(self, total_volume: float, current_volume: float):
        """
        Создание и подготовка к работе объекта "Ведро"

        :param total_volume: Общий объем ведра
        :param current_volume: Текущий объем жидкости в ведре

        Примеры:
        >>> bucket = Bucket(10, 0)  # инициализация экземпляра класса
        """
        if not isinstance(total_volume, (int, float)):
            raise TypeError("Объем ведра должен быть числом")
        if total_volume <= 0:
            raise ValueError("Объем ведра должен быть положительным")
        self.total_volume = total_volume

        if not isinstance(current_volume, (int, float)):
            raise TypeError("Текущий объем должен быть числом")
        if current_volume < 0:
            raise ValueError("Текущий объем не может быть отрицательным")
        self.current_volume = current_volume

    def is_bucket_empty(self) -> bool:
        """
        Проверка, пустое ли ведро

        :return: Пустое ли ведро

        Примеры:
        >>> bucket = Bucket(10, 0)
        >>> bucket.is_bucket_empty()
        True
        """
        return self.current_volume == 0

    def fill_bucket(self, water_amount: float) -> None:
        """
        Наполнение ведра водой

        :param water_amount: Количество воды для наполнения
        :raise ValueError: Если количество воды превышает свободное место

        Примеры:
        >>> bucket = Bucket(10, 0)
        >>> bucket.fill_bucket(5)
        """
        if not isinstance(water_amount, (int, float)):
            raise TypeError("Количество воды должно быть числом")
        if water_amount < 0:
            raise ValueError("Количество воды должно быть положительным")

        if self.current_volume + water_amount > self.total_volume:
            raise ValueError("Количество воды превышает объем ведра")

        self.current_volume += water_amount

    def pour_out_water(self, water_amount: float) -> None:
        """
        Выливание воды из ведра

        :param water_amount: Количество воды для выливания
        :raise ValueError: Если количество воды превышает текущий объем

        Примеры:
        >>> bucket = Bucket(10, 8)
        >>> bucket.pour_out_water(5)
        """
        if not isinstance(water_amount, (int, float)):
            raise TypeError("Количество воды должно быть числом")
        if water_amount < 0:
            raise ValueError("Количество воды должно быть положительным")

        if water_amount > self.current_volume:
            raise ValueError("Количество воды превышает текущий объем ведра")

        self.current_volume -= water_amount


if __name__ == "main":
    doctest.testmod()