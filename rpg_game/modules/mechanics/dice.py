# Стандартные библиотеки
import sys
import random as rd

# Сторонние библиотеки

# Проектные библиотеки
sys.path.insert(0, "/Users/dmitrijkolganov/Yandex.Disk.localized/git/pet_projects/console_rpg/modules")
from modules.data_validation.check import Check

class Dice:
    """
    Notes:
        Класс описывает игровой кубик и взаимодействие с ним;
    
    Attributes:
        * available_dices (set[int]): множество доступных кубиков;
    
    Methods:
        * roll() - Метод реализует симуляцию броска кубика посредством генерации псевдослучайного числа, находящегося в диапазоне граней кубика;
    """
    
    # =========================
    # АТРИБУТЫ
    # =========================
    _available_dices: set[int] = {2, 4, 6, 8, 10, 12, 20, 100, 1000}

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(self, d: int) -> None:
        Check.value_type(value=d, expected_type=int)
        Check.value_is_available(value=d, available=self.available_dices)
        
        self._d: int = d

    # =========================
    # СВОЙСТВА
    # =========================
    @property
    def available_dices(self) -> set[int]:
        """
        Notes:
            Метод возвращает множество доступных значений граней кубика. 

        Returns:
            set[int]: Множество доступных граней кубика.
        """
        return self._available_dices
    
    @property
    def d(self) -> int:
        """
        Notes:
            Метод возвращает значение количества граней кубика.

        Returns:
            int: _description_
        """
        return self._d

    # =========================
    # МЕТОДЫ
    # =========================
    def roll(self) -> int:
        """
        Notes:
            Метод реализует симуляцию броска кубика посредством генерации псевдослучайного числа, находящегося в диапазоне граней кубика;

        Returns:
            int: Результат броска кубика (псевдослучайное число);
        """
        
        if self._d in {2, 10}:
            return rd.randint(a=0, b=self._d - 1)
        
        elif self._d in {4, 6, 8, 12, 20}:
            return rd.randint(a=1, b=self._d)
        
        elif self._d in {100}:
            return rd.randrange(start=0, stop=100, step=10) + rd.randint(a=0, b=9)
        
        else:
            return rd.randrange(start=0, stop=1000, step=10) + rd.randrange(start=0, stop=100, step=10) + rd.randint(a=0, b=9)
        