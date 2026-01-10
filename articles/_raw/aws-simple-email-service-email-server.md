---
title: How to use Amazon Simple Email Service (SES) to replace your server-based email
  server
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-03-02T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/aws-simple-email-service-email-server
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/email_square.svg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: email
  slug: email
- name: servers
  slug: servers
seo_title: null
seo_desc: "One fine day, for no discernible reason, my Ubuntu 18.04 business server\
  \ stopped forwarding mail to my Gmail address. \nJust the day before, the .forward\
  \ files I'd created in the home directories of the local server accounts I use for\
  \ email - like /ho..."
---

One fine day, for no discernible reason, my Ubuntu 18.04 [business server](https://bootstrap-it.com) stopped forwarding mail to my Gmail address. 

Just the day before, the .forward files I'd created in the home directories of the local server accounts I use for email - like /home/office/.forward - were cheerfully redirecting all the mail aimed at my business addresses to my daily-use Gmail account. And then they suddenly stopped.

When I noticed something was wrong, I immediately consulted my server logs. /var/log/mail.err was spitting out charming messages that included things like:

```
status=deferred (delivery temporarily suspended: connect to alt2.gmail-smtp-in.l.google.com[219.8.202.27]:25: Connection timed out)
```

Checking the server mailboxes told me that mail was coming in, but that Postfix couldn't establish a connection to Gmail to forward messages to my address.

Naturally I restarted Postfix, but that didn't help.

```
sudo systemctl restart postfix
```

I confirmed that there was nothing blocking outgoing messages from leaving my server on port 25 (SMTP). Then I checked to make sure my domain hadn't somehow been blacklisted (there are [numerous](https://mxtoolbox.com/domain) online [tools](https://www.ultratools.com/tools/emailTest) that'll do that for you), and peeked at the state of my MX records by running dig from the command line:

```
dig MX bootstrap-it.com
```

Nothing doing. Everything seemed to check out.

After a few frustrating troubleshooting sessions I gave up and figured I'd try something completely different. 

Being an AWS solutions architect and having co-authored two books for Wiley/Sybex on AWS (one a [guide to the Cloud Practitioners exam](https://www.amazon.com/gp/product/1119490707/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1119490707&linkCode=as2&tag=projemun-20&linkId=c407a50c1752a2bc7d9ff3ea66ac8cdc) and one for the [Solutions Architect Associate exam](https://www.amazon.com/Certified-Solutions-Architect-Study-Guide/dp/111950421X/ref=as_sl_pc_tf_til?tag=projemun-20&linkCode=w00&linkId=7c57304cbc082e8d089c86fda94aad7c&creativeASIN=111950421X)), shouldn't I be willing and able to build my own stack of AWS tools that'll handle my email server needs in the cloud?

Well it turns out that I was both willing and - after some serious research and trial and error - able. Getting it done would require:

* Creating an S3 bucket where incoming emails will be stored.
* Creating a Simple Notification Service (SNS) topic to email me a notice every time a new email arrives.
* Configuring Amazon's Simple Email Service (SES) to take over my email domain (bootstrap-it.com) and handle incoming mail. That involves adding an MX record to Route 53 (where my domains are managed) and pointing SES to my domain; adding and verifying each email address I want SES to control; and then telling SES to send new messages to my S3 bucket while also triggering an alert for the SNS topic.
* Assuming you will also want to _send_ email messages through the service, it's also a good idea to configure SES to sign your outgoing messages using DomainKeys Identified Mail (DKIM).

I'm not going to describe all those steps in detail here. There's plenty of [excellent documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html) available for that. But I will briefly mention some pain points you might encounter.

You'll have to add an MX record to your DNS hosted zone for each domain you're using. Even if your domains are managed within Amazon's Route 53, you'll need to provide a value for your record. 

What you use for that value will depend on the AWS region where your SES resource is located. In my case, it looked like this:

```
10 inbound-smtp.us-east-1.amazonaws.com
```

The SNS notifications will arrive in a single long string of text containing just a couple of short morsels of useful but hard-to-read information. That'll be enough to identify spam, but you'll usually need more information than what you'll find here. I use the notifications as a heads-up telling me that there's new mail in my S3 bucket.

Viewing the emails themselves within your S3 bucket via the AWS Management Console isn't the end of the world if it only happens once or twice a month. But if they're coming in faster than that, you'll need to find a better way to access and read your messages. 

However, creating a protocol for automating that process is really a local operating system problem that requires an entirely different set of tools. I solved the problem for myself using the AWS CLI and a cool Bash script. If you'd like to see how I did that, [click through to this article](https://www.freecodecamp.org/news/bash-script-download-view-from-s3-bucket/).

_There's much more administration goodness in the form of books, courses, and articles available at my [bootstrap-it.com](https://bootstrap-it.com)._ 

