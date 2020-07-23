from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest  
from django.template.loader import render_to_string

import time

from cv.views import cv_home
from .models import Qualification

class CvPageTest(TestCase):

    def test_cv_home_returns_correct_html(self):
        response = self.client.get('/cv/')

        self.assertTemplateUsed(response, 'cv/cv_home.html')

    def test_new_qualification_returns_correct_html(self):
        response = self.client.get('/cv/qualification/new/')

        self.assertTemplateUsed(response, 'cv/qualification_edit.html')
    
    def test_can_save_a_qualification_POST_request(self):
        self.client.post('/cv/qualification/new/', {
         'title': 'Bachelor of Computer Science',
         'date_started': '2020-06-18',
         'date_completed': '2020-07-18',
         'awarding_body': 'University of Birmingham',
         'text': 'This is my degree and this is my 10/10 description of what it includes',
          })
        
        self.assertEqual(Qualification.objects.count(), 1)
        new_item = Qualification.objects.first()
        self.assertTrue('Bachelor of Computer Science' in new_item.title)