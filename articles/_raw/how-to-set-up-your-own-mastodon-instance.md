---
title: How to Set Up Your Own Mastodon Instance
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2022-11-11T16:29:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-your-own-mastodon-instance
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-14-at-4.49.55-PM.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: mastadon
  slug: mastadon
- name: social media
  slug: social-media
seo_title: null
seo_desc: "Mastodon is a decentralized, federated social media platform based on the\
  \ ActivityPub protocol. It allows you to follow and interact with friends across\
  \ multiple instances. \nIn this article, you will learn how freeCodeCamp set up\
  \ our own Mastodon ins..."
---

Mastodon is a decentralized, federated social media platform based on the [ActivityPub](https://www.w3.org/TR/activitypub/) protocol. It allows you to follow and interact with friends across multiple instances. 

In this article, you will learn how freeCodeCamp set up our own Mastodon instance - and how you can too.

## What is Mastodon?

Imagine if there were multiple different websites for Twitter. On each of those websites, you could create an account (create one on all of them, if you were feeling ambitious). 

You could then use your account to follow any of your friends on any of the other websites. You could repost their content to your account, and see activity from all of your followed accounts on a single timeline.

While Mastodon is by far the most popular platform to use, there are also other options such as [Misskey](https://github.com/misskey-dev/misskey), [Pleroma](https://git.pleroma.social/pleroma/pleroma), and their various forks. 

Some of these platforms will be able to federate with each other, with cross-platform capabilities, while others will not.

## Getting Started with Mastadon

There are a couple of things you will need to get started with the process we followed for freeCodeCamp:

* A [DigitalOcean](https://digitalocean.com) account
* A DNS provider (we use [Cloudflare](https://cloudflare.com)).

Begin by logging in to DigitalOcean and creating a new droplet. In the image options, select the marketplace tab. Then, search for the Mastodon image - this will handle a good portion of the setup for you.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-48.png)

Configure the rest of the droplet settings to your own needs - for the size, we began with the $12 option with the plan to scale up as necessary.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-49.png)

Once the droplet has finished provisioning, copy the IP address. Set up an A record for your domain or subdomain to point to your droplet - **do this BEFORE you SSH into the droplet**.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-50.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-52.png)

Once your DNS is ready, SSH into the droplet as the `root` user.

## How to Set Up Your Mastadon Instance

When you first SSH into the server, the automatic setup tool will run.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-54.png)

Follow the prompts:

* For `Domain name`, enter the new domain/subdomain record you just set up.
* The tool will ask if you want to store user-uploaded files on the cloud. If you do, you'll need to provide credentials for a storage provider such as Amazon S3.
* Mastodon requires an SMTP server for email notifications and the registration flow. You can either spin up your own, or provide credentials for a service like [SendGrid](https://sendgrid.com).
* The SMTP flow will prompt you to send a test email. This is _highly recommended_, as this will confirm your SMTP settings are correct. If they are not, the setup wizard will prompt you to re-enter them.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-55.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-67.png)

You will next create a Mastodon account to serve as the administrator. This can be your personal account, or it can be a shared account among your team.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-68.png)

Finally, you'll be prompted to enter your email for LetsEncrypt certificate renewal notifications.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-57.png)

After a few minutes, your instance should be up and running.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-61.png)

## How to Configure Your Mastadon Instance

Visiting your new domain/subdomain should display the Mastodon landing page.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-58.png)

Sign in using the admin credentials you generated earlier. Then, select `Preferences` on the right sidebar, followed by `Administration` -> `Site Settings` on the left.

Here you can configure the basic information related to your instance, and upload your branding assets.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-59.png)

These will be displayed on your instance's `/about` page, shown to users when they register/login (and available in the footer).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-66.png)

When you are ready to start accepting user sign-ups, change the `Registration mode` setting to either `Anyone can sign up` or `Approval required for sign up`.

## How to Manage Users

Under the `Moderation` -> `Accounts` tab in the settings, you can see registered and pending users.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-63.png)

If you click on a username, you will be taken to the user management view.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-65.png)

From this screen, you can manage their permission level (that is, grant moderation or admin status), check IP information, and block email domains. 

Your moderation team can also leave private notes (only visible to the team) on a user account, to help keep a history of any moderation concerns.

## Conclusion

Now that your instance is up and running, feel free to poke around the settings and interaction options. For more information on the various options, check out the [official documentation](https://docs.joinmastodon.org/).

You can find the freeCodeCamp core team and volunteer moderators on [our private instance](https://social.freecodecamp.org), where you can follow us from the instance you just created.

Enjoy your new platform, and happy coding!

_Cover image from Mastodon's [branding update page](https://blog.joinmastodon.org/2022/06/mastodon-branding-updates/)._

