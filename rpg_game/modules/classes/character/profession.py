# Стандартные библиотеки

# Сторонние библиотеки

# Проектные библиотеки

class Profession:
    """
    Notes:
        pass
    
    Attributes:
        pass
    
    Methods:
        pass
    """
    
    # =========================
    # АТРИБУТЫ
    # =========================
    pass

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(self) -> None:
        
        # ОПИСАНИЕ
        self._name: str = "Родительский класс Профессии"
        self._dice: int = 0
        
        # ВЛАДЕНИЕ
        self._armors_posession: set[str] = {"LightArmor", "MediumArmor", "HeavyArmor", "Robe", "Shields"}
        self._weapons_posession: set[str] = {"OneHandSword", "TwoHandSword", "Dagger", "Bow", "CrossBow", "Staff"}
        self._tools_posession: set[str] = {"ArtistsTools", "BurglarsTools", "DiplomatsTools", "DungeonExplorersTools", "TravelersTools", "PriestsTools", "ScientistsTools"}
        
        # БАЗОВАЯ ЭКИПИРОВКА
        self._basic_armor_helmet = None
        self._basic_armor_chest = None
        self._basic_armor_legs = None
        self._basic_armor_boots = None
        self._basic_armor_gloves = None
        
        # БАЗОВОЕ ОРУЖИЕ
        self._basic_weapon_right_hand = None
        self._basic_weapon_left_hand = None

    # =========================
    # СВОЙСТВА
    # =========================
    @property
    def name(self) -> str:
        """
        Notes:
            Метод возвращает название профессии/класса.

        Returns:
            str: Название профессии/класса.
        """
        
        return self._name
    
    @property
    def dice(self) -> int:
        """
        Notes:
            Метод возвращает значение граней кубика, используемого при расчёте очков жизней.

        Returns:
            int: значение граней кубика для расчёта очков жизней.
        """
        
        return self._dice
    
    @property
    def armor_posession(self) -> set[str]:
        """
        Notes:
            Метод возвращает множество с типами брони, которыми владеет персонаж данной профессии/класса. 

        Returns:
            _type_: Множество с типами брони.
        """
        
        return self._armors_posession
    
    @property
    def weapon_posession(self) -> set[str]:
        """
        Notes:
            Метод возвращает множество с типами оружия, которыми владеет персонаж данной профессии/класса. 

        Returns:
            _type_: Множество с типами оружия.
        """
        
        return self._weapons_posession
    
    @property
    def tools_posession(self) -> set[str]:
        """
        Notes:
            Метод возвращает множество с типами инструментов, которыми владеет персонаж данной профессии/класса. 

        Returns:
            _type_: Множество с типами инструментами.
        """
        
        return self._tools_posession
    
    @property
    def basic_armor_helmet(self):
        """
        Notes:
            Метод возвращает екземпляр шлема базовой экипировки.

        Returns:
            _type_: Екземпляр шлема базовой экипировки.
        """
        
        return self._basic_armor_helmet
    
    @property
    def basic_armor_chest(self):
        """
        Notes:
            Метод возвращает екземпляр нагрудника/рубахи/туники базовой экипировки.

        Returns:
            _type_: Екземпляр нагрудника/рубахи/туники базовой экипировки.
        """
        
        return self._basic_armor_chest
    
    @property
    def basic_armor_legs(self):
        """
        Notes:
            Метод возвращает екземпляр набедренников/бриджей/штанов базовой экипировки.

        Returns:
            _type_: Екземпляр набедренников/бриджей/штанов базовой экипировки.
        """
        
        return self._basic_armor_legs
    
    @property
    def basic_armor_boots(self):
        """
        Notes:
            Метод возвращает екземпляр сапогов/ботинок/сандалий базовой экипировки.

        Returns:
            _type_: Екземпляр сапогов/ботинок/сандалий базовой экипировки.
        """
        
        return self._basic_armor_boots
    
    @property
    def basic_armor_gloves(self):
        """
        Notes:
            Метод возвращает екземпляр наручей/перчаток базовой экипировки.

        Returns:
            _type_: Екземпляр наручей/перчаток базовой экипировки.
        """
        
        return self._basic_armor_gloves
    
    @property
    def basic_weapon_right_hand(self):
        """
        Notes:
            Метод возвращает екземпляр оружия/щита базовой экипировки.

        Returns:
            _type_: Екземпляр оружия/щита базовой экипировки.
        """
        
        return self._basic_weapon_right_hand
    
    @property
    def basic_weapon_left_hand(self):
        """
        Notes:
            Метод возвращает екземпляр оружия/щита базовой экипировки.

        Returns:
            _type_: Екземпляр оружия/щита базовой экипировки.
        """
        
        return self._basic_weapon_left_hand

    # =========================
    # МЕТОДЫ
    # =========================
    pass


class Warrior(Profession):
    """
    Notes:
        pass
    
    Attributes:
        pass
    
    Methods:
        pass
    """
    
    # =========================
    # АТРИБУТЫ
    # =========================
    pass

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(self) -> None:
        
        # ОПИСАНИЕ
        super().__init__()
        self._name: str = "Воин"
        self._dice: int = 10
        
        # ВЛАДЕНИЕ
        self._armors_posession: set[str] = {"LightArmor", "MediumArmor", "HeavyArmor", "Shields"}
        self._weapons_posession: set[str] = {"OneHandSword", "TwoHandSword", "Dagger", "Bow", "CrossBow"}
        self._tools_posession: set[str] = {"",}

    # =========================
    # СВОЙСТВА
    # =========================
    pass

    # =========================
    # МЕТОДЫ
    # =========================
    pass