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

        self.fail("Finish the test!")
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')