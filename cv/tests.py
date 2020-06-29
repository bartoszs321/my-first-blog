from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest  
from django.template.loader import render_to_string

from cv.views import cv_home

class CvPageTest(TestCase):

    def test_cv_home_returns_correct_html(self):
        response = self.client.get('/cv/')

        self.assertTemplateUsed(response, 'cv/cv_home.html')

    
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()  
    #     response = post_list(request)  
    #     html = response.content.decode('utf8')  
    #     self.assertTrue(html.startswith('<html>'))  
    #     self.assertIn('<title>To-Do lists</title>', html)  
    #     self.assertTrue(html.endswith('</html>'))  