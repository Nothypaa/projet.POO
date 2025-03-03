from flask import Flask, request, jsonify
import datetime

# Import models
from models.student import Student, UndergraduateStudent, GraduateStudent
from models.course import Course
from models.enrollment import Enrollment

app = Flask(__name__)

# Simple in-memory storage for demonstration
students = {}
courses = {}
enrollments = []

@app.route('/')
def home():
    """Root endpoint that returns basic API information"""
    return jsonify({"message": "Student Management System API"})

# Student endpoints
@app.route('/students', methods=['POST'])
def create_student():
    """Endpoint to create a new student"""
    data = request.get_json()
    
    try:
        student_type = data.get('student_type', 'regular')
        
        # Create different types of students based on student_type
        if student_type == 'undergraduate':
            student = UndergraduateStudent(
                name=data['name'],
                student_id=data['student_id'],
                age=int(data['age']),
                major=data.get('major', '')
            )
        elif student_type == 'graduate':
            student = GraduateStudent(
                name=data['name'],
                student_id=data['student_id'],
                age=int(data['age']),
                research_area=data.get('research_area', '')
            )
        else:
            student = Student(
                name=data['name'],
                student_id=data['student_id'],
                age=int(data['age'])
            )
        
        # Add grades if provided
        if 'grades' in data and isinstance(data['grades'], list):
            for grade in data['grades']:
                student.add_grade(float(grade))
        
        # Store the student
        students[data['student_id']] = student
        
        return jsonify({
            "message": "Student created",
            "student": student.get_details()
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Endpoint to retrieve a student's details"""
    if student_id in students:
        return jsonify(students[student_id].get_details()), 200
    return jsonify({"error": "Student not found"}), 404

# Course endpoints
@app.route('/courses', methods=['POST'])
def create_course():
    """Endpoint to create a new course"""
    data = request.get_json()
    
    try:
        course = Course(
            course_name=data['course_name'],
            course_code=data['course_code'],
            credit_hours=int(data['credit_hours'])
        )
        
        # Store the course
        courses[data['course_code']] = course
        
        return jsonify({
            "message": "Course created",
            "course": {
                "course_name": course.course_name,
                "course_code": course.course_code,
                "credit_hours": course.credit_hours
            }
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/courses/<course_code>', methods=['GET'])
def get_course(course_code):
    """Endpoint to retrieve course details including enrolled students"""
    if course_code in courses:
        course = courses[course_code]
        enrolled_students = []
        
        # Get details of all enrolled students
        for student in course.get_enrolled_students():
            enrolled_students.append(student.get_details())
        
        return jsonify({
            "course_name": course.course_name,
            "course_code": course.course_code,
            "credit_hours": course.credit_hours,
            "enrolled_students": enrolled_students
        }), 200
    
    return jsonify({"error": "Course not found"}), 404

# Enrollment endpoint
@app.route('/enrollments', methods=['POST'])
def create_enrollment():
    """Endpoint to enroll a student in a course"""
    data = request.get_json()
    
    try:
        student_id = data.get('student_id')
        course_code = data.get('course_code')
        
        # Check if student exists
        if student_id not in students:
            return jsonify({"error": f"Student {student_id} not found"}), 404
        
        # Check if course exists
        if course_code not in courses:
            return jsonify({"error": f"Course {course_code} not found"}), 404
        
        student = students[student_id]
        course = courses[course_code]
        
        # Create enrollment and register
        enrollment = Enrollment(student, course)
        success = enrollment.register()
        
        if success:
            enrollments.append(enrollment)
            return jsonify({
                "message": "Student enrolled in course",
                "details": {
                    "student_id": student.student_id,
                    "student_name": student.name,
                    "course_code": course.course_code,
                    "course_name": course.course_name
                }
            }), 201
        else:
            return jsonify({"error": "Student already enrolled in this course"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Start the Flask app in debug mode
    app.run(debug=True)