class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print("Error: Student is already enrolled!")
        else:
            self.__is_enrolled = True
            print("Student enrolled successfully!")

    def drop_student(self):
        if not self.__is_enrolled:
            print("Error: Student is not enrolled!")
        else:
            self.__is_enrolled = False
            print("Student dropped successfully!")

    def view_student_info(self):
        print("Student ID:", self.__student_id)
        print("Name:", self.__name)
        print("Department:", self.__department)
        print("Enrollment Status:", self.__is_enrolled)


# Create Student Objects
s1 = Student(101, "Rahim Ahmed", "CSE", True)
s2 = Student(102, "Karim Hasan", "EEE", False)
s3 = Student(103, "Sakib Hasan", "BBA", True)


# Menu Driven System
while True:
    print("\n===== Student Management System =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for student in StudentDatabase.student_list:
            student.view_student_info()
            print("----------------------")

    elif choice == "2":
        try:
            student_id = int(input("Enter Student ID to enroll: "))
            found = False

            for student in StudentDatabase.student_list:
                if student._Student__student_id == student_id:
                    student.enroll_student()
                    found = True
                    break

            if not found:
                print("Error: Invalid Student ID!")

        except ValueError:
            print("Error: Enter a valid numeric Student ID!")

    elif choice == "3":
        try:
            student_id = int(input("Enter Student ID to drop: "))
            found = False

            for student in StudentDatabase.student_list:
                if student._Student__student_id == student_id:
                    student.drop_student()
                    found = True
                    break

            if not found:
                print("Error: Invalid Student ID!")

        except ValueError:
            print("Error: Enter a valid numeric Student ID!")

    elif choice == "4":
        print("Exiting Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")