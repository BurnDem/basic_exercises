# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

all_names = []
for name in students:
    student_names = name['first_name']
    all_names.append(student_names)

stud_count = Counter(all_names)
for stud_name in stud_count:
    print(f'{stud_name}: {stud_count[stud_name]}')

# Я чую , что тут есть решение получше, но не вижу его, крутил по-разному, но так ни к чему и не пришел

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
all_names = []
for name in students:
    student_names = name['first_name']
    all_names.append(student_names)

stud_count = Counter(all_names)
for stud_name, count in stud_count.most_common(1):
    print(f'Самое частое имя среди учеников: {stud_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for num, one_class in enumerate(school_students, 1):
    names = dict()
    for stud_name in one_class:
        names[stud_name['first_name']] = names.setdefault(stud_name['first_name'], 0) + 1
    common_name = max(names, key=names.get)
    print(f'Самое частое имя в классе {num}: {common_name}')
    

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def count_boys_and_girls(all_students):
    girls = 0
    boys = 0
    all_names = []
    for name in all_students:
        student_names = name['first_name']
        all_names.append(student_names)
    for stud_name in all_names:
        for key, value in is_male.items():
            if key == stud_name:
                if value == False:
                    girls += 1
                elif value == True:
                    boys += 1
    return f'девочки {girls}, мальчики {boys}'
    
for one_class in school:
    all_genders = count_boys_and_girls(one_class['students'])
    print(f'Класс {one_class["class"]}: {all_genders}')
# понимаю, что можно упростить, но не вижу как


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

def count_boys_and_girls(all_students):
    girls = 0
    boys = 0
    all_names = []
    for name in all_students:
        student_names = name['first_name']
        all_names.append(student_names)
    for stud_name in all_names:
        for key, value in is_male.items():
            if key == stud_name:
                if value == False:
                    girls += 1
                elif value == True:
                    boys += 1
    return girls, boys


all_classes = dict()
for one_class in school:
    all_classes[one_class['class']] = count_boys_and_girls(one_class['students'])

def comp_classes(first_class, second_class):
    key_list = list(all_classes.keys())
    val_list = list(all_classes.values())
    first_class_name = val_list.index(first_class)
    second_class_name = val_list.index(second_class)
    if first_class[0] > second_class[0] and first_class[1] < second_class[1]:
        return (f'Больше всего девочек в классе {key_list[first_class_name]}\nБольше всего мальчиков в классе {key_list[second_class_name]}')
    elif first_class[0] > second_class[0] and first_class[1] > second_class[1]:
        return (f'Больше всего девочек в классе {key_list[first_class_name]}\nБольше всего мальчиков в классе {key_list[first_class_name]}')
    elif first_class[0] < second_class[0] and first_class[1] < second_class[1]:
        return (f'Больше всего девочек в классе {key_list[second_class_name]}\nБольше всего мальчиков в классе {key_list[second_class_name]}')
    elif first_class[0] < second_class[0] and first_class[1] > second_class[1]:
        return (f'Больше всего девочек в классе {key_list[second_class_name]}\nБольше всего мальчиков в классе {key_list[first_class_name]}')
    
most_gender = comp_classes(all_classes['2a'], all_classes['3c'])
print(most_gender)
#думается мне, тут вообще фигни наворотил лишней
