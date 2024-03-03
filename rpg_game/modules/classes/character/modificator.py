# Стандартные библиотеки
import sys
import math

# Сторонние библиотеки

# Проектные библиотеки
sys.path.insert(0, "/Users/dmitrijkolganov/Yandex.Disk.localized/git/pet_projects/rpg_game")
from modules.data_validation.check import Check

from modules.classes.character.characteristic import Characteristic

class Modificator:
    
    # =========================
    # АТРИБУТЫ
    # =========================
    pass

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(
            self,
            class_characteristic: Characteristic
    ) -> None:
        
        # ПРОВЕРКА КОРРЕКТНОСТИ ДАННЫХ
        Check.value_type(value=class_characteristic, expected_type=Characteristic)

        # МОДИФИКАТОРЫ
        self._strength: int = self.calc_modificator_value(characteristic = class_characteristic.strength)
        self._dexterity: int = self.calc_modificator_value(characteristic = class_characteristic.dexterity)
        self._endurance: int = self.calc_modificator_value(characteristic = class_characteristic.endurance)
        self._inteligence: int = self.calc_modificator_value(characteristic = class_characteristic.inteligence)
        self._wisdom: int = self.calc_modificator_value(characteristic = class_characteristic.wisdom)
        self._charisma: int = self.calc_modificator_value(characteristic = class_characteristic.charisma)

    # =========================
    # СВОЙСТВА
    # =========================
    @property
    def strength(self) -> int:
        """
        Notes:
            Метод возвращает значение характеристики силы.

        Returns:
            int: Значение характеристики силы.
        """
        
        return self._strength
    
    @property
    def dexterity(self) -> int:
        """
        Notes:
            Метод возвращает значение характеристики ловкости.

        Returns:
            int: Значение характеристики ловкости.
        """
        
        return self._dexterity
    
    @property
    def endurance(self) -> int:
        """
        Notes:
            Метод возвращает значение характеристики выносливости.

        Returns:
            int: Значение характеристики выносливости.
        """
        
        return self._endurance
    
    @property
    def inteligence(self) -> int:
        """
        Notes:
            Метод возвращает значение характеристики интеллекта.

        Returns:
            int: Значение характеристики интеллекта.
        """
        
        return self._inteligence
    
    @property
    def wisdom(self) -> int:
        """
        Notes:
            Метод возвращает значение характеристики мудрости.

        Returns:
            int: Значение характеристики мудрости.
        """
        
        return self._wisdom
    
    @property
    def charisma(self) -> int:
        """
        Notes:
            Метод возвращает значение характеристики харизмы.

        Returns:
            int: Значение характеристики харизмы.
        """
        
        return self._charisma

    # =========================
    # МЕТОДЫ
    # =========================
    def calc_modificator_value(
            self,
            characteristic: int
    ) -> int:
        """
        Notes:
            Метод рассчитывает значение модфикатора характеристики по формуле:
            math.floor((ХАРАКТЕРИСТИКА - 10) / 2).

        Args:
            characteristic (int): Характеристика, для которой требуется рассчитать значение модификатора.

        Returns:
            int: Значение модификатора.
        """
        
        return math.floor((characteristic - 10) / 2)
