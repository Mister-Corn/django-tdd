from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    
  def tearDown(self):
    self.browser.quit()
  
  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text, [row.text for row in rows])

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Some schmo wants a to-do list web app. I don't know why
    # They open their browser to get there
    self.browser.get('http://localhost:8000')

    # Page title tells schmo they're in the right place
    # structure: assertion to test, message when test fails
    # OLD: assert 'To-Do' in browser.title, "Browser title was " + browser.title
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # Schmo is invited to enter a to-do item straight away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
    )

    # Schmo types "Get a life" into a text box
    inputbox.send_keys('Get a life')

    # Schmo hits enter, the page updates, and the page lists
    # "1: Get a life" as an item in the to-do list
    inputbox.send_keys(Keys.ENTER)
    time.sleep(2)
    self.check_for_row_in_list_table('1: Get a life')

    # The text box persists, ever hungry for more inane tasks for 
    # schmo to keep track of. Schmo enters another tasks:
    # "Made dat money"
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Make dat money')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(2)

    # Page updates again, and now shows both items in the list
    self.check_for_row_in_list_table('1: Get a life')
    self.check_for_row_in_list_table('2: Make dat money')

    # Schmo notices site has generated a unique url
    self.fail('Test ain\'t finished, bruh')

    # Schmo visits the URL, and sees the to-do list persisting

    # OK cool

if __name__ == '__main__':
  unittest.main()