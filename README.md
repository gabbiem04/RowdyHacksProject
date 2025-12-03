# RowdyHacksProject
## RowdyHacks Project Course Catalog

This project is an user-friendly Course Catalog program written in Python that runs in a console.  It shows basic object-oriented design principles and lets users browse and interact with a list of academic courses.  The program is written in Python, but its structure is very similar to Java's object-oriented programming style. This makes it a good reference for people who are learning both languages.

### Overview

The application consists of two central components:

 - Course – a Python @dataclass representing a single academic course with attributes such as course number, name, description, instructor, location, and time.

 - CourseCatalog – a manager class that stores multiple Course objects, allowing operations such as adding new courses, listing all courses, and searching for courses by keyword.

The main() function initializes the catalog, holds the sample data, and presents a command-line menu through which the user can browse or search for courses. The program runs continuously until the user chooses to exit or the user input is invalid.

### How the program works:

The Course dataclass is a simple, clear way to show information about a course.  The @dataclass decorator in Python makes the initializer and other boilerplate methods for you, which cuts down on duplication and makes the code easier to read.

The CourseCatalog class keeps a list of course objects and gives you ways to modify and display them.  A helper method is used inside the program to format and print information about the course.  When the program starts, it fills the catalog with sample courses and starts a menu loop that the user can control.  Users can see all the courses that are available, search for a course by keyword, or close the app.

### Python and Java

#### Similarities 
- Object-oriented structure
- Both Python and Java stress using classes, objects, and encapsulation to model things in the real world, like academic courses and the catalog that holds them.
- The catalog uses a list of Course objects, which is similar to how Java uses generic collections like List to store multiple instances of a class.
- The main loop of the program, which uses user input to control what the program does, is very similar to how Java usually uses a Scanner in a continuous loop to read and process user commands.
- The logic for matching keywords in the course search function is similar to how Java handles strings, especially how it normalizes case and compares substrings.

### Potential Issues/Problems:

- User Input Handling:
User input is unpredictable and may require validation to prevent errors or unexpected behavior.

- Search Functionality:
Performing accurate keyword searches requires proper normalization of text (e.g., converting strings to lowercase). Missing these steps can lead to inconsistent search results.

- Data Management:
While storing courses in a list works for small programs, larger systems may need more efficient data structures or persistent storage solutions such as databases.

### Summary

This project serves as a clear example of object-oriented programming in Python, while also reflecting patterns familiar to Java developers. It demonstrates how to model data using classes, interact with collections, and build a user-driven console application. Although simple, the program highlights common development challenges and provides a strong foundation for extending the system into a more advanced application.
