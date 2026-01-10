---
title: Send Emails Using Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-07T16:14:20.000Z'
originalURL: https://freecodecamp.org/news/send-emails-using-code-4fcea9df63f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qTKddOEkMZiri9ldfzBauQ.jpeg
tags:
- name: marketing
  slug: marketing
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Arjun Krishna Babu

  As a learning exercise, I recently dug into Python 3 to see how I could fire off
  a bunch of emails. There may be more straightforward methods of doing this in a
  production environment, but the following worked well for me.

  So, h...'
---

By Arjun Krishna Babu

As a learning exercise, I recently dug into Python 3 to see how I could fire off a bunch of emails. There may be more straightforward methods of doing this in a production environment, but the following worked well for me.

So, here’s a scenario: You have the names and email addresses of a bunch of contacts. And you want to send a message to each one of those contacts, while adding a _“Dear [name]”_ at the top of the message.

For simplicity’s sake you can store the contact details in a file rather than a database. You can also store the template of the message you wish to send in a file.

The [smtplib](https://docs.python.org/3/library/smtplib.html) module of Python is basically all you need to send simple emails, without any subject line or such additional information. But for _real_ emails, you do need a subject line and lots of information — maybe even pictures and attachments.

This is where Python’s [email package](https://docs.python.org/3/library/email.html) comes in. Keep in mind that it’s not possible to send an email message using the `email` package alone. You need a combination of both `email` and `smtplib`.

Be sure to check out the comprehensive official documentation for both of these.

Here are four basic steps for sending emails using Python:

1. Set up the SMTP server and log into your account.
2. Create the `MIMEMultipart` message object and load it with appropriate headers for `From`, `To`, and `Subject` fields.
3. Add your message body.
4. Send the message using the SMTP server object.

Now let me walk you through the whole process.

Let’s say you have a contacts file `mycontacts.txt` as follows:

```bash
user@computer ~ $ cat mycontacts.txt
john johndoe@example.com
katie katie2016@example.com
```

Each line represents a single contact. We have the name followed by the email address. I’m storing everything in lowercase. I’ll leave it to the programming logic to convert any fields to upper-case or sentence-case if necessary. All of that is pretty easy in Python.

Next, we have the message template file `message.txt`.

```bash
user@computer ~ $ cat message.txt 

Dear ${PERSON_NAME}, 

This is a test message. 
Have a great weekend! 

Yours Truly
```

Notice the word “`${PERSON_NAME}`”? That is a [template string](https://docs.python.org/3.5/library/string.html#template-strings) in Python. Template strings can easily be replaced with other strings; in this example, `${PERSON_NAME}` is going to be replaced with the actual name of the person, as you’ll see shortly.

Now let’s start with the Python code. First up, we need to read the contacts from the `mycontacts.txt` file. We might as well generalize this bit into its own function.

```py
# Function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
```

The function `get_contacts()` takes a filename as its argument. It will open the file, read each line (i.e., each contact), split it into name and email, and then append them into two separate lists. Finally, the two lists are returned from the function.

We also need a function to read in a template file (like `message.txt`) and return a `Template` object made from its contents.

```py
from string import Template

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
```

Just like the previous function, this one takes a filename as its argument.

To send the email, you need to make use of [SMTP (Simple Mail Transfer Protocol)](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol). As mentioned earlier, Python provides libraries to handle this task.

```py
# import the smtplib module. It should be included in Python by default
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
```

In the above code snippet, you’re importing the `smtplib` and then creating an [SMTP instance](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP) that encapsulates an SMTP connection. It takes as parameter the host address and a port number, both of which entirely depends on the SMPT settings of your particular email service provider. For instance, in the case of Outlook, line 4 above would instead be:

```py
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
```

You should use the host address and port number of your particular email service provider for the whole thing to work.

`MY_ADDRESS` and `PASSWORD` above are two variables that holds the full email address and password of the account you’re going to use.

Now would be a good time to fetch the contact information and the message templates using the functions we defined above.

```py
names, emails = get_contacts('mycontacts.txt')  # read contacts
message_template = read_template('message.txt')
```

Now, for each of those contacts, let’s send the mail separately.

```py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# For each contact, send the email:
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="This is TEST"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    
    del msg
```

For each `name` and `email` (from the contacts file), you’re creating a [MIMEMultipart](https://docs.python.org/3/library/email.mime.html#email.mime.multipart.MIMEMultipart) object, setting up the `From`, `To`, `Subject` content-type headers as a keyword dictionary, and then attaching the message body to the `MIMEMultipart` object as plain text. You might want to read the documentation to find out more about other MIME types you can experiment with.

Also note that on line 10 above, I’m replacing `${PERSON_NAME}` with the actual name extracted from the contacts file using the [templating mechanism in Python](https://docs.python.org/3.5/library/string.html#template-strings).

In this particular example I’m deleting the `MIMEMultipart` object and re-creating it each time you iterate through the loop.

Once that is done, you can send the message using the handy [send_message()](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.send_message) function of the SMTP object you created earlier.

Here’s the full code:

```py
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'my_address@example.comm'
PASSWORD = 'mypassword'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()
```

There you go! I believe the code is now fairly clear.

Feel free to copy and tweak it as necessary.

Apart from the official Python docs, I would also like to mention [this resource](http://naelshiab.com/tutorial-send-email-python/) which helped me a lot.

Happy coding :)

_I originally published this article [here](https://arjunkrishnababu96.gitlab.io/post/send-emails-using-code/). If you liked this article, please hit the small heart below. Thanks!_

