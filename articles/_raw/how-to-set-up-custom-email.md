---
title: How to Set Up a Custom Email with Cloudflare and Mailgun
subtitle: ''
author: San B
co_authors: []
series: null
date: '2024-04-15T13:49:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-custom-email
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/boolfalse-gmail-manage-custom-email.png
tags:
- name: cloudflare
  slug: cloudflare
- name: email
  slug: email
seo_title: null
seo_desc: 'As a software engineer, you may consider having a professional email account
  along with your own website, like "info@example.com". But this may cost a certain
  amount that you''ll not be willing to pay.

  But do you know you can do it for free? There is ...'
---

As a software engineer, you may consider having a professional email account along with your own website, like "_info@example.com_". But this may cost a certain amount that you'll not be willing to pay.

But do you know you can do it for free? There is actually a way to do it, and besides the fact that having the professional email account is free, it will help you be more efficient, reliable and secure in your daily work.

In this article, you'll learn how to create and set up your own email address using Cloudflare and Mailgun to manage emails in Gmail. This means that you can send and receive emails directly in your Gmail inbox.

I've done this already for personal use and have taken screenshots of the entire process that you'll see in this article. So I'll share all the necessary steps you need to follow to set up your own email.

Let's figure out what you need to have before you start, what you are going to do, and how it will work.

## What you need to have before you start

I assume that you already have a domain, let's call it "_yourdomain.com_". Specifically, you need to have accessibility to connect your domain with Cloudflare and setup DNS records there. A classic example of that is having a domain on some domain registrar (like GoDaddy, Namecheap), and adding your domain to Cloudflare by setting DNS records provided by Cloudflare on your domain registrar account.

Adding a domain to Cloudflare involves updating your domain's DNS nameservers to point to Cloudflare's nameservers. Once the domain is added, Cloudflare acts as an intermediary for web traffic, providing security features like DDoS protection, firewall, and SSL encryption, as well as performance enhancements through caching and content optimization.

If you haven't done that yet, here's the official [video on YouTube](https://www.youtube.com/watch?v=7hY3gp_-9EU) on how to connect your domain to Cloudflare.

Additionally, Cloudflare manages DNS records for your domain, allowing you to control how traffic is routed and ensuring reliable delivery of services like email.  
So, our work in this article will be focusing exactly on that: how to setup your domain on Cloudflare Email.

[Cloudflare Email](https://blog.cloudflare.com/email-routing-leaves-beta/) has been one of the services of Cloudflare since 2021, which can be used for free (as of now, at least).

The second assumption is that you have Gmail account, and you have access to its email settings. Simply, if you just have a regular "_youremail@gmail.com_" email, which isn't under the control of any administrator, then you have nothing to worry about. We'll explore and work on email settings later on.

## What you are going to do

In simple words, you're going to create a custom email like "_something@yourdomain.com_", which you can use to send and receive emails using Gmail's platform. So you will be receiving and reading emails sent to "_something@yourdomain.com_" in Gmail, as well as sending emails from that custom email using Gmail.

You'll use Cloudflare Email for the email routing, and Mailgun's SMTP server for sending emails.

## How it will work

When composing an email from Gmail with the sender set as "_something@yourdomain.com_", Gmail utilizes Mailgun's SMTP server through the provided credentials, transmitting the email. Mailgun then processes the message and forwards it to the recipient's email server, likely involving DNS lookups to find the recipient's server.

Emails sent to "_something@yourdomain.com_" are received by Cloudflare's email servers, configured via MX records in the domain's DNS settings. Cloudflare stores the received emails in the associated account, accessible through Gmail, which periodically connects to Cloudflare's servers (using IMAP or POP3 protocols) to retrieve new messages, enabling seamless access to incoming emails.

## Email Routing on Cloudflare

> Cloudflare Email Routing is designed to simplify the way you create and manage email addresses, without needing to keep an eye on additional mailboxes. With Email Routing, you can create any number of custom email addresses to use in situations where you do not want to share your primary email address, such as when you subscribe to a new service or newsletter. Emails are then routed to your preferred email inbox, without you ever having to expose your primary email address. ([Cloudflare Docs](https://developers.cloudflare.com/email-routing/))

Sign in to your Cloudflare account and navigate to the Dashboard.  
Choose and click on the desired website. For me it's "_boolfalse.com_", as I want to create a custom email like "_email@boolfalse.com_".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/01-dashboard.png)
_Cloudflare: Websites_

Navigate to **Email Routing** for the selected website.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/02-email-routing.png)
_Cloudflare: Email Routing_

If you don't have email routing configured, you may see something similar to the screenshot above. Click "Get started". You may be able to create your own address to receive emails and take action.

We'll skip this without creating our own address because we'll do it manually.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/03-skip-custom-address.png)
_Cloudflare: Custom Email_

By default, email routing is disabled, so you need to enable it. Click the link to navigate to the **Email Routing** page.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/04-enable-email-routing.png)
_Cloudflare: Email Routing_

Submit it by clicking "Enable Email Routing".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/05-email-dns-records-enable-email-routing.png)
_Cloudflare: Enable Email Routing_

You need to have three MX and one TXT records:

* Type: _**MX**_; Name: _**@**_; Mail Server: _**route1.mx.cloudflare.net**_; TTL: **_Auto_**; Priority: _**69**_
* Type: _**MX**_; Name: _**@**_; Mail Server: _**route2.mx.cloudflare.net**_; TTL: **_Auto_**; Priority: **_99_**
* Type: _**MX**_; Name: **_@_**; Mail Server: _**route3.mx.cloudflare.net**_; TTL: **_Auto_**; Priority: **_40_**
* Type: _**TXT**_; Name: _**@**_; TTL: **_Auto_**; Content: **_v=spf1 include:_spf.mx.cloudflare.net ~all_**

You can see them at the bottom of the **Email Routing** page.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/06-required-dns-records.png)
_Cloudflare: DNS records for Email Routing_

So, as already said, in the left menu, go to "DNS" -> "Records" and add the following records there.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/06-dns-records-added-2.png)
_Cloudflare: DNS records added_

After creating these records, go to the **Email Routing** page again.

Here, you only need to have the records you just created. So if you have any other records, just delete them.

For example, I already had an unnecessary entry there that I should delete.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/07-unnecessary-dns-records.png)
_Cloudflare: existing records for Email Routing_

Submit to delete existing unnecessary records.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/08-delete-existing-dns-records.png)
_Cloudflare: deleting unnecessary records_

After removing unnecessary DNS records, you will see only the ones you need there.

You will now be able to enable email routing by clicking the "Add records and enable" button.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/09-enabling-email-routing.png)
_Cloudflare: Enable Email Routing_

After enabling it you should see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/10-email-routing-enabled.png)
_Cloudflare: Email DNS records configured_

## How to Create a Custom Email on Cloudflare

Now go to the **Routes** tab and create an email by clicking the "Create address" button.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/11-email-routing-routes-tab.png)
_Cloudflare: Email Routing (enabled)_

In this example, we'll create "_email@boolfalse.com_" email address, by adding "_email_" as a custom address, and a destination email address, where I'll be able to receive emails.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/12-creating-email-address.png)
_Cloudflare: Email Routing_

You should see a notification about that.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/13-email-address-created.png)
_Cloudflare: creating a custom email_

You should also get an email for confirming this action.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/14-getting-confirmation-email.png)
_Verifying the destination email_

Go on and verify the email address.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/15-verify-email-address.png)
_Verify email address_

Once you've verified the email address, you may get this page:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/16-email-address-verified.png)
_Cloudflare: custom email address is verified_

You will probably get an email that you've verified your domain with Mailgun:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/36-mailgun-domain-verified-2.png)
_Notification about custom email address verification_

## How to Receive Emails in the Custom Email

Now, your email address is activated, and you can see that here:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/17-email-address-activated.png)
_Cloudflare: custom email address is active_

At this point you can send emails to the custom email you just set up. In this case, it's "_email@boolfalse.com_".

Below is a test email sent from a different email.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/18-test-email-sending-1.png)
_Testing email receiving_

You'll receive a test email to the custom email.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/19-test-email-received.png)
_Test email has been received_

## Mailgun: Adding New Domain

You can now successfully receive emails, but you can't send emails from that custom email yet.

So, it's time to switch to the mail service provider. In our case, it will be [Mailgun](https://www.mailgun.com/).  
To do this, you just need to register and attach the card to your Mailgun account. After activating your account with the card attached, you can set up a domain for your email.

You don't have to worry about the card, because Mailgun does not charge for limited quantities. I think the amount it gives is quite suitable for a free package.  
You can find the price packages in detail [here](https://www.mailgun.com/pricing/).

Go to **Sending** -> **Domains** page, and click the "Add New Domain" button.

In our case it will be "_mg.boolfalse.com_", as Mailgun recommends that to be able to send emails from your root domain, that is: "_email@boolfalse.com_".

You should see that recommendation on the right in below image:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/24-mailgun-adding-domain.png)
_Mailgun: create a new domain_

You can also select the domain region and DCIM key length, but you can leave everything as default.  
I will leave DCIM key length as 1024 and "US" as a domain region.

After creating the domain, you may be shown some tips on how to verify your domain.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/23-add-new-domain-2.png)
_Mailgun: adding a new domain_

Mailgun will give you two TXT records, two MX records and one CNAME record to add to your provider.

* Type: _**TXT**_; Name: _**mailto._domainkey.mg.boolfalse.com**_; TTL: **_Auto_**; Content: **_<SECRET>_**
* Type: _**TXT**_; Name: _**mg.boolfalse.com**_; TTL: **_Auto_**; Content: **_v=spf1 include:mailgun.org ~all_**
* Type: _**MX**_; Name: _**mg.boolfalse.com**_; Mail Server: _**mxa.mailgun.org**_; TTL: **_Auto_**; Priority: _**10**_
* Type: _**MX**_; Name **_mg.boolfalse.com_**; Mail Server: _**mxb.mailgun.org**_; TTL: **_Auto_**; Priority: **_10_**
* Type: **_CNAME_**; Name: **_email_**; Target: **_mailgun.org_**; TTL: **_Auto_**; Proxy Status: **_On_**

In our case, we will add them to Cloudflare.

Below is the first TXT record:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/27-mailgun-dns-record-1-new.png)
_Mailgun: first TXT record for a new domain_

Below is the second TXT record:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/29-mailgun-dns-record-2-new.png)
_Mailgun: second TXT record for a new domain_

Below is the first MX record:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/30-mailgun-dns-record-3.png)
_Mailgun: first MX record for a new domain_

Below is the second MX record:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/31-mailgun-dns-record-4.png)
_Mailgun: second MX record for a new domain_

After you've added two TXT and two MX records, you can check and verify them by clicking the "Verify DNS Records" button.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/32-mailgun-checking-dns-records.png)
_Mailgun: checking TXT and MX records for a new domain_

Lastly, add CNAME record.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/33-mailgun-dns-record-5-2.png)
_Mailgun: adding CNAME record for a new domain_

You may see a warning icon on the left of the CNAME record. You don't need to worry about that. Here's what [official documentation](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages) says about it:

> If you recently [added your domain](https://developers.cloudflare.com/fundamentals/setup/manage-domains/add-site/) to Cloudflare - meaning that your zone is in a [pending state](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/) - you can often ignore this warning.  
> Once most domains becomes **Active**, Cloudflare will automatically issue a Universal SSL certificate, which will provide SSL/TLS coverage and remove the warning message.

After adding a CNAME record, you can check and verify it again by clicking the second "Verify DNS Records" button.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/34-mailgun-checking-dns-records.png)
_Mailgun: checking CNAME record for a new domain_

If you have added all 5 records on the Cloudflare successfully, after clicking the verifying button, Mailgun will automatically redirect you to the **Overview** page.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/36-mailgun-verified-1.png)
_Mailgun: 2 TXT, 2 MX and 1 CNAME records added for a new domain_

It means you're ready to add a Sending API key on Mailgun.

## Mailgun: Sending API key & SMPT User

Go to **Sending** -> **Domain Settings** page. Choose the **Sending API keys** tab at the top. You probably won't see any API keys there. You just need to create a new Sending API key. 

Click "Add sending key" from the top right corner, and in the pop-up, fill the name of the key you're about to create.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/37-mailgun-create-sending-api-key-1.png)
_Mailgun: creating a Sending API key_

After pressing "Create sending key", you'll get the secret API key that you need to copy and save somewhere safe. After saving the key, you can just close the pop-up.

You should see the created key listed:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/38-mailgun-sending-api-key-created.png)
_Mailgun: Sending API key created_

You also need to create a new SMTP user in the Mailgun dashbaord.  
Go to **Sending** -> **Domain Settings** page. Choose the **SMTP credentials** tab at the top and click the "Add new SMTP user" button on the top left corner. It will open up a pop-up. 

Type user credentials there. In our case I'll create a user with the name "email". It will be like a login for your email on Gmail.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/41-mailgun-create-smtp-user.png)
_Mailgun: creating SMTP user_

Once you create an SMTP user in Mailgun, you'll see it listed and a password for that user will be generated automatically. To get this password, copy it by clicking the "Copy" button in the pop-up notification in the lower right corner.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/42-mailgun-smtp-user-created.png)
_Mailgun: SMTP user created_

Keep this in a safe place for future use. You will need this login and password to authenticate on Gmail.

You are now ready to set up email configurations with your email provider. In our case, we will do this in Gmail.

Open your Gmail account in your desktop browser and go to Settings by clicking the settings icon in the top right corner and click the "See all settings" button.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/39-gmail-settings-page.png)
_Mailgun: new domain is verified_

## Gmail Authentication with Mailgun SMTP Server

In the Gmail settings page choose the **Accounts and Import** tab and click on the "Add another email address" from the "Send mail as" section:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/40-gmail-add-another-email-2.png)
_Gmail: Settings_

It will open a pop-up for the authentication. Use the login and the password you just got by creating an SMTP user on Mailgun. Make sure to fill out the credentials correctly.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/43-gmail-add-smtp-user.png)
_Gmail: authenticate a new user using a created SMTP server on Mailgun_

Submit the form by clicking the "Add Account" button. It'll probably ask you to save the username/password in your browser. It's up to you.

And the last important thing here: it'll ask you to verify adding an account.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/44-gmail-verify-account.png)
_Gmail: authentication confirmation for a new user_

For the verification, the confirmation email will be sent to your primary email.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/45-gmail-confirmation-code.png)
_Gmail: authentication verification email_

You can either use the confirmation code to verify it using the pop-up window or simply follow the link provided in the confirmation email.

In this case, we'll click on a link which will open the page, where you'll be asked to confirm. Click on "Confirm" and simply close the previously opened pop-up window without worrying.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/47-gmail-adding-user-confirmed.png)
_Gmail: verifying the authentication_

Now you're ready to send and receive emails from the custom email you just created.

For sending an email from the custom email, you just need to choose that email as a sender email:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/49-gmail-send-emails-from-custom-email.png)
_Gmail: sending emails_

**That's it!**

An additional thing that may be useful to you is that you can set the custom email address you just created as the default address for sending emails from Gmail.

You can set this on the settings page in the "Send mail as" section:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/48-gmail-another-email-default.png)
_Gmail: Settings (default sender)_

I hope this guide will be a good resource for setting up your custom email.

## **Conclusion**

In this article, you learned how to set up your own email to manage emails in Gmail using Cloudflare Email and Mailgun.

In conclusion, it is worth noting that the choice of tools is not mandatory, other tools can be used instead, but the basic idea and logic will be similar.

You can check out my website at: [**boolfalse.com**](https://boolfalse.com/)

Feel free to share this article. 😇

