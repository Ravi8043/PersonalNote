from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from .models import Note

# Create your tests here.
class PostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='testmail@gmail.com'
        )

        self.note = Note.objects.create(
            title='Test Blog',
            content='this is a test blog content'
        )
    def test_string_representation(self):
        self.assertEqual(self.note.title, 'Test Blog')

    def test_blog_content(self):
        self.assertEqual(self.note.content, 'this is a test blog content')
    def test_blog_list_view(self):
        response = self.client.get(reverse('list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')
        self.assertTemplateUsed(response, 'list.html')


