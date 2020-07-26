from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def signIn(self):
        self.browser.get('http://localhost:8000/accounts/login/')

        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')

        username.send_keys('testaccount')
        password.send_keys('testPass')

        submitButton = self.browser.find_element_by_id('submit')
        submitButton.click()

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
        self.signIn()
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
        self.signIn()
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
        self.signIn()
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
        self.signIn()
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

    def test_can_edit_a_profile_entry(self):
        self.signIn()
        #You are looking at the cv home page and want to edit a profile entry
        self.browser.get('http://localhost:8000/cv/')

        #Saving the contents of the current profile section
        oldProfile = self.browser.find_element_by_id('profile')
        oldProfile = oldProfile.text

        #Find all profile entries and click the edit button on the last one
        editButtons = self.browser.find_elements_by_id('edit_profile')
        editButtons[len(editButtons)-1].click()

        #Your are shown the edit page for a profile
        title = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual(title, 'New Profile Details')

        #You input new details for your profile paragraph
        detailInputBox = self.browser.find_element_by_id('id_text')
        detailInputBox.send_keys('I have changed the detail of my profile')

        submitButton = self.browser.find_element_by_id('save_button')
        submitButton.click()

        #Check if the contents on the home page has changed
        newProfile = self.browser.find_element_by_id('profile')

        self.assertNotEqual(oldProfile, newProfile.text)

    def test_can_edit_a_qualification_entry(self):
        self.signIn()
        #You are looking at the cv home page and want to edit a qualification entry
        self.browser.get('http://localhost:8000/cv/')

        #Saving contents of current qualification section
        oldQualifications = self.browser.find_element_by_id('education')
        oldQualifications = oldQualifications.text

        #Find all qualification entries and click the edit button on the last one
        editButtons = self.browser.find_elements_by_id('edit_qualification')
        editButtons[len(editButtons)-1].click()

        #You are shown the edit page for a qualification and change the description
        title = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual(title, 'New Qualification')

        detailInputBox = self.browser.find_element_by_id('id_text')
        detailInputBox.send_keys('I have changed something or other')
 
        submitButton = self.browser.find_element_by_id('save_button')
        submitButton.click()

        #Check if the qualifications section has updated
        newQualifications = self.browser.find_element_by_id('education')

        self.assertNotEqual(oldQualifications, newQualifications)  

    def test_can_edit_an_experience_entry(self):
        self.signIn()
        #You are looking at the cv home page and want to edit an experience entry
        self.browser.get('http://localhost:8000/cv/')

        #Saving contents of current experience section
        oldExperiences = self.browser.find_element_by_id('experiences')
        oldExperiences = oldExperiences.text

        #Find all experiences entries and click the edit button on the last one
        editButtons = self.browser.find_elements_by_id('edit_experience')
        editButtons[len(editButtons)-1].click()

        #You are shown the edit page for an experience and change the description
        title = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual(title, 'New Experience')

        detailInputBox = self.browser.find_element_by_id('id_text')
        detailInputBox.send_keys('I have changed something or other')
 
        submitButton = self.browser.find_element_by_id('save_button')
        submitButton.click()

        #Check if the experience section has updated
        newExperiences = self.browser.find_element_by_id('experiences')

        self.assertNotEqual(oldExperiences, newExperiences)

    def test_can_edit_an_interest_entry(self):
        self.signIn()
        #You are looking at the cv home page and want to edit an interest entry
        self.browser.get('http://localhost:8000/cv/')

        #Saving contents of current interest section
        oldInterests = self.browser.find_element_by_id('interests')
        oldInterests = oldInterests.text

        #Find all interest entries and click the edit button on the last one
        editButtons = self.browser.find_elements_by_id('edit_interest')
        editButtons[len(editButtons)-1].click()

        #You are shown the edit page for an interest and change the description
        title = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual(title, 'New Interest')

        detailInputBox = self.browser.find_element_by_id('id_text')
        detailInputBox.send_keys('I have changed something or other')
 
        submitButton = self.browser.find_element_by_id('save_button')
        submitButton.click()

        #Check if the interests section has updated
        newInterests = self.browser.find_element_by_id('interests')

        self.assertNotEqual(oldInterests, newInterests)  

    def test_can_zdelete_a_profile_entry(self):
        self.signIn()
        #You are looking at the home page of the cv and want to delete a profile entry
        self.browser.get('http://localhost:8000/cv/')

        #Saving number of profile entries before any actions taken
        profiles = self.browser.find_elements_by_id('information')
        numberOfProfiles = len(profiles)

        #You click the button to remove a post
        deleteButtons = self.browser.find_elements_by_id('remove_profile')
        deleteButtons[len(deleteButtons)-1].click()

        newProfiles = self.browser.find_elements_by_id('information')
        newNumberOfProfiles = len(newProfiles)

        self.assertEqual(numberOfProfiles-1, newNumberOfProfiles)

    def test_can_zdelete_an_education_entry(self):
        self.signIn()
        #You are looking at the home page of the cv and want to delete an education entry
        self.browser.get('http://localhost:8000/cv/')

        #Saving number of education entries before any actions taken
        qualifications = self.browser.find_elements_by_id('qualification')
        numberOfQualifications = len(qualifications)

        #You click the button to remove a qualification
        deleteButtons = self.browser.find_elements_by_id('remove_qualification')
        deleteButtons[len(deleteButtons)-1].click()

        newQualifications = self.browser.find_elements_by_id('qualification')
        newNumberOfQualifications = len(newQualifications)

        self.assertEqual(numberOfQualifications-1, newNumberOfQualifications)

    def test_can_zdelete_an_experience_entry(self):
        self.signIn()
        #You are looking at the home page of the cv and want to delete an experience entry
        self.browser.get('http://localhost:8000/cv/')

        #Saving number of experience entries before any actions taken
        experiences = self.browser.find_elements_by_id('experience')
        numberOfExperiences = len(experiences)

        #You click the button to remove an experience
        deleteButtons = self.browser.find_elements_by_id('remove_experience')
        deleteButtons[len(deleteButtons)-1].click()

        newExperiences = self.browser.find_elements_by_id('experience')
        newNumberOfExperiences = len(newExperiences)

        self.assertEqual(numberOfExperiences-1, newNumberOfExperiences)

    def test_can_zdelete_an_interest_entry(self):
        self.signIn()
        #You are looking at the home page of the cv and want to delete an interest entry
        self.browser.get('http://localhost:8000/cv/')

        #Saving number of interest entries before any actions taken
        interests = self.browser.find_elements_by_id('interest')
        numberOfInterests = len(interests)

        #You click the button to remove an interest
        deleteButtons = self.browser.find_elements_by_id('remove_interest')
        deleteButtons[len(deleteButtons)-1].click()

        newInterests = self.browser.find_elements_by_id('interest')
        newNumberOfInterests = len(newInterests)

        self.assertEqual(numberOfInterests-1, newNumberOfInterests)


if __name__ == '__main__':
    unittest.main(warnings='ignore')