---
title: How to Send Emails With Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-17T02:25:12.145Z'
originalURL: https://freecodecamp.org/news/how-to-send-emails-with-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744856526204/09de1f52-e08a-4b4c-a5fe-199aea652e20.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: null
seo_desc: 'If you''re building a Django app and you want to connect with users – maybe
  to welcome them, send password reset links, or deliver updates – email is one of
  the best tools you’ve got.

  Setting up email in Django might sound tricky at first, but it''s pr...'
---

If you're building a Django app and you want to connect with users – maybe to welcome them, send password reset links, or deliver updates – email is one of the best tools you’ve got.

Setting up email in Django might sound tricky at first, but it's pretty straightforward once you get the hang of it.

I’ve walked a bunch of people through it, and by the end of this guide, you’ll feel confident about sending emails from your own Django projects.

## Why Email Matters in Web Apps

Email isn’t just a nice-to-have – it's essential for communication, trust, and user experience.

Think about it:

* How do you confirm someone’s account? Email.
    
* How do you help users reset a password? Email.
    
* Want to send updates, alerts, or custom reports? You guessed it – email.
    

That’s why it’s worth setting up properly.

## What You’ll Learn in This Guide

Here’s what I’ll walk you through:

* How to set up email in Django
    
* How to choose between development and production settings
    
* How to send basic emails
    
* How to send HTML and multi-part emails
    
* How to use templates for emails
    
* Common mistakes to avoid
    

Let’s get into it.

## How to Send Emails With Django

Here is how to get started.

### Step 1: Configure Your Email Settings in Django

Django uses the `EmailMessage` class and the built-in `send_mail` function to send emails. But first, you have to tell Django how to connect to your email provider.

Open your `settings.py` file and add your email backend configuration.

Here’s an example using Gmail:

```python
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

**Important:** If you're using Gmail, you’ll need to set up App Passwords because regular account passwords won’t work with SMTP anymore.

#### For Development

If you're just testing emails locally and don’t want to actually send anything, Django makes it easy.

Use this in your `settings.py`:

```python
# Settings.oy
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This prints emails to your console instead of sending them. Perfect for debugging!

### Step 2: Sending a Simple Email

Now that your settings are in place, you can send an email with just a few lines of code.

Here’s a quick example using Django’s `send_mail` function:

```python
# Views.py or anywhere you want this logic to live

from django.core.mail import send_mail

send_mail(
    'Welcome to My Site!',
    'Thanks for signing up. Glad to have you!',
    'from@example.com',        # From
    ['to@example.com'],        # To
    fail_silently=False,
)
```

And just like that, you’ve sent an email

### Step 3: Sending HTML Emails

Plain text is okay, but HTML emails look way better. Django lets you send multi-part messages that include both plain text and HTML.

Here’s how:

```python


from django.core.mail import EmailMultiAlternatives

subject = 'Welcome!'
text_content = 'Thanks for joining us.'
html_content = '<p>Thanks for <strong>joining</strong> us.</p>'

msg = EmailMultiAlternatives(subject, text_content, 'from@example.com', ['to@example.com'])
msg.attach_alternative(html_content, "text/html")
msg.send()
```

Now, your email will look polished in modern email clients but will still work if someone’s email reader only supports plain text.

### Step 4: Use Templates for Better Emails

If you're sending emails with similar structure – like a welcome message or invoice – it makes sense to use templates.

Create a file like `welcome_email.html` in your templates folder:

```xml
<!-- templates/welcome_email.html -->
<h2>Hello {{ user.first_name }}!</h2>
<p>Welcome to our platform. We’re happy you’re here.</p>
```

Then, load and render it in your email:

```python
from django.template.loader import render_to_string

html_message = render_to_string('welcome_email.html', {'user': user})
```

You can plug this into the `EmailMultiAlternatives` setup we used above.

### Step 5: Common Pitfalls and How to Avoid Them

Here are a few things I’ve seen people run into:

1. **Incorrect app passwords**: If you’re using Gmail and it keeps failing, double-check your app password setup.
    
2. **Port and TLS confusion**: For most SMTP providers:
    
    * Use port **587** with `EMAIL_USE_TLS = True`
        
    * Or port **465** with `EMAIL_USE_SSL = True`
        
3. **Email going to spam**: Use real sender names and avoid spammy subject lines. Consider setting up SPF, DKIM, and DMARC records if you're going live. Here’s a simple guide on email authentication.
    

## How to Test Emails Without Sending Them

You can use [Mailtrap](https://mailtrap.io/) or [Papercut SMTP](https://github.com/ChangemakerStudios/Papercut-SMTP) to test emails in a sandboxed environment.

These tools catch emails in a fake inbox, so nothing gets sent to real users. Super useful when you're working on production-level templates or transactional emails.

## FAQs

### **Can I send attachments with Django emails?**

Yes! Use `msg.attach()` with `EmailMessage` or `EmailMultiAlternatives`. Here's an example:

```python
msg.attach('invoice.pdf', pdf_content, 'application/pdf')
```

### **What’s the difference between** `send_mail` and `EmailMessage`?

`send_mail` is a shortcut for simple use cases. For more complex ones – like HTML emails, attachments, or custom headers – `EmailMessage` or `EmailMultiAlternatives` is better.

### **How do I send bulk emails?**

Use the `send_mass_mail()` function or loop through a list and send emails individually. If you’re sending many emails, it’s better to use an email service provider (like SendGrid, Mailgun, and so on) that supports bulk delivery and handles rate limits.

## Conclusion

Email is one of those features that seems small until it breaks—or until you need it to shine.

Do you have it working? Great.

Still stuck? Don’t worry – it’s one of those things that gets easier every time.

### Further Resources

If you want to dive deeper into emails with Django, check out these links:

* [Official Django Email Docs](https://docs.djangoproject.com/en/stable/topics/email/)
    
* [Mailtrap Django Guide](https://mailtrap.io/blog/django-send-email/)
    
* [SendGrid Django Integration](https://www.twilio.com/docs/sendgrid/for-developers/sending-email/django)
    
* [Django Email Templates Package](https://github.com/milkpep/django-email-templates)
