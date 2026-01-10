---
title: Automation with Python – How to Build an Automated Email System for Job Applications
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-12-11T18:39:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-automated-email-system-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/automate-email-with-python.png
tags:
- name: automation
  slug: automation
- name: Python
  slug: python
seo_title: null
seo_desc: "By Jess Wilk\nWe all receive promotional emails from companies like Swiggy\
  \ and Amazon encouraging us to check out their new dish or flash sales. \nHave you\
  \ ever wondered how they manage to send emails to millions of customers? It’s impossible\
  \ to do it ..."
---

By Jess Wilk

We all receive promotional emails from companies like Swiggy and Amazon encouraging us to check out their new dish or flash sales. 

Have you ever wondered how they manage to send emails to millions of customers? It’s impossible to do it manually! Instead, they use Automated Email Systems to manage and schedule their emails efficiently. 

The best part is that you can build it quickly with open-source Python packages. Suppose you are a student or a working professional searching for a new job. Manually sending your résumé and cover letter to multiple recruiters can be time-consuming and often prone to mistakes. 

In this article, I will show how to automate sending out job applications using the Python library step-by-step with code. 

## Prerequisites

Before we dive into the process of automating email systems with Python, make sure you have a basic working knowledge of general Python concepts. 

If you’re new to Python, you can check out the [Introduction to Python](https://hyperskill.org/tracks/6) course on Hyperskill, where I contribute as an expert.

## Step 1: Set Up the Connection to Your Email Server

Smtplib is a built-in Python package. It's free to use and it lets you send out emails through any service like Gmail, Yahoo, and so on. I'll use Gmail in this example. 

The port number depends on what server you choose. We can start the connection using the package's `smtplib.SMTP` class, with the server and port as input parameters. SMTP stands for Simple Mail Transfer Protocol.

```python

    import smtplib 
   
    my_email=’jess_xxx@gmail.com’
    password_key=’xxxxx’
    
    # SMTP Server and port no for GMAIL.com
    gmail_server= "smtp.gmail.com"
    gmail_port= 587


    # Starting connection
    my_server = smtplib.SMTP(gmail_server, gmail_port)
    my_server.ehlo()
    my_server.starttls()
      
    # Login with your email and password
    my_server.login(my_email, password_key)

```

Next, to identify the client to the server, we call the `ehlo()` or extended hello method. It’s also crucial to ensure that your connection is secure and there is no information leakage. 

We can enable encryption for the connection using **Transport Layer Security** (TLS) by calling the `starttls()` method. After this, you can use the login() method with your email and password credentials.

## Step 2: Add Different Types of Content Using MIME

Your connection is ready! But before we see how to send emails to a list of people, it's crucial to understand how to attach different types of content to your email.  
  
You can send your email directly to your SMTP server if your email is a text message. But what if you want to add a link to your LinkedIn profile or a PDF of your grade card or résumé?  

Enter the MIMEMultipart. MIME stands for **Multipurpose Internet Mail Extensions**. It’s also called Multipart, which supports plain text and HTML languages. Using HTML to add your content gives flexibility in formatting and attaching images.  
  
The `MIMEMultipart` module provides a class for creating MIME documents representing a multipart message. It can include text, images, and attachments.  
  
Let’s create a `MIMEMultipart` object named _message_, as shown below. We use the alternative subtype, which includes plain text and HTML versions of the message.

```python
from email.mime.multipart import MIMEMultipart
message = MIMEMultipart("alternative")
```

### How to add text content:

The `MIMEText` module provides a class for creating MIME documents representing plain text in an email message.

```python
from email.mime.text import MIMEText


text_content= “ Hello, I am a final year student with an Mtech degree in Computer science specializing in Artificial Intelligence. I’m interested in data science roles at your organization.”


message.attach(MIMEText(text))

```

### How to add images to your email:

The `MIMEImage` module provides a class for creating MIME documents representing image data in an email message.   
  
Import the `MIMEImage` module and define the path that has your image file. Here, we read its binary data and attach it to the message object as a MIMEImage part.

```python
from email.mime.image import MIMEImage
import os


# define your location
grade_card_path = 'path/to/your/grade_card.jpg'


# Read the image from location
grade_card_img = open(grade_card, 'rb').read()


# Attach your image
message.attach(MIMEImage(grade_card_img, name=os.path.basename(grade_card_path)))

```

### How to attach files to your email:

The `MIMEApplication` module provides a class for creating MIME documents representing arbitrary binary data in an email message. It is often used for attaching files.  
  
First, define the path to an attachment file (_resume_file_), read its binary data, and attach it to the message object as a MIMEApplication part. It also sets the Content-Disposition header to specify the filename.

```python
resume_file = '...../resume.txt'


# Read the file from location
with open(resume_file, 'rb') as f:
    file = MIMEApplication(
        f.read(),
        name=os.path.basename(resume_file)
    )
    file['Content-Disposition'] = f'attachment; 


    filename="{os.path.basename(resume_file)}"'
    message.attach(file)

```

When attaching files, replace the placeholder paths with the actual ones. You can also attach a list of files using this function.

## Step 3: Send Multiple Customized Emails

I hope you are familiar with how to add different types of content to your email. Let’s gear up and start our project: automating personalized emails to job recruiters.   
  
While creating an automation system, it is essential to customize it according to specific needs. For instance, if you are a recruiter, you would prefer an email tailored to your company and you over one that simply addresses you as 'Sir/Madam.' 

To achieve this, you'll create personalized fields in your text message that receive input parameters.  
  
Create a CSV file with the information you want to personalize in different columns. For example, I have created a CSV with the Recruiter Name, Recruiter Email, Organization Name, and Job Role.

Save the CSV file as _job_contacts.csv_. Ensure that a comma separates the values and that there are no whitespaces to avoid formatting issues. Design a text message by adding personalized content using the **str.format()** function. You can use curly-bracket placeholders for the parts you want to customize.

Look at my example:

> text_content= """  
> Hello **{recruiter_name}**, I hope you are doing well. I’m Jane Doe, an engineering graduate with an Mtech in Computer Science and a specialization in Artificial Intelligence.   
>   
> I am writing to inquire regarding open roles in **{job_role}** at **{organization}**. I have experience performing data analysis and modeling through my internships and research projects. I’m excited to have an opportunity to apply my skills and learn more in the **{organization_sector}**.   
>   
> I have attached my grade card and résumé below. Looking forward to hearing from you.  
>   
> Thanks,  
> …… """

Now comes the final part. We read the CSV file and loop over each row, as shown in the below snippet. New job details are read and replaced at each step in the message, and an email is sent to the recruiter.

```python
import csv


with open("job_contacts.csv") as csv_file:
        jobs = csv.reader(csv_file)
        next(jobs)  # Skip header row
        
        for recruiter_name, recruiter_email, organization, 
        organization_sector,job_role in jobs:
            
            email_text=text_content.format(recruiter_name, recruiter_email
            Organziation, organization_sector, job_role)
            
            # Attaching the personalized text to our message
            message.attach(MIMEText(email_text))
            
            my_server.sendmail(
                from_addr= my_email,
                to_addrs=recruiter_email,
                msg=message
            )




my_server.quit()

```

Finally, we use SMTP’s `sendmail()` function with the from and to email addresses and messages as input. Don’t forget to quit the server once the process is complete.

## Tips & Best Practices

I hope you enjoyed the project. You can use this template to create an automated email system for diverse purposes like marketing campaigns, promoting your newsletter, and more. 

Here are a few recommendations to remember:

* You shouldn't store your email password in the code. Instead, prompt it through input or store it as an environment variable.
* You can create a secured SMTP connection with SSL (Secure Sockets Layer). It is an alternative to TLS we have used to provide encryption on an insecure connection.
* You can create multiple personalized email messages for different job sectors and use the most fitting one using a switch-case match.

Thank you for reading! I'm Jess, and I'm an expert at Hyperskill. You can check out an **[Introduction to Python](https://hyperskill.org/tracks/6)** course on the platform.

