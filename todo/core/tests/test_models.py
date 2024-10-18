from django.test import TestCase
from django.core.exceptions import ValidationError

from core.models import Todo


class TodoModelTest(TestCase):

    def test_create_todo_with_valid_data(self):
        todo = Todo.objects.create(
            title='Buy groceries',
            description='Milk, Bread, Eggs',
            completed=False
        )
        self.assertEqual(todo.title, 'Buy groceries')
        self.assertEqual(todo.description, 'Milk, Bread, Eggs')
        self.assertFalse(todo.completed)

    def test_title_max_length(self):
        max_length_title = 'A' * 100
        todo = Todo(title=max_length_title, description='Test description')
        todo.full_clean()  # Validates the model fields
        todo.save()
        self.assertEqual(todo.title, max_length_title)

    def test_title_exceeds_max_length(self):
        over_length_title = 'A' * 101
        todo = Todo(title=over_length_title, description='Test description')
        with self.assertRaises(ValidationError):
            todo.full_clean()

    def test_title_cannot_be_empty(self):
        todo = Todo(title='', description='Test description')
        with self.assertRaises(ValidationError):
            todo.full_clean()

    def test_description_can_be_empty(self):
        todo = Todo.objects.create(title='Test Todo', description='')
        self.assertEqual(todo.description, '')

    def test_description_can_be_very_long(self):
        long_description = 'A' * 10000  # Simulate a long text
        todo = Todo.objects.create(title='Test Todo', description=long_description)
        self.assertEqual(todo.description, long_description)

    def test_completed_defaults_to_false(self):
        todo = Todo.objects.create(title='Test Todo', description='Test description')
        self.assertFalse(todo.completed)

    def test_completed_can_be_true(self):
        todo = Todo.objects.create(title='Test Todo', description='Test description', completed=True)
        self.assertTrue(todo.completed)

    def test_completed_cannot_be_none(self):
        todo = Todo(title='Test Todo', description='Test description', completed=None)
        with self.assertRaises(ValidationError):
            todo.full_clean()

    def test_str_method_returns_title(self):
        todo = Todo.objects.create(title='Test Todo', description='Test description')
        self.assertEqual(str(todo), 'Test Todo')

    def test_create_multiple_todos(self):
        todo1 = Todo.objects.create(title='Todo 1', description='First todo')
        todo2 = Todo.objects.create(title='Todo 2', description='Second todo')
        todos = Todo.objects.all()
        self.assertEqual(todos.count(), 2)
        self.assertIn(todo1, todos)
        self.assertIn(todo2, todos)

    def test_retrieve_todo_by_title(self):
        todo = Todo.objects.create(title='Unique Title', description='Test description')
        retrieved_todo = Todo.objects.get(title='Unique Title')
        self.assertEqual(retrieved_todo, todo)

    def test_update_todo_completed_status(self):
        todo = Todo.objects.create(title='Test Todo', description='Test description')
        todo.completed = True
        todo.save()
        updated_todo = Todo.objects.get(id=todo.id)
        self.assertTrue(updated_todo.completed)

    def test_delete_todo(self):
        todo = Todo.objects.create(title='Test Todo', description='Test description')
        todo_id = todo.id
        todo.delete()
        with self.assertRaises(Todo.DoesNotExist):
            Todo.objects.get(id=todo_id)
