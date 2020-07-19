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

        # self.fail('Finish the Test!')
        # self.browser.quit()

    def test_can_create_a_new_qualification_and_view_it_later(self):
        #Want to create a new qualification
        self.browser.get('http://localhost:8000/cv/qualification/new')

        #You are invited to enter the title of a qualification
        titleInputBox = self.browser.find_element_by_id('id_title')
        
        #You enter the title of your qualification
        titleInputBox.send_keys('Bachelor of Computer Science')

        #You are invited to fill out the start and completion date of your qualification
        startDateInputBox = self.browser.find_element_by_id('id_date_started')
        startDateInputBox.send_keys('2020-06-18')

        completeDateInputBox = self.browser.find_element_by_id('id_date_completed')
        completeDateInputBox.send_keys('2020-07-18')

        #You are invited to enter the awarding body
        awardingBodyInputBox = self.browser.find_element_by_id('id_awarding_body')
        awardingBodyInputBox.send_keys('University of Birmingham')

        #You are invited to enter the details of the qualification
        detailInputBox = self.browser.find_element_by_id('id_text')
        detailInputBox.send_keys('This is my degree and this is my 10/10 description of what it includes')

        #You save the qualification
        submitButton = self.browser.find_element_by_id('save_button')
        submitButton.click()

        time.sleep(10)

        #Load the CV home page
        # self.browser.get('http:localhost:8000/cv/')

        #Find the qualifications section and check if the qualification was added
        qualifications = self.browser.find_elements_by_tag_name('h4')
        
        self.assertTrue(
            any(qualification.text == 'Bachelor of Computer Science' for qualification in qualifications),
            f"Qualification did not appear on home page. Contents were: \n{qualifications[0].text}"
        )

        self.fail("Finish this test!")

if __name__ == '__main__':
    unittest.main(warnings='ignore')