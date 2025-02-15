class Automobile:
    """Базовый класс для всех автомобилей."""

    def __init__(self, brand: str, model: str, year: int) -> None:
        """Инициализация автомобиля.

        Args:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
        """
        self._brand = brand  # Атрибуты могут быть непубличными для инкапсуляции
        self._model = model
        self._year = year

    def __str__(self) -> str:
        """Строковое представление автомобиля."""
        return f"{self._brand} {self._model}, {self._year}"

    def __repr__(self) -> str:
        """Официальное строковое представление автомобиля."""
        return f"Automobile(brand={self._brand!r}, model={self._model!r}, year={self._year!r})"

    def start_engine(self) -> str:
        """Запустить двигатель автомобиля.

        Returns:
            str: Сообщение о запуске двигателя.
        """
        return "Двигатель запущен."


class PassengerCar(Automobile):
    """Класс легкового автомобиля, наследующий Automobile."""

    def __init__(self, brand: str, model: str, year: int, seats: int) -> None:
        """Инициализация легкового автомобиля, расширяя базовый класс.

        Args:
            brand (str): Марка легкового автомобиля.
            model (str): Модель легкового автомобиля.
            year (int): Год выпуска легкового автомобиля.
            seats (int): Количество мест в легковом автомобиле.
        """
        super().__init__(brand, model, year)
        self._seats = seats

    def __str__(self) -> str:
        """Строковое представление легкового автомобиля."""
        return super().__str__() + f", {self._seats} мест"

    def __repr__(self) -> str:
        """Официальное строковое представление легкового автомобиля."""
        return f"PassengerCar(brand={self._brand!r}, model={self._model!r}, year={self._year!r}, seats={self._seats!r})"

    def start_engine(self) -> str:
        """Запустить двигатель легкового автомобиля с дополнительным сообщением.

        Returns:
            str: Сообщение о запуске двигателя, уточняющее тип автомобиля.
        """
        return f"{super().start_engine()} Легковой автомобиль готов к поездке."


class CargoCar(Automobile):
    """Класс грузового автомобиля, наследующий Automobile."""

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """Инициализация грузового автомобиля, расширяя базовый класс.

        Args:
            brand (str): Марка грузового автомобиля.
            model (str): Модель грузового автомобиля.
            year (int): Год выпуска грузового автомобиля.
            capacity (float): Грузоподъемность в тоннах.
        """
        super().__init__(brand, model, year)
        self._capacity = capacity

    def __str__(self) -> str:
        """Строковое представление грузового автомобиля."""
        return super().__str__() + f", грузоподъемность {self._capacity} т"

    def __repr__(self) -> str:
        """Официальное строковое представление грузового автомобиля."""
        return f"CargoCar(brand={self._brand!r}, model={self._model!r}, year={self._year!r}, capacity={self._capacity!r})"

    def start_engine(self) -> str:
        """Запустить двигатель грузового автомобиля с дополнительным сообщением.

        Returns:
            str: Сообщение о запуске двигателя, уточняющее тип автомобиля.
        """
        return f"{super().start_engine()} Грузовой автомобиль загружен и готов к рейсу."


# Примеры использования

passenger_car = PassengerCar("Toyota", "Camry", 2020, 5)
cargo_car = CargoCar("Volvo", "FH", 2019, 18.5)

print(passenger_car)
print(cargo_car)

print(passenger_car.start_engine())
print(cargo_car.start_engine())