# file: course_catalog.py
from dataclasses import dataclass
from typing import List

@dataclass
class Course:
    number: str
    name: str
    description: str
    instructor: str
    location: str
    time: str


class CourseCatalog:
    def __init__(self):
        self.courses: List[Course] = []

    def add_course(self, course: Course):
        self.courses.append(course)

    def list_courses(self):
        if not self.courses:
            print("No courses available.")
            return
        for c in self.courses:
            self._print_course(c)

    def search_courses(self, keyword: str):
        keyword = keyword.lower()
        results = [
            c for c in self.courses
            if keyword in c.number.lower()
            or keyword in c.name.lower()
            or keyword in c.instructor.lower()
        ]
        if not results:
            print("No matching courses found.")
            return
        for c in results:
            self._print_course(c)

    def _print_course(self, c: Course):
        print(f"\nCourse Number : {c.number}")
        print(f"Course Name   : {c.name}")
        print(f"Description   : {c.description}")
        print(f"Instructor    : {c.instructor}")
        print(f"Location      : {c.location}")
        print(f"Time          : {c.time}")
        print("-" * 50)


def main():
    catalog = CourseCatalog()

    # Sample Data
    catalog.add_course(Course(
        "CS101", "Intro to Programming",
        "Learn JAVA basics and problem solving.",
        "Al Dungo", "Online", "T/TH 1730-1900"
    ))
    catalog.add_course(Course(
        "CS201", "Data Structures",
        "Covers lists, stacks, queues, trees, and graphs.",
        "Prof. Bob Johnson", "Room 305", "Wed 1300"
    ))
    catalog.add_course(Course(
        "CS301", "Database Systems",
        "Introduction to SQL and database design.",
        "Dr. Carol White", "Room 410", "Fri 0900"
    ))

    while True:
        print("\n=== COURSE CATALOG ===")
        print("1. List all courses")
        print("2. Search for a course")
        print("3. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            catalog.list_courses()
        elif choice == "2":
            keyword = input("Enter course number, name, or instructor: ")
            catalog.search_courses(keyword)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
