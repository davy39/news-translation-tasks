---
title: What Makes Code Vulnerable – And How to Fix It
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-04-21T16:59:21.428Z'
originalURL: https://freecodecamp.org/news/what-makes-code-vulnerable-and-how-to-fix-it
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745251285687/7ce5aca0-1edc-49e4-879d-b5690cbb64ea.png
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: vulnerability
  slug: vulnerability
- name: coding
  slug: coding
- name: Validation
  slug: validation
seo_title: null
seo_desc: 'Writing code is relatively easy. But writing secure code is much harder.

  The truth is, most developers don’t realize their code is vulnerable until something
  breaks. Or, worse, until someone attacks it. So if you want secure code, you first
  have to k...'
---

Writing code is relatively easy. But writing secure code is much harder.

The truth is, most developers don’t realize their code is vulnerable until something breaks. Or, worse, until someone attacks it. So if you want secure code, you first have to know what bad code looks like.

In this tutorial, we’ll see 10 clear signs that your code might be vulnerable to attacks. And more importantly, how to fix it.

### Here’s what we’ll cover:

* [1\. Hardcoded Credentials](#heading-1-hardcoded-credentials)
    
* [2\. No Input Validation](#heading-2-no-input-validation)
    
* [3\. Poor Error Handling](#heading-3-poor-error-handling)
    
* [4\. Outdated Dependencies](#heading-4-outdated-dependencies)
    
* [5\. No Authentication or Weak Authentication](#heading-5-no-authentication-or-weak-authentication)
    
* [6\. Missing Authorization Checks](#heading-6-missing-authorization-checks)
    
* [7\. Exposed Sensitive Data in URLs](#heading-7-exposed-sensitive-data-in-urls)
    
* [8\. No Rate Limiting](#heading-8-no-rate-limiting)
    
* [9\. Unsafe File Uploads](#heading-9-unsafe-file-uploads)
    
* [10\. Missing HTTPS](#heading-10-missing-https)
    
* [Final Thoughts](#heading-final-thoughts)
    

## **1\. Hardcoded Credentials**

This one is *everywhere*. Maybe you’ve seen it yourself – an API key sitting right there in the code. A database password written in plain text.

It looks like this:

```plaintext
DB_PASSWORD = "supersecret123"
API_KEY = "sk_test_abc123"
```

If this code leaks (and it will), attackers can do whatever they want. They can log into your systems, steal your data, or run up huge bills on cloud services – all without breaking a sweat.

And here’s the scary part: this kind of leak doesn’t just happen when your whole project gets hacked. It can happen when someone pushes code to GitHub and forgets to add `.env` to `.gitignore`. Boom – your secret keys are now public.

### **How to Protect Against It**

Never hardcode sensitive data like API keys, database passwords, or tokens. Instead, use environment variables.

These are hidden from the source code and can be safely managed per environment (dev, test, production). For example, a `.env` file imported into your codebase:

```plaintext
import os
db_password = os.getenv("DB_PASSWORD")
```

## **2\. No Input Validation**

If you trust user input, you’re already in trouble. Attackers love sending weird stuff, like super long strings, funky characters, or unexpected formats.

Here’s what it looks like:

```plaintext
username = request.GET['username']
print("Hello " + username)
```

Now someone enters:

```plaintext
username=Robert'); DROP TABLE users; --
```

**Boom.** You’ve just been SQL injected. Your database table? Gone.

Without validation, your app can break or even be hijacked. Bad input can lead to issues like SQL injection, cross-site scripting (XSS), and general bugs.

Basically, you’re giving attackers a blank check.

### **How to Protect Against It**

Make sure you validate all inputs. For example:

```plaintext
import re
email = request.GET.get('email')
if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    return "Invalid email format"
```

Use parameterized queries. Never build SQL strings from raw user input:

```plaintext
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
```

And use strict data types. Don’t just assume input is clean. Make it pass a test.Limit input length. No one needs a 5,000-character username.Escape special characters especially if you’re using input in HTML or SQL.

## **3\. Poor Error Handling**

This is what lazy error handling looks like:

```plaintext
except Exception as e:
    print(e)  # Exposes internal errors to the user
```

Or worse:

```plaintext
except:
    pass  # Silently swallows all errors
```

In the first example, the error is fully displayed to the user. The second example ignores all errors.

Silent errors are dangerous. And showing full error messages to users? That’s handing over a map to your system.

Imagine a database error pops up in production, and your app spits out something like:

```plaintext
psycopg2.OperationalError: could not connect to server: Connection refused
```

Great – now attackers know what database you’re using, and they might start poking around.

### **How to Protect Against It**

* **Log detailed errors** – but do it securely. Use logging tools or services, and don’t store logs where users can see them.
    
* **Show users simple messages** like:  
    `"Oops! Something went wrong. Please try again later."`  
    That’s all they need to know.
    
* **Never expose stack traces in production.** Turn off debug mode and use proper error pages.
    
* **Handle specific exceptions** where possible, so you know exactly what failed and why.
    

Example:

```plaintext
try:
    process_data()
except ValueError as e:
    logger.error(f"Data error: {e}")
    return "Invalid input. Please check your data."
except Exception as e:
    logger.exception("Unexpected error")
    return "Something went wrong. Try again later."
```

Use error monitoring tools like Sentry, Rollbar, or LogRocket. They catch errors, track them, and help you fix them – before users even notice.

## **4\. Outdated Dependencies**

Using old packages is like leaving your front door wide open. Attackers know exactly where the weak spots are – and they actively scan for them.

If your `package.json` or `requirements.txt` file hasn’t changed in years, that’s a red flag.

### **How to Protect Against It**

* **Update regularly.** New versions often patch security flaws.
    
* **Audit your dependencies.** Use tools like `npm audit` and `pip-audit` based on your codebase.
    
* **Automate updates** with tools like Dependabot, Renovate, or PyUp.
    

```plaintext
pip-audit
# or
npm audit
```

Even small packages can have big impacts. Stay updated, stay safe.

## **5\. No Authentication or Weak Authentication**

If your app lets anyone in without verifying who they are, that’s game over. Weak logins are just as dangerous.

Common mistakes include:

* **No password complexity rules** – Weak passwords like “123456” or “password” can be cracked in seconds using brute-force or dictionary attacks.
    
* **Storing passwords in plain text** – If your database is ever breached, all user credentials are exposed instantly, leading to massive data leaks and account takeovers.
    
* **No account lockout after repeated failed logins** – Without a limit on login attempts, attackers can keep guessing passwords endlessly using automated tools.
    

### **How to Protect Against It**

First, you can hash passwords using strong algorithms like `bcrypt`.

Here’s an example in Python:

```plaintext
import bcrypt
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
```

You can also enforce strong password policies (min length, symbols, and so on) and use multi-factor authentication (MFA) if available for extra protection.

A few extra lines of code can stop a full-blown breach.

## **6\. Missing Authorization Checks**

Authentication checks *who you are*. Authorization checks *what you can do*. Skipping the second one is like giving everyone admin access.

Example:

```plaintext
@app.route('/user/<id>')
def get_user(id):
    return User.query.get(id)
```

Here, there’s no check to see if the current user is allowed to view that data.

### **How to Protect Against It**

```plaintext
@app.route('/user/<id>')
@login_required
def get_user(id):
    if current_user.id != int(id):
        return "Unauthorized", 403
    return User.query.get(id)
```

In the above code, a login is required and the user is verified before giving them access to the data.

* Always verify ownership and roles before showing or modifying data.
    
* Implement access control rules across your API and frontend.
    
* Don’t trust IDs from the frontend – verify on the backend too.
    

## **7\. Exposed Sensitive Data in URLs**

Ever seen a password reset link like this?

```plaintext
https://example.com/reset-password?token=abcd1234
```

Looks harmless – but it’s not. Tokens, session IDs, and API keys **should never be in URLs**. They get saved in:

* Browser history
    
* Server logs
    
* Analytics tools
    

### **How to Protect Against It**

Make sure you only send sensitive data in POST requests or headers, like this:

```plaintext
POST /reset-password
Authorization: Bearer abcd1234
```

## **8\. No Rate Limiting**

Rate limiting is a security technique that controls how many times a user (or system) can make a request to your server within a given time frame – for example, no more than 10 login attempts per minute.

Without rate limits,

* An attacker can make 1,000 login attempts in a minute
    
* Your server may crash under fake requests
    

### **How to Protect Against It**

Set a max request limit per IP or user. You can use tools like Cloudflare or inbuilt tools in programming languages to do this. For example, in Python, we can use flask\_limiter.

```plaintext
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(app, key_func=get_remote_address)

@app.route("/login")
@limiter.limit("5 per minute")
def login():
    # login logic
```

In the above code, the login attempts are limited to 5 per minute. Stop abuse before it starts.

## **9\. Unsafe File Uploads**

Letting users upload files? Cool. But if you’re not careful, they can:

* Upload malware
    
* Overwrite key files
    
* Execute scripts on your server
    

Here’s an example of a common mistake:

```plaintext
file. Save(f"/uploads/{file.filename}")
```

Any type of file could be uploaded this way.

### **How to Protect Against It**

To start, you can rename files before saving:

```plaintext
pythonCopyEditimport uuid
filename = str(uuid.uuid4()) + ".jpg"
```

You can check content type (not just file extension):

```plaintext
pythonCopyEditif file.content_type not in ["image/jpeg", "image/png"]:
    return "Invalid file type"
```

You also can store files outside public directory, and finally limit file size in your server config and backend code

## **10\. Missing HTTPS**

If your app still uses plain old HTTP, all data travels in the open – including:

* Passwords
    
* Tokens
    
* Personal info
    

Attackers can sniff it all with tools like [Wireshark](https://www.freecodecamp.org/news/learn-wireshark-computer-networking/).

### **How to Protect Against It**

To start, you can use HTTPS everywhere and get a free SSL cert from [Let’s Encrypt](https://letsencrypt.org/).

You can also redirect insecure traffic – here’s how you’d do it in Flask, for example:

```plaintext
@app.before_request
def before_request():
    if not request.is_secure:
        return redirect(request.url.replace("http://", "https://"))
```

Encrypting traffic is not optional – it’s table stakes for modern apps.

## **Final Thoughts**

Writing secure code isn’t about being perfect. It’s about being careful. Slow down. Look at your code with fresh eyes. Think like an attacker. Plan for failure before it happens.

The best security isn’t patched in later – it’s baked in from the start.

For more cybersecurity tutorials, [join my newsletter](https://newsletter.stealthsecurity.sh/). New to cybersecurity? Check out my [Security Starter Course](https://start.stealthsecurity.sh/).
