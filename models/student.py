from models.person import Person

class Student(Person):
    """
    Student class that inherits from Person.
    Demonstrates Inheritance OOP principle.
    """
    
    def __init__(self, name, student_id, age):  # Remove the major parameter
        # Call the parent class constructor
        super().__init__(name, age)
        self._student_id = student_id
        self._grades = []  # List to store student grades
    
    @property
    def student_id(self):
        return self._student_id
    
    @property
    def grades(self):
        return self._grades
    
    def add_grade(self, grade):
        """Adds a grade to the student's grade list"""
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    def get_average_grade(self):
        """Returns the average grade of the student"""
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)
    
    def get_details(self):
        """Implements the abstract method from Person"""
        return {
            "name": self.name,
            "student_id": self.student_id,
            "age": self.age,
            "grades": self.grades,
            "average_grade": self.get_average_grade()
        }


class UndergraduateStudent(Student):
    """
    Undergraduate student class that inherits from Student.
    Shows inheritance and polymorphism.
    """

    def __init__(self, name, student_id, age, major):  # Fix method name
        super().__init__(name, student_id, age)
        self._major = major

    @property
    def major(self):
        return self._major

    def get_average_grade(self):
        """
        Override for undergraduate students
        """
        if not self._grades:
            return 0
        
        return sum(self._grades) / len(self._grades) * 0.9

    def get_details(self):
        """Override get_details to include major"""
        details = super().get_details()
        details["major"] = self.major
        details["type"] = "undergraduate"
        return details


class GraduateStudent(Student):
    """
    Graduate student class that inherits from Student.
    Shows inheritance and polymorphism.
    """

    def __init__(self, name, student_id, age, research_area):
        super().__init__(name, student_id, age)
        self._research_area = research_area

    @property
    def research_area(self):  # Fix property name
        return self._research_area
    
    def get_average_grade(self):
        """
        Override for graduate students - demonstrates polymorphism
        """
        if not self._grades:
            return 0
        
        return sum(self._grades) / len(self._grades) * 1.1
    
    def get_details(self):
        """Override get_details to include research area"""
        details = super().get_details()
        details["research_area"] = self._research_area
        details["type"] = "graduate"
        return details