from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest  
from django.template.loader import render_to_string

import time

from cv.views import cv_home
from .models import Qualification, Experience, Interest, Profile

class CvPageTest(TestCase):

    ##
    ## Home page tests
    ##

    def test_cv_home_returns_correct_html(self):
        response = self.client.get('/cv/')

        self.assertTemplateUsed(response, 'cv/cv_home.html')

    ##
    ## Profile Tests
    ##

    def test_new_profile_returns_correct_html(self):
        response = self.client.get('/cv/profile/new/')

        self.assertTemplateUsed(response, 'cv/profile_edit.html')

    def test_can_save_a_profile_POST_request(self):
        self.client.post('/cv/profile/new/', {
            'text': "Personal Email: abc@gmail.com\n University Email: abc123@student.bham.ac.uk"
        })

        self.assertEqual(Profile.objects.count(), 1)
        new_item = Profile.objects.first()
        self.assertTrue('Personal Email: abc@gmail.com\n University Email: abc123@student.bham.ac.uk' in new_item.text)
    ##
    ## Qualification Tests
    ##

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

    ##
    ## Experience tests
    ##

    def test_new_experience_returns_correct_html(self):
        response = self.client.get('/cv/experience/new/')

        self.assertTemplateUsed(response, 'cv/experience_edit.html')

    def test_can_save_an_experience_POST_request(self):
        self.client.post('/cv/experience/new/', {
         'title': 'PwC Summer Placement',
         'date_started': '6/6/2020',
         'date_completed': 'Present',
         'company': 'PwC',
         'text': 'Made a bot using Google Cloud Platform',
          })

        self.assertEqual(Experience.objects.count(), 1)
        new_item = Experience.objects.first()
        self.assertTrue('PwC Summer Placement' in new_item.title)
        
    ##
    ## Interest tests
    ##

    def test_new_interest_returns_correct_html(self):
        response = self.client.get('/cv/interest/new/')

        self.assertTemplateUsed(response, 'cv/interest_edit.html')

    def test_can_save_an_interest_POST_request(self):
        self.client.post('/cv/interest/new/', {
         'title': 'Walking',
         'text': 'I enjoy going for walks in the country side',
          })

        self.assertEqual(Interest.objects.count(), 1)
        new_item = Interest.objects.first()
        self.assertTrue('Walking' in new_item.title)
    
    ##
    ## Deletion Tests
    ##

    def test_delete_profile_detail_returns_correct_html(self):
        response = self.client.get('/cv/profile/remove/')

        self.assertTemplateUsed(response, 'cv/profile_remove.html')