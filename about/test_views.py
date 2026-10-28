from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(title="About title",
                                   content="About content")
        self.about_content.save()

    def test_render_about_page_with_collaborate_request_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'viktor',
            'email': 'viktor@gmail.com',
            'message': 'This is a test collaboration request.'
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )
