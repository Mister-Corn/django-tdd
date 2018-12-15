## Functional Test to Scope Out MVP

> Terminology:
> Functional Test == Acceptance Test == End-to-End Test
>
> What I call functional tests, some people prefer to call acceptance tests, or end-to-end tests. The main point is that these kinds of tests look at how the whole application functions, from the outside. Another term is black box test, because the test doesn’t know anything about the internals of the system under test.

Functional tests, then, mirror User Story.

Structure functional tests around User Story.

---

### Aside: Comments

Remember to write comments that explain _why_. Explaining _what_ should be done by the code itself, not by the comments around it. Use _what_ only if you're forced/too lazy to refactor spaghetti-ass code, and keep _why_ comments concise and topical.

> When I first started at Resolver, I used to virtuously pepper my code with nice descriptive comments. My colleagues said to me: “Harry, we have a word for comments. We call them lies.” I was shocked! But I learned in school that comments are good practice?

> They were exaggerating for effect. There is definitely a place for comments that add context and intention. But their point was that it’s pointless to write a comment that just repeats what you’re doing with the code:

```
# increment wibble by 1
wibble += 1
```

> Not only is it pointless, but there’s a danger that you’ll forget to update the comments when you update the code, and they end up being misleading. The ideal is to strive to make your code so readable, to use such good variable names and function names, and to structure it so well that you no longer need any comments to explain what the code is doing. Just a few here and there to explain why.

> There are other places where comments are very useful. We’ll see that Django uses them a lot in the files it generates for us to use as a way of suggesting helpful bits of its API. And, of course, we use comments to explain the User Story in our functional tests—​by forcing us to make a coherent story out of the test, it makes sure we’re always testing from the point of view of the user.

---

## Testing Process

Remember

1. Write tests first
2. Test for failure
3. Write code to pass test
4. Test again

We test before we even write the code so that we can have some assurance we're testing the right thing. (e.g. _if tests pass before you even wrote anything, good sign tests are bad_)

## Breakdown of `NewVistorTest`

```python
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
```

Use a class to represent the test. All methods starting with `test` will be run. `setUp` is run before test, whereas `tearDown` is run after test.

```python
if __name__ == '__main__':
  unittest.main()
```

Python script checks if it’s been executed from the command line, rather than just imported by another script). We call `unittest.main()`, which launches the unittest test runner, which will automatically find test classes and methods in the file and run them.

## Unit Tests

Unit tests test a particular function of code. Another way of looking at it:

> Unit tests test the application from the inside, from the point of view of the programmer.