---
title: 5 Helpful Visual Studio Plugins for Ruby on Rails Developers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-03T06:16:55.000Z'
originalURL: https://freecodecamp.org/news/visual-studio-plugins-for-ruby-on-rails-developers
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/visual_studio_ruby_on_rails-1.png
tags:
- name: plugins
  slug: plugins
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: visual studio
  slug: visual-studio
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Vishnu Chilamakuru

  In this article, I''ll share some of the plugins that I use to make development
  with Ruby on Rails easier and more fun.

  Why use these tools?

  Development tools play a significant role in a developer''s life. If you are a junior
  dev...'
---

By Vishnu Chilamakuru

In this article, I'll share some of the plugins that I use to make development with Ruby on Rails easier and more fun.

## Why use these tools?

Development tools play a significant role in a developer's life. If you are a junior developer and are just getting started working on projects, then knowing about the appropriate tools is a must. 

These tools can save you a lot of time and they allow you to code more efficiently and thus increase your productivity.

If you are Ruby on Rails developer who's looking for free development tools, I would recommend Visual Studio. It has a ton of plugins, like the ones mentioned below, and they have helped me increase my productivity a lot.

_Note: All visual studio plugins are available on the_ [_Visual Studio Marketplace_](https://marketplace.visualstudio.com/) _for free._

So let's dive in.

## [Ruby](https://marketplace.visualstudio.com/items?itemName=rebornix.Ruby)

With ~1.3M downloads, this is one of the most popular plugins for Ruby. It provides enhanced Ruby language and debugging support. 

With enhanced debugging support, developers can set breakpoints and inspect the local and global variables in debug mode. This helps to debug any issues easily and in quick time. 

This plugin also supports code formatting via **_rubocop_** which is very much needed when you are working with team of developers to maintain consistent code format.

Ruby plugin has the following features:

> - Automatic Ruby environment detection with support for rvm, rbenv, chruby, and asdf  
>   
> - Lint support via RuboCop, Standard, and Reek  
>   
> - Format support via RuboCop, Standard, Rufo, and RubyFMT  
>   
> - Basic Intellisense support  
>   
> - Ruby debugging support  
>   
> Source: [Ruby](https://marketplace.visualstudio.com/items?itemName=rebornix.Ruby)

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-30-at-3.13.49-PM.png)

## [Rails](https://marketplace.visualstudio.com/items?itemName=bung87.rails)

This is another popular plugin for Rails which provides enhanced Rails support. 

ERB HTML templating is widely used in Rails ecosystem as views to render HTML pages for websites. The Rails plugin has support for the `.erb` syntax and also provides auto-completion for popular HTML tags like stylesheet, meta tags, asset tags, and so on. 

This plugin also helps to switch between Rails views (`*.erb` files) easily. It also helps you see online documentation of any methods or commands easily side by side.

Here are some of the features this plugin supports:

> - Ruby on Rails “Asset Helpers” and “Tag Helpers” snippets.  
>   
> - .erb syntax highlights.  
>   
> - Navigation between related files through command.  
>   
> - Go to Definition.  
>   
> - View path suggestion, Model’s static method suggestion, and Model’s field suggestion.  
>   
> - Open the online document to the side through command.  
>   
> Source: [Rails](https://marketplace.visualstudio.com/items?itemName=bung87.rails)

![Image](https://www.freecodecamp.org/news/content/images/2020/08/vscode-rails.gif)
_Image from [VSCode Rails](https://marketplace.visualstudio.com/items?itemName=bung87.rails)_

## [Ruby Solargraph](https://marketplace.visualstudio.com/items?itemName=castwide.solargraph)

Ruby Solargraph is one of the most helpful plugins on this list, and provides IntelliSense, code completion, and inline documentation for Ruby. 

Inline documentation helps you view all the allowed methods of the class/object, and also helps you easily understand the definition of each method and its arguments.

This is one of the plugins I have personally used many times to refer to a Ruby method's documentation, arguments for a method, and so on.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/vscode-solargraph-0.34.1.gif)
_Image from [VSCode Solargraph](https://marketplace.visualstudio.com/items?itemName=castwide.solargraph)_

## [Vscode Endwise](https://github.com/kaiwood/vscode-endwise)

This is my favorite extension that can save you a lot of time and headaches. This extension automatically adds  `end` to all your Ruby code blocks.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/endwise.gif)
_Image from [VSCode Endwise](https://github.com/kaiwood/vscode-endwise)_

## [Rails Db Schema](https://marketplace.visualstudio.com/items?itemName=aki77.rails-db-schema)

This plugin helps you define a DB schema and also enables auto-completion for Rails DB schemas. 

While defining schemas or creating tables for any Entity, this plugin enables and autocompletes syntax for all your DDLs (Database definition language) like `create_table`, `create_index`, `delete_table`, `update_table`, and so on. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/definition.gif)
_Image from [VSCode DB Schema](https://marketplace.visualstudio.com/items?itemName=aki77.rails-db-schema)_

It helps in autocomplete of all attributes of any database entity. For example, if `User` has `email`, `name`, and `date_of_birth` attributes, this plugin will automatically detect the definition of entity and autocompletes its attributes when you type `User`. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/autocompletion.gif)
_Image from [VSCode DB Schema](https://marketplace.visualstudio.com/items?itemName=aki77.rails-db-schema)_

## Why use Visual Studio?

There are many other IDE options for Ruby on Rails developers like RubyMine (the enterprise version), Sublime, Vim, and so on. 

But my personal favorite is Visual Studio as it has extensive plugin support for multiple languages like Golang, PHP, Node.js, and more. So it's the default IDE, especially for polyglot developers.

Even though visual studio lacks few features compared to RubyMine like getting support for the latest Rails version updates, it covers the majority of the features required for development via community plugins.

If this article was useful, please share it with your network. Also, follow me on [Twitter](https://twitter.com/vishnuchi) to know when I publish my next article.

