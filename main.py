class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0
    def rate(self, mentor, course, grade):
        if isinstance(
                mentor, Lecturer
        ) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        all_grades = []
        sum_grades = 0
        all_courses = []
        for course, grades in self.grades.items():
            all_grades.extend(grades)
            all_courses.append(course)
        for grade in all_grades:
          sum_grades += grade
        self.average_rating = sum_grades / len(all_grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания  {self.average_rating}\nКурсы в процессе изучения: {''.join(all_courses)}\nЗавершенные курсы: {''.join(self.finished_courses)}"
    def __lt__(self, other):
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average_rating = 0
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"      


class Lecturer(Mentor):
    def __str__(self):
        all_grades = []
        sum_grades = 0
        for course, grades in self.grades.items():
            all_grades.extend(grades)
        for grade in all_grades:
          sum_grades += grade
        self.average_rating = sum_grades / len(all_grades)  
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}" 
    def __lt__(self, other):
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

bad_student = Student('Jack', 'Black', 'your_gender')
bad_student.courses_in_progress += ['Python']



cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


cool_mentor.rate_hw(bad_student, 'Python', 6)
cool_mentor.rate_hw(bad_student, 'Python', 3)
cool_mentor.rate_hw(bad_student, 'Python', 2)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Python']

best_student.rate(cool_lecturer, 'Python', 10)
best_student.rate(cool_lecturer, 'Python', 2)
best_student.rate(cool_lecturer, 'Python', 1)
print(cool_lecturer.grades)

print(best_student.grades)

print(str(best_student))
print(str(cool_mentor))
print(str(cool_lecturer))

#Задание №4 функция для лекторов и студентов

def get_average_rating(students_list, course_name):
  sum_grades = 0
  all_length = 0
  for student in students_list:
    all_length += len(student.grades[course_name])
    for grade in student.grades[course_name]:
      sum_grades += grade
  return sum_grades / all_length


print(get_average_rating([cool_lecturer], 'Python')) 
