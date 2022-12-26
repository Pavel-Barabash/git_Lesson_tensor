'''
Перегрузить операторы сравнения так, чтобы студенты сравнивались по количеству сданных ими дз. 
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
    mammal species -- вид (человек, волк, кит, дельфит и тд),
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
    mammal species -- вид (человек, волк, кит, дельфит и тд),
    gender -- пол,
    name -- имя,
    age -- возраст,
    height -- рост,
    weight -- вес,
    profession -- профессия,
    marital_status -- семейное положение,
    hobby - хоби.


    """

    def __init__(self, animal_species, origin, habitat, mammal_species,
                 gender, name, age, height, weight, profession, marital_status, hobby):
        super().__init__(animal_species, origin, habitat, mammal_species,
                         gender, name, age, height, weight)
        self.profession = profession
        self.marital_status = marital_status
        self.hobby = hobby


class Student(Human):
    """Класс человек.


    animal_species -- вид животных(млекопиающие, земноводные и тд),
    origin -- происхождение,
    habitat -- место обитания,
    mammal species -- вид (человек, волк, кит, дельфит и тд),
    gender -- пол,
    name -- имя,
    age -- возраст,
    height -- рост,
    weight -- вес,
    profession -- профессия,
    marital_status -- семейное положение,
    hobby - хоби,
    speciality -- специальность,
    num_course -- номер курса,
    count_executed_works -- кооличество сданных ДЗ.


    """

    def __init__(self, animal_species, origin, habitat, mammal_species, gender,
                 name, age, height, weight, profession, marital_status, hobby,
                 speciality, num_course, count_executed_works):
        super().__init__(animal_species, origin, habitat, mammal_species, gender,
                         name, age, height, weight, profession, marital_status, hobby)
        self.speciality = speciality
        self.num_course = num_course
        self.count_executed_works = count_executed_works

    # перезагружаем операторы сравнения по сданным ДЗ
    def __gt__(self, other):
        return int(self.count_executed_works) > int(other.count_executed_works)

    def __eq__(self, other):
        return int(self.count_executed_works) == int(other.count_executed_works)

    def __ne__(self, other):
        return int(self.count_executed_works) != int(other.count_executed_works)


Dasha = Student('Mammals', 'Eurasia', 'Northern part of Eurasia', 'Human', 'female',
                'Dasha', 19, 168, 60, 'student', 'unmarried', 'read boks', 'programmer', 2, 15)
Vova = Student('Mammals', 'Eurasia', 'Northern part of Eurasia', 'Human', 'male',
               'Vova', 21, 190, 85, 'student', 'unmarried', 'play football ', 'programmer', 2, 7)
Bob = Student('Mammals', 'Latin America', 'Northern part of Eurasia', 'Human', 'male',
              'Bob', 20, 175, 75, 'student', 'unmarried', 'car', 'programmer', 2, 13)

print(f'{Dasha.name} находится на курсе {Dasha.speciality}')
print('Сдала домашних заданий:', Dasha.count_executed_works)
print('')
print(f'{Vova.name} находится на курсе {Vova.speciality}')
print('Сдал домашних заданий:', Vova.count_executed_works)
print('')
print(f'{Bob.name} находится на курсе {Bob.speciality}')
print('Сдал домашних заданий:', Bob.count_executed_works)
print('')
print(f'Даша сдала больше заданий: {Dasha > Bob}')
print(f'Боб сдал меньше заданий: {Bob < Vova}')
