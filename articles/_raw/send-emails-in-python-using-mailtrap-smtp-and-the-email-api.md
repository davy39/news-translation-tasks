---
title: How to Send Emails in Python using Mailtrap SMTP and the Email API
subtitle: ''
author: Alex Tray
co_authors: []
series: null
date: '2025-03-28T13:59:31.054Z'
originalURL: https://freecodecamp.org/news/send-emails-in-python-using-mailtrap-smtp-and-the-email-api
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743110284000/6fb2a037-ddca-4625-acfb-cffbd167ec55.png
tags:
- name: Phyton
  slug: phyton
- name: smtp
  slug: smtp
- name: mailtrap
  slug: mailtrap
- name: api
  slug: api
seo_title: null
seo_desc: "In this tutorial, I’ll walk you through the process of sending emails in\
  \ Python using two different methods: \n\nThe traditional SMTP setup with the built-in\
  \ ‘smtplib’ module. \n\nMailtrap email API via Mailtrap’s official SDK. \n\n\nIf\
  \ you’re unfamiliar wi..."
---

In this tutorial, I’ll walk you through the process of sending emails in Python using two different methods: 

1. The traditional SMTP setup with the built-in ‘smtplib’ module. 
    
2. Mailtrap email API via Mailtrap’s official SDK. 
    

If you’re unfamiliar with the tools and workflows, SMTP (Simple Mail Transfer Protocol) is the protocol commonly used for sending emails via apps and websites. Mailtrap is an email delivery platform designed for high deliverability with growth-focused features and industry-best analytics. 

By the end of the article, you’ll understand how to integrate email-sending capabilities into Python projects and use Mailtrap for reliable email delivery in real-world scenarios.

## Table of Contents

1. ['smtplib' Setup](#heading-smtplib-setup)
    
2. [How to Send emails with Mailtrap SMTP](#heading-how-to-send-emails-with-mailtrap-smtp)
    
3. [How to Send emails with the Mailtrap Email API](#heading-how-to-send-emails-with-the-mailtrap-email-api)
    
4. [Wrapping Up](#heading-wrapping-up)
    

## ‘smtplib’ Setup

To start sending emails with Python, I'll first use the built-in ‘smtplib’ module. This lets you connect to an SMTP server and send emails directly from your app. 

So, start by importing the ‘smtplib’ module with the statement below:

```python
import smtplib
```

Next, create an ‘SMTP’ object to configure the connection to your SMTP server. This object handles the email sending. 

```python
smtpObj = smtplib.SMTP(host, port)
```

* ‘host’ refers to the SMTP server endpoint, such as ‘live.smtp.mailtrap.io’
    
* ‘port’ is the communication channel used by the server. The recommended port is usually 587 for secure email sending with TLS encryption. 
    

**Pro tip**: An SMTP object has a ‘sendmail’ instance object with three parameters, where each parameter is a string (‘receivers’ is a list of strings). 

```python
smtpObj.sendmail(sender, receivers, message)
```

If you want to ensure you’ve properly imported the ‘smtplib’ module and check the full description of arguments and classes, run the following command:

```python
help(smtplib)
```

## How to Send emails with Mailtrap SMTP

This method involves setting up the custom SMTP credentials you get for Mailtrap.

**Important notes**: 

* **Testing out the service with Mailtrap’s dummy domain** – To try Mailtrap, you don’t need to verify your domain right away. You can use Mailtrap’s dummy domain (you get access to it when you sign up), which allows you to simulate sending emails without worrying about the DNS records. This is ideal for testing the service and getting familiar with Mailtrap’s features.  
    
* **Domain verification for production** – If you plan to send real emails to recipients, you’ll need to verify your domain. This involves adding DNS records such as SPF, DKIM, and [DMARC](https://dmarcreport.com/) to your domain provider’s DNS settings. These records ensure your emails are delivered successfully and help protect against phishing and spoofing. In the next section, I'll show you how to set these up in your domain provider's dashboard. 
    

### Verify your sending domain (SPF, DKIM, and DMARC)

DNS records are critical to ensure your emails are delivered successfully, and mailbox providers such as Gmail and Yahoo require DNS authentication. 

But before we go through a quick tutorial on how to do it, let’s review each type of record so you understand why they’re so important:

* **SPF (Sender Policy Framework)**: The record helps mail servers determine if the sender’s IP address is authorized to send emails from your domain. Simply, adding an SPF record prevents spammers from sending emails that appear to come from your domain. 
    
* **DKIM (DomainKeys Identified Mail)**: DKIM uses encryption to verify the sender's domain and ensures that the email content hasn't been tampered with during transmission. This protects your emails from being spoofed. 
    
* **DMARC (Domain-based Message Authentication, Reporting & Conformance)**: DMARC ties SPF and DKIM together, providing a policy for handling unauthenticated emails and reporting on email activities. In a nutshell, it gives you more control over your domain’s email security. 
    

Now, here’s how to add the records: 

1. First, you need to access your domain provider's DNS settings. Usually, you can access them in the domain register or domain settings. For example, GoDaddy calls the menu Manage DNS, and it's dubbed similarly with other providers. 
    
2. Next, add (copy-paste) the DNS records Mailtrap provides into your domain provider's DNS settings. Note that Mailtrap's records are read-made, and SPF is pre-parsed, so you don't need to create anything additional – just add the records. 
    

![Screenshot showing domain verification](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfHx2AAc87krxYh7twU5Ypuz-Iu6gklvJeVBzpdgptvfc7B9g7X3BBnqWai8n47HTDJrj1rZ2ny0jfscJJYgAAFcuEsZeVqYO2OellzvQgaXMjnMMxIeOoPGF0ildRbecEi7rjPbg?key=CJmzmKUWxlFjIw3A041wXvaj align="left")

3. Finally, you can check the status of your records with Mailtrap. 
    

Below is the bare-bones script for sending emails via Mailtrap using Python. For security reasons, the script uses placeholder credentials for the username and password (except for the SMTP server endpoint and port).

When running the script, be sure to replace these placeholders with your actual Mailtrap credentials to ensure the email is sent successfully. 

```python
import smtplib
from email.mime.text import MIMEText

# Configuration
port = 587
smtp_server = "live.smtp.mailtrap.io"
login = "api"  # Your login generated by Mailtrap
password = "1a2b3c4d5e6f7g"  # Your password generated by Mailtrap

sender_email = "mailtrap@example.com"
receiver_email = "new@example.com"

# Plain text content
text = """\
Hi,
Check out the new post on the Mailtrap blog:
SMTP Server for Testing: Cloud-based or Local?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
Feel free to let us know what content would be useful for you!
"""

# Create MIMEText object
message = MIMEText(text, "plain")
message["Subject"] = "Plain text email"
message["From"] = sender_email
message["To"] = receiver_email

# Send the email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Secure the connection
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent')
```

**In the script**:

* The ‘smtplib’ and ‘MIMEText’ modules have been imported from Python’s library. 
    
* As mentioned, SMTP server configuration needs to be updated with your credentials. But the server endpoint and port are as is. 
    
* Since this is a bare-bones script, I used ‘MIMEText’, which holds ‘plaintext’ only. But the script can be easily refactored to use ‘MIMEMultipart’ for both ‘plaintext’ and ‘HTML’. Jump to the quick tut below to see how it’s done. 
    
* When sending the email, I chose to use the ‘with’ statement (context manager) to ensure the SMTP server connection gets closed right after the email gets sent. 
    

**Security tip**: 

Server information and the login credentials shouldn't be hardcoded into your sending script. When setting the script for production, make sure you use environment variables to store sensitive information. This makes the code more secure and more flexible, particularly when you move it between different dev stages. For example ⬇️

```python
import os

smtp_server = os.getenv("SMTP_SERVER", "default.smtp.server")
login = os.getenv("SMTP_LOGIN")
password = os.getenv("SMTP_PASSWORD")

# Example usage in an SMTP connection setup
# smtp.login(login, password)
```

Note that you need to set the variables in your operating system prior to running the script. 

### Refactor the script to use HTML emails

HTML emails provide a better user experience. They allow you to include formatted text, images, tables, clickable links, and custom styling. This works great for marketing emails, newsletters, or any communication where design and branding matter. 

So, to refactor the script, you would import ‘MIMEMultipart’ and ‘MIMEText’. This action allows you to customize the HTML emails yet keep the plain-text versions as a fallback if your recipients cannot open the HTML email. 

Here’s the revised script:

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuration
smtp_server = "live.smtp.mailtrap.io"
port = 587
login = "api"  # Mailtrap login
password = "1a2b3c4d5e6f7g"  # Mailtrap password

sender_email = "mailtrap@example.com"
receiver_email = "new@example.com"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "HTML Email"

# Add plain text content (optional, for email clients that don't render HTML)
message.attach(MIMEText("This is a plain text version of the email.", "plain"))

# Add HTML content
html_content = """\
<html>
  <body>
    <h1>Welcome to Mailtrap!</h1>
    <p>This is an example of an HTML email.</p>
  </body>
</html>
"""
message.attach(MIMEText(html_content, "html"))

# Send the email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent')
```

Lastly, I’ve included video instructions for the SMTP method – so if that works better for you, feel free to check it out 🔽. 

[How to send email in Python using Mailtrap - Tutorial by Mailtrap](https://www.youtube.com/watch?v=ufLpTc9up8s&t=1s)

## How to Send emails with the Mailtrap email API

If you're looking to move beyond using SMTP for sending emails and want to integrate Mailtrap’s email API into your Python applications, this section will walk you through how to do that. 

The Mailtrap [SMTP email API](https://mailtrap.io/smtp-api/) allows you to send emails more efficiently, with added flexibility and scalability. Before starting, make sure you have a verified sending domain on Mailtrap and the Mailtrap API token, which you’ll use to authenticate requests.

**Note**: I’m covering the API integration using the official Mailtrap Python SDK. 

So, first you install the official SDK with the command below. 

```python
pip install mailtrap
```

**Prerequisite**: Ensure your Python package version is 3.6+ or higher. 

After installing the SDK, the next step is to create a Mail object. This object will represent the email you want to send, including essential details like the sender, recipient, subject, and email content. 

```python
import mailtrap as mt

# Create the mail object
mail = mt.Mail(
    sender=mt.Address(email="mailtrap@example.com", name="Mailtrap Test"),  # Sender info
    to=[mt.Address(email="your@email.com")],  # Recipient info
    subject="You are awesome!",  # Email subject
    text="Congrats for sending a test email with Mailtrap!"  # Email content (plain text)
)

# Create a client using your API key
client = mt.MailtrapClient(token="your-api-key")

# Send the email
client.send(mail)
```

**Quick notes:**

* **Sender and recipient**: You need to specify the sender’s email address, which must match your verified domain. Similarly, define the recipient's email.
    
* **Subject and text content**: Set the subject and plain text content of the email. You can also add HTML content as I'll cover later.
    
* **Client and sending**: The ‘MailtrapClient’ is initialized with your Mailtrap API token, which authenticates the API request. The ‘send’ method is then called on the client, passing the ‘mail’ object.
    

To create the client using the Mailtrap API token, take the following path within Mailtrap:  
**Settings** &gt; **API Tokens** &gt; **Add Token** 

![Add API tokens](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeLlNbf0Uiub9YYVxcfiNsZL6_uNHKfuO4dW6ZZGXWEGkF7X4mw82KMsrAWX4hA_u_jYqi1G8aoh1-vOnxKjdXKackVG8HdrsyfHulzaIJVMrMcxmZvllXcNOXVxG7hFOJXgl2VBw?key=CJmzmKUWxlFjIw3A041wXvaj align="left")

With that, you can use the following command to send emails:

```python
# create client and send
client = mt.MailtrapClient(token="your-api-key")
client.send(mail)
```

Finally, here’s the SDK script for sending a bare-bones ‘plaintext’ email via Python SDK.

```python
 from mailtrap import Mail, Address, MailtrapClient

# Create a Mail object with basic details for a plain text email
mail = Mail(
    # Specify the sender's email address and optional name
    sender=Address(email="mailtrap@example.com", name="Mailtrap Test"),
    # Specify one or more recipients; here we use a list with a single recipient
    to=[Address(email="your@email.com", name="Your Name")],
    # Subject of the email
    subject="Simple Plain Text Email",
    # The plain text content of the email
    text="This is a plain text email sent using the Mailtrap SDK. Simple and straightforward.",
    # Optional: categorize this email for easier sorting or management in the Mailtrap service
    category="Test",
    # Optional: Additional headers can be specified, but are not required for plain text emails
    headers={"X-Example-Header": "HeaderValue"}
)

# Initialize the MailtrapClient with your API token
client = MailtrapClient(token="your-api-key")

# Send the email using the client's send method
client.send(mail)

print("Plain text email sent successfully.")
```

**In the script**:

* The imported classes include ‘MailtrapClient’, ‘Mail’, and ‘Address’ because I’m sending a plain text message. 
    
* The ‘Mail’ object contains:
    
    * ‘Mail’ constructor to create the object.
        
    * ‘Sender’ which uses ‘Address’ class to define the name and email of the sender.
        
    * ‘to’ which is typically an ‘Address’ objects list, but since this is a plain text email, it usually has direct recipients instead of the list. 
        
    * ‘subject’ which is the subject of the email. 
        
    * ‘text’ which contains the email content (in ‘plaintext’)
        
    * ‘headers’ and ‘category’ which are optional fields that help better manage your emails. 
        

* The email sending flow:
    
    * ‘MailtrapClient’ gets created and authenticated via the API token. 
        
    * The ‘MailtrapClient’ ‘send’ method gets called and passes the ‘mail’ object as an email-sending argument.  
        
    * The “Plain text email sent successfully.” message gets printed to confirm the action. 
        

### Refactor the script to include HTML and attachments

Again, it’s pretty straightforward to refactor the script using the ‘MIMEMultipart’ class for more complex email structures. 

Here’s the refactored code:

```python
import mailtrap as mt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a multipart email message
message = MIMEMultipart()
message["Subject"] = "HTML Email"

# Plain text version (for email clients that don't support HTML)
message.attach(MIMEText("This is the plain text version.", "plain"))

# HTML version
html_content = """\
<html>
  <body>
    <h1>Welcome to Mailtrap!</h1>
    <p>This is an HTML email with some <b>bold text</b> and a <a href="https://example.com">link</a>.</p>
  </body>
</html>
"""
message.attach(MIMEText(html_content, "html"))

client = mt.MailtrapClient(token="your-api-key")

# Now send the email with Mailtrap's API
mail = mt.Mail(
    sender=mt.Address(email="mailtrap@example.com", name="Mailtrap Test"),
    to=[mt.Address(email="your@email.com")],
    subject="You are awesome!",
    html=message.as_string()  # Pass the HTML content as a string
)
client.send(mail)
```

### Environmental setup for production

Before I dive into the details, I’d like to remind you of security best practices:

1. **Securely store API keys and credentials**: On production, never hardcode sensitive data like API keys, email login credentials, or other secrets directly into your source code. Doing so exposes your application.
    
2. **Use environment variables**: By doing this, you can keep your credentials safe and easily switch between different configurations (like dev, staging, and production). 
    

Now, here’s how to set it all up:

1. Use the ‘python-dotenv’ package to load environment variables from a ‘.env’ file. Install the lib with the following command:
    
    ```python
    pip install python-dotenv
    ```
    

2. Create a ‘.env’ file in the root of your project to store your environment variables securely. This file will contain sensitive information, such as your Mailtrap API key, login credentials, and SMTP server details. Here’s an example:
    
    ```python
    SMTP_SERVER=smtp.mailtrap.io
    SMTP_PORT=587
    SMTP_LOGIN=your_mailtrap_login
    SMTP_PASSWORD=your_mailtrap_password
    MAILTRAP_API_KEY=your_mailtrap_api_key
    ```
    

**Important note**: Ensure this ‘.env’ file is never pushed to version control (like Git). Add it to your ‘.gitignore’ to avoid accidental exposure.

3. Once you've created your ‘.env’ file, you need to load the variables into your Python script. At the top of your script, import the ‘dotenv’ package and call ‘load\_dotenv()’ to load the environment variables.
    
    ```python
    from dotenv import load_dotenv
    import os
    
    # Load environment variables from the .env file
    load_dotenv()
    
    # Retrieve environment variables securely
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_login = os.getenv("SMTP_LOGIN")
    smtp_password = os.getenv("SMTP_PASSWORD")
    mailtrap_api_key = os.getenv("MAILTRAP_API_KEY")
    ```
    

4. With the environment variables loaded, you can replace the hardcoded credentials in the script with these environment variables. Here’s an example:
    
    ```python
    import smtplib
    from email.mime.text import MIMEText
    from dotenv import load_dotenv
    import os
    
    # Load environment variables
    load_dotenv()
    
    # Fetching SMTP credentials from environment variables
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_login = os.getenv("SMTP_LOGIN")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    sender_email = "mailtrap@example.com"
    receiver_email = "new@example.com"
    subject = "Plain text email"
    text = """\
    Hi,
    Check out the new post on the Mailtrap blog:
    https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
    """
    
    # Create MIMEText object
    message = MIMEText(text, "plain")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Send email using environment variables
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(smtp_login, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    
    print("Email sent successfully!")
    ```
    

#### Pro tips:

First, ensure your environment variables are only accessible to authorized users. On a production server, this typically means only allowing access to the environment variables through the deployment configuration (for example, through Heroku’s config vars, AWS Secrets Manager, or other cloud-based secret management tools).

Second, use different environment variables for development, staging, and production. This ensures that your production environment is isolated and secured from the rest of your development process.

Once your environment variables are configured locally, deploy your application to a production environment. Make sure to set the same environment variables in your production server or service.

If you're deploying to platforms like Heroku, AWS, or Google Cloud, you can use their environment variable management tools to securely store and access your secrets without having to manage a ‘.env’ file manually.

## Wrapping up

This quick tutorial provides more than enough to get started with sending emails in Python. And note that the scripts featured above can be extended to include HTML, multiple recipients, attachments, images, and so on. 

If you’re interested in that and more security tips and best practices, you can check out the Mailtrap blog for more detailed tutorials.
