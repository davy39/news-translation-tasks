---
title: How to Secure an Existing WordPress Site in Six Easy Steps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-29T20:02:51.000Z'
originalURL: https://freecodecamp.org/news/secure-wordpress-site-six-steps
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/wordpress-site-security-tips.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: "By Andrej Kovacevic\nIf you're looking to build a flexible website these\
  \ days, there's a good chance you're going to use a content management system (CMS).\
  \ And WordPress is, by far, the most popular one. \nAt last count, WordPress powered\
  \ about 40% of ..."
---

By Andrej Kovacevic

If you're looking to build a flexible website these days, there's a good chance you're going to use a content management system (CMS). And WordPress is, by far, the most popular one. 

At last count, WordPress powered about [40% of all websites on the internet](https://w3techs.com/technologies/overview/content_management). So that means if you're a web programmer, you're likely going to encounter WordPress at some point in the course of your work.

But because WordPress is so widely used, any programmer working with it has to take great care to harden it against external attacks. And those attacks continue to multiply. In a single incident last year alone, almost [a million websites were attacked](https://www.helpnetsecurity.com/2020/05/06/wordpress-extensive-attacks/) in a single month.

The trouble is, no two WordPress sites are built in the same way, which means there's an infinite number of potential vulnerabilities to watch out for. And when you add 3rd-party plugins into the mix, it becomes impossible to mount a perfect website defense. 

But there are some things you can do that will harden a WordPress site against attacks that will stop all but the most sophisticated threats. Here are six security steps to take on every WordPress site you work with.

## Step One: Update WordPress to the Latest Version

Since WordPress is a piece of software, it's critical to keep it updated to patch vulnerabilities as they're identified. But a shocking number of developers and site owners neglect to do so. 

Recent data indicates that as many as 70% of known WordPress installations [still use versions with known vulnerabilities](https://www.wpwhitesecurity.com/statistics-70-percent-wordpress-installations-vulnerable/).

Although you'd think that this information would set off alarm bells all over the internet, the problem persists. Some of it is due to businesses being unwilling to pay for professional help to complete the work. And some of it is because certain sites rely on legacy plugins that won't work with newer WordPress versions.

But any developer that works on such a site is asking for trouble. So, you'd be better off insisting on a site update whenever you encounter an outdated WordPress installation. 

If you take the time to share some of the threat statistics with the site's owner, they'll see the light eventually. Just make sure to do a complete site backup before making any changes.

If something goes wrong and pages break or plugins fail, you'll create a bigger problem than you solve. According to [Vudu Digital](https://vududigital.co.uk/), this is a problem many developers encounter, and it causes real-world harm. They've said,

> _"We've had to clean up after failed WordPress upgrades that led to disabled pages due to site breakage. When that happens, those pages can fall off of search indexes quite fast, so rolling back the changes in a hurry is essential."_

## Step Two: Remove Unused Plugins and Update the Rest

Just like a core WordPress installation, plugins also suffer from vulnerabilities that developers patch from time to time. And WordPress is unusually dependent on plugins to provide all kinds of functionality. 

For example, when I worked recently on the website of a local [plumbing business](https://www.yourchoiceplumbers.com.au/), I was surprised to see which plugins were in use, given the relative simplicity of the site.

But the best way to minimize the potential attack surface is to first work to remove any redundant or disused site plugins before bothering to look for available updates. That will simplify the ongoing maintenance tasks and cut down on the potential for vulnerabilities. 

Only once that's done should you check the remaining plugins for their update status.

After applying available updates, don't assume that all is well. Check to see if any of the remaining plugins haven't had updates in some time, and try to figure out why. 

If you find that a plugin developer has either vanished or discontinued a plugin, look for an actively maintained replacement. The longer a plugin goes without any development activity, the greater the odds that it will become a security problem.

## Step Three: Minimize User Permissions and Secure Logins

Even if the WordPress site you're working on contains no known vulnerabilities, that doesn't mean it's safe. This is because [brute force credential attacks](https://www.malcare.com/blog/wordpress-brute-force/) are the most common way that hackers gain unauthorized access to WordPress websites. And the best way to prevent damage from those is to review user permissions and password policies.

First, try to narrow down how many accounts have administrator-level access. It's not uncommon for small businesses to designate almost everyone as an administrator, but that's an enormous risk. 

So, review every account and assign the lowest permission level possible from the built-in access groups:

* **Super Administrators** – WordPress super-users. Try to limit these to a maximum of two.
* **Administrators** – This is the highest general-user permission. Again, try to keep these to a minimum.
* **Editor** – For users that need to control and make changes to all posted articles.
* **Author** – A user that can only publish and change things in their own name.
* **Contributor –** Can add, but not publish articles in their own name.
* **Subscriber –** Cannot make site changes except to their user profile.

If you encounter any users that no longer need access, remove them. And then, use the [Google Authenticator plugin](https://wordpress.org/plugins/google-authenticator/) or another two-factor authentication system to secure the remaining accounts.

## Step Four: Disable PHP Execution in Untrusted Folders

So far, all of the preceding steps have revolved around preventing common, low-level attacks. 

But there are some more sophisticated threats to WordPress sites you should be worried about too. And many of them involve attackers finding ways to execute code on a site without gaining account access at all. 

This is common with WordPress because of the way it manages default folder permissions.

For example, if you install a plugin that will manage user-uploaded media like pictures and videos, it will need an upload folder that's writable to the outside world. If an attacker can gain access to that folder, they may try to upload a malicious script and use it to alter or take over the entire site. 

The good news is that you can guard against this with a simple access control file in the necessary folders.

What you'll need to do is to create a new file in each writable folder called .htaccess. It's a text file that tells the web server what to allow or disallow in a given directory. In it, include the following:

```php
# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase
RewriteRule ^index\.php$ - [L] RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L] </IfModule>
# END WordPress
<FilesMatch "\.(php|php\.)$">
Order Allow,Deny
Deny from all
</FilesMatch>
```

This .htaccess file will allow users to upload the kinds of files you want, but will prevent anyone from uploading any executable code in the writable directory. 

You can do this in any user-facing folders you'd like to protect. But beware of overusing these restrictions. Most of WordPress involves PHP execution, and you can disable your entire site if you put one of these in the wrong place.

## Step Five: Disable PHP Error Display

Gaining write and execute access to directories is just one of the ways that an attacker might try and run malicious code on a WordPress website. They may also look for parts of the site that do run PHP (which is pretty much everywhere you didn't lock down) and find weaknesses there. But you can make their job much harder.

To do that, you should turn off PHP error display so they can't see any results when they try to break site pages on purpose. If the site gives them hints as to what works and what doesn't, it could provide a roadmap to finding a way to exploit existing site pages. 

The good news is that it's simple to disable PHP error reporting in WordPress. All you have to do is edit the site's wp-config.php file, which is in the root directory and contains the site's base configuration information. 

Just add the following line to the file:

```php
define( 'WP_DEBUG', false);
```

This will disable PHP debugging site-wide. Just make a note when you make this change just in case the site runs into trouble in the future and requires authorized debugging efforts.

## Step Six – Disable Theme and Plugin Editing

Even after you've done all of the above, you can't be certain that nobody will ever find their way into a WordPress site with the intent to harm. So, you should throw a final set of roadblocks in the way. 

This won't stop any serious attacker from creating havoc, but it might buy the site's operators enough time to notice that something's wrong and take action to correct it.

What you should do is disable the built-in WordPress theme and plugin editing capability to make it harder for someone who's gained access to the administrative interface to alter the site's base coding. 

Once again, you can do this by altering the site's wp-config.php file located in its root directory. Add the following line just before where you see the words 'That's all, stop editing! Happy publishing':

```php
define( 'DISALLOW_FILE_EDIT', true );
```

This will hide the theme and plugin editors from the administrative interface and prevent any easy means of altering site files. To undo this change, the attacker would need FTP or file-level access to the web host, which will at least slow them down a bit.

And as a final note, although you may see advice elsewhere instructing you to use a code snippet plugin to make these changes, don't do it. If you do, an attacker could use that same plugin to undo your changes, negating the security value of making the changes in the first place.

## Imperfect Protections Are Still Worth Trying

The bottom line here is that WordPress is always going to be something of a victim of its own success. There are just so many websites relying on it which makes it a big and inviting target for attackers. 

And while these six measures won't stop every possible type of threat, they'll do a decent job defending against most garden-variety attacks.

You can (and should) also try to protect your site databases by changing the default table prefix to something obscure. But since that's a bit out of scope for an existing website, I've omitted it as a security measure here. 

If you want to give it a shot, there's an [excellent how-to located here](https://www.wpbeginner.com/wp-tutorials/how-to-change-the-wordpress-database-prefix-to-improve-security/). Otherwise, be satisfied that you've done your part to help keep one of the countless WordPress sites in operation worldwide just a little bit safer.

_Featured photo by IB Photography - stock.adobe.com._

