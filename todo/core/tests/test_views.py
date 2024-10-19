from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from core.models import Todo
from core.serializers import TodoSerializer


class TodoListTests(APITestCase):
    def setUp(self):
        # Create initial data
        self.todo1 = Todo.objects.create(title="Task 1", description="Task 1 description", completed=False)
        self.todo2 = Todo.objects.create(title="Task 2", description="Task 2 description", completed=True)
        self.valid_payload = {
            "title": "Task 3",
            "description": "Task 3 description",
            "completed": False
        }
        self.invalid_payload = {
            "title": "",
            "description": "Task 4 description",
            "completed": False
        }
    
    def test_get_all_todos(self):
        url = '/api/v1/todos/'
        response = self.client.get(url)
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_valid_todo(self):
        url = '/api/v1/todos/'
        response = self.client.post(url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_todo(self):
        url = '/api/v1/todos/'
        response = self.client.post(url, data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class TodoDetailTests(APITestCase):
#     def setUp(self):
#         self.todo = Todo.objects.create(title="Task 1", description="Task 1 description", completed=False)
#         self.valid_payload = {
#             "title": "Updated Task",
#             "description": "Updated description",
#             "completed": True
#         }
#         self.invalid_payload = {
#             "title": "",
#             "description": "Updated description",
#             "completed": True
#         }

#     def test_get_valid_single_todo(self):
#         url = '/api/v1/todos/{}/'.format(self.todo.pk)
#         response = self.client.get(url)
#         todo = Todo.objects.get(pk=self.todo.pk)
#         serializer = TodoSerializer(todo)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)

#     def test_get_invalid_single_todo(self):
#         url = '/api/v1/todos/{}/'.format(999)
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_update_valid_todo(self):
#         url = '/api/v1/todos/{}/'.format(self.todo.pk)
#         response = self.client.put(url, data=self.valid_payload, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_invalid_todo(self):
#         url = '/api/v1/todos/{}/'.format(self.todo.pk)
#         response = self.client.put(url, data=self.invalid_payload, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_delete_todo(self):
#         url = '/api/v1/todos/{}/'.format(self.todo.pk)
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
