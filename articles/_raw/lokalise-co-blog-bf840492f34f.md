---
title: The Complete Guide to Rails Internationalization (i18n)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-23T11:17:13.000Z'
originalURL: https://freecodecamp.org/news/lokalise-co-blog-bf840492f34f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oNjw5BDpdjHzMGKwIyWmQA.jpeg
tags:
- name: internationalization
  slug: internationalization
- name: localization
  slug: localization
- name: Ruby on Rails
  slug: ruby-on-rails
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Anastasia

  In this article you are going to learn how to translate your Rails application into
  multiple languages, work with translations, localize datetime, and switch locales.
  We are going to see all these aspects in action by creating a sample a...'
---

By Anastasia

In this article you are going to learn how to translate your [Rails application](https://rubyonrails.org/) into multiple languages, work with translations, localize datetime, and switch locales. We are going to see all these aspects in action by creating a sample application and enhancing it step by step. By the end of the article you will have all the necessary knowledge to start implementing these concepts in real projects.

### Preparing your Rails App

So, as I already said, we are going to see all the concepts in action, therefore let’s create a new Rails application by running:

```
rails new SampleApp
```

For this tutorial I am using _Rails 5.2.1_, but most of the described concepts apply to older versions as well.

Now let’s generate a `StaticPagesController` which is going to have an `index` action (our main page):

```
rails g controller StaticPages index
```

Tweak the `views/static_pages/index.html.erb` view by adding some sample content:

```
<h1>Welcome!</h1> <p>We provide some fancy services to <em>good people</em>.</p>
```

Also I would like to add a Feedback page where our users will be able to share their opinion (hopefully, a positive one) about the company. Each feedback will have an author’s name and the actual message:

```
rails g scaffold Feedback author message
```

We will be interested only in two actions: `new` (which is going to render the form to post a review and also list all the existing reviews) and `create` (to actually validate and persist the reviews). Of course, ideally the reviews should be pre-moderated but we won’t bother with this today.

Tweak the `new` action to fetch all the reviews from the database and order them by creation date:

```
# feedbacks_controller.rb # ... def new @feedback = Feedback.new @feedbacks = Feedback.order created_at: :desc end
```

Also I would like to redirect the user to the Feedback page when the form is processed and the new record is persisted:

```
# feedbacks_controller.rb # ... def create @feedback = Feedback.new(feedback_params) if @feedback.save redirect_to new_feedback_path else @feedbacks = Feedback.order created_at: :desc render :new end end
```

Render the feedbacks collection on the `new` page:

```
<!-- views/feedbacks/new.html.erb --> <!-- other code goes here... --> <%= render @feedbacks %>
```

Lastly, create a partial for an individual feedback:

```
<!-- views/feedbacks/_feedback.html.erb --> <article> <em> <%= tag.time feedback.created_at, datetime: feedback.created_at %><br> Posted by <%= feedback.author %> </em> <p> <%= feedback.message %> </p> <hr> </article>
```

Take care of the routes:

```
# config/routes.rb Rails.application.routes.draw do resources :feedbacks root 'static_pages#index' end
```

Lastly add a global menu to the layout:

```
<!-- views/layouts/application.html.erb --> <!-- other code goes here... --> <nav> <ul> <li><%= link_to 'Home', root_path %></li> <li><%= link_to 'Feedback', new_feedback_path %></li> </ul> </nav>
```

Now run migrations and boot up the server:

```
rails db:migrate rails s
```

Navigate to the `http://locahost:3000` and make sure that everything is fine. Now that we have something to work with, let’s proceed to the main part and localize our application.

### A Bit of Configuration

Before performing translations, we need to decide which languages will be supported. You can choose any, but I will stick with Russian and English, with the latter set as a default. Reflect this inside the `config/application.rb` file:

```
# ... config.i18n.available_locales = [:en, :ru] config.i18n.default_locale = :en
```

Also hook up a [rails-i18n gem](https://github.com/svenfuchs/rails-i18n) that has locale data for [different languages](https://github.com/svenfuchs/rails-i18n#available-locales). For example, it has translated names of the months, pluralization rules, and other useful stuff.

```
# Gemfile # ... gem 'rails-i18n'
```

Just install this gem and you are good to go:

```
bundle install
```

### Storing Translations

Now that everything is configured, let’s take care of the home page and translate the text there.

The simplest way to do this is by utilizing [localized views](https://guides.rubyonrails.org/i18n.html#localized-views). All you need to do is create views named `index.LANG_CODE.html.erb`, where the `LANG_CODE` corresponds to one of the supported languages. So, in this demo we should created two views: `index.en.html.erb` and `index.ru.html.erb`. Inside just place content for English and Russian version of the site, and Rails will automatically pick the proper view based on the currently set locale. Convenient, eh?

This approach, however, is not always feasible. Another way would be to store your translated strings in a separate file, and render a proper version of the string based on the chosen language. By default, Rails employs [YAML files](https://en.wikipedia.org/wiki/YAML) that has to be stored under the `config/locales` directory. Translations for different languages are stored in separate files, and each file is named after this language.

Open the `config/locales` folder and note that there is already an `en.yml` file inside which has some sample data:

```
en: hello: "Hello world"
```

So, `en` is a top-level key representing the language that these translations are for. Next, there is a nested key-value pair, where `hello` is the _translation key_, and `Hello world` is the actual translated string. Let’s replace this pair with the following content:

```
en: welcome: "Welcome!"
```

This is just a welcoming message from our homepage. Now create a `ru.yml` file in the `config/locales` folder and provide translated welcoming message there as well:

```
ru: welcome: "Добро пожаловать!"
```

We have just created translation for our first string, which is really great.

### Performing Simple Translations

Now that we have populated the YAML files with some data, let’s see how to employ the translated strings in the views. Actually, it is as simple as utilizing the `translate` method which is aliased as `t`. This method has one required argument: the name of the translation key:

```
<!-- views/static_pages/index.html.erb --> <h1><%= t 'welcome' %></h1>
```

When the page is requested, Rails looks up the string that corresponds to the provided key, and renders it. If the requested translation cannot be found, Rails will just render the key on the screen (and turn it to a more human-readable form).

Translation keys can be named anything you like (well, nearly anything) but of course it is advised to give them some meaningful names so that you can understand what text they correspond to.

Let’s take care of the second message:

```
en: welcome: "Welcome!" services_html: "We provide some fancy services to <em>good people</em>."
```

```
ru: welcome: "Добро пожаловать!" services_html: "Мы предоставляем различные услуги для <em>хороших людей</em>."
```

Why do we need this `_html` postfix? Well, as you can see our string has some HTML markup, and by default Rails will render the `em` tag as plain text. As long as we don’t want this to happen, we mark the string as a “safe HTML”.

Now just use the `t` method again:

```
<!-- views/static_pages/index.html.erb --> <!-- ... ---> <p><%= t 'services_html' %></p>
```

### More On Translation Keys

Our homepage is now localized, but let’s stop for a moment and think about what we have done. All in all, our translation keys have meaningful names, but what happens if we are going to have, say, 500 messages in the app? This number is actually not that big, and large websites may have thousands of translations.

If all our key-values pairs are stored right under the `en` (or `ru`) key without any further grouping, this leads to two main problems:

* We need to make sure that all the keys have unique names. This becomes increasingly complex as your application grows.
* It is hard to locate all related translations (for example, translations for a single page or feature).

Therefore, it would be a good idea to further group your translations under arbitrary keys. For example, you may do something like this:

```
en: main_page: header: welcome: "Welcoming message goes here"
```

The level of nesting is not limited (but you should be reasonable about it), and the keys in different groups may have identical names.

It is beneficial, however, to follow the folder structure of your views (in a moment we will see why). Therefore, tweak the YAML files in the following way:

```
en: static_pages: index: welcome: "Welcome!" services_html: "We provide some fancy services to <em>good people</em>."
```

```
ru: static_pages: index: welcome: "Добро пожаловать!" services_html: "Мы предоставляем различные услуги для <em>хороших людей</em>."
```

Generally, you need to provide full path to the translation key when referencing it in the `t` method:

```
<!-- views/static_pages/index.html.erb --> <h1><%= t 'static_pages.index.welcome' %></h1> <p><%= t 'static_pages.index.services_html' %></p>
```

However, there is also a “lazy” lookup available. If you perform translation in a view or controller, and the translation keys are namespaced properly following the folder structure, you may omit the namespaces all together. This way, the above code turns to:

```
<!-- views/static_pages/index.html.erb --> <h1><%= t '.welcome' %></h1> <p><%= t '.services_html' %></p>
```

Note that the leading dot is required here.

Let’s also translate our global menu and namespace the translations properly:

```
en: global: menu: home: "Home" feedback: "Feedback"
```

```
ru: global: menu: home: "Главная" feedback: "Отзывы"
```

In this case we can’t take advantage of the lazy lookup, so provide the full path:

```
<!-- views/layouts/application.html.erb --> <!-- ... ---> <nav> <ul> <li><%= link_to t('global.menu.home'), root_path %></li> <li><%= link_to t('global.menu.feedback'), new_feedback_path %></li> </ul> </nav>
```

### Translating Models

Now let’s proceed to the Feedback page and take care of the form. The first thing we need to translate is the labels for the inputs. It appears that Rails allows us to provide translations for the model attributes, and they will be automatically utilized as needed. All you need to do is namespace these translations properly:

```
en: activerecord: attributes: feedback: author: "Your name" message: "Message"
```

```
ru: activerecord: attributes: feedback: author: "Ваше имя" message: "Сообщение"
```

The labels will now be translated automatically. As for the “submit” button, you can provide translation for model itself by saying:

```
en: activerecord: models: feedback: "Feedback"
```

But honestly I don’t like the “Create Feedback” text on this button, so let’s stick with a generic “Submit” word:

```
en: global: forms: submit: Submit
```

```
ru: global: forms: submit: Отправить
```

Now utilize this translation:

```
<!-- views/feedbacks/_form.html.erb --> <!-- ... ---> <%= form.submit t('global.forms.submit') %>
```

### Error Messages

Probably we do not want the visitors to post empty feedback messages, therefore provide some simple validation rules:

```
# models/feedback.rb # ... validates :author, presence: true validates :message, presence: true, length: {minimum: 5}
```

But what about the corresponding error messages? How do we translate them? It appears that we don’t need to do anything at all as rails-i18n gem already knows how to localize common errors. For example, [this file](https://github.com/svenfuchs/rails-i18n/blob/master/rails/locale/ru.yml#L133) contains error messages for the Russian locale. If you actually _do_ want to tweak the default error messages, then [check the official doc](https://guides.rubyonrails.org/i18n.html#error-message-scopes) that explains how to achieve that.

One problem with the form, however, is that the error messages subtitle (the one that says “_N_ errors prohibited this feedback from being saved:”) is not translated. Let’s fix it now and also talk about pluralization.

### Pluralization Rules

As long as potentially there can be one or more error messages, the “error” word in the subtitle should be pluralized accordingly. In English words are usually pluralized by adding an “s” postfix, but for Russian the rules are a bit more complex.

I already mentioned that the rails-i18n gem contains pluralization rules for all the supported languages, so we don’t need to bother writing them from scratch. All you need to do is provide the proper key for each possible case. So, for English there are only two possible cases: one error or many errors (of course, there can be no errors, but in this case the message won’t be displayed at all).

```
en: global: forms: submit: Submit messages: errors: one: "One error prohibited this feedback from being saved" other: "%{count} errors prohibited this feedback from being saved"
```

The `%{count}` here is interpolation – we take the passed value and place it right into the string.

Now take care of the Russian locale which has more possible cases:

```
ru: global: forms: submit: Отправить messages: errors: one: "Не удалось сохранить отзыв! Найдена одна ошибка:" few: "Не удалось сохранить отзыв! Найдены %{count} ошибки:" many: "Не удалось сохранить отзыв! Найдено %{count} ошибок:" other: "Не удалось сохранить отзыв! Найдена %{count} ошибка:"
```

Having this in place, just utilize these translation:

```
<!-- views/feedbacks/_form.html.erb --> <!-- ... ---> <%= form_with(model: feedback, local: true) do |form| %> <% if feedback.errors.any? %> <div id="error_explanation"> <h2><%= t 'global.forms.messages.errors', count: feedback.errors.count %></h2> <!-- errors... --> </ul> </div> <% end %> <!-- form fields --> <% end %>
```

Note that in this case we pass the translation key as well as the value for the `count` variable. Rails will take the proper translation variant based on this number. Also the value of the `count` will be interpolated into each `%{count}` placeholder.

Our next stop is the `_feedback.html.erb` partial. Here we need to localize two strings: “Posted by…” and datetime (`created_at` field). As for “Posted by…”, let’s just utilize the interpolation again:

```
en: global: feedback: posted_by: "Posted by %{author}"
```

```
ru: global: feedback: posted_by: "Автор: %{author}"
```

```
<!-- views/feedbacks/_feedback.html.erb --> <article> <em> <%= tag.time feedback.created_at, datetime: feedback.created_at %><br> <%= t 'global.feedback.posted_by', author: feedback.author %> </em> <p> <%= feedback.message %> </p> <hr> </article>
```

But what about the `created_at`? To take care of it, we can take advantage of the `localize` method aliased as just `l`. It is very similar to the Ruby’s `strftime`, but produces a translated version of the date (specifically, the months’ names are translated properly). Let’s use a [predefined format](https://github.com/svenfuchs/rails-i18n/blob/master/rails/locale/ru.yml#L265) called `:long`:

```
<!-- views/feedbacks/_feedback.html.erb --> <article> <em> <%= tag.time l(feedback.created_at, format: :long), datetime: feedback.created_at %><br> <%= t 'global.feedback.posted_by', author: feedback.author %> </em> <!--... --> </article>
```

If you would like to add your very own format, it is possible too [as explained here](https://guides.rubyonrails.org/i18n.html#adding-date-time-formats).

### Switching Between Locales

So, our app is now fully translated… but there is a very minor thing: we cannot change the locale! Come to think of it, this is quite a major issue really, so let’s fix it now.

There are a [handful of possible ways](https://guides.rubyonrails.org/i18n.html#managing-the-locale-across-requests) of setting and persisting the chosen locale across the requests. We are going to stick with the following approach:

* Our URLs will have an optional `:locale` parameter, and so they’ll look like `[http://localhost:3000/en/some_page](http://localhost:3000/en/some_page)`
* If this parameter is set and the specified locale is supported, we translate the app into the corresponding language
* If this parameter is not set or the locale is not supported, set a default locale

Sounds straightforward? Then let’s dive into the code!

First of all, tweak the `routes.rb` by including a `scope`:

```
# config/routes.rb scope "(:locale)", locale: /#{I18n.available_locales.join("|")}/ do # your routes here... end
```

Here we are validating the specified parameter using a RegEx to make sure that the locale is supported (note that the anchor characters like `\A` are not permitted here).

Next, set a `before_action` in the `ApplicationController` to check and set the locale on each request:

```
# application_controller.rb # ... before_action :set_locale private def set_locale I18n.locale = extract_locale || I18n.default_locale end def extract_locale parsed_locale = params[:locale] I18n.available_locales.map(&:to_s).include?(parsed_locale) ? parsed_locale : nil end
```

Also, in order to persist the chosen locale across the requests, set the `default_url_options`:

```
# application_controller.rb # ... private def default_url_options { locale: I18n.locale } end
```

The is going to include the `locale` parameter into every link generated with Rails helpers.

The last step is to present two links to switch between locales:

```
<!-- views/layouts/application.html.erb --> <!-- ... --> <nav> <ul> <li><%= link_to t('global.menu.home'), root_path %></li> <li><%= link_to t('global.menu.feedback'), new_feedback_path %></li> </ul> <ul> <li><%= link_to 'English', root_path(locale: :en) %></li> <li><%= link_to 'Русский', root_path(locale: :ru) %></li> </ul> </nav>
```

As an exercise, you may make these links more fancy and, for instance, redirect the user back to the page that he was browsing.

### Simplify Your Life With Lokalise

By now you are probably thinking that supporting multiple languages on a big website is probably a pain. And, honestly, you are right. Of course, the translations can be namespaced, and [even split into multiple YAML files](https://guides.rubyonrails.org/i18n.html#organization-of-locale-files) if needed, but still you must make sure that all the keys are translated for each and every locale.

Luckily, there is a solution to this problem: the Lokalise platform that [makes working with the localization files much simpler](https://lokalise.co/features). Let me guide you through the initial setup which is nothing complex really.

* To get started, [grab your free trial](https://lokalise.co/signup)
* [Install Lokalise CLI](https://docs.lokalise.co/api-and-cli/lokalise-cli-tool) that will be used to upload and download translation files
* Open your [personal profile page](https://lokalise.co/profile), navigate to the “API tokens” section, and generate a read/write token
* Create a new project, give it some name, and set English as a base language
* On the project page click the “More” button and choose “Settings”. On this page you should see the project ID
* Now from the command line simply run `lokalise --token <token> import <project_id> --lang_iso en --file config/lo`cales/en.yml while providing your generated token and project ID (on Windows you may also need to provide the full path to the file). This should upload English translation to Lokalise. Run the same command for the Russian locale.
* Navigate back to the project overview page. You should see all your translation keys and values there. Of course, it is possible to edit, delete them, as well as add new ones. Here you may also filter the keys and, for example, find the untraslated ones which is really convenient.
* After you are done editing the translations, download them back by running `lokalise --token <token> export <project_id> --type yaml --bundle_structure %LANG_ISO%.yml --unzip_to E:/Supreme/docs/work/lokalise/rails/SampleApp/con`fig/locales/. Great!

Lokalise has many more features including support for dozens of platforms and formats, ability to order translations from professionals, and even the possibility to upload screenshots in order to read texts from them. So, stick with Lokalise and make your life easier!

### Conclusion

In this article we have thoroughly discussed how to introduce internationalization support in Rails applications and implemented it ourselves. You have learned how and where to store translations, how to look them up, what are localized views, how to translate error messages and ActiveRecord-related stuff, as well as how to switch between locales and persist the chosen locale among the request. Not bad for today, eh?

Of course, it is impossible to cover all ins and outs of Rails I18n in one article, and so I recommend checking out [the official guide](https://guides.rubyonrails.org/i18n.html) that gives some more detailed information on the topic and provides useful examples.

_Originally published at [blog.lokalise.co](https://blog.lokalise.co/rails-i18n/) on August 23, 2018._

