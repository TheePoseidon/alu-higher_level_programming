class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        total_points = 0
        total_credits = 0
        for course, grade in self.courses_registered:
            total_points += grade * course.credits
            total_credits += course.credits
        self.GPA = total_points / total_credits if total_credits != 0 else 0

    def register_for_course(self, course, grade):
        self.courses_registered.append((course, grade))


class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = self.find_student(student_email)
        course = self.find_course(course_name)
        if student and course:
            student.register_for_course(course, grade)

    def find_student(self, email):
        for student in self.student_list:
            if student.email == email:
                return student
        return None

    def find_course(self, name):
        for course in self.course_list:
            if course.name == name:
                return course
        return None

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        self.calculate_GPA()
        self.student_list.sort(key=lambda x: x.GPA, reverse=True)
        return [(student.names, student.GPA) for student in self.student_list]

    def search_by_grade(self, grade):
        results = []
        for student in self.student_list:
            for course, student_grade in student.courses_registered:
                if student_grade == grade:
                    results.append((student.names, course.name))
        return results

    def generate_transcript(self, student_email):
        student = self.find_student(student_email)
        if student:
            transcript = f"Transcript for {student.names} (Email: {student.email})\n"
            transcript += "Courses Registered:\n"
            for course, grade in student.courses_registered:
                transcript += f"{course.name} (Trimester: {course.trimester}, Credits: {course.credits}) - Grade: {grade}\n"
            transcript += f"GPA: {student.GPA:.2f}\n"
            return transcript
        return "Student not found."


def main():
    gradebook = GradeBook()
    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Choose an action: ")
        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            gradebook.add_student(student)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            course = Course(name, trimester, credits)
            gradebook.add_course(course)
        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(student_email, course_name, grade)
        elif choice == '4':
            ranking = gradebook.calculate_ranking()
            print("\nStudent Rankings:")
            for i, (names, GPA) in enumerate(ranking):
                print(f"{i + 1}. {names} - GPA: {GPA:.2f}")
        elif choice == '5':
            grade = float(input("Enter grade to search for: "))
            results = gradebook.search_by_grade(grade)
            print("\nSearch Results:")
            for names, course_name in results:
                print(f"{names} - {course_name}")
        elif choice == '6':
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            print("\n" + transcript)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
