from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest  
from django.template.loader import render_to_string

from cv.views import cv_home

class CvPageTest(TestCase):

    def test_cv_home_returns_correct_html(self):
        response = self.client.get('/cv/')

        self.assertTemplateUsed(response, 'cv/cv_home.html')

    def test_new_qualification_returns_correct_html(self):
        response = self.client.get('/cv/qualification/new/')

        self.assertTemplateUsed(response, 'cv/qualification_edit.html')
    
    def test_can_save_a_qualification_POST_request(self):
        response = self.client.post('http://localhost:8000/cv/qualification/new/', form={
         'title': 'Bachelor of Computer Science',
         'date_started': '2020-06-18',
         'date_completed': '2020-07-18',
         'awarding_body': 'University of Birmingham',
         'text': 'This is my degree and this is my 10/10 description of what it includes',
          })

        self.assertIn('Bachelor of Computer Science', response.content.decode())
        self.assertIn('2020-06-18', response.content.decode())
        self.assertIn('2020-07-18', response.content.decode())
        self.assertIn('University of Birmingham', response.content.decode())
        self.assertIn('This is my degree and this is my 10/10 description of what it includes', response.content.decode())

        self.assertTemplateUsed(response, 'cv/qualification_edit.html')