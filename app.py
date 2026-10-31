from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory student database
students = [
    {
        "id": 1,
        "name": "Navya",
        "rollNo": "23071A0500",
        "course": "Computer Science"
    },
    {
        "id": 2,
        "name": "Rahul",
        "rollNo": "23071A0501",
        "course": "Information Technology"
    }
]


# 1. GET: Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200


# 2. GET: Retrieve a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


# 3. POST: Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    if not data or not all(
        key in data for key in ["name", "rollNo", "course"]
    ):
        return jsonify({
            "error": "name, rollNo and course are required"
        }), 400

    new_id = max(
        (student["id"] for student in students),
        default=0
    ) + 1

    new_student = {
        "id": new_id,
        "name": data["name"],
        "rollNo": data["rollNo"],
        "course": data["course"]
    }

    students.append(new_student)

    return jsonify(new_student), 201


# 4. PATCH: Update an existing student
@app.route('/students/<int:student_id>', methods=['PATCH'])
def update_student(student_id):
    data = request.get_json()

    if not isinstance(data, dict) or not data:
        return jsonify({"error": "Provide fields to update"}), 400

    for student in students:
        if student["id"] == student_id:
            allowed_fields = ["name", "rollNo", "course"]

            for key in allowed_fields:
                if key in data:
                    student[key] = data[key]

            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


# 5. DELETE: Remove a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return jsonify({
                "message": "Student deleted successfully"
            }), 200

    return jsonify({"error": "Student not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, port=3000)