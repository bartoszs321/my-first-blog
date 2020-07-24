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
        self.browser.get('http://localhost:8000/cv/')

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

    def test_can_create_a_new_about_me_entry_and_view_it_later(self):
        #Want to create a new information section
        self.browser.get('http://localhost:8000/cv/profile/new/')

        #You are invited to enter some information about yourself
        detailInputBox = self.browser.find_element_by_id('id_text')
        detailInputBox.send_keys('Some very very very interesting information about me :)')

        #You save the qualification and are redirected to the cv home page
        submitButton = self.browser.find_element_by_id('save_button')
        submitButton.click()

        #Find profile section of website and see if new information has been added
        profile = self.browser.find_element_by_id('profile')
        self.assertTrue('Some very very very interesting information about me :)' in profile.text,
         f"Information not added to home page. Actual contents: {profile.text}")

    def test_can_create_a_new_qualification_and_view_it_later(self):
        #Want to create a new qualification
        self.browser.get('http://localhost:8000/cv/qualification/new/')

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

        #You save the qualification and are redirected to the cv home page
        submitButton = self.browser.find_element_by_id('save_button')
        submitButton.click()

        #Find the qualifications section and check if the qualification was added
        qualifications = self.browser.find_element_by_id('education')
        self.assertTrue('Bachelor of Computer Science' in qualifications.text,
         f"Qualification not added to home page. Actual contents: {qualifications.text}")

    def test_can_create_a_new_experience_and_view_it_later(self):
        #Want to add a new experience
        self.browser.get('http://localhost:8000/cv/experience/new/')

        #You are invited to input the title for the experience
        titleInputBox = self.browser.find_element_by_id('id_title')
        titleInputBox.send_keys("Summer Placement at PwC")

        #You are invited to enter your start date and finish date
        startDateInputBox = self.browser.find_element_by_id('id_date_started')
        startDateInputBox.send_keys("6/6/2020")

        completeDateInputBox = self.browser.find_element_by_id('id_date_completed')
        completeDateInputBox.send_keys("Present")

        #You are invited to enter the company your experience is at
        companyInputBox = self.browser.find_element_by_id('id_company')
        companyInputBox.send_keys("PwC")

        #You are invited to enter extra detail about your experience
        detailInputBox = self.browser.find_element_by_id('id_text')
        detailInputBox.send_keys("Made a bot using Google Cloud Platform")

        #You click submit to save your experience entry
        submitButton = self.browser.find_element_by_id('save_button')
        submitButton.click()

        #Check if the experience entry has been added to the home page
        experience = self.browser.find_element_by_id('experiences')
        self.assertTrue('Summer Placement at PwC' in experience.text,
        f"Experience not added to home page. Actual content: {experience.text}")

    def test_can_create_a_new_interest_and_view_it_later(self):
        #Want to add a new interest
        self.browser.get('http://localhost:8000/cv/interest/new/')

        #You are invited to enter a title for your interest
        titleInputBox = self.browser.find_element_by_id('id_title')
        titleInputBox.send_keys('Walking')

        #You are invited to enter any details about your interest
        detailInputBox = self.browser.find_element_by_id('id_text')
        detailInputBox.send_keys('I enjoy going for walks in the country side')

        #You click the submit button to save your interest
        submitButton = self.browser.find_element_by_id('save_button')
        submitButton.click()

        #Check if the interest entry has been added to the home page
        interests = self.browser.find_element_by_id('interests')
        self.assertTrue('Walking' in interests.text,
        f"Interest not added to home page. Actual content: {interests.text}")

if __name__ == '__main__':
    unittest.main(warnings='ignore')