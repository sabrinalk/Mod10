"""
student class definition for unit testing
"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)
                and name_characters.issuperset(major)):
            raise ValueError
        if not isinstance(gpa, float):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

if __name__ == '__main__':
    stu_one = Student("Doe", "John", "Biology", 3.8)
    print(stu_one)
    stu_two = Student("Kho", "Sab", "Math", 3.5)
    print(stu_two)