---
title: How to Change the Password of a Superuser in Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-23T13:59:23.545Z'
originalURL: https://freecodecamp.org/news/how-to-change-the-password-of-a-superuser-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745416742960/89cce35f-2e91-4329-8fea-0d1551bea2c7.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
- name: Security
  slug: security
seo_title: null
seo_desc: 'Changing a superuser password in Django might sound like a big task, but
  it’s one of the easiest things to do once you know how.

  If you’re working on a Django project – whether it’s a hobby blog, a client’s website,
  or a bigger web application – mana...'
---

Changing a superuser password in Django might sound like a big task, but it’s one of the easiest things to do once you know how.

If you’re working on a Django project – whether it’s a hobby blog, a client’s website, or a bigger web application – managing your admin accounts safely is a must.

And one key part of that? Making sure your superuser password is strong, secure, and easy for *you* to update.

You might be doing this because you forgot the old password, you're handing the project off to someone else, or you're tightening security after a team change.

Whatever your reason is, this guide will walk you through the easiest and safest ways to change a superuser password in Django.

I’ll break everything down in simple language, no heavy tech lingo or assumptions.

Let’s dive in.

### What we’ll cover:

* [Why Changing the Superuser Password Matters](#heading-why-changing-the-superuser-password-matters)
    
* [3 Simple Ways to Change a Django Superuser Password](#heading-3-simple-ways-to-change-a-django-superuser-password)
    
    * [Method 1: Use Django’s Built-In Command](#heading-method-1-use-djangos-built-in-command)
        
    * [Method 2: Use the Django Shell](#heading-method-2-use-the-django-shell)
        
    * [Method 3: Use Django Admin (If You’re Logged In)](#heading-method-3-use-django-admin-if-youre-logged-in)
        
* [Bonus: Forgot Your Superuser Username?](#heading-bonus-forgot-your-superuser-username)
    
* [FAQs](#heading-faqs)
    
    * [What if I forgot both the username and password?](#heading-what-if-i-forgot-both-the-username-and-password)
        
    * [Will this log out other users?](#heading-will-this-log-out-other-users)
        
    * [Can I change the password from the database directly?](#heading-can-i-change-the-password-from-the-database-directly)
        
    * [How do I know if my new password is secure?](#heading-how-do-i-know-if-my-new-password-is-secure)
        
* [Final Thoughts](#heading-final-thoughts)
    
* [Further Reading and Tools](#heading-further-reading-and-tools)
    

## Why Changing the Superuser Password Matters

Your Django superuser has full access to the admin dashboard. This means they can add or delete users, edit data, manage settings – everything. If that account gets compromised, the whole site is at risk.

Here’s what could go wrong if the password is weak or outdated:

* Someone could delete your database.
    
* A hacker could inject malicious data.
    
* Private user info could be exposed.
    

According to [Verizon’s Data Breach Investigations Report](https://www.verizon.com/business/en-sg/resources/articles/analyzing-covid-19-data-breach-landscape/), over **80%** of hacking-related breaches are due to compromised or weak passwords. That’s a huge risk for something that’s easy to fix in a few minutes.

So let’s make sure your Django admin is locked down tight – without breaking anything.

## 3 Simple Ways to Change a Django Superuser Password

I’ll show you three different ways to update your superuser password. You only need to pick one that fits your current setup.

### Method 1: Use Django’s Built-In Command

If you have access to the command line and your project’s virtual environment, this is the cleanest way.

#### **Activate your virtual environment**

This depends on your setup, but if you're using `venv` it might look like this:

```bash
source venv/bin/activate
```

Or on Windows:

```python
venv\Scripts\activate
```

#### **Navigate to your project folder**

This is where `manage.py` lives:

```bash
cd your_project_folder
```

#### **Run the following command:**

```bash
python manage.py changepassword your_superuser_username
```

Example:

```bash
python manage.py changepassword admin
```

Django will then ask you to enter a new password. Type it in, hit enter, confirm it again, and you’re done.

That’s it. You just changed your superuser password!

### Method 2: Use the Django Shell

Maybe you don’t remember the username or want more control. The Django shell lets you interact directly with your database using Python.

Here’s how:

First, open the shell:

```bash
python manage.py shell
```

Then run the following code:

```python
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.get(username="admin")  # Replace 'admin' with your username
user.set_password("new_secure_password")   # Replace with your new password
user.save()
```

Now exit the shell:

```python
exit()
```

That’s it. This method is especially helpful if you’re working in a staging environment or doing things programmatically.

### Method 3: Use Django Admin (If You’re Logged In)

This one only works if you can still log in with the current superuser account.

1. Go to your Django admin page, usually at `http://127.0.0.1:8000/admin/`.
    
2. Log in with your current credentials.
    
3. Click on **Users**.
    
4. Find your superuser account and click on it.
    
5. Scroll down to the “Password” section and click **"this form"** under the "Raw passwords are not stored..." message.
    
6. Enter your new password twice and save.
    

This method is super quick and doesn’t require any code at all.

## Bonus: Forgot Your Superuser Username?

If you don’t remember the exact username of your superuser, no worries. You can list all users like this:

```bash
python manage.py shell
```

Then:

```python
from django.contrib.auth import get_user_model

User = get_user_model()

for user in User.objects.all():
    print(user.username)
```

This will print out all usernames in your system, including your superuser.

## FAQs

### **What if I forgot both the username and password?**

Use the shell method above to list all usernames, then reset it using either the shell or the `changepassword` command.

### **Will this log out other users?**

Changing your superuser password won’t affect other users unless you have custom logic tied to sessions. For most projects, everything else keeps running just fine.

### **Can I change the password from the database directly?**

Technically yes, but **don’t do it**. Passwords in Django are hashed using PBKDF2 by default. If you enter something manually in the database, it won’t work unless it's hashed the right way. Always use the Django shell or admin panel instead.

### **How do I know if my new password is secure?**

Django checks password strength by default. But if you want to be extra safe, use a tool like [Bitwarden Password Generator](https://bitwarden.com/password-generator/) or [1Password’s Generator](https://1password.com/password-generator/).

## Final Thoughts

That’s pretty much everything you need to know to change your superuser password in Django. It’s quick, safe, and once you’ve done it once, it’ll be second nature.

It’s small actions like this that go a long way in keeping your Django projects secure. And since it only takes a minute or two, there’s no reason to put it off.

Let’s keep the conversation going, Connect with me on [x.com/\_udemezue](http://X.com/_udemezue)

### Further Reading and Tools

* [Official Django change password documentation](https://docs.djangoproject.com/en/stable/ref/django-admin/#changepassword)
    
* [How Django stores passwords securely](https://docs.djangoproject.com/en/stable/topics/auth/passwords/)
    
* [PBKDF2 explained on OWASP](https://owasp.org/www-community/vulnerabilities/Using_Insufficiently_Random_Values)
