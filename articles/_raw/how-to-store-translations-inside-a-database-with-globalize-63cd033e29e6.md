---
title: How to store translations inside a database with Globalize
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-16T10:01:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-store-translations-inside-a-database-with-globalize-63cd033e29e6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m8n4yc-F8Ln4EcnbL3H-CQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Rails
  slug: rails
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: translation
  slug: translation
seo_title: null
seo_desc: 'By Anastasia

  In one of my previous articles, I talked about the process of internationalizing
  Rails applications. That article explained all I18n basics, but it was revolving
  around placing all translations inside YAML files. There is nothing wrong w...'
---

By Anastasia

In one of my previous articles, I talked about the process of [internationalizing Rails applications](https://blog.lokalise.co/rails-i18n/). That article explained all [I18n](https://guides.rubyonrails.org/i18n.html) basics, but it was revolving around placing all translations inside YAML files. There is nothing wrong with this approach, but unfortunately it does not always work.

Suppose your website has lots of user-generated content which should be adapted for different languages. I propose that you _store your translations inside the database._ Why will YAML files not work in this case?

* The content itself may be quite large and it would be inconvenient to store it inside a file
* The content is dynamic and users should be able to create translated versions themselves, without the help of the site’s developer

It appears that the I18n module [allows you to define a custom backend](https://guides.rubyonrails.org/i18n.html#using-different-backends) that, for instance, may be powered by ActiveRecord. Luckily, there is no need to craft your own solution as there is already an existing one: [Globalize](https://github.com/globalize/globalize). Globalize is a battle-tested library characterized as “Rails I18n de-facto standard library for ActiveRecord model/data translation.” With its help you can easily translate model attributes, scope them, introduce fallbacks, and so on.

So, in this article we are going to talk about Globalize and see it in action by creating a sample Rails application. Shall we start?

### Preparing the Application

Let’s get started by generating a new Rails app:

```
rails new GlobalizeSample
```

I’ll assume you are using _Rails 5.2.1_ for this demo but still the described concepts apply to earlier versions as well.

Let’s suppose we are building an [international online shop](https://www.shopify.com/plus) showcasing various products. These products will be added by the administrator, and so we can’t know what the content will be ahead of the game. This means that the traditional method of using YAML files to store translations won’t work. Our content manager will have access to the CMS only, and we would rather not give them access to the source code of the app (I shudder to think about it!).

But, fear not, in the next section we will overcome this problem easily. For now, however, let’s take care of the basics.

### Administering Products

Utilize code generator and create a new scaffold for the `Product`:

```
rails g scaffold Product title:string description:text
```

This should create a model, controller, routes, and views for the products. Don’t forget to run the migration:

```
rails db:migrate
```

Now start the server:

```
rails s
```

Visit the `http://localhost:3000/products` path and make sure that you are able to add, modify, and delete the products.

### Switching the Language

In order to see the Globalize library in action, we will need a way to switch the app’s locale. I won’t cover this process in detail (as we have a [separate article on the topic](https://blog.lokalise.co/rails-i18n/)) so let’s do it quickly.

First, add the list of supported locales to the `config/application.rb`:

```
# ... config.i18n.available_locales = [:en, :ru]
```

I will be supporting English and Russian, but you may choose any other languages.

Next, tweak the `config/routes.rb` and wrap the product resource with a scope. Also, while we are here, add a root route:

```
scope "(:locale)", locale: /#{I18n.available_locales.join("|")}/ do # <== add this resources :products root 'products#index' # <== add this end # <== add this
```

After that, modify the `application_controller.rb` file:

```
# ... before_action :set_locale private def set_locale I18n.locale = extract_locale || I18n.default_locale end def extract_locale parsed_locale = params[:locale] I18n.available_locales.map(&:to_s).include?(parsed_locale) ? parsed_locale : nil end def default_url_options { locale: I18n.locale } end
```

This code will set the locale on every request while making sure the chosen language is actually supported. Also, it will add a `locale` GET param to each link generated with the `link_to` helper.

Lastly, add two links to the application layout:

```
<!-- views/layouts/application.html.erb --> <ul> <li><%= link_to 'English', root_path(locale: :en) %></li> <li><%= link_to 'Русский', root_path(locale: :ru) %></li> </ul>
```

To ensure that this new feature works, add translation for the Products page title:

```
# config/locales/en.yml en: products: index: title: Our Products
```

```
# config/locales/ru.yml ru: products: index: title: Наши продукты
```

Now simply utilize these translations inside the `views/products/index.html.erb`:

```
<!-- ... --> <h1><%= t '.title' %></h1> <!-- ... -->
```

Note that we can take advantage of the “lazy lookup” because the translation keys were named in the proper way.

Translate other static content as necessary, then reload the server, and make sure that the locale can be properly switched. Great!

### Globalize, Globalize it Hard!

#### Defining Attributes For Translation

Okay, the ground work is done and we may proceed to the next part. Before Globalize can get into the game, it should be added to the `Gemfile`:

```
# ... gem 'globalize', git: 'https://github.com/globalize/globalize'
```

At the time of writing this article, the stable version was not yet compatible with Rails 5.2, so we have to install directly from the `master` branch. Also note that the latest stable does not support ActiveRecord 4.1 and below, therefore [refer to the documentation](https://github.com/globalize/globalize#installation) to learn which Globalize version to use for older AR.

Next, you have to decide which model attributes will be translated with Globalize. We are going to translate both `:title` and `:description` so list them in the model in the following way:

```
# models/products.rb # ... translates :title, :description
```

This will allow you to store store translations inside the database per locale. To make it work, however, you also need to create a special _translation table_.

#### Translation Table

So, if you are creating a new model and a migration, things are as simple as using a `create_translation_table!` method as [explained here](https://github.com/globalize/globalize#creating-translation-tables). Our case is a bit more complex, because we already have a `products` table with some data. Therefore it is required to move these data to the translation table. Start by generating a new migration:

```
rails g migration translate_products
```

Now flesh it out with the following code:

```
# db/migrate/xyz_translate_products.rb class TranslateProducts < ActiveRecord::Migration[5.2] def change reversible do |dir| # <=== 1 dir.up do Product.create_translation_table!({ # <=== 2 title: :string, # <=== 3 description: :text }, { migrate_data: true, # <=== 4 remove_source_columns: true # <=== 5 }) end dir.down do Product.drop_translation_table! migrate_data: true # <=== 6 end end end end
```

I’ve pinpointed the main things to note about this code:

1. This is going to be a reversible migration.
2. We are creating a translation table for the `Product`.
3. Carefully list all the fields that should be translated as well as their types. As you recall, these fields were passed to the `translates` method inside the model.
4. Don’t forget to provide the `migrate_data` option that should preserve your original database records.
5. `remove_source_columns` will ensure that the original columns (`:title` and `:description`) will be removed from the `products` table. You may also perform this step later in a separate migration.
6. That’s the action to perform when the migration is rolled back. Data should be preserved as well.

Run the migration:

```
rails db:migrate
```

After this command finishes its job, you will see a new `product_translations` table:

As you see, there is a `product_id` column that establishes relation to the product, and also a `locale` field to denote which language this translation is for. When you migrate your original data, it will be associated with the app’s default locale (which is English in our case). Override this behavior by using a `with_locale` method, for example:

```
I18n.with_locale(:ru) do Post.create_translation_table!(...) end
```

If you need to add more translated fields to the table later, utilize an `add_translation_fields!` method [as shown in this example](https://github.com/globalize/globalize#adding-additional-fields-to-the-translation-table). Also, don’t forget to define these new fields in the model.

#### Try It!

At this point Globalize is integrated into our application and ready to get rolling! Perform the following steps to see it in action:

* Reload your server and try to create a new product: its title and description will be provided for the currently set locale only (English in my case).
* Switch to Russian locale and make sure that both title and description are missing for the new product.
* Edit this product and enter values for the Russian version of the product.

As a result you should see two translations being stored inside the `product_translations` table:

Great job!

### Some More Globalize Features

#### Fallbacks

What happens if Globalize cannot find translated attributes for the given locale? As we’ve seen in the previous section, by default it will return blank values (which are actually `nil`s). However, it is possible to enable [I18n fallbacks](https://github.com/globalize/globalize#i18n-fallbacks-for-empty-translations) and display attribute values from another locale. To achieve that, just turn fallbacks on inside the `config/application.rb` file:

```
# ... config.i18n.fallbacks = true
```

Now when the translated attribute is `nil`, Globalize will try to load values from another locale. To make sure this feature is working, reload the server, create a new product, and then switch to another language. The title and description should fallback to another locale.

If you would like to employ fallbacks when the translation values are also blank (not `nil`), set the `fallbacks_for_empty_translations` option to `true`:

```
# models/product.rb # ... translates :title, :description, fallbacks_for_empty_translations: true
```

Also note that it is possible to define a custom fallback chain globally in the following way:

```
# somewhere in an initializer Globalize.fallbacks = {:en => [:de, :ru]}
```

#### Scope and Context

Globalize provides a special model scope called `with_translations` that can be used to load translation for a given language. In this example we are loading all translations for the English locale only:

```
Product.with_translations('en')
```

On top of that, it is possible to display translation for a desired locale in your views. To achieve that, use a `with_locale` method:

```
<% Globalize.with_locale(:en) do %> <!-- render your stuff here... --> <% end %>
```

#### Interpolation

What’s interesting is that Globalize even supports interpolation in the translated attributes. It works in the same way as interpolation in YAML translation files:

```
product.title = "Product for %{someone}" product.title someone: "John" # => "Product for John"
```

So, the placeholder here is `%{someone}`. To provide its value, simply pass a hash to the proper model attribute. Really convenient!

### Conclusion

In this section we have seen how to store translations inside database with the help of Globalize solution. We have discussed its basics, seen how to install and configure it, how to migrate data properly, how to define translations, provide fallbacks and utilize scopes. All in all, we have covered nearly everything Globalize has to offer, and so you may now apply these concepts into practice! Also don’t forget that Globalize can safely play with YAML files, so you can mix and match these approaches as you see fit.

Which solution do you utilize to internationalize user-generated content? Would you give Globalize a go? Share your thoughts in the comments section!

### Make Your Life Easier With Lokalise

Supporting multiple languages on a big website may become a serious pain. You must make sure that all the keys are translated for each and every locale. Luckily, there is a solution to this problem: the Lokalise platform that [makes working with the localization files much simpler](https://lokalise.co/features). Let me guide you through the initial setup which is nothing complex really.

* To get started, [grab your free trial](https://lokalise.co/signup)
* Create a new project, give it some name, and set English as a base language
* Click “Upload Language Files”
* Upload translation files for all your languages
* Proceed to the project, and edit your translations as needed
* You may also contact professional translator to do the job for you
* Next simply download your files back
* Profit!

Lokalise has many more features including support for dozens of platforms and formats, and even the possibility to upload screenshots in order to read texts from them. So, stick with Lokalise and make your life easier!

_Originally published at [blog.lokalise.co](https://blog.lokalise.co/store-translations-inside-database-globalize/) on November 16, 2018._

