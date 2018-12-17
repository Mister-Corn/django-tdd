## Functional Test to Scope Out MVP

> Terminology:
> Functional Test == Acceptance Test == End-to-End Test
>
> What I call functional tests, some people prefer to call acceptance tests, or end-to-end tests. The main point is that these kinds of tests look at how the whole application functions, from the outside. Another term is black box test, because the test doesn’t know anything about the internals of the system under test.

Functional tests, then, mirror User Story.

Structure functional tests around User Story.

---

### Aside: Comments

Remember to write comments that explain _why_. Explaining _what_ should be done by the code itself, not by the comments around it. Use _what_ only if you're forced to keep/too lazy to refactor spaghetti-ass code, and keep _why_ comments concise and topical.

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

## Django Workflow

> Django’s main job is to decide what to do when a user asks for a particular URL on our site. Django’s workflow goes something like this:

  * An HTTP request comes in for a particular URL.
  * Django uses some rules to decide which view function should deal with the request (this is referred to as resolving the URL).
  * The view function processes the request and returns an HTTP response.

## Isn't this amount of testing excessive?

It might seem silly to test at such a degree, but considering how quickly things can get complex, having tests on each step of the complexity ladder leads to much higher confidence and easier testing than writing tests when things are already crazy.

## Don't Test Constants

> Unit tests are really about testing logic, flow control, and configuration. Making assertions about exactly what sequence of characters we have in our HTML strings isn’t doing that.

## Rendering HTML Templates

```py
# lists/views.py

from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')
```

> Instead of building our own HttpResponse, we now use the Django render function. It takes the request as its first parameter (for reasons we’ll go into later) and the name of the template to render. Django will automatically search folders called templates inside any of your apps' directories. Then it builds an HttpResponse for you, based on the content of the template.

# 5

## Cross-Site Request Forgery Protection

When using the form tag in Django's templates:

> Django’s CSRF protection involves placing a little auto-generated token into each generated form, to be able to identify POST requests as having come from the original site. So far our template has been pure HTML, and in this step we make the first use of Django’s template magic. To add the CSRF token we use a template tag, which has the curly-bracket/percent syntax, {% ... %}—famous for being the world’s most annoying two-key touch-typing combination:

## Default Values for Dicts

```py
def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
```

> We use dict.get to supply a default value, for the case where we are doing a normal GET request, so the POST dictionary is empty.

## Red/Green/Refactor Triangulation

The unit-test/code cycle:

* RED: Start by writing a unit test which fails
* GREEN: Write the simplest possible code to get it to pass. Cheat if necessary.
* REFACTOR: Refactor to get to better code that makes more sense.

> So what do we do during the Refactor stage? What justifies moving from an implementation where we "cheat" to one we’re happy with?

> One methodology is eliminate duplication: if your test uses a magic constant (like the "1:" in front of our list item), and your application code also uses it, that counts as duplication, so it justifies refactoring. Removing the magic constant from the application code usually means you have to stop cheating.

> I find that leaves things a little too vague, so I usually like to use a second technique, which is called triangulation: if your tests let you get away with writing "cheating" code that you’re not happy with, like returning a magic constant, write another test that forces you to write some better code. That’s what we’re doing when we extend the FT to check that we get a "2:" when inputting a second list item.

## Three Strikes and Refactor

Using a thing three times or more? Refactor dat.