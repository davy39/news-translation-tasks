---
title: Essential Gems for Rails Applications
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T22:30:05.000Z'
originalURL: https://freecodecamp.org/news/cjn-essential-gems-for-rails-applications-75fed43d2798
coverImage: https://cdn-media-1.freecodecamp.org/images/0*cw0oHjOoBMDeba6_.jpg
tags:
- name: Apps
  slug: apps-tag
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Clark Jason Ngo

  Gems are located in the Gemfile inside your project folder. Let’s have a look at
  some you’ll want to have.

  will_paginate

  Adds pagination to your app

  Installation

  Add to Gemfile

  gem ''will_paginate''

  Install

  bundle install

  Usage

  In a ...'
---

By Clark Jason Ngo

Gems are located in the Gemfile inside your project folder. Let’s have a look at some you’ll want to have.

### **will_paginate**

**Adds pagination to your app**

#### **Installation**

Add to `Gemfile`

```
gem 'will_paginate'
```

Install

```
bundle install
```

**Usage**

In a .html.erb file, render page links in the view:

```erb
<%= will_paginate @places %>
  <% @places.each do |place| %>
    <h1><%= place.name %></h1>
    <br />
  <% end %>
<%= will_paginate @places %>
```

In your controller, you can define how many entries per page you want to display. In the example below, it will list 3 entries per page.

```ruby
def index
  @places = Place.all.paginate(page: params[:page], per_page: 3)
end
```

Source: [https://github.com/mislav/will_paginate](https://github.com/mislav/will_paginate)

### **simple_form**

**Forms made easy!**

#### **Installation**

Add to `Gemfile`

```
gem 'simple_form'
```

Install

```
bundle install
```

Run the generator

```
rails generate simple_form:install
```

**Usage**

In a `.html.erb` file:

```ruby
<%= simple_form_for @place do |f| %>
  <%= f.input :name %>
  <%= f.input :address %>
  <%= f.input :description %>
  <br />
  <%= f.submit 'Create', class: 'btn btn-primary' %>
<% end %>
```

Source: [https://github.com/plataformatec/simple_form](https://github.com/plataformatec/simple_form)

### **devise**

**Adds user management**

#### **Installation**

Add to `Gemfile`

```ruby
gem 'devise'
```

Install

```ruby
bundle install
```

Run the generator

```ruby
rails generate devise:install
```

Configure device at _config/environments/development.rb_

Add this line:

```ruby
config.action_mailer.default_url_options = { host: 'localhost', port: 3000 } 
```

Edit code in _app/views/layouts/application.html.erb_

Add this line:

```ruby
<% if notice %>
  <p class="alert alert-success"><%= notice %></p>
<% end %>
<% if alert %>
  <p class="alert alert-danger"><%= alert %></p>
<% end %>
```

Add sign-up and login links in _app/views/layouts/application.html.erb_

```ruby
<p class="navbar-text pull-right">
<% if user_signed_in? %>
  Logged in as <strong><%= current_user.email %></strong>.
  <%= link_to 'Edit profile', edit_user_registration_path, :class => 'navbar-link' %> |
  <%= link_to "Logout", destroy_user_session_path, method: :delete, :class => 'navbar-link'  %>
<% else %>
  <%= link_to "Sign up", new_user_registration_path, :class => 'navbar-link'  %> |
  <%= link_to "Login", new_user_session_path, :class => 'navbar-link'  %>
<% end %>
</p>
```

Force user to be redirected to login page if not logged in.

Edit in _app/controllers/application_controller.rb_

```ruby
before_action :authenticate_user!
```

Source: [https://guides.railsgirls.com/devise](https://guides.railsgirls.com/devise)

### **geocoder**

**Adds geocoding from Google API**

#### **Installation**

Add to `Gemfile`

```ruby
gem 'geocoder'
```

Install

```
bundle install
```

Create a migration file, run this in your terminal:

```
rails generate migration AddLatitudeAndLongitudeToModel latitude:float longitude:float
```

```
rake db:migrate
```

Example of a migration file adding latitude and longitude columns for existing Places table:

```ruby
class AlterPlacesAddLatAndLng < ActiveRecord::Migration[5.0]
  def change
    add_column :places, :latitude, :float
    add_column :places, :longitude, :float
  end
end
```

Add these lines in your `app/model/place.rb`

```ruby
geocoded_by :address
after_validation :geocode
```

Add this script in _`show.html.erb`_

```js
<script>
<% if @place.latitude.present? && @place.longitude.present? %>
  function initMap() {
  var myLatLng = {lat: <%= @place.latitude %>, lng: <%= @place.longitude %>};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: myLatLng
  });
  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}
</script>
```

Source: [https://www.rubydoc.info/gems/geocoder/1.3.7](https://www.rubydoc.info/gems/geocoder/1.3.7)

### **figaro**

**Easily configure your APIs in Heroku deployment**

#### **Installation**

Add to `Gemfile`

```
gem 'figaro'
```

Install and create a commented `config/application.yml` file and add it to your `.gitignore`

```
bundle exec figaro install
```

Update your API keys in `config/application.yml`

For updating API keys in heroku, go to your terminal:

```
figaro heroku:set -e productionheroku restart
```

Source: [https://github.com/laserlemon/figaro](https://github.com/laserlemon/figaro)

### carrierwave

**image uploader**

#### **Installation**

Add to `Gemfile`

```
gem 'carrierwave'
```

Install

```
bundle install
```

In your terminal

```
rails generate uploader Image
```

It will generate this:

```
app/uploaders/image_uploader.rb
```

Create a migration file

```
rails g migration add_image_to_courses image:string
```

Run the migration file

```
rake db:migrate
```

In your model

```ruby
class User < ApplicationRecord  mount_uploader :image, ImageUploaderend
```

Add to a `html.erb` i.e. `app/views/instructor/courses/new.html.erb`

```ruby
<%= f.input :image %>
```

Add to controller `app/controllers/instructor/courses_controller.rb`

```ruby
params.require(:course).permit(:title, :description, :cost, :image)
```

Add to `show.html.erb` i.e. `app/views/instructor/courses/show.html.erb`

```ruby
<%= image_tag @course.image, class: 'img-fluid' %>
```

Also update the following:

* `app/views/courses/show.html.erb`
* `app/views/courses/index.html.erb`
* `app/views/instructor/courses/show.html.erb`

#### **Image Resolution with ImageMagick, more on carrierwave**

Carrierwave in shows that `MiniMagick` and `RMagick` can be used

It shows here `app/uploaders/image_uploader.rb`

```ruby
class ImageUploader < CarrierWave::Uploader::Base
  # Include RMagick or MiniMagick support:
  # include CarrierWave::RMagick
  # include CarrierWave::MiniMagick
```

#### **Installing ImageMagick**

We need to update our development environment’s database of programs to make sure when we install a program we’re getting the latest version.

```
$ sudo apt-get update
```

Install ImageMagick

```
$ sudo apt-get install imagemagick
```

Installation MiniMagick

Add to `Gemfile`

```
gem 'mini_magick'
```

Install

```
bundle install
```

Uncomment MiniMagick in `app/uploaders/image_uploader.rb`

```ruby
class ImageUploader < CarrierWave::Uploader::Base
  # Include RMagick or MiniMagick support:
  # include CarrierWave::RMagick
  include CarrierWave::MiniMagick
```

That line gives CarrierWave the ability to reach out to the ImageMagick program we installed on our program, through the MiniMagick gem. This will allow us to resize the image.

Unlocks image-resizing abilities such as `resize_to_fill`, `resize_to_fit`, `resize_and_pad`, and `resize_to_limit`.

Add this in `app/uploaders/image_uploader.rb`

```ruby
# Process files as they are uploaded:
process resize_to_fill: [800, 350]
```

### Integrating Amazon S3 for Video Uploads

#### **Installation**

Add this line to your application’s `Gemfile`:

```
gem 'carrierwave-aws'
```

Run the bundle command from your shell to install it:

```
bundle install
```

#### Step 1: Configuring the Initializer

Normally we would install our gem first, however to prevent bugs when switching from fog to AWS we need to update our initializer first.

You can read the details of how to configure the carrierwave-aws gem [in the Usage Section of the Documentation](https://github.com/sorentwo/carrierwave-aws#usage). Following the pattern they specify, we should update `config/initializers/carrierwave.rb` to look like this:

```ruby
# config/initializers/carrierwave.rb
CarrierWave.configure do |config|
  config.storage    = :aws
  config.aws_bucket = ENV["AWS_BUCKET"]
  config.aws_acl    = "public-read"
  config.aws_credentials = {
      access_key_id:     ENV["AWS_ACCESS_KEY"],
      secret_access_key: ENV["AWS_SECRET_KEY"],
      region:            ENV["AWS_REGION"]
  }
end
```

Now save the file.

#### Step 2: Updating our Gemfile

Add the `carrierwave-aws` gem as [described by the documentation](https://github.com/sorentwo/carrierwave-aws#installation). Edit the `Gemfile` to look like this:

```
gem 'carrierwave'gem 'mini_magick'gem 'carrierwave-aws'
```

Save the file and run the command to install the gem.

```
$ bundle install
```

Then restart your server.

#### Step 3: Add Region to application.yml

We need to add a region to our `application.yml` file. Open up your `config/application.yml` and add this line to specify the region we want to use:

```
# config/application.yml
AWS_ACCESS_KEY: "Your-access-key"
AWS_SECRET_KEY: "Your-secret-key"
AWS_BUCKET:     "Your-bucket"
AWS_REGION:     "us-east-1"
```

Save the file.

#### Step 4: Updating the Uploader

If you remember from before, we specified inside the storage provider for the uploader to use `:fog`. Rather than that, we need to switch it to `:aws`.

```ruby
# encoding: utf-8
class ImageUploader < CarrierWave::Uploader::Base
  # Include RMagick or MiniMagick support:
  # include CarrierWave::RMagick
  include CarrierWave::MiniMagick
  # Choose what kind of storage to use for this uploader:
  #storage :file
  storage :aws
  # A bunch more comments down here....
end
```

Save the file.

One more thing we will have to do is re-sync the localhost with heroku. To do this we need to run a simple command:

```
$ figaro heroku:set -e production
```

Make sure uploads continue to work by uploading an image for a course and make sure it goes through successfully.

### **VideoJS**

Add css file before `</head>`

```js
<link href="http://vjs.zencdn.net/5.12.6/video-js.css" rel="stylesheet">
```

Add JavaScript files before `</body>`

```
<script src="http://vjs.zencdn.net/5.12.6/video.js"></script>
```

```js
<script src="http://vjs.zencdn.net/ie8/1.1.2/videojs-ie8.min.js"></script>
```

Note: You must place the videoJS `script` tags in the bottom of the body otherwise you will have issues loading the video player because of Turbolinks.

Thanks for reading! Hope this was helpful.

