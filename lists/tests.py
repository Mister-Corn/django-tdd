from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

  # def test_bad_maths(self):
  #   """
  #   Silly test to check tests are working.
  #   """
  #   self.assertEqual(1 + 1, 3)

  # def test_root_url_resolves_to_home_page_view(self):
  #   found = resolve('/')
  #   self.assertEqual(found.func, home_page)
  # The above test is no longer necessary if using Django Test Client

  def test_home_page_returns_correct_html(self):
    # While the below works, we are testing constants, which is pointless
    # request = HttpRequest()
    # response = home_page(request)
    # html = response.content.decode('utf8')
    # We should test structure with templates instead
    # self.assertTrue(html.startswith('<html>'))
    # self.assertIn('<title>To-Do Lists</title>', html)
    # self.assertTrue(html.endswith('</html>'))
    response = self.client.get('/')

    # Checks what template was used to generate response
    # It will only work for responses that were retrieved by the test client
    self.assertTemplateUsed(response, 'home.html')
