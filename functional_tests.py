from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    
  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Some schmo wants a to-do list web app. I don't know why
    # They open their browser to get there
    self.browser.get('http://localhost:8000')

    # Page title tells schmo they're in the right place
    # structure: assertion to test, message when test fails
    # OLD: assert 'To-Do' in browser.title, "Browser title was " + browser.title
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

    # Schmo is invited to enter a to-do item straight away

    # Schmo types "Get a life" into a text box

    # Schmo hits enter, the page updates, and the page lists
    # "1: Get a life" as an item in the to-do list

    # The text box persists, ever hungry for more inane tasks for 
    # schmo to keep track of. Schmo enters another tasks:
    # "Made dat money"

    # Page updates again, and now shows both items in the list

    # Schmo notices site has generated a unique url

    # Schmo visits the URL, and sees the to-do list persisting

    # OK cool

if __name__ == '__main__':
  unittest.main()