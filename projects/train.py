class Users:
    type = 'Пользователи'
    def __init__(self, name, surname, age, address, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone_number = phone_number
    
    def print_info(self):
        print(self)
    
    def __str__(self):
        return f'Пользователь {self.name} {self.surname}. Возраст {self.age}. Проживает по адресу {self.address} . Контактный номер телефона {self.phone_number}'

objects_list = [] #Список всех обЪектов добавленных в класс Users. Нужен для поиска по индексу

def change(): #Функция для добавления объектов в класс Users и в список objects_list
    print('Введите имя')
    name = input()
    print('Введите фамилию')
    surname = input()
    while True:
        print('Введите возраст')
        age_input = input()
        try:
            age = int(age_input)
            break
        except ValueError:
            print('Возраст должен быть числом. Попробуйте еще раз')
    print('Введите адрес проживания')
    address = input()
    print('Введите номер телефона')
    phone_number = input()
    num = Users(name, surname, age, address, phone_number)
    global objects_list
    objects_list.append(num)

def demonstration(): #Функция для вывода информации из класса Users с помощью индекса из списка objects_list
    while True:
        print(f'Какой по номеру пользователь вам нужен? В данный момент их {len(objects_list)}')
        try:
            index_user = int(input())
            demonstr_info = objects_list[index_user - 1]
            return demonstr_info
            break
        except ValueError:
            print('Пожалуйста, вводите целое число')
        except IndexError:
            print('Пользователь с таким номером не найден')

print('Здравствуйте. Желаете добавить пользователя?')
while True: #Цикл добавляющий объекты в Users пока использующий того желает
    answer = input()
    if answer.lower() == 'да':
        change()
        print('Желаете добавить еще?')
    elif answer.lower() == 'нет':
        break
    else:
        print('Меня не учили обрабатывать подобные запросы. Пожалуйста, напишите "да" или "нет"')

print('Желаете увидеть информацию о пользователе?')
while True: #Цикл выводящий всю информацию о выбранных по номеру объектах класса Users пока использующий того желает
    answer = input()
    if answer.lower() == 'да':
        index = demonstration()
        index.print_info()
        print('Желаете увидеть информацию о ком-то еще?')
    elif answer.lower() == 'нет':
        print('Всего доброго!')
        break
    else:
        print('Меня не учили обрабатывать подобные запросы. Пожалуйста, введите "да" или "нет"')
