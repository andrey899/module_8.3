# Домашнее задание по теме "Создание исключений".

# Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи.
# Повторить тему ООП и принцип инкапсуляции.

# Задача "Некорректность".

# Класс исключений IncorrectVinNumber
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        # Обладает атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.
        self.message = message
        super().__init__(self.message)

# Класс исключений IncorrectCarNumbers
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        # Обладает атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.
        self.message = message
        super().__init__(self.message)

# Класс Car обладает следующими свойствами:
class Car:
    def __init__(self, model, vin, numbers):
        # Атрибут объекта model - название автомобиля (строка).
        self.model = model
        # Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
        self.__vin = vin
        # Атрибут __numbers - номера автомобиля (строка).
        self.__numbers = numbers
        # Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта
        # (в __init__ при объявлении атрибутов __vin и __numbers).
        if not self.__is_valid_vin(self.__vin):
            # Для выбрасывания исключений используйте оператор raise
            raise IncorrectVinNumber("Некорректный тип vin номер или неверный диапазон для vin номера")
        if not self.__is_valid_numbers(self.__numbers):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров или неверная длина номера")

    # Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
    # Уровень доступа private.
    def __is_valid_vin(self, vin_number):
        # Если некорректный, выбрасывает исключение.
        # Если экземпляр не целое число (тип данных проверить функцией isinstance).
        if not isinstance(vin_number, int):
            # Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
            # если передано не целое число.
            raise IncorrectVinNumber("Некорректный тип vin номер")
        # Если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
        if vin_number < 1000000 or vin_number > 9999999:
            # Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера'.
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        # Возвращает True, если исключения не были выброшены.
        return True

    # Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
    # Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    def __is_valid_numbers(self, numbers):
        # Если экземпляр не строка (тип данных можно проверить функцией isinstance).
        if not isinstance(numbers, str):
            # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
            # если передана не строка.
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        # Переданная строка должна состоять ровно из 6 символов.
        if len(numbers) != 6:
            # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
            raise IncorrectCarNumbers("Неверная длина номера")
        # Возвращает True, если исключения не были выброшены.
        return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')