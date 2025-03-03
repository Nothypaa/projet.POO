class Course:
    """
    Course class for managing course information.
    Demonstrates Encapsulation OOP principle.
    """


    def __init__(self, course_name, course_code, credit_hours):

        self._course_name = course_name
        self._course_code = course_code
        self._credit_hours = credit_hours
        self._students = []

    @property
    def course_name(self):
        return self._course_name
    

    @property
    def course_code(self):
        return self._course_code
    
    @property
    def credit_hours(self):
        return self._credit_hours
    
    def enroll_student(self, student):
        """Adds a student to the course"""

        if student.student_id not in [s.student_id for s in self._students]:
            self._students.append(student)
            return True
        return False
    

    def get_enrolled_students(self):
       """Returns the list of students in the course"""
       return self._students 
    