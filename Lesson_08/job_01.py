'''
Написать класс “animals” (животные), который включает общие признаки и поведения животных.
От “animals” наследовать класс “mammals” (млекопитающие), который включает общие признаки и поведения млекопитающих.
От “mammals” наследовать “human” (человек), “cat”(кот), “dog”(собака), у каждого свои признаки и поведения.
'''


class Animals:
    """Класс животные.


    animal_species -- вид животных(млекопиающие, земноводные и тд),
    origin -- происхождение,
    habitat -- место обитания.


    """

    def __init__(self, animal_species, origin, habitat) -> None:
        self.animal_species = animal_species
        self.origin = origin
        self.habitat = habitat


class Mammals(Animals):
    """Класс млекопитающие.

    animal_species -- вид животных(млекопиающие, земноводные и тд),
    origin -- происхождение,
    habitat -- место обитания,
    mammal_species -- вид (человек, волк, кит, дельфит и тд),
    gender -- пол,
    name -- имя,
    age -- возраст,
    height -- рост,
    weight -- вес.


    """

    def __init__(self, animal_species, origin, habitat, mammal_species,
                 gender, name, age, height, weight):
        super().__init__(animal_species, origin, habitat)
        self.mammal_species = mammal_species
        self.gender = gender
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Human(Mammals):
    """Класс человек.

    animal_species -- вид животных(млекопиающие, земноводные и тд),
    origin -- происхождение,
    habitat -- место обитания,
    mammal_species -- вид (человек, волк, кит, дельфит и тд),
    gender -- пол,
    name -- имя,
    age -- возраст,
    height -- рост,
    weight -- вес,
    profession -- профессия,
    marital_status -- семейное положение,
    hobby - хоби.


    """

    def __init__(self, animal_species, origin, habitat, mammal_species, gender, name,
                 age, height, weight, profession, marital_status, hobby):
        super().__init__(animal_species, origin, habitat, mammal_species,
                         gender, name, age, height, weight)
        self.profession = profession
        self.marital_status = marital_status
        self.hobby = hobby


class Cat(Mammals):
    """Класс коты.

    animal_species -- вид животных(млекопиающие, земноводные и тд),
    origin -- происхождение,
    habitat -- место обитания,
    mammal_species -- вид (человек, волк, кит, дельфит и тд),
    gender -- пол,
    name -- имя,
    age -- возраст,
    height -- рост,
    weight -- вес,
    breed -- порода,
    cat_view -- вид(домашние, дикие и тд.).


    """

    def __init__(self, animal_species, origin, habitat, gender, name,
                 age, height, weight, breed, cat_view):
        super().__init__(animal_species, origin, habitat, gender,
                         name, age, height, weight)
        self.breed = breed
        self.cat_view = cat_view

    def say(self):
        print('Mur-Mur')


class Dog(Mammals):
    """Класс собаки.

    animal_species -- вид животных(млекопиающие, земноводные и тд),
    origin -- происхождение,
    habitat -- место обитания,
    mammal_species -- вид (человек, волк, кит, дельфит и тд),
    gender -- пол,
    name -- имя,
    age -- возраст,
    height -- рост,
    weight -- вес,
    breed -- порода,
    dog_view -- вид(домашние, дикие и тд.).


    """

    def __init__(self, animal_species, origin, habitat, gender, name,
                 age, height, weight, breed, dog_view):
        super().__init__(animal_species, origin, habitat, gender,
                         name, age, height, weight)
        self.breed = breed
        self.dog_view = dog_view

    def say(self):
        print('gav-gav')
