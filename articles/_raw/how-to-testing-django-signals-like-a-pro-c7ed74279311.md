---
title: How to test Django Signals like a pro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-18T05:43:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-testing-django-signals-like-a-pro-c7ed74279311
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UTaOKkC0_Ha3DgqrzrcPzw.jpeg
tags:
- name: Django
  slug: django
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Haki Benita

  For a better reading experience, check out this article on my website.

  Django Signals are extremely useful for decoupling modules. They allow a low-level
  Django app to send events for other apps to handle without creating a direct depe...'
---

By Haki Benita

For a better reading experience, check out [this article on my website](https://hakibenita.com/how-to-test-django-signals-like-a-pro).

[Django Signals](https://docs.djangoproject.com/en/1.10/topics/signals/) are extremely useful for decoupling modules. They allow a low-level Django app to send events for other apps to handle without creating a direct dependency.

Signals are easy to set up, but harder to test. So In this article, I’m going to walk you through implementing a context manager for testing Django signals, step by step.

### The Use Case

Let’s say you have a payment module with a charge function. (I [write a lot about payments](https://medium.com/@hakibenita/working-with-apis-the-pythonic-way-484784ed1ce0#.ji6p00af1), so I know this use case well.) Once a charge is made, you want to increment a total charges counter.

What would that look like using signals?

First, define the signal:

```
# signals.py
```

```
from django.dispatch import Signal
```

```
charge_completed = Signal(providing_args=['total'])
```

Then send the signal when a charge completes successfully:

```
# payment.py
```

```
from .signals import charge_completed
```

```
@classmethoddef process_charge(cls, total):
```

```
    # Process charge…
```

```
    if success:        charge_completed.send_robust(            sender=cls,            total=total,        )
```

A different app, such as a summary app, can connect a handler that increments a total charges counter:

```
# summary.py
```

```
from django.dispatch import receiver
```

```
from .signals import charge_completed
```

```
@receiver(charge_completed)def increment_total_charges(sender, total, **kwargs):    total_charges += total
```

The payment module does not have to know the summary module or any other module handling completed charges. **You can add many receivers without modifying the payment module**.

For example, the following are good candidates for receivers:

* Update the transaction status.
* Send an email notification to the user.
* Update the last used date of the credit card.

### Testing Signals

Now that you got the basics covered, let’s write a test for `process_charge`. You want to make sure the signal is sent with the right arguments when a charge completes successfully.

The best way to test if a signal was sent is to connect to it:

```
# test.py
```

```
from django.test import TestCase
```

```
from .payment import chargefrom .signals import charge_completed
```

```
class TestCharge(TestCase):
```

```
    def test_should_send_signal_when_charge_succeeds(self):        self.signal_was_called = False        self.total = None
```

```
        def handler(sender, total, **kwargs):            self.signal_was_called = True            self.total = total
```

```
        charge_completed.connect(handler)
```

```
        charge(100)
```

```
        self.assertTrue(self.signal_was_called)        self.assertEqual(self.total, 100)
```

```
        charge_completed.disconnect(handler)
```

We create a handler, connect to the signal, execute the function and check the args.

We use `self` inside the handler to create a closure. If we hadn’t used `self` the handler function would update the variables in its local scope and we won’t have access to them. We will revisit this later.

Let’s add a test to **make sure the signal is not called if the charge failed**:

```
def test_should_not_send_signal_when_charge_failed(self):    self.signal_was_called = False
```

```
    def handler(sender, total, **kwargs):        self.signal_was_called = True
```

```
    charge_completed.connect(handler)
```

```
    charge(-1)
```

```
    self.assertFalse(self.signal_was_called)
```

```
    charge_completed.disconnect(handler)
```

This is working but it’s **a lot of boilerplate!** There must be a better way.

### Enter Context Manager

Let’s break down what we did so far:

1. Connect a signal to some handler.
2. Run the test code and save the arguments passed to the handler.
3. Disconnect the handler from the signal.

This pattern sounds familiar…

Let’s look at what a (file) [open context manager](https://docs.python.org/3/library/functions.html#open) does:

1. Open a file.
2. Process the file.
3. Close the file.

And a [database transaction context manager](https://docs.djangoproject.com/en/1.10/topics/db/transactions/#controlling-transactions-explicitly):

1. Open transaction.
2. Execute some operations.
3. Close transaction (commit / rollback).

It looks like **a context manager can work for signals as well**.

Before you start, think how you want to use a context manager to test signals:

```
with CatchSignal(charge_completed) as signal_args:    charge(100)
```

```
self.assertEqual(signal_args.total, 100)
```

Nice, let’s give it a try:

```
class CatchSignal:    def __init__(self, signal):        self.signal = signal        self.signal_kwargs = {}
```

```
        def handler(sender, **kwargs):            self.signal_kwrags.update(kwargs)
```

```
        self.handler = handler
```

```
    def __enter__(self):        self.signal.connect(self.handler)        return self.signal_kwrags
```

```
    def __exit__(self, exc_type, exc_value, tb):        self.signal.disconnect(self.handler)
```

What we have here:

* You initialized the context with the signal you want to “catch”.
* The context creates a handler function to save the arguments sent by the signal.
* You create closure by updating an existing object (`signal_kwargs`) on `self`.
* You connect the handler to the signal.
* Some processing is done (by the test) between `__enter__` and `__exit__`.
* You disconnect the handler from the signal.

Let’s use the context manager to test the charge function:

```
def test_should_send_signal_when_charge_succeeds(self):    with CatchSignal(charge_completed) as signal_args:        charge(100)    self.assertEqual(signal_args[‘total’], 100)
```

This is better, but **how would the negative test look like?**

```
def test_should_not_send_signal_when_charge_failed(self):    with CatchSignal(signal) as signal_args:        charge(100)    self.assertEqual(signal_args, {})
```

Yak, that’s bad.

Let’s take another look at the handler:

* We want to make sure the handler function was invoked.
* We want to test the args sent to the handler function.

Wait… **I already know this function!**

### Enter Mock

Let’s replace our handler with a Mock:

```
from unittest import mock
```

```
class CatchSignal:    def __init__(self, signal):        self.signal = signal        self.handler = mock.Mock()
```

```
    def __enter__(self):        self.signal.connect(self.handler)        return self.handler
```

```
    def __exit__(self, exc_type, exc_value, tb):        self.signal.disconnect(self.handler)
```

And the tests:

```
def test_should_send_signal_when_charge_succeeds(self):    with CatchSignal(charge_completed) as handler:        charge(100)    handler.assert_called_once_with(        total=100,        sender=mock.ANY,        signal=charge_completed,    )
```

```
def test_should_not_send_signal_when_charge_failed(self):    with CatchSignal(charge_completed) as handler:        charge(-1)        handler.assert_not_called()
```

**Much better!**

You used the mock for exactly what it should be used for, and you don’t need to worry about scope and closure.

Now that you have this working, **can you make it even better?**

### Enter contextlib

Python has a utility module for handling context managers called [contextlib](https://docs.python.org/3.6/library/contextlib.html).

Let’s rewrite our context using `contextlib`:

```
from unittest import mockfrom contextlib import contextmanager
```

```
@contextmanagerdef catch_signal(signal):    """Catch django signal and return the mocked call."""    handler = mock.Mock()    signal.connect(handler)    yield handler    signal.disconnect(handler)
```

I like this approach better because it’s easier to follow:

* The yield makes it clear where the test code is executed.
* No need to save objects on `self` because the setup code (enter and exit) are in the same scope.

And that’s it — 4 lines of code to rule them all! Profit!

