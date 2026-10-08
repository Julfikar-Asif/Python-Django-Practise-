# # # def hello(greeting, name = "asif"):
# # #     return '{} {}'.format(greeting, name)

# # # print(hello("Hi"))  

# # def studnet_info(*args, **kwargs):
# #     print(args)
# #     print(kwargs)

# # course = ['Math', 'Science', 'History']
# # info = {'name': 'Alice', 'age': 20}

# # studnet_info(*course, **info)

# # Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# def is_leap(year):
#     """Return True for leap years, False for non-leap years."""

#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# def days_in_month(year, month):
#     """Return number of days in that month in that year."""

#     # year 2017
#     # month 2
#     if not 1 <= month <= 12:
#         return 'Invalid Month'

#     if month == 2 and is_leap(year):
#         return 29

#     return month_days[month]

# print(days_in_month(2017, 2))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [num for num in numbers if num % 2 == 0]
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(even_numbers)  
# print(odd_numbers)

students = [
    {"name": "Rahim", "marks": 85},
    {"name": "Karim", "marks": 72},
    {"name": "Fatema", "marks": 90},
    {"name": "Jamal", "marks": 95},
    {"name": "Nusrat", "marks": 65},
]
# scores = [student["name"] for student in students if student["marks"] >= 80]
# print(scores)
def get_grade(marks):
    if marks >= 93:
        return "A+"
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def get_passed_students(students):
    passed_students = [student["name"] for student in students if student["marks"] >= 40]
    return passed_students

def get_avg(students):
    total_marks = sum(student["marks"] for student in students)
    avg_marks = total_marks / len(students)
    return avg_marks
def get_student_with_grade(students, grade):
    students_with_grade = [student["name"] for student in students if get_grade(student["marks"]) == grade]
    return students_with_grade

for student in students:
    grade = get_grade(student["marks"])
    print(f"{student['name']}  has grade {grade}")

print(f" passed: {get_passed_students(students)}")
print(f"Average marks: {get_avg(students)}")
print(f"Students with grade  A+ : {get_student_with_grade(students,  'A+')}")    


