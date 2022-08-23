class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_current_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        """Оценка лекторам от студента"""
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                print(f'Оценка {grade} лектору {lecturer.name} {lecturer.surname} \n'
                      f'за курс {course} от студента {self.name} {self.surname} выставлена.\n')
                return
            else:
                lecturer.grades[course] = [grade]
                print(f'Оценка {grade} лектору {lecturer.name} {lecturer.surname} \n'
                      f'за курс {course} от студента {self.name} {self.surname} выставлена.\n')
                return
        else:
            return print('Оценка лектору не выставлена!')

    def hw_average_grade(self):
        """Средняя оценка по курсам"""
        if len(self.grades) == 0:
            return 'У студента нет оценок.'
        else:
            total = 0
            list_len_sum = 0
            for grade_list in self.grades.values():
                list_len_sum += len(grade_list)
                for grade in grade_list:
                    total += grade
            return round(total / list_len_sum, 1)

    def __str__(self):
        """Вывод информации о студенте"""
        average_grade = self.hw_average_grade()
        fin_course_str = ', '.join(self.finished_courses)
        current_course_str = ', '.join(self.courses_in_progress)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка: {average_grade}\n'
                f'Текущие курсы: {current_course_str}\n'
                f'Завершенные курсы: {fin_course_str}')

    def __lt__(self, other_student):
        """Сравнение студентов"""
        if isinstance(other_student, Student) and len(self.grades) > 0 and len(other_student.grades) > 0:
            return (f'Средняя оценка студента {self.name} {self.surname} = {self.hw_average_grade()}. \n'
                    f'Средняя оценка студента {other_student.name} {other_student.surname} = {other_student.hw_average_grade()}\n'
                    f'У студента {self.name} {self.surname} оценка выше.')
        else:
            return 'Нет оценки у одного из студентов.'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def grade_hw(self, student, course, grade):
        """Ревьювер ставит оценки"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                print(f'Оценка {grade} у студента {student.name} {student.surname} \n'
                      f'за курс {course} от ревьювера {self.name} {self.surname} поставлена.\n')
            else:
                student.grades[course] = [grade]
                print(f'Оценка {grade} у студента {student.name} {student.surname}\n'
                      f'за курс {course} от ревьювера {self.name} {self.surname} поставлена.\n')
        else:
            print(f'Ошибка. {self.name} не ревьювер.')
            return


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def lesson_average_grade(self):
        """Средняя оценка по курсам лектора"""
        if len(self.grades) == 0:
            return 'Лектору не проставили оценок.'
        else:
            total = 0
            list_len_sum = 0
            for grade_list in self.grades.values():
                list_len_sum += len(grade_list)
                for grade in grade_list:
                    total += grade
            return round(total / list_len_sum, 1)

    def __str__(self):
        """Вывод информации о лекторе"""
        res = (f'Имя лектора: {self.name}\n'
               f'Фамилия лектора: {self.surname}\n'
               f'Средняя оценка за лекции: {self.lesson_average_grade()}')
        return res

    def __lt__(self, other_lecturer):
        """Сравнение лекторов"""
        if isinstance(other_lecturer, Lecturer) and len(self.grades) > 0 and len(other_lecturer.grades) > 0:
            return (f'Средняя оценка лектору {self.name} = {self.lesson_average_grade()}. \n'
                    f'Средняя оценка лектору {other_lecturer.name} {other_lecturer.lesson_average_grade()}\n'
                    f'У лектора {self.name} оценка выше.')
        else:
            return 'Нет оценки у одного из лекторов.'


class Reviewer(Mentor):
    def __str__(self):
        """Вывод информации о ревьювере"""
        res = (f'Имя ревьювера: {self.name}\n'
               f'Фамилия ревьювера: {self.surname}')
        return res


# Студенты

igor_student = Student('Игорь', 'Перлин', 'male')
igor_student.add_current_courses('python')
igor_student.add_finished_courses('GIT')

natalia_student = Student('Наталья', 'Чуднова', 'female')
natalia_student.add_current_courses('python')
natalia_student.add_current_courses('GIT')
# natalia_student.add_finished_courses('GIT')

# Лекторы

oleg = Lecturer('Олег', 'Булыгин')
oleg.courses_attached.append('python')
oleg.courses_attached.append('SQL')

alena = Lecturer('Алёна', 'Батицкая')
alena.courses_attached.append('GIT')

# Ревьюверы

glafira = Reviewer('Глафира', 'Пуговкина')
glafira.courses_attached.append('python')

dobrinja = Reviewer('Добрыня', 'Булочкин')
dobrinja.courses_attached.append('GIT')


students_list = [igor_student, natalia_student]
lecturers_list = [alena, oleg]


def st_course_average(some_list, course):
    """Средняя оценка студентов по курсу"""
    total_rate = []
    for person in some_list:
        if not isinstance(person, Student):
            return f'{person} не студент.'
        else:
            if course in person.grades:
                total_rate += person.grades[course]
    res = round(sum(total_rate) / len(total_rate), 2)
    print(f'Средняя оценка студентов по курсу {course} = {res}.')
    return


def lecturer_course_average(some_list, course):
    """Средняя оценка лекторов по курсу"""
    total_rate = []
    for person in some_list:
        if not isinstance(person, Lecturer):
            print(f'{person} не лектор.')
            return
        else:
            if course in person.grades:
                total_rate += person.grades[course]
    res = round(sum(total_rate) / len(total_rate), 2)
    print(f'Средняя оценка лекторов по курсу {course} = {res}.')
    return

from pprint import pprint

# Тестировние результатов

igor_student.rate_lecturer(oleg, 'python', 9)
igor_student.rate_lecturer(alena, 'GIT', 10)

natalia_student.rate_lecturer(oleg, 'python', 7)
natalia_student.rate_lecturer(alena, 'GIT', 8)

glafira.grade_hw(igor_student, 'python', 5)
dobrinja.grade_hw(igor_student, 'python', 9)
glafira.grade_hw(natalia_student, 'python', 9)
dobrinja.grade_hw(natalia_student, 'python', 2)

# print()

print(igor_student, natalia_student, alena, oleg, glafira, dobrinja, sep='\n\n')

print(igor_student < natalia_student)
print(alena < oleg)

lecturer_course_average(lecturers_list, 'python')
st_course_average(students_list, 'python')