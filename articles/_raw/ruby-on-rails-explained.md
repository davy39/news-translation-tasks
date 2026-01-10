---
title: Ruby on Rails Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/ruby-on-rails-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cff740569d1a4ca3552.jpg
tags:
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Ruby on Rails is a server-side framework (gem) built on the Ruby language
  to make websites. It includes everything you need to build web applications and
  has a big community.

  Ruby on Rails is an opinionated framework, and emphasizes the use of conven...'
---

[Ruby on Rails](http://rubyonrails.org/) is a server-side framework (gem) built on the Ruby language to make websites. It includes everything you need to build web applications and has a big community.

Ruby on Rails is an opinionated framework, and emphasizes the use of convention over configuration (CoC), and don't repeat yourself (DRY) practices. Rails can best be described as a model-view-controller (MVC) framework, and provides sensible defaults and structures for rapid application development. Lately, Rails has integrated an API module to make the creation of web-services faster and easier.

Ruby on Rails was created by David Heinemeir Hansson and is currently on it’s 6th version.

## **How to install Rails**

Rails is downloaded in the same way as any other Ruby gem: with the `gem install` command. Before we download it, we’ll need to [download Ruby](https://www.ruby-lang.org/). Afterwards we’re only 3 words away from starting with Ruby on Rails:

```shell
$ gem install rails
```

Rails ships with sqlite3 as the default database, which is a simple file on disk. You need to install MySQL or PostgreSQL if you want to use something more robust.

## **How to create a Rails application**

1. After you install Ruby on Rails, it’s very simple to create a brand new application, we’ll just need 3 more words:

```shell
$ rails new your_application_name
```

2. If you want to use MySQL:

```shell
$ rails new <application_name> -d mysql
```

3. If you want to use Postgres:

```shell
$ rails new <application_name> -d postgresql
```

4. This command will create a folder with the _your_application_name_ you informed in the last command. Next step is to go to the new directory you’ve just created:

```shell
$ cd your_application_name
```

5. Get the necessary gems and software packages before running your application:

```shell
$ bundle install
```

6. To run the rails server and see if everything went accordingly is also fast:

```shell
$ rails server
```

It couldn’t be anymore simple! Well, this isn’t actually 100% true, we could make it even smaller by reducing the `rails server` command to:

```shell
$ rails s
```

7. Now with your preferred browser, go to `http://localhost:3000` and you’ll see: “Yay! You’re on Rails!”

### **Alternative method for creating a Rails application**

1. Create a new directory:

```shell
$ mkdir <application_name>
```

2. Go into the new directory:

```shell
$ cd <application_name>
```

3. Create the Rails application using the Unix dot notation. This results in assigning the name of the directory to the new application:

```shell
$ rails new .
```

4. Start exploring the framework of the application you just created. To see a useful table of the folder structure, check out [Getting Started with Rails](https://guides.rubyonrails.org/getting_started.html).

## **Convention over Configuration**

_Convention over Configuration_ means a developer only needs to specify unconventional aspects of the application. For example, if there is a class `Sale` in the model, the corresponding table in the database is called `sales` by default. It is only if one deviates from this convention, such as calling the table “products sold”, that the developer needs to write code regarding these names. Generally, Ruby on Rails conventions lead to less code and less repetition.

## **What is MVC?**

Model (Active record) contains the business logic and interacts with the database. Views (Action views) all of the HTML files and structure. Controller (Action controller) interacts with the views and model to direct the actions of the application.

## **DRY - Don’t Repeat Yourself**

_Don’t repeat yourself_ means that information is located in a single, unambiguous place. For example, using the ActiveRecord module of Rails, the developer does not need to specify database column names in class definitions. Instead, Ruby on Rails can retrieve this information from the database based on the class name.

## **Ruby on Rails is open source**

Not only is it free to use, you can also help make it better. More than 4,500 people have already contributed code to [Rails](https://github.com/rails/rails). It’s easier than you think to become one of them.

