# Стандартные библиотеки
import sys

# Сторонние библиотеки

# Проектные библиотеки
sys.path.insert(0, "/Users/dmitrijkolganov/Yandex.Disk.localized/git/pet_projects/rpg_game")
from modules.data_validation.check import Check

from modules.classes.character.race import Race
from modules.classes.character.profession import Profession
from modules.classes.character.characteristic import Characteristic
from modules.classes.character.modificator import Modificator

class Character:
    """
    Notes:
        Класс описывает (не)игрового персонажа и всё, что с ним связано.
    
    Attributes:
        pass
    
    Properties:
        * name - Имя (не)игрового персонажа;
        * surname - Фамилия (не)игрового персонажа;
        * fullname - Имя и Фамилия (не)игрового персонажа;
        * race - раса (не)игрового персонажа;
        * profession - профессия (игровой класс) (не)игрового персонажа;
        * characteristics - характеристики (не)игрового персонажа;
        * modificators - модификаторы (не)игрового персонажа;
    
    Methods:
        
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
            name: str,
            surname: str,
            class_race: Race,
            class_profession: Profession,
            # level: int = 1
    ) -> None:
        
        # ПРОВЕРКА КОРРЕКТНОСТИ ДАННЫХ
        for value, expected_type in zip(
                (name, surname, class_race, class_profession),
                (str, str, Race, Profession)
        ):
            Check.value_type(value=value, expected_type=expected_type)
        
        # БАЗОВАЯ ИНФОРМАЦИЯ
        self._name: str = name
        self._surname: str = surname
        self._fullname: str = f"{name} {surname}"
        
        self._race: Race = class_race
        self._profession: Profession = class_profession
        
        # self._level: Level = Level(level = level)
        
        # ХАРАКТЕРИСТИКИ
        self._characteristics: Characteristic = Characteristic(class_race=class_race)
        self._modificators: Modificator = Modificator(class_characteristic=self.characteristics)
            
    # =========================
    # СВОЙСТВА
    # =========================
    @property
    def name(self) -> str:
        """
        Notes:
            Метод возвращает имя (не)игрового персонажа.

        Returns:
            int: Имя (не)игрового персонажа.
        """
        
        return self._name
    
    @property
    def surname(self) -> str:
        """
        Notes:
            Метод возвращает фамилию (не)игрового персонажа.

        Returns:
            int: Фамилия (не)игрового персонажа.
        """
        
        return self._surname
    
    @property
    def fullname(self) -> str:
        """
        Notes:
            Метод возвращает имя и фамилию (не)игрового персонажа.

        Returns:
            int: Имя и фамилия (не)игрового персонажа.
        """
        
        return self._fullname
    
    @property
    def race(self) -> Race:
        """
        Notes:
            Метод возвращает расу (не)игрового персонажа.

        Returns:
            int: Раса (не)игрового персонажа.
        """
        
        return self._race
    
    @property
    def profession(self) -> Profession:
        """
        Notes:
            Метод возвращает профессию (игровой класс) (не)игрового персонажа.

        Returns:
            int: Профессия (игровой класс) (не)игрового персонажа.
        """
        
        return self._profession
    
    @property
    def characteristics(self) -> Characteristic:
        """
        Notes:
            Метод возвращает характеристики (не)игрового персонажа.

        Returns:
            int: Характеристики (не)игрового персонажа.
        """
        
        return self._characteristics
    
    @property
    def modificators(self) -> Modificator:
        """
        Notes:
            Метод возвращает модификаторы (не)игрового персонажа.

        Returns:
            int: Модификаторы (не)игрового персонажа.
        """
        
        return self._modificators

    # =========================
    # МЕТОДЫ
    # =========================
    pass