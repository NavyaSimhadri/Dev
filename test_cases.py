```python
import unittest
import requests

BASE_URL = "http://localhost:3000"


class StudentAPITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create a temporary student for testing."""
        cls.temporary_student = {
            "name": "TestStudent",
            "rollNo": "TEST1001",
            "course": "DevOps"
        }

        response = requests.post(
            f"{BASE_URL}/students",
            json=cls.temporary_student,
            timeout=5
        )

        if response.status_code != 201:
            raise RuntimeError(
                f"Could not create test student: "
                f"{response.status_code} {response.text}"
            )

        cls.student_id = response.json()["id"]

    def test_01_get_students(self):
        response = requests.get(
            f"{BASE_URL}/students",
            timeout=5
        )

        self.assertEqual(response.status_code, 200)
        print("PASS: GET /students returns status 200")

    def test_02_get_student_data(self):
        response = requests.get(
            f"{BASE_URL}/students",
            timeout=5
        )

        self.assertEqual(response.status_code, 200)

        students = response.json()
        self.assertIsInstance(students, list)
        self.assertTrue(len(students) > 0)

        print("PASS: GET response contains student data")

    def test_03_post_student(self):
        response = requests.get(
            f"{BASE_URL}/students/{self.student_id}",
            timeout=5
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["name"],
            "TestStudent"
        )

        print("PASS: POST creates a temporary student")

    def test_04_patch_student(self):
        response = requests.patch(
            f"{BASE_URL}/students/{self.student_id}",
            json={"course": "Cloud Computing"},
            timeout=5
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["course"],
            "Cloud Computing"
        )

        print("PASS: PATCH updates the temporary student")

    def test_05_delete_student(self):
        response = requests.delete(
            f"{BASE_URL}/students/{self.student_id}",
            timeout=5
        )

        self.assertEqual(response.status_code, 200)

        print("PASS: DELETE removes the temporary student")

    def test_06_verify_deletion(self):
        response = requests.get(
            f"{BASE_URL}/students/{self.student_id}",
            timeout=5
        )

        self.assertEqual(response.status_code, 404)

        print("PASS: Deleted student returns status 404")


if __name__ == "__main__":
    unittest.main(verbosity=2)
```