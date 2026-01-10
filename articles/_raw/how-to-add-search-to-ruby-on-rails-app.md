---
title: How to Add Search Functionality to a Ruby on Rails Application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-13T18:22:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-search-to-ruby-on-rails-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/markus-winkler-afW1hht0NSs-unsplash.jpg
tags:
- name: Ruby on Rails
  slug: ruby-on-rails
- name: search
  slug: search
seo_title: null
seo_desc: 'By Sampurna Chapagain

  Nowadays, most web applications have a search feature. Users can use the search
  feature in order to navigate websites more easily.

  Implementing a search feature in Ruby on Rails is very easy. By using only a few
  lines of code yo...'
---

By Sampurna Chapagain

Nowadays, most web applications have a search feature. Users can use the search feature in order to navigate websites more easily.

Implementing a search feature in Ruby on Rails is very easy. By using only a few lines of code you can set it up.

This tutorial assumes that you have basic knowledge of Ruby on Rails. If you need an introduction to the framework, [check out this course](https://www.freecodecamp.org/news/learn-ruby-on-rails-video-course/).

### What Will We Be Creating

By the end of this article, we'll have a web app with a search feature that looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/searchresults.gif)
_Demo of the app_

## How to Generate the Post Scaffold

Here we're using Ruby version 3.0 and Rails version 6.1.7.

Rails scaffold refers to the automatic generation of files that forms the basic structure of the rails project. These files include controllers, views, models, routes, and migration.

Now, let's scaffold the post using the following command:

`rails g scaffold post title description:text`

Now, you need to run the migration in order to update the schema using the `rails db:migrate` command. 

If you run the server now, you can perform all the CRUD operations in the project.

## How to Add Haml to the Project

You will be using haml in views instead of erb. You can do this by simply adding `gem 'haml', '~> 6.1', '>= 6.1.1'` in the gemfile. You can get all gems from the [https://rubygems.org/](https://rubygems.org/) website. 

Haml uses indentation and its main purpose is to make the markup look beautiful.

Now, you can use the haml extension in views instead of erb. So, you can rename application.html.erb to application.html.haml. You can also use [html to haml tools](https://awsm-tools.com/html-to-haml) for converting erb to haml files. 

## How to Build the Search Form 

Once that's done, you're at the main part of the tutorial. So, let's add the form in the application.html.haml file. 

```ruby
%body
    %form{action: "/search"}
      %input{placeholder: "Search",name: "key",type: "text"}
      %button{type: "submit"} Search
    = yield

This code will generate a form in the whole application.

Here, you are passing the action attribute which will redirect to the search page when the form is submitted. Also, you are passing the key as the name attribute for the input element.

If you submit the form now you will get the following routing error:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/searcherror.gif)
_Screen recording showing the routing error._

### How to Add Root and Search Routes 

Let's add a few routes in the routes.rb file.

```ruby
root "posts#index"

get '/search', to: "posts#search"

The first route makes the index view the root page.

The second route adds the search route as a get method. So, you need to create a search action with some SQL queries in the posts controller.

### How to Add the Search Action in the Controller

In the above route, the search route is looking for search actions in the posts controller. So, let's create it.

```ruby
def search
    key = "%#{params[:key]}%"
    @posts = Post.where("name LIKE ?", key)
end

Here, in the search action, the `key` variable holds the value of `params[:key]`. You get the value of `params[:key]` after the form submission. 

The `%` symbol matches zero, one, or multiple characters. The above code uses two `%` symbols before and after `params[:key]` to match the value of `params[:key]` present in any position with the `name` column records in the database.

It is using the `LIKE` operator with a `where` clause in order to perform a search. `?` is a placeholder value in queries and gets replaced with whatever arguments get passed – for example, `key` in this case. 

Additionally, you can also use the `or` operator for searching multiple columns in the database.


`@posts = Post.where("name LIKE ? or description LIKE ?", key, key)`

You can search for both the `name` and `description` records using the above code. 

### How to Add the Necessary Views

Next, you need to add a search.html.haml file. But before that, let's create a new partial called _post.html.haml file in order to reuse the code. The post partial will look like this:

```ruby

%tbody
  -@posts.each do |post|
    %tr
      %td= post.name
      %td= post.description
      %td= link_to 'Show', post
      %td= link_to 'Edit', edit_post_path(post)
      %td= link_to 'Destroy', post, method: :delete, data: { confirm: 'Are you sure?' }
%br/
= link_to 'New Post', new_post_path


This is how the search.html.haml file will look:

```ruby

%h1 Search Results
%p#notice= notice
%h1 Posts
%table
    %thead
        %tr
            %th Name
            %th Description
            %th{colspan: "3"}
    =render "post"


And, you need to update the index.html.haml file as well.

```ruby

%p#notice= notice
%h1 Posts
%table
    %thead
        %tr
            %th Name
            %th Description
            %th{colspan: "3"}
    = render "post"


By doing this, you are using the post partial in both index and search view. 

Finally, the search feature works as expected.

You can find the full source code of this project in this [GitHub repository](https://github.com/SampurnaC/search_demo_app_fcc).

## Conclusion

This is how you can create a search feature in a Rails application. 

If you liked this article, please consider [buying me a coffee](https://www.buymeacoffee.com/SamChapagain) ☕. 

You can find me on [Twitter](https://twitter.com/saam_codes) for various content related to Web Development. 

Thanks for reading. 


