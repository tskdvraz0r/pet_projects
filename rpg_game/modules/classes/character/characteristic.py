# Стандартные библиотеки
import sys

# Сторонние библиотеки

# Проектные библиотеки
sys.path.insert(0, "/Users/dmitrijkolganov/Yandex.Disk.localized/git/pet_projects/console_rpg/modules")
from modules.data_validation.check import Check
from modules.mechanics.dice import Dice
from modules.classes.character.race import Race


class Characteristic:
    """
    Notes:
        Класс описывает характеристики персонажа;
    
    Properties:
        * strength - расовый бонус силы;
        * dexterity - расовый бонус ловкости;
        * endurance - расовый бонус выносливости;
        * inteligence - расовый бонус интеллекта;
        * wisdom - расовый бонус мудрости;
        * charisma - расовый бонус харизмы;
    
    Methods:
        * gen_characteristic_value() - Метод генерирует значение характеристики по правилу: бросается 4d6, вычитается наименьшее, остальные суммируются;
    """
    
    # =========================
    # АТРИБУТЫ
    # =========================
    pass

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(
            self,
            class_race: Race
    ) -> None:
        Check.value_type(value=class_race, expected_type=Race)
        Check.value_is_available(value=class_race, available=Race.available_races)
        
        self._strength: int = (
            self.gen_characteristic_value()
            + class_race.strength
        )
        self._dexterity: int = (
            self.gen_characteristic_value()
            + class_race.dexterity
        )
        self._endurance: int = (
            self.gen_characteristic_value()
            + class_race.endurance
        )
        self._inteligence: int = (
            self.gen_characteristic_value()
            + class_race.inteligence
        )
        self._wisdom: int = (
            self.gen_characteristic_value()
            + class_race.wisdom
        )
        self._charisma: int = (
            self.gen_characteristic_value()
            + class_race.charisma
        )

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
    def gen_characteristic_value(self) -> int:
        """
        Notes:
            Метод генерирует значение характеристики по правилу: бросается 4d6, вычитается наименьшее, остальные суммируются;

        Returns:
            int: Значение характеристики;
        """
        roll_4_dices: list[int] = sorted([Dice(d=6).roll() for _ in range(4)])
        
        return sum(roll_4_dices[1:])