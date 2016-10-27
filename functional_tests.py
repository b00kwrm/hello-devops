from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_get_hello_world(self):
        # Edith goes to the homepage.  
        self.browser.get('http://localhost:8000')

        # She notices the title page mentions hello world.
        self.assertIn('hello world', self.browser.title)
        #self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
