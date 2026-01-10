---
title: 'The Ultimate Intermediate Ruby on Rails Tutorial: Let’s Create an Entire App!'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-16T21:57:00.000Z'
originalURL: https://freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f
coverImage: https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_UH-HEG_VCXKMShU5iRbtFw-2.png
tags:
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Domantas G


  There are plenty tutorials online which show how to create your first app. This
  tutorial will go a step further and explain line-by-line how to create a more complex
  Ruby On Rails application.

  Throughout the whole tutorial, I will grad...'
---

### By Domantas G

![Image](https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_UH-HEG_VCXKMShU5iRbtFw-1.png)

There are plenty tutorials online which show how to create your first app. This tutorial will go a step further and explain line-by-line how to create a more complex Ruby On Rails application.

Throughout the whole tutorial, I will gradually introduce new techniques and concepts. The idea is that with every new section you should learn something new.

The following topics will be discussed throughout this guide:

* Ruby On Rails basics
* Refactoring: helpers, partials, concerns, design patterns
* Testing: TDD/BDD (RSpec & Capybara), Factories (Factory Girl)
* Action Cable
* Active Job
* CSS, Bootstrap, JavaScript, jQuery

#### **So what is the app is going to be about?**

It’s going to be a platform where you could search and meet like-minded people.

Main functionalities which the app will have:

* Authentication (with Devise)
* Ability to publish posts, and search and categorize them
* Instant messaging (popup windows and a separate messenger), with the ability to create private and group conversations.
* Ability to add users to contacts
* Real time notifications

**You can see how the** [**complete application**](https://www.youtube.com/watch?time_continue=10&v=KkgJRe7df04) **is going to look.**

**And you can find the complete project’s source code on** [**GitHub**](https://github.com/domagude/collabfield)**.**

**Table of Contents**

1. **[Introduction and Setup](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#so-what-is-the-app-is-going-to-be-about)** [Prequisites](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#prerequisites) [Setup](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#setup) [Create a new app](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#create-a-new-app)
2. **[Layout](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#layout)** [Home page](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#home-page) [Bootstrap](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#bootstrap) [Navigation bar](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#navigation-bar) [Style sheets](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#style-sheets)
3. **[Posts](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#posts)** [Authentication](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#authentication) [Helpers](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#helpers) [Testing](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#testing) [Main feed](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#main-feed) [Single post](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#single-post) [Specific branches](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#specific-branches) [Service objects](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#service-objects) [Create a new post](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#create-a-new-post)
4. **[Instant messaging](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#instant-messaging)** [Private conversation](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#private-conversation) [Contacts](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#contacts) [Group conversation](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#group-conversation) [Messenger](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#messenger)
5. **[Notifications](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#notifications)** [Contact requests](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#contact-requests) [Conversations](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#conversations)

### Prerequisites

I will try to explain every line of code and how I came up with the solutions. I think it is entirely possible for a total beginner to complete this guide. But keep in mind that this tutorial covers some topics which are beyond the basics.

So if you are a total beginner, it’s going to be harder, because your learning curve is going to be pretty steep. I will provide links to resources where you could get some extra information about every new concept we touch.

Ideally, it’s best if you are aware of the fundamentals of:

* [HTML](https://www.w3schools.com/html/), [CSS](https://www.w3schools.com/css/), [Bootstrap](https://getbootstrap.com/docs/3.3/getting-started/), [JavaScript](https://www.w3schools.com/js/), [jQuery](https://www.w3schools.com/jquery/)
* [Ruby](https://www.tutorialspoint.com/ruby/), [Ruby On Rails](http://guides.rubyonrails.org/getting_started.html)
* [Git](https://www.tutorialspoint.com/git/git_quick_guide.htm)

### Setup

I assume that you have already set up your basic Ruby On Rails development environment. If not, check [RailsInstaller](http://railsinstaller.org/en).

I had been developing on Windows 10 for a while. At first it was okay, but after some time I got tired of overcoming mystical obstacles which were caused by Windows. I had to keep figuring out hack ways to make my applications work. I’ve realized that it isn’t worth my time. Overcoming those obstacles didn’t give me any valuable skills or knowledge. I was just spending my time by duct taping Windows 10 setup.

So I switched to a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) instead. I chose to use [Vagrant](https://www.vagrantup.com/) to create a development environment and [PuTTY](http://www.putty.org/) to connect to a virtual machine. If you want to use Vagrant too, this is the [tutorial](https://www.youtube.com/watch?v=qjCMtR2Z-kA&t=) which I found useful.

### Create a new app

We are going to use PostgreSQL as our database. It is a popular choice among Ruby On Rails community. If you haven’t created any Rails apps with PostgreSQL yet, you may want to check this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-setup-ruby-on-rails-with-postgres).

Once you are familiar with PostgreSQL, navigate to a directory where you keep your projects and open a command line prompt.

To generate a new app run this line:

```bash
rails new collabfield --database=postgresql
```

`**Collabfield**`, that’s how our applications is going to be called. By default Rails uses SQlite3, but since we want to use PostgreSQL as our database, we need to specify it by adding:

```bash
--database=postgresql
```

Now we should’ve successfully generated a new application.

Navigate to a newly created directory by running the command:

```bash
cd collabfield
```

And now we can run our app by entering:

```bash
rails s
```

We just started our app. Now we should be able to see what we got so far. Open a browser and go to [http://localhost:3000](http://localhost:3000/). If everything went well, you should see the Rails signature welcome page.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-58.png)

## Layout

Time to code. Where should we start? Well, we can start wherever we want to. When I build a new website, I like to start by creating some kind of basic visual structure and then build everything else around that. Let’s do just that.

### Home page

When we go to [http://localhost:3000](http://localhost:3000/), we see the Rails welcome page. We’re going to switch this default page with our own home page. In order to do that, generate a new controller called `Pages`. If you are not familiar with Rails controllers, you should skim through the [Action Controller](http://guides.rubyonrails.org/action_controller_overview.html) to get an idea what the Rails controller is. Run this line in your command prompt to generate a new controller.

```bash
rails g controller pages
```

This rails generator should have created some files for us. The output in the command prompt should look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-59.png)

We are going to use this `PagesController` to manage our special and static pages. Now open the Collabfield project in a text editor. I use [Sublime Text](https://www.sublimetext.com/), but you can use whatever you want to.

Open a file `pages_controller.rb`

```rb
app/controllers/pages_controller.rb
```

We’ll define our home page here. Of course we could define home page in a different controller and in different ways. But usually I like to define the home page inside the `PagesController`.

When we open `pages_controller.rb`, we see this:

```rb
class PagesController < ApplicationController
end
```

It’s an empty class, named `PagesController`, which inherits from the `ApplicationController` class. You can find this class’s source code in `app/controllers/application_controller.rb`.

All our controllers, which we will create, are going to inherit from `ApplicationController` class. Which means that all methods defined inside this class are going to be available across all our controllers.

We’ll define a public method named `index`, so it can be callable as an action:

```rb
class PagesController < ApplicationController

  def index
  end

end
```

As you may have read in the [Action Controller](https://guides.rubyonrails.org/action_controller_overview.html), routing determines which controller and its public method (action) to call. Let’s define a route, so when we open our root page of the website, Rails knows which controller and its action to call. Open a `routes.rb` file in `app/config/routes.rb`.

If you don’t know what Rails routes is, it is a perfect time to get familiar by reading the Rails Routing.

Insert this line:

```rb
root to: 'pages#index'
```

Your `routes.rb` file should look like this:

```rb
Rails.application.routes.draw do
  root to: 'pages#index'
end
```

Hash symbol `#` in Ruby represents a method. As you remember an action is just a public method, so `pages#index` says “call the `PagesController` and its public method (action) `index`.”

If we went to our root path [http://localhost:3000](http://localhost:3000/), the index action would be called. But we don’t have any templates to render yet. So let’s create a new template for our `index` action. Go to `app/views/pages` and create an `index.html.erb` file inside this directory. Inside this file we can write our regular HTML+ [Embedded Ruby](https://www.tutorialspoint.com/ruby-on-rails/rails-and-html-erb.htm) code. Just write something inside the file, so we could see the rendered template in the browser.

```html
<h1>Home page</h1>
```

Now when we go to [http://localhost:3000](http://localhost:3000), we should see something like this instead of the default Rails information page.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-60.png)

Now we have a very basic starting point. We can start introducing new things to our website. I think it’s time to create our first commit.

In your command prompt run:

```bash
git status
```

And you should see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-61.png)

If you don’t already know, when we generate a new application, a new local git repository is initialized.

Add all current changes by running:

```bash
git add -A
```

Then commit all changes by running:

```bash
git commit -m "Generate PagesController. Initialize Home page"
```

If we ran this:

```bash
git status
```

We would see that there’s nothing to commit, because we just successfully committed all changes.

![Image](https://www.freecodecamp.org/news/content/images/2019/05/image-4.png)

### Bootstrap

For the navigation bar and the responsive grid system we’re going to use the [Bootstrap](https://getbootstrap.com/) library. In order to use this library we have to install the 

[bootstrap-sass](https://github.com/twbs/bootstrap-sass) gem. Open the `Gemfile` in your editor.

```bash
collabfield/Gemfile
```

Add a `bootstrap-sass` gem to the Gemfile. As the documentation says, you have to ensure that `sass-rails` gem is present too.

```
...
gem 'bootstrap-sass', '~> 3.3.6'
gem 'sass-rails', '>= 3.2'
...
```

Save the file and run this to install newly added gems:

```bash
bundle install
```

If you are still running the application, restart the Rails server to make sure that new gems are available. To restart the server simply shutdown it by pressing `Ctrl + C` and run `rails s` command again to boot the server.

Go to `assets` to open the `application.css` file:

`app/assets/stylesheets/application.css`

Below all the commented text add this:

```css
...
@import "bootstrap-sprockets";
@import "bootstrap";
```

Now change the `application.css` name to `application.scss`. This is necessary in order to use Bootstrap library in Rails, also it allows us to use [Sass](https://sass-lang.com/) features.

We want to control the order in which all `.scss` files are rendered, because in the future we might want to create some Sass variables. We want to make sure that our variables are going to be defined before we use them.

To accomplish it, remove those two lines from the `application.scss` file:

```scss
*= require_self
*= require_tree .
```

We’re almost able to use Bootstrap library. There’s a one more thing which we have to do. As the [bootstrap-sass](https://github.com/twbs/bootstrap-sass) docs says, Bootstrap JavaScript is dependent on jQuery library. To use jQuery with Rails, you have to add [jquery-rails](https://github.com/rails/jquery-rails) gem.

```bash
gem 'jquery-rails'
```

Run…

```bash
bundle install
```

…again, and restart the server.

Last step is to require Bootstrap and jQuery in the application’s JavaScript file. Go to `application.js`

```
app/assets/javascripts/application.js
```

Then add the following lines in the file:

```js
//= require jquery
//= require bootstrap-sprockets
```

Commit the changes:

```bash
git add -A
git commit -m "Add and configure bootstrap gem"
```

### Navigation bar

For the navigation bar we’ll use Bootstrap’s [navbar component](https://getbootstrap.com/docs/3.3/components/#navbar) as the starting point and then quite modify it. We will store our navigation bar inside a [partial template](https://guides.rubyonrails.org/layouts_and_rendering.html#using-partials).

We’re doing this because it’s better to keep every component of the app in separate files. It allows to test and manage app’s code much easier. Also we can reuse those components in other parts of the app, without duplicating the code.

Navigate to:

```
views/layouts
```

Create a new file:

```bash
_navigation.html.erb
```

For partials we use underscore prefix, so the Rails framework can distinguish it as a partial. Now copy and paste navbar component from Bootstrap docs and save the file. To see the partial on the website, we have to render it somewhere. Navigate to `views/layouts/application.html.erb` . This is the default file where everything gets rendered.

Inside the file we see the following method:

```
<%= yield %>
```

It renders the requested template. To use ruby syntax inside the HTML file, we have to wrap it around with `<% %>` (embedded ruby allows us to do that). To quickly learn the differences between ERB syntax, checkout this [StackOverflow answer](https://stackoverflow.com/questions/7996695/what-is-the-difference-between-and-in-erb-in-rails).

In [Home page section](https://medium.com/free-code-camp/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f#b574) we set the [route](https://medium.com/free-code-camp/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f#1faf) to recognize the root URL. So whenever we send a [GET request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) to go to a root page, `PagesController‘sindex` action gets called. And that respective action (in this case the `index`action) responds with a template which gets rendered with the `yield`method. As you remember, our template for a home page is located at `app/views/pages/index.html.erb`.

Since we want to have a navigation bar across all pages, we’ll render our navigation bar inside the default `application.html.erb` file. To render a partial file , simply use the `render` method and pass partial’s path as an argument. Do it just above the `yield` method like this:

```rb
...
<%= render 'layouts/navigation' %>
<%= yield %>
...
```

Now go to [http://localhost:3000](http://localhost:3000/) and you should be able to see the navigation bar.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-62.png)

As mentioned above, we’re going to modify this navigation bar. First let’s remove all `<li>` and `<form>` elements. In the future we’ll create our own elements here. The `_navigation.html.erb` file should look like this now.

```rb
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Brand</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
      </ul>

      <ul class="nav navbar-nav navbar-right">
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
```

We have a basic responsive navigation bar now. It’s a good time to create a new commit. In command prompt run the following commands:

```bash
git add -A
git commit -m "Add a basic navigation bar
```

We should change the navigation bar’s name from `Brand` to `collabfield`. Since `Brand` is a link element, we should use a `[link_to](https://apidock.com/rails/ActionView/Helpers/UrlHelper/link_to)` method to generate links. Why? Because this method allows us to easily generate URI paths. Open a command prompt and navigate to the project’s directory. Run the the following command:

```bash
rails routes
```

This command outputs our available routes, which are generated by the `routes.rb`file. As we see:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-63.png)

Currently, we have only one route, the one which we’ve defined before. If you look at the given routes, you can see a `Prefix` column. We can use those prefixes to generate a path to a wanted page. All we have to do is use a prefix name and add `_path` to it. If we wrote the `root_path`, that would generate a path to the root page. So let’s use the power of `link_to` method and routes.

Replace this line:

```html
<a class="navbar-brand" href="#">Brand</a>
```

With this line:

```html
<%= link_to 'collabfield', root_path, class: 'navbar-brand' %>
```

Remember that whenever you don’t quite understand how a particular method works, just Google it and you will probably find its documentation with an explanation. Sometimes documentations are poorly written, so you might want to Google a little bit more and you might find a blog or a StackOverflow answer, which would help.

In this case we pass a string as our first argument to add the `<a>`element’s value, the second argument is needed for a path, this is where routes helps us to generate it. The third argument is optional, which is accumulated inside the options hash. In this case we needed to add `navbar-brand`class to keep our Bootstrap powered navigation bar to function.

Let’s do another commit for this small change. In the upcoming section we’ll start changing our app’s design, starting from the navigation bar.

```bash
git add -A
git commit -m "Change navigation bar's brand name from Brand to collabfield"
```

### Style sheets

Let me introduce you how I structure my style sheet files. From what I know there aren’t any strong conventions on how to structure your style sheets in Rails. Everyone is doing it slightly differently.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-64.png)

This is how I usually structure my files.

* **Base directory** — This is where I keep Sass variables and styles which are used throughout the whole app. For instance default font sizes and default elements’ styles.
* **Partials** — Most of my styles go there. I keep all styles for separate components and pages in this directory.
* **Responsive** — Here I define different style rules for different screen sizes. For example, styles for a desktop screen, tablet screen, phone screen, etc.

First, let’s create a new repository branch by running this:

```bash
git checkout -b "styles"
```

We’ve just created a new [git branch](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) and automatically switched to it. From now on this is how we’re going to implement new changes to the code.

The reason for doing this is that we can isolate our currently functional version (master branch) and write a new code inside a project’s copy, without being afraid to damage anything.

Once we are complete with the implementation, we can just merge changes to the `master` branch.

Start by creating few directories:

```
app/assets/stylesheets/partials/layout
```

Inside the layout directory create a file `navigation.scss` and inside the file add:

```scss
.navbar-default, .navbar-toggle:focus, .collapsed, button.navbar-toggle {
  background: $navbarColor !important;
  border: none;
  a {
    color: white !important;
  }
}
```

With these lines of code we change navbar’s background and links color. As you may have noticed, `a` selector is nested inside another declaration block. Sass allows us to use this functionality. `!important` is used to strictly override default Bootstraps styles. The last thing which you may have noticed is that instead of a color name, we use a Sass variable. The reason for this is that we are going to use this color multiple times across the app. Let’s define this variable.

First create a new folder:

```
app/assets/stylesheets/base
```

Inside the base directory create a new file `variables.scss`. Inside the file define a variable:

```scss
$navbarColor: #323738;
```

If you tried to go to [http://localhost:3000](http://localhost:3000/), you wouldn’t notice any style changes. The reason for that is that in the [Bootstrap section](https://medium.com/free-code-camp/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f#58cf) we removed these lines:

```
*= require_self
*= require_tree .
```

from `application.scss`, to not automatically import all style files.

This means that now we have to import our newly created files to the main `application.scss` file. The file should look like this now:

```scss
// ...default comments

// Bootstrap
@import "bootstrap-sprockets";
@import "bootstrap";

// Variables
@import "base/variables";

// Partials - main css files
@import "partials/layout/*";
```

The reason for importing `variables.scss` file at the top is to make sure that the variables are defined before we use them.

Add some more CSS at the top of the `navigation.scss` file:

```scss
nav {
  .navbar-header {
    width: 100%;
    button, .navbar-brand {
      transition: opacity 0.15s;
    }
    button {
      margin-right: 0;
    }
    button:hover, .navbar-brand:hover {
      opacity: 0.8;
    }
  }
}
```

Of course you can put this code at the bottom of the file if you want to. Personally, I order and group CSS code based on [CSS selectors’ specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity). Again, everyone is doing it slightly differently. I put less specific selectors above and more specific selectors below. So for instance Type selectors go above Class selectors and Class selectors go above ID selectors.

Let’s commit changes:

```bash
git add -A
git commit -m "Add CSS to the navigation bar"
```

We want to make sure that the navigation bar is always visible, even when we scroll down. Right now we don’t have enough content to scroll down, but we will in the future. Why don’t we give this feature to the navigation bar right now?

To do that use Bootstrap class `navbar-fixed-top`. Add this class to the `nav` element, so it looks like this:

```html
<nav class="navbar navbar-default navbar-fixed-top">
```

Also we want to have `collabfield` to be to the [Bootstrap Grid System’s](https://getbootstrap.com/docs/3.3/css/#grid)left side boundaries. Right now it is to the viewport’s left side boundaries, because our class is currently `container-fluid`. To change that, change the class to `container`.

It should look like this:

```html
<div class="container">
```

Commit the changes:

```bash
git add -A 
git commit -m "
- in _navigation.html.erb add navbar-fixed-top class to nav. 
- Replace container-fluid class with container"
```

If you go to [http://localhost:3000](http://localhost:3000/), you see that the `Home page` text is hidden under the navigation bar. That’s because of the `navbar-fixed-top` class. To solve this issue, push the body down by adding the following to `navigation.scss`:

```scss
body {
 margin-top: 50px;
}
```

At this stage the app should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-65.png)

Commit the change:

```bash
git add -A
git commit -m "Add margin-top 50px to the body"
```

As you remember, we’ve created a new branch before and switched to it. It’s time to go back to the `master` branch.

Run the command:

```bash
git branch
```

You can see the list of our branches. Currently we’re in the `styles` branch.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-66.png)

To switch back to the `master` branch, run:

```bash
git checkout master
```

To merge our all changes, which we did in the `styles` branch, simply run:

```bash
git merge styles
```

The command merged those two branches and now we can see the summary of changes we made.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-67.png)

We don’t need `styles` branch anymore, so we can delete it:

```bash
git branch -D styles
```

## Posts

It’s almost a right time to start implementing the posts functionality. Since our app goal is to let users meet like-minded people, we have to make sure that posts’ authors can be identified. To achieve that, authentication system is required.

### Authentication

For an authentication system we are going to use the [devise gem](https://github.com/plataformatec/devise). We could create our own authentication system, but that would require a lot of effort. We’ll choose an easier route. Also it’s a popular choice among Rails community.

Start by creating a new branch:

```bash
git checkout -b authentication
```

Just like with any other gem, to set it up we’ll follow its documentation. Fortunately, it’s very easy to set up.

Add to your `Gemfile`

```
gem 'devise'
```

Then run commands:

```bash
bundle install
rails generate devise:install
```

You probably see some instructions in the command prompt. We won’t use mailers in this tutorial, so no further configuration is needed.

At this point, if you don’t know anything about Rails models, you should get familiar with them by skimming through [Active Record](http://guides.rubyonrails.org/active_record_basics.html) and [Active Model](http://guides.rubyonrails.org/active_model_basics.html)documentations.

Now let’s use a devise generator to create a `User` model.

```bash
rails generate devise User
```

Initialize a database for the app by running:

```bash
rails db:create
```

Then run this command to create new tables in your database:

```bash
rails db:migrate
```

That’s it. Technically our authentication system is set up. Now we can use Devise given methods and create new users. Commit the change:

```bash
git add -A
git commit -m "Add and configure the Devise gem"
```

By installing Devise gem, we not only get the back-end functionality, but also default views. If you list your routes by running:

```bash
rails routes
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-68.png)

You can see that now you have a bunch of new routes. Remember, we only had a one root route until now. If something seems to be confusing, you can always open [devise docs](https://github.com/plataformatec/devise/wiki) and get your answers. Also don’t forget that a lot of same questions come to other people’ s minds. There’s a high chance that you’ll find the answer by Googling too.

Try some of those routes. Go to [localhost:3000/users/sign_in](http://localhost:3000/users/sign_in) and you should see a sign in page.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-69.png)

If you went to [localhost:3000/users/sign_up](http://localhost:3000/users/sign_up), you would see a sign up page too. God Damn! as Noob Noob says. If you look at the `views` directory, you see that there isn’t any Devise directory, which we could modify. As Devise docs says, in order to modify Devise views, we’ve to generate it with a devise generator. Run

```bash
rails generate devise:views
```

If you check the `views` directory, you’ll see a generated devise directory inside. Here we can modify how sign up and login pages are going to look like. Let’s start with the login page, because in our case this is going to be a more straightforward implementation. With the registration page, due to our wanted feature, an extra effort will be required.

**Login page**

Navigate to and open `app/views/devise/sessions/new.html.erb`.

This is where the login page views are stored. There’s just a login form inside the file. As you may have noticed, the `[form_for](http://api.rubyonrails.org/v5.1/classes/ActionView/Helpers/FormHelper.html)` method is used to generate this form. This is a handy Rails method to generate forms. We’re going to modify this form’s style with bootstrap. Replace all file’s content with:

```rb
<%= bootstrap_form_for(resource, 
                       as: resource_name, 
                       url: session_path(resource_name)) do |f| %>

    <%= f.email_field :email, 
                      autofocus: true, 
                      class: 'form-control', 
                      placeholder: 'email' %>

    <%= f.password_field  :password, 
                          autocomplete: "off", 
                          class: 'form-control',
                          placeholder: 'password' %>


  <% if devise_mapping.rememberable? -%>
     <%= f.check_box :remember_me %>
  <% end -%>

   <%= f.submit "Log in", class: 'form-control login-button' %>
<% end %>
```

Nothing fancy is going here. We just modified this form to be a bootstrap form by changing the method’s name to `bootstrap_form_for` and adding `form-control` classes to the fields.

Take a look how arguments inside the methods are styled. Every argument starts in a new line. The reason why I did this is to avoid having long code lines. Usually code lines shouldn’t be longer than 80 characters, it improves readability. We’re going to style the code like that for the rest of the guide.

If we visit [localhost:3000/users/sign_in](http://localhost:3000/users/sign_in), we’ll see that it gives us an error:

```
undefined method 'bootstrap_form_for'
```

In order to use bootstrap forms in Rails we’ve to add a [bootstrap_form](https://github.com/bootstrap-ruby/rails-bootstrap-forms) gem. Add this to the `Gemfile`

```bash
gem 'bootstrap_form'
```

Then run:

```bash
bundle install
```

At this moment the login page should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-70.png)

Commit changes:

```bash
git add -A
git commit -m "Generate devise views, modify sign in form 
and add the bootstrap_form gem."
```

To give the bootstrap’s grid system to the page, wrap login form with the bootstrap container.

```html
<div class="container">
  <div class="row">
    <div class="col-sm-6 col-sm-offset-3">
      <h2 class="text-center">Log in</h2>
      
      <!-- PASTE LOGIN FORM HERE -->
      
    </div>
  </div> 
</div>
```

The width of the login form is 6 columns out of 12. And the offset is 3 columns. On smaller devices the form will take full screen’s width. That’s how the [bootstrap grid](https://getbootstrap.com/docs/3.3/css/#grid)works.

Let’s do another commit. Quite a minor change, huh? But that’s how I usually do commits. I implement a definite change in one area and then commit it. I think doing it this way helps to track changes and understand how the code has evolved.

```bash
git add -A
git commit -m "wrap login form in the login page with a boostrap container"
```

It would be better if we could just reach the login page by going to `/login`instead of `/users/sign_in`. We have to change the route. To do that we need to know where the action, which gets called when we go to login page, is located. Devise controllers are located inside the gem itself. By reading Devise docs we can see that all controllers are located inside the `devise` directory. Not really surprised by the discovery, to be honest U_U. By using the `devise_scope` method we can simply change the route. Go to `routes.rb` file and add

```rb
devise_scope :user do
  get 'login', to: 'devise/sessions#new'
end
```

Commit the change:

```bash
git add -A
git commit -m "change route from /users/sign_in to /login"
```

For now, leave the login page as it is.

**Sign up page**

If we navigated to [localhost:3000/users/sign_up](http://localhost:3000/users/sign_up), we would see the default Devise sign up page. But as mentioned above, the sign up page will require some extra effort. Why? Because we want to add a new `:name` column to the `users` table, so a User object could have the `:name` attribute.

We’re about to do some changes to the `schema.rb` file. At this moment, if you aren’t quite familiar with schema changes and migrations, I recommend you to read through [Active Record Migrations](http://guides.rubyonrails.org/active_record_migrations.html) docs.

First, we have to add an extra column to the `users` table. We could create a new migration file and use a `change_table` method to add an extra column. But we are just at the development stage, our app isn’t deployed yet. We can just define a new column straight inside the `devise_create_users` migration file and then recreate the database. Navigate to `db/migrate` and open the `*CREATION_DATE*_devise_create_users.rb` file and add `t.string :name, null: false, default: ""` inside the `create_table` method.

Now run the commands to drop and create the database, and run migrations.

```bash
rails db:drop
rails db:create
rails db:migrate
```

We added a new column to the users table and altered the `schema.rb` file.

To be able to send an extra attribute, so the Devise controller would accept it, we’ve to do some changes at the controller level. We can do changes to Devise controllers in few different ways. We can use devise generator and generate controllers. Or we can create a new file, specify the controller and the methods that we want to modify. Both ways are good. We are going to use the latter one.

Navigate to `app/controllers` and create a new file `registrations_controller.rb`. Add the following code to the file:

```rb
class RegistrationsController < Devise::RegistrationsController

  private

  def sign_up_params
    params.require(:user).permit( :name, 
                                  :email, 
                                  :password, 
                                  :password_confirmation)
  end

  def account_update_params
    params.require(:user).permit( :name, 
                                  :email, 
                                  :password, 
                                  :password_confirmation, 
                                  :current_password)
  end
end
```

This code overwrites the `sign_up_params` and `account_update_params` methods to accept the `:name` attribute. As you see, those methods are in the Devise `RegistrationsController`, so we specified it and altered its methods. Now inside our routes we have to specify this controller, so these methods could be overwritten. Inside `routes.rb` change

```
devise_for :users
```

to

```
devise_for :users, :controllers => {:registrations => "registrations"}
```

Commit the changes.

```bash
git add -A
git commit -m "
- Add the name column to the users table. 
- Include name attribute to sign_up_params and account_update_params 
  methods inside the RegistrationsController"
```

Open the `new.html.erb` file:

```
app/views/devise/registrations/new.html.erb
```

Again, remove everything except the form. Convert the form into a bootstrap form. This time we add an additional name field.

```rb
<%= bootstrap_form_for(resource, 
                       :as => resource_name, 
                       :url => registration_path(resource_name)) do |f| %>

  <%= f.text_field :name, 
	           placeholder: 'username (will be shown publicly)', 
	           class: 'form-control' %>
  <%= f.text_field :email, 
	           placeholder: 'email', 
	           class: 'form-control' %>
  <%= f.password_field :password, 
                       placeholder: 'password', 
                       class: 'form-control' %>
  <%= f.password_field :password_confirmation, 
                       placeholder: 'password confirmation', 
                       class: 'form-control' %>
  <%= f.submit 'Sign up', class: 'btn sign-up-button' %>
<% end %>
```

Commit the change.

```bash
git add -A
git commit -m "
Delete everything from the signup page, except the form. 
Convert form into a bootstrap form. Add an additional name field"
```

Wrap the form with a bootstrap container and add some text.

```html
<div class="container" id="sign-up-form">
  <div class="row">
    <h1>Get in touch with like-minded people</h1>
    <h3>Create, study, accomplish goals together</h3>

    <div class="col-sm-offset-4 col-sm-4">
      <h3>Sign up <small>it's free!</small></h3> 

        <!-- PASTE THE FORM HERE -->
		
    </div>
  </div>
</div>
```

Commit the change.

```bash
git add -A
git commit -m "
Wrap the sign up form with a bootstrap container. 
Add informational text inside the container"
```

Just like with the login page, it would be better if we could just open a sign up page by going to `/signup` instead of `users/sign_up`. Inside the `routes.rb` file add the following code:

```rb
devise_scope :user do
  get 'signup', to: 'devise/registrations#new'
end
```

Commit the change.

```bash
git add -A
git commit -m "Change sign up page's route from /users/sign_up to /signup"
```

Let’s apply a few style changes before we move on. Navigate to `app/assets/sytlesheets/partials` and create a new `signup.scss` file. Inside the file add the following CSS:

```scss
#sign-up-form {
  margin-top: 100px;
  h1 {
    font-size: 36px !important;
    font-size: 3.6rem !important;
  }
  text-align: center;
  padding-bottom: 20px; 
}
```

Also we haven’t imported files from the `partials` directory inside the `application.scss` file. Let’s do it right now. Navigate to the `application.scss` and just above the `@import partials/layout/*`, import all files from the `partials` directory. `Application.scss` should look like this

```scss
...

// Partials - main css files
@import "partials/*";
@import "partials/layout/*";
```

Commit the changes.

```bash
git add -A
git commit -m "
- Create a signup.scss and add CSS to the sign up page
- Import all files from partials directory to the application.scss"
```

Add few other style changes to the overall website look. Navigate to `app/assets/stylesheets/base` and create a new `default.scss` file. Inside the file add the following CSS code:

```scss
* {
  box-sizing: border-box;
}

html {
  font-size: 62.5%;
}

body {
  background: $backgroundColor;
  font-size: 14px;
  font-size: 1.4rem;
}

h1 {
  font-size: 24px;
  font-size: 2.4rem;
}

i {
  width: 26px;
}

ul {
  list-style-type: none;
}

a:hover, a:active, a:link, a:visited {
  text-decoration: none;
}

.control-label {
  display: none;
}
```

Here we apply some general style changes for the whole website. `font-size` is set to `62.5%`, so `1 rem` unit could represent `10px`. If you don’t know what the rem unit is, you may want to read this [tutorial](https://www.sitepoint.com/understanding-and-using-rem-units-in-css/). We don’t want to see a label text on bootstrap forms, that’s why we set this:

```scss
.control-label {
  display: none;
}
```

You may have noticed that the `$backgroundColor` variable is used. But this variable isn’t set yet. So let’s do it by opening `variables.scss` file and adding this:

```
$backgroundColor: #f0f0f0;
```

The `default.scss` file isn’t imported inside the `application.scss`. Import it below variables, the `application.scss` file should look like this:

```scss
...

// Variables
@import "base/variables";

// Default styles
@import "base/default";

...
```

Commit the changes.

```bash
git add -A
git commit -m "
Add CSS and import CSS files inside the main file
- Create a default.scss file and add CSS 
- Define $backgroundColor variable 
- Import default.scss file inside the application.scss"
```

**Navigation bar update**

Right now we have three different pages: home, login and signup. It is a good idea to connect them all together, so users could navigate through the website effortlessly. We’ll put links to signup and login pages on the navigation bar. Navigate to and open the `_navigation.html.erb` file.

```
app/views/layouts/_navigation.html.erb
```

We’re going to add some extra code here. In the future we will add even more code here. This will lead to a file with lots of code, which is hard to manage and test. In order to handle a long code easier, we’re going to start splitting larger code into smaller chunks. To achieve that, we’ll use partials. Before adding extra code, let’s split the current `_navigation.html.erb` code into partials already.

Let me quickly introduce you how our navigation bar is going to work. We’ll have two major parts. On one part elements will be shown all the time, no matter what the screen size is. On the other part of the navigation bar, elements will be shown only on bigger screens and collapsed on the smaller ones.

This is how the structure inside the `.container` element will look like:

```html
<div class="row">

  <!-- Elements visible all the time -->
  <div class="col-sm-7">
  </div><!-- col-sm-7 -->

  <!-- Elements collapses on smaller devices -->
  <div class="col-sm-5">
  </div><!-- col-sm-5 -->

</div><!-- row -->
```

Inside the layouts directory:

```
app/views/layouts
```

Create a new `navigation` directory. Inside this directory create a new partial `_header.html.erb` file.

```
app/views/layouts/navigation/_header.html.erb
```

From the `_navigation.html.erb` file cut the whole `.navbar-header` section and paste it inside the `_header.html.erb` file. Inside the `navigation` directory, create another partial file named `_collapsible_elements.html.erb` .

```
app/views/layouts/navigation/_collapsible_elements.html.erb
```

From the `_navigation.html.erb` file cut the whole `.navbar-collapse` section and paste it inside the `_collapsible_elements.html.erb`. Now let’s render those two partials inside the `_navigation.html.erb` file. The file should look like this now.

```html
<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    <div class="row">

      <!-- Elements visible all the time -->
      <div class="col-sm-7">
        <%= render 'layouts/navigation/header' %>
      </div><!-- col-sm-7 -->

      <!-- Elements collapses on smaller devices -->
      <div class="col-sm-5">
        <%= render 'layouts/navigation/collapsible_elements' %>
      </div><!-- col-sm-5 -->

    </div><!-- row -->
  </div><!-- container -->
</nav>
```

If you went to [http://localhost:3000](http://localhost:3000/) now, you wouldn’t notice any difference. We just cleaned our code a little bit and prepared it for a further development.

We are ready to add some links to the navigation bar. Navigate to and open the `_collapsible_elements.html.erb` file again:

```
app/views/layouts/_collapsible_elements.html.erb
```

Let’s fill this file with links, replace the file’s content with:

```html
<!-- Collect the nav links, forms, and other content for toggling -->
<div class="collapse navbar-collapse navbar-right" id="navbar-collapsible-content">
  <ul class="nav navbar-nav ">
    <% if user_signed_in? %>
      <li class="dropdown pc-menu">
        <a id="user-settings" class="dropdown-toggle" data-toggle="dropdown" href="#">
          <span id="user-name"><%= current_user.name %></span>
          <span class="caret"></span>
        </a>

        <ul class="dropdown-menu" role="menu">
          <li><%= link_to 'Edit Profile', edit_user_registration_path %></li>
          <li><%= link_to 'Log out', destroy_user_session_path, method: :delete %></li>
        </ul>
      </li>

      <li class="mobile-menu">
        <%= link_to 'Edit Profile', edit_user_registration_path %>
      </li>
      <li class="mobile-menu">
        <%= link_to 'Log out', destroy_user_session_path, method: :delete %>
      </li>

    <% else # user not signed it %>
      <li ><%= link_to 'Login', login_path %></li>
      <li ><%= link_to 'Signup', signup_path %></li>
    <% end # if user is signed it %>
  </ul>
</div><!-- navbar-collapse -->
```

Let me briefly explain to you what is going on here. First, at the second line I changed the element’s `id` to `navbar-collapsible-content`. This is required in order to make this content collapsible. It’s a bootstrap’s functionality. The default `id` was `bs-example-navbar-collapse-1`. To trigger this this function there’s the button with the `data-target`attribute inside the `_header.html`file. Open `views/layouts/navigation/_header.html.erb` and change `data-target` attribute to `data-target="#navbar-collapsible-content"`. Now the button will trigger the collapsible content.

Next, inside the`_collapsible_elements.html.erb` file you see some `if else`logic with the `user_signed_in?` Devise method. This will show different links based on if a user is signed in, or not. Leaving logic, such as `if else`statements inside views isn’t a good practice. Views should be pretty “dumb” and just spit the information out, without “thinking” at all. We will refactor this logic later with Helpers.

The last thing to note inside the file is `pc-menu` and `mobile-menu` CSS classes. The purpose of these classes is to control how links are displayed on different screen sizes. Let’s add some CSS for these classes. Navigate to `app/assets/stylesheets` and create a new directory `responsive`. Inside the directory create two files, `desktop.scss` and `mobile.scss`. The purpose of those files is to have different configurations for different screen sizes. Inside the `desktop.scss` file add:

```scss
@media screen and (min-width: 767px) {
  .mobile-menu {
    display: none !important;
  }
}
```

Inside the `mobile.scss` file add:

```scss
@media screen and (max-width: 767px) {
  .pc-menu {
    display: none !important;
  }
}
```

If you aren’t familiar with CSS media queries, read [this](https://www.w3schools.com/css/css_rwd_mediaqueries.asp). Import files from the `responsive` directory inside the `application.scss` file. Import it at the bottom of the file, so the `application.scss` should look like this:

```scss
...

// Media queries for a responsive design
@import "responsive/*";
```

Navigate to and open `navigation.scss` file

```
app/assets/stylesheets/partials/layout/navigation.scss
```

and do some stylistic tweaks to the navigation bar by adding the following inside the `nav` element’s selector:

```scss
.col-sm-5, .col-sm-7 {
  padding: 0;
}
```

And outside the `nav` element, add the following CSS code:

```scss
.pc-menu {
  margin-right: 10px;
}

.mobile-menu {
  i {
    color: white;
  }
  ul {
    padding: 0px;
  }
  a {
    display: block;
    padding: 10px 0px 10px 25px !important;
  }
  a:hover {
    background: white !important;
    color: black !important;
    i {
      color: black;
    }
  }
}

.icon-bar {
  background-color: white !important;
}

.active a {
  background: $navbarColor !important;
  border-bottom: solid 5px white;
}

.dropdown-toggle, .dropdown-menu {
  background: $navbarColor !important;
  border: none;
}

.dropdown-menu a:hover {
  color: black !important;
  background: white !important;
}
```

At this moment, our application should look like this when a user is not logged in:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-71.png)

Like this when a user is logged in:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-73.png)

And like this when the screen size is smaller:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-74.png)

Commit the changes.

```bash
git add -A
git commit -m "
Update the navigation bar
- Add login, signup, logout and edit profile links on the navigation bar 
- Split _navigation.scss code into partials 
- Create responsive directory inside the stylesheets directory and add CSS. 
- Add CSS to tweak navigation bar style"
```

Now we have a basic authentication functionality. It satisfies our needs. So let’s merge `authentication` branch with the `master` branch.

```bash
git checkout master
git merge authentication
```

We can see the summary of changes again. Authentication branch is not needed anymore, so delete it.

```
git branch -D authentication
```

### Helpers

When we were working on the `_collapsible_elements.html.erb`file, I mentioned that Rails views is not the right place for logic. If you look inside the `app` directory of the project, you see there’s the directory called `helpers`. We’ll extract logic from Rails views and put it inside the `helpers` directory.

```
app/views/pages
```

Let’s create our first helpers. Firstly, create a new branch and switch to it.

```
git checkout -B helpers
```

Navigate to the `helpers` directory and create a new `navigation_helper.rb` file

```
app/helpers/navigation_helper.rb
```

Inside helper files, helpers are defined as [modules](https://www.tutorialspoint.com/ruby/ruby_modules.htm). Inside the `navigation_helper.rb` define the module.

```rb
module NavigationHelper
end
```

By default Rails loads all helper files to all views. Personally I do not like this, because methods’ names from different helper files might clash. To override this default behavior open the `application.rb` file

```
config/application.rb
```

Inside the `Application` class add this configuration

```
config.action_controller.include_all_helpers = false
```

Now helpers are available for corresponding controller’s views only. So if we have the `PagesController`, all helpers inside the `pages_helper.rb` file will be available to all view files inside the `pages` directory.

We don’t have the `NavigationController`, so helper methods defined inside the `NavigationHelper` module won’t be available anywhere. The navigation bar is available across the whole website. We can include the `NavigationHelper` module inside the `ApplicationHelper`. If you aren’t familiar with loading and including files, read through this [article](https://prograils.com/posts/ruby-methods-differences-load-require-include-extend) to get an idea what is going to happen.

Inside the `application_helper.rb` file, require the `navigation_helper.rb` file. Now we have an access to the `navigation_helper.rb` file’s content. So let’s inject `NavigationHelper` module inside the `ApplicationHelper` module by using an `include` method. The `application_helper.rb` should look like this:

```rb
require 'navigation_helper.rb'

module ApplicationHelper
  include NavigationHelper
end
```

Now `NavigationHelper` helper methods are available across the whole app.

Navigate to and open the `_collapsible_elements.html.erb` file

```
app/views/layouts/navigation/_collapsible_elements.html.erb
```

We’re going to split the content inside the `if else` statements into partials. Create a new `collapsible_elements` directory inside the `navigation` directory.

```
app/views/layouts/navigation/collapsible_elements
```

Inside the directory create two files: `_signed_in_links.html.erb`and `_non_signed_in_links.html.erb`. Now cut the content from `_collapsible_elements.html.erb` file’s `if else` statements and paste it to the corresponding partials. The partials should look like this:

```html
<li class="dropdown pc-menu">
  <a id="user-settings" class="dropdown-toggle" data-toggle="dropdown" href="#">
    <span id="user-name"><%= current_user.name %></span>
    <span class="caret"></span>
  </a>

  <ul class="dropdown-menu" role="menu">
    <li><%= link_to 'Edit Profile', edit_user_registration_path %></li>
    <li><%= link_to 'Log out', destroy_user_session_path, method: :delete %></li>
  </ul>
</li>

<li class="mobile-menu">
  <%= link_to 'Edit Profile', edit_user_registration_path %>
</li>
<li class="mobile-menu">
  <%= link_to 'Log out', destroy_user_session_path, method: :delete %>
</li>
```

```html
<li ><%= link_to 'Login', login_path %></li>
<li ><%= link_to 'Signup', signup_path %></li>
```

Now inside the `_collapsible_elements.html.erb` file, instead of `if else`statements, add the`render` method with the `collapsible_links_partial_path`helper method as an argument. The file should look like this

```html
<!-- Collect the nav links, forms, and other content for toggling -->
<div class="collapse navbar-collapse navbar-right" id="navbar-collapsible-content">
  <ul class="nav navbar-nav ">
    <%= render collapsible_links_partial_path %>
  </ul>
</div><!-- navbar-collapse -->
```

`collapsible_links_partial_path` is the method we are going to define inside the `NavigationHelper`. Open `navigation_helper.rb`

```
app/helpers/navigation_helper.rb
```

and define the method inside the module. The `navigation_helper.rb` file should look like this:

```rb
module NavigationHelper

  def collapsible_links_partial_path
    if user_signed_in?
      'layouts/navigation/collapsible_elements/signed_in_links'
    else
      'layouts/navigation/collapsible_elements/non_signed_in_links'
    end
  end
  
end
```

The defined method is pretty straightforward. If a user is signed in, return a corresponding partial’s path. If a user is not signed in, return another partial’s path.

We’ve created our first helper method and extracted logic from views to a helper method. We’re going to do this for the rest of the guide, whenever we encounter logic inside a view file. By doing this we’re making a favor to ourselves, testing and managing the app becomes much easier.

The app should look and function the same.

Commit the changes.

```bash
git add -A
git commit -m "Configure and create helpers
- Change include_all_helpers config to false 
- Split the _collapsible_elements.html.erb file's content into 
  partials and extract logic from the file into partials"
```

Merge the `helpers` branch with the `master`

```bash
git checkout master
git merge helpershttps://gist.github.com/domagude/419bba70cb97e27f4ea04fe37820194a#file-rails_helper-rb
```

### Testing

At this point the application has some functionality. Even thought there aren’t many features yet, but we already have to spend some time by manually testing the app if we want to make sure that everything works. Imagine if the application had 20 times more features than it has now. What a frustration would be to check that everything works fine, every time we did code changes. To avoid this frustration and hours of manual testing, we’ll implement [automated tests](https://en.wikipedia.org/wiki/Test_automation).

Before diving into tests writing, allow me to introduce you how and what I test. Also you can read through [A Guide to Testing Rails Applications](http://guides.rubyonrails.org/testing.html) to get familiar with default Rails testing techniques.

**What I use for testing**

* **Framework:** [RSpec](https://relishapp.com/rspec/) When I started testing my Rails apps, I used the default [Minitest](http://guides.rubyonrails.org/testing.html#rails-meets-minitest)framework. Now I use RSpec. I don’t think there’s a good or a bad choice here. Both frameworks are great. I think it depends on a personal preference, which framework to use. I’ve heard that RSpec is a popular choice among Rails community, so I’ve decided to give it a shot. Now I am using it most of the time.
* **Sample data:** [factory_girl](https://github.com/thoughtbot/factory_girl) Again, at first I tried the default Rails way — [fixtures](http://guides.rubyonrails.org/testing.html#the-low-down-on-fixtures), to add sample data. I’ve found that it’s a different case than it is with testing frameworks. Which testing framework to choose is probably a personal preference. In my opinion it’s not the case with sample data. At first fixtures were fine. But I’ve noticed that after apps become larger, controlling sample data with fixtures becomes tough. Maybe I used it in a wrong way. But with factories everything was nice and peaceful right away. No matter if an app is smaller or bigger — the effort to set sample data is the same.
* **Acceptance tests:** [Capybara](https://github.com/teamcapybara/capybara) By default Capybara uses rack_test driver. Unfortunately, this driver doesn’t support JavaScript. Instead of the default Capybara’s driver, I chose to use [poltergeist](https://github.com/teampoltergeist/poltergeist). It supports JavaScript and in my case it was the easiest driver to set up.

**What I test**

I test all logic which is written by me. It could be:

* Helpers
* Models
* Jobs
* Design Patterns
* Any other logic written by me

Besides logic, I wrap my app with acceptance tests using Capybara, to make sure that all app’s features are working properly by simulating a user’s interaction. Also to help my simulation tests, I use [request tests](https://relishapp.com/rspec/rspec-rails/docs/request-specs/request-spec) to make sure that all requests return correct responses.

That’s what I test in my personal apps, because it fully satisfies my needs. Obviously, testing standards could be different from person to person and from company to company.

Controllers, views and gems weren’t mentioned, why? As many Rails developers say, controllers and views shouldn’t contain any logic. And I agree with them. In this case there isn’t much to test then. In my opinion, user simulation tests are enough and efficient for views and controllers. And gems are already tested by their creators. So I think that simulation tests are enough to make sure that gems work properly too.

**How I test**

Of course I try to use TDD approach whenever is possible. Write a test first and then implement the code. In this case the development flow becomes more smoother. But sometimes you aren’t sure how the completed feature is going to look like and what kind of output to expect. You might be experimenting with the code or just trying different implementation solutions. So in those cases, test first and implementation later approach doesn’t really work.

Before (sometimes after, as discussed above) every piece of logic I write, I write an isolated test for it a.k.a. [unit test](https://en.wikipedia.org/wiki/Unit_testing). To make sure that every feature of an app works, I write acceptance (user simulation) tests with Capybara.

**Set up a test environment**

Before we write our first tests, we have to configure the testing environment.

Open the `Gemfile` and add those gems to the test group

```bash
gem 'rspec-rails', '~> 3.6'
gem 'factory_girl_rails'
gem 'rails-controller-testing'
gem 'headless'
gem 'capybara'
gem 'poltergeist'
gem 'database_cleaner'
```

As discussed above, `rspec` gem is a testing framework, `factory_girl`is for adding sample data, `capybara` is for simulating a user’s interaction with the app and `poltergeist` driver gives the JavaScript support for your tests.

You can use another driver which supports JavaScript if it’s easier for you to set up. If you decide to use `poltergeist` gem, you will need PhantomJS installed. To install PhantomJS read [poltergeist docs](https://github.com/teampoltergeist/poltergeist).

`headless` gem is required to support headless drivers. `poltergeist` is a headless driver, that’s why we need this gem. `rails-controller-testing` gem is going to be required when we will test requests and responses with the [requests specs](https://relishapp.com/rspec/rspec-rails/docs/request-specs/request-spec). More on that later.

`database_cleaner` is required to clean the test database after tests where JavaScript was executed. Normally the test database cleans itself after each test, but when you test features which has some JavaScript, the database doesn’t clean itself automatically. It might change in the future, but at the moment, of writing this tutorial, after tests with JavaScript are executed, the test database isn’t cleaned automatically. That’s why we have to manually configure our test environment to clean the test database after each JavaScript test too. We’ll configure when to run the `database_cleaner` gem in just a moment.

Now when the purpose of these gems is covered, let’s install them by running:

```bash
bundle install
```

To initialize the `spec` directory for the RSpec framework run the following:

```bash
rails generate rspec:install
```

Generally speaking, spec means a single test in RSpec framework. When we run our specs, it means that we run our tests.

If you look inside the `app` directory, you will notice a new directory called `spec`. This is where we’re going to write tests. Also you may have noticed a directory called `test`. This is where tests are stored when you use a default testing configuration. We won’t use this directory at all. You can simply remove it from the project c(x_X)b.

As mentioned above, we have to set up the `database_cleaner` for the tests which include JavaScript. Open the `rails_helper.rb` file

```
spec/rails_helper.rb
```

Change this line

```
config.use_transactional_fixtures = true
```

to

```
config.use_transactional_fixtures = false
```

and below it add the following code:

```rb
  config.before(:suite) do
    DatabaseCleaner.clean_with(:truncation)
  end
 
  config.before(:each) do
    DatabaseCleaner.strategy = :transaction
  end
 
  config.before(:each, :js => true) do
    DatabaseCleaner.strategy = :truncation
  end
 
  config.before(:each) do
    DatabaseCleaner.start
  end
 
  config.after(:each) do
    DatabaseCleaner.clean
  end

```

I took this code snippet from this [tutorial](http://www.virtuouscode.com/2012/08/31/configuring-database_cleaner-with-rails-rspec-capybara-and-selenium/).

The last thing we’ve to do is to add some configurations. Inside the `rails_helper.rb` file’s configurations, add the following lines

```rb
  require 'capybara/poltergeist'
  require 'factory_girl_rails'
  require 'capybara/rspec'

  config.include Devise::Test::IntegrationHelpers, type: :feature
  config.include FactoryGirl::Syntax::Methods
  Capybara.javascript_driver = :poltergeist
  Capybara.server = :puma 
```

Let’s breakdown the code a little bit.

With `require` methods we load files from the new added gems, so we could use their methods below.

```bash
config.include Devise::Test::IntegrationHelpers, type: :feature
```

This configuration allows us to use `devise` methods inside `capybara`tests. How did I come up with this line? It was provided inside the [Devise docs](https://github.com/plataformatec/devise).

```
config.include FactoryGirl::Syntax::Methods
```

This configuration allows to use `factory_girl` gem’s methods. Again, I found this configuration inside the gem’s documentation.

```rb
Capybara.javascript_driver = :poltergeist 
Capybara.server = :puma
```

Those two configurations are required in order to be able to test JavaScript with `capybara`. Always read the documentation first, when you want to implement something you don’t know how to.

The reason why I introduced you with most of the testing gems and configurations at once and not gradually, once we meet a particular problem, is to give you a clear picture what I use for testing. Now you can always come back to this section and check majority of the configurations in one place. Rather than jumping from one place to another and putting gems with configurations like puzzle pieces together.

Let’s commit the changes and finally get our hands dirty with tests.

```bash
git add -A
git commit -m "
Set up the testing environment
- Remove test directory
- Add and configure rspec-rails, factory_girl_rails, 
  rails-controller-testing, headless, capybara, poltergeist,
  database_cleaner gems"
```

**Helper specs**

About each type of specs (tests), you can find general information by reading [rspec docs](https://relishapp.com/rspec) and its [gem docs](https://github.com/rspec/rspec-rails). Both are pretty similar, but you can find some differences between each other.

Create and switch to a new branch:

```bash
git checkout -b specs
```

So far we’ve created only one helper method. Let’s test it.

Navigate to `spec` directory an[https://gist.github.com/domagude/3c42ba6ccf31bf1c50588c59277a9146#file-navigation_helper_spec-rb](https://gist.github.com/domagude/3c42ba6ccf31bf1c50588c59277a9146#file-navigation_helper_spec-rb)d create a new directory called `helpers`.

```
spec/helpers
```

Inside the directory, create a new file `navigation_helper_spec.rb`

```
spec/helpers/navigation_helper_spec.rb
```

Inside the file, write the following code:

```rb
require 'rails_helper'

RSpec.describe NavigationHelper, :type => :helper do
  
end
```

`require ‘rails_helper'` gives us an access to all testing configurations and methods. `:type => :helper` treats our tests as helper specs and provides us with specific methods.

That’s how the `navigation_helper_spec.rb` file should look like when the `collapsible_links_partial_path` method is tested.

```rb
require 'rails_helper'

RSpec.describe NavigationHelper, :type => :helper do

  context 'signed in user' do
    before(:each) { helper.stub(:user_signed_in?).and_return(true) }

    context '#collapsible_links_partial_path' do
      it "returns signed_in_links partial's path" do
        expect(helper.collapsible_links_partial_path).to (
          eq 'layouts/navigation/collapsible_elements/signed_in_links'
        )
      end
    end
  end

  context 'non-signed in user' do
    before(:each) { helper.stub(:user_signed_in?).and_return(false) }
    
    context '#collapsible_links_partial_path' do
      it "returns non_signed_in_links partial's path" do
        expect(helper.collapsible_links_partial_path).to (
          eq 'layouts/navigation/collapsible_elements/non_signed_in_links'
        )
      end
    end
  end

end
```

To learn more about the `context` and `it`, read the [basic structure](https://relishapp.com/rspec/rspec-core/v/3-6/docs/example-groups/basic-structure-describe-it) docs. Here we test two cases — when a user is logged in and when a user is not logged in. In each context of `signed in user` and `non-signed in user`, we have [before hooks](https://relishapp.com/rspec/rspec-core/v/2-0/docs/hooks/before-and-after-hooks). Inside the corresponding context, those hooks (methods) run before each our tests. In our case, before each test we run the [stub](https://relishapp.com/rspec/rspec-mocks/v/2-4/docs/method-stubs/stub-with-a-simple-return-value) method, so the `user_signed_in?` returns whatever value we tell it to return.

And finally, with the [expect](https://relishapp.com/rspec/rspec-expectations/docs/built-in-matchers) method we check that when we call `collapsible_links_partial_path` method, we get an expected return value.

To run all tests, simply run:

```
rspec spec
```

To run specifically the `navigation_helper_spec.rb` file, run:

```
rspec spec/helpers/navigation_helper_spec.rb
```

If the tests passed, the output should look similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-75.png)

Commit the changes.

```bash
git add -A
git commit -m "Add specs to NavigationHelper's collapsible_links_partial_path method"
```

**Factories**

Next, we’ll need some sample data to perform our tests. `factory_girl` gem gives us ability to add sample data very easily, whenever we need it. Also it provides a good quality docs, so it makes the overall experience pretty pleasant. The only object we can create with our app so far is the `User`. To define the user factory, create a `factories` directory inside the `spec` directory.

```
spec/factories
```

Inside the factories directory create a new file users.rb and add the following code:

```rb
FactoryGirl.define do 
  factory :user do
    sequence(:name) { |n| "test#{n}" }
    sequence(:email) { |n| "test#{n}@test.com" }
    password '123456'
    password_confirmation '123456'
  end
end
```

Now within our specs, we can easily create new users inside the test database, whenever we need them, using `factory_girl` gem’s methods. For the comprehensive guide how to define and use factories, checkout the `factory_girl` gem’s docs.

Our defined factory, `user`, is pretty straightforward. We defined the values, `user`objects will have. Also we used the `sequence` method. By reading docs, you can see that with every additional `User` record, `n` value gets incremented by one. I.e. the first created user‘s name is going to be `test0`, the second one’s `test1`, etc.

Commit the changes

```bash
git add -A
git commit -m "add a users factory"
```

**Feature specs**

In the [feature specs](https://relishapp.com/rspec/rspec-rails/docs/feature-specs/feature-spec) we write code which simulates a user’s interaction with an app. Feature specs are powered by the `capybara` gem.

Good news is that we’ve everything set up and ready to write our first feature specs. We’re going to test the login, logout and signup functionalities.

Inside the `spec` directory, create a new directory called `features`.

```
spec/features
```

Inside the `features` directory, create another directory called `user`.

```
spec/features/user
```

Inside the `user` directory, create a new file called `login_spec.rb`

That’s how the login test looks like:

```rb
require "rails_helper"

RSpec.feature "Login", :type => :feature do
  let(:user) { create(:user) }

  scenario 'user navigates to the login page and succesfully logs in', js: true do
    user
    visit root_path
    find('nav a', text: 'Login').click
    fill_in 'user[email]', with: user.email
    fill_in 'user[password]', with: user.password
    find('.login-button').click
    expect(page).to have_selector('#user-settings')
  end

end
```

With this code we simulate a visit to the login page, starting from the home page. Then we fill the form and submit it. Finally, we check if we have the `#user-settings` element on the navigation bar, which is available only for signed in users.

`feature` and `scenario` are part of the Capybara’s syntax. `feature` is the same as `context`/`describe` and `scenario` is the same as `it`. More info you can find in Capybara’s docs, [Using Capybara With Rspec](https://github.com/teamcapybara/capybara#using-capybara-with-rspec).

`[let](https://relishapp.com/rspec/rspec-core/v/2-5/docs/helper-methods/let-and-let)` method allows us to write memorized methods which we could use across all specs within the context, the method was defined.

Here we also use our created `users` factory and the `create` method, which comes with the `factory_girl` gem.

`js: true` argument allows to test functionalities which involves JavaScript.

As always, to see if a test passes, run a specific file. In this case it is the `login_spec.rb` file:

```
rspec spec/features/user/login_spec.rb
```

Commit the changes.

```bash
git add -A
git commit -m "add login feature specs"
```

Now we can test the logout functionality. Inside the `user` directory, create a new file named `logout_spec.rb`

```
spec/features/user/logout_spec.rb
```

The implemented test should look like this:

```rb
require "rails_helper"

RSpec.feature "Logout", :type => :feature do
  let(:user) { create(:user) }

  scenario 'user successfully logs out', js: true do
    sign_in user
    visit root_path
    find('nav #user-settings').click
    find('nav a', text: 'Log out').click
    expect(page).to have_selector('nav a', text: 'Login')
  end

end
```

The code simulates a user clicking the logout button and then expects to see non-logged in user’s links on the navigation bar.

`sign_in` method is one of the Devise helper methods. We have included those helper methods inside the `rails_helper.rb` file previously.

Run the file to see if the test passes.

Commit the changes.

```bash
git add -A
git commit -m "add logout feature specs"
```

The last functionality we have is ability to sign up a new account. Let’s test it. Inside the `user` directory create a new file named `sign_up_spec.rb`. That’s how the file with the test inside should look like:

```rb
require "rails_helper"

RSpec.feature "Sign up", :type => :feature do
  let(:user) { build(:user) }

  scenario 'user navigates to sign up page and successfully signs up', js: true do
    visit root_path
    find('nav a', text: 'Signup').click
    fill_in 'user[name]', with: user.name
    fill_in 'user[email]', with: user.email
    fill_in 'user[password]', with: user.password
    fill_in 'user[password_confirmation]', with: user.password_confirmation
    find('.sign-up-button').click
    expect(page).to have_selector('#user-settings')
  end

end
```

We simulate a user navigating to the signup page, filling the form, submitting the form and finally, we expect to see the `#user-settings`element which is available only for logged in users.

Here we use the Devise’s `build` method instead of `create`. This way we create a new object without saving it to the database.

We can run the whole test suite and see if all tests pass successfully.

```
rspec spec
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-76.png)

Commit the changes.

```bash
git add -A
git commit -m "add sign up features specs"
```

We’re done with our first tests. So let’s merge the `specs` branch with the `master`.

```bash
git checkout master
git merge specs
```

Specs branch isn’t needed anymore. Delete it q__o.

```bash
git branch -D specs
```

### Main feed

On the the home page we’re going to create a posts feed. This feed is going to display all type of posts in a card format.

Start by creating a new branch:

```bash
git checkout -b main_feed
```

Generate a new model called `Post`.

```bash
rails g model post
```

Then we’ll need a `Category` model to categorize the posts:

```bash
rails g model category
```

Now let’s create some associations between `User`, `Category` and `Post` models.

Every post is going to belong to a category and its author (user). Open the models’ files and add the associations.

```rb
class Post < ApplicationRecord
  belongs_to :user
  belongs_to :category
end
class User < ApplicationRecord
  ...
  has_many :posts, dependent: :destroy       
end

class Category < ApplicationRecord
  has_many :posts
end
```

The `dependent: :destroy` argument says, when a user gets deleted, all posts what the user has created will be deleted too.

Now we’ve to define data columns and associations inside the migrations files.

```rb
class CreatePosts < ActiveRecord::Migration[5.1]
  def change
    create_table :posts do |t|
      t.string :title
      t.text :content
      t.belongs_to :category, index: true
      t.belongs_to :user, index: true
      t.timestamps
    end
  end
end
```

```rb
class CreateCategories < ActiveRecord::Migration[5.1]
  def change
    create_table :categories do |t|
      t.string :name
      t.string :branch
    end
  end
end
```

Now run the migration files:

```bash
rails db:migrate
```

Commit the changes:

```bash
git add -A
git commit -m "
- Generate Post and Category models. 
- Create associations between User, Post and Category models. 
- Create categories and posts database tables."
```

**Specs**

We can test the newly created models. Later we’ll need sample data for the tests. Since a post belongs to a category, we also need sample data for categories to set up the associations.

Create a `category` factory inside the `factories` directory.

```rb
FactoryGirl.define do 
  factory :category do
    sequence(:name) { |n| "name#{n}" }
    sequence(:branch) { |n| "branch#{n}" }
  end
end
```

Create a `post` factory inside the `factories` directory

```
spec/factories/posts.rb
```

```rb
FactoryGirl.define do 
  factory :post do
    title 'a' * 20
    content 'a' * 20
    user
    category
  end
end
```

As you see, it’s very easy to set up an association for factories. All we had to do to set up `user` and `category` associations for the `post` factory, is to write factories’ names inside the `post` factory.

Commit the changes.

```bash
git add -A
git commit -m "Add post and category factories"
```

For now we’ll only test the associations, because that’s the only thing we wrote yet inside the models.

Open the `post_spec.rb`

```bash
spec/models/post_spec.rb
```

Add specs for the associations, so the file should look like this:

```rb
require 'rails_helper'

RSpec.describe Post, type: :model do
  context 'Associations' do
    it 'belongs_to user' do
      association = described_class.reflect_on_association(:user).macro
      expect(association).to eq :belongs_to
    end

    it 'belongs_to category' do
      association = described_class.reflect_on_association(:category).macro
      expect(association).to eq :belongs_to
    end
  end
end
```

We use the `[described_class](https://relishapp.com/rspec/rspec-core/docs/metadata/described-class)` method to get the current context’s class. Which is basically the same as writing `Post` in this case. Then we use `[reflect_on_association](https://apidock.com/rails/v2.3.2/ActiveRecord/Reflection/ClassMethods/reflect_on_association)` method to check that it returns a correct association.

Do the same for other models.

```rb
require 'rails_helper'

RSpec.describe Category, type: :model do
  context 'Associations' do
    it 'has_many posts' do
      association = described_class.reflect_on_association(:posts)
      expect(association.macro).to eq :has_many
    end
  end
end
```

```rb
require 'rails_helper'

RSpec.describe User, type: :model do

  context 'Associations' do
    it 'has_many posts' do
      association = described_class.reflect_on_association(:posts)
      expect(association.macro).to eq :has_many
      expect(association.options[:dependent]).to eq :destroy
    end
  end
end
```

Commit the changes.

```bash
git add -A
git commit -m "Add specs for User, Category, Post models' associations"
```

**Home page layout**

Currently the home page has nothing inside, only the dummy text “Home page”. It’s time to create its layout with bootstrap. Open the home page’s view file `views/pages/index.html.erb` and replace the file’s content with the following code to create the page’s layout:

```html
<div class="container">
  <div class="row">
    <div id="side-menu"  class="col-sm-3">
    </div><!-- side-menu -->

    <div id="main-content" class="col-sm-9">
    </div><!-- main-content -->

  </div><!-- row -->
</div><!-- container -->
```

Now add some CSS to define elements’ style and responsive behavior.

Inside the `stylesheets/partials` directory create a new file `home_page.scss`

```
assets/stylesheets/partials/home_page.scss
```

In the file add the following CSS:

```scss
#main-content {
  background: white;
  min-height: 800px;
  margin: 0;
  padding: 10px 0 0 0;
}

#side-menu {
  padding: 0;
  #links-list {
    margin-top: 20px;
    padding: 0;
    font-size: 14px;
    font-size: 1.4rem;
    a {
      display: block;
      padding: 5px 15px;
      margin: 2px 0;
    }
    li {
      min-width: 195px;
      max-width: 195px;
    }
    li, li a {
      color: black;
      text-decoration: none;
    }
    li:hover {
      border-radius: 50px;
      background: $navbarColor;
    }
    li:hover a, li:hover i {
      color: white;
    }
  }
}
```

Inside the `mobile.scss` file’s `max-width: 767px` media query add:

```scss
#side-menu {
  display: none !important;
}
```

Now the home page should look like this on bigger screens

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-77.png)

and like this on the smaller screens

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-78.png)

Commit the changes.

```bash
git add -A
git commit -m "
- Add the bootstrap layout to the home page 
- Add CSS to make home page layout's stylistic and responsive design changes"
```

**Seeds**

To display posts on the home page, at first we need to have them inside the database. Creating data manually is boring and time consuming. To automate this process, we’ll use seeds. Open the `seeds.rb` file.

```
db/seeds.rb
```

Add the following code:

```rb
def seed_users
  user_id = 0
  10.times do 
    User.create(
      name: "test#{user_id}",
      email: "test#{user_id}@test.com",
      password: '123456',
      password_confirmation: '123456'
    )
    user_id = user_id + 1
  end
end


def seed_categories
  hobby = ['Arts', 'Crafts', 'Sports', 'Sciences', 'Collecting', 'Reading', 'Other']
  study = ['Arts and Humanities', 'Physical Science and Engineering', 'Math and Logic',
          'Computer Science', 'Data Science', 'Economics and Finance', 'Business',
          'Social Sciences', 'Language', 'Other']
  team = ['Study', 'Development', 'Arts and Hobby', 'Other']

  hobby.each do |name|
    Category.create(branch: 'hobby', name: name)
  end

  study.each do |name|
    Category.create(branch: 'study', name: name)
  end

  team.each do |name|
    Category.create(branch: 'team', name: name)
  end
end

def seed_posts
  categories = Category.all

  categories.each do |category|
    5.times do
      Post.create(
        title: Faker::Lorem.sentences[0], 
        content: Faker::Lorem.sentences[0], 
        user_id: rand(1..9), 
        category_id: category.id
      )
    end
  end
end

seed_users
seed_categories
seed_posts
```

As you see, we create `seed_users`, `seed_categories` and `seed_posts` methods to create `User`, `Category` and `Post` records inside the development database. Also the [faker](https://github.com/stympy/faker) gem is used to generate dummy text. Add `faker` gem to your `Gemfile`

```
gem 'faker'
```

and

```bash
bundle install
```

To seed data, using the `seeds.rb` file, run a command

```bash
rails db:seed
```

Commit the changes.

```bash
git add -A
git commit -m "
- Add faker gem 
- Inside the seeds.rb file create methods to generate 
  User, Category and Post records inside the development database"
```

**Rendering the posts**

To render the posts, we’ll need a `posts` directory inside the views.

Generate a new controller called `Posts`, so it will automatically create a `posts` directory inside the views too.

```bash
rails g controller posts
```

Since in our app the `PagesController` is responsible for the homepage, we’ll need to query data inside the `pages_controller.rb` file’s `index` action. Inside the `index` action retrieve some records from the `posts` table. Assign the retrieved records to an instance variable, so the retrieved objects are going to be available inside the home page’s views.

* If you aren’t familiar with ruby variables, read this [guide](https://www.tutorialspoint.com/ruby/ruby_variables.htm).
* If you aren’t familiar with retrieving records from the database in Rails, read the [Active Record Query Interface](http://guides.rubyonrails.org/active_record_querying.html) guide.

The `index` action should look something like this right now:

```rb
def index
  @posts = Post.limit(5)
end
```

Navigate to the home page’s template

```
views/pages/index.html.erb
```

and inside the `.main-content` element add

```
<%= render @posts %>
```

This will render all posts, which were retrieved inside the `index` action. Because `post` objects belong to the `Post` class, Rails automatically tries to render the `_post.html.erb` partial template which is located

```
views/posts/_post.html.erb
```

We haven’t created this partial file yet, so create it and add the following code inside:

```html
<div class="col-sm-3 single-post-card" id=<%= post_path(post.id) %>>
  <div class="card">
    <div class="card-block">
      <h4 class="post-text">
        <%= truncate(post.title, :length => 60) %>
      </h4>
      <div class="post-content">
        <div class="posted-by">Posted by <%= post.user.name %></div>
        <h3><%= post.title %></h3> 
        <p><%= post.content %></p>
        <%= link_to "I'm interested", post_path(post.id), class: 'interested' %>
      </div>
    </div>
  </div><!-- card -->
</div><!-- col-sm-3 -->
```

I’ve used a [bootstrap card](https://v4-alpha.getbootstrap.com/components/card/) component here to achieve the desired style. Then I just stored post’s content and its path inside the element. Also I added a link which will lead to the full post.

So far we didn’t define any routes for posts. We need them right now, so let’s declare them. Open the `routes.rb` file and add the following code inside the routes

```rb
resources :posts do
  collection do
    get 'hobby'
    get 'study'
    get 'team'
  end
end
```

Here I’ve used a [resources](http://guides.rubyonrails.org/routing.html#resource-routing-the-rails-default) method to declare routes for `index`, `show`, `new`, `edit`, `create`, `update` and `destroy` actions. Then I’ve declared some custom `collection` routes to access pages with multiple `Post` instances. These pages are going to be dedicated for separate branches, we’ll create them later.

Restart the server and go to [http://localhost:3000](http://localhost:3000/). You should see rendered posts on the screen. The application should look similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-79.png)

Commit the changes.

```bash
git add -A
git commit -m "Display posts on the home page
- Generate Posts controller and create an index action.
  Inside the index action retrieve Post records
- Declare routes for posts
- Create a _post.html.erb partial inside posts directory
- Render posts inside the home page's main content"
```

To start styling posts, create a new scss file inside the `partials` directory:

```
assets/stylesheets/partials/posts.scss
```

and inside the file add the following CSS:

```scss
.single-post-card {
  min-height: 135px;
  max-height: 135px;
  box-shadow: 1px 1px 4px rgba(0,0,0, 0.3);
  color: black;
  padding: 10px;
  text-align: left;
  transition: border 0.1s, background 0.5s;
  .post-text {
    overflow: hidden;
  }
  a, a:active, a:hover {
    color: black;
  }
  &:hover {
    cursor: pointer;
    background: white;
    box-shadow: none;
    border-radius: 1%;
  }
}

.post-content {
  display: none;
}

```

The home page should look similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-80.png)

Commit the change.

```bash
git add -A
git commit -m "Create a posts.scss file and add CSS to it"
```

**Styling with JavaScript**

Currently the site’s design is pretty dull. To create contrast, we’re going to color the posts. But instead of just coloring it with CSS, let’s color them with different color patterns every time a user refreshes the website. To do that we’ll use JavaScript. It’s probably a silly idea, but it’s fun c(o_u)?

Navigate to the `javascripts` directory inside your `assets` and create a new directory called `posts`. Inside the directory create a new file called `style.js`. Also if you want, you can delete by default generated `.coffee`, files inside the `javascripts` directory. We won’t use CoffeeScript in this tutorial.

```
assets/javascripts/posts/style.js
```

Inside the `style.js` file add the following code.

```js
$(document).on('turbolinks:load', function() {
    if ($(".single-post-card").length) {
        // set a solid background color style
        if (mode == 1) {
            $(".single-post-card").each(function() {
                $(this).addClass("solid-color-mode");
                $(this).css('background-color', randomColor());
            });
        }
        // set a border color style
        else {
            $(".single-post-card").each(function() {
                $(this).addClass("border-color-mode");
                $(this).css('border', '5px solid ' + randomColor());
            });
        }	
    }


    $('#feed').on( 'mouseenter', '.single-post-list', function() {
        $(this).css('border-color', randomColor());	
    });

    $('#feed').on( 'mouseleave', '.single-post-list', function() {
        $(this).css('border-color', 'rgba(0, 0 , 0, 0.05)');	
    });

});

var colorSet = randomColorSet();
var mode = Math.floor(Math.random() * 2);

// Randomly returns a color scheme
function randomColorSet() {
    var colorSet1 = ['#45CCFF', '#49E83E', '#FFD432', '#E84B30', '#B243FF'];
    var colorSet2 = ['#FF6138', '#FFFF9D', '#BEEB9F', '#79BD8F', '#79BD8F'];
    var colorSet3 = ['#FCFFF5', '#D1DBBD', '#91AA9D', '#3E606F', '#193441'];
    var colorSet4 = ['#004358', '#1F8A70', '#BEDB39', '#FFE11A', '#FD7400'];
    var colorSet5 = ['#105B63', '#FFFAD5', '#FFD34E', '#DB9E36', '#BD4932'];
    var colorSet6 = ['#04BFBF', '#CAFCD8', '#F7E967', '#A9CF54', '#588F27'];
    var colorSet7 = ['#405952', '#9C9B7A', '#FFD393', '#FF974F', '#F54F29'];
    var randomSet = [colorSet1, colorSet2, colorSet3, colorSet4, colorSet5, colorSet6, colorSet7];
    return randomSet[Math.floor(Math.random() * randomSet.length )];
}

// Randomly returns a color from an array of colors
function randomColor() {
    var color = colorSet[Math.floor(Math.random() * colorSet.length)];
    return color;
}
```

With this piece of code we randomly set one of two style modes when a browser gets refreshed, by adding attributes to posts. One style has colored borders only, another style has solid color posts. With every page change and browser refresh we also recolor posts randomly too. Inside the `randomColorSet()` function you can see predefined color schemes.

`mouseenter` and `mouseleave` event handlers are going to be needed in the future for posts in specific pages. There posts’ style is going to be different than posts’ on the home page. When you’ll hover on a post, it will slightly change its bottom border’s color. You’ll see this later.

Commit the changes.

```bash
git add -A
git commit -m "Create a style.js file and add js to create posts' style"
```

To complement the styling, add some CSS. Open the `posts.scss` file

```bash
assets/stylesheets/partials/posts.scss
```

and add the following CSS:

```scss
...
.solid-color-mode, .border-color-mode {
  .post-text {
    text-align: center;
  }
}

.solid-color-mode {
  .post-text {
    padding: 10px;
    background-color: white;
    border-radius: 25px;
  }
}

.border-color-mode {
  background-color: white;
}
```

Also inside the `mobile.scss` add the following code to fix too large text issues on smaller screens:

```scss
@media screen and (max-width: 1000px) {
  .solid-color-mode, .border-color-mode {
    .post-text {
      font-size: 16px;  
    }
  }
}
```

The home page should look similar to this right now:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-81.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-82.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-83.png)

Commit the changes

```bash
git add -A
git commit -m "Add CSS to posts on the home page
- add CSS to the posts.scss file
- add CSS to the mobile.scss to fix too large text issues on smaller screens"
```

**Modal window**

I want to be able to click on a post and see its full content, without going to another page. To achieve this functionality I’ll use a bootstrap’s [modal component](https://v4-alpha.getbootstrap.com/components/modal/).

Inside the `posts` directory, create a new partial file `_modal.html.erb`

```
views/posts/_modal.html.erb
```

and add the following code:

```html
<!-- Modal -->
<div  class="modal myModal" 
      tabindex="-1" 
      role="dialog" 
      aria-labelledby="myModalLabel">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <span class="posted-by"></span>
        <button type="button" 
                class="close" 
                data-dismiss="modal" 
                aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
        <div class="modal-body">
          <div class="loaded-data">
            <h3></h3>
            <p></p>
            <div class="interested"><a href="">I'm interested</a></div>
          </div><!-- loaded-data -->
        </div><!-- modal-body -->
    </div>
  </div>
</div>
```

This is just a slightly modified bootstrap’s component to accomplish this particular task.

Render this partial at the top of the home page’s template.

```html
<%= render 'posts/modal' %>
...
```

To make this modal window functional, we have to add some JavaScript. Inside the `posts` directory, create a new file `modal.js`

```
assets/javascripts/posts/modal.js
```

Inside the file, add the following code:

```js
$(document).on('turbolinks:load', function() {
  // when a post is clicked, show its full content in a modal window
  $("body").on( "click", ".single-post-card, .single-post-list", function() {
    var posted_by = $(this).find('.post-content .posted-by').html();
    var post_heading = $(this).find('.post-content h3').html();
    var post_content = $(this).find('.post-content p').html();
    var interested = $(this).find('.post-content .interested').attr('href');
    $('.modal-header .posted-by').text(posted_by);
    $('.loaded-data h3').text(post_heading);
    $('.loaded-data p').text(post_content);
    $('.loaded-data .interested a').attr('href', interested);
    $('.myModal').modal('show');
  });
});
```

With this js code we simply store selected post’s data into variables and fill modal window’s elements with this data. Finally, with the last line of code we make the modal window visible.

To enhance the modal window’s looks, add some CSS. But before adding CSS, let’s do a quick management task inside the `stylesheets` directory.

Inside the `partials` directory create a new directory called `posts`

```
assets/stylesheets/partials/posts
```

Inside the `posts` directory create a new file `home_page.scss`. Cut all code from the `posts.scss` file and paste it inside the `home_page.scss` file. Delete the `posts.scss`file. We’re doing this for a better CSS code management. It’s clearer when have few smaller CSS files with a distinguishable purpose, rather than one big file where everything is mashed together.

Also inside the `posts` directory, create a new file `modal.scss` and add the following CSS:

```scss
.modal-content {
  h3 {
    text-align: center;
  }
  p {
    margin: 50px 0;
  }
  .posted-by {
    color: rgba(0,0,0,0.5);
  }
}

.modal-content {
  .loaded-data {
    h3, p {
      overflow: hidden;
    }
    padding: 0 10px;
    .posted-by {
      margin: 0;
    }
  }
}

.interested {
  text-align: center;
  a {
    background-color: $navbarColor;
    padding: 10px;
    color: white;
    border-radius: 10px;
    &:hover {
      background-color: black;
      color: white;
    }
  }
}
```

Now when we click on the post, the application should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-84.png)

Commit the changes.

```bash
git add -A
git commit -m "Add a popup window to show a full post's content
- Add bootstrap's modal component to show full post's content
- Render the modal inside the home page's template
- Add js to fill the modal with post's content and show it
- Add CSS to style the modal"
```

Also merge the `main_feed` branch with the `master`

```bash
git checkout master
git merge main_feed
```

Get rid of the `main_feed` branch

```bash
git branch -D main_feed
```

**Single post**

Switch to a new branch

```bash
git checkout -b single_post
```

**Show a single post**

If you try to click on the `I'm interested` button, you will get an error. We haven’t created a `show.html.erb` template nor we’ve created a corresponding controller’s action. By clicking the button I want to be redirected to a selected post’s page.

Inside the `PostsController`, create a `show` action and then query and store a specific post object inside an instance variable:

```rb
...
  def show
    @post = Post.find(params[:id])
  end
...
```

`I'm interested` button redirects to a selected post. It has a `href` attribute with a path to a post. By sending a `GET` request to get a post, rails calls the `show` action. Inside the `show` action, we’ve an access to the id param, because by sending a `GET` request to get a specific post, we provided its `id`. I.e. by going to a `/posts/1` path, we would send a request to get a post whose `id` is `1`.

Create a `show.html.erb` template inside the `posts` directory

```
views/posts/show.html.erb
```

Inside the file add the following code:

```html
<div id="single-post-content" class="container">
  <div class="row">
    <div class="col-sm-6 col-sm-offset-3">
      <div class="posted-by">Posted by <%= @post.user.name %></div>
      <h3><%= @post.title %></h3>
      <p><%= @post.content %></p>
    </div>
  </div><!-- row -->
</div>
```

Create a `show.scss` file inside the `posts` directory and add CSS to style the page’s look:

```scss
#single-post-content {
  background: white;
  height: calc(100vh - 50px);

  h3 { 
    text-align: center;
  }
  p {
    margin: 50px 0;
  }
  .posted-by {
    font-size: 12px;
    font-size: 1.2rem;
    margin: 20px 0;
    color: rgba(0,0,0,0.5);
  }
}
```

Here I defined the page’s height to be `100vh-50px`, so the page’s content is full viewport’s height. It allows the container to be colored white across the full browser’s height, no matter if there is enough of content inside the element or not. `vh` property means viewport’s height, so `100vh` value means that the element is stretched 100% of viewport’s height. `100vh-50px` is required to subtract navigation bar’s height, otherwise the container would be stretched too much by `50px`.

If you click on the `I'm interested` button now, you will be redirected to a page which looks similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-85.png)

We’ll add extra features to the `show.html.erb` template later. Now commit the changes.

```bash
git add -A
git commit -m "Create a show template for posts
- Add a show action and query a post to an instance variable
- Create a show.scss file and add CSS"
```

**Specs**

Instead of manually checking that this functionality, of modal window appearance and redirection to a selected post, works, wrap it all with specs. We’re going to use capybara to simulate a user’s interaction with the app.

Inside the `features` directory, create a new directory called `posts`

```
spec/features/posts
```

Inside the new directory, create a new file `visit_single_post_spec.rb`

```
spec/features/posts/visit_single_post_spec.rb
```

And add a feature spec inside. The file looks like this:

```rb
require "rails_helper"

RSpec.feature "Visit single post", :type => :feature do
  let(:user) { create(:user) }
  let(:post) { create(:post) }

  scenario "User goes to a single post from the home page", js: true do
    post
    visit root_path
    page.find(".single-post-card").click
    expect(page).to have_selector('body .modal')
    page.find('.interested a').click
    expect(page).to have_selector('#single-post-content p', text: post.content)
  end

end
```

Here I defined all steps which I would perform manually. I start by going to the home page, click on the post, expect to see the popped up modal window, click on the `I'm interested` button, and finally, expect to be redirected to the post’s page and see its content.

By default RSpec matchers `have_selector`, `have_css`, etc. return true if an element is actually visible to a user. So after it was clicked on a post, testing framework expects to see a visible modal window. If you don’t care if a user sees an element or not and you just care about an element’s presence in the DOM, pass an additional `visible: false` argument.

Try to run the test

```
rspec spec/features/posts/visit_single_post_spec.rb
```

Commit the changes.

```bash
git add -A
git commit -m "Add a feature spec to test if a user can go to a
single post from the home page"
```

Merge the `single_post` branch with the `master`.

```bash
git checkout master
git merge single_post
git branch -D single_post
```

**Specific branches**

Every post belongs to a particular branch. Let’s create specific pages for different branches.

Switch to a new branch

```bash
git checkout -b specific_branches
```

**Home page’s side menu**

Start by updating the home page’s side menu. Add links to specific branches. Open the `index.html.erb` file:

```
views/pages/index.html.erb
```

We are going to put some links inside the `#side-menu` element. Split file’s content into partials, otherwise it will get noisy very quickly. Cut `#side-menu` and `#main-content` elements, and paste them into separate partial files. Inside the `pages` directory create an `index` directory, and inside the directory create corresponding partial files to the elements. The files should look like this:

```html
<div id="side-menu"  class="col-sm-3">
</div><!-- side-menu -->
```

```html
<div id="main-content" class="col-sm-9">
  <%= render @posts %>
</div><!-- main-content -->
```

Render those partial files inside the home page’s template. The file should look like this:

```html
<%= render 'posts/modal' %>

<div class="container">
  <div class="row">
    <%= render 'pages/index/side_menu' %>
    <%= render 'pages/index/main_content' %>
  </div><!-- row -->
</div><!-- container -->
```

Commit the changes.

```bash
git add -A
git commit -m "Split home page template's content into partials"
```

Inside `the _side_menu.html.erb` partial add a list of links, so the file should look like this:

```html
<div id="side-menu"  class="col-sm-3">
  <ul id="links-list">
    <%= render 'pages/index/side_menu/no_login_required_links' %>
  </ul>
</div><!-- side-menu -->
```

An unordered list was added. Inside the list we render another partial with links. Those links are going to be available for all users, no matter if they are signed in or not. Create this partial file and add the links.

Inside the `index` directory create a `side_menu` directory:

```
views/pages/index/side_menu
```

Inside the directory create a `_no_login_required_links.html.erb` partial with the following code:

```html
<li id="hobby">
  <%= link_to hobby_posts_path do %>
    <i class="fa fa-user-circle-o" aria-hidden="true"></i> Find a hobby buddy
  <% end %>
</li>

<li id="study">
  <%= link_to study_posts_path do %>
    <i class="fa fa-graduation-cap" aria-hidden="true"></i> Find a study buddy
  <% end %>
</li>

<li id="team">
  <%= link_to team_posts_path do %>
    <i class="fa fa-users" aria-hidden="true"></i> Find a team member
  <% end %>
</li>
```

Here we simply added links to specific branches of posts. If you are wondering how do we have paths, such as `hobby_posts_path`, etc., look at the `routes.rb` file. Previously we’ve added nested `collection` routes inside the `resources :posts` declaration.

If you pay attention to `i` elements’ attributes, you will notice `fa` classes. With those classes we declare [Font Awesome](http://fontawesome.io/icons/) icons. We haven’t set up this library yet. Fortunately, it’s very easy to set up. Inside the main `application.html.erb` file’s `head` element, add the following line

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
```

The side menu should be present now.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-86.png)

Commit the changes.

```bash
git add -A
git commit -m "Add links to the home page's side menu"
```

On smaller screens, where width is between `767px` and `1000px`, bootstrap’s container looks unpleasant, it looks overly compressed. So stretch it among those widths. Inside the `mobile.scss` file, add the following code:

```scss
...
@media only screen and (min-width:767px) and (max-width: 1000px) {
  .container {
     width: 100% !important;
  }
}
```

Commit the change.

```bash
git add -A
git commit -m "set .container width to 100% 
when viewport's width is between 767px and 1000px"
```

**Branch page**

If you try to click on one of those side menu links, you will get an error. We haven’t set up actions inside the `PostsController` nor we created any templates for it.

Inside the `PostsController`, define `hobby`, `study`, and `team` actions.

```rb
...  
  def hobby
    posts_for_branch(params[:action])
  end

  def study
    posts_for_branch(params[:action])
  end

  def team
    posts_for_branch(params[:action])
  end
...
```

Inside every action, `posts_for_branch` method is called. This method will return data for the specific page,  depending on the action’s name. Define the method inside the `private` scope.

```rb
...
private

def posts_for_branch(branch)
  @categories = Category.where(branch: branch)
  @posts = get_posts.paginate(page: params[:page])
end
...
```

In the `@categories` instance variable we retrieve all categories for a specific branch.  I.e. if you go to the hobby branch page, all categories which belong to  the hobby branch will be retrieved.

To get and store posts inside the `@posts` instance variable, `get_posts` method is used and then it is chained with a `paginate` method. `paginate` method comes from [will_paginate](https://github.com/mislav/will_paginate) gem. Let’s start by defining the `get_posts` method. Inside the `PostsController`’s `private` scope add:

```rb
...
def get_posts
  Post.limit(30)
end
...
```

Right now `get_posts` method just retrieves any 30 posts, not specific to anything, so we  could move on and focus on further development. We’ll come back to this  method in the near future.

Add the `will_paginate` gem to be able to use pagination.

```
gem 'will_paginate', '~> 3.1.0'
```

run

```bash
bundle install
```

All we miss now is templates. They are going to be similar to all  branches, so instead of repeating the code, inside every of those  branches, create a partial with a general structure for a branch. Inside  the `posts` directory create a `_branch.html.erb` file.

```html
<div id="branch-main-content" class="container">
  <div class="row">
    <h1 class="page-title"><%= page_title %></h1>
    <%= render 'posts/branch/create_new_post', branch: branch %>
  </div><!-- row -->

  <div class="row">
    <%= render 'posts/branch/categories', branch: branch %>
  </div>

  <div class="row">
    <div class="col-sm-12" id="feed">
      <%= render @posts %>
      <%= render no_posts_partial_path %>		
    </div>
  </div><!-- row -->	

  <div class="infinite-scroll">
    <%= will_paginate @posts %>
  </div>
</div><!-- container -->
```

First you see a `page_title` variable being printed on the page. We’ll pass this variable as an argument when we’ll render the `_branch.html.erb` partial. Next, a `_create_new_post` partial is rendered to display a link, which will lead to a page, where  a user could create a new post. Create this partial file inside a new `branch`directory:

```html
<div class="col-sm-12">
  <div class="col-sm-8 col-sm-offset-2">
    <%= render create_new_post_partial_path, branch: branch %>
  </div><!-- col-sm-8 -->	
</div><!-- col-sm-12 -->
```

Here we’ll use a `create_new_post_partial_path` helper method to determine which partial file to render. Inside the `posts_helper.rb` file, implement the method:

```rb
...  
  def create_new_post_partial_path
    if user_signed_in?
      'posts/branch/create_new_post/signed_in'
    else
      'posts/branch/create_new_post/not_signed_in'
    end
  end
...
```

Also create those two corresponding partials inside a new `create_new_post`directory:

```html
<div class="new-post-button-parent">
  <span>Cannot find anyone? Try to: </span>
  <%= link_to "Create a new post", 
              new_post_path(branch: branch), 
              :class => "new-post-button" %>
</div>
```

```html
<div class="text-center login-branch">
  To create a new post you have to 
  <%= link_to 'Login', 
              login_path, 
              class: 'login-button login-button-branch' %>
</div>
```

Next, inside the `_branch.html.erb` file we render a list of categories. Create a `_categories.html.erb` partial file:

```html
<% branch_path_name = "#{params[:action]}_posts_path" %>

<div class="col-sm-12">
  <ul class="categories-list">
    <%= render all_categories_button_partial_path, 
               branch_path_name: branch_path_name %>
    <% @categories.each do |category| %>
      <li class="category-item">
        <%= link_to category.name, 
                    send(branch_path_name, category: category.name), 
                    :class => ("selected-item" if params[:category] == category.name) %>
      </li>
    <% end %>
  </ul>
</div><!-- col-sm-12 -->
```

Inside the file, we have a `all_categories_button_partial_path` helper method which determines which partial file to render. Define this method inside the `posts_helper.rb` file:

```rb
...
   def all_categories_button_partial_path
    if params[:category].blank?
      'posts/branch/categories/all_selected'
    else
      'posts/branch/categories/all_not_selected'
    end
  end
...
```

All categories are going to be selected by default. If the `params[:category]` is empty, it means that none categories were selected by a user, which means that currently the default value `all` is selected. Create the corresponding partial files:

```html
<li class="category-item">
  <%= link_to "All", 
              send(branch_path_name), 
              :class => "selected-item"  %>
</li>
```

```html
<li class="category-item">
  <%= link_to "All", send(branch_path_name) %>
</li>
```

The [send](https://apidock.com/ruby/Object/send) method is used here to call a method by using a string, this allows to  be flexible and call methods dynamically. In our case we generate  different paths, depending on the current controller’s action.

Next, inside the `_branch.html.erb` file we render posts and call the `no_posts_partial_path` helper method. If posts are not found, the method will display a message.

Inside the `posts_helper.rb` add the helper method:

```rb
...
def no_posts_partial_path
  @posts.empty? ? 'posts/branch/no_posts' : 'shared/empty_partial'
end
...
```

Here I use a [ternary operator,](https://www.w3resource.com/ruby/ruby-ternary-operator.php) so the code looks a little bit cleaner. If there are any posts, I don’t  want to show any messages. Since you cannot pass an empty string to the  `render` method, I pass a path to an empty partial instead, in occasions where I don’t want to render anything.

Create a `shared` directory inside the views and then create an empty partial:

```
views/shared/_empty_partial.html.erb
```

Now create a `_no_posts.html.erb` partial for the message inside the `branch`directory.

```html
<div class="text-center">Currently there are no published posts</div>
```

Finally, we use the `will_paginate` method from the gem to split posts into multiple pages if there are a lot of posts.

Create templates for `hobby`, `study` and `team` actions. Inside them we’ll render the `_branch.html.erb` partial file and pass specific local variables.

```html
<%= render 'posts/modal' %>
<%= render partial: 'posts/branch', locals: { 
    branch: 'hobby',
    page_title: 'Find a person with the same hobby',
    search_placeholder: 'E.g. guitar playing, programming, cooking'
  } %>
```

```html
<%= render 'posts/modal' %>
<%= render partial: 'posts/branch', locals: { 
    branch: 'study',
    page_title: 'Find a person who studies the same field as you',
    search_placeholder: 'E.g. nutrition, calculus, astrophysics'
  } %>
```

```html
<%= render 'posts/modal' %>
<%= render partial: 'posts/branch', locals: { 
    branch: 'team',
    page_title: 'Find a person with similar interests as yours to your team',
    search_placeholder: 'E.g. musician for a band, developer for a project'
  } %>
```

If you go to any of those branch pages, you will see something like this

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-87.png)

Also if you scroll down, you will see that now we have a pagination

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-88.png)

We’ve done quite a lot of work to create these branch pages. Commit the changes

```bash
git add -A
git commit -m "Create branch pages for specific posts

- Inside the PostsController define hobby, study and team actions.
  Define a posts_for_branch method and call it inside these actions
- Add will_paginate gem
- Create a _branch.html.erb partial file
- Create a _create_new_post.html.erb partial file
- Define a create_new_post_partial_path helper method
- Create a _signed_in.html.erb partial file
- Create a _not_signed_in.html.erb partial file
- Create a _categories.html.erb partial file
- Define a all_categories_button_partial_path helper method
- Create a _all_selected.html.erb partial file
- Create a _all_not_selected.html.erb partial file
- Define a no_posts_partial_path helper method
- Create a _no_posts.html.erb partial file
- Create a hobby.html.erb template file
- Create a study.html.erb template file
- Create a team.html.erb template file"
```

**Specs**

Cover helper methods with specs. The `posts_helper_spec.rb` file should look like this:

```rb
require 'rails_helper'

RSpec.describe PostsHelper, :type => :helper do

  context '#create_new_post_partial_path' do
    it "returns a signed_in partial's path" do
      helper.stub(:user_signed_in?).and_return(true)
      expect(helper.create_new_post_partial_path). to (
        eq 'posts/branch/create_new_post/signed_in'
      )
    end

    it "returns a signed_in partial's path" do
      helper.stub(:user_signed_in?).and_return(false)
      expect(helper.create_new_post_partial_path). to (
        eq 'posts/branch/create_new_post/not_signed_in'
      )
    end
  end

  context '#all_categories_button_partial_path' do
    it "returns an all_selected partial's path" do
      controller.params[:category] = ''
      expect(helper.all_categories_button_partial_path).to (
        eq 'posts/branch/categories/all_selected'
      )
    end

    it "returns an all_not_selected partial's path" do
      controller.params[:category] = 'category'
      expect(helper.all_categories_button_partial_path).to (
        eq 'posts/branch/categories/all_not_selected'
      )
    end
  end

  context '#no_posts_partial_path' do
    it "returns a no_posts partial's path" do
      assign(:posts, [])
      expect(helper.no_posts_partial_path).to (
        eq 'posts/branch/no_posts'
      )
    end

    it "returns an empty partial's path" do
      assign(:posts, [1])
      expect(helper.no_posts_partial_path).to (
        eq 'shared/empty_partial'
      )
    end
  end
end
```

Again, specs are pretty simple here. I used the `stub` method to define methods’ return values. To define params, I selected the controller and simply defined it like this `controller.params[:param_name]`. And finally, I assigned instance variables by using an [assign](https://relishapp.com/rspec/rspec-rails/docs/helper-specs/helper-spec#helper-method-that-accesses-an-instance-variable) method.

Commit the changes

```bash
git add -A
git commit -m "Add specs for PostsHelper methods"
```

**Design changes**

In these  branch pages we want to have different posts’ design. In the home page  we have the cards design. In branch pages let’s create a list design, so  a user could see more posts and browse through them more efficiently.

Inside the `posts` directory, create a `post` directory with a `_home_page.html.erb`partial inside.

```
posts/post/_home_page.html.erb
```

Cut the `_post.html.erb` partial’s content and paste it inside the `_home_page.html.erb` partial file. Inside the `_post.html.erb` partial file add the following line of code:

```html
<%= render post_format_partial_path, post: post %>
```

Here we call the `post_format_partial_path` helper method to decide which post design to render, depending on the  current path. If a user is on the home page, render the post design for  the home page. If a user is on the branch page, render the post design  for the branch page. That’s why we cut `_post.html.erb` file’s content into `_home_page.html.erb` file.

Inside the `post` directory, create a new `_branch_page.html.erb` file and paste this code to define the posts design for the branch page.

```html
<div class="single-post-list" id=<%= post_path(post.id) %>>
  <%= truncate(post.title, :length => 60) %>
  <div class="post-content">
    <div class="posted-by">Posted by <%= post.user.name %></div>
    <h3><%= post.title %></h3> 
    <p><%= post.content %></p>
    <%= link_to "I'm interested", post_path(post.id), class: 'interested' %> 
  </div>
</div>
```

To decide which partial file to render, define the `post_format_partial_path`helper method inside the `posts_helper.rb`

```rb
def post_format_partial_path
  current_page?(root_path) ? 'posts/post/home_page' : 'posts/post/branch_page'
end
```

The `post_format_partial_path` helper method won’t be available in the home page, because we render  posts inside the home page’s template, which belongs to a different  controller. To have an access to this method, inside the home page’s  template, include `PostsHelper` inside the `ApplicationHelper`

```
include PostsHelper
```

**Specs**

Add specs for the `post_format_partial_path` helper method:

```rb
...
context '#post_format_partial_path' do
  it "returns a home_page partial's path" do
    helper.stub(:current_page?).and_return(true)
    expect(helper.post_format_partial_path).to (
      eq 'posts/post/home_page'
    )
  end

  it "returns a branch_page partial's path" do
    helper.stub(:current_page?).and_return(false)
    expect(helper.post_format_partial_path).to (
      eq 'posts/post/branch_page'
    )
  end
end
...
```

Commit the changes

```bash
git add -A
git commit -m "Add specs for the post_format_partial_path helper method"
```

**CSS**

Describe the posts style in branch pages with CSS. Inside the `posts` directory, create a new `branch_page.scss` style sheet file:

```scss
.single-post-list {
  min-height: 45px;
  max-height: 45px;
  padding: 10px 20px 10px 0px;
  margin: 0 10px;
  border-bottom: solid 3px rgba(0, 0 , 0, 0.05);
  border-bottom-right-radius: 10%;
  transition: border-color 0.1s;
  overflow: hidden;
  &:hover {
    cursor: pointer;
  }
}

.page-title {
  margin: 30px 0;
  text-align: center;
  background-color: white !important;
  font-weight: bold;
  a {
    color: black;
  }
  a:hover {
    text-decoration: underline;
  }
}

.categories-list {
  margin: 10px 0;
  padding: 0;
}

.category-item {
  display: inline-block;
  margin: 15px 0;
  a {
    font-size: 16px;
    font-size: 1.6rem;
    color: rgba(0,0,0,0.7);
    border: solid 2px rgba(0,0,0,0.4);
    border-radius: 8%;
    padding: 10px;
  }
  a:hover, .selected-item {
    background: $navbarColor;
    color: white;
    border: solid 2px white;
    border-radius: 0px;
  }
}

.new-post-button-parent {
  text-align: right;
  span {
    font-size: 12px;
    font-size: 1.2rem;
  }
}

.new-post-button {
  display: inline-block;
  background: $navbarColor;
  color: white;
  padding: 8px;
  border-radius: 10px;
  font-weight: bold;
  border: solid 2px $navbarColor;
  margin: 10px 0;
  &:hover, &:active, &:focus {
    background: white;
    color: black;
  }
}

.login-branch {
  margin: 10px 0;
}

.login-button-branch {
  padding: 5px 10px;
  border-radius: 10px;
  &:hover, &:active, &:visited, &:link {
    color: white;
  }
}

#branch-main-content {
  background: white;
  height: calc(100vh - 50px);
}

#feed {
  background-color: white;
}
```

Inside the `base/default.scss` add:

```scss
...
.login-button, .sign-up-button {
  background-color: $navbarColor;
  color: white !important;
}
```

To fix style issues on smaller devices, inside the `responsive/mobile.scss` add:

```scss
...
@media screen and (max-width: 550px) {
  .page-title {
      font-size: 20px;
      font-size: 2rem;
  }
  .new-post-button-parent {
    text-align: center;
    span {
      display: none !important;
    }
  }
  .post-button {
    padding: 5px;
  }
  .category-item {
    a {
      padding: 5px;
    }
  }
}

@media screen and (max-width: 767px) {
  .single-post-list {
    min-height: 65px;
    max-height: 65px;
    padding: 10px 0;
  }
}
...
```

Now the branch pages should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-89.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-90.png)

Commit the changes.

```bash
git add -A
git commit -m "Describe the posts style in branch pages

- Create a branch_page.scss file and add CSS
- Add CSS to the default.scss file
- Add CSS to the mobile.scss file"
```

#### **Search bar**

We want not only be able to browse through posts, but also search for specific ones. Inside the `_branch.html.erb` partial file, above the `categories` row, add:

```html
...
<div class="row">
  <%= render  'posts/branch/search_form', 
              branch: branch,
              search_placeholder: search_placeholder %>
</div><!-- row -->
...
```

Create a `_search_form.html.erb` partial file inside the `branch` directory and add the following code inside:

```html
<div class="col-sm-12">
  <%= form_tag(send("#{branch}_posts_path"), 
               :method => "get", 
               id: "search-form") do %>
    <i class="fa fa-search" aria-hidden="true"></i>
    <%= text_field_tag  :search, 
                        params[:search], 
                        placeholder: search_placeholder, 
                        class: "form-control" %>
    <%= render category_field_partial_path %>
  <% end %>
</div><!-- col-sm-12 -->
```

Here with the `send` method we dynamically generate a path to a specific `PostsController`’s  action, depending on a current branch. Also we send an extra data field  for the category if a specific category is selected. If a user has  selected a specific category, only search results from that category  will be returned.

Define the `category_field_partial_path` helper method inside the `posts_helper.rb`

```rb
...  
  def category_field_partial_path
    if params[:category].present?
      'posts/branch/search_form/category_field'
    else
      'shared/empty_partial'
    end
  end
...
```

Create a `_category_field.html.erb` partial file and add the code:

```html
<%= hidden_field_tag :category, params[:category] %>
```

To give the search form some style, add CSS to the `branch_page.scss` file:

```scss
.fa-search {
  position:absolute; 
  bottom:14px; 
  left:10px; 
  width:20px; 
  height:10px;
}

#search-form {
  position:relative;
  input {
    border: solid 2px rgba(0,0,0,0.2);
    border-radius: 10px;
    box-shadow: none;
    outline: 0;
  }
  input:focus {
    border: solid 2px rgba(0,0,0,0.35);
  }
  input#search {
    padding: 15px;
    width: 100%;
    height:20px; 
    margin: 10px 0; 
    padding-left: 30px;
  }
}
```

The search form, in branch pages, should look likes this now

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-91.png)

Commit the changes

```bash
git add -A
git commit -m "Add a search form in branch pages
- Render a search form inside the _branch.html.erb
- Create a _search_form.html.erb partial file
- Define a category_field_partial_path helper method in PostsHelper
- Create a _category_field.html.erb partial file
- Add CSS for the the search form in branch_page.scss"
```

Currently  our form isn’t really functional. We could use some gems to achieve  search functionality, but our data isn’t complicated, so we can create  our own simple search engine. We’ll use [scopes](http://guides.rubyonrails.org/active_record_querying.html#scopes) inside the `Post` model to make queries chainable and some conditional logic inside the  controller (we will extract it into service object in the next section  to make the code cleaner).

Start by defining scopes inside the `Post` model. To warm up, define the `default_scope` inside the `post.rb` file. This orders posts in descending order by the creation date, newest posts are at the top.

```rb
...
default_scope -> { includes(:user).order(created_at: :desc) }
...
```

Commit the change

```bash
git add -A
git commit -m "Define a default_scope for posts"
```

Make sure that the `default_scope` works correctly by wrapping it with a spec. Inside the `post_spec.rb` file, add:

```rb
context 'Scopes' do
  it 'default_scope orders by descending created_at' do
    first_post = create(:post)
    second_post = create(:post)
    expect(Post.all).to eq [second_post, first_post]
  end
end
```

Commit the change:

```bash
git add -A
git commit -m "Add a spec for the Post model's default_scope"
```

Now let’s make the search bar functional. Inside the `posts_controller.rb`replace the `get_posts` method’s content with:

```rb
def get_posts
  branch = params[:action]
  search = params[:search]
  category = params[:category]

  if category.blank? && search.blank?
    posts = Post.by_branch(branch).all
  elsif category.blank? && search.present?
    posts = Post.by_branch(branch).search(search)
  elsif category.present? && search.blank?
    posts = Post.by_category(branch, category)
  elsif category.present? && search.present?
    posts = Post.by_category(branch, category).search(search)
  else
  end
end
```

As I’ve  mentioned a little bit earlier, logic, just like in views, isn’t really  a good place in controllers. We want to make them clean. So we’ll  extract the logic out of this method in the upcoming section.

As you see, there is some conditional logic going on. Depending on a user request, data gets queried differently using scopes.

Inside the `Post` model, define those scopes:

```rb
...
  scope :by_category, -> (branch, category_name) do 
    joins(:category).where(categories: {name: category_name, branch: branch}) 
  end

  scope :by_branch, -> (branch) do
    joins(:category).where(categories: {branch: branch}) 
  end

  scope :search, -> (search) do
    where("title ILIKE lower(?) OR content ILIKE lower(?)", "%#{search}%", "%#{search}%")
  end
...
```

The `[joins](http://guides.rubyonrails.org/active_record_querying.html#joins)` method is used to query records from the associated tables. Also the  basic SQL syntax is used to find records, based on provided strings.

Now  if you restart the server and go back to any of those branch pages, the  search bar should work! Also now you can filter posts by clicking on  category buttons. And also when you select a particular category, only  posts from that category are queried when you use the search form.

Commit the changes

```bash
git add -A
git commit -m "Make search bar and category filters 
in branch pages functional
- Add by_category, by_branch and search scopes in the Post model
- Modify the get_posts method in PostsController"
```

Cover these scopes with specs. Inside the `post_spec.rb` file’s `Scopes` context add:

```rb
...
  it 'by_category scope gets posts by particular category' do
    category = create(:category)
    create(:post, category_id: category.id)
    create_list(:post, 10)
    posts = Post.by_category(category.branch, category.name)
    expect(posts.count).to eq 1
    expect(posts[0].category.name).to eq category.name
  end

  it 'by_branch scope gets posts by particular branch' do
    category = create(:category)
    create(:post, category_id: category.id)
    create_list(:post, 10)
    posts = Post.by_branch(category.branch)
    expect(posts.count).to eq 1
    expect(posts[0].category.branch).to eq category.branch
  end

  it 'search finds a matching post' do
    post = create(:post, title: 'awesome title', content: 'great content ' * 5)
    create_list(:post, 10, title: ('a'..'c' * 2).to_a.shuffle.join)
    expect(Post.search('awesome').count).to eq 1
    expect(Post.search('awesome')[0].id).to eq post.id
    expect(Post.search('great').count).to eq 1
    expect(Post.search('great')[0].id).to eq post.id
  end
...
```

Commit the changes

```bash
git add -A
git commit -m "Add specs for Post model's 
by_branch, by_category and search scopes"
```

#### **Infinite scroll**

When you go to any of these branch pages, at the bottom of the page you see the pagination

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-92.png)

When  you click on the next link, it redirects you to another page with older  posts. Instead of redirecting to another page with older posts, we can  make an infinite scrolling functionality, similar to the Facebook’s and  Twitter’s feed. You just scroll down and without any redirection and  page reload, older posts are appended to the bottom of the list.  Surprisingly, it is very easy to achieve. All we have to do is write  some JavaScript. Whenever a user reaches the bottom of the page, [AJAX](https://www.w3schools.com/xml/ajax_intro.asp) request is sent to get data from the `next` page and that data gets appended to the bottom of the list.

Start  by configuring the AJAX request and its conditions. When a user passes a  certain threshold by scrolling down, AJAX request gets fired. Inside  the `javascripts/posts` directory, create a new `infinite_scroll.js` file and add the code:

```js
$(document).on('turbolinks:load', function() {
  var isLoading = false;
  if ($('.infinite-scroll', this).size() > 0) {
    $(window).on('scroll', function() {
      var more_posts_url = $('.pagination a.next_page').attr('href');
      var threshold_passed = $(window).scrollTop() > $(document).height() - $(window).height() - 60;
      if (!isLoading && more_posts_url && threshold_passed) {
        isLoading = true;
        $.getScript(more_posts_url).done(function (data,textStatus,jqxhr) {
          isLoading = false;
        }).fail(function() {
          isLoading = false;
        });
      }
    });
  }
});
```

The `isLoading` variable makes sure that only one request is sent at a time. If there  is currently a request in progress, other requests won’t be initiated.

First  check if pagination is present, if there are any more posts to render.  Next, get a link to the next page, this is where the data will be  retrieved from. Then set a threshold when to call an AJAX request, in  this case the threshold is `60px` from the bottom of the window. Finally, if all conditions successfully pass, load data from the `next` page using the `[getScript()](https://api.jquery.com/jquery.getscript/)` function.

Because the `getScript()` function loads the JavaScript file, we have to specify which file to render inside the `PostsController`. Inside the `posts_for_branch`method specify `respond_to` formats and which files to render.

```rb
respond_to do |format|
  format.html
  format.js { render partial: 'posts/posts_pagination_page' }
end
```

When the controller tries to respond with the `.js` file, the`posts_pagination_page`template  gets rendered. This partial file appends newly retrieved posts to the  list. Create this file to append new posts and update the pagination  element.

```js
$('#feed').append('<%= j render @posts %>');
<%= render update_pagination_partial_path %>
```

Create an `update_pagination_partial_path` helper method inside the `posts_helper.rb`

```rb
def update_pagination_partial_path
  if @posts.next_page
    'posts/posts_pagination_page/update_pagination'
  else
    'posts/posts_pagination_page/remove_pagination'
  end
end
```

Here the `next_page` method from the `will_paginate` gem is used, to determine if there are any more posts to load in the future or not.

Create the corresponding partial files:

```js
$('.pagination').replaceWith('<%= j will_paginate @posts %>');
```

```js
$(window).off('scroll');
$('.pagination').remove();
```

If you go to any of the branch pages and scroll down, older posts should be automatically appended to the list.

Also we no longer need to see the pagination menu, so hide it with CSS. Inside the `branch_page.scss` file add:

```scss
...
.infinite-scroll {
  display: none;
}
...
```

Commit the changes

```bash
git add -A
git commit -m "Transform posts pagination into infinite scroll
- Create an infinite_scroll.js file
- Inside PostController's posts_for_branch method add respond_to format
- Define an update_pagination_partial_path
- Create _update_pagination.js.erb and _remove_pagination.js.erb partials
- hide the .infinite-scroll element with CSS"
```

**Specs**

Cover the `update_pagination_partial_path` helper method with specs:

```rb
context '#update_pagination_partial_path' do
  it "returns an update_pagination partial's path" do
    posts = double('posts', :next_page => 2)
    assign(:posts, posts)
    expect(helper.update_pagination_partial_path).to(
      eq 'posts/posts_pagination_page/update_pagination'
    )
  end

  it "returns a remove_pagination partial's path" do
    posts = double('posts', :next_page => nil)
    assign(:posts, posts)
    expect(helper.update_pagination_partial_path).to(
      eq 'posts/posts_pagination_page/remove_pagination'
    )
  end
end
```

Here I’ve used a test `double` to simulate the `posts` instance variable and its chained method `next_page`. You can learn more about the RSpec Mocks [here](https://relishapp.com/rspec/rspec-mocks/docs).

Commit the changes:

```bash
git add -A
git commit -m "Add specs for the update_pagination_partial_path
helper method"
```

We can also write feature specs to make sure that posts are successfully appended, after you scroll down. Create an `infinite_scroll_spec.rb` file:

```rb
require "rails_helper"

RSpec.feature "Infinite scroll", :type => :feature do
  Post.per_page = 15  

  let(:check_posts_count) do
    expect(page).to have_selector('.single-post-list', count: 15)
    page.execute_script("$(window).scrollTop($(document).height())")
    expect(page).to have_selector('.single-post-list', count: 30)
  end

  scenario "User scrolls down the hobby page 
            and posts list will be appended with older posts", js: true do      
    create_list(:post, 30, category: create(:category, branch: 'hobby'))     
    visit hobby_posts_path
    check_posts_count
  end

  scenario "User scrolls down the study page 
            and posts list will be appended with older posts", js: true do      
    create_list(:post, 30, category: create(:category, branch: 'study'))        
    visit study_posts_path
    check_posts_count
  end

  scenario "User scrolls down the team page 
            and posts list will be appended with older posts", js: true do      
    create_list(:post, 30, category: create(:category, branch: 'team'))      
    visit team_posts_path
    check_posts_count
  end

end
```

In the spec file all branch pages are covered. We make sure that this functionality works on all three pages. The `per_page` is `will_paginate` gem’s method. Here the `Post` model is selected and the default number of posts per page is set.

The `check_posts_count` method is defined to reduce the amount of code the file has. Instead of  repeating the same code over and over again in different specs, we  extracted it into a single method. Once the page is visited, it is  expected to see 15 posts. Then the `execute_script` method is used to run JavaScript, which scrolls the scrollbar to the  browser’s bottom. Finally, after the scroll, it is expected to see an  additional 15 posts. Now in total there should be 30 posts on the page.

Commit the changes:

```bash
git add -A
git commit -m "Add feature specs for posts' infinite scroll functionality"
```

**Home page update**

Currently  on the home page we can only see few random posts. Modify the home  page, so we could see a few posts from all branches.

Replace the `_main_content.html.erb` file’s content with:

```html
<div id="main-content" class="col-sm-9">
  <h3 class="page-name"><%= link_to 'Hobby', hobby_posts_path %></h3>
  <div class="row">
    <%= render @hobby_posts %>
    <%= render no_posts_partial_path(@hobby_posts) %>
  </div><!-- row -->

  <h3 class="page-name"><%= link_to 'Study', study_posts_path %></h3>
  <div class="row">
    <%= render @study_posts %>
    <%= render no_posts_partial_path(@study_posts) %>
  </div><!-- row -->

  <h3 class="page-name"><%= link_to 'Team member', team_posts_path %></h3>
  <div class="row">
    <%= render @team_posts %>
    <%= render no_posts_partial_path(@team_posts) %>
  </div><!-- row -->
</div><!-- main_content -->
```

We created sections with posts for every branch.

Define instance variables inside the `PagesController`’s `index` action. The action should look like this:

```rb
  def index
    @hobby_posts = Post.by_branch('hobby').limit(8)
    @study_posts = Post.by_branch('study').limit(8)
    @team_posts = Post.by_branch('team').limit(8)
  end
```

We have the `no_posts_partial_path` helper method from before, but we should modify it a little bit and  make it more reusable. Currently it works only for branch pages. Add a `posts` parameter to the method, so it should look like this now:

```rb
def no_posts_partial_path(posts)
  posts.empty? ? 'posts/shared/no_posts' : 'shared/empty_partial'
end
```

Here the `posts` parameter was added, instance variable was changed to a simple variable and the partial’s path was changed too. So move the `_no_posts.html.erb`partial file from

```
posts/branch/_no_posts.html.erb
```

to

```
posts/shared/_no_posts.html.erb
```

Also inside the `_branch.html.erb` file pass the `@posts` instance variable to the `no_posts_partial_path` method as an argument.

Add some style changes. Inside the `default.scss` file add:

```scss
...
.container {
  padding: 0;
}

.row {
  margin: 0;
}
```

And inside the `home_page.scss` add:

```scss
.page-name {
  margin: 15px 0px 15px 0px;
  text-align: center;
  background-color: white !important;
  font-weight: bold;
  a {
    color: black;
  }
  a:hover {
    text-decoration: underline;
  }
}
...
```

The home page should look similar to this right now

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-93.png)

Commit the changes

```bash
git add -A
git commit -m "Add posts from all branches in the home page
- Modify the _main_content.html.erb file
- Define instance variables inside the PagesController’s index action
- Modify the no_posts_partial_path helper method to be more reusable
- Add CSS to style the home page"
```

#### Service objects

As  I’ve mentioned before, if you put logic inside controllers, they become  complicated very easily and a huge pain to test. That’s why it’s a good  idea to extract logic from them somewhere else. To do that I use design  patterns, service objects (services) to be more specific.

Right now inside the `PostsController`, we have this method:

```rb
def get_posts
  branch = params[:action]
  search = params[:search]
  category = params[:category]

  if category.blank? && search.blank?
    posts = Post.by_branch(branch).all
  elsif category.blank? && search.present?
    posts = Post.by_branch(branch).search(search)
  elsif category.present? && search.blank?
    posts = Post.by_category(branch, category)
  elsif category.present? && search.present?
    posts = Post.by_category(branch, category).search(search)
  else
  end
end
```

It has a  lot of conditional logic which I want to remove by using services.  Service objects (services) design pattern is just a basic [ruby class](https://www.tutorialspoint.com/ruby/ruby_classes.htm). It’s very simple, we just pass data which we want to process and call a defined method to get a desired return value.

In ruby we pass data to Class’s `initialize` method, in other languages it’s known as the `constructor`.  And then inside the class, we just create a method which will handle  all defined logic. Let’s create that and see how it looks in code.

Inside the `app` directory, create a new `services` directory:

```
app/services
```

Inside the directory, create a new `posts_for_branch_service.rb` file:

```rb
class PostsForBranchService
  def initialize(params)
    @search = params[:search]
    @category = params[:category]
    @branch = params[:branch]
  end

  # get posts depending on the request
  def call
    if @category.blank? && @search.blank?
      posts = Post.by_branch(@branch).all
    elsif @category.blank? && @search.present?
      posts = Post.by_branch(@branch).search(@search)
    elsif @category.present? && @search.blank?
      posts = Post.by_category(@branch, @category)
    elsif @category.present? && @search.present?
      posts = Post.by_category(@branch, @category).search(@search)
    else
    end
  end

end
```

Here, as described above, it is just a plain ruby class with an `initialize`method to accept parameters and a `call` method to handle the logic. We took this logic from the `get_posts` method.

Now simply create a new object of this class and call the `call` method inside the `get_posts` method. The method should look like this right now:

```rb
  def get_posts
    PostsForBranchService.new({
      search: params[:search],
      category: params[:category],
      branch: params[:action]
    }).call
  end
```

Commit the changes:

```bash
git add -A
git commit -m "Create a service object to extract logic
from the get_posts method"
```

**Specs**

A  fortunate thing about design patterns, like services, is that it’s easy  to write unit tests for it. We can simply write specs for the `call` method and test each of its conditions.

Inside the `spec` directory create a new `services` directory:

```
spec/services
```

Inside the directory create a new file `posts_for_branch_service_spec.rb`

```rb
require 'rails_helper'
require './app/services/posts_for_branch_service.rb'

describe PostsForBranchService do

  context '#call' do
    let(:not_included_posts) { create_list(:post, 2) }
    let(:category) { create(:category, branch: 'hobby', name: 'arts') }
    let(:post) do
      create(:post,
              title: 'a very fun post', 
              category_id: category.id)
    end
    it 'returns posts filtered by a branch' do
      not_included_posts
      category
      included_posts = create_list(:post, 2, category_id: category.id)
      expect(PostsForBranchService.new({branch: 'hobby'}).call).to(
        match_array included_posts
      )
    end

    it 'returns posts filtered by a branch and a search input' do
      not_included_posts
      category
      included_post = [] << post
      expect(PostsForBranchService.new({branch: 'hobby', search: 'fun'}).call).to(
        eq included_post
      )
    end

    it 'returns posts filtered by a category name' do
      not_included_posts
      category
      included_post = [] << post
      expect(PostsForBranchService.new({branch: 'hobby', category: 'arts'}).call).to(
        eq included_post
      )
    end

    it 'returns posts filtered by a category name and a search input' do
      not_included_posts
      category
      included_post = [] << post
      expect(PostsForBranchService.new({name: 'arts', 
                                        search: 'fun', 
                                        branch: 'hobby'}).call).to eq included_post
    end
  end
end
```

At the top of the file, the `posts_for_branch_service.rb` file is loaded and then each of the `call` method’s conditions are tested.

Commit the changes

```bash
git add -A
git commit -m "Add specs for the PostsForBranchService"
```

#### Create a new post

Until now posts were created artificially, by using seeds. Let’s add a user interface for it, so a user could create posts.

Inside the `posts_controller.rb` file add `new` and `create` actions.

```rb
...
  def new
    @branch = params[:branch]
    @categories = Category.where(branch: @branch)
    @post = Post.new
  end

  def create
    @post = Post.new(post_params)
    if @post.save 
      redirect_to post_path(@post) 
    else
      redirect_to root_path
    end
  end
...
```

Inside the `new` action, we define some instance variables for the form to create new posts. Inside the `@categories` instance variable, categories for a specific branch are stored. The `@post` instance variable stores an object of a new post, this is needed for the Rails form.

Inside the `create` action’s `@post` instance variable, we create a new `Post`object and fill it with data, using the `post_params` method. Define this method within the `private` scope:

```rb
...
def post_params
  params.require(:post).permit(:content, :title, :category_id)
                       .merge(user_id: current_user.id)
end
...
```

The `[permit](https://apidock.com/rails/ActionController/Parameters/permit)` method is used to whitelist attributes of the object, so only these specified attributes are allowed to be passed.

Also at the top of the `PostsController`, add the following line:

```rb
...
before_action :redirect_if_not_signed_in, only: [:new]
...
```

The `before_action` is one of the Rails [filters](http://guides.rubyonrails.org/action_controller_overview.html#filters).  We don’t want to allow for not signed in users to have an access to a  page where they can create new posts. So before calling the `new` action, the `redirect_if_not_signed_in` method is called. We’ll need this method across other controllers too, so define it inside the `application_controller.rb` file. Also a method to redirect signed in users would be useful in the future too. So define them both.

```rb
...
def redirect_if_not_signed_in
  redirect_to root_path if !user_signed_in?
end

def redirect_if_signed_in
  redirect_to root_path if user_signed_in?
end
...
```

Now the `new` template is required, so a user could create new posts. Inside the `posts` directory, create a `new.html.erb` file:

```html
<div class="container new-post">
  <div class="row">
    <div class="col-sm-6 col-sm-offset-3">
      <h1>Create a new post</h1>
        <%= render 'posts/new/post_form' %>
    </div>
  </div>
</div>
```

Create a `new` directory and a `_post_form.html.erb` partial file inside:

```html
<%= bootstrap_form_for(@post) do |f| %>
  <%= f.text_field  :title, 
                    maxlength: 100, 
                    placeholder: 'Title', 
                    class: 'form-control',
                    required: true, 
                    minlength: 5,
                    maxlength: 100 %>
  <%= f.hidden_field :branch, :value => @branch %>
  <%= f.text_area :content, 
                  rows: 6,
                  required: true, 
                  minlength: 20,
                  maxlength: 1000,
                  placeholder: 'Describe what you are looking for. E.g. specific interests, expertise level, etc.', 
                  class: 'form-control' %>
  <%= f.collection_select :category_id, @categories, :id, :name, class: 'form-control' %>
  <%= f.submit "Create a post", class: 'form-control' %>
<% end %>
```

The form is pretty straightforward. Attributes of the fields are defined and the `collection_select` method is used to allow to select one of the available categories.

Commit the changes

```bash
git add -A
git commit -m "Create a UI to create new posts
- Inside the PostsController: 
  define new and create actions
  define a post_params method
  define a before_action filter
- Inside the ApplicationController:
  define a redirect_if_not_signed_in method
  define a redirect_if_signed_in method
- Create a new template for posts"
```

We can test if the form works by writing specs. Start by writing [request specs](https://relishapp.com/rspec/rspec-rails/docs/request-specs/request-spec), to make sure that we get correct responses after we send particular requests. Inside the `spec` directory create a couple directories.

```
spec/requests/posts
```

And a `new_spec.rb` file inside:

```rb
require 'rails_helper'
include Warden::Test::Helpers
RSpec.describe "new", :type => :request do

  context 'non-signed in user' do
    it 'redirects to a root path' do
      get '/posts/new'
      expect(response).to redirect_to(root_path)
    end
  end

  context 'signed in user' do
    let(:user) { create(:user) }
    before(:each) { login_as user }

    it 'renders a new template' do
      get '/posts/new'
      expect(response).to render_template(:new)
    end
  end

end
```

As  mentioned in the documentation, request specs provide a thin wrapper  around the integration tests. So we test if we get correct responses  when we send certain requests. The `include Warden::Test::Helpers` line is required in order to use `login_as` method. The method logs a user in.

Commit the change.

```bash
git add -A
git commit -m "Add request specs for a new post template"
```

We can even add some more request specs for the pages which we created previously.

Inside the same directory create a `branches_spec.rb` file:

```rb
require 'rails_helper'
include Warden::Test::Helpers
RSpec.describe "branches", :type => :request do

  shared_examples 'render_templates' do
    it 'renders a hobby template' do
      get '/posts/hobby'
      expect(response).to render_template(:hobby)
    end

    it 'renders a study template' do
      get '/posts/study'
      expect(response).to render_template(:study)
    end

    it 'renders a team template' do
      get '/posts/team'
      expect(response).to render_template(:team)
    end
  end

  context 'non-signed in user' do
    it_behaves_like 'render_templates'
  end

  context 'signed in user' do
    let(:user) { create(:user) }
    before(:each) { login_as user }

    it_behaves_like 'render_templates'
  end

end
```

This way we check that all branch pages’ templates successfully render. Also the `[shared_examples](https://relishapp.com/rspec/rspec-core/docs/example-groups/shared-examples)` is used to reduce the repetitive code.

Commit the change.

```bash
git add -A
git commit -m "Add request specs for Posts branch pages' templates"
```

Also we can make sure that the `show` template renders successfully. Inside the same directory create a `show_spec.rb` file:

```rb
require 'rails_helper'
include Warden::Test::Helpers
RSpec.describe "show", :type => :request do

  shared_examples 'render_show_template' do
    let(:post) { create(:post) }
    it 'renders a show template' do
      get post_path(post)
      expect(response).to render_template(:show)
    end
  end

  context 'non-signed in user' do
    it_behaves_like 'render_show_template'
  end

  context 'signed in user' do
    let(:user) { create(:user) }
    before(:each) { login_as user }

    it_behaves_like 'render_show_template'
  end

end
```

Commit the changes.

```bash
git add -A
git commit -m "Add request specs for the Posts show template"
```

To make sure that a user is able to create a new post, write feature specs to test the form. Inside the `features/posts` directory create a new file `create_new_post_spec.rb`

```rb
require "rails_helper"

RSpec.feature "Create a new post", :type => :feature do
  let(:user) { create(:user) }
  before(:each) { sign_in user }

  shared_examples 'user creates a new post' do |branch|
    scenario 'successfully' do
      create(:category, name: 'category', branch: branch)
      visit send("#{branch}_posts_path")
      find('.new-post-button').click
      fill_in 'post[title]', with: 'a' * 20
      fill_in 'post[content]', with: 'a' * 20
      select 'category', from: 'post[category_id]' 
      click_on 'Create a post'
      expect(page).to have_selector('h3', text: 'a' * 20)
    end
  end

  include_examples 'user creates a new post', 'hobby'
  include_examples 'user creates a new post', 'study'
  include_examples 'user creates a new post', 'team'
end
```

Commit the changes.

```bash
git add -A
git commit -m "Create a create_new_post_spec.rb file with feature specs"
```

Apply some design to the `new` template.

Within the following directory:

```
assets/stylesheets/partials/posts
```

Create a `new.scss` file:

```scss
.new-post {
  height: calc(100vh - 50px);
  background-color: white;
  h1 {
    text-align: center;
    margin: 25px 0;
  }
  input, textarea, select {
    width: 100%;
  }
}
```

If you go to the template in a browser now, you should see a basic form

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-94.png)

Commit the changes

```bash
git add -A
git commit -m "Add CSS to the Posts new.html.erb template"
```

Finally, we want to make sure that all fields are filled correctly. Inside the `Post` model we’re going to define some [validations](http://guides.rubyonrails.org/active_record_validations.html). Add the following code to the `Post`model:

```rb
...
validates :title, presence: true, length: { minimum: 5, maximum: 255 }
validates :content, presence: true, length: { minimum: 20, maximum: 1000 }
validates :category_id, presence: true
...
```

Commit the changes.

```bash
git add -A
git commit -m "Add validations to the Post model"
```

Cover these validations with specs. Go to the `Post` model’s spec file:

```
spec/models/post_spec.rb
```

Then add:

```rb
context 'Validations' do
  let(:post) { build(:post) }

  it 'creates succesfully' do 
    expect(post).to be_valid
  end

  it 'is not valid without a category' do 
    post.category_id = nil
    expect(post).not_to be_valid
  end

  it 'is not valid without a title' do 
    post.title = nil
    expect(post).not_to be_valid
  end

  it 'is not valid  without a user_id' do
    post.user_id = nil
    expect(post).not_to be_valid
  end

  it 'is not valid  with a title, shorter than 5 characters' do 
    post.title = 'a' * 4
    expect(post).not_to be_valid
  end

  it 'is not valid  with a title, longer than 255 characters' do 
    post.title = 'a' * 260
    expect(post).not_to be_valid
  end

  it 'is not valid without a content' do 
    post.content = nil
    expect(post).not_to be_valid
  end

  it 'is not valid  with a content, shorter than 20 characters' do 
    post.content = 'a' * 10
    expect(post).not_to be_valid
  end

  it 'is not valid  with a content, longer than 1000 characters' do 
    post.content = 'a' * 1050
    expect(post).not_to be_valid
  end
end 
```

Commit the changes.

```bash
git add -A
git commit -m "Add specs for the Post model's validations"
```

Merge the `specific_branches` branch with the `master`

```bash
git checkout -b master
git merge specific_branches
git branch -D specific_branches
```

### Instant Messaging

Users  are able to publish posts and read other users’ posts, but they have no  ability to communicate with each other. We could create a simple mail  box system, which would be much easier and faster to develop. But that  is a very old way to communicate with someone. Real time communication  is much more exciting to develop and comfortable to use.

Fortunately, Rails has [Action Cables](http://edgeguides.rubyonrails.org/action_cable_overview.html) which makes real time features’ implementation relatively easy. The core concept behind the Action Cables is that it uses a [WebSockets Protocol](https://en.wikipedia.org/wiki/WebSocket) instead of [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol).  And the core concept of WebSockets is that it establishes a  client-server connection and keeps it open. This means that no page  reloads are required to send and receive additional data.

#### Private conversation

The goal of this section is to create a working feature which would allow to have a private conversation between two users.

Switch to a new branch

```bash
git checkout -B private_conversation
```

**Namespacing models**

Start  by defining necessary models. We’ll need two different models for now,  one for private conversations and another for private messages. We could  name them `PrivateConversation` and `PrivateMessage`, but you can quickly encounter a little problem. While everything would work fine, imagine how the `models` directory would start to look like after we create more and more models  with similar name prefixes. The directory would become hardly  manageable in no time.

To avoid chaotic structure inside directories, we can use a namespacing technique.

Let’s see how it would look like. An ordinary model for private conversation would be called `PrivateConversation` and its file would be called `private_conversation.rb`, and stored inside the `models` directory

```
models/private_conversation.rb
```

Meanwhile, the namespaced version would be called `Private::Conversation`. The file would be called `conversation.rb` and located inside the `private`directory

```
models/private/conversation.rb
```

Can you see how it might be useful? All files with the `private` prefix would be stored inside the `private` directory, instead of accumulating inside the main `models` directory and making it hardly to read.

As  usually, Rails makes the development process enjoyable. We’re able to  create namespaced models by specifying a directory which we want to put a  model in.

To create the namespaced `Private::Conversation` model run the following command:

```
rails g model private/conversation
```

Also generate the `Private::Message` model:

```
rails g model private/message
```

If you look at the `models` directory, you will see a `private.rb` file. This is required to add prefix to database tables’ names, so  models could be recognized. Personally I don’t like keeping those files  inside the `models`directory, I prefer to specify a table’s name inside a model itself. To specify a table’s name inside a model, you have to use `self.table_name =` and provide a table’s name as a string. If you choose to specify names  of database tables this way, like I do, then the models should look like  this:

```rb
class Private::Conversation < ApplicationRecord
  self.table_name = 'private_conversations'
end
```

```rb
class Private::Message < ApplicationRecord
  self.table_name = 'private_messages'
end
```

The `private.rb` file, inside the `models` directory, is no longer needed, you can delete it.

A  user will be able to have many private conversations and conversations  will have many messages. Define these associations inside the models:

```rb
...
has_many :messages, 
         class_name: "Private::Message", 
         foreign_key: :conversation_id
belongs_to :sender, foreign_key: :sender_id, class_name: 'User'
belongs_to :recipient, foreign_key: :recipient_id, class_name: 'User'
...
```

```rb
...
  belongs_to :user
  belongs_to :conversation, 
             class_name: 'Private::Conversation',
             foreign_key: :conversation_id
...
```

```rb
...
has_many :private_messages, class_name: 'Private::Message'
has_many  :private_conversations, 
          foreign_key: :sender_id, 
          class_name: 'Private::Conversation'
...
```

Here the `class_name` method is used to define a name of an associated model. This allows to  use custom names for our associations and make sure that namespaced  models get recognized. Another use case of the `class_name`method  would be to create a relation to itself, this is useful when you want  to differentiate same model’s data by creating some kind of hierarchies  or similar structures.

The `foreign_key` is used to specify a name of association’s column in a database table. A data column in a table is only created on the `belongs_to`association’s side, but to make the column recognizable, we’ve to define the `foreign_key` with same values on both models.

Private conversations are going to be between two users, here these two users are `sender` and `recipient`. We could’ve named them like `user1` and `user2`. But it’s handy to know who initiated a conversation, so the `sender` here is a creator of a conversation.

Define data tables inside the migration files:

```rb
class CreatePrivateConversations < ActiveRecord::Migration[5.1]
  def change
    create_table :private_conversations do |t|
      t.integer :recipient_id
      t.integer :sender_id

      t.timestamps
    end
    add_index :private_conversations, :recipient_id
    add_index :private_conversations, :sender_id
    add_index :private_conversations, [:recipient_id, :sender_id], unique: true
  end
end
```

The `private_conversations` table is going to store users’ ids, this is needed for `belongs_to` and `has_many` associations to work and of course to create a conversation between two users.

```rb
class CreatePrivateMessages < ActiveRecord::Migration[5.1]
  def change
    create_table :private_messages do |t|
      t.text :body
      t.references :user, foreign_key: true
      t.belongs_to :conversation, index: true
      t.boolean :seen, default: false
      
      t.timestamps
    end
  end
end
```

Inside the `body` data column, a message’s content is going to be stored. Instead of  adding indexes and id columns to make associations between two models  work, here we used the `references` method, which simplified the implementation.

run migration files to create tables inside the development database

```
rails db:migrate
```

Commit the changes

```bash
git add -A
git commit -m "Create Private::Conversation and Private::Message models
- Define associations between User, Private::Conversation
  and Private::Message models
- Define private_conversations and private_messages tables"
```

**A non-real time private conversation window**

We  have a place to store data for private conversations, but that’s pretty  much it. Where should we start from now? As mentioned in previous  sections, personally I like to create a basic visual side of a feature  and then write some logic to make it functional. I like this approach  because when I have a visual element, which I want to make functional,  it’s more obvious what I want to achieve. Once you have a user  interface, it’s easier to start breaking down a problem into smaller  steps, because you know what should happen after a certain event. It’s  harder to program something that doesn’t exist yet.

To start building the user interface for private conversations, create a `Private::Conversations` controller. Once I namespace something in the app, I like to stay  consistent and namespace all its other related parts too. This allows to  understand and navigate through the source code more intuitively.

```
rails g controller private/conversations
```

Rails generator is pretty sweet. It created a namespaced model and namespaced views, everything is ready for development.

**Create a new conversation**

We  need a way to initiate a new conversation. In a case of our app, it  makes sense that you want to contact a person which has similar  interests to yours. A convenient place for this functionality is inside a  single post’s page.

Inside the `posts/show.html.erb` template, create a form to initiate a new conversation. Below the `<p><%= @post.content %></p>` line add:

```html
...
<%= render contact_user_partial_path %>
...
```

Define the helper method inside the `posts_helper.rb`

```rb
...
def contact_user_partial_path
  if user_signed_in?
    @post.user.id != current_user.id ? 'posts/show/contact_user' : 'shared/empty_partial'
  else 
    'posts/show/login_required'
  end
end
...
```

Add specs for the helper method:

```rb
...
context '#contact_user_partial_path' do
  before(:each) do
    @current_user = create(:user, id: 1)
    helper.stub(:current_user).and_return(@current_user)
  end

  it "returns a contact_user partial's path" do
    helper.stub(:user_signed_in?).and_return(true)
    assign(:post, create(:post, user_id: create(:user, id: 2).id))
    expect(helper.contact_user_partial_path).to(
      eq 'posts/show/contact_user' 
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:user_signed_in?).and_return(true)
    assign(:post, create(:post, user_id: @current_user.id))

    expect(helper.contact_user_partial_path).to(
      eq 'shared/empty_partial'
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:user_signed_in?).and_return(false)
    expect(helper.contact_user_partial_path).to(
      eq 'posts/show/login_required'
    )
  end
end
...
```

Create a `show` directory and the corresponding partial files:

```html
<div class="contact-user">
  <%= render leave_message_partial_path %>
</div><!-- contact-user -->
```

```html
<div class="text-center">
  To contact the user you have to <%= link_to 'Login', login_path %> 
</div>
```

Define the `leave_message_partial_path` helper method inside the `posts_helper.rb`

```rb
...
def leave_message_partial_path
  if @message_has_been_sent
    'posts/show/contact_user/already_in_touch'
  else
    'posts/show/contact_user/message_form'
  end
end
...
```

Add specs for the method

```rb
...
context '#leave_message_partial_path' do
  it "returns an already_in_touch partial's path" do
    assign('message_has_been_sent', true)
    expect(helper.leave_message_partial_path).to(
      eq 'posts/show/contact_user/already_in_touch'
    )
  end

  it "returns an already_in_touch partial's path" do
    assign('message_has_been_sent', false)
    expect(helper.leave_message_partial_path).to(
      eq 'posts/show/contact_user/message_form'
    )
  end
end
...
```

We’ll define the `@message_has_been_sent` instance variable inside the `PostsController` in just a moment, it will determine if an initial message to a user was already sent, or not.

Create partial files, corresponding to the `leave_message_partial_path` helper method, inside a new `contact_user` directory

```html
<div class="contacted-user">
  You are already in touch with this user
</div>
```

```html
<%= form_tag({controller: "private/conversations", action: "create"},
              method: "post",
              remote: true) do %>
  <%= hidden_field_tag(:post_id, @post.id)  %>
  <%= text_area_tag(:message_body,
                    nil,
                    rows: 3,
                    class: 'form-control', 
                    placeholder: 'Send a messsage to the user') %>
  <%= submit_tag('Send a message', class: 'btn send-message-to-user') %>
<% end %>
```

Now configure the `PostsController`’s `show` action. Inside the action add

```rb
...
if user_signed_in?
  @message_has_been_sent = conversation_exist?
end
...
```

Within the controller’s `private` scope, define the `conversation_exist?` method

```rb
...
def conversation_exist?
  Private::Conversation.between_users(current_user.id, @post.user.id).present?
end
...
```

The `between_users` method queries private conversations between two users. Define it as a scope inside the `Private::Conversation` model

```rb
...
scope :between_users, -> (user1_id, user2_id) do
  where(sender_id: user1_id, recipient_id: user2_id).or(
    where(sender_id: user2_id, recipient_id: user1_id)
  )
end
...
```

We have to test if the scope works. Before writing specs, define a `private_conversation` factory, because we’ll need sample data inside the test database.

```rb
FactoryGirl.define do
  factory :private_conversation, class: 'Private::Conversation' do
    association :recipient, factory: :user
    association :sender, factory: :user

    factory :private_conversation_with_messages do
      transient do
        messages_count 1
      end

      after(:create) do |private_conversation, evaluator|
        create_list(:private_message, evaluator.messages_count, 
                     conversation: private_conversation)
      end
    end
  end
end
```

We see a nested factory here, this allows to create a factory with its  parent’s configuration and then modify it. Also because we’ll create  messages with the `private_conversation_with_messages` factory, we need to define the `private_message` factory too

```rb
FactoryGirl.define do 
  factory :private_message, class: 'Private::Message' do
    body 'a' * 20
    association :conversation, factory: :private_conversation
    user
  end
end
```

Now we have everything ready to test the `between_users` scope with specs.

```rb
...
context 'Scopes' do
  it 'gets a conversation between users' do
    user1 = create(:user)
    user2 = create(:user)
    create(:private_conversation, recipient_id: user1.id, sender_id: user2.id)
    conversation = Private::Conversation.between_users(user1.id, user2.id)
    expect(conversation.count).to eq 1
  end
end
...
```

Define the `create` action for the `Private::Conversations` controller

```rb
...
def create
  recipient_id = Post.find(params[:post_id]).user.id
  conversation = Private::Conversation.new(sender_id: current_user.id, 
                                           recipient_id: recipient_id)
  if conversation.save
    Private::Message.create(user_id: recipient_id, 
                            conversation_id: conversation.id, 
                            body: params[:message_body])
    respond_to do |format|
      format.js {render partial: 'posts/show/contact_user/message_form/success'}
    end
  else
    respond_to do |format|
      format.js {render partial: 'posts/show/contact_user/message_form/fail'}
    end
  end
end
...
```

Here we create a conversation between a post’s author and a current user. If everything goes well, the app will create a message, written by a current user, and give a feedback by rendering a corresponding JavaScript partial.

Create these partials

```js
$('.contact-user').replaceWith('\
    <div class="contact-user">\
        <div class="contacted-user">Message has been sent</div>\
    </div>');
```

```js
$('.contact-user').replaceWith('<div>Message has not been sent</div>');
```

Create routes for the `Private::Conversations` and `Private::Messages`controllers

```rb
...
namespace :private do 
  resources :conversations, only: [:create] do
    member do
      post :close
    end
  end
  resources :messages, only: [:index, :create]
end
...
```

For now we’ll only need few actions, this is where the `only` method is handy. The `namespace` method allows to easily create routes for namespaced controllers.

Test the overall `.contact-user` form’s performance with feature specs

```rb
require "rails_helper"

RSpec.feature "Contact user", :type => :feature do
	let(:user) { create(:user) }
	let(:category) { create(:category, name: 'Arts', branch: 'hobby') }
	let(:post) { create(:post, category_id: category.id) }

  context 'logged in user' do
    before(:each) do
      sign_in user 
    end

    scenario "successfully sends a message to a post's author", js: true do
      visit post_path(post)
      expect(page).to have_selector('.contact-user form')

      fill_in('message_body', with: 'a' * 20)
      find('form .send-message-to-user').trigger('click')

      expect(page).not_to have_selector('.contact-user form')
      expect(page).to have_selector('.contacted-user', 
                                      text: 'Message has been sent')
    end

    scenario 'sees an already contacted message' do
      create(:private_conversation_with_messages, 
              recipient_id: post.user.id, 
              sender_id: user.id)
      visit post_path(post)
      expect(page).to have_selector(
        '.contact-user .contacted-user', 
        text: 'You are already in touch with this user')
    end
  end

  context 'non-logged in user' do
    scenario 'sees a login required message to contact a user' do
      visit post_path(post)
      expect(page).to have_selector('div', text: 'To contact the user you have to')
    end
  end
end
```

Commit the changes

```bash
git add -A
git commit -m "Inside a post add a form to contact a user
- Define a contact_user_partial_path helper method in PostsHelper. 
  Add specs for the method
- Create _contact_user.html.erb and _login_required.html.erb partials
- Define a leave_message_partial_path helper method in PostsHelper.
  Add specs for the method
- Create _already_in_touch.html.erb and _message_form.html.erb 
  partial files
- Define a @message_has_been_sent in PostsController's show action
- Define a between_users scope inside the Private::Conversation model
  Add specs for the scope
- Define private_conversation and private_message factories
- Define routes for Private::Conversations and Private::Messages
- Define a create action inside the Private::Conversations
- Create _success.js and _fail.js partials
- Add feature specs to test the overall .contact-user form"
```

Change the form’s style a little bit by adding CSS to the `branch_page.scss` file

```scss
...
.send-message-to-user {
  background-color: $navbarColor;
  padding: 10px;
  color: white;
  border-radius: 10px;
  margin-top: 10px;
  &:hover {
    background-color: black;
    color: white;
  }
}

.contact-user {
  text-align: center;
}

.contacted-user {
  display: inline-block;
  border-radius: 10px;
  padding: 10px;
  background-color: $navbarColor;
  color: white;
}
...
```

When you visit a single post, the form should look something like this

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-95.png)

When you send a message to a post’s author, the form disappears

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-96.png)

That’s how it looks like when you are already in touch with a user

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-97.png)

Commit the changes

```bash
git add -A
git commit -m "Add CSS to style the .contact-user form"
```

**Render a conversation window**

We  sent a message and created a new conversation. That is the only our  power right now, we cannot do anything else. What a useless power thus  far. We need a conversation window to read and write messages.

Store  opened conversations’ ids inside the session. This allows to keep  conversations opened in the app until a user closes them or destroys the  session.

Inside the `Private::ConversationsController`’s `create` action call a `add_to_conversations unless already_added?` method if a conversation is successfully saved. Then define the method within the `private` scope

```rb
...
private

def add_to_conversations
  session[:private_conversations] ||= []
  session[:private_conversations] << @conversation.id
end
```

This will store the conversation’s id inside the session. And the `already_added?`private method is going to make sure that the conversation’s id isn’t added inside the session yet.

```rb
def already_added?
  session[:private_conversations].include?(@conversation.id)
end
```

And lastly, we’ll need an access to the conversation inside the views, so convert the `conversation` variable into an instance variable.

Now we can start building a template for the conversation window. Create a partial file for the window

```html
<% @recipient = private_conv_recipient(conversation) %>
<% @is_messenger = false %>
<li class="conversation-window" 
    id="pc<%= conversation.id %>" 
    data-pconversation-user-name="<%= @recipient.name %>" 
    data-turbolinks-permanent>
  <div class="panel panel-default" data-pconversation-id="<%= conversation.id %>">
    <%= render 'private/conversations/conversation/heading', 
                conversation: conversation %>

    <!-- Conversation window's content -->
    <div class="panel-body">
      <%= render 'private/conversations/conversation/messages_list', 
                  conversation: conversation %>
      <%= render 'private/conversations/conversation/new_message_form', 
                  conversation: conversation,
                  user: user %>
    </div><!-- panel-body -->
  </div>
</li><!-- conversation-window -->
```

Here we get the conversation’s recipient with the `private_conv_recipient`method. Define the helper method inside the `Private::ConversationsHelper`

```rb
...
# get the opposite user of the conversation
def private_conv_recipient(conversation)
  conversation.opposed_user(current_user)
end
...
```

The `opposed_user` method is used. Go to the `Private::Conversation` model and define the method

```rb
...
def opposed_user(user)
  user == recipient ? sender : recipient
end
...
```

This will return an opposed user of a private conversation. Make sure that the method works correctly by covering it with specs

```rb
...
context 'Methods' do
  it 'gets an opposed user of the conversation' do
    user1 = create(:user)
    user2 = create(:user)
    conversation = create(:private_conversation,
                           recipient_id: user1.id,
                           sender_id: user2.id)
    opposed_user = conversation.opposed_user(user1)
    expect(opposed_user).to eq user2
  end
end
...
```

Next, create missing partial files for the `_conversation.html.erb` file

```html
<div class="panel-heading conversation-heading">
  <span class="contact-name-notif"><%= @recipient.name %></span>  
</div> <!-- conversation-heading -->

<!-- Close conversation button -->
<%= link_to "X", 
            close_private_conversation_path(conversation), 
            class: 'close-conversation', 
            title: 'Close', 
            remote: true, 
            method: :post %>
```

```html
<div class="messages-list">
  <%= render load_private_messages(conversation), conversation: conversation %>
  <div class="loading-more-messages">
    <i class="fa fa-spinner" aria-hidden="true"></i>
  </div>
  <!-- messages -->
  <ul>
  </ul>
</div>
```

Inside the `Private::ConversationsHelper`, define the `load_private_messages`helper method

```rb
...
# if the conversation has unshown messages, show a button to get them
def load_private_messages(conversation)
  if conversation.messages.count > 0 
    'private/conversations/conversation/messages_list/link_to_previous_messages'
  else
    'shared/empty_partial'
  end 
end
...
```

This will add a link to load previous messages. Create a corresponding partial file inside a new `messages_list` directory

```html
<%= link_to "Load messages", 
            private_messages_path(:conversation_id => conversation.id, 
                                  :messages_to_display_offset => @messages_to_display_offset,
                                  :is_messenger => @is_messenger),
            class: 'load-more-messages', 
            remote: true %>
```

Don’t forget to make sure that everything is fine with the method and write specs for it

```rb
...
context '#load_private_messages' do
  let(:conversation) { create(:private_conversation) }

  it "returns load_messages partial's path" do
    create(:private_message, conversation_id: conversation.id)
    expect(helper.load_private_messages(conversation)).to eq (
      'private/conversations/conversation/messages_list/link_to_previous_messages'
    )
  end

  it "returns empty partial's path" do
    expect(helper.load_private_messages(conversation)).to eq (
      'shared/empty_partial'
    )
  end
end
...
```

Because conversations’ windows are going to be rendered throughout the whole app, it means we’ll need an access to `Private::ConversationsHelper`helper methods. To have an access to all these methods across the whole app, inside the `ApplicationHelper` add

```
include Private::ConversationsHelper
```

Then create the last missing partial file for the conversation’s new message form

```html
<form class="send-private-message">
  <input name="conversation_id" type="hidden" value="<%= conversation.id %>">
  <input name="user_id" type="hidden" value="<%= user.id %>">
  <textarea name="body" rows="3" class="form-control" placeholder="Type a message..."></textarea>
  <input type="submit" class="btn btn-success send-message">
</form>
```

We’ll make this form functional a little bit later.

Now  let’s create a feature that after a user sends a message through an  individual post, the conversation window gets rendered on the app.

Inside the `_success.js.erb` file

```
posts/show/contact_user/message_form/_success.js.erb
```

add

```
<%= render 'private/conversations/open' %>
```

This partial file’s purpose is to add a conversation window to the app. Define the partial file

```js
var conversation = $('body').find("[data-pconversation-id='" + 
                                "<%= @conversation.id %>" + 
                                "']");
var chat_windows_count = $('.conversation-window').length + 1;

if (conversation.length !== 1) {
  $('body').append("<%= j(render 'private/conversations/conversation',\
                                  conversation: @conversation,\
                                  user: current_user) %>");
  conversation = $('body').find("[data-conversation-id='" + 
                                "<%= @conversation.id %>" + 
                                "']");
}

// Toggle conversation window after its creation
$('.conversation-window:nth-of-type(' + chat_windows_count + ')\
   .conversation-heading').click();
// mark as seen by clicking it
setTimeout(function(){ 
  $('.conversation-window:nth-of-type(' + chat_windows_count + ')').click();
 }, 1000);
// focus textarea
$('.conversation-window:nth-of-type(' + chat_windows_count + ')\
   form\
   textarea').focus();

// repositions all conversation windows
positionChatWindows();
```

This  callback partial file is going to be reused in multiple scenarios. To  avoid rendering the same window multiple times, before rendering a  window we check if it already exists on the app. Then we expand the  window and auto focus the message form. At the bottom of the file, the `positionChatWindows()`function  is called to make sure that all conversations’ windows are well  positioned. If we didn’t position them, they would just be rendered at  the same spot, which of course would be unusable.

Now in the `assets` directory create a file which will take care of the conversations’ windows visibility and positioning

```js
$(document).on('turbolinks:load', function() { 
    chat_windows_count = $('.conversation-window').length;
    // if the last visible chat window is not set and conversation windows exist
    // set the last_visible_chat_window variable
    if (gon.last_visible_chat_window == null && chat_windows_count > 0) {
        gon.last_visible_chat_window = chat_windows_count;
    }
    // if gon.hidden_chats doesn't exist, set its value
    if (gon.hidden_chats == null) {
        gon.hidden_chats = 0;
    }
    window.addEventListener('resize', hideShowChatWindow);

    positionChatWindows();
    hideShowChatWindow();
});

function positionChatWindows() {
    chat_windows_count = $('.conversation-window').length;
    // if a new conversation window was added, 
    // set it as the last visible conversation window
    // so the hideShowChatWindow function can hide or show it, 
    // depending on the viewport's width
    if (gon.hidden_chats + gon.last_visible_chat_window !== chat_windows_count) {
        if (gon.hidden_chats == 0) {
            gon.last_visible_chat_window = chat_windows_count;
        }
    }

    // when a new chat window is added, position it to the most left of the list
    for (i = 0; i < chat_windows_count; i++ ) {
        var right_position = i * 410;
        var chat_window = i + 1;
        $('.conversation-window:nth-of-type(' + chat_window + ')')
            .css('right', '' + right_position + 'px');
    }
}

// Hides last conversation window whenever it is close to viewport's left side
function hideShowChatWindow() {
    // if there are no conversation windows, stop the function
    if ($('.conversation-window').length < 1) {
        return;
    }
    // get an offsset of the most left conversation window
    var offset = $('.conversation-window:nth-of-type(' + gon.last_visible_chat_window + ')').offset();
    // if the left offset of the conversation window is less than 50, 
    // hide this conversation window
    if (offset.left < 50 && gon.last_visible_chat_window !== 1) {
        $('.conversation-window:nth-of-type(' + gon.last_visible_chat_window + ')')
            .css('display', 'none');
        gon.hidden_chats++;
        gon.last_visible_chat_window--;
    }
    // if the offset of the most left conversation window is more than 550 
    // and there is a hidden conversation, show the hidden conversation
    if (offset.left > 550 && gon.hidden_chats !== 0) {
        gon.hidden_chats--;
        gon.last_visible_chat_window++;
        $('.conversation-window:nth-of-type(' + gon.last_visible_chat_window + ')')
            .css('display', 'initial');
    }
}
```

Instead  of creating our own functions for setting and getting cookies or  similar way to manage data between JavaScript, we can use the [gon](https://github.com/gazay/gon) gem. An original usage of this gem is to send data from the server side  to JavaScript. But I also find it useful for keeping track of  JavaScript variables across the app. Install and set up the gem by  reading the instructions.

We  keep track of the viewport’s width with an event listener. When a  conversation gets close to the viewport’s left side, the conversation  gets hidden. Once there is enough of free space for a hidden  conversation window, the app displays it again.

On  a page visit we call the positioning and visibility functions to make  sure that all conversations’ windows are in right positions.

We’re  using the bootstrap’s panel component to easily expand and collapse  conversations’ windows. By default they are going to be collapsed and  not interactive at all. To make them toggleable, inside the `javascripts` directory create a new file `toggle_window.js`

```js
$(document).on('turbolinks:load', function() { 

    // when conversation heading is clicked, toggle conversation
    $('body').on('click', 
    	         '.conversation-heading, .conversation-heading-full', 
    	         function(e) {
        e.preventDefault();
        var panel = $(this).parent();
        var panel_body = panel.find('.panel-body');
        var messages_list = panel.find('.messages-list');

        panel_body.toggle(100, function() {
        }); 
    });
});
```

Create a new `conversation_window.scss` file

```
assets/stylesheets/partials/conversation_window.scss
```

And add CSS to style conversations’ windows

```scss
textarea {
  resize: none;
}

.panel {
  margin: 0;
  border: none !important;
}

.panel-heading {
  border-radius: 0;
}

.panel-body {
  position: relative;
  display: none;
  padding: 0 0 5px 0;
}

.conversation-window, .new_chat_window {
  min-width: 400px;
  max-width: 400px;
  position: fixed;
  bottom: 0;
  right: 0;
  list-style-type: none;
}

.conversation-heading, .conversation-heading-full, .new_chat_window {
  background-color: $navbarColor !important;
  color: white !important;
  height: 40px;
  border: none !important;
  a {
    color: white !important;
  }

}

.conversation-heading, .conversation-heading-full {
  padding: 0 0 0 15px;
  width: 360px;
  display: inline-block;
  vertical-align: middle;
  line-height: 40px;
}

.close-conversation, .add-people-to-chat, .add-user-to-contacts, .contact-request-sent {
  color: white;
  float: right;
  height: 40px;
  width: 40px;
  font-size: 20px;
  font-size: 2.0rem;
  border: none;
  background-color: $navbarColor;
}

.close-conversation, .add-user-to-contacts {
  text-align: center;
  vertical-align: middle;
  line-height: 40px;
  font-weight: bold;
}

.close-conversation {
  &:hover {
    border: none;
    background-color: white;
    color: $navbarColor !important;
  }
  &:visited, &:focus {
    color: white;
  }
}

.form-control[disabled] {
  background-color: $navbarColor;
}

.send-private-message, .send-group-message {
  textarea {
    border-radius: 0;
    border: none;
    border-top: 1px solid rgba(0, 0, 0, 0.2);
  }
}

.loading_svg {
  display: none;
}

.loading_svg {
  text-align: center;
}

.messages-list {
  z-index: 1;
  min-height: 300px;
  max-height: 300px;
  overflow-y: auto;
  overflow-x: hidden;
  ul {
    padding: 0;
  }
}

.message-received, .message-sent {
  max-width: 300px;
  word-wrap: break-word;
  z-index: 1;
}

.message-sent {
  position: relative;
  background-color: white;
  border: 1px solid rgba(0, 0, 0, 0.5);
  border-radius: 5px;
  margin: 5px 5px 5px 50px;
  padding: 10px;
  float: right;
}

.message-received {
  background-color: $backgroundColor;
  border-color: #EEEEEE;
  border-radius: 5px;
  margin: 5px 50px 5px 5px;
  padding: 10px;
  float: left;
}

.messages-date {
  width: 100%; 
  text-align: center; 
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
  line-height: 1px; 
  line-height: 0.1rem;
  margin: 20px 0 20px;
  span {
    background: #fff; 
    padding: 0 10px; 
  }
  
}

.load-more-messages {
  display: none;
}

.loading-more-messages {
  font-size: 20px;
  font-size: 2.0rem;
  padding: 10px 0;
  text-align: center;
}

.send-message {
  display: none;
}
```

You  might noticed that there are some classes that haven’t been defined yet  in any HTML file. That’s because the future files, we’ll create in the `views`directory,  are going to have shared CSS with already existent HTML elements.  Instead of jumping back and forth to CSS files multiple times after we  add any minor HTML element, I have included some classes, defined in  future HTML elements, right now. Remember, you can always go to style  sheets and analyze how a particular styling works.

Previously  we’ve saved an id of a newly created conversation inside the session.  It’s time to take an advantage of it and keep the conversation window  opened until a user closes it or destroys the session. Inside the `ApplicationController` define a filter

```
before_action :opened_conversations_windows
```

and then define the `opened_conversations_windows` method

```rb
...
def opened_conversations_windows
  if user_signed_in?
    # opened conversations
    session[:private_conversations] ||= []
    @private_conversations_windows = Private::Conversation.includes(:recipient, :messages)
                                      .find(session[:private_conversations])
  else
    @private_conversations_windows = []
  end
end
...
```

The `[includes](https://apidock.com/rails/ActiveRecord/QueryMethods/includes)` method is used to include the data from associated database tables. In  the near future we’ll load messages from a conversation. If we didn’t  use the `includes` method, we wouldn’t have loaded messages records of a conversation with this query. This would lead to a [N + 1 query](https://secure.phabricator.com/book/phabcontrib/article/n_plus_one/) problem. If we didn’t load messages with the query, an additional query  would be fired for every message. This would significantly impact  performance of the app. Now instead of 100 queries for 100 messages, we  have an only one initial query for any number of messages.

Inside the `application.html.erb` file, just below the `yield` method, add

```html
...
<%= render 'layouts/application/private_conversations_windows' %>
...
```

Create a new `application` directory and inside create the `_private_conversations_windows.html.erb` partial file

```html
<% private_conversations_windows.each do |conversation| %>
  <%= render partial: "private/conversations/conversation",
             locals: { conversation: conversation, 
                       user: current_user } %>
<% end %>
```

Now when we browse through the app, we see opened conversations all the time, no matter what page we are in.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-98.png)

Commit the changes

```bash
git add -A
git commit -m "Render a private conversation window on the app
- Add opened conversations to the session
- Create a _conversation.html.erb file inside private/conversations
- Define a private_conv_recipient helper method in the
  private/conversations_helper.rb
- Define an opposed_user method in Private::Conversation model
  and add specs for it
- Create _heading.html.erb and _messages_list.html.erb files
  inside the private/conversations/conversation
- Define a load_private_messages in private/conversations_helper.rb
  and add specs for it
- Create a _new_message_form.html.erb inside the 
  private/conversations/conversation
- Create a _open.js.erbinside private/conversations
- Create a  position_and_visibility.js inside the
  assets/javascripts/conversations
- Create a  conversation_window.scss inside the
  assets/stylesheets/partials
- Define an opened_conversations_windows helper method in 
  ApplicationController
- Create a _private_conversations_windows.html.erb inside the
  layouts/application
```

**Close a conversation**

The conversation’s close button isn’t functional yet. But we have everything ready to make it so. Inside the `Private::ConversationsController`, define a `close` action

```rb
...
def close
  @conversation_id = params[:id].to_i
  session[:private_conversations].delete(@conversation_id)

  respond_to do |format|
    format.js
  end
end
...
```

When the close button is clicked, this action will be called. The action deletes conversation’s id from the session and then responds with a js partial file, identical to the action’s name. Create the partial file

```js
$('body')
    .find("[data-pconversation-id='" + "<%= @conversation_id %>" + "']")
    .parent()
    .remove();
positionChatWindows();
```

It removes the conversation’s window from the DOM and re-positions the rest of conversations’ windows.

Commit the changes

```bash
git add -A
git commit -m "Make the close conversation button functional
- Define a close action inside the Private::ConversationsController
- Create a close.js.erb inside the private/conversations"
```

**Render messages**

Currently  in the messages list we see a loading icon without any messages. That’s  because we haven’t created any templates for messages. Inside the `views/private`directory, create a `messages` directory. Inside the directory, create a new file

```html
<%= render private_message_date_check(message, previous_message),
           locals: { message: message } %>
<li title="<%= message.created_at.to_s(:time) %>">
  <div class="row">   
    <div class="<%= sent_or_received(message, user) %> <%= seen_or_unseen(message) %>">
      <%= message.body %>
    </div>
  </div>
</li>
```

The `private_message_date_check` helper method checks if this message is written at the same day as a  previous message. If not, it renders an extra line with a new date.  Define the helper method inside the `Private::MessagesHelper`

```rb
module Private::MessagesHelper 
  
  def private_message_date_check(message, previous_message)
    if defined?(previous_message) && previous_message.present? 
      # if messages are not created at the same day
      if previous_message.created_at.to_date != message.created_at.to_date
        @message = message
        'private/messages/message/new_date'
      else
        'shared/empty_partial'
      end 
    else
      'shared/empty_partial'
    end 
  end
end
```

Inside the `ApplicationHelper`, include the `Private::MessagesHelper`, so we could have an access to it across the app

```
include Private::MessagesHelper
```

Write specs for the method. Create a new `messages_helper_spec.rb` file

```rb
require 'rails_helper'
RSpec.describe Private::MessagesHelper, :type => :helper do
  context '#private_message_date_check' do
    let(:message) { create(:private_message) }
    let(:previous_message) { create(:private_message) }

    it "returns new_date partial's path" do
      message.update(created_at: 2.days.ago)
      expect(helper.private_message_date_check(message, previous_message)).to(
        eq 'private/messages/message/new_date'
      )
    end

    it "returns an empty partial's path" do
      expect(helper.private_message_date_check(message, previous_message)).to(
        eq 'shared/empty_partial'
      )
    end

    it "returns an empty partial's path" do
      previous_message = nil
      expect(helper.private_message_date_check(message, previous_message)).to(
        eq 'shared/empty_partial'
      )
    end
  end
end
```

Inside a new `message` directory, create a `_new_date.html.erb` file

```html
<div class="messages-date">
  <span><%= @message.created_at.to_date %></span> 
</div>
```

Then inside the `_message.html.erb` file, we have `sent_or_received` and `seen_or_unseen` helper methods. They return different classes in different cases. Define them inside the `Private::MessagesHelper`

```rb
...
def sent_or_received(message, user)
  user.id == message.user_id ? 'message-sent' : 'message-received'
end

def seen_or_unseen(message)
  message.seen == false ? 'unseen' : ''
end
...
```

Write specs for them:

```rb
...
context '#sent_or_received' do
  let(:user) { create(:user) }
  let(:message) { create(:private_message) }
  it 'returns message-sent' do
    message.update(user_id: user.id)
    expect(helper.sent_or_received(message, user)).to eq 'message-sent'
  end

  it 'returns message-received' do
    expect(helper.sent_or_received(message, user)).to eq 'message-received'
  end
end

context '#seen_or_unseen' do
  let(:message) { create(:private_message) }
  it 'returns unseen' do
    message.update(seen: false)
    expect(helper.seen_or_unseen(message)).to eq 'unseen'
  end

  it 'returns nothing' do
    message.update(seen: true)
    expect(helper.seen_or_unseen(message)).to eq ''
  end
end
...
```

Now we  need a component to load messages into the messages list. Also this  component is going to add previous messages at the top of the list, when  a user scrolls up, until there is no messages left in a conversation.  We are going to have an infinite scroll mechanism for messages, similar  to the one we have in posts’ pages.

Inside the `views/private/messages` directory create a `_load_more_messages.js.erb` file:

```js
<% @id_type = 'pc' %>
<%= render append_previous_messages_partial_path %>
<%= render replace_link_to_private_messages_partial_path %>
```

The `@id_type` instance variable determines a type of the conversation. In the future  we will be able to create not only private conversations, but group too.  This leads to common helper methods and partial files between both  types.

Inside the `helpers` directory, create a `shared` directory. Create a `messages_helper.rb` file and define a helper method

```rb
module Shared::MessagesHelper

  def append_previous_messages_partial_path
    'shared/load_more_messages/window/append_messages' 
  end

end
```

So far the method is pretty dumb. It just returns a partial’s path.  We’ll give some intelligence to it later, when we’ll build extra  features to our messaging system. Right now we won’t have an access to  helper methods, defined in this file, in any other file. We have to  include them inside other helper files. Inside the  
`Private::MessagesHelper`, include methods from the `Shared::MessagesHelper`

```bash
require 'shared/messages_helper'
include Shared::MessagesHelper
```

Inside the shared directory, create few new directories:

```
shared/load_more_messages/window
```

Then create an _append_messages.js.erb file:

```js
// temporary remove load more messages link
// so it cannot be clicked if new messages aren't rendered yet
$('#<%= @id_type %><%= @conversation.id %> .load-more-messages')
    .replaceWith('<span class="load-more-messages"></span>');
// render previous messages
$('#<%= @id_type %><%= @conversation.id %> .messages-list ul')
    .prepend('<%= j render "#{@type}/conversations/messages" %>');
// after new messages are appended, leave a gap at the top of the scrollbar
$('#<%= @id_type %><%= @conversation.id %> .messages-list').scrollTop(400);
```

This code takes care that previous messages get appended to the top of  the messages list. Then define another, again, not that fascinating,  helper method inside the `Private::MessagesHelper`

```rb
def replace_link_to_private_messages_partial_path
  'private/messages/load_more_messages/window/replace_link_to_messages'
end
```

Create the corresponding directories inside the `private/messages` directory and create a `_add_link_to_messages.js.erb` file

```js
$('#<%= @id_type %><%= @conversation.id %> .load-more-messages')
    .replaceWith('\
        <%= j render partial: "private/conversations/conversation/messages_list/link_to_previous_messages",\
                     locals: { conversation: @conversation } %>\
    ');
```

This  file is going to update the link which loads previous messages. After  previous messages are appended, the link is replaced with an updated  link to load older previous messages.

Now  we have all this system, how previous messages get appended to the top  of the messages list. But, if we tried to go to the app and opened a  conversation window, we wouldn’t see any rendered messages. Why? Because  nothing triggers the link to load previous messages. When we open a  conversation window for the first time, we want to see the most recent  messages. We can program the conversation window in a way that once it  gets expanded, the load more messages link gets triggered, to load the  most recent messages. It initiates the first cycle of appending previous  messages and replacing the load more messages link with an updated one.

Inside the `toggle_window.js` file update the `toggle` function to do exactly what is described above

```js
panel_body.toggle(100, function() {
    var messages_visible = $('ul', this).has('li').length;

    // Load first 10 messages if messages list is empty
    if (!messages_visible && $('.load-more-messages', this).length) {
        $('.load-more-messages', this)[0].click(); 
    }
}); 
```

Create an event handler, so whenever a user scrolls up and reaches almost the top of the messages list, the load more messages link will be triggered.

```js
$(document).on('turbolinks:load ajax:complete', function() {
    var iScrollPos = 0;
    var isLoading = false;
    var currentLoadingIcon;

    $(document).ajaxComplete(function() {
        isLoading = false;
        // hide loading icon
        if (currentLoadingIcon !== undefined) {
            currentLoadingIcon.hide();
        }
    });

    $('.messages-list', this).scroll(function () {
        var iCurScrollPos = $(this).scrollTop();
        
        if (iCurScrollPos > iScrollPos) {
            //Scrolling Down
        } else {
           //Scrolling Up
           if (iCurScrollPos < 300 && isLoading == false && $('.load-more-messages', this).length) {
                // trigger link, which loads 10 more messages
                $('.load-more-messages', this)[0].click();
                isLoading = true;

                // select conversation window's loading icon and show it
                currentLoadingIcon = $('.loading-more-messages', this);
                currentLoadingIcon.show();
           }
        }
        iScrollPos = iCurScrollPos;
    });
});
```

When the load more messages link is going to be clicked, a `Private::MessagesController`'s `index` action gets called. That’s the path, we defined to the load previous messages link. Create the controller and its `index`action

```rb
class Private::MessagesController < ActionController::Base
  include Messages

  def index
    get_messages('private', 10)
    @user = current_user
    @is_messenger = params[:is_messenger]
    respond_to do |format|
      format.js { render partial: 'private/messages/load_more_messages' }
    end
  end
end
```

Here we include methods from the `Messages` module. The module is stored inside the `concerns` directory. [ActiveSupport::Concern](http://api.rubyonrails.org/classes/ActiveSupport/Concern.html) is one of the places, where you can store modules which you can later  use in classes. In our case we include extra methods to our controller  from the module. The `get_messages` method comes from the `Messages` module. The reason why it is stored inside the module is that we’ll use  this exact same method in another controller a little bit later. To  avoid code duplication, we make the method more reusable.

I’ve seen some people complaining about the `ActiveSupport::Concern` and suggest not to use it at all. I challenge those people to fight me  in the octagon. I’m kidding :D. This is an independent application and  we can create our app however we like it. If you don’t like `concerns`, there are bunch of other ways to create reusable methods.

Create the module

```rb
require 'active_support/concern'

module Messages
  extend ActiveSupport::Concern

  def get_messages(conversation_type, messages_amount)
    # convert a string into a constant, so the models can be called dynamically
    model = "#{conversation_type.capitalize}::Conversation".constantize
    @conversation = model.find(params[:conversation_id])
    # get previous messages of the conversation
    @messages = @conversation.messages.order(created_at: :desc)
                                      .limit(messages_amount)
                                      .offset(params[:messages_to_display_offset].to_i)
    # set a variable to get another previous messages of the conversation
    @messages_to_display_offset = params[:messages_to_display_offset].to_i + messages_amount

    @type = conversation_type.downcase
    # if messages are the last in the conversation, mark the variable as 0
    # so the load more messages link will be removed
    if @conversation.messages.count < @messages_to_display_offset
      @messages_to_display_offset = 0
    end
  end

end
```

Here we require the `active_support/concern` and then extend our module with `ActiveSupport::Concern`, so Rails knows that it is a concern.

With the `[constantize](https://apidock.com/rails/String/constantize)` method we dynamically create a constant name by inputting a string  value. We call models dynamically. The same method is going to be used  for `Private::Conversation` and `Group::Conversation`models.

After the `get_messages` method sets all necessary instance variables, the `index`action responds with the `_load_more_messages.js.erb` partial file.

Finally,  after messages get appended to the top of the messages list, we want to  remove the loading icon from the conversation window. At the bottom of  the `_load_more_messages.js.erb` file add

```
<%= render remove_link_to_messages %>
```

Now define the `remove_link_to_messages` helper method inside the `Shared::MessagesHelper`

```rb
# if there are no previous messages
def remove_link_to_messages
  if @is_messenger == 'false'
    if @messages_to_display_offset != 0
      'shared/empty_partial'
    else
      'shared/load_more_messages/window/remove_more_messages_link' 
    end
  else
    'shared/empty_partial'
  end
end
```

Try to write specs for the method on your own.

Create the `_remove_more_messages_link.js.erb` partial file

```js
$('#<%= @id_type %><%= @conversation.id %> .loading-more-messages')
    .replaceWith('');
$('#<%= @id_type %><%= @conversation.id %> .load-more-messages')
.replaceWith('');
```

Now in a case, where are no previous messages left, the link to previous messages and the loading icon will be removed.

If  you try to contact a user now, a conversation window will be rendered  with a message, you sent, inside. We’re able to render messages via AJAX  requests.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-99.png)

Commit the changes.

```bash
git add -A
git commit -m "Render messages with AJAX

- Create a _message.html.erb inside private/messages
- Define a private_message_date_check helper method in 
  Private::MessagesHelper and write specs for it
- Create a _new_date.html.erb inside private/messages/message
- Define sent_or_received and seen_or_unseen helper methods in
  Private::MessagesHelper and write specs for them
- Create a _load_more_messages.js.erb inside private/messages
- Define an  append_previous_messages_partial_path helper method in
  Shared::MessagesHelper
- Create a _append_messages.js.erb inside
  shared/load_more_messages/window
- Define a  replace_link_to_private_messages_partial_path in
  Private::MessagesHelper
- Create a _add_link_to_messages.js.erb inside 
  private/messages/load_more_messages/window
- Create a toggle_window.js inside javascripts/conversations
- Create a messages_infinite_scroll.js inside
  assets/javascripts/conversations
- Define an index action inside the Private::MessagesController
- Create a messages.rb inside controllers/concerns
- Define a remove_link_to_messages inside helpers/shared
- Create a _remove_more_messages_link.js.erb inside 
  shared/load_more_messages/window"
```

#### **Real time functionality with Action Cable**

Conversations’  windows look pretty neat already. And they also have some sweet  functionality. But, they are lacking the most important  feature — ability to send and receive messages in real time.

As briefly discussed previously, [Action Cable](http://guides.rubyonrails.org/action_cable_overview.html) will allow us to achieve the desired real time feature for  conversations. You should skim through the documentation to be aware how  it all works.

The  first thing which we should do is create a WebSocket connection and  subscribe to a specific channel. Luckily, WebSocket connections are  already covered by default Rails configuration. Inside the `app/channels/application_cable` directory you see `channel.rb` and `connection.rb` files. The `Connection` class takes care of the authentication and the `Channel` class is a parent class to store shared logic between all channels.

Connection is set by default. Now we need a private conversation channel to subscribe to. Generate a namespaced channel

```
rails g channel private/conversation
```

Inside the generated `Private::ConversationChannel`, we see `subscribed` and `unsubscribed` methods. With the `subscribed` method a user creates a connection to the channel. With the `unsubscribed` method a user, obviously, destroys the connection.

Update those methods:

```rb
...
def subscribed
  stream_from "private_conversations_#{current_user.id}"
end

def unsubscribed
  stop_all_streams
end
...
```

Here we  want that a user would have its own unique channel. From the channel a  user will receive and send data. Because users’ ids are unique, we make  the channel unique by adding a user’s id.

This is a server side connection. Now we need to create a connection on the client side too.

To  create an instance of the connection on the client side, we have to  write some JavaScript. Actually, Rails has already created it with the  channel generator. Navigate to `assets/javascripts/channels/private` and by default Rails generates `CoffeeScript` files. I’m going to use JavaScript here. So rename the file to `conversation.js` and replace its content with:

```js
App.private_conversation = App.cable.subscriptions.create("Private::ConversationChannel", {
    connected: function() {},
    disconnected: function() {},
    received: function(data) {}
});
```

Restart the server, go to the app, login and check the server log.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-100.png)



We got the connection. The core of the real time communication is set. We’ve a constantly open client-server connection. It means that we can send and receive data from the server without restarting the connection or refreshing a browser, man! A really powerful thing when you think about it. From now we’ll build the messaging system around this connection.

Commit the changes.

```bash
git add -A
git commit -m "Create a unique private conversation channel and subscribe to it"
```

Let’s make the conversation window’s new message form functional. At the bottom of the `assets/javascripts/channels/private/conversations.js` file add this function:

```js
...
$(document).on('submit', '.send-private-message', function(e) {
    e.preventDefault();
    var values = $(this).serializeArray();
    App.private_conversation.send_message(values);
    $(this).trigger('reset');
});
```

The function is going to get values from the new message form and pass them to a `send_message` function. The `send_message` function is going to call a `send_message` method on the server side, which will take care of creating a new message.

Also  take a note, the event handler is on a submit button, but on the  conversation window we don’t have any visible submit buttons. It’s a  design choice. We have to program the conversation window in a way that  submit button is triggered when the enter key is clicked on a keyboard.  This function is going to be used in the future by other features, so  create a `conversation.js` file inside the `assets/javascripts/conversations` directory

```js
$(document).on('turbolinks:load', function() { 
    
    // leave a gap at the top of the conversation windows' scrollbar
    $('.messages-list').scrollTop(500);

    // send a message on Enter key click and leave textarea in its original state
    $(document).on('keydown', 
                   '.conversation-window, .conversation',
                   function(event) {
        if (event.keyCode === 13) {
            // if textarea window is not empty
            if ($.trim($('textarea', this).val())) {
                $('.send-message', this).click();
                event.target.value = "";
                event.preventDefault();
            }  
        }
    });

});

function calculateUnseenConversations() {
    var unseen_conv_length = $('#conversations-menu').find('.unseen-conv').length;
    if (unseen_conv_length) {
        $('#unseen-conversations').css('visibility', 'visible');
        $('#unseen-conversations').text(unseen_conv_length);
    } else {
        $('#unseen-conversations').css('visibility', 'hidden');
        $('#unseen-conversations').text('');
    }
}
```

In the  file we describe some general behavior for conversations’ windows. The  first behavior is to keep the scrollbar away from the top, so previous  messages aren’t loaded when it is not needed. The second function makes  sure that the submit button is triggered on the enter key click and then  cleans input’s value back to an empty string.

Start by creating the `send_message` function inside the `private_conversation`object. Add it below the `received` callback function

```js
...
send_message: function(message) {
    return this.perform('send_message', {
        message: message
    });
}
```

This calls the `send_message` method on the server side and passes the message value. The server side method should be defined inside the `Private::ConversationChannel`. Define the method:

```rb
...
def send_message(data)
  message_params = data['message'].each_with_object({}) do |el, hash|
    hash[el['name']] = el['value']
  end
  Private::Message.create(message_params)
end
```

This will take care of a new message’s creation. The `data` parameter, which we get from the passed argument, is a nested hash. So  to reduce this nested complexity into a single hash, the `[each_with_object](https://apidock.com/rails/Enumerable/each_with_object)` method is used.

If  you try to send a new message inside a conversation’s window, a new  message record will actually be created. It won’t show up on the  conversation window instantly yet, only when you refresh the website. It  would show up, but we haven’t set anything to broadcast newly created  messages to a private conversation’s channel. We’ll implement it in just  a moment. But before we continue and commit changes, quickly recap how  the current messaging system works.

1. A user fills the new message form and submits the message
2. The event handler inside the `javascripts/channels/private/conversations.js` gets a conversation window’s data, a conversation id and a message  value, and triggers the channel instances on the client-side `send_message` function.

3. The `send_message` function on the client side calls the `send_message`method on the server side and passes data to it

4. The `send_message` method on the client side processes provided data and creates a new `Private::Message` record

Commit the changes.

```bash
git add -A
git commit -m "Make a private conversation window's new message form functional
- Add an event handler inside the
  javascripts/channels/private/conversation.js to trigger the submit button
- Define a common behavior among conversation windows inside the
  assets/javascripts/conversations/conversation.js
- Define a send_message function on both, client and server, sides"
```

**Broadcast a new message**

After a new message is created, we want to broadcast it to a corresponding channel somehow. Well, [Active Record Callbacks](http://guides.rubyonrails.org/active_record_callbacks.html) arms us with plenty of useful callback methods for models. There is a `after_create_commit` callback method, which runs whenever a new model’s record gets created. Inside the `Private::Message` model’s file add

```rb
...
after_create_commit do 
  Private::MessageBroadcastJob.perform_later(self, previous_message)
end

def previous_message
  previous_message_index = self.conversation.messages.index(self) - 1
  self.conversation.messages[previous_message_index]
end
...
```

As you see, after a record’s creation, the `Private::MessageBroadcastJob.perform_later` gets called. And what’s that? It’s a background job, handling back-end  operations. It allows to run certain operations whenever we want to. It  could be immediately after a particular event, or be scheduled to run  some time later after an event. If you aren’t familiar with background  jobs, checkout [Active Job Basics](http://guides.rubyonrails.org/active_job_basics.html).

Add specs for the `previous_message` method. If you are going to try run specs now, comment out the `after_create_commit` method. We haven’t defined the `Private::MessageBroadcastJob`, so currently specs would raise an undefined constant error.

```rb
...
context 'Methods' do
  it 'gets a previous message' do
    conversation = create(:private_conversation)
    message1 = create(:private_message, conversation_id: conversation.id)
    message2 = create(:private_message, conversation_id: conversation.id)
    expect(message2.previous_message).to eq message1
  end
end
...
```

Now we can create a background job which will broadcast a newly created message to a private conversation’s channel.

```
rails g job private/message_broadcast
```

Inside the file we see a `perform` method. By default, when you call a job, this method is called. Now  inside the job, process the given data and broadcast it to channel’s  subscribers.

```rb
class Private::MessageBroadcastJob < ApplicationJob
  queue_as :default

  def perform(message, previous_message)
    sender = message.user
    recipient = message.conversation.opposed_user(sender)

    broadcast_to_sender(sender, recipient, message, previous_message)
    broadcast_to_recipient(sender, recipient, message, previous_message)
  end

  private

  def broadcast_to_sender(sender, recipient, message, previous_message)
    ActionCable.server.broadcast(
      "private_conversations_#{sender.id}",
      message: render_message(message, previous_message, sender),
      conversation_id: message.conversation_id,
      recipient_info: recipient
    )
  end

  def broadcast_to_recipient(sender, recipient, message, previous_message)
    ActionCable.server.broadcast(
      "private_conversations_#{recipient.id}",
      recipient: true,
      sender_info: sender,
      message: render_message(message, previous_message, recipient),
      conversation_id: message.conversation_id
    )
  end

  def render_message(message, previous_message, user)
    ApplicationController.render(
      partial: 'private/messages/message',
      locals: { message: message, 
                previous_message: previous_message, 
                user: user }
    )
  end
end
```

Here we  render a message and send it to both channel’s subscribers. Also we  pass some additional key-value pairs to properly display the message. If  we tried to send a new message, users would receive data, but the  message wouldn’t be appended to the messages list. No visible changes  would be made.

When data is broadcasted to a channel, the `received` callback function on the client side gets called. This is where we have an opportunity to append data to the DOM. Inside the `received` function add the following code:

```js
...
received: function(data) {
    // if a link to the conversation in the conversations menu list exists
    // move the link to the top of the conversations menu list
    var conversation_menu_link = $('#conversations-menu ul')
                                     .find('#menu-pc' + data['conversation_id']);
    if (conversation_menu_link.length) {
        conversation_menu_link.prependTo('#conversations-menu ul');
    }
    
    // set variables
    var conversation = findConv(data['conversation_id'], 'p');
    var conversation_rendered = ConvRendered(data['conversation_id'], 'p');
    var messages_visible = ConvMessagesVisiblity(conversation);

    if (data['recipient'] == true) {
        // mark conversation as unseen, after new message is received
        $('#menu-pc' + data['conversation_id']).addClass('unseen-conv');
        // if conversation window exists
        if (conversation_rendered) {
            if (!messages_visible) {
            // change style of conv window when there are unseen messages
            // add an additional class to the conversation's window or something
            }
            conversation.find('.messages-list').find('ul').append(data['message']);
        }
        calculateUnseenConversations();
    }
    else {
        conversation.find('ul').append(data['message']);
    }

    if (conversation.length) {
        // after a new message was appended, scroll to the bottom of the conversation window
        var messages_list = conversation.find('.messages-list');
        var height = messages_list[0].scrollHeight;
        messages_list.scrollTop(height);
    }
}
...
```

Here we see that the sender and the recipient get treated a little bit differently.

```
// change style of conv window when there are unseen messages
// add an additional class to the conversation's window or something
```

I’ve  created this intentionally, so whenever a conversation has unseen  messages, you could style its window however you like it. You can change  a window’s color, make it blink, or whatever you want to.

Also there are `findConv`, `ConvRendered`, `ConvMessagesVisibility` functions used. We’ll use these functions for both type of chats, private and group.

Create a `shared` directory:

```
assets/javascripts/channels/shared
```

Create a `conversation.js` file inside this directory.

```js
// finds a conversation in the DOM
function findConv(conversation_id, type) {
    // if a current conversation is opened in the messenger
    var messenger_conversation = $('body .conversation');
    if (messenger_conversation.length) {
        // conversation is opened in the messenger
        return messenger_conversation;
    } else { 
        // conversation is opened in a popup window
        var data_attr = "[data-" + type + "conversation-id='" + 
                         conversation_id + 
                         "']";
        var conversation = $('body').find(data_attr);
        return conversation;
    }
}

// checks if a conversation window is rendered and visible on a browser
function ConvRendered(conversation_id, type) {
    // if a current conversation is opened in the messenger
    if ($('body .conversation').length) {
        // conversation is opened in the messenger
        // so it automatically means that is visible
        return true;
    } else { 
        // conversation is opened in a popup window
        var data_attr = "[data-" + type + "conversation-id='" + 
                         conversation_id + 
                         "']";
        var conversation = $('body').find(data_attr);
        return conversation.is(':visible');
    }
}

function ConvMessagesVisiblity(conversation) {
    // if current conversation is opened in the messenger
    if ($('body .conversation').length) {
        // conversation is opened in the messenger
        // so it is automatically means that messages are visible
        return true;
    } else {
        // conversation is opened in a popup window
        // check if the window is collapsed or expanded
        var visibility = conversation
                             .find('.panel-body')
                             .is(':visible');
        return visibility;
    }
}
```

A  messenger is mentioned in the code quite a lot and we don’t have the  messenger yet. The messenger is going to be a separate way to open  conversations. To prevent a lot of small changes in the future, I’ve  included cases with the messenger right now.

That’s  it, the real time functionality should work. Both users, the sender and  the recipient, should receive and get displayed new messages on the  DOM. When we send a new message, we should see it instantly appended to  the messages list. But there’s one little problem now. We only have a  one way to render a conversation window. It gets rendered only when a  conversation is created. We’ll add additional ways to render  conversations’ windows in just a moment. But before that, let’s recap  how data reaches channel’s subscribers.

1. After a new `Private::Message` record is created, the `after_create_commit`method gets triggered, which calls the background job
2. `Private::MessageBroadcastJob` processes given data and broadcasts it to channel’s subscribers
3. On the client side the `received` callback function is called, which appends data to the DOM

Commit the changes.

```bash
git add -A
git commit -m "Broadcast a new message
- Inside the Private::Message define an after_create_comit callback method.
- Create a Private::MessageBroadcastJob
- Define a received function inside the
  assets/javascripts/channels/private/conversation.js
- Create a conversation.js inside the
  assets/javascripts/channels/shared"
```

#### **Navigation bar update**

On  the navigation bar we’re going to render a list of user’s  conversations. When a list of conversations is opened, we want to see  conversations ordered by the latest messages. Conversations with the  most recent messages are going to be at the top of the list. This list  should be accessible throughout the whole application. So inside the `ApplicationController`, store ordered user’s conversations inside an instance variable. The way I suggest doing that is define an `all_ordered_conversations` method inside the controller

```rb
def all_ordered_conversations 
  if user_signed_in?
    @all_conversations = OrderConversationsService.new({user: current_user}).call
  end
end
```

Add a `before_action` filter, so the `@all_conversations` instance variable is available everywhere.

```
before_action :all_ordered_conversations
```

And then create an `OrderConversationsService` to take care of conversations’ querying and ordering.

```rb
class OrderConversationsService

  def initialize(params)
    @user = params[:user]
  end

  # get and order conversations by last messages' dates in descending order
  def call
    all_private_conversations = Private::Conversation.all_by_user(@user.id)
                                                     .includes(:messages)
    return all_conversations = all_private_conversations.sort{ |a, b| 
      b.messages.last.created_at <=> a.messages.last.created_at
    }
  end

end
```

Currently  this service only deals with private conversations, that’s the only  type of conversations we’ve developed so far. In the future we’ll mash  private and group conversations together, and sort them by their latest  messages. The `[sort](https://apidock.com/ruby/Array/sort)` method is used to sort an array of conversations. Again, if we didn’t use the `includes`method,  we would experience a N + 1 query problem. Because when we sort  conversations, we check the latest messages’ creation dates of every  conversation and compare them. That’s why with the query we have  included messages’ records.

The `<=>` operator evaluates which `created_at` value is higher. If we used   
`a <=> b`, it would sort a given array in ascending order. When you evaluate values in the opposite way, `b <=> a`, it sorts an array in descending order.

We haven’t defined the `all_by_user` scope inside the `Private::Conversation`model yet. Open the model and define the scope:

```rb
...
scope :all_by_user, -> (user_id) do
  where(recipient_id: user_id).or(where(sender_id: user_id))
end
...
```

Write specs for the service and the scope:

```rb
context 'Scopes' do
  it "gets all user's conversations" do
    create_list(:private_conversation, 5)
    user = create(:user)
    create_list(:private_conversation, 2, recipient_id: user.id)
    create_list(:private_conversation, 2, sender_id: user.id)
    conversations = Private::Conversation.all_by_user(user.id)
    expect(conversations.count).to eq 4
  end 
end
```

```rb
require 'rails_helper'
require './app/services/order_conversations_service.rb'

describe OrderConversationsService do
  context '#call' do
    it 'returns ordered conversations in descending order' do
      user = create(:user)
      conversation1 = create(:private_conversation,
                              sender_id: user.id,
                              messages: [create(:private_message)])
      conversation2 = create(:private_conversation,
                              sender_id: user.id,
                              messages: [create(:private_message)])
      conversations = [conversation2, conversation1]
      expect(OrderConversationsService.new({user: user}).call).to eq conversations
    end
  end
end
```

Commit the changes.

```bash
git add -A
git commit -m "
- Create an OrderConversationsService and add specs for it
- Define an all_by_user scope inside the Private::Conversation
  model and add specs for it"
```

Now inside  views, we have an access to an array of ordered conversations. Let’s  render a list of their links. Whenever a user clicks on any of them, a  conversation window gets rendered on the app. If you recall, our  navigation bar has two major components. Inside one component, elements  are displayed constantly. Within another component, elements collapse on  smaller devices. So inside the navigation’s header, where components  are visible all the time, we’re going to create a drop down menu of  conversations. As usually, to prevent having a large view file, split it  into multiple smaller ones.

Open the navigation’s `_header.html.erb` file and replace its content with the following:

```html
<div class="navbar-header">
  <% nav_header_content_partials.each do |partial_path| %>
    <%= render partial: partial_path %>
  <% end %>
</div><!-- navbar-header -->
```

Now create a `header` directory with a `_toggle_button.html.erb` file inside

```html
<button type="button" 
        class="navbar-toggle collapsed" 
        data-toggle="collapse" 
        data-target="#navbar-collapsible-content" 
        aria-expanded="false">
  <span class="sr-only">Toggle navigation</span>
  <span class="icon-bar"></span>
  <span class="icon-bar"></span>
  <span class="icon-bar"></span>
</button>
```

This is a toggle button which was formerly located inside the `_header.html.erb`file. Create another file inside the `header` directory

```html
<%= link_to 'collabfield', root_path, class: 'navbar-brand' %>
<%= link_to root_path, class: 'navbar-brand brand-mobile' do %>
	<i class="fa fa-home" aria-hidden="true"></i>
<% end %>
```

And this is the home button from the `_header.html.erb`. Also there is an extra link here. On smaller devices we’re going to display an icon, instead of the name of the application.

Look back at the `_header.html.erb` file. There is a helper method `nav_header_content_partials`,  which returns an array of partials’ paths. The reason why we don’t just  render partials one by one is because the array is going to differ in  different cases. Inside the `NavigationHelper` define the method

```rb
# render the navigation header's content
def nav_header_content_partials
  partials = []
  if params[:controller] == 'messengers' 
    partials << 'layouts/navigation/header/messenger_header'
  else # controller is not messengers  
    partials << 'layouts/navigation/header/toggle_button'
    partials << 'layouts/navigation/header/home_button'
    partials << 'layouts/navigation/header/dropdowns' if user_signed_in?
  end
  partials
end
```

Write specs for the methods inside the `navigation_helper_spec.rb`

```rb
context '#nav_header_content_partials' do
  it "returns messenger_header partial's path" do
    controller.params[:controller] = 'messengers'
    partials = ['layouts/navigation/header/messenger_header']
    expect(helper.nav_header_content_partials).to eq partials
  end

  it "returns partials' paths for buttons without dropdowns" do
    controller.params[:controller] = 'not_messengers'
    view.stub(:user_signed_in?).and_return(false)
    partials = ['layouts/navigation/header/toggle_button']
    partials << 'layouts/navigation/header/home_button'
    expect(helper.nav_header_content_partials).to eq partials
  end

  it "returns partials' paths for buttons and dropdowns" do
    controller.params[:controller] = 'not_messengers'
    view.stub("user_signed_in?").and_return(true)
    partials = ['layouts/navigation/header/toggle_button']
    partials << 'layouts/navigation/header/home_button'
    partials << 'layouts/navigation/header/dropdowns'
    expect(helper.nav_header_content_partials).to eq partials
  end
end
```

Now create necessary files to display drop down menus on the navigation bar. Start by creating a `_dropdowns.html.erb` file

```html
<div class='pull-right' id ='conversations-menu'>
  <%= render 'layouts/navigation/header/dropdowns/conversations' %>
</div>
```

Create a `dropdowns` directory with a `_conversations.html.erb` file inside

```html
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
  <i class="fa fa-envelope-o" aria-hidden="true">
    <span id="unseen-conversations"></span>
  </i>
</a>

<ul class="dropdown dropdown-menu" role="menu">
  <% @all_conversations.each do |conversation| %>
    <%= render partial: conversation_header_partial_path(conversation),
               locals: { conversation: conversation, 
                         user_id: current_user.id } %>
  <% end %>
</ul><!-- dropdown-menu -->
```

This where we use the `@all_conversations` instance variable, defined inside the controller before, and render  links to open conversations. Links for different type of conversations  are going to differ. We’ll need to create two different versions of  links for private and group conversations. First define the `conversation_header_partial_path` helper method inside the `NavigationHelper`

```rb
# return a conversation header partial's path
def conversation_header_partial_path(conversation)
  if conversation.class == Private::Conversation
    'layouts/navigation/header/dropdowns/conversations/private_conversation'
  else
    'layouts/navigation/header/dropdowns/conversations/group_conversation'
  end  
end
```

Write specs for it:

```rb
context '#conversation_header_partial_path' do
  it "returns a partial's path for a private conversation's header" do
    conversation = create(:private_conversation)
    expect(helper.conversation_header_partial_path(conversation)). to eq(
      'layouts/navigation/header/dropdowns/conversations/private'
    )
  end

  it "returns a partial's path for a group conversation's header" do
    conversation = create(:group_conversation)
    expect(helper.conversation_header_partial_path(conversation)). to eq(
      'layouts/navigation/header/dropdowns/conversations/group'
    )
  end
end
```

Of course we haven’t done anything with group conversations yet. So you have to comment out the group conversation’s part in specs for a while to avoid failure.

Create a file for private conversations’ links:

```html
<% recipient = private_conv_recipient(conversation) %>
<% seen_status = private_conv_seen_status(conversation) %>
<li id="menu-pc<%= conversation.id %>" 
    class="<%= seen_status %>"
    data-id="<%= conversation.id %>"
    data-type="private">
    <%= link_to recipient.name, 
                open_private_conversation_path(id: conversation.id), 
                remote: true, 
                method: :post,
                class: 'bigger-screen-link' %>
</li>
```

Define the `private_conv_seen_status` helper method inside a new `Shared::ConversationsHelper`

```rb
module Shared::ConversationsHelper

  def private_conv_seen_status(conversation) 
    # if the latest message of a conversation is not created by a current_user
    # and it is unseen, return an unseen-conv value
    not_created_by_user = conversation.messages.last.user_id != current_user.id
    unseen = conversation.messages.last.seen == false
    not_created_by_user && unseen ? 'unseen-conv' : ''
  end
end
```

Add this this module to the `Private::ConversationsHelper`

```include Shared::ConversationsHelper

Inside specs create a `shared` directory with a `conversations_helper_spec.rb`file to test the `private_conv_seen_status` helper method.

```rb
require 'rails_helper'

RSpec.describe Shared::ConversationsHelper, :type => :helper do

  context '#private_conv_seen_status' do
    it 'returns an empty string' do
      current_user = create(:user)
      conversation = create(:private_conversation)
      create(:private_message, 
              conversation_id: conversation.id,
              seen: false, 
              user_id: current_user.id)
      view.stub(:current_user).and_return(current_user)
      expect(helper.private_conv_seen_status(conversation)).to eq ''
    end

    it 'returns an empty string' do
      current_user = create(:user)
      recipient = create(:user)
      conversation = create(:private_conversation)
      create(:private_message, 
              conversation_id: conversation.id,
              seen: true, 
              user_id: recipient.id)
      view.stub(:current_user).and_return(current_user)
      expect(helper.private_conv_seen_status(conversation)).to eq ''
    end

    it 'returns unseen-conv status' do
      current_user = create(:user)
      recipient = create(:user)
      conversation = create(:private_conversation)
      create(:private_message, 
              conversation_id: conversation.id,
              seen: false, 
              user_id: recipient.id)
      view.stub(:current_user).and_return(current_user)
      expect(helper.private_conv_seen_status(conversation)).to eq(
        'unseen-conv'
      )
    end
  end

end
```

When a link to a conversation is clicked, the `Private::Conversation`controller’s `open` action gets called. Define a route to this action. Inside the `routes.rb` file, add a `post :open` member inside the namespaced `privateconversations`resources, just below the `post :close`.

Of course don’t forget to define the action itself inside the controller:

```rb
def open
  @conversation = Private::Conversation.find(params[:id])
  add_to_conversations unless already_added?
  respond_to do |format|
    format.js { render partial: 'private/conversations/open' }
  end
end
```

Now a conversation window should open when you click on its link. The  navigation bar right now is messy, we have to take care of its design.  To style the drop down menus, add CSS to the `navigation.scss` file.

```scss
.brand-mobile {
  font-size: 20px;
  font-size: 2.0rem;
}

.navigation-items {
  position: absolute;
  top: 0;
  left: 50%;
}

.navbar-header {
  .open {
    width: 36px;
  }
}

.non-user-nav-links {
  display: inline-block;
  height: 50px;
  line-height: 50px;
  vertical-align: middle;
  padding-right: 20px;
}

#conversations-menu, #contacts-requests {
  font-size: 20px;
  font-size: 2.0rem;
  height: 50px;
  line-height: 50px;
  padding-right: 10px;

  ul {
    margin: 0;
    position: relative;
    top: 50px;
    right: 200px;
    border-radius: 0 0 5px 5px;
    height: 300px;
    overflow: scroll;
    overflow-x: hidden;
    li {
      a {
        width: 100%;
      }
    }
  }
  .unseen-conv {
    a {
      background: $backgroundColor;
      color: black !important;
    }
  }
}

#unseen-conversations, #unresponded-contact-requests {
  visibility: hidden;
  padding: 1px;
  position: absolute;
  // color: white;
  font-size: 13px;
  font-size: 1.3rem;
}

#unseen-conversations {
  right: 5px;
  background: #E92F2F;
}

#conversations-menu {
  i {
    position: relative;
  }
}

#conversations-list {
  position: fixed;
  bottom: 0;
  right: 0;
  padding: 0;
  .col-sm-2 {
    padding: 0;
  }
}
```

Update the `max-width: 767px` media query inside the `mobile.scss`

```scss
@media screen and (max-width: 767px) {
  .col-sm-10 {
    display: none;
    padding: 0 !important;
    .conversation {
      padding: 50px 0 0 0;
    }
    .private-conversation .messages-list {
      width: 100%;
      right: 0;
    }
    .group-conversation .messages-list {
      width: 100%;
      left: 0;
    }
    .send-private-message, .send-group-message {
      position: fixed;
      bottom: 0;
    }
  }
  .pc-menu {
    display: none !important;
  }
  .single-post-list {
    min-height: 65px;
    max-height: 65px;
    padding: 10px 0;
  }
  .bigger-screen-link, .brand-bigger-screen {
    display: none !important;
  }
  .smaller-screen-link {
    padding: 10px 20px !important;
  }
  .conversation-window {
    display: none !important;
  }
  .navbar-brand {
    margin: 0 !important;
  }
  .mobile-menu {
    i {
      color: white;
    }
    ul {
      padding: 0px;
    }
    a {
      display: block;
      padding: 10px 0px 10px 25px !important;
    }
    a:hover {
      background: white !important;
      color: black !important;
      i {
        color: black;
      }
    }
  }
  .navbar-header {
    #conversations-menu, #messages-page-name {
      a {
        float: left;
      }
      ul {
        position: absolute;
        left: 0;
        width: 100%;
      }
    }
    #conversations-menu {
      width: 40%;
    }
    #messages-page-name  {
      width: 50%;
    }
    #contacts-requests {
      ul {
        position: absolute;
        left: 0;
        width: 100%;
      }
    }
  }
  #side-menu {
    display: none !important;
  }
  #feed {
    padding: 0;
  }
}
```

Update the `min-width: 767px` media query in `desktop.scss`

```scss
@media screen and (min-width: 767px) {
  // scrollbar styling
  ::-webkit-scrollbar-track
  {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    // border-radius: 10px;
    background-color: #F5F5F5;
  }
  ::-webkit-scrollbar
  {
    width: 12px;
    background-color: #F5F5F5;
  }
  ::-webkit-scrollbar-thumb
  {
    // border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    background-color: $navbarColor;
  }
  body nav {
    display: initial !important;
  }
  .smaller-screen-link {
    display: none !important;
  }
  .brand-mobile {
    display: none;
  }
  .mobile-menu {
    display: none !important;
  }
  #conversations-menu, #contacts-requests {
    ul {
      width: 400px;
      top: 0;
    }
  }
}
```

The app looks like this now

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-101.png)

Then you can expand the conversations list

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-102.png)

By clicking on any of the menu links, a conversation window should appear on the app

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-103.png)

If you try to contract the browser’s size, conversations should be hidden one by one

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-104.png)

Also notice that instead of the collabfield logo we have the home page icon now. And the conversations list is still available on smaller screens. Well, if conversations’ windows are hidden on smaller devices, how users are going to communicate on mobile devices? We’ll create a messenger which will be opened instead of a conversation window.

Commit the changes

```bash
git add -A
git commit -m "Render a drop down menu of conversations links
- split layouts/navigation/_header.html.erb file's content into partials
- Create a _toggle_button.erb.html inside layouts/navigation/header
- Create a _home_button.html.erb inside  layouts/navigation/header
- Define a nav_header_content_partials inside NavigationHelper 
  and write specs for it
- Create a _dropdowns.html.erb inside layouts/navigation/header
- Create a _conversation.html.erb inside
  layouts/navigation/header/dropdowns
- Define a conversation_header_partial_path inside NavigationHelper
  and write specs for it
- Create a  _private.html.erb inside 
  layouts/navigation/header/dropdowns/conversations
- Define a private_conv_seen_status inside
  Shared::ConversationsHelper and write specs for it
- Define an open action inside the Private::Conversations controller
- add CSS to style drop down menus on the navigation bar.
  Inside navigation.scss, mobile.scss and desktop.scss"
```

It’s a good time to make sure that all features of the real time messaging works correctly.

Because  we’re adding elements to the DOM dynamically, sometimes elements are  added too late and Capybara thinks that an element doesn’t exist,  because the wait time by default is 2 seconds only. To avoid these  failures, inside the `rails_helper.rb`, change wait time somewhere between 5 to 10 seconds.

```rb
Capybara.default_max_wait_time = 5
```

Inside the `spec/features/private/conversations folder`create a `window_spec.rb` file.

```rb
require "rails_helper"

RSpec.feature "window", :type => :feature do
  let(:user) { create(:user) }
  let(:conversation) { create(:private_conversation, sender_id: user.id) }
  let(:open_window) do
    sign_in user
    visit root_path
    find('#conversations-menu .dropdown-toggle').trigger('click')
    find('#conversations-menu li a').click
    expect(page).to have_selector('.conversation-window')
  end
  before(:each) do 
    conversation
    create(:private_message, conversation_id: conversation.id, user_id: user.id)
  end

  scenario 'user opens a conversation', js: true do
    open_window
  end

  scenario 'user closes a conversation', js: true do 
    open_window
    find('.conversation-window .close-conversation').click
    expect(page).not_to have_selector('.conversation-window')
  end

  scenario 'user sends a message', js: true do 
    open_window
    expect(page).to have_selector('.conversation-window .messages-list li', count: 1)
    find('.conversation-window').fill_in 'body', with: 'hey, mate'
    find('.conversation-window form .send-message', visible: false).trigger('click')
    expect(page).to have_selector('.conversation-window .messages-list li', count: 2)
  end

  scenario 'user collapses and expands a conversation window', js: true do
    open_window
    find('.conversation-window .conversation-heading').click
    expect(page).not_to have_selector('.conversation-window .messages-list')
  end
end
```

Here I haven’t defined specs, to test if a recipient user receives messages in real time. Try to figure out how to write such tests on your own.

Commit the changes

```bash
git add -A
git commit -m "Add specs to test the conversation window's functionality"
```

If you logged in an account which has received messages, you would notice a conversation, marked as an unseen

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-105.png)

At this moment there is no way to mark conversations as seen. By default a new message has an unseen value. Program the app in a way that when a conversation window is opened or clicked, its messages get marked as seen. Also note that currently we only see highlighted unseen conversations when the drop down menu is expanded. In the future we will create a notifications feature, so users will know that they got new messages without expanding anything.

Let’s tackle the first problem. When a conversation is already rendered on the app, but it is collapsed, and a user clicks on the drop down menu’s link to open that conversation, nothing happens. That collapsed conversation stays collapsed. We’ve to add some JavaScript, so in the case of the drop down menu’s link click, the conversation should expand and focus its new message area.

Open the file below and add the code from the Gist to achieve that.

```
assets/javascripts/conversations/toggle_window.js
```

```js
// when the link to open a conversation is clicked
// and the conversation window already exists on the page
// but it is collapsed, expand it
$('#conversations-menu').on('click', 'li', function(e) {
    // get conversation window's id
    var conv_id = $(this).attr('data-id');
    // get conversation's type
    if ($(this).attr('data-type') == 'private') {
        var conv_type = '#pc';
    } else {
        var conv_type = '#gc';
    }
    var conversation_window = $(conv_type + conv_id);

    // if conversation window exists 
    if (conversation_window.length) {
        // if window is collapsed, expand it
        if (conversation_window.find('.panel-body').css('display') == 'none') {
            conversation_window.find('.conversation-heading').click();
        }
        // mark as seen by clicking it and focus textarea
        conversation_window.find('form textarea').click().focus();
    }
});
```

When  you click on a link, to open a conversation window, no matter if a  conversation is already present on the app, or not, it will be expanded.

Now  we need an event handler. After a conversation window which has unseen  messages is clicked, the private conversation client’s side should fire a  callback function. First, define an event handler inside the private  conversation client’s side, at the bottom of the file

```js
$(document).on('click', '.conversation-window, .private-conversation', function(e) {
    // if the last message in a conversation is not a user's message and is unseen
    // mark unseen messages as seen
    var latest_message = $('.messages-list ul li:last .row div', this);
    if (latest_message.hasClass('message-received') && latest_message.hasClass('unseen')) {
        var conv_id = $(this).find('.panel').attr('data-pconversation-id');
        // if conv_id doesn't exist, it means that conversation is opened in messenger
        if (conv_id == null) {
            var conv_id = $(this).find('.messages-list').attr('data-pconversation-id');
        }
        // mark conversation as seen in conversations menu list
        latest_message.removeClass('unseen');
        $('#menu-pc' + conv_id).removeClass('unseen-conv');
        calculateUnseenConversations();
        App.private_conversation.set_as_seen(conv_id);
    }
});

$(document).on('turbolinks:load', function() {
    calculateUnseenConversations();
});
```

A case of messenger’s existence is already included in this snippet of code.

Then, define the callback function inside the `private_conversation` instance, just below the `send_message` function

```js
set_as_seen: function(conv_id) {
    return this.perform('set_as_seen', { conv_id: conv_id });
}
```

Finally, define this method on the server side

```rb
def set_as_seen(data)
  # find a conversation and set its all unseen messages as seen
  conversation = Private::Conversation.find(data["conv_id"].to_i)
  messages = conversation.messages.where(seen: false)
  messages.each do |message|
    message.update(seen: true)
  end
end
```

After a user clicks on a link to open a conversation window or clicks directly on a conversation window, its unseen messages will be marked as seen.

Commit the changes

```bash
git add -A
git commit -m "Add ability to mark unseen messages as seen
- Add an event handler to expand conversation windows inside the
  assets/javascripts/conversations/toggle_window.js
- Add an event handler to mark unseen messages as seen inside the
  assets/javascripts/channels/private/conversation.js
- Define a set_as_seen method for Private::ConversationChannel"
```

Make sure that everything works as we expect by writing the specs.

#### Contacts

To  stay in touch with people, you met on the app, you have to be able to  add them to contacts. We’re missing this functionality right now. Also  having a contacts feature opens a lot of possibilities to create other  features that only users who are accepted as a contact could perform.

Generate a `Contact` model

```
rails g model contact
```

Define associations, validation and a method to find a contact record by providing users’ ids.

```rb
class Contact < ApplicationRecord
  belongs_to :user
  belongs_to :contact, class_name: "User"

  validates_uniqueness_of :user_id, scope: :contact_id

  def self.find_by_users(user_id, contact_id)
    where('user_id = ? AND contact_id = ?', user_id, contact_id).or(
           where('user_id = ? AND contact_id = ?', contact_id, user_id)
         )[0]
  end
end
```

Define the contacts table

```rb
class CreateContacts < ActiveRecord::Migration[5.1]
  def change
    create_table :contacts do |t|
      t.belongs_to :user, index: true
      t.belongs_to :contact, index: true
      t.boolean :accepted, default: false

      t.timestamps
    end
  end
end
```

A factory for contacts is going to be needed. Define it:

```rb
FactoryGirl.define do 
  factory :contact do
    association :user, factory: :user
    association :contact, factory: :user
  end
end
```

Write specs to test the model

```rb
require 'rails_helper'

RSpec.describe Contact, type: :model do

  let(:contact) { build(:contact) }

  context 'Associations' do
    it 'belongs_to user' do
      association = described_class.reflect_on_association(:user)
      expect(association.macro).to eq :belongs_to
    end

    it 'belongs_to contact' do
      association = described_class.reflect_on_association(:contact)
      expect(association.macro).to eq :belongs_to
      expect(association.options[:class_name]).to eq 'User'
    end
  end

  context 'Validations' do
    it 'is valid to create a new contact' do
      expect(contact).to be_valid
    end

    it 'is not valid with the same user' do
      contact = create(:contact)
      duplicate_contact = contact.dup
      expect(duplicate_contact).not_to be_valid
    end
  end

  context 'Methods' do
    it 'finds by users' do
      user1 = create(:user)
      user2 = create(:user)
      contact = create(:contact, user_id: user1.id, contact_id: user2.id)
      expect(Contact.find_by_users(user1.id, user2.id)).to eq contact
    end
  end

end
```

Commit the changes

```bash
git add -A
git commit -m "Create a Contact model and write specs for it"
```

Inside the `User` model’s file, we have to define appropriate associations and also define some methods to help with contacts’ queries.

```rb
has_many :contacts
has_many :all_received_contact_requests,  
          class_name: "Contact", 
          foreign_key: "contact_id"

has_many :accepted_sent_contact_requests, -> { where(contacts: { accepted: true}) }, 
          through: :contacts, 
          source: :contact
has_many :accepted_received_contact_requests, -> { where(contacts: { accepted: true}) }, 
          through: :all_received_contact_requests, 
          source: :user
has_many :pending_sent_contact_requests, ->  { where(contacts: { accepted: false}) }, 
          through: :contacts, 
          source: :contact
has_many :pending_received_contact_requests, ->  { where(contacts: { accepted: false}) }, 
          through: :all_received_contact_requests, 
          source: :user


# gets all your contacts
def all_active_contacts
  accepted_sent_contact_requests | accepted_received_contact_requests
end

# gets your pending sent and received contacts
def pending_contacts
  pending_sent_contact_requests | pending_received_contact_requests
end

# gets a Contact record
def contact(contact)
  Contact.where(user_id: self.id, contact_id: contact.id)[0]
end
```

Cover associations and methods with specs

```rb
context 'Associations' do

  ...
  
  it 'has_many contacts' do
    association = described_class.reflect_on_association(:contacts)
    expect(association.macro).to eq :has_many
  end

  it 'has_many all_received_contact_requests' do
    association = described_class.reflect_on_association(:all_received_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:class_name]).to eq 'Contact'
    expect(association.options[:foreign_key]).to eq 'contact_id'
  end

  it 'has_many accepted_sent_contact_requests' do
    association = described_class.reflect_on_association(:accepted_sent_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:through]).to eq :contacts
    expect(association.options[:source]).to eq :contact
  end

  it 'has_many accepted_received_contact_requests' do
    association = described_class.reflect_on_association(:accepted_received_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:through]).to eq :all_received_contact_requests
    expect(association.options[:source]).to eq :user
  end

  it 'has_many pending_sent_contact_requests' do
    association = described_class.reflect_on_association(:pending_sent_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:through]).to eq :contacts
    expect(association.options[:source]).to eq :contact
  end

  it 'has_many pending_received_contact_requests' do
    association = described_class.reflect_on_association(:pending_received_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:through]).to eq :all_received_contact_requests
    expect(association.options[:source]).to eq :user
  end
end

context 'Methods' do
  let(:user) { build(:user) }
  let(:contact_requests) do
    @user = create(:user)
    create_list(:contact, 2)
    create_list(:contact, 2, accepted: true)
    create(:contact, user_id: @user.id)
    create(:contact, user_id: @user.id, accepted: true)
    create(:contact, contact_id: @user.id)
    create(:contact, contact_id: @user.id, accepted: true)
  end

  it 'accepted_sent_contact_requests gets only accepted requests' do
    contact_requests
    expect(@user.accepted_sent_contact_requests.count).to eq 1
  end

  it 'accepted_received_contact_requests gets only accepted requests' do
    contact_requests
    expect(@user.accepted_received_contact_requests.count).to eq 1
  end

  it 'pending_sent_contact_requests gets only unaccepted requests' do
    contact_requests
    expect(@user.pending_sent_contact_requests.count).to eq 1
  end

  it 'pending_received_contact_requests gets only unaccepted requests' do
    contact_requests
    expect(@user.pending_received_contact_requests.count).to eq 1
  end
end
```

Commit the changes

```bash
git add -A
git commit -m "Add associations and helper methods to the User model
- Create relationship between the User the Contact models
- Methods help query the Contact records"
```

Generate a `Contacts` controller and define its actions

```
rails g controller contacts
```

```rb
class ContactsController < ApplicationController

  def create
    @contact = current_user.contacts.create(contact_id: params[:contact_id])
    respond_ok
  end

  def update
    @contact = Contact.find_by_users(params[:id], current_user.id)
    @contact.update(accepted: true)
    respond_ok
  end

  def destroy
    @contact = Contact.find_by_users(params[:id], current_user.id)
    @contact.destroy
    respond_ok
  end

  private

  def respond_ok
    respond_to do |format|
      format.json  { head :ok } 
    end
  end

end
```

As you  see, users will be able to create a new contact record, update its  status (accept a user to their contacts) and remove a user from their  contact list. Because all actions are called via AJAX and we don’t want  to render any templates as a response, we respond with a success  response. This way Rails doesn’t have to think what to respond with.

Define the corresponding routes:

```rb
resources :contacts, only: [:create, :update, :destroy]
```

Commit the changes.

```bash
git add -A
git commit -m "Create a ContactsController and define routes to its actions"
```

#### **Private conversation’s window update**

The  way users are going to be able to send and accept contact requests is  through a private conversation’s window. Later we’ll add an extra way to  accept requests through a navigation bar’s drop down menu.

Create a new `heading` directory

```
private/conversations/conversation/heading
```

This is where we’ll keep extra options for a private conversation’s window. Inside the directory, create a `_add_user_to_contacts.html.erb` file

```html
<%= link_to contacts_path(contact_id: @recipient), 
            method: :post, 
            remote: true, 
            class: 'add-user-to-contacts add-user-to-contacts-notif' do %>
  <i class="fa fa-user-plus" aria-hidden="true" title="Add to contacts"></i>
<% end %>
```

At the bottom of the `_heading.html.erb` file, render the option to add the conversation’s opposite user to contacts:

```html
<%= render add_to_contacts_partial_path(@contact) %>
```

Define the helper method and additional methods within a private scope

```rb
# decide to show an option or not
def add_to_contacts_partial_path(contact)
  if recipient_is_contact? 
    'shared/empty_partial'
  else 
    non_contact(contact)
  end 
end

private

def recipient_is_contact?
  # check if recipient is a user's contact
  contacts = current_user.all_active_contacts
  contacts.find {|contact| contact['id'] == @recipient.id}.present?
end

def non_contact(contact)
  # if the contact request was sent by the user or recipient 
  if unaccepted_contact_exists(contact)
    'shared/empty_partial'
  else 
    # contact requests wasn't sent by any users 
    'private/conversations/conversation/heading/add_user_to_contacts' 
  end
end

def unaccepted_contact_exists(contact)
  # get a contact status with the recipient
  if contact.present?
    # check if an unaccepted contact between a user and a recipient exists
    contact.accepted ? false : true
  else
    false
  end
end
```

Write specs for these helper methods

```rb
context '#add_to_contacts_partial_path' do
  let(:contact) { create(:contact) }

  it "returns an empty partial's path" do
    helper.stub(:recipient_is_contact?).and_return(true)
    expect(helper.add_to_contacts_partial_path(contact)).to eq(
      'shared/empty_partial'
    )
  end

  it "returns add_user_to_contacts partial's path" do
    helper.stub(:recipient_is_contact?).and_return(false)
    helper.stub(:unaccepted_contact_exists).and_return(false)
    expect(helper.add_to_contacts_partial_path(contact)).to eq(
      'private/conversations/conversation/heading/add_user_to_contacts' 
    )
  end
end

context 'private scope' do
  let(:current_user) { create(:user) }
  let(:recipient) { create(:user) }

  context '#unaccepted_contact_exists' do
    it 'returns false' do
      contact = create(:contact, accepted: true)
      expect(helper.instance_eval {
        unaccepted_contact_exists(contact)
      }).to eq false
    end

    it 'returns false' do
      contact = nil
      expect(helper.instance_eval {
        unaccepted_contact_exists(contact)
      }).to eq false
    end

    it 'returns true' do
      contact = create(:contact, accepted: false)
      expect(helper.instance_eval {
        unaccepted_contact_exists(contact)
      }).to eq true
    end
  end

  context '#recipient_is_contact?' do
    it 'returns false' do
      helper.stub(:current_user).and_return(current_user)
      assign(:recipient, recipient)
      create_list(:contact, 2, user_id: current_user.id, accepted: true)
      expect(helper.instance_eval { recipient_is_contact? }).to eq false
    end

    it 'returns true' do
      helper.stub(:current_user).and_return(current_user)
      assign(:recipient, recipient)
      create_list(:contact, 2, user_id: current_user.id, accepted: true)
      create(:contact, 
              user_id: current_user.id, 
              contact_id: recipient.id, 
              accepted: true)
      expect(helper.instance_eval { recipient_is_contact? }).to eq true
    end
  end
end
```

The `instance_eval` method is used to test methods within a private scope.

Because  we’re going to display options on the conversation window’s heading  element, we have to make sure that additional options fit perfectly on  the heading. Inside the `_heading.html.erb` file, replace the `conversation-heading`  
class with `<%= conv_heading_class(@contact) %>`, to determine which class to add.

Define the helper method

```rb
# decide which conversation heading style to show
def conv_heading_class(contact)
  # show a conversation heading without or with options
  if unaccepted_contact_exists(contact)
   'conversation-heading-full'
  else
   'conversation-heading'
  end
end
```

Write specs for the method

```rb
context '#conv_heading_class' do
  let(:contact) { create(:contact) }

  it 'returns a conversation-heading-full class' do
    contact.update(accepted: false)
    expect(helper.conv_heading_class(contact)).to eq 'conversation-heading-full'
  end

  it 'returns a conversation-heading class' do
    contact.update(accepted: true)
    expect(helper.conv_heading_class(contact)).to eq 'conversation-heading'
  end
end
```

The options, to send or accept a contact request, won’t be shown yet. More elements need to be added. Open the `_conversation.html.erb` file

```
private/conversations/_conversation.html.erb
```

At the top of the file, define a `@contact` instance variable, so it is accessible across all partials

```html
<% @contact = get_contact_record(@recipient) %>
```

Define the `get_contact_record` helper method

```rb
def get_contact_record(recipient)
  contact = Contact.find_by_users(current_user.id, recipient.id)
end
```

Cover the method with specs

```rb
context '#get_contact_record' do
  it 'returns a Contact record' do
    contact = create(:contact, user_id: current_user.id, contact_id: recipient.id)
    helper.stub(:current_user).and_return(current_user)
    expect(helper.get_contact_record(recipient)).to eq contact
  end
end
```

Previously, we used `current_user` and `recipient` `let` methods only within a private scope’s context. Now we need access to  them on both private and public methods. So cut and place them outside  of private scope’s context.

At the top of the `.panel-body` element, render a partial file which will show an extra message window to accept or decline a contact request

```html
<%= render 'private/conversations/conversation/request_status' %>
```

Create the `_request_status.html.erb` file

```html
<%= render unaccepted_contact_request_partial_path(@contact) %>
<%= render not_contact_no_request_partial_path(@contact) %>
```

Define the needed helper methods

```rb
# show an unaccepted contact request's status if any
def unaccepted_contact_request_partial_path(contact)
  if unaccepted_contact_exists(contact) 
    if request_sent_by_user(contact)
      "private/conversations/conversation/request_status/sent_by_current_user"  
    else
      "private/conversations/conversation/request_status/sent_by_recipient" 
    end
  else
    'shared/empty_partial'
  end
end

# show a link to send a contact request
# if an opposite user is not in contacts and no requests exist
def not_contact_no_request_partial_path(contact)
  if recipient_is_contact? == false && unaccepted_contact_exists(contact) == false
    "private/conversations/conversation/request_status/send_request"
  else
    'shared/empty_partial'
  end
end

private

def request_sent_by_user(contact)
  # true if contact request was sent by the current_user 
  # false if it was sent by a recipient
  contact['user_id'] == current_user.id
end
```

Writes specs for the helper methods

```rb
context '#unaccepted_contact_request_partial_path' do
  let(:contact) { contact = create(:contact) }

  it "returns sent_by_current_user partial's path" do
    helper.stub(:unaccepted_contact_exists).and_return(true)
    helper.stub(:request_sent_by_user).and_return(true)
    expect(helper.unaccepted_contact_request_partial_path(contact)).to eq(
      'private/conversations/conversation/request_status/sent_by_current_user' 
    )
  end

  it "returns sent_by_recipient partial's path" do
    helper.stub(:unaccepted_contact_exists).and_return(true)
    helper.stub(:request_sent_by_user).and_return(false)
    expect(helper.unaccepted_contact_request_partial_path(contact)).to eq(
      'private/conversations/conversation/request_status/sent_by_recipient'
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:unaccepted_contact_exists).and_return(false)
    expect(helper.unaccepted_contact_request_partial_path(contact)).to eq(
      'shared/empty_partial'
    )
  end
end

context '#not_contact_no_request' do
  let(:contact) { contact = create(:contact) }

  it "returns send_request partial's path" do
    helper.stub(:recipient_is_contact?).and_return(false)
    helper.stub(:unaccepted_contact_exists).and_return(false)
    expect(helper.not_contact_no_request_partial_path(contact)).to eq(
      'private/conversations/conversation/request_status/send_request'
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:recipient_is_contact?).and_return(true)
    helper.stub(:unaccepted_contact_exists).and_return(false)
    expect(helper.not_contact_no_request_partial_path(contact)).to eq(
      'shared/empty_partial'
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:recipient_is_contact?).and_return(false)
    helper.stub(:unaccepted_contact_exists).and_return(true)
    expect(helper.not_contact_no_request_partial_path(contact)).to eq(
      'shared/empty_partial'
    )
  end
end

context 'private scope' do
  context '#request_sent_by_user' do
    it 'returns true' do
      contact = create(:contact, user_id: current_user.id)
      helper.stub(:current_user).and_return(current_user)
      expect(helper.instance_eval { request_sent_by_user(contact) }).to eq true
    end

    it 'returns false' do
      contact = create(:contact, user_id: recipient.id)
      helper.stub(:current_user).and_return(current_user)
      expect(helper.instance_eval { request_sent_by_user(contact) }).to eq false
    end
  end
end
```

Create the `request_status` directory and then create `_send_request.html.erb`, `_sent_by_current_user.html.erb` and `_sent_by_recipient.html.erb` partial files

```html
<div class="contact-request-status">
  <div class="add-user-to-contacts-message">
    <div>
      <%= @recipient.name %> is not in your contacts
    </div>
    <div>
      <%= link_to "Add to contacts", 
                  contacts_path(contact_id: @recipient), 
                  remote: true, 
                  method: :post, 
                  class: 'add-user-to-contacts-notif' %>
    </div>
  </div>   
</div>
```

```html
<div class="contact-request-status">
  <div class="pending-request">
    Contact request is pending
  </div>
</div>
```

```html
<div class="contact-request-status" 
     data-user-name="<%= @recipient.name %>">
  <div class="contact-name">
    <%= @recipient.name %> sent you a contact request
  </div>
  <div class="request-response">
    <span class="accept-request">
      <%= link_to "Accept",  
          contact_path(id: @recipient.id), 
          remote: true, 
          method: "put" %>
    </span>  
    <span class="decline-request">
      <%= link_to "Decline", 
                  contact_path(id: @recipient.id), 
                  remote: true, 
                  method: :delete %>
    </span>              
  </div>
</div>
```

Commit the changes

```bash
git add -A
git commit -m "Add a button on private conversation's window
to add a recipient to contacts"
```

Implement design changes and take care of styling issues which appear  due to extra elements on the conversation window. Add CSS to the `conversation_window.scss` file

```scss
.add-user-to-contacts {
  display: none;
  i {
    opacity: 0.8;
    &:hover {
      opacity: 1;
    }
  }
  &:hover {
    color: white;
  }
}

.add-user-to-contacts-message {
  text-align: center;
  padding: 10px 0;
}

.add-people-to-chat, .contact-request-sent {
  display: none;
  margin: 0;
  padding: 0;
  div {
    width: 40px;
    height: 40px;
    display: table;
    i {
      display: table-cell;
      text-align: center;
      vertical-align: middle;
    }
  }
}

.add-people-to-chat {
  i {
    opacity: 0.8;
    transition: opacity 0.15s;
  }
  &:hover i {
    opacity: 1;
  }
}

.contact-request-status {
  position: relative;
  left: 0;
  top: 0;
  width: 400px;
  text-align: center;
  background-color: white;
  z-index: 2;
  .pending-request {
    padding: 10px 0;
  }
  .request-response {
    padding: 10px 0;
  }
  .accept-request, .decline-request {
    a {
      padding: 10px 0;
    }
  }
  .contact-name {
    padding: 10px 0 0 0;
  }
  .accept-request {
    margin-right: 10px;
    a {
      color: green;
    }
  }
  .decline-request {
    a {
      font-weight: bold;
      color: red;
    }
  }
}
```

Commit the changes

```bash
git add -A
git commit -m "Add CSS to conversation_window.scss to style option buttons"
```

When a conversation window is collapsed, it would be better to not see  any options. It’s a more convenient design to see options only when a  conversation window is expanded. To achieve it, inside the `toggle_window.js` file’s toggle function, just below the `messages_visible` variable, add

```js
// if window is collapsed, hide conversation menu options
if ( panel_body.css('display') == 'none' ) {
    panel.find('.add-people-to-chat,\
                .add-user-to-contacts,\
                .contact-request-sent').hide();
    conversation_heading = panel.find('.conversation-heading');
    conversation_heading.css('width', '360px');

} else { // show conversation menu options
    conversation_heading = panel.find('.conversation-heading');
    conversation_heading.css('width', '320px');
    panel.find('.add-people-to-chat,\
                .add-user-to-contacts,\
                .contact-request-sent').show();
    // focus textarea
    $('form textarea', this).focus();
}
```

Now the collapsed window looks like this, it has no visible options

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-106.png)



The expanded window has an option to add a user to contacts. Also there’s a message which suggests to do that

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-107.png)

Actually, you can send and accept a contact request right now by clicking an icon on the conversation’s header or clicking the `Add to contacts` link. For now, there isn’t any response after you click on those links  and buttons. We’ll add some feedback and real time notification system a  little bit later. But technically, you can add users to your contacts,  it is just not highly user friendly yet.

After you send a contact request, the opposite user’s side looks like this

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-108.png)

Commit the changes

```bash
git add -A
git commit -m "Add JS inside the toggle_window.js to show and hide additional options"
```

#### Currently  users are able to talk privately, have one on one conversations. Since  the app is about collaboration, it would be logical to have group  conversations too.

Start by generating a new model

```
rails g model group/conversation
```

Multiple users will be able to participate in one conversation. Define associations and the database table

```rb
class Group::Conversation < ApplicationRecord
  self.table_name = 'group_conversations'
  
  has_and_belongs_to_many :users
  has_many :messages, 
           class_name: "Group::Message",
           foreign_key: 'conversation_id', 
           dependent: :destroy
end
```

```rb
has_many :group_messages, class_name: 'Group::Message'
has_and_belongs_to_many :group_conversations, class_name: 'Group::Conversation'
```

A [join table](http://guides.rubyonrails.org/active_record_migrations.html#creating-a-join-table) is going to be used to track who belongs to which group conversation

Then generate a model for messages

```bash
rails g model group/message
```

```rb
class Group::Message < ApplicationRecord
  serialize :seen_by, Array
  serialize :added_new_users, Array
  self.table_name = "group_messages"

  belongs_to  :conversation,
              class_name: 'Group::Conversation',
              foreign_key: 'conversation_id'
  belongs_to :user

  validates :content, presence: true
  validates :user_id, presence: true
  validates :conversation_id, presence: true

  default_scope { includes(:user) }

  # get a previous message of a conversation
  def previous_message
    previous_message_index = self.conversation.messages.index(self) - 1
    self.conversation.messages[previous_message_index]
  end
end
```

We’ll store users’ ids who have seen a message into an array. To create and manage objects, such as array, inside a database column, a serialize method is used. A default scope, to minimize the amount of queries, and some validations are added.

The way we’re building group conversations is pretty similar to private conversations. In fact, styling and some parts are going to be in common between both types of conversations.

Write specs for the models. Also a factory for group messages is going to be needed

```rb
FactoryGirl.define do 
  factory :group_message, class: 'Group::Message' do
    content 'a' * 20
    association :conversation, factory: :group_conversation
    user
  end
end
```

```rb
it 'has_many group_messages' do 
  association = described_class.reflect_on_association(:group_messages)
  expect(association.macro).to eq :has_many
  expect(association.options[:class_name]).to eq 'Group::Message'
end

it 'has_and_belongs_to_many group_conversations' do
  association = described_class.reflect_on_association(:group_conversations)
  expect(association.macro).to eq :has_and_belongs_to_many
  expect(association.options[:class_name]).to eq 'Group::Conversation'
end
```

```rb
require 'rails_helper'

RSpec.describe Group::Conversation, type: :model do

  let(:conversation) { build(:group_conversation) }

  context 'Associations' do
    it 'has_and_belongs_to_many users' do
      association = described_class.reflect_on_association(:users)
      expect(association.macro).to eq :has_and_belongs_to_many
    end

    it 'has_many messages' do
      association = described_class.reflect_on_association(:messages)
      expect(association.macro).to eq :has_many
      expect(association.options[:class_name]).to eq 'Group::Message'
      expect(association.options[:foreign_key]).to eq 'conversation_id'
      expect(association.options[:dependent]).to eq :destroy
    end
  end

end
```

```rb
require 'rails_helper'

RSpec.describe Group::Message, type: :model do

  let(:message) { build(:group_message) }

  context 'Associations' do
    it 'belongs_to group_conversation' do
      association = described_class.reflect_on_association(:conversation)
      expect(association.macro).to eq :belongs_to
      expect(association.options[:class_name]).to eq 'Group::Conversation'
      expect(association.options[:foreign_key]).to eq 'conversation_id'
    end
  end

  context 'Validations' do
    it "is not valid without a content" do 
      message.content = nil
      expect(message).not_to be_valid 
    end

    it "is not valid without a conversation_id" do 
      message.conversation_id = nil
      expect(message).not_to be_valid 
    end

    it "is not valid without a user_id" do 
      message.user_id = nil
      expect(message).not_to be_valid 
    end
  end

  context 'Methods' do
    it 'gets a previous message of a conversation' do
      conversation = create(:group_conversation)
      message1 = create(:group_message, conversation_id: conversation.id)
      message2 = create(:group_message, conversation_id: conversation.id)
      expect(message2.previous_message).to eq message1
    end
  end
 
end
```

Define the migration files

```rb
class CreateGroupConversations < ActiveRecord::Migration[5.1]
  def change
    create_table :group_conversations do |t|
      t.string :name
      t.timestamps
    end
  end
end
```

```rb
class CreateGroupConversationsUsersJoinTable < ActiveRecord::Migration[5.1]
  def change
    create_table :group_conversations_users, id: false do |t|
      t.integer :conversation_id
      t.integer :user_id
    end
    add_index :group_conversations_users, :conversation_id
    add_index :group_conversations_users, :user_id
  end
end
```

```rb
class CreateGroupMessages < ActiveRecord::Migration[5.1]
  def change
    create_table :group_messages do |t|
      t.string :content
      t.string :added_new_users
      t.string :seen_by
      t.belongs_to :user, index: true
      t.belongs_to :conversation, index: true
      t.timestamps
    end
  end
end
```

The fundamentals of the group conversation are set.

Commit the changes

```bash
git add -A
git commit -m "Create Group::Conversation and Group::Message models
- Define associations
- Write specs"
```

**Create a group conversation**

As  mentioned before, the process of creating the group conversation  feature is going to be similar to what we did with the private  conversation. Start by creating a controller and a basic user interface.

Generate a namespaced controller

```bash
rails g controller group/conversations
```

Inside the controller define a `create` action and `add_to_conversations`, `already_added?` and `create_group_conversation` methods within a private scope

```rb
class Group::ConversationsController < ApplicationController

  def create
    @conversation = create_group_conversation
    add_to_conversations unless already_added?

    respond_to do |format|
      format.js
    end
  end
  
  private

  def add_to_conversations
    session[:group_conversations] ||= []
    session[:group_conversations] << @conversation.id
  end
 
  def already_added?
    session[:group_conversations].include?(@conversation.id)
  end

  def create_group_conversation
    Group::NewConversationService.new({
      creator_id: params[:creator_id],
      private_conversation_id: params[:private_conversation_id],
      new_user_id: params[:group_conversation][:id]
    }).call
  end
  
end
```

There is some complexity involved in creating a new group conversation, so we’ll extract it into a service object. Then we have `add_to_conversations` and `already_added?` private methods. If you recall, we have them in the `Private::ConversationsController` too, but this time it stores group conversations’ ids into the session.

Now define the `Group::NewConversationService` inside a new `group` directory

```rb
class Group::NewConversationService

  def initialize(params)
    @creator_id = params[:creator_id]
    @private_conversation_id = params[:private_conversation_id]
    @new_user_id = params[:new_user_id]
  end

  def call
    creator = User.find(@creator_id)
    pchat_opposed_user = Private::Conversation.find(@private_conversation_id)
                           .opposed_user(creator)
    new_user_to_chat = User.find(@new_user_id)
    new_group_conversation = Group::Conversation.new
    new_group_conversation.name = '' + creator.name + ', ' + 
                                  pchat_opposed_user.name + ', ' + 
                                  new_user_to_chat.name 
    if new_group_conversation.save
      arr_of_users_ids = [creator.id, pchat_opposed_user.id, new_user_to_chat.id]
      # add users to the conversation
      creator.group_conversations << new_group_conversation
      pchat_opposed_user.group_conversations << new_group_conversation
      new_user_to_chat.group_conversations << new_group_conversation
      # create an initial message with an information about the conversation
      create_initial_message(creator, arr_of_users_ids, new_group_conversation)
      # return the conversation
      new_group_conversation
    end
  end

  private

  def create_initial_message(creator, arr_of_users_ids, new_group_conversation)
    message = Group::Message.create(
      user_id: creator.id, 
      content: 'Conversation created by ' + creator.name, 
      added_new_users: arr_of_users_ids , 
      conversation_id: new_group_conversation.id
    )
  end
end
```

The way a new group conversation is going to be created, is actually  through a private conversation. We’ll create this interface as an option  on the private conversation’s window soon. Before doing that, make sure  that the service object functions properly by covering it with specs.  Inside the `services`, create a new directory `group` with a `new_conversation_service_spec.rb` file inside

```rb
require 'rails_helper'
require './app/services/group/new_conversation_service.rb'

describe Group::NewConversationService do
  let(:user1) { create(:user) }
  let(:user2) { create(:user) }
  let(:new_user) { create(:user) }
  let(:private_conversation) { create(:private_conversation,
                                       sender_id: user1.id,
                                       recipient_id: user2.id) }
  context '#call' do
    it 'returns a new created group conversation' do
      new_conversation = Group::NewConversationService.new({
                           creator_id: user1.id,
                           private_conversation_id: private_conversation.id,
                           new_user_id: new_user.id
                         }).call
      last_conversation = Group::Conversation.last
      expect(new_conversation).to eq last_conversation
      expect(last_conversation.messages.count).to eq 1
    end
  end
end
```

Commit the changes

```bash
git add -A
git commit -m "Create back-end for creating a new group conversation
- Create a Group::ConversationsController
  Define a create action and add_to_conversations, 
  create_group_conversation and already_added? private methods inside
- Create a  Group::NewConversationService and write specs for it"
```

Define routes for the group conversation and its messages

```rb
namespace :group do 
  resources :conversations do
    member do
      post :close
      post :open
    end
  end
  resources :messages, only: [:index, :create]
end
```

Commit the changes

```bash
git add -A
git commit -m "Define specs for Group::Conversations and Messages"
```

Currently we only take care of private conversations inside the `ApplicationController`.  Only private conversations are being ordered and only their ids, after a  user opens them, are available across the app. Inside the `ApplicationController`, update the `opened_conversations_windows` method

```rb
def opened_conversations_windows
  if user_signed_in?
    # opened conversations
    session[:private_conversations] ||= []
    session[:group_conversations] ||= []
    @private_conversations_windows = Private::Conversation.includes(:recipient, :messages)
                                         .find(session[:private_conversations])
    @group_conversations_windows = Group::Conversation.find(session[:group_conversations])
  else
    @private_conversations_windows = []
    @group_conversations_windows = []
  end
end
```

Because conversations’ ordering happens with a help of the `OrderConversationsService`, we’ve to update this service

```rb
# get and order conversations by last messages' dates in descending order
def call
  all_private_conversations = Private::Conversation.all_by_user(@user.id)
                                                   .includes(:messages)
  all_group_conversations = @user.group_conversations.includes(:messages)
  all_conversations = all_private_conversations + all_group_conversations

  return all_conversations = all_conversations.sort{ |a, b| 
    b.messages.last.created_at <=> a.messages.last.created_at
  }
end
```

Previously we only had the private conversations array and we sorted it by the latest messages’ creation dates. Now we have private and group conversations arrays, then we join them together into one array and sort it the same way, as we did before.

Also update the specs

```rb
describe OrderConversationsService do
  context '#call' do
    it 'returns ordered conversations in descending order' do
      user = create(:user)
      conversation1 = create(:private_conversation,
                              sender_id: user.id,
                              messages: [create(:private_message)])
      conversation2 = create(:group_conversation,
                              users: [user],
                              messages: [create(:group_message)])
      conversation3 = create(:private_conversation,
                              sender_id: user.id,
                              messages: [create(:private_message)])
      conversations = [conversation3, conversation2, conversation1]
      expect(OrderConversationsService.new({user: user}).call).to eq conversations
    end
  end
end
```

Commit the changes

```bash
git add -A
git commit -m "Get data for group conversations in ApplicationController
- Update the opened_conversations_windows method
- Update the OrderConversationsService"
```

In just a moment we’ll need to pass some data from a controller to JavaScript. Luckily, we have already installed the `gon` gem, which allows us to do that easily. Inside the `ApplicationController`, within a `private` scope, add

```rb
def set_user_data
  if user_signed_in?
    gon.group_conversations = current_user.group_conversations.ids
    gon.user_id = current_user.id
    cookies[:user_id] = current_user.id if current_user.present?
    cookies[:group_conversations] = current_user.group_conversations.ids
  else
    gon.group_conversations = []
  end
end
```

Use the `before_action` filter to call this method

```
before_action :set_user_data
```

Commit the changes

```bash
git add -A
git commit -m "Define a set_user_data private method in ApplicationController"
```

Technically we can create a new group conversation now, but users have no interface to do that. As mentioned, they will do it through a private conversation. Let’s create this option on the private conversation’s window.

Inside the

```bash
views/private/conversations/conversation/heading
```

directory create a new file

```html
<!-- Add more contacts to chat button -->
<div class="add-people-to-chat" title="Create a group chat">
  <div>
    <i class="fa fa-plus" aria-hidden="true" data-toggle="dropdown"></i>
  </div>
</div>
<!-- select users to add to conversation -->
<div class="select-users-to-chat">
  <%= form_for(Group::Conversation.new, remote: true, class: 'form-group') do |f| %>
    <%= hidden_field_tag :creator_id, current_user.id %>
    <%= hidden_field_tag :private_conversation_id, conversation.id %>
    <%= f.collection_select(:id, 
                            contacts_except_recipient(@recipient), 
                            :id, 
                            :name, 
                            {}, 
                            {:class=>'form-control select-users-dropdown'}) %>
    <%= f.submit 'Start a conversation', class: 'form-control select-users-button' %>
  <% end %>
</div>
```

A `[collection_select](https://apidock.com/rails/ActionView/Helpers/FormOptionsHelper/collection_select)` method is used to display a list of users. Only users who are in contacts are going to be included in the list. Define the `contacts_except_recipient` helper method

```rb
def contacts_except_recipient(recipient)
  contacts = current_user.all_active_contacts
  # return all contacts, except the opposite user of the chat
  contacts.delete_if {|contact| contact.id == recipient.id }
end
```

Write specs for the method

```rb
context '#contacts_except_recipient' do
  it 'return all contacts, except the opposite user of the chat' do
    contacts = create_list(:contact, 
                            5, 
                            user_id: current_user.id, 
                            accepted: true)

    contacts << create(:contact, 
                        user_id: current_user.id, 
                        contact_id: recipient.id,
                        accepted: true)
    helper.stub(:current_user).and_return(current_user)
    expect(helper.contacts_except_recipient(recipient)).not_to include recipient
  end
end
```

Render the partial at the bottom of the `_heading.html.erb`

```html
<%= render create_group_conv_partial_path, conversation: conversation %>
```

Define the helper method

```rb
def create_group_conv_partial_path(contact)
  if recipient_is_contact?
    'private/conversations/conversation/heading/create_group_conversation'
  else
    'shared/empty_partial'
  end
end
```

Wrap it with specs

```rb
context '#create_group_conv_partial_path' do
  let(:contact) { create(:contact) }

  it "returns a create_group_conversation partial's path" do 
    helper.stub(:recipient_is_contact?).and_return(true)
    expect(helper.create_group_conv_partial_path(contact)).to(
      eq 'private/conversations/conversation/heading/create_group_conversation'
    )
  end

  it "returns an empty partial's path" do 
    helper.stub(:recipient_is_contact?).and_return(false)
    expect(helper.create_group_conv_partial_path(contact)).to(
      eq 'shared/empty_partial'
    )
  end
end
```

Commit the changes.

```bash
git add -A
git commit -m "Add a UI on private conversation to create a group conversations"
```

Add CSS to style the component which allows to create a new group conversation

```scss
.select-users-to-chat {
  padding: 5px 0 5px 5px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  position: absolute;
  top: 40px;
  background-color: white;
  display: none;
  height: 45px;
  width: 100%;
  z-index: 2;
}

.select-users-dropdown, .select-users-button {
  border: none;
  display: inline-block;
  margin: 0;
  height: 35px;
}

.select-users-dropdown {
  width: 55%;
  border: 1px solid rgba(0, 0, 0, 0.2);
}

.select-users-button {
  width: 40%;
  background-color: $navbarColor;
  color: white;
  border: 1px solid $navbarColor;
}
```

A selection of contacts is hidden by default. To open the selection, a  user has to click on the button. The button isn’t interactive yet.  Create an `options.js` file with JavaScript inside to make the selection list toggleable.

```js
$(document).on('turbolinks:load', function() { 

  //  when add more contacts to a conversation button is clicked
  //  toggle contacts selection
  $('body').on('click', '.add-people-to-chat', function(e) {
      $(this).next().toggle(100, 'swing');
  });

});
```

Now a conversation window with a recipient who is a contact looks like this

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-109.png)

There is a button which opens a list of contacts, you can create a group conversation with, when you click on it

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-110.png)

Commit the changes.

```bash
git add -A
git commit -m "
- Describe style for the create a group conversation option
- Make the option toggleable"
```

We have a list of ordered conversations, including group conversations now, which will be rendered on the navigation bar’s drop down menu. If you recall, we specified different partials for different types of conversations. When the app tries to render a link, to open a group conversation, it will look for a different file than for a private conversation. The file isn’t created yet.

Create a `_group.html.erb` file

```html
<% seen_status = group_conv_seen_status(conversation, current_user) %>
<li id="menu-gc<%= conversation.id %>" class="<%= seen_status %>">
  <%= link_to truncate(conversation.name, :length => 40), 
              open_group_conversation_path(id: conversation.id), 
              remote: true, 
              method: :post, 
              class: 'bigger-screen-link' %>
</li>
```

Define the `group_conv_seen_status` helper method inside the `Shared::ConversationsHelper`

```rb
def group_conv_seen_status(conversation, current_user)
  # if the current_user is nil, it means that the helper is called from the service
  # return an empty string
  if current_user == nil
    ''
  else
    # if the last message of the conversation is not created by this user
    # and is unseen, return an unseen-conv value
    not_created_by_user = conversation.messages.last.user_id != current_user.id
    seen_by_user = conversation.messages.last.seen_by.include? current_user.id
    not_created_by_user && seen_by_user == false ? 'unseen-conv' : ''
  end
end
```

Write specs for the method

```rb
context '#group_conv_seen_status' do
  it 'returns unseen-conv status' do
    conversation = create(:group_conversation)
    create(:group_message, conversation_id: conversation.id)
    current_user = create(:user)
    view.stub(:current_user).and_return(current_user)
    expect(helper.group_conv_seen_status(conversation)).to eq(
      'unseen-conv'
    )
  end

  it 'returns an empty string' do
    user = create(:user)
    conversation = create(:group_conversation)
    create(:group_message, conversation_id: conversation.id, user_id: user.id)
    view.stub(:current_user).and_return(user)
    expect(helper.group_conv_seen_status(conversation)).to eq ''
  end

  it 'returns an empty string' do
    user = create(:user)
    conversation = create(:group_conversation)
    message = build(:group_message, conversation_id: conversation.id)
    message.seen_by << user.id
    message.save
    view.stub(:current_user).and_return(user)
    expect(helper.group_conv_seen_status(conversation)).to eq ''
  end
end
```

Commit the changes.

```bash
git add -A
git commit -m "Create a link on the navigation bar to open a group conversation"
```

Render group conversations’ windows on the app, the same way as we rendered the private conversations. Inside the `application.html.erb`, just below the rendered private conversations, add:

```hrml
<%= render 'layouts/application/group_conversations_windows' %>
```

Create the partial file to render group conversations’ windows one by one:

```hrml
<% @group_conversations_windows.each do |conversation| %>
  <%= render partial: "group/conversations/conversation",
            locals: { conversation: conversation, 
                      user: current_user } %>
<% end %>
```

Commit the change.

```bash 
git add -A
git commit -m "Render group conversations' windows inside the
application.html.erb"
```

We have a mechanism how group conversations are created and rendered on the app. Now let’s build a conversation window itself.

Inside the `group/conversations` directory, create a `_conversation.html.erb`file.

```html
<% add_people_to_conv_list = add_people_to_group_conv_list(conversation) %>
<% @is_messenger = false %>
<li class="conversation-window" id="gc<%= conversation.id %>" data-turbolinks-permanent>
  <div class="panel panel-default" data-gconversation-id="<%= conversation.id %>">
    <%= render  'group/conversations/conversation/heading',
                conversation: conversation %> 
    <%= render  'group/conversations/conversation/select_users',
                conversation: conversation,
                add_people_to_conv_list: add_people_to_conv_list %>
    <div class="panel-body">
      <%= render  'group/conversations/conversation/messages_list',
                  conversation: conversation %>
      <%= render  'group/conversations/conversation/new_message_form',
                  conversation: conversation,
                  user: user %> 
    </div><!-- panel-body -->
  </div><!-- panel -->
</li>
```

Define the `add_people_to_group_conv_list` helper method:

```rb
module Group::ConversationsHelper
  def add_people_to_group_conv_list(conversation)
    contacts = current_user.all_active_contacts
    users_in_conv = conversation.users
    add_people_to_conv_list = []
    contacts.each do |contact|
      # if the contact is already in the conversation, remove it from the list
      if !users_in_conv.include?(contact)
        add_people_to_conv_list << contact
      end
    end
    add_people_to_conv_list
  end
end
```

Write specs for the helper:

```rb
context '#add_people_to_group_conv_list' do
  let(:conversation) { create(:group_conversation) }
  let(:current_user) { create(:user) }
  let(:user) { create(:user) }
  before(:each) do
    create(:contact, 
            user_id: current_user.id, 
            contact_id: user.id,
            accepted: true)
  end

  it 'a user is not included in a list' do
    conversation.users << current_user
    conversation.users << user
    helper.stub(:current_user).and_return(current_user)
    expect(helper.add_people_to_group_conv_list(conversation)).not_to include user
  end

  it 'a user is included in a list' do
    conversation.users << current_user
    helper.stub(:current_user).and_return(current_user)
    expect(helper.add_people_to_group_conv_list(conversation)).to include user
  end
end
```

Just like with private conversations, group conversations are going to  be accessible across the whole app, so obviously, we need access to the `Group::ConversationsHelper` methods everywhere too. Add this module inside the `ApplicationHelper`

```
include Group::ConversationsHelper
```

Commit the changes.

```bash
git add -A
git commit -m "
- Create a _conversation.html.erb inside the group/conversations
- Define a add_people_to_group_conv_list and write specs for it"
```

Create a new `conversation` directory with a `_heading.html.erb` file inside:

```html
<div class="panel-heading conversation-heading">
  <%= truncate(conversation.name, :length => 40) %>
</div>

<!-- Close the conversation button -->
<%= link_to "X", 
            close_group_conversation_path(conversation), 
            class: 'close-conversation', 
            title: 'Close', 
            remote: true, 
            method: :post %>

<!-- Add more contacts to the conversation button -->
<div class="add-people-to-chat" title="Add people to chat">
  <div>
    <i class="fa fa-plus" aria-hidden="true" data-toggle="dropdown"></i>
  </div>
</div>
```

Commit the change.

```bash
git add -A
git commit -m "Create a _heading.html.erb inside the
group/conversations/conversation"
```

Next we have `_select_user.html.erb` and `_messages_list.html.erb` partial files. Create them:

```html
<div class="select-users-to-chat">
  <%= form_tag  group_conversation_path(conversation), 
                method: 'put', 
                class: 'form-group' do %>
    <%= hidden_field_tag :added_by, current_user.id %>
    <%= collection_select(:user, 
                          :id, 
                          add_people_to_conv_list, 
                          :id, 
                          :name, 
                          {}, 
                          {:class=>'form-control select-users-dropdown'}) %>
    <%= submit_tag 'Add the user', class: 'form-control select-users-button' %>
  <% end %>
</div>
```

```html
<div class="messages-list">
  <%= render partial: load_group_messages_partial_path(conversation),
             locals: { conversation: conversation, messenger_boolean: false } %>
  <div class="loading-more-messages">
    <i class="fa fa-spinner" aria-hidden="true"></i>
  </div>
  <!-- messages -->
  <ul>
  </ul>
</div>
```

Define the `load_group_messages_partial_path` helper method:

```rb
def load_group_messages_partial_path(conversation)
  if conversation.messages.count > 0
    'group/conversations/conversation/messages_list/load_messages'
  else
    'shared/empty_partial'
  end
end
```

Wrap it with specs:

```rb
context '#load_group_messages_partial_path' do
  let(:conversation) { create(:group_conversation) }
  it "returns load_messages partial's path" do
    create_list(:group_message, 2, conversation_id: conversation.id)
    expect(helper.load_group_messages_partial_path(conversation)).to eq(
      'group/conversations/conversation/messages_list/link_to_previous_messages'
    )
  end

  it "returns an empty partial's path" do
    expect(helper.load_group_messages_partial_path(conversation)).to eq(
      'shared/empty_partial'
    )
  end
end
```

Commit the changes.

```bash
git add -A
git commit -m "
- Create _select_user.html.erb and _messages_list.html.erb inside
  group/conversations/conversation
- Define a load_group_messages_partial_path helper method 
  and write specs for it"
```

Create a `_link_to_previous_messages.html.erb` file, to have a link which loads previous messages:

```html
<%= link_to "Load messages", 
            group_messages_path(:conversation_id => conversation.id, 
                                :messages_to_display_offset => @messages_to_display_offset,
                                :is_messenger => @is_messenger), 
            class: 'load-more-messages', 
            remote: true %>
```

Commit the change.

```bash
git add -A
git commit -m "Create a _load_messages.html.erb inside the
group/conversations/conversation/messages_list"
```

Create a new message form

```html
<form class="send-group-message">
  <input  name="conversation_id" 
          type="hidden" 
          value="<%= conversation.id %>">
  <input  name="user_id" 
          type="hidden" 
          value="<%= user.id %>">
  <textarea name="content" 
            rows="3" 
            class="form-control" 
            placeholder="Type a message..."></textarea>
  <input type="submit" class="btn btn-success send-message">
</form>
```

Commit the change.

```bash
git add -A
git commit -m "Create a _new_message_form.html.erb inside the 
group/conversations/conversation/"
```

The application is now able to render group conversations’ windows too.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-111.png)

But, they aren’t functional yet. First, we need to load messages. We need a controller for messages and views. Generate a `Messages` controller:

```
rails g controller group/messages
```

Include the `Messages` module from `concerns` and define an `index` action:

```rb
class Group::MessagesController < ApplicationController
  include Messages
  
  def index
    get_messages('group', 15)
    @user = current_user
    @is_messenger = params[:is_messenger]
    respond_to do |format|
      format.js { render partial: 'group/messages/load_more_messages' }
    end
  end
end
```

Commit the changes.

```bash
git add -A
git commit -m "Create a Group::MessagesController and define an index action"
```

Create a `_load_more_messages.js.erb`

```js
<% @id_type = 'gc' %>
<%= render append_previous_messages_partial_path %>
<%= render replace_link_to_group_messages_partial_path %>
<%= render remove_link_to_messages %>
```

We’ve already defined the `append_previous_messages_partial_path` and `remove_link_to_messages` helper methods earlier on. We only have to define the `replace_link_to_group_messages_partial_path` helper method

```rb
def replace_link_to_group_messages_partial_path
  'group/messages/load_more_messages/window/replace_link_to_messages'   
end 
```

Again, this method, just like on the private side, is going to become more “intelligent”, once we develop the messenger.

Create the `_replace_link_to_messages.js.erb`

```js
$('#<%= @id_type %><%= @conversation.id %> .load-more-messages')
    .replaceWith('\
        <%= j render partial: "group/conversations/conversation/messages_list/link_to_previous_messages",\
                     locals: { conversation: @conversation } %>\
        ');
```

Also add the `Group::MessagesHelper` to the `ApplicationHelper`

```
include Group::MessagesHelper
```

Commit the changes.

```bash
git add -A
git commit -m "Create a _load_more_messages.js.erb inside the group/messages"
```

The only way group conversations can be opened right now is after their initialization. Obviously, this is not a thrilling thing, because once you destroy the session, there is no way to open the same conversation again. Create an `open` action inside the controller.

```rb
def open
  @conversation = Group::Conversation.find(params[:id])
  add_to_conversations unless already_added?
  respond_to do |format|
    format.js { render partial: 'group/conversations/open' }
  end
end
```

Create the `_open.js.erb` partial file:

```js
var conversation = $('body').find("[data-gconversation-id='" + 
                                "<%= @conversation.id %>" + 
                                "']");
var chat_windows_count = $('.conversation-window').length + 1;


if (conversation.length !== 1) {
  $('body').append("<%= j(render 'group/conversations/conversation',\
                                  conversation: @conversation,\
                                  user: current_user) %>");
  conversation = $('body').find("[data-gconversation-id='" + 
                                "<%= @conversation.id %>" + 
                                "']");
}

// Toggle conversation window after its creation
$('.conversation-window:nth-of-type(' + chat_windows_count + ')\
   .conversation-heading').click();
// mark as seen by clicking it
setTimeout(function(){ 
  $('.conversation-window:nth-of-type(' + chat_windows_count + ')').click();
 }, 1000);
// focus textarea
$('.conversation-window:nth-of-type(' + chat_windows_count + ')\
   form\
   textarea').focus();

var messages_list = conversation.find('.messages-list');
var height = messages_list[0].scrollHeight;
messages_list.scrollTop(height);

// repositions all conversation windows
positionChatWindows();
```

Now we’re able to open conversations by clicking on navigation bar’s drop down menu links. Try to test it with feature specs on your own.

Commit the changes.

```bash
git add -A
git commit -m "Add ability to open group conversations
- Create an open action in the Group::ConversationsController
- Create an _open.js.erb inside the group/conversations"
```

The app will try to render messages, but we haven’t created any templates for them. Create a `_message.html.erb`

```html
<%= render partial: group_message_date_check_partial_path(message, 
                                                          previous_message),
           locals: { message: message } %>
<li class="group-message">
  <div class="row <%= seen_by_user? %>" data-seen-by="<%= group_message_seen_by(message) %>">
    <%= render partial: message_content_partial_path(user, message, previous_message),
               locals: { user: user, message: message } %>
  </div>
</li>
```

Define `group_message_date_check_partial_path`, `group_message_seen_by` and `message_content_partial_path` helper methods.

```rb
def group_message_date_check_partial_path(new_message, previous_message)
  # if a previous message exists
  if defined?(previous_message) && previous_message.present?
    # if the date is different between the previous and new messages
    if previous_message.created_at.to_date != new_message.created_at.to_date
      'group/messages/message/new_date'
    else
      'shared/empty_partial'
    end
  else
    'shared/empty_partial'
  end
end

def group_message_seen_by(message)
  seen_by_names = []
  # If anyone has seen the message
  if message.seen_by.present?
    message.seen_by.each do |user_id|
      seen_by_names << User.find(user_id).name
    end
  end
  seen_by_names
end

def message_content_partial_path(user, message, previous_message)
  # if previous message exists
  if defined?(previous_message) && previous_message.present?
    # if new message is created by the same user as previous'
    if previous_message.user_id == user.id
      'group/messages/message/same_user_content'
    else
      'group/messages/message/different_user_content'
    end
  else
    'group/messages/message/different_user_content'
  end
end

def seen_by_user?
  @seen_by_user ? '' : 'unseen'
end
```

The `group_message_seen_by` method will return a list of users who have seen a message. This little  information allows us to create extra features, like show to  conversation participants who have seen messages, etc. But in our case,  we’ll use this information to determine if a current user has seen a  message, or not. If not, then after the user sees it, the message is  going to be marked as seen.

Also we’ll need helper methods from the `Shared` module. Inside the `Group::MessagesHelper`, add the module.

```
require 'shared/messages_helper'
include Shared::MessagesHelper
```

Wrap helper methods with specs:

```rb
context '#group_message_seen_by' do
  let(:message) { create(:group_message) }
  it 'returns an array with users' do
    users = create_list(:user, 2)
    users.each do |user|
      message.seen_by << user.id
    end
    message.save
    users.map! { |user| user.name }
    expect(helper.group_message_seen_by(message)).to eq users
  end

  it 'returns an empty array' do
    users = []
    expect(helper.group_message_seen_by(message)).to eq users
  end
end

context '#message_content_partial_path' do
  let(:user) { create(:user) }
  let(:message) { create(:group_message) }
  let(:previous_message) { create(:group_message) }

  it "returns same_user_content partial's path" do
    previous_message.update(user_id: user.id)
    expect(helper.message_content_partial_path(user, 
                                               message, 
                                               previous_message)).to eq(
      'group/messages/message/same_user_content'
    )
  end

  it "returns different_user_content partial's path" do
    expect(helper.message_content_partial_path(user, 
                                               message, 
                                               previous_message)).to eq(
      'group/messages/message/different_user_content'
    )
  end

  it "returns different_user_content partial's path" do
    previous_message = nil
    expect(helper.message_content_partial_path(user, 
                                               message, 
                                               previous_message)).to eq(
      'group/messages/message/different_user_content'
    )
  end
end

context '#group_message_date_check_partial_path' do
  let(:new_message) { create(:group_message) }
  let(:previous_message) { create(:group_message) }

  it "returns a new_date partial's path" do
    new_message.update(created_at: 2.days.ago)
    expect(helper.group_message_date_check_partial_path(new_message, 
                                                        previous_message)).to eq(
      'group/messages/message/new_date'
    )
  end

  it "returns an empty partial's path" do
    expect(helper.group_message_date_check_partial_path(new_message, 
                                                        previous_message)).to eq(
      'shared/empty_partial'
    )
  end

  it "returns an empty partial's path" do
    previous_message = nil
    expect(helper.group_message_date_check_partial_path(new_message, 
                                                        previous_message)).to eq(
      'shared/empty_partial'
    )
  end
end
```

Commit the changes.

```bash
git add -A
git commit -m "Create a _message.html.erb inside group/messages
- Define group_message_date_check_partial_path,
  group_message_seen_by and message_content_partial_path helper
  methods and write specs for them"
```

Create partial files for the message:

```html
<div class="messages-date">
  <span><%= message.created_at.to_date %></span>
</div>
```

```html
<span class="message-author"><%= user.name %></span>
<span class="message-time"><%= message.created_at.to_s(:time) %></span>
<p class="message-content">
  <%= message.content %>
</p>
```

```html
<div class="message-time hidden-item"><%= message.created_at.to_s(:time) %></div> 
<p class="message-content">
  <%= message.content %>
</p>
```

Commit the changes.

```bash
git add -A
git commit -m "Create _new_date.html.erb,
_different_user_content.html.erb and _same_user_content.html.erb
inside the group/messages/message/"
```

Now we need a mechanism which will render messages one by one. Create a `_messages.html.erb` partial file:

```html
<% previous_message = nil %>
<% @messages.reverse.each do |message| %>
  <%= render  partial: 'group/messages/message', 
              locals: { user: message.user, 
                        conversation_id: @conversation.id,
                        message: message, 
                        previous_message: previous_message } %>
  <% previous_message = message %>
<% end %>
```

Commit the change.

```bash
git add -A
git commit -m "Create _messages.html.erb inside group/conversations"
```

Add styling for group messages:

```scss
.group-message {
  padding: 0 10px;
  word-wrap: break-word;
  z-index: 1;
  .row {
    position: relative;
  }
  .hidden-item {
    position: absolute; 
    left: 0; 
    vertical-align: middle;
    line-height: 20px;
    visibility: hidden;
  }
  .message-content {
    margin-left: 40px;
  }
  &:hover {
    background-color: rgb(250, 250, 250);
  }
  p {
    margin: 0;
  }
  .message-author, .message-time {
    font-size: 12px;
    font-size: 1.2rem;
  }
  .message-author {
    margin-left: 40px;
    font-weight: bold;
  }
  .message-time {
    padding-left: 2px;
    color: rgba(0,0,0,0.5);
  }
  &:hover .message-time {
    visibility: visible;
  }
}
```

Commit the change.

```bash
git add -A
git commit -m "Add CSS for group messages in conversation_window.scss"
```

Make the close button functional by defining a `close` action inside the `Group::ConversationsController`

```rb
def close
  @conversation = Group::Conversation.find(params[:id])

  session[:group_conversations].delete(@conversation.id)

  respond_to do |format|
    format.js
  end
end
```

Create the corresponding template file:

```js
$('body').find("[data-gconversation-id='" + "<%= @conversation.id %>" + "']")
    .parent()
    .remove();
positionChatWindows();
```

Commit the changes.

```bash
git add -A
git commit -m "Add a close group conversation window functionality
- Define a close action inside the Group::ConversationsController
- Create a close.js.erb inside the group/conversations"
```

**Communicating in real time**

Just  like with private conversations, we want to be able to have  conversations in real time with multiple users at the same window. The  process of achieving this feature is going to be pretty similar to what  we did with private conversations.

Generate a new channel for group conversations

```bash
rails g channel group/conversation
```

```rb
class Group::ConversationChannel < ApplicationCable::Channel
  def subscribed
    if belongs_to_conversation(params[:id])
      stream_from "group_conversation_#{params[:id]}"
    end
  end

  def unsubscribed
    stop_all_streams
  end

  def set_as_seen(data)
    # find a conversation and set its last message as seen
    conversation = Group::Conversation.find(data['conv_id'])
    last_message = conversation.messages.last 
    last_message.seen_by << current_user.id
    last_message.save
  end

  def send_message(data)
    message_params = data['message'].each_with_object({}) do |el, hash|
      hash[el['name']] = el['value']
    end
    message = Group::Message.new(message_params)
    if message.save
      previous_message = message.previous_message
      Group::MessageBroadcastJob.perform_later(message, previous_message, current_user)
    end
  end

  private

  # checks if a user belongs to a conversation
  def belongs_to_conversation(id)
    conversations = current_user.group_conversations.ids
    conversations.include?(id)
  end

end
```

This time we check if a user belongs to a conversation, before establishing the connection, with the `belongs_to_conversation` method. In private conversations we streamed from a unique channel, by providing the `current_user`’s id. In a case of group conversations, an id of a conversation is passed from the client side. With the `belongs_to_conversation` method we check if users didn’t do any manipulations and didn’t try to connect to a channel which they don’t belong to.

Commit the change

```bash
git add -A
git commit -m "Create a Group::ConversationChannel"
```

Create the `Group::MessageBroadcastJob`

```
rails g job group/message_broadcast
```

```rb
class Group::MessageBroadcastJob < ApplicationJob
  queue_as :default

  def perform(message, previous_message, current_user)
    # broadcast message to all conversation's participants
    conversation_id = message.conversation_id
    ActionCable.server.broadcast(
      "group_conversation_#{conversation_id}",
      message: render_message(message, previous_message),
      conversation_id: conversation_id,
      user_id: message.user_id
    )
  end

  def render_message(message, previous_message)
    ApplicationController.render(
      partial: 'group/messages/message',
      locals: { message: message, 
                previous_message: previous_message, 
                user: message.user }
    )
  end

end
```

Commit the change.

```bash
git add -A
git commit -m "Create a Group::MessageBrodcastJob"
```

The last missing puzzle piece left — the client side:

```js
for (i = 0; i < gon.group_conversations.length; i++) {
    subToGroupConversationChannel(gon.group_conversations[i]);
}

function subToGroupConversationChannel(id) {
    App['group_conversation_' + id]  = App.cable.subscriptions.create(
        {
            channel: 'Group::ConversationChannel',
            id: id
        },
        {
            connected: function() {},
            disconnected: function() {},
            received: function(data) {
                console.log('sawp');
                // prepend link to the conversation 
                // to the top of conversations menu list
                modifyConversationsMenuList(data['conversation_id']);

                // set variables
                var conversation = findConv(data['conversation_id'], 'g');
                var conversation_rendered = ConvRendered(data['conversation_id'], 'g');
                var messages_visible = ConvMessagesVisiblity(conversation);

                // if the message is not sent by the user, 
                // mark the conversation as unseen
                MarkGroupConvAsUnseen(data['user_id'], data['conversation_id']);

                // append the new message
                appendGroupMessage(conversation_rendered, 
                                   messages_visible, 
                                   conversation,
                                   data['message']);

                // if the conversation window is rendered
                if (conversation_rendered) {
                    // after the new message was appended 
                    // scroll to the bottom of the conversation window
                    var messages_list = conversation.find('.messages-list');
                    var height = messages_list[0].scrollHeight;
                    messages_list.scrollTop(height);
                }
                
            },
            send_message: function(message) {
                return this.perform('send_message', {
                    message: message
                });
            },
            set_as_seen: function(conv_id) {
                return this.perform('set_as_seen', { conv_id: conv_id });
            }
        }
    );
}

$(document).on('submit', '.send-group-message', function(e) {
    e.preventDefault();
    var id = $(this).find('input[name=conversation_id]').val();
    var message_values = $(this).serializeArray();
    App['group_conversation_' + id].send_message(message_values);
});

// if the last message in the conversation is not seen by the user
// mark unseen messages as seen
$(document).on('click', '.conversation-window, .group-conversation', function(e) {
    var latest_message = $('.messages-list ul li:last .row', this);
    var unseen_by_user = latest_message.hasClass('unseen');
    // if not seen by the user
    if (unseen_by_user) {
        var conv_id = $(this).find('.panel').attr('data-gconversation-id');
        // if conv_id doesn't exist, it means that message was seen in messenger
        if (conv_id == null) {
            var conv_id = $(this).find('.messages-list').attr('data-gconversation-id');
        }
        // mark conversation as seen in conversations menu list
        $('#menu-gc' + conv_id).removeClass('unseen-conv');
        latest_message.removeClass('unseen');
        calculateUnseenConversations();
        App['group_conversation_' + conv_id].set_as_seen(conv_id);
    }
});

function MarkGroupConvAsUnseen(message_user_id, conversation_id) {
     // if the message is not sent by the user, mark the conversation as unseen
    if (message_user_id != gon.user_id) {
        newGroupConvMenuListLink(conversation_id);

        // mark the conversation as unseen, after the new message is received
        $('#menu-gc' + conversation_id).addClass('unseen-conv');
        calculateUnseenConversations();
    }
                  
}

// prepend link to the conversation to the top of conversations menu list
function modifyConversationsMenuList(conversation_id) {
    // if the conversation link in conversations menu list exists
    // move conversation link to the top of the conversations menu list
    var conversation_menu_link = $('#conversations-menu ul')
                                     .find('#menu-gc' + conversation_id);
    if (conversation_menu_link.length) {
        conversation_menu_link.prependTo('#conversations-menu ul');
    }
}

// append the new message to the list
function appendGroupMessage(conversation_rendered, 
                            messages_visible, 
                            group_conversation,
                            message) {
    if (conversation_rendered) {
        // if the conversation is collapsed
        if (!messages_visible) {
            // mark its header color
        }
        // append the new message to the list
        group_conversation
            .find('.messages-list')
            .find('ul')
            .append(message);
    }

}

// if the conversation link in the conversations menu list doesn't exist
// create a new link with the receiver's name and prepend it to the list
function newGroupConvMenuListLink(conversation_id) {
    var id_attr = '#menu-gc' + conversation_id;
    var conversation_menu_link = $('#conversations-menu ul').find(id_attr);
    if (conversation_menu_link.length == 0) {
        var list_item = '<li class="conversation-window">\
                             <a data-remote="true"\
                                rel="nofollow"\
                                data-method="post"\
                                href="/group_conversations?group_conversation_id=' +  conversation_id + '">\
                                    group conversation\
                             </a>\
                         </li>';
        $('#conversations-menu ul').prepend(list_item);
    }
}
```

Essentially, it’s very similar to the private conversation’s `.js` file. The layout of the code is a little bit different. The main difference is an ability to pass conversation’s `id` to  a channel and a loop at the top of the file. With this loop we connect a  user to all its group conversations’ channels. That is the reason why  we have used the `belongs_to_conversation` method on the server side. Id’s of the conversations are passed from  the client side. This method on the server side makes sure that a user  really belongs to a provided conversation.

When  you think about it, we could have just created this loop on the server  side and wouldn’t have to deal with all this confirmation process. But  here’s a reason why we pass an id of a conversation from the client  side. When new users get added to a group conversation, we want to  connect them immediately to the conversation’s channel, without  requiring to reload a page. The passable conversation’s id allows us to  effortlessly achieve that. In the upcoming section we’ll create a unique  channel for every user to receive notifications in real time. When new  users will be added to a group conversation, we’ll call the `subToGroupConversationChannel` function, through their unique notification channels, and connect them  to the group conversation channel. If we didn’t allow to pass a  conversation’s id to a channel, connections to new channels would have  occurred only after a page reload. We wouldn’t have any way to connect  new users to a conversation channel dynamically.

Now we are able to send and receive group messages in real time. Try to test the overall functionality with specs on your own.

Commit the changes.

```bash
git add -A
git commit -m "Create a conversation.js inside the
assets/javascripts/channels/group"
```

Inside the `Group::ConversationsController` define an `update` action

```rb
def update
  Group::AddUserToConversationService.new({
    conversation_id: params[:id],
    new_user_id: params[:user][:id],
    added_by_id: params[:added_by]
  }).call
end
```

Create the `Group::AddUserToConversationService`, which is going to take care that a selected user will be added to a conversation

```rb
class Group::AddUserToConversationService

  def initialize(params)
    @group_conversation_id = params[:group_conversation_id]
    @new_user_id = params[:new_user_id]
    @added_by_id = params[:added_by_id]
  end

  def call
    group_conversation = Group::Conversation.find(@group_conversation_id)
    new_user = User.find(@new_user_id)
    added_by = User.find(@added_by_id)
    if new_user.group_conversations << group_conversation
      create_info_message(new_user, added_by)
    end
  end

  private

  def create_info_message(new_user, added_by)
    message = Group::Message.new(
      user_id: added_by.id, 
      content: '' + new_user.name + ' added by ' + added_by.name, 
      added_new_users: [new_user.id], 
      group_conversation_id: @group_conversation_id)
    if message.save
      Group::MessageBroadcastJob.perform_later(message, nil, nil)
    end
  end

end
```

Test the service with specs:

```rb
require 'rails_helper'
require './app/services/group/add_user_to_conversation_service.rb'

describe Group::AddUserToConversationService do
  context '#call' do
    let(:user) { create(:user) }
    let(:new_user) { create(:user) }
    let(:conversation) { create(:group_conversation, users: [user]) }
    let(:add_user_to_conversation) do
      Group::AddUserToConversationService.new({
        conversation_id: conversation.id,
        new_user_id: new_user.id,
        added_by_id: user.id
      }).call
    end

    it 'adds user to a group conversation' do
      add_user_to_conversation
      conversation_users = Group::Conversation.find(conversation.id).users
      expect(conversation_users).to include new_user
    end

    it 'creates an informational message' do
      add_user_to_conversation
      group_conversation = Group::Conversation.find(conversation.id)
      expect(group_conversation.messages.count).to eq 1
    end
  end
end
```

We have working private and group conversations now. A few nuances are still missing, which we will implement later, but the core functionality is here. Users are able to communicate one on one, or if they need, they can build an entire chat room with multiple people.

Commit the changes.

```bash
git add -A
git commit -m "Create a Group::AddUserToConversationService and test it"
```

#### Messenger

What  is the purpose of having a messenger? On mobile screens instead of  opening a conversation window, the app will load the messenger. On  bigger screens, users could choose where to chat, on the conversation  window or on the messenger. If the messenger is going to fill the whole  browser’s window, it should be more comfortable to communicate.

Since  we’ll use the same data and models, we just need to open conversations  in a different environment. Generate a new controller to handle requests  to open a conversation inside the messenger.

```
rails g controller messengers
```

```rb
class MessengersController < ApplicationController
  before_action :redirect_if_not_signed_in

  def index
    @users = User.all.where.not(id: current_user)
  end

  def get_private_conversation
  	conversation = Private::Conversation.between_users(current_user.id, params[:id])
  	@conversation = conversation[0]
  	respond_to do |format|
      format.js { render 'get_private_conversation'}
    end
  end

  def get_group_conversation
    @conversation = Group::Conversation.find(params[:group_conversation_id])
    respond_to do |format|
      format.js { render 'get_group_conversation'}
    end
  end

  def open_messenger
    @type = params[:type]
    @conversation = get_conversation
  end

  private

    def get_conversation
      ConversationForMessengerService.new({
          conversation_type: params[:type],
          user1_id: current_user.id,
          user2_id: params[:id],
          group_conversation_id: params[:group_conversation_id]
        }).call
    end
  
end
```

`get_private_conversation` and `get_group_conversation` actions will get a user’s selected conversation. Those actions’  templates are going to append a selected conversation to the  conversation placeholder. Every time a new conversation is selected to  be opened the old one gets removed and replaced with a newly selected  one.

Define routes for the actions:

```rb
get 'messenger', to: 'messengers#index'
get 'get_private_conversation', to: 'messengers#get_private_conversation'
get 'get_group_conversation', to: 'messengers#get_group_conversation'
get 'open_messenger', to: 'messengers#open_messenger'
```

Commit the changes.

```bash
In the controller is an open_messenger action. The purpose of this action is to go from any page straight to the messenger and render a selected conversation. On smaller screens users are going to chat through messenger instead of conversation windows. In just a moment, we’ll switch links for smaller screens to open conversations inside the messenger.

Create a template for the open_messenger action
```

In the controller is an `open_messenger` action. The purpose of this action is to go from any page straight to  the messenger and render a selected conversation. On smaller screens  users are going to chat through messenger instead of conversation  windows. In just a moment, we’ll switch links for smaller screens to  open conversations inside the messenger.

Create a template for the `open_messenger` action

```html
<div class="container-fluid messenger">
  <div class="row">
    <div class="col-sm-2">
      <ul>
      </ul>
    </div>
    <div class="col-sm-10">
      <div class="conversation">
        <%= render partial: "messengers/#{@type}_conversation",
                      locals: { conversation: @conversation, 
                                user: current_user } %>
      </div>
    </div>
  </div>
</div>

<script>
  $('body nav').hide();
  $('.messenger .col-sm-2').hide();
  $('.messenger .col-sm-10').show();
  $('body').css('margin', '0 0 0 0');
  $('.messenger').css('height', '100vh');
</script>
```

```bash
git add -A
git commit -m "Create an open_messenger.html.erb in the /messengers"
```

Then we see the `ConversationForMessengerSerivce`, it retrieves a selected conversation’s object. Create the service:

```rb
class ConversationForMessengerService
  def initialize(params)
    @conversation_type = params[:conversation_type]
    @user1_id = params[:user1_id] || nil
    @user2_id = params[:user2_id] || nil
    @group_conversation_id = params[:group_conversation_id] || nil
  end

  def call
    if @conversation_type == 'private'
      Private::Conversation.between_users(@user1_id, @user2_id)[0]
    else
      Group::Conversation.find(@group_conversation_id) 
    end
  end

end
```

Add specs for the service:

```rb
require 'rails_helper'
require './app/services/conversation_for_messenger_service.rb'

describe ConversationForMessengerService do
  let(:user1) { create(:user) }
  let(:user2) { create(:user) }
  let(:group_conversation) { create(:group_conversation) }
  let(:private_conversation) do 
    create(:private_conversation,
            sender_id: user1.id,
            recipient_id: user2.id)
  end

  context '#call' do
    it 'returns a group conversation' do
      expect(ConversationForMessengerService.new({
        conversation_type: 'group',
        group_conversation_id: group_conversation.id
      }).call).to eq group_conversation
    end

    it 'returns a private conversation' do
      private_conversation
      expect(ConversationForMessengerService.new({
        conversation_type: 'private',
        user1_id: user1.id,
        user2_id: user2.id
      }).call).to eq private_conversation
    end
  end

end
```

Commit the changes.

```bash
git add -A
git commit -m "Create a ConversationForMessengerSerivce and add specs for it"
```

Create a template for the index action:

```html
<div class="container-fluid messenger">
  <div class="row">
    <%= render 'messengers/index/conversations_list' %>
    <%= render 'messengers/index/conversation' %>
  </div><!-- row -->
</div>
```

This is going to be the messenger itself. Inside the messenger, we’ll be able to see a list of user’s conversations and a selected conversation. Create the partial files:

```html
<div class="col-sm-2">
  <ul>
    <% @all_conversations.each do |conversation| %>
      <%= render partial: conversations_list_item_partial_path(conversation),
                 locals: { conversation: conversation } %>
    <% end %>
  </ul>
</div>
```

Define the helper method:

```rb
module MessengersHelper
  def conversations_list_item_partial_path(conversation)
    # if it's a private conversation
    if conversation.class == Private::Conversation
      'messengers/index/conversations_list_item/private'
    else # it is a group conversation
      'messengers/index/conversations_list_item/group'
    end
  end
end
```

Try to test it with specs yourself.

Create the partial files for links to open conversations:

```html
<% recipient = private_conv_recipient(conversation) %>
<% seen_status = private_conv_seen_status(conversation) %>
<li id="menu-pc<%= conversation.id %>" class="<%= seen_status %>">
  <%= link_to recipient.name, 
              get_private_conversation_path(id: recipient.id), 
              remote: true  %>
</li>
```

```html
<% seen_status = group_conv_seen_status(conversation, current_user) %>
<li id="menu-gc<%= conversation.id %>" class="<%= @seen_by_user %>">
    <%= link_to conversation.name, 
                get_group_conversation_path(group_conversation_id: conversation.id), 
                remote: true %>
</li>
```

Now create a partial for the conversation space, selected conversations are going to be rendered there:

```html
<div class="col-sm-10">
  <div class="conversation">
    <div class="start-conversation">
      <div>
        <i class="fa fa-inbox" aria-hidden="true"></i><br>
        Open a conversation
      </div>
    </div>
  </div>
</div>
```

Commit the changes.

```bash
git add -A
git commit -m "Create a template for the MessengersController's index action"
```

Create a template for the `get_private_conversation` action:

```js
$('.conversation').replaceWith('<div class="conversation private-conversation"></div>');
$('.conversation').append("<%= j(render partial: 'messengers/private_conversation',\
                                        locals: { conversation: @conversation,\
                                                  user: current_user}) %>");
```

Create a `_private_conversation.html.erb` file:

```html
<% @recipient = private_conv_recipient(conversation) %>
<% @contact = get_contact_record(@recipient) %>
<% @is_messenger = true %>
<%= render 'private/conversations/conversation/request_status' %>
<%= render 'messengers/private_conversation/details' %>
<%= render 'private/conversations/conversation/messages_list', 
            conversation: conversation %>
<%= render  'private/conversations/conversation/new_message_form', 
            conversation: conversation,
            user: user %>
```

This file will render a private conversation inside the messenger. Also notice that we reuse some partials from the private conversation views. Create the `_details.html.erb` partial:

```html
<div class="conversation-details">
  <%= link_to :back do %>
    <i class="fa fa-arrow-left back-to-chats-main" aria-hidden="true"></i>
  <% end %>
  <div class="conversation-name">
    <%= @recipient.name %>
  </div>
</div>
```

Commit the changes.

```bash
git add -A
git commit -m "Create a template for the MessengersController's
get_private_conversation action"
```

When we go  to the messenger, it’s better to not see drop down menus on the  navigation bar. Why? We don’t want to render conversation windows inside  the messenger, otherwise it would look chaotic. A conversation window  and the messenger at the same time to chat with the same person. That  would be a highly faulty design.

At  first, forbid conversations’ windows to be rendered on the messenger’s  page. Not that hard to do. To control it, remember how conversations’  windows are rendered on the app. They are rendered inside the `application.html.erb` file. Then we have `@private_conversations_windows`and `@group_conversations_windows` instance variables. Those variables are arrays of conversations.  Instead of just rendering conversations from those arrays, define helper  methods to decide to give those arrays to users or not, depending on  which page they are in. If users are inside the messenger’s page, they  will get an empty array and no conversations’ windows will be rendered.

Replace those instance variables with `private_conversations_windows` and `group_conversations_windows` helper methods. Now define them inside the `ApplicationHelper`

```rb
def private_conversations_windows
  params[:controller] != 'messengers' ? @private_conversations_windows : []
end

def group_conversations_windows
  params[:controller] != 'messengers' ? @group_conversations_windows : []
end
```

Wrap them with specs

```rb
require 'rails_helper'

RSpec.describe ApplicationHelper, :type => :helper do
  context '#private_conversations_windows' do
    let(:conversations) { conversations = create_list(:private_conversation, 2) }
    
    it 'returns private conversations' do
      assign(:private_conversations_windows, conversations)
      controller.params[:controller] = 'not_messengers'
      expect(helper.private_conversations_windows).to eq conversations
    end

    it 'returns an empty array' do
      assign(:private_conversations_windows, conversations)
      controller.params[:controller] = 'messengers'
      expect(helper.private_conversations_windows).to eq []
    end
  end

  context '#group_conversations_windows' do
    let(:conversations) { create_list(:group_conversation, 2) }

    it 'returns group conversations' do
      assign(:group_conversations_windows, conversations)
      controller.params[:controller] = 'not_messengers'
      expect(helper.group_conversations_windows).to eq conversations
    end

    it 'returns an empty array' do
      assign(:group_conversations_windows, conversations)
      controller.params[:controller] = 'messengers'
      expect(helper.group_conversations_windows).to eq []
    end
  end
end
```

Commit the changes

```bash
git add -A
git commit -m "
Define private_conversations_windows and group_conversations_windows
helper methods inside the ApplicationHelper and test them"
```

Next, create an alternative partial file for navigation’s header, so drop down menus won’t be rendered. Inside the `NavigationHelper`, we’ve defined the `nav_header_content_partials` helper method before. It determines which navigation’s header to render.

Inside the

```
layouts/navigation/header
```

directory, create a `_messenger_header.html.erb` file

```html
<%= link_to 'collabfield', root_path, class: 'navbar-brand' %>
<div class="pull-right" id="messages-page-name">Messages</div>
```

Style the messenger. Create a `messenger.scss` file inside the `partials`directory

```scss
.messenger {
  z-index: 2;
  padding: 0;
  background-color: white;
  height: calc(100vh - 50px);
  .conversation-details {
    z-index: 3;
    background-color: white;
    position: fixed;
    top: 0;
    width: 100%;
    text-align: center;
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
    .back-to-chats-main, .conversation-name {
      height: 50px;
      line-height: 50px;
      vertical-align: middle;
      color: $navbarColor;
    }
    .back-to-chats-main {
      position: absolute;
      left: 10px;
      font-size: 24px;
      font-size: 2.4rem;
    }
    .conversation-name {
      display: inline-block;
      font-size: 20px;
      font-size: 2.0rem;
    }
  }
  .row {
    height: 100%;
  }
  .col-sm-2, .col-sm-10, .conversation {
    height: 100%;
  }
  .conversation {
    position: relative;
    .contact-request-sent {
      display: none !important;
    }
    .start-conversation {
      height: 100%;
      display: table;
      margin: 0 auto;
      div {
        display: table-cell;
        vertical-align: middle;
        text-align: center;
        i {
          font-size: 40px;
          font-size: 4.0rem;
        }
      }
    }
  }
  .col-sm-2 {
    padding: 0;
    background-color: $navbarColor;
    ul {
      padding: 20px 0 0 0;
      background-color: $navbarColor;
      li a {
        color: white;
        display: inline-block;
        padding: 10px 0 10px 10px;
        width: 100%;
        border-bottom: 1px solid rgba(255,255,255,0.4);
        &:hover {
          background-color: white;
          color: black;
        }
      }
    }
    border-right: 1px solid $navbarColor;
  }
  .messages-list {
    min-height: 100%;
    height: 100%;
  }
  .send-private-message, .send-group-message {
    z-index: 3;
    position: absolute;
    width: 100%;
    bottom: 7px;
  }
  .contact-request-status {
    width: 100%;
  }
}
```

Commit the change

```bash
git add -A
git commit -m "Create a messenger.scss inside the partials"
```

Inside the `desktop.scss`, within the `min-width: 767px`, add

```scss
.messenger {
  .col-sm-2 {
    display: initial !important;
  }
  .col-sm-2, .col-sm-10 {
    display: initial;
  }
  .conversation {
    padding: 0 0 60px 0;
    .conversation-details {
      display: none;
    }
  }
}
```

When we click on a conversation to open it, we want to be able to load previous messages somehow. We could add a visible link for loading them. Or we can automatically load some amount of messages until the scroll bar appears, so a user could load previous messages by scrolling up. Create a helper method which will take care of it

```rb
# in the messenger load previous messages until the scroll bar appears
def autoload_messenger_messages
  if @is_messenger == 'true'
    # if previous messages exist, load them
    if @messages_to_display_offset != 0
      'shared/load_more_messages/messenger/load_previous_messages'
    else 
      # remove load previous messages link 
      'shared/load_more_messages/messenger/remove_previous_messages_link'
    end 
  else
    'shared/empty_partial'
  end
end
```

Test it with specs on your own. Create the partial files

```js
var scrollbar_visible = $('.conversation .messages-list').scrollTop();
if (scrollbar_visible == 0) {
    $('.conversation .messages-list .load-more-messages').click();
}
```

```js
$('body .conversation .messages-list .loading-more-messages')
    .replaceWith('');
$('body .conversation .messages-list .load-more-messages')
.replaceWith('');
```

Commit the changes

```bash
git add -A
git commit -m "Define an autoload_messenger_messages in the
Shared::MessagesHelper"
```

Use the helper method inside the `_load_more_messages.js.erb` file, just above the `<%= render remove_link_to_messages %>`

```js
<%= render autoload_messenger_messages %>
```

Now we have `append_previous_messages_partial_path` and   
`replace_link_to_private_messages_partial_path` helper methods which we should update, to make them compatible with the messenger

```rb
def append_previous_messages_partial_path
  # if a conversation is opened in the messenger
  if @is_messenger == 'true'
    'shared/load_more_messages/messenger/append_messages' 
  else 
    'shared/load_more_messages/window/append_messages' 
  end 
end
```

Create a missing partial file

```js
// temporary remove the load more messages link 
// so it cannot be clicked if new messages aren't rendered yet
$('body .conversation .messages-list .load-more-messages')
    .replaceWith('<span class="load-more-messages"></span>');
// render previous messages
$('body .conversation .messages-list ul')
    .prepend('<%= j render "#{@type}/conversations/messages" %>');
// after new messages are appended, leave a gap at the top of the scrollbar
$('body .conversation .messages-list').scrollTop(400);
```

Update another method

```rb
def replace_link_to_private_messages_partial_path
  if @is_messenger == 'true'
    'private/messages/load_more_messages/messenger/replace_link_to_messages'
  else
    'private/messages/load_more_messages/window/replace_link_to_messages'
  end
end
```

Create the partial file

```js
$('.conversation .load-more-messages')
    .replaceWith('\
        <%= j render partial: "private/conversations/conversation/messages_list/link_to_previous_messages",\
                     locals: { conversation: @conversation } %>\
        ');
```

Test the helper methods with specs on your own.

Commit the changes

```bash
git add -A
git commit -m "
- Update the append_previous_messages_partial_path helper method in
  Shared::MessagesHelper
- Update the replace_link_to_private_messages_partial_path method in
  Private::MessagesHelper"
```

Now after an initial load messages link click, the app will automatically keep loading previous messages until there is a scroll bar on the messages list. To make the initial click happen, add some JavaScript:

```js
$(document).on('turbolinks:load ajax:complete', function() {
    var messages_visible = $('.conversation .messages-list ul', this)
                               .has('li').length;
    var previous_messages_exist = $('.conversation .messages-list .load-more-messages', this).length;
    // Load previous messages if messages list is empty && scrollbar doesn't exist
    if (!messages_visible && previous_messages_exist) {
        $('.load-more-messages', this)[0].click();
        $('.conversation .messages-list .loading-more-messages').hide();
    }
});
```

When you visit the `/messenger` path, you see the messenger:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-112.png)

Then you can open any of your conversations.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-113.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-114.png)

Commit the changes.

Now on  smaller screens, when users click on the navigation bar’s link to open a  conversation, their conversation should be opened inside the messenger  instead of a conversation window. To make this possible, we’ve to create  different links for smaller screens.

Inside the navigation’s `_private.html.erb` partial, which stores a link to open a private conversation, add an  additional link for smaller screen devices. Add this link just below the  `open_private_conversation_path` path’s link in the file

```html
<%= link_to recipient.name, 
        open_messenger_path(id: recipient.id, 
                            smaller_device: true, 
                            type: 'private'), 
        class: 'smaller-screen-link' %> 
```

On smaller screens, this link is going to be shown instead of the previous one, dedicated for bigger screens. Add an additional link to open group conversations too

```html
<%= link_to truncate(conversation.name, :length => 40), 
          open_messenger_path(group_conversation_id: conversation.id, 
          smaller_device: true, type: 'group'), 
          class: 'smaller-screen-link' %> 
```

The reason why we see different links on different screen sizes is that previously we’ve set CSS for `bigger-screen-link` and `smaller-screen-link`classes.

Commit the changes.

```bash
git add -A
git commit -m "Inside _private.html.erb and _group.html.erb, in the 
layouts/navigation/header/dropdowns/conversations, add alternative
links for smaller devices to open conversations"
```

Messenger’s versions on desktop and mobile devices are going to differ a little bit. Write some JavaScript inside the `messenger.js`, so after a user clicks to open a conversation, js will determine to show a mobile version or not.

```js
// if the messenger is opened on a smaller screen device
// show the messenger's version for mobile devices
$(".messenger .col-sm-2 ul").on( "click", "a", function() {
    var col_2_width = $('.messenger .col-sm-2').css('width');
    var window_width = '' + $('.messenger').width() + 'px';
    // check if bootstrap columns are stacked (page is opened on a smaller device)
    if (col_2_width == window_width) {
        $('body nav').hide();
        $('.messenger .col-sm-2').hide();
        $('.messenger .col-sm-10').show();
        $('body').css('margin', '0 0 0 0');
        $('.messenger').css('height', '100vh');
    }
});
```

Now when you open a conversation on a mobile device, it looks like this

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-115.png)

Commit the change.

```bash
git add -A
git commit -m "Add JavaScript to messenger.js to show a different
messenger's version on mobile devices"
```

Now make group conversations functional on the messenger. Majority of  work with the messenger is already done, so setting up group  conversations is going to be much easier. If you look back inside the `MessengersController`, we have the `get_group_conversation` action. Create a template file for it:

```js
$('.conversation').replaceWith('<div class="conversation group-conversation"></div>');
$('.conversation').append("<%= j(render 'messengers/group_conversation',\
                                         conversation: @conversation) %>");
```

Then create a file to render a group conversation in the messenger:

```html
<% @is_messenger = true %>
<%= render 'messengers/group_conversation/details', 
            conversation: conversation %>
<%= render 'group/conversations/conversation/messages_list', 
            conversation: conversation %>
<%= render 'messengers/group_conversation/new_message_form', 
            conversation: conversation %>
```

Create its partials:

```html
<div class="conversation-details">
  <%= link_to :back do %>
    <i class="fa fa-arrow-left back-to-chats-main" aria-hidden="true"></i>
  <% end %>
  <div class="conversation-name">
    <%= conversation.name %>
  </div>
</div>
```

```html
<form class="send-group-message">
  <input  name="conversation_id" 
          type="hidden" 
          value="<%= conversation.id %>">
  <input name="user_id" type="hidden" value="<%= current_user.id %>">
  <textarea name="content" 
            rows="2" 
            class="form-control" 
            placeholder="Type a message..."></textarea>
  <input type="submit" class="btn btn-success send-message">
</form>
```

Commit the changes:

```bash
git add -A
git commit -m "Create a get_group_conversation.js.erb template and 
its partials inside the messengers"
```

That’s what group conversations in the messenger look like:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-116.png)

### 5. Notifications

The  application already has all fundamental features ready. In this section  we’ll put our energy on enhancing those vital features. Instantaneous  notifications, when other users try to get in touch with you, provide a  better user experience. Let’s make users aware whenever they get a  contact request update or joined to a group conversation.

#### Contact requests

Generate a notification channel which will handle all user’s notifications.

```bash
rails g channel notification
```

```rb
class NotificationChannel < ApplicationCable::Channel
  def subscribed
    stream_from "notifications_#{current_user.id}"
  end

  def unsubscribed
    stop_all_streams
  end

  def contact_request_response(data)
    receiver_user_name = data['receiver_user_name']
    sender_user_name = data['sender_user_name']
    notification = data['notification']
    receiver = User.find_by(name: receiver_user_name)

    ActionCable.server.broadcast(
      "notifications_#{receiver.id}",
      notification: notification,
      sender_user_name: sender_user_name,
    )

  end
end
```

Commit the change.

```bash
git add -A
git commit -m "Create a NotificationChannel"
```

Every user is going to have its own unique notification channel. Then we have the `ContactRequestBroadcastJob`, which will broadcast contact requests and responses.

Generate the job.

```bash
rails g job contact_request_broadcast
```

```rb
class ContactRequestBroadcastJob < ApplicationJob
  queue_as :default

  def perform(contact_request)

    sender = User.find(contact_request.user_id)
    receiver = User.find(contact_request.contact_id)
    ActionCable.server.broadcast(
      "notifications_#{receiver.id}",
      notification: 'contact-request-received',
      sender_name: sender.name,
      contact_request: render_contact_request(sender, contact_request)
    )

  end

  private

  def render_contact_request(sender, contact_request)
    ApplicationController.render(
      partial: 'contacts/contact_request',
      locals: { sender: sender }
    )
  end

end
```

Create a `_contact_request.html.erb` partial, which will be used to add contact requests in the navigation  bar’s drop down menu. In this case we’ll add those requests dynamically  with the `ContactRequestBroadcastJob`

```html
<li class="contact-request" data-user-name="<%= sender.name %>">
  <div class="sixty-percent">
    <span class="contact-name"><%= sender.name %></span> 
  </div>
  <div class="forty-percent">
    <span class="accept-request">
      <%= link_to "Accept",  
                  contact_path(id: sender.id), 
                  remote: true, 
                  method: "put" %>
    </span> 
    <span class="decline-request">
      <%= link_to "Decline",
                  contact_path(id: sender.id), 
                  remote: true, 
                  method: :delete %>
    </span>
  </div>
</li>
```

Fire the job every time a new `Contact` record is created:

```rb
after_create_commit { ContactRequestBroadcastJob.perform_later(self) }
```

Commit the changes.

```bash
git add -A
git commit -m "Create a ContactRequestBroadcastJob"
```

Then create a drop down menu itself on the navigation bar:

```html
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
  <i class="fa fa-user-o" aria-hidden="true">
    <span id="unresponded-contact-requests"></span>
  </i>
</a>
<ul class="dropdown dropdown-menu" role="menu">
  <%= render nav_contact_requests_partial_path %>
</ul><!-- dropdown-menu -->
```

Define the `nav_contact_requests_partial_path` helper method:

```rb
def nav_contact_requests_partial_path
  # if contact requests exist
  if current_user.pending_received_contact_requests.present? 
    'layouts/navigation/header/dropdowns/contact_requests/requests' 
  else # contact requests do not exist 
    'layouts/navigation/header/dropdowns/contact_requests/no_requests'
  end
end
```

Wrap the method with specs and then create the partial files:

```html
<% current_user.pending_received_contact_requests.each do |user| %>
  <%= render partial: "layouts/"\
                      "navigation/"\
                      "header/"\
                      "dropdowns/"\
                      "contact_requests/"\
                      "request", 
             locals: { user: user } %>
<% end %>
```

```html
<li class="no-requests">You have no new requests</li>
```

Inside the `_dropdowns.html.erb` file, render the `_contact_requests.html.erb`, just below the conversations. So we could see a drop down menu of contacts’ requests on the navigation bar

```html
<div class='pull-right' id='contacts-requests'>
  <%= render 'layouts/navigation/header/dropdowns/contact_requests' %>
</div>
```

Commit the changes.

```bash
git add -A
git commit -m "
- Create a _contact_requests.html.erb inside the
  layouts/navigation/header/dropdowns
- Define a nav_contact_requests_partial_path in NavigationHelper"
```

Also create a partial file for a single contact request:

```html
<li class="contact-request" data-user-name="<%= user.name %>">
  <div class="sixty-percent">
    <span class="contact-name"><%= user.name %></span> 
  </div>
  <div class="forty-percent">
    <span class="accept-request">
      <%= link_to "Accept",  
                  contact_path(id: user.id), 
                  remote: true, 
                  method: "put" %>
    </span> 
    <span class="decline-request">
      <%= link_to "Decline",
                  contact_path(id: user.id), 
                  remote: true, 
                  method: :delete %>
    </span>
  </div>
</li><!-- contact-request -->
```

Commit the change.

```bash
git add -A
git commit -m "Create a _request.html.erb inside the
layouts/navigation/header/dropdowns"
```

Add CSS to style and position the contact requests’ drop down menu:

```scss
#contacts-requests {
  li {
    color: black;
    background-color: $backgroundColor;
    border-bottom: 1px solid $navbarColor;
  }
  i {
    position: relative;
  }
  .sixty-percent {
    display: inline-block;
    width: 60%;
  }
  .forty-percent {
    display: inline-block;
    float: right;
    width: 40%;
  }
  .contact-request, .contact-request-responded {
    .contact-name {
      padding-left: 10px;
      padding-right: 20px;
    }
    .accept-request, .decline-request {
      a {
        border: 2px solid $navbarColor;
        padding: 5px;
      }
      &:hover a {
        border-color: black;
      }
      transition: 0.15s border-color;
      transition: 0.15s background-color;
    }
    .accept-request {
      a:hover {
        background-color: black !important;
      }
      a {
        background-color: $navbarColor;
        color: white !important;
      }
    }
    .decline-request {
      a {
        background-color: $backgroundColor;
        color: black !important;
      }
      a:hover, &:hover {
        background-color: white !important;
      }
    }
    .accepted-request {
      background: $navbarColor;
      color: white;
      padding: 5px;
    }
  }
  .no-requests {
    text-align: center;
  }
}

#unresponded-contact-requests {
  top: 0;
  right: 5px;
  background: #3F4EBF;
}
```

Commit the changes.

```bash
git add -A
git commit -m "Add CSS in navigation.scss to style and position the
contact requests drop down menu"
```

On the navigation bar, we can see a drop down menu for contact requests now.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-117.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-118.png)

We have the notifications channel and the job to broadcast contact requests’ updates. Now we need to create a connection on the client side, so users could send and receive data in real time.

```js
App.notification = App.cable.subscriptions.create("NotificationChannel", {
  connected: function() {},
  disconnected: function() {},
  received: function(data) {
    // if a contact request was accepted
    if (data['notification'] == 'accepted-contact-request') {

    }
    // if a contact request was declined
    if (data['notification'] == 'declined-contact-request') {
      
    }
    // if a contact request was received
    if (data['notification'] == 'contact-request-received') {
      conversation_window = $('body').find('[data-pconversation-user-name="' + data["sender_name"] + '"]');
      has_no_contact_requests = $('#contacts-requests ul').find('.no-requests');
      contact_request = data['contact_request'];

      if (has_no_contact_requests.length) {
        // remove has no contact request message
        has_no_contact_requests.remove();
      }

      if (conversation_window.length) {
        // remove add user to contacts button
        conversation_window.find('.add-user-to-contacts-message').parent().remove();

        conversation_window.find('.add-user-to-contacts').remove();
        conversation_window.find('.conversation-heading').css('width', '360px');
      }

      // append a new contact request
      $('#contacts-requests ul').prepend(contact_request);
      calculateContactRequests();
    }

  },
  contact_request_response: function(sender_user_name, receiver_user_name, notification) {
    return this.perform('contact_request_response', {
      sender_user_name: sender_user_name,
    	receiver_user_name: receiver_user_name,
    	notification: notification
    });
  }
});
```

Notice that `if` statements,  where a contact request was accepted and declined, have empty code  blocks. You can play around and add your own code here.

Also create a `contact_requests.js` file to perform DOM changes after certain events and broadcast performed actions to the opposed user, using the `contact_request_response` callback function

```js
$(document).on('turbolinks:load', function() {
    // when a contact request is accepted, mark it as accepted
    $('body').on('click', '.accept-request a', function() {
        var sender_user_name = $('nav #user-name').html();
        var receiver_user_name = $(this)
                                    .parents('[data-user-name]')
                                    .attr('data-user-name');
                                    
        var requests_menu_item = $('#contacts-requests ul');
        requests_menu_item = requests_menu_item
                                 .find('\
                                       [data-user-name="' + 
                                       receiver_user_name + 
                                       '"]');
        var conversation_window_request_status = $('.conversation-window')
                                                    .find('[data-user-name="' + 
                                                           receiver_user_name + 
                                                           '"]');
        // if a conversation is opened in the messenger                                            
        if(conversation_window_request_status.length == 0) {
          conversation_window_request_status = $('.contact-request-status');
        }   
        requests_menu_item.find('.decline-request').remove();
        requests_menu_item
            .find('.accept-request')
            .replaceWith('<span class="accepted-request">Accepted</span>');
        requests_menu_item
            .removeClass('contact-request')
            .addClass('contact-request-responded');
        conversation_window_request_status
            .replaceWith('<div class="contact-request-status">\
                              Request has been accepted\
                          </div>');
        calculateContactRequests();
        // update the opposite user with your contact request response
        App.notification.contact_request_response(sender_user_name, 
                                                  receiver_user_name, 
                                                  'accepted-contact-request');
    });
    
    // when a contact request is declined, mark it as declined
    $('body').on('click', '.decline-request a', function() {
        var sender_user_name = $('nav #user-name').html();
        var receiver_user_name = $(this)
                                    .parents('[data-user-name]')
                                    .attr('data-user-name');
        var requests_menu_item = $('#contacts-requests ul')
                                    .find('[data-user-name="' + 
                                           receiver_user_name + 
                                           '"]');
        var conversation_window_request_status = $('.conversation-window')
                                                    .find('[data-user-name="' + 
                                                           receiver_user_name + 
                                                           '"]');
        // if a conversation is opened in the messenger                                            
        if(conversation_window_request_status.length == 0) {
          conversation_window_request_status = $('.contact-request-status');
        }   
        requests_menu_item.find('.accept-request').remove();
        requests_menu_item
            .find('.decline-request')
            .replaceWith('<span class="accepted-request">Declined</span>');
        requests_menu_item
            .removeClass('contact-request')
            .addClass('contact-request-responded');
        conversation_window_request_status
            .replaceWith('<div class="contact-request-status">\
                              Request has been declined\
                          </div>');
        calculateContactRequests();
        // update the opposite user with your contact request response
        App.notification.contact_request_response(sender_user_name, 
                                                  receiver_user_name, 
                                                  'declined-contact-request');
    });

    // when a contact request is sent
    $('body').on('click', '.add-user-to-contacts-notif', function() {
        var sender_user_name = $('nav #user-name').html();
        var receiver_user_name = $(this)
                                    .parents('.conversation-window')
                                    .find('.contact-name-notif')
                                    .html();
        App.notification.contact_request_response(sender_user_name, 
                                                  receiver_user_name, 
                                                  'contact-request-received');
    });

    calculateContactRequests();
});

function calculateContactRequests() {
  var unresponded_requests = $('#contacts-requests ul')
                                .find('.contact-request')
                                .length;
  if (unresponded_requests) {
    $('#unresponded-contact-requests').css('visibility', 'visible');
    $('#unresponded-contact-requests').text(unresponded_requests);
  } else {
    $('#unresponded-contact-requests').css('visibility', 'hidden');
    $('#unresponded-contact-requests').text('');
  }
}
```

Also after a new contact request is sent from a conversation window,  remove the option to send the request again. Inside the conversation’s `options.js` file, add the following:

```js
// on the add-user-to-contacts link click
// remove the link and notify, that the request has been sent
$(document).on('click', 
               '.add-user-to-contacts, .add-user-to-contacts-notif', 
               function(e) {
    var conversation_window = $(this).parents('.conversation-window,\
                                               .conversation');
    conversation_window
        .find('.add-user-to-contacts')
        .replaceWith('<div class="contact-request-sent"\
                           style="display: block;">\
                          <div>\
                              <i class="fa fa-question"\
                                 aria-hidden="true"\
                                 title="Contact request sent">\
                              </i>\
                          </div>\
                      </div>');
    conversation_window.find('.add-user-to-contacts-message').remove();
    conversation_window
        .find('.messages_list ul')
        .append('<div class="add-user-to-contacts-message">\
                     Contact request sent\
                 </div>');
});
```

Now contact requests are going to be handled in real time and the user interface will be changed after particular events.

Thanks to Toni Shortsleeve.

