import unittest
from app import app

class TestStudents(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_students(self):
        res = self.client.get('/students')
        self.assertEqual(res.status_code, 200)

    def test_post_student(self):
        res = self.client.post('/students', json={
            'name': 'Sam',
            'rollNo': '23071A0502',
            'course': 'Computer Science'
        })
        self.assertEqual(res.status_code, 201)

    def test_invalid_student(self):
        res = self.client.get('/students/999')
        self.assertEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()
