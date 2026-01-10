---
title: How to Use the WordPress Command Line Interface – WP-CLI Tutorial
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2023-08-11T21:37:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-wordpress-cli
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/pexels-pixabay-207580.jpg
tags:
- name: command line
  slug: command-line
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: "In the world of website development and content management, efficiency\
  \ and automation are key. The WordPress Command Line Interface – or WP-CLI – is\
  \ a powerful tool that can help you streamlines tasks and manage WordPress websites\
  \ more effectively. \n..."
---

In the world of website development and content management, efficiency and automation are key. The WordPress Command Line Interface – or WP-CLI – is a powerful tool that can help you streamlines tasks and manage WordPress websites more effectively. 

This article provides an overview of WP-CLI, focusing on its capabilities to create, modify, and delete users, as well as handle plugins with ease. This article will show you how WP-CLI can significantly elevate your WordPress management experience.

## What is WP-CLI?

WP-CLI is a command-line tool designed for managing WordPress installations. It empowers developers, administrators, and site owners to interact with their websites directly from the command line, bypassing the need for manual interventions through the web interface. 

It's built on PHP, and offers a wide range of commands that you can execute right from the terminal.

By using WP-CLI, you'll be able to manage your WordPress sites much more efficiently. Let's see a few examples of how WP-CLI commands can simplify your workflow:

## WP-CLI Commands

### Site Information Retrieval

The `wp site info` command provides a quick overview of your WordPress site's important details, including the site's URL, the number of posts and pages, the active theme, and more. 

For instance, by running `wp site info`, you can promptly gather essential information about your site without navigating through the WordPress admin dashboard.

### Database Management

WP-CLI allows you to manage your WordPress database seamlessly. Use the `wp db export` command to create a database export file, ensuring a backup of your site's data. 

If you need to import data, the `wp db import` command facilitates this process. For example, if you have a database backup named `backup.sql`, executing `wp db import backup.sql` restores the database to a previous state.

### Theme Manipulation

Manipulating themes is extremely efficient with WP-CLI. For example, the `wp theme install` command lets you install a theme directly from the official WordPress theme repository. To install the "Twenty Twenty-One" theme, you can use the command `wp theme install twentytwentyone`.

### Post and Page Creation

Generating new content is made easier using WP-CLI. The `wp post create` and `wp post generate` commands enable you to create and populate posts and pages with content. 

For example, `wp post create --post_type=post --post_title="New Post"` creates a new post with the specified title.

These examples illustrate the versatility and power of WP-CLI in managing various aspects of your WordPress site. By harnessing its capabilities, you can enhance your efficiency, reduce manual tasks, and gain greater control over your website's management.

## How to Install WP-CLI

Before diving into more features of WP-CLI, let's understand the installation process. 

You can install WP-CLI globally on your system, making it accessible from any directory. 

To install WP-CLI, make sure you have PHP installed, along with a compatible version of WordPress. Download the Phar archive, place it in a directory reachable through your system's PATH, and you're ready to go. 

You can verify the installation by typing `wp --info` in your terminal. [Here](https://wp-cli.org) you can find the doc with the URL to download WP-CLI with a wget.

## How to Manage Users with WP-CLI

Managing users is a fundamental task when overseeing a WordPress site. WP-CLI simplifies user management with various commands that make creating, modifying, and deleting users much easier.

### How to Create Users

The `wp user create` command lets you quickly create users directly from the command line. 

To illustrate, let's create a new user named "Alice" with the email address "alice@example.com" and the role of editor. Simply enter:

```
wp user create alice alice@example.com --role=editor

```

### How to Modify Users

WP-CLI also streamlines user modifications. Use the `wp user update` command to adjust a user's details. 

For instance, let's change Alice's display name to "Alice Johnson" using the following command:

```
wp user update 123 --display_name="Alice Johnson"

```

In this example, "123" is Alice's ID.

### How to Delete Users

When user accounts become obsolete or require removal for security reasons, WP-CLI simplifies the process. 

To delete a user, use the `wp user delete` command. To remove Alice's account, simply execute:

```
wp user delete 123 --reassign=567

```

In this case, again "123" is Alice's ID and "567" is the ID of the user you want to assign Alice's content to (for example posts, pages, and so on).

## How to Manage Plugins with WP-CLI

Plugins play a crucial role in enhancing WordPress websites. WP-CLI extends its capabilities to manage plugins, making tasks such as installation, activation, deactivation, and updates incredibly efficient.

### How to Install Plugins

Use the `wp plugin install` command to seamlessly install plugins from the WordPress repository. 

For instance, let's install the "Akismet" anti-spam plugin:

```
wp plugin install akismet

```

### How to Activate and Deactivate Plugins

Managing plugin status is quite easy with WP-CLI. Activate or deactivate plugins using the `wp plugin activate` and `wp plugin deactivate` commands respectively. 

To activate the "Akismet" plugin, type the following command:

```
wp plugin activate akismet

```

### How to Update Plugins

Keeping plugins up to date is vital for security and performance. The `wp plugin update` command makes updates hassle-free. 

To update all installed plugins, simply run:

```
wp plugin update --all

```

### How to List Installed Plugins

WP-CLI offers an overview of installed plugins with the `wp plugin list` command. This provides a quick snapshot of each plugin's status, version, and available updates:

```
wp plugin list

```

## Conclusion

WP-CLI is an invaluable asset in the world of WordPress management. Its extensive command set helps you manage users and plugins – and much more – with remarkable ease. This saves you time and minimizes manual interventions. 

By harnessing the power of WP-CLI, administrators and developers can streamline workflows, improve security, and ensure their WordPress websites operate seamlessly. 


