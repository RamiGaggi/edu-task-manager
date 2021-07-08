from django.test import TestCase
from django.urls import reverse


class TasksIndexViewTests(TestCase):
    """Test index view."""

    def test_index(self):
        """If no questions exist, an appropriate message is displayed."""
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)
