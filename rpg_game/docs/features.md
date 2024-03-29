# 1. Реализовать класс "Character", описывающий (не)игрового персонажа.
На базовом этапе, при создании экземпляра класс должен принимать следующие аргументы:
* name (str) - имя персонажа;
* surname (str) - фамилия персонажа;
* race (class Race) - экземпляр класса расы персонажа;
* profession (class Profession) - экземпляр класса профессии (игрового класса) персонажа;

Экземпляр данного класса должен именть следующие атрибуты:
* name (str) - имя персонажа;
* surname (str) - фамилия персонажа;
* fullname (str) - имя и фамилия персонажа;
* race (class Race) - экземпляр класса расы персонажа;
* profession (class Profession) - экземпляр класса профессии (игрового класса) персонажа;
* level (class Level) - экземпляр класса уровня персонажа;
* characteristics (class Characteristics) - экземпляр класса характеристик персонажа;
* skills (class Skills) - экземпляр класса навыков персонажа;

# 2. Реализовать родительский класс "Race", описывающий игровые расы;
Класс должен иметь следующие аргументы:
* available_races (set[str]) - множество доступных игровых рас;

При создании экземпляра класс принимает следующие аргументы:
* name (str) - название расы (рус.);

Экземпляр данного класса должен именть следующие атрибуты:
* name (str) - название расы на русском языке;
* strength (int) - расовый бонус к силе. По умолчанию 0;
* dexterity (int) - расовый бонус к ловкости. По умолчанию 0;
* endurance (int) - расовый бонус к выносливости. По умолчанию 0;
* intelligence (int) - расовый бонус к интеллекту (эта характеристика бесполезна для вас...). По умолчанию 0;
* wisdom (int) - расовый бонус к мудрости. По умолчанию 0;
* charisma (int) - расовый бонус к харизме. По умолчанию 0;

Экземпляр данного класса должен иметь следующие свойства:
* available_races (чтение) - возвращает множество доступных игровых рас;
* strength (чтение) - возвращает значение расового бонуса к силе;
* dexterity (чтение) - возвращает значение расового бонуса к ловкости;
* endurance (чтение) - возвращает значение расового бонуса к выносливости;
* intelligence (чтение) - возвращает значение расового бонуса к интеллекту;
* wisdom (чтение) - возвращает значение расового бонуса к мудрости;
* charisma (чтение) - возвращает значение расового бонуса к харизме;

# 3. Для родительского класса Race реализовать дочерние классы Human, Zenhaas, Ksilaat, Naara;
Все дочерние классы наслудеют атрибуты, свойства и методы от родительского класса Race.

## 3.1. class Human(Race);
Экземпляр данного класса должен иметь следующие атрибуты:
* name (str) - Человек;
* strength (int) - расовый бонус к силе = 1;
* dexterity (int) - расовый бонус к ловкости = 1;
* endurance (int) - расовый бонус к выносливости = 1;
* intelligence (int) - расовый бонус к интеллекту  = 1 (эта характеристика бесполезна для вас...);
* wisdom (int) - расовый бонус к мудрости = 1;
* charisma (int) - расовый бонус к харизме = 1;

## 3.2. class Zenhaas(Race);
Экземпляр данного класса должен иметь следующие атрибуты:
* name (str) - Зенхаас;
* strength (int) - расовый бонус к силе = 2;
* endurance (int) - расовый бонус к выносливости = 2;
* wisdom (int) - расовый бонус к мудрости = 2;

## 3.3. class Naara(Race);
Экземпляр данного класса должен иметь следующие атрибуты:
* name (str) - Наара;
* strength (int) - расовый бонус к силе = 4;
* endurance (int) - расовый бонус к выносливости = 2;

## 3.4. class Ksilaat(Race);
Экземпляр данного класса должен иметь следующие атрибуты:
* name (str) - Ксилаат;
* dexterity (int) - расовый бонус к ловкости = 3;
* intelligence (int) - расовый бонус к интеллекту  = 2 (эта характеристика бесполезна для вас...);
* wisdom (int) - расовый бонус к мудрости = 1;

# 4. Реализовать класс Check, описывающий проверки входных/выходных данных;
Класс должен иметь следующие методы:
* value_type() - метод принимает на вход значение и ожидаемый тип данных. Проводит проверку на соответствие переданного типа данных к ожидаемому;
* value_is_available() - метод принимает на вход значение и проверяет, доступно ли оно для использования;

# 5. Реализовать класс Dice, описывающий механику бросания игрового кубика;
Класс должен иметь следующие атрибуты:
* available_dices (set[int]) - доступные разновидности (количество граней) кубика.

При создании экземпляра класс должен принимать следующие атрибуты:
* d (int) - количество граней кубика

Экземпляр данного класса должен иметь следующие свойства:
* types_of_dices (чтение) - возвращает множество доступных типов (граней) игровых кубиков;
* d (чтение) - возвращает тип (количество граней) текущего кубика;

Экземпляр данного класса должен иметь следующие методы:
* roll() - метод реализует бросок кубика посредством генерации псевдослучайного числа в диапазоне граней кубика;

# 6. Реализовать класс Characteristic, описывающий характеристики персонажа;
При создании экземпляра класс должен принимать следующие атрибуты:
* class_race: Race - экземпляр класса расы персонажа;

Экземпляр данного класса должен иметь следующие аргументы:
* strength (int) - показатель силы персонажа;
* dexterity (int) - показатель ловкости персонажа;
* endurance (int) - показатель выносливости персонажа;
* intelligence (int) - показатель интеллекта персонажа (эта характеристика бесполезна для вас);
* wisdom (int) - показатель мудрости персонажа;
* charisma (int) - показатель харизмы персонажа;

Экземпляр данного класса должен иметь следующие свойства:
* strength (чтение) - возвращает показатель силы;
* dexterity (чтение) - возвращает показатель ловкости;
* endurance (чтение) - возвращает показатель выносливости;
* intelligence (чтение) - возвращает показатель интеллекта;
* wisdom (чтение) - возвращает показатель мудрости;
* charisma (чтение) - возвращает показатель харизмы;

Экземпляр данного класса должен иметь следующие методы:
* gen_chracteristic_value() - метод генерирует значение для характеристики по правилу: бросается 4d6, вычитается наименьшее, остальные суммируются.

Базовые значения характеристик рассчитываются следующим образом:
* gen_chracteristic_value() + расовый бонус характеристики

# 7. Реализовать родительский класс Profession, описывающий профессию (игровой класс) персонажа;
Экземпляр данного класса должен иметь следующие аргументы:
* name (str) - Наименование профессии (игрового класса) персонажа;
* dice (int) - кубик, отвечающий за количество очков здоровья;
* armors_posession (set[str]) - владение броней;
* weapons_posession (set[str]) - владение оружием;
* tools_posession (set[str]) - владение инструментами;
* basic_armor_helmet - базовая экипировка. Экземпляр класса Шлем;
* basic_armor_chest - базовая экипировка. Экземпляр класса Нагрудная Броня;
* basic_armor_legs - базовая экипировка. Экземпляр класса Броня Ног;
* basic_armor_boots - базовая экипировка. Экземпляр класса Сапоги;
* basic_armor_gloves - базовая экипировка. Экземпляр класса Перчатки;
* basic_weapon_right_hand - базовая экипировка. Экземпляр класса Оружие;
* basic_weapon_left_hand - базовая экипировка. Экземпляр класса Оружие;

Экземпляр данного класса должен иметь следующие свойства:
* name (чтение) - Наименование профессии (игрового класса) персонажа;
* dice (чтение) - кубик, отвечающий за количество очков здоровья;
* armors_posession (чтение) - владение броней;
* weapons_posession (чтение) - владение оружием;
* tools_posession (чтение) - владение инструментами;
* basic_armor_helmet (чтение) - базовая экипировка. Экземпляр класса Шлем;
* basic_armor_chest (чтение) - базовая экипировка. Экземпляр класса Нагрудная Броня;
* basic_armor_legs (чтение) - базовая экипировка. Экземпляр класса Броня Ног;
* basic_armor_boots (чтение) - базовая экипировка. Экземпляр класса Сапоги;
* basic_armor_gloves (чтение) - базовая экипировка. Экземпляр класса Перчатки;
* basic_weapon_right_hand (чтение) - базовая экипировка. Экземпляр класса Оружие;
* basic_weapon_left_hand (чтение) - базовая экипировка. Экземпляр класса Оружие;

# 8. Для родительского класса Profession реализовать дочерний класс Warrior;
Экземпляр данного класса должен иметь следующие аргументы:
* name (str) - Наименование профессии (игрового класса) персонажа;
* dice (int) - кубик, отвечающий за количество очков здоровья;
* armors_posession (set[str]) - владение броней;
* weapons_posession (set[str]) - владение оружием;
* tools_posession (set[str]) - владение инструментами;

# 9. Реализовать класс Modificator, описывающий модификаторы (не)игрового персонажа;
При создании экземпляра класс должен принимать следующие атрибуты:
* class_race: Race - экземпляр класса расы персонажа;

Экземпляр данного класса должен иметь следующие аргументы:
* strength (int) - модификатор силы персонажа;
* dexterity (int) - модификатор ловкости персонажа;
* endurance (int) - модификатор выносливости персонажа;
* intelligence (int) - модификатор интеллекта персонажа (эта характеристика бесполезна для вас);
* wisdom (int) - модификатор мудрости персонажа;
* charisma (int) - модификатор харизмы персонажа;

Экземпляр данного класса должен иметь следующие свойства:
* strength (чтение) - возвращает значение модификатора силы;
* dexterity (чтение) - возвращает значение модификатора ловкости;
* endurance (чтение) - возвращает значение модификатора выносливости;
* intelligence (чтение) - возвращает значение модификатора интеллекта;
* wisdom (чтение) - возвращает значение модификатора мудрости;
* charisma (чтение) - возвращает значение модификатора харизмы;

Экземпляр данного класса должен иметь следующие методы:
* calc_modificator_value() - метод рассчитывает значение модфикатора характеристики по формуле:
    math.floor((ХАРАКТЕРИСТИКА - 10) / 2).