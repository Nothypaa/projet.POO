class Enrollment:
    """
    Enrollment class to link students with courses.
    Demonstrates Encapsulation OOP principle.
    """
    
    def __init__(self, student, course):
        # Protected attributes for encapsulation
        self._student = student
        self._course = course
        self._date = None  # Will store enrollment date
    
    @property
    def student(self):
        return self._student
    
    @property
    def course(self):
        return self._course
    
    def register(self):
        """Links a student to a course"""
        import datetime
        # Try to enroll the student in the course
        success = self._course.enroll_student(self._student)
        if success:
            # Set enrollment date if successful
            self._date = datetime.datetime.now()
            return True
        return False