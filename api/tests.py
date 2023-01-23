from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random
import string


# Create your tests here.
class PlacardTest(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(TodoFormTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TodoFormTest, self).tearDown()

    def test_sign_up(self):
        self.selenium.get('http://127.0.0.1:8000/user/register')

        username = self.selenium.find_element_by_id('id_username')
        email = self.selenium.find_element_by_id('id_email')
        password = self.selenium.find_element_by_id('id_password')
        password2 = self.selenium.find_element_by_id('id_password2')

        submit = self.selenium.find_element_by_id('submit_button')

        username.send_keys('user-test')
        email.send_keys('user-test@test.com')
        password.send_keys('password12345')
        password2.send_keys('password12345')

        submit.send_keys(Keys.RETURN)

        self.selenium.get('http://localhost:8000/user/user_profile/')

        assert 'user-test' in self.selenium.page_source

    def test_sign_in(self):
        self.selenium.get('http://127.0.0.1/user/login')

        username = self.selenium.find_element_by_id('id_username')
        password = self.selenium.find_element_by_id('id_password')

        submit = self.selenium.find_element_by_id('submit_button')

        username.send_keys('user-test')
        password.send_keys('password12345')

        submit.send_keys(Keys.RETURN)

        self.selenium.get('http://localhost:8000/user/user_profile/')

        assert 'user-test' in self.selenium.page_source
    
    def test_create_post(self):
        self.selenium.get('http://localhost:8000/api/createpost')

        title = self.selenium.find_element_by_id('id_title')
        contact_info = self.selenium.find_element_by_id('id_contact_info')
        price = self.selenium.find_element_by_id('id_price')
        desc = self.selenium.find_element_by_id('description-input')

        submit = self.selenium.find_element_by_id('submit_button')

        title.send_keys('test title')
        contact_info.send_keys('+123456789')
        price.send_keys('100')
        desc.send_keys('test description')

        submit.send_keys(Keys.RETURN)

        self.selenium.get('http://localhost:8000/api/list')

        assert 'test title' in self.selenium.page_source

