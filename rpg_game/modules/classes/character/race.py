# Стандартные библиотеки

# Сторонние библиотеки

# Проектные библиотеки


class Race:
    """
    Notes:
        Класс описывает игровые расы;

    Attributes:
        * available_races - множество наименований игровых рас;
    
    Properties:
        * strength - расовый бонус силы;
        * dexterity - расовый бонус ловкости;
        * endurance - расовый бонус выносливости;
        * inteligence - расовый бонус интеллекта;
        * wisdom - расовый бонус мудрости;
        * charisma - расовый бонус харизмы;
    """
    
    # =========================
    # АТРИБУТЫ
    # =========================
    _available_races: set[str] = {
        "Человек",
        "Зенхаас",
        "Ксилаат",
        "Наара"
    }

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(self) -> None:
        
        # ОПИСАНИЕ РАСЫ
        self._name: str = "Базовый класс расы"
        
        # МОДИФИКАТОРЫ ХАРАКТЕРИСТИК РАСЫ
        self._strength: int = 0
        self._dexterity: int = 0
        self._endurance: int = 0
        self._inteligence: int = 0
        self._wisdom: int = 0
        self._charisma: int = 0

    # =========================
    # СВОЙСТВА
    # =========================
    @property
    def available_races(self) -> set[str]:
        """
        Notes:
            Метод возвращает множество наименований рас, доступных к использованию.

        Returns:
            set[str]: Множество наименований рас.
        """
        
        return self._available_races
    
    @property
    def strength(self) -> int:
        """
        Notes:
            Метод возвращает значение расового модификатора силы. 

        Returns:
            int: Значение расового модификатора силы.
        """
        
        return self._strength
    
    @property
    def dexterity(self) -> int:
        """
        Notes:
            Метод возвращает значение расового модификатора ловкости. 

        Returns:
            int: Значение расового модификатора ловкости.
        """
        
        return self._dexterity
    
    @property
    def endurance(self) -> int:
        """
        Notes:
            Метод возвращает значение расового модификатора выносливости. 

        Returns:
            int: Значение расового модификатора выносливости.
        """
        
        return self._endurance
    
    @property
    def inteligence(self) -> int:
        """
        Notes:
            Метод возвращает значение расового модификатора интеллекта. 

        Returns:
            int: Значение расового модификатора интеллекта.
        """
        
        return self._inteligence
    
    @property
    def wisdom(self) -> int:
        """
        Notes:
            Метод возвращает значение расового модификатора мудрости. 

        Returns:
            int: Значение расового модификатора мудрости.
        """
        
        return self._wisdom
    
    @property
    def charisma(self) -> int:
        """
        Notes:
            Метод возвращает значение расового модификатора харизмы. 

        Returns:
            int: Значение расового модификатора харизмы.
        """
        
        return self._charisma

    # =========================
    # МЕТОДЫ
    # =========================
    pass


class Human(Race):
    """
    Notes:
        Класс описывает расу "Человек";

    Attributes:
        * available_races - множество наименований игровых рас;
    
    Properties:
        * strength - расовый бонус силы;
        * dexterity - расовый бонус ловкости;
        * endurance - расовый бонус выносливости;
        * inteligence - расовый бонус интеллекта;
        * wisdom - расовый бонус мудрости;
        * charisma - расовый бонус харизмы;
    """
    
    # =========================
    # АТРИБУТЫ
    # =========================
    pass

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(self) -> None:
        
        # ОПИСАНИЕ РАСЫ
        super().__init__()
        self._name: str = "Человек"
        
        # МОДИФИКАТОРЫ ХАРАКТЕРИСТИК РАСЫ
        self._strength: int = 1
        self._dexterity: int = 1
        self._endurance: int = 1
        self._inteligence: int = 1
        self._wisdom: int = 1
        self._charisma: int = 1

    # =========================
    # СВОЙСТВА
    # =========================
    pass

    # =========================
    # МЕТОДЫ
    # =========================
    pass


class Zenhaas(Race):
    """
    Notes:
        Класс описывает расу "Зенхаас";

    Attributes:
        * available_races - множество наименований игровых рас;
    
    Properties:
        * strength - расовый бонус силы;
        * dexterity - расовый бонус ловкости;
        * endurance - расовый бонус выносливости;
        * inteligence - расовый бонус интеллекта;
        * wisdom - расовый бонус мудрости;
        * charisma - расовый бонус харизмы;
    """
    
    # =========================
    # АТРИБУТЫ
    # =========================
    pass

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(self) -> None:
        
        # ОПИСАНИЕ РАСЫ
        super().__init__()
        self._name: str = "Зенхаас"
        
        # МОДИФИКАТОРЫ ХАРАКТЕРИСТИК РАСЫ
        self._strength: int = 2
        self._endurance: int = 2
        self._wisdom: int = 2

    # =========================
    # СВОЙСТВА
    # =========================
    pass

    # =========================
    # МЕТОДЫ
    # =========================
    pass


class Ksilaat(Race):
    """
    Notes:
        Класс описывает расу "Ксилаат";

    Attributes:
        * available_races - множество наименований игровых рас;
    
    Properties:
        * strength - расовый бонус силы;
        * dexterity - расовый бонус ловкости;
        * endurance - расовый бонус выносливости;
        * inteligence - расовый бонус интеллекта;
        * wisdom - расовый бонус мудрости;
        * charisma - расовый бонус харизмы;
    """
    
    # =========================
    # АТРИБУТЫ
    # =========================
    pass

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(self) -> None:
        
        # ОПИСАНИЕ РАСЫ
        super().__init__()
        self._name: str = "Ксилаат"
        
        # МОДИФИКАТОРЫ ХАРАКТЕРИСТИК РАСЫ
        self._dexterity: int = 3
        self._inteligence: int = 2
        self._wisdom: int = 1

    # =========================
    # СВОЙСТВА
    # =========================
    pass

    # =========================
    # МЕТОДЫ
    # =========================
    pass


class Naara(Race):
    """
    Notes:
        Класс описывает расу "Наара";

    Attributes:
        * available_races - множество наименований игровых рас;
    
    Properties:
        * strength - расовый бонус силы;
        * dexterity - расовый бонус ловкости;
        * endurance - расовый бонус выносливости;
        * inteligence - расовый бонус интеллекта;
        * wisdom - расовый бонус мудрости;
        * charisma - расовый бонус харизмы;
    """
    
    # =========================
    # АТРИБУТЫ
    # =========================
    pass

    # =========================
    # ИНИЦИАЛИЗАЦИЯ
    # =========================
    def __init__(self) -> None:
        
        # ОПИСАНИЕ РАСЫ
        super().__init__()
        self._name: str = "Наара"
        
        # МОДИФИКАТОРЫ ХАРАКТЕРИСТИК РАСЫ
        self._strength: int = 4
        self._endurance: int = 2

    # =========================
    # СВОЙСТВА
    # =========================
    pass

    # =========================
    # МЕТОДЫ
    # =========================
    pass
