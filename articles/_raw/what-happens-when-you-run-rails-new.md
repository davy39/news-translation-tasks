---
title: What happens when you create a new Rails project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-08T01:12:00.000Z'
originalURL: https://freecodecamp.org/news/what-happens-when-you-run-rails-new
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca107740569d1a4ca4c41.jpg
tags:
- name: Ruby on Rails
  slug: ruby-on-rails
seo_title: null
seo_desc: 'By Travis Fantina

  The first time you open your terminal and write rails new the sheer number of files
  and folders that are created can be overwhelming. You may even work on numerous
  Rails projects without ever opening many of these folders - so what ...'
---

By Travis Fantina

The first time you open your terminal and write `rails new` the sheer number of files and folders that are created can be overwhelming. You may even work on numerous Rails projects without ever opening many of these folders - so what exactly are they? What are they doing behind the scenes? 

Well, the truth is that you don’t need many of them and Rails has several flags built into the `new` command which will allow you to create a new project without some of the built-in defaults of Rails (to learn more just type out `rails new —help`). That said, for most projects you’ll be running `rails new` and creating a beastly project folder. 

In this post I’m going to go through every single file and folder in a new Rails 6 project. Feel free to use this as a reference as you are working through your new Rails project to understand some of the more obscure folders. Bookmark this post and return to it anytime you find yourself in the weeds on a new Rails project.

So let's start:

`rails new example-project`

Wow, that’s a lot!

First, Rails is creating all the files and folders required by a new Rails app.  
Then it’s fetching gems and bundling them; these are the dependencies that Rails needs in order to run your website in its simplest iteration. Seem like a lot? To some extent it is but these gems add the functionality that makes a Rails project so easy to get off the ground. Essentially all you need to do now is run `rails server` and you have a webapp running locally: that’s pretty powerful and not something you can get so easily /without/ all that boilerplate.

Let's get into all those folders:

```shell
  create README.md
   create Rakefile
   create .ruby-version
   create config.ru
   create .gitignore
   create Gemfile
     run git init from "."
Initialized empty Git repository in /Users/tfantina/Documents/Code/FileStructure/.git/
   create package.json
   create app
   create app/assets/config/manifest.js
   create app/assets/stylesheets/application.css
   create app/channels/application_cable/channel.rb
   create app/channels/application_cable/connection.rb
   create app/controllers/application_controller.rb
   create app/helpers/application_helper.rb
   create app/javascript/channels/consumer.js
   create app/javascript/channels/index.js
   create app/javascript/packs/application.js
   create app/jobs/application_job.rb
   create app/mailers/application_mailer.rb
   create app/models/application_record.rb
   create app/views/layouts/application.html.erb
   create app/views/layouts/mailer.html.erb
   create app/views/layouts/mailer.text.erb
   create app/assets/images/.keep
   create app/controllers/concerns/.keep
   create app/models/concerns/.keep
   create bin
   create bin/rails
   create bin/rake
   create bin/setup
   create bin/yarn
   create config
   create config/routes.rb
   create config/application.rb
   create config/environment.rb
   create config/cable.yml
   create config/puma.rb
   create config/spring.rb
   create config/storage.yml
   create config/environments
   create config/environments/development.rb
   create config/environments/production.rb
   create config/environments/test.rb
   create config/initializers
   create config/initializers/application_controller_renderer.rb
   create config/initializers/assets.rb
   create config/initializers/backtrace_silencers.rb
   create config/initializers/content_security_policy.rb
   create config/initializers/cookies_serializer.rb
   create config/initializers/cors.rb
   create config/initializers/filter_parameter_logging.rb
   create config/initializers/inflections.rb
   create config/initializers/mime_types.rb
   create config/initializers/new_framework_defaults_6_0.rb
   create config/initializers/wrap_parameters.rb
   create config/locales
   create config/locales/en.yml
   create config/master.key
   append .gitignore
   create config/boot.rb
   create config/database.yml
   create db
   create db/seeds.rb
   create lib
   create lib/tasks
   create lib/tasks/.keep
   create lib/assets
   create lib/assets/.keep
   create log
   create log/.keep
   create public
   create public/404.html
   create public/422.html
   create public/500.html
   create public/apple-touch-icon-precomposed.png
   create public/apple-touch-icon.png
   create public/favicon.ico
   create public/robots.txt
   create tmp
   create tmp/.keep
   create tmp/cache
   create tmp/cache/assets
   create vendor
   create vendor/.keep
   create test/fixtures
   create test/fixtures/.keep
   create test/fixtures/files
   create test/fixtures/files/.keep
   create test/controllers
   create test/controllers/.keep
   create test/mailers
   create test/mailers/.keep
   create test/models
   create test/models/.keep
   create test/helpers
   create test/helpers/.keep
   create test/integration
   create test/integration/.keep
   create test/channels/application_cable/connection_test.rb
   create test/test_helper.rb
   create test/system
   create test/system/.keep
   create test/application_system_test_case.rb
   create storage
   create storage/.keep
   create tmp/storage
   create tmp/storage/.keep
   

```

Let's jump in:

```
cd example-project
code . 

```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0DE7CF47-259B-4346-8FB4-DEE2EE74709B.png)
_In VSCode this is what we have_

We will go in order as Rails organizes them, for the most part, I will be talking about every single folder and file, for repeated files (such as .keep) I will only mention it once.  You will notice a lot of conventions in Rails such as “application_[framework]s” (`application_controller.rb`, `application_helper.rb`, `application_job.rb` etc).  In such instances I will cover the folder in detail so you know what goes inside, just know that the existing file “application_[...].rb” is a parent class that other classes you create in the folder will inherit from.

# The app folder

Is where the majority of your development work will take place /app contains the Models, Views, and Controllers that will be served to users when requested by the browser.

### app/assets

Stores assets for the Rails Asset Pipeline. The Asset Pipeline brings together the assets (JavaScript, CSS, and images), in a project and serves them to the client in the most efficient way possible. It does this by concatenating and minifying assets. It also precompiles assets written in Sass and CoffeeScript.  
More info: [The Asset Pipeline — Ruby on Rails Guides](https://guides.rubyonrails.org/asset_pipeline.html)

### app/assets/config

See below

#### app/assets/config/manifest.js

The aforementioned Asset Pipeline is managed by a Ruby gem called “Sprockets-rails” which does all of the above. “Sprockets-rails” has some associated helper gems such as “sass-rails”, “uglifier” and “coffee-rails”. Coffee-rails and Sass-rails precompile your Sass and CoffeeScript into CSS and JavaScript while Uglifier minifies these assets.  Manifest.js lets you specifically set what is going to get pre-compiled.  
For more on this specific file see: [eileen.codes | Rails 5: The Sprockets 4 Manifest](https://eileencodes.com/posts/the-sprockets-4-manifest/)

### app/assets/images

Image assets, such as icons and SVGs for the Asset Pipeline can be placed here.

#### .keep

This is the first of many .keep files you will see throughout a new Rails project. These are not Rails files but files for Git which won’t normally track empty folders. The keep. file just says “someone’s in here”. Anything with a .keep file will be tracked by Git. You don’t need .keep if you put something else in the folder.

### app/assets/stylesheets

The stylesheets folder is where you will place styles associated with your app. You can write stylesheets in CSS or SASS out of the box., the Asset Pipeline will precompile any and all stylesheets for you.

#### app/assets/stylesheets/application.css

Contains all styles that will be included in the Asset Pipeline.  Global styles can be written in Application.css but you can also write Controller specific stylesheets (when you run the command `rails g`  to create a new Controller it will create an associated stylesheet.  `=require_tree .`  is Rails way of including all associated folders inside a directory so any other CSS files inside this project will be included when compiled `=require_self` will include any CSS that you write inside the Application.css file itself, this is location specific so the CSS inside Application.css will be run /after/ the other folders that are pulled in by `require_tree .`

## .app/channels

Rails has numerous smaller internal frameworks. ActionCable is a framework that lets you use WebSockets to create realtime features in your app like chats and auto-updating “subscriptions” to notifications and new content. If you are not going to implement any realtime features you don’t need to worry about any ActionCable folders. The channels folder holds the server-side Ruby files for creating these connections.  
You can read all about ActionCable here: [Action Cable Overview — Ruby on Rails Guides](https://guides.rubyonrails.org/action_cable_overview.html)

### app/channels/application_cable

Application_cable holds channel and connection files for creating new realtime features in your app.

#### app/channels/application_cable/channel.rb

Each individual realtime features of your app would be encapsulated into an individual channel channel. For example, a chat feature chat, could be one channel. A notification system for newly published content would be a separate channel. This folder contains all the channels of your application.

#### app/channels/application_cable/connection.rb

Connections are the authentication between the user and the server. They don’t deal with any logic (that’s what channels do), rather they just check to make sure the current user is authorized to subscribe to the various channels in your application. In most cases, this would be a simple verification that the user is logged in.

## app/controllers

Part “C” of the “MVC” pattern in Model View Controllers. Controllers like a middleman between the model and the view. Based on the user’s request the Controller will grab any associated data from the Model and pass it to the view which the user is shown. For example, if a user is navigating to the localhost:3000/posts page the Controller will determine what View they are shown as well as any associated records from the Model.

### app/controllers/concerns

Concerns are a way to shrink your Models down, rather than writing a huge amount of reusable methods in a single model you can throw those methods into concerns where they can be easily reused in your Controllers.

### app/controllers/application_controller.rb

Controllers are just ruby classes that inherit from a class called ActionController. As you add more models to your project you will have more controllers to deal with. application_controller.rb is required for any Rails project because it inherits from `ActionController::Base` and all future controllers intern inherit from it, giving them the functionality of Controllers.  
You’ll see a lot of “application_[insert relative title here].rb” files: application_controller.rb, application_helper.rb, application_record.rb. In most cases, these represent a global way of interacting with the app, an intermediary that inherits from a base class and then is inherited by future classes or both. I won’t discuss the functions of these files in all cases.

## app/helpers

Helpers are a way to keep your views tidy. Views should be concerned simply with displaying information as html to the user. If you find your html.erb files are getting bogged down with lots of little calculations or logic you should move that code into helper methods.

### app/helpers/application_helper.rb

Provides a place to write global helpers, as you create more Controllers you will have more helpers to work with specific Controllers and Views.

## app/javascript

This folder is a handy place to put all the javascript you use in your application, the Rails Asset Pipeline will include them from this folder into any pages where they apply (the Asset Pipeline knows where the scripts belong because the files, normally, follow a naming convention of the Controller they apply too).

### app/javascript/channels

We’ve already looked at ActionCable’s channels above but this folder contains client-side specific javascript for creating realtime WebSocket connections.

#### app/javascript/channels/consumer.js

Consumers are the clients of a WebSocket connection; the end-users who are subscribing to the channel. This script will connect those consumers to the channel on the client-side.

#### app/javascript/channels/index.js

An application can have multiple Channels (chat, alerts, new posts, etc). index.js is a client-side directory of all the channels in your application.

#### app/javascript/packs/application.js

Webpacker is a ruby gem which allows you to use Webpack, the JavaScript bundler in your Rails project. It works in conjunction with the Asset Pipeline and is intended for large JavaScript frameworks, not small scripts or other assets like CSS or images (which Webpack generally would handle in a Javascript project).  Webpacker, however, is flexible and this is just the default. You can have Webpack handle images and smaller JavaScripts completely bypassing the Asset Pipeline if you’d like. You can specify that in this folder by requiring different assets. The default assets that get packed are:

```js
*require("@rails/ujs").start()*
*require("turbolinks").start()*
*require("@rails/activestorage").start()*
*require("channels")*


```

### app/jobs

Jobs are background tasks that you run while users continue to use your application Any time you have an operation that will involve a lot of processing, enough to slow the user’s experience down significantly and cause your application to “hang”, you should create a background job that will run the task behind the scenes allowing the user to continue using your site uninterrupted.  
For more info on Jobs see: [Rails Active Job Tutorial: How to Use activejob | Codeship | via @codeship](https://blog.codeship.com/how-to-use-rails-active-job/)

#### app/assets/jobs/application_job.rb

See above.

## app/mailers

You can think of mailers as controllers for emails. You can create a new mailer with `Rails generate mailer`. This will give you the equivalent of a Model and a Controller for sending emails to your users.

### app/mailers/application_mailer.rb

See above.

## app/models

The “M” of MVC; a Model is a template for the data stored in your database. Generally, any table is considered a “Model”.  Common models may be  `User` ,  `Post`  or  `Comment` .  Note that these things are singular rather than plural, this is a reference to the prototypical nature of a model.  This is in contrast to Controllers why by convention are plural because Controllers are referencing multiple records.

### app/models/concerns

Concerns are modules - little nuggets of reusable code generally extracted from Models when they get too fat.  The Concerns folder is part of an internal Rails framework called ActiveSupport which makes modules a bit easier to manage.

For more info see the Rails [guides on concerns](https://api.rubyonrails.org/classes/ActiveSupport/Concern.html).

### app/models/application_record.rb

Application_record.rb inherits from `ActiveRecord::Base` all subsequent models in your app will inherit from `ApplicationRecord` , similar to how Application_controller makes the functionality of the `ActionController` available to all other Controllers.

## app/views

The last piece of the MVC pattern is Views. The Views folder contains everything the user will see in their browser, mostly in the form of HTML with embedded Ruby (ERB) or .Haml which is a templating language for Ruby. New controllers will most likely have an associated view folder with the same name (unless you’re creating an API).  Generally speaking, every method in the Controller will have an associated View.

### app/views/layouts

Your new Rails app will have a Layouts folder with **application.html.erb**, **mailer.html.erb** and **mailer.text.erb** these set global layouts for the Rails app in various domains such as the browser and the inbox.  You may wish to add other components of a layout into this folder, for example, a **_header.html.erb** but most of your views will be organized into View folders specific to their Controller. **Application.html.erb** is the main template for your app, this file creates the main HTML `<head>` and `<body>` tags for your application with the views themselves shown in `<%= yield %>` . Yield is just a bit of Ruby code that adds the appropriate view for the page the user is looking at. Having an **Application.html.erb** file keeps your code DRY since you don’t have to repeatedly declare a doctype, head elements or include scripts and stylesheets, for every page in the View. Rails and the Asset Pipeline take care of this for you. The three files in this folder as stated above are:

* app/views/layouts/application.html.erb
* app/views/layouts/mailer.html.erb
* app/views/layouts/mailer.text.erb

# bin folder

The bin folder helps set up the Rails application so it and associated commands can run properly.

## bin/bundle

Ensures that the Gem Bundler works properly.

## bin/rails

Spring is a preloader which keeps Rails running in the background as you work (there are some cases where you need to restart the server but for the most part changes to the Views or Controllers will be loaded automatically and immediately into your app running in a development environment).  This file loads spring when you start the Rails application.

## bin/rake

Rake stands for Ruby Make and is used to run several commands that will both set up and update the server.

## bin/setup

Lets you write commands that will run when your app is first started.

## bin/spring

Allows Spring to run without using the Bundler to bundle all your gems, this lets spring quickly reload your pages in development whenever you make a change.

## bin/webpack

As discussed above Rails uses Webpack for bundling some JavaScripts as opposed to the AssetPipeline, this file requires the necessary setup and then runs Webpack.

## bin/webpack-dev-server

Allows you to customize the dev server of Webpack which you may wish to do if you don’t want some or all of your assets bundled in your development environment.

## bin/yarn

Yarn is a JavaScript package manager similar to NPM.  You can use either with Rails projects.

# config

Config, much like the name implies contains files for setting up your Rails application in different environments; development and test.

## config/environments

This folder lets you configure how your application will work in development, production and testing environments. For example, you may wish to ensure that your action_mail is configured to send emails through a mail service in production but not in development.

## config/initializers

This folder allows you to set granular initializers to define how your Rails app will preform there is a good chance you won’t spend too much time in here especially when working on your first few Rails applications.

### config/initializers/application_controller_renderer.rb

Allows controllers to render outside their scope. For more information see: [Upgrading to Ruby on Rails 5.0 from Rails 4.2 - application use case - Running with Ruby](https://mensfeld.pl/2015/12/upgrading-to-ruby-on-rails-5-0-from-rails-4-2-application-use-case/)

### config/initializers/assets.rb

Relates to the Asset Pipeline; which, you’ll remember, serves pages in your Rails app with the specific assets (CSS, JS, etc) they need. Here, you can add assets to the load path such as node_modules.

### config/initializers/ backtrace_silencers.rb

Backtraces are a debugging tool that allows you to see what’s going on in your Rails app, particularly useful when things blow up and you can pinpoint the specific area of failure. Configure what backtraces show by determining which libraries are allowed to show backtraces in this file.

### config/initializers/content_security_policy.rb

From Mozilla: “The HTTP _Content-Security-Policy_ response header allows web site administrators to control resources the user agent is allowed to load for a given page. With a few exceptions, policies mostly involve specifying server origins and script endpoints.“ [Content-Security-Policy - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy). In essence, this controls the data that is allowed to flow into your app and from what external sources. For example linking to external scripts, fonts or images outside of your app.

### config/initializers/cookies_serializer.rb

Determines the format for cookies, by default this is `:json`

### config/initializers/filter_parameter_logging.rb

We’ll discuss logging below but there are some parameters (accepted user inputs) like passwords or sensitive user data that you don’t want to show up in your log, you can add them here. filter_paramiter_logging is sort of like .gitignore for parameters.

### config/initializers/inflections.rb

As discussed in the Model explanation, Rails has naming conventions for what is singular and plural. Based on locales (language settings for your app see Locales folder below) you can update these inflections in this initializer although it’s probably not a good idea unless it’s absolutely necessary.

### config/initializers/mime_types.rb

MIME types - Multipurpose Internet Mail Extensions specify the format of email attachments.  
[MIME - Wikipedia](https://en.wikipedia.org/wiki/MIME)

### config/initializers/wrap_parameters.rb

By default, Rails wraps all parameters into JSON but you can specify other formats using the `wrap_parameters` hash. [ActionController::ParamsWrapper](https://api.rubyonrails.org/classes/ActionController/ParamsWrapper.html)

## config/locales

Will generally load with en.yml as the only file. If your application is going to have multiple language options you can include all the translations as YML files here.

## config/webpack

```
Allows you to configure Webpack settings based on the environment. 

```

### config/webpack/development.js

### config/webpack/environment.js

### config/webpack/production.js

### config/webpack/test.js

### config/application.rb

Will run the boot.rb file if you are using Passenger.  It pulls all gems you’ve required in the gem file into your project and creates a class `Application` that inherits from `Rails::Application`

## config/boot.rb

Creates an environment variable `BUNDLE_GEMFILE` set to the location of your project’s gem file, this is how Rails will know where to pull in dependencies or Gems, of which there are about 2 dozen in an out-of-the-box Rails install.

## config/cable.yml

Similar to database.yml (see below) cable.yml sets development, test and production adapters for ActionCable, which you will remember is Rails way of implementing realtime features into your application.

## config/credentials.yml.enc

credentials.yml replaces secrets.yml as the location of secret keys. This file is encrypted so nobody can read your secret keys and is only decrypted by the master key (see below).

## config/database.yml

You can set a default database (to make your code a little DRYer) as well as specific DBs for development, test, and production.

## config/environment.rb

Initializing the Rails application on the server requires a lot of steps, depending on if you’re using `rails server` or Passenger these steps may be slightly different but once environment.rb loads the application is initialized and begins running.

## config/master.key

Throw this into your .gitignore file right away (see below), this is the master key that decrypts credentials.yml.enc in Rails and nobody should have it. For more info you can read this brilliant article: [Rails 5.2 credentials – cedarcode – Medium](https://medium.com/cedarcode/rails-5-2-credentials-9b3324851336)

## config/puma.rb

Puma is a web server for Ruby and is the default web server for Rails’ development environment. You can configure Puma through this folder altering things like thread count and the default port that puma will listen for incoming requests on (default is 3000).

## config/routes.rb

Routes are the road map around your Controllers. Routes take incoming requests to the server and direct them to the correct Controller.  Unlike most other files in the config folder, you will spend a lot of time here setting up routes as you build your app.

## config/spring.rb

As discussed in the bin folder Spring is a preloader this file actually tells Spring which files and folders should trigger a restart.

## config/storage.yml

ActiveStorage is a framework introduced in Rails 5.2 for uploading and storing assets such as images. You need a place to put those things such as an AWS instance, you specify that location in this file.

## config/webpacker.yml

Allows you to add additional environments too Webpacker.

# db

## db/seeds

Seeds let you fill a database with data. Let’s say you wanted to see your pagination feature in action; you could create 11 posts by hand or you could just use a gem such as Faker to create 11 random posts for you and insert them directly into your database.

## lib

Lib is defined by Rails guides as “Extended modules for your application.” If this sounds vague you're not the only one who feels that way. What specifically goes in the lib folder is somewhat controversial: see [What goes in Rails lib/ – Extreme Programming – Medium](https://medium.com/extreme-programming/what-goes-in-rails-lib-92c74dfd955e) and [What code goes in the lib/ directory?](https://codeclimate.com/blog/what-code-goes-in-the-lib-directory/) but the general consensus is that lib should be reserved for code that does not fit into the app folder, that could be easily extracted out for use in other applications. It has two subfolders assets and tasks

## lib/assets

From Ruby on Rails Guides: 

> "lib/assets is for your own libraries’ code that doesn’t really fit into the scope of the application or those libraries which are shared across applications."

## lib/tasks

You can write custom `rake` tasks and put them in this folder.  It's not a very commonly used location.

# log

Logging is an important way to see how your application is performing and for finding and troubleshooting issues. By default, this folder will be empty. You can initialize various loggers in the config/environments folder with a command like: `config.log_level = :info` from there as you’re run your application the Log file will be created.  For more detailed info see this great article from Datadog: [How to collect, customize, and manage Rails application logs](https://www.datadoghq.com/blog/managing-rails-application-logs/)

Included in the Log folder:

* log/development.log

# node_modules

Any node packages you are using in your project (such as Webpack and Babel) will be dependant on dozens if not hundreds of other node packages. A package manager such as NPM or Yarn will manage these packages for you. You shouldn’t go into this folder or edit anything in it.

# public

The public folder contains resources that are external and may be accessed outside the normal structure of your application, favicon, apple-touch-icons, robots.txt and of course error pages. Pages like: 404, 422 and 500. Should the application in production experience some kind of error these HTML pages will be served automatically bypassing routes, controllers or any specific views. These pages are not part of the Rails Asset Pipeline so you will need to write any styles inline.

## public/robots.txt

Allows you to specify how search engines crawl your website.

# storage

Rails 5.2 introduced ActiveStorage which replaced gems like PaperClip and allows Rails to directly interface with cloud services like AWS or Google

# test

Rails has testing built-in from the ground up! The default test suite in Rails is MiniTest so you will find that all these folders are ready to go with MiniTest.  
There are folders where you can test specific Controllers, Helpers, Models, Mailers as well as write Integration tests which work across multiple Controllers and recreate something akin to actual user experience. For more on what a constitutes a controller test vs an integration test I recommend this article from ([Jason Swett](https://www.codewithjason.com/difference-integration-tests-controller-tests-rails/))

## test/channels

#### test/channels/application_cable/connection_test.rb

Tests for ActionCable connections like all ActionCable stuff you will only need this if you are using channels in your application.

## test/controllers

You can test your controllers here, these tests are generally looking at how well your controller goes between the model and the view, they are larger in scope then Model tests but smaller in scope then Integration tests.

## test/fixtures

Not a place for writing tests but generating dummy test data. Inside the fixtures folder you can add any number of YML files with predefined data. You can pull this data into your tests to make sure that your models are working correctly and interacting with the application as expected.

### test/fixtures/files

Now that Rails has file handling built-in with ActiveStorage not only can you test data from models you can also test files.

## test/helpers

You can write specific tests for the helpers you have in app/helpers. Testing helpers is not too common but you can do it if a helper is overly complex or seems brittle.

## test/integration

Integration tests allow you to test interactions between controllers and provide a testing option closer to the actual user experience.

## test/mailers

You can even write tests for your mailers, to ensure emails are being sent correctly and formatted properly.

## test/models

One of the most granular tests; you can ensure that a record is saved properly, the database has updated, etc.

## test/system

System tests are a way of testing your application in a real browser generating screenshots to show you how everything looks in action.  System tests will also test the JavaScript, not that you should use MiniTest system tests as a replacement for a good JavaScript testing library like Jest. System tests; however, will allow you to see how your JavaScript is functioning in the browser.

## test/application_system_test_case.rb

This file holds the defaults for your system tests, you can change browsers, drivers or screen resolution.

## test/test_helper.rb

Test helper brings in external data and libraries that are required for tests. You will notice that right off the bat `fixtures :all` is imported. This gives your tests access to fixtures. You could set up a host of other test suites and frameworks from test_helper.rb to include their functions and DSLs such as Capybara, FactoryBot and Faker.

# tmp

Temporary - this folder contains caches and sessions it may be cleared on occasion either manually or on deploy (depending on how you are deploying your app).

# vendor

The vendor folder is a place for 3rd party code somewhat like Gems. Gems; however, are a bit more self-contained whereas the vendor folder may contain specific scripts not bundled as gems.  For more on this as well as some of the benefits see [How to Vendor Gem a Gem](http://fuzzyblog.io/blog/ruby/2014/08/22/how-to-vendor-gem-a-gem.html).

# .browserslistrc

Browserslist is a tool to target specific browser versions for NPM tools such as Babel. Set to “defaults” by default, ensures that

# .gitignore

As with any other project, your version control will ignore any files or folders you specify in here.

# .ruby-version

Simply contains the version of Ruby the project is working under, RVM can read this file and set the correct version of ruby on your computer (if you have multiple versions of Ruby installed).

# babel.config.js

Babel is a JavaScript compiler that lets you use the latest and greatest features of JavaScript and compiles them to be compatible with web browsers that may not yet have adopted those features. For more information on Babel configuration see their [official docs.](https://babeljs.io/docs/en/)

# config.ru

Rack (the popular Ruby server) uses this file to start the application.

# gemfile

Inside the gemfile you store all your application’s dependencies, as you have seen the Rails New command installs a lot of gems but as you add more functionality to your application you’ll be hopping in and out of this file a lot.

# gemfile.lock

Similar to package-lock.json for Node projects, this file is updated when you run `bundle install` or `bundle update` and resolves all gem dependencies above and beyond what you included manually in the gem file. Don’t mess with this file it’s updated automatically.

# package.json

Establishes NPM dependencies for Javascript modules, these will be packed with Webpacker.

# postscss.config.js

PostCSS gives you a lot of modern functionality with CSS, from automatically adding vendor prefixes to including CSS Modules. For more on this cool tool check it out.

# rakefile

Again Rake stands for “Ruby Make”. Rails has several commands built in which require Rake such as `rake routes` (showing you all routes for your application) `rake db:migrate` to add new Models and columns to your db. Among others, you can add custom rake commands here.

# README.md

This is the Readme for your project, it will be displayed on your projects Github page, include any information you believe would be useful for others investigating or working with your project.

# yarn.lock

Much like package.json, Yarn is Webpacker default package manager. This is a lock file, so like Gemfile.lock it will be updated automatically and you should not change it manually.

You made it through! Congratulations!

<iframe src="https://giphy.com/embed/LVWQ9iBwkpLmU" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/reactiongifs-LVWQ9iBwkpLmU">via GIPHY</a></p>


---

# Additional Resources

Helpers([The Beginner’s Guide to Rails Helpers - Mix & Go](https://mixandgo.com/learn/the-beginners-guide-to-rails-helpers))  
Info on Keep Files ([StackOverflow keep files](https://stackoverflow.com/questions/29183372/rails-why-is-there-keep-file-in-every-directory))  
Rails Initialization ([The Rails Initialization Process — Ruby on Rails Guides](https://guides.rubyonrails.org/initialization.html))  
Creating the Blog Application([Getting Started with Rails — Ruby on Rails Guides](https://guides.rubyonrails.org/getting_started.html#creating-the-blog-application))

---

I realize that's pretty overwhelming but let me simplify it a bit. 99% of Rails is there to let you customize your project to the nth degree this is why Rails continues to work well for large enterprises and startups alike; you can easily adjust and tweak almost any part of your application with very little effort. That said, for most beginners, personal projects and even a decent amount of corporate projects you will use very little of this functionality.

 Since Models, Views, and Controllers represent the core of a Rails application you will be spending most of your development time in the app folder. You will use the routes.rb file a fair amount in the config folder while you set up how users will step through your app and as you add new Controller actions. Be sure to always write proper test coverage for your applications. If you are, you will spend a lot of time in the test folder. The gemfile is one final place you will visit often adding and updating gems as needed.

Although there are a ton of files and folders created in every new `rails new` you shouldn’t be overwhelmed by it; if you ever get lost this post has your back.

# 

