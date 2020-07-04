from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_the_cv_and_retrieve_it_later(self):
        #I want to view my CV
        self.browser.get('http://localhost:8000/cv')

        #The header mentions that this is Bartosz's CV
        self.assertIn('Bartosz\'s CV', self.browser.title)

        #We can see section titles for different sections of the CV
        #At the top of the page is a title
        title = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(title, 'Bartosz\'s CV')

        #The first section is an about me section
        profile = self.browser.find_element_by_id('profile_header').text
        self.assertEqual(profile, 'About me')

        #The second is education
        educationHeading = self.browser.find_element_by_id('education_header').text
        self.assertEqual(educationHeading, 'Education')

        #The third is experience
        experienceHeading = self.browser.find_element_by_id('experience_header').text
        self.assertEqual(experienceHeading, 'Experience')

        #The fourth is my interests
        interestsHeading = self.browser.find_element_by_id('interests_header').text
        self.assertEqual(interestsHeading, 'Interests')

        #Other useful things...

        self.fail('Finish the Test!')
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')