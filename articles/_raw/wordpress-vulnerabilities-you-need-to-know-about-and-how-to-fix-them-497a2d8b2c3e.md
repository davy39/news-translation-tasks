---
title: WordPress vulnerabilities you need to know about — and how to fix them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T17:30:27.000Z'
originalURL: https://freecodecamp.org/news/wordpress-vulnerabilities-you-need-to-know-about-and-how-to-fix-them-497a2d8b2c3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZjOP68Ue2tyBjLPZS4Nz1g.jpeg
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: 'By Joel S. Syder

  WordPress is an incredibly useful and versatile platform for all kinds of blogging.
  It’s become very popular. Unfortunately, that popularity has brought with it quite
  a few vulnerabilities that can be exploited by hackers. It’s impor...'
---

By Joel S. Syder

WordPress is an incredibly useful and versatile platform for all kinds of blogging. It’s become very popular. Unfortunately, that popularity has brought with it quite a few vulnerabilities that can be exploited by hackers. It’s important that you know about these weaknesses and take measures to prevent their exploitation. Here are six WordPress vulnerabilities you need to know about.

#### **WordPress login**

“The easiest way for someone to access your WordPress is by attacking your login. These kinds of brute force attacks are the most common way of having your WordPress compromised. “This method works by guessing your login and password over and over again by using certain software,” advises Martha Goss, WP programmer at [WriteMyX](https://writemyx.com/) and [BritStudent](https://britstudent.com/).

WordPress doesn’t limit the number of login attempts, so brute force attacks can be very effective. Your best defense against this vulnerability is installing a plugin that will limit the number of allowed login attempts, such as iThemes Security Pro. You can also use a password manager to generate random passwords that are much less likely to be guessed. Stay away from passwords that seem obvious — don’t use anything like 123456, password, or anything related to you.

For example, no pet names, children names, partner names, street names and so on since all of this can be used against you. If you think that mixing them together may prove to be a better security measure but still fairly easy to remember, think again. Your social media profiles are an easy way into your psychology, and anyone could find these passwords among your posts.

It’s best to choose something unrelated to you — and make sure that you use a good combination of letters, upper case letters, and numbers as well as symbols. You can never be too careful or underestimate your enemy.

Source: [https://www.wordfence.com/blog/2017/12/aggressive-brute-force-wordpress-attack/](https://www.wordfence.com/blog/2017/12/aggressive-brute-force-wordpress-attack/)

#### **Default admin user account**

Hackers can gain access to the back end of your WordPress account by exploiting your default admin user account. Try deleting your admin account and accessing your site from a common account that has admin privileges. People can gain access by injecting SQL commands using a cookie value parameter. To prevent this kind of compromise, try updating your security software to the most current IPS.

Jibu Pro can also be accessed by cross-site scripting because it doesn’t clear out user-supplied input properly. To guard against this vulnerability, strengthen the permissions on your site. You can even go as far as to hide your admin login so well that no one can find it. The best way to do that — and the simplest one by far — is naming it something else. Admin is quite obvious, and hackers will be searching for that. But if you name it something entirely different — Cat, SpaceMonkey or choose from a wide variety of funny and clever possibilities — the hackers will have a hard time finding it. By default, they will have a much harder time injecting an SQL command — they don’t know where to inject it.

Source: [https://www.acunetix.com/blog/articles/exploiting-sql-injection-example/](https://www.acunetix.com/blog/articles/exploiting-sql-injection-example/)

#### **URL hacking**

“WordPress uses PHP to execute all its server-side scripts, and that, unfortunately, makes it susceptible to URL attacks. It is all too easy for hackers to sneak into WordPress operations and create problems for you,” warns Dorothy Cox, tech writer at [1Day2Write](https://1day2write.com/). Because of the nature of its database, there is ample opportunity for hackers to steal your sensitive information. To avoid these breaches, host your WordPress on Apache Web Server, which uses .htaccess files and will protect you from URL hacking.

Make sure you uninstall and delete all of the unnecessary plugins that you have on your website. This limits the access points for the hackers — themes could also be your enemy, especially if you have a ton of them that you aren’t using. PHP is all too easy to exploit, and you should protect your website the best you can. As a bonus, those themes and extra plugins may be slowing your loading time down so you would be improving your SEO while protecting your website.

Source: [https://blog.websecurify.com/2017/02/hacking-wordpress-4-7-0-1.html](https://blog.websecurify.com/2017/02/hacking-wordpress-4-7-0-1.html)

#### **Out of date software**

Any time you’re running your WordPress using outdated software, you run an increased risk of being compromised. It’s easy to fall into the trap of thinking that updates just improve minor bugs and annoyances, but they also are important for the security patches they include.

Keeping your software updated is a very easy thing to do, and it will protect you from many hacking threats. If you’re worried, you will forget to update your software, simply install automatic updates with plugins such as iThemes’ WordPress version management. These kinds of features both save you time and ensure you don’t miss a security patch and have your site compromised.

Hackers will be looking for something that’s easy to crack. By updating, you are probably installing new security patches which can prevent any hacker from entering. Also, make sure that you don’t install anything from sources that are not safe. You could be inviting the hackers right in.

Source: [https://www.kimiweb.com/wordpress-help/updating-wordpress-and-plugins/](https://www.kimiweb.com/wordpress-help/updating-wordpress-and-plugins/)

#### **Default prefix for database tables**

There are many tables in the WordPress database, and in many installs, they are named with a default prefix beginning with “_wp_.” That may not sound like a big deal, but it gives hackers a bit of an advantage because it is one less thing for them to decipher.

You can make things a lot more difficult for them by simply changing these default prefixes. Will it stop every hacker? No, but it will stop a lot, and it’s just one more useful tool in defending your WordPress account. This is a simple process that you can easily do on your own — hackers are always looking for an easy entry point first, and if you eliminate those, they might give up.

Source: [https://www.cloudways.com/blog/change-wordpress-database-table-prefix-manually/](https://www.cloudways.com/blog/change-wordpress-database-table-prefix-manually/)

#### **PHP vulnerabilities**

Hackers can gain access to your account by exploiting your PHP code, and it’s more common than you would think. Limit your risk by uninstalling and then deleting any plugins you don’t need. Each one is a potential access point for people looking to compromise your information. Try and avoid using plugins that aren’t being updated anymore; if it’s been more than six months since an update, it’s time to consider just deleting it.

Source: [https://www.cloudways.com/blog/change-wordpress-database-table-prefix-manually/](https://www.cloudways.com/blog/change-wordpress-database-table-prefix-manually/)

#### **Switch to better hosting**

When you are just starting out, the cheapest hosting seems like the best idea. But, cheap hosting also comes with a lack of security features that could be harmful. Make sure that you have the best and the safest hosting in order to protect yourself and your customers.

Source: [https://www.webhostingsecretrevealed.net/blog/web-hosting-guides/switching-web-host/](https://www.webhostingsecretrevealed.net/blog/web-hosting-guides/switching-web-host/)

#### **Conclusion**

Keeping your site secure is one of the most important responsibilities when you’re running a WordPress account. Limit the number of tries for your login. Change the default prefixes for your tables. Download the plugins recommended in this article and see how they work for you. WordPress is a great resource for blogging, but just remember that there are plenty of people looking around the site for accounts vulnerable to hacking. Make sure yours isn’t one of them.

_Joel Syder is WP coach at [Originwritings.com](https://originwritings.com/) and [Australia2write.com](https://australia2write.com/). He enjoys helping people to build websites of their dreams as well as creating articles about things that excite him for [Academicbrits.com](https://academicbrits.com/), tutoring service._

