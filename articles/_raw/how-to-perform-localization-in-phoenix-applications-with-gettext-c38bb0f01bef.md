---
title: How to perform localization in Phoenix applications with Gettext
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-27T06:46:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-localization-in-phoenix-applications-with-gettext-c38bb0f01bef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9FLnNCwPgLPZBvQ4pfwnzg.jpeg
tags:
- name: localization
  slug: localization
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: translation
  slug: translation
seo_title: null
seo_desc: 'By Anastasia

  In my previous tutorial, we discussed how to introduce support for I18n into Rails
  apps. Today we will continue covering back-end frameworks and talk about localization
  of Phoenix applications with the help of Gettext.

  You might not have...'
---

By Anastasia

In my previous tutorial, we discussed [how to introduce support for I18n into Rails apps](https://blog.lokalise.co/rails-i18n/). Today we will continue covering back-end frameworks and talk about _localization of Phoenix applications_ with the help of _Gettext_.

You might not have heard about [Phoenix](http://phoenixframework.org/) before, so let me say a couple of words about it. This is a server-side MVC framework written in [Elixir](https://elixir-lang.org/), which is a functional programming language working on [Erlang virtual machine](https://en.wikipedia.org/wiki/BEAM_(Erlang_virtual_machine)). The framework itself is quite young but still it is very promising thanks to Erlang’s and Elixir’s features. It is very fast, scalable, and concurrency-oriented which is really important for heavily loaded applications.

[Gettext](https://www.gnu.org/software/gettext/manual/gettext.html#Why), in turn, is an I18n tool maintained by GNU which may be used for web, desktop applications, and even in operating systems.

Throughout this article we will be localizing a Phoenix demo project and will see Gettext in action. Also, we will discuss how to introduce support for locale switching and persisting user preferences throughout the requests. Before proceeding to the main part of the tutorial, you also might want to learn common recommendations [which are listed in our recent article](https://blog.lokalise.co/localization-5-focus-points/).

### Hello, Gettext!

Alright, let’s dive straight into the code and observe the localization of Phoenix applications in practice. Create a new project without a default DBMS and change directory into the project:

```
mix phx.new lokalise_demo --no-ecto cd lokalise_demo
```

It appears that Phoenix has support for Gettext out of the box: you don’t need to install any third-party libraries. Moreover, if you navigate to the `demo/lib/demo_web/templates/page/index.html.eex` file, you’ll notice the following line of code:

```
<h2><%= gettext "Welcome to %{name}!", name: "Phoenix" %></h2>
```

What is going on here? Well, `gettext` [is a function](https://hexdocs.pm/gettext/Gettext.html#gettext/2) that tries to load translation for the string `"Welcome to %{name}!"`. `%{name}` here is a [placeholder that will be replaced](https://hexdocs.pm/gettext/Gettext.html#module-interpolation) with a `"Phoenix"` string as dictated by the second argument `name: "Phoenix"` (this argument contains so-called _bindings_).

By default, Phoenix applications have English as the default locale set, and no other locales are supported. However, you may easily change that by adding a new line to the `config/config.exs` file:

```
config :lokalise_demo, LokaliseDemoWeb.Gettext, locales: ~w(en ru)
```

Now we are supporting both English and Russian locales.

The next step is to provide translations for the string passed to the `gettext` function inside the `index.html.eex` file. The simplest way to do that is by extracting all translation strings into separate files automatically:

```
mix gettext.extract mix gettext.merge priv/gettext mix gettext.merge priv/gettext --locale ru
```

These commands are going to create three new files inside the `priv/gettext` folder. Therefore, let’s stop for a second and talk a bit more about these files.

### Gettext File Types

The first command above, `mix gettext.extract`, searches for all Gettext messages that require translation and places them into the `priv/gettext/default.pot` file. POT means “portable object template”, and such files serve as templates for language-specific translations. Our `default.pot` has the following contents:

```
## This file is a PO Template file. ## ## msgid here are often extracted from source code. ## Add new translations manually only if they're dynamic ## translations that can't be statically extracted. ## ## Run mix gettext.extract to bring this file up to ## date. Leave msgstr empty as changing them here as no ## effect: edit them in PO (.po) files instead. msgid "" msgstr "" #, elixir-format #: lib/lokalise_demo_web/templates/page/index.html.eex:2 msgid "Welcome to %{name}!" msgstr ""
```

The template conveniently shows the lines where the extracted messages are located. `msgid` is the string to translate (some developers may refer to it as a “key”). `msgstr` is, of course, the actual translation.

The name of the POT file — `default` — is also a [_domain name_](https://hexdocs.pm/gettext/Gettext.html#module-domains) which serves as a namespace. Initially, there is only one namespace, but for larger sites with hundreds of translations it may be a good idea to create multiple domains and, consequently, separate translations into different files.

The `mix gettext.merge priv/gettext --locale LOCALE_CODE_HERE` command creates [translation files](https://hexdocs.pm/gettext/Gettext.html#module-translations) for the given language based on the template. These translation files have `.po` extension (“portable object”) and live inside the `priv/gettext/LOCALE_CODE_HERE/LC_MESSAGES` folder. Remember that in order to provide translations for the messages, you should edit these PO files, not the templates directly!

### Gettext Domains

As already mentioned above, Gettext supports multiple domains or namespaces. When you are utilizing the `gettext/4` function, you always assume a `default` domain. If you would like to employ a different namespace, use the `[dgettext/6](https://hexdocs.pm/gettext/Gettext.html#dngettext/6)` [function](https://hexdocs.pm/gettext/Gettext.html#dngettext/6) instead which accepts the domain, the message, optional bindings, and some other arguments:

```
<%= dgettext "custom_domain", "message is ${placeholder}", placeholder: "my binding" %>
```

Now the `mix gettext.extract` command is going to create a new `custom_domain.pot` file. Similarly, running `mix gettext.merge` creates a `custom_domain.po` file based on the template.

Note once again that for smaller sites, using multiple domains is usually an overkill. Still, their usage for large resources is very much recommended because this way you don’t end up with hundreds of translations in a single file. Another reason is the ability to have the same translation keys under different namespaces.

### Providing Translations

So, having discussed some Gettext internals, we can now translate the `Welcome to %{name}!` string into Russian (this message is already in English, so of course no translation is needed for this language). Modify the `priv/gettext/ru/LC_MESSAGES/default.po` file like this:

```
# ... some other stuff goes here ... #, elixir-format #: lib/lokalise_demo_web/templates/page/index.html.eex:2 msgid "Welcome to %{name}!" msgstr "Вас приветствует %{name}"
```

This is it! Currently we do not have any mechanism to switch the language, so set Russian as a [default locale](https://hexdocs.pm/gettext/Gettext.html#module-default-locale):

```
# config/config.exs config :lokalise_demo, LokaliseDemoWeb.Gettext, locales: ~w(en ru), default_locale: "ru" # <== modify this line
```

Now start the server by running:

```
mix phx.server
```

Open `http://localhost:4000` page in your browser and make sure that the translated message is shown!

### Gettext Pluralization

Another important feature that I would like to cover is the [pluralization](https://hexdocs.pm/gettext/Gettext.html#module-pluralization). Different languages have different pluralization rules, and Gettext supports many of them out of the box. Still, it is our job to provide proper translations for all potential cases.

As a very simple example, let’s say how many apples the user has. Suppose we don’t know the exact amount, which means that the sentence may read as “1 apple” or “X apples”. To support pluralization, we have to stick with the `[ngettext/5](https://hexdocs.pm/gettext/Gettext.html#ngettext/5)` [function](https://hexdocs.pm/gettext/Gettext.html#ngettext/5):

```
ngettext "You have 1 apple", "You have %{count} apples", 2
```

This function accepts both singular and plural forms of the sentence, as well as the `count`. Under the hood, Gettext takes this count and chooses the proper translation based on the pluralization rules.

Next you may update the POT and PO files with the following commands:

```
mix gettext.extract --merge priv/gettext mix gettext.extract --merge priv/gettext --locale=ru
```

You’ll find a couple of new lines inside the Gettext files:

```
msgid "You have 1 apple" msgid_plural "You have %{count} apples" msgstr[0] "" msgstr[1] ""
```

`msgstr[0]` and `msgstr[1]` contain translations for singular and plural forms respectively. For English we don’t need to do anything else, but the Russian language requires some extra steps:

```
msgid "You have one message" msgid_plural "You have %{count} messages" msgstr[0] "У вас одно яблоко" msgstr[1] "У вас %{count} яблока" msgstr[2] "У вас %{count} яблок"
```

The pluralization rules in this case are a bit more complex, therefore we must provide not two, but three possible options. You may find more information on the topic [in the official docs](https://hexdocs.pm/gettext/Gettext.Plural.html).

### Choosing The App’s Locale

As I already mentioned earlier, currently there is no way to actually switch between locales when browsing the app. This is an important feature, so let’s add it now!

All in all, we have two potential solutions:

* Utilize a third-party solution, for example the [set_locale](https://github.com/smeevil/set_locale) plug (the easy way)
* Write everything from scratch (the warrior’s way)

If you choose to stick with the third-party plug, things will be very simple indeed. You need to perform [only three quick steps](https://github.com/smeevil/set_locale#setup):

1. Install the package
2. Add a new plug to the `router.ex` file
3. Add a new `:locale` routing scope

After that the [locale will be inferred](https://github.com/smeevil/set_locale#fallback-chain-and-precedence) from the URL, cookies, or the `accept-language` request header. Simple.

However, in this tutorial I propose choosing a more complex way and writing this feature from scratch.

### Reading Locale From the URL

The most common way of specifying the desired locale is via the URL. The language’s code may be a part of the domain name, or a part of the path:

* `[http://en.example.com/some/path](http://en.example.com/some/path)`
* `[http://example.com/en/some/path](http://example.com/en/some/path)`
* `[http://example.com/some/path?locale=en](http://example.com/some/path?locale=en)`

Let’s stick with the latter option and provide the locale as a GET parameter. To read the locale’s value and do something about it, we need a [custom plug](https://hexdocs.pm/phoenix/plug.html#module-plugs). Create a new `lib/lokalise_demo_web/plugs/set_locale_plug.ex` file with the following contents:

```
defmodule LokaliseDemoWeb.Plugs.SetLocale do import Plug.Conn # 1 @supported_locales Gettext.known_locales(LokaliseDemoWeb.Gettext) # 2 def init(_options), do: nil # 3 def call(%Plug.Conn{params: %{"locale" => locale}} = conn, _options) when locale in @supported_locales do # 4 end def call(conn, _options), do: conn # 5 end
```

Let’s discuss this code snippet:

1. On this line we are importing a behavior. It requires us to fulfill a certain contract (see below).
2. This is the module attribute with a list of supported locales
3. This is the actual fulfillment of the contract: a callback that gets invoked automatically. It may return options passed to the `call/2` function, or just `nil`
4. The `call/2` is initialized with all the GET parameters of the request. We are only interested in the `locale` part and fetch it using the pattern matching mechanism. Also on this line we have a guard clause that ensures the chosen language is actually supported
5. This is the fallback clause that gets invoked when the passed locale is unsupported. In this case we just return the connection without any modifications.

The last thing we need to do is flesh out the first clause of the `call/2` function. It simply has to set the chosen locale as the current one:

```
def call(%Plug.Conn{params: %{"locale" => locale}} = conn, _options) when locale in @supported_locales do LokaliseDemoWeb.Gettext |> Gettext.put_locale(locale) conn end
```

Note that the `conn` must be returned by the `call/2` function!

The plug is ready, and you may place it inside the `:browser` pipeline:

```
# lib/router.ex # ... pipeline :browser do plug :accepts, ["html"] plug :fetch_session plug :fetch_flash plug :protect_from_forgery plug :put_secure_browser_headers plug LokaliseDemoWeb.Plugs.SetLocale end
```

Now reload the server and navigate to `http://localhost:4000/?locale=en`. The welcoming message should be in English which means that the custom plug is working as expected!

### Storing Locale Into a Cookie

Our next task is persisting the chosen locale among requests so that the user does not need to provide it every time. The perfect candidate for such persistence would be cookies: small text files stored on the user’s PC. Phoenix indeed has support for cookies out of the box, so just utilize a `[put_resp_cookies/4](https://hexdocs.pm/plug/Plug.Conn.html#put_resp_cookie/4)` [function](https://hexdocs.pm/plug/Plug.Conn.html#put_resp_cookie/4) inside your plug:

```
def call(%Plug.Conn{params: %{"locale" => locale}} = conn, _options) when locale in @supported_locales do LokaliseDemoWeb.Gettext |> Gettext.put_locale(locale) conn |> put_resp_cookie "locale", locale, max_age: 365*24*60*60 end
```

We modify the connection by storing a cookie named `"locale"`. It has a lifetime of 1 year which effectively means eternity in terms of the web.

The last step here is reading the chosen locale from the cookie. Unfortunately, we cannot use a guard clause for this task anymore, so let’s replace two clauses of the `call/2` function with only one:

```
def call(conn, _options) do case fetch_locale_from(conn) do nil -> conn locale -> LokaliseDemoWeb.Gettext |> Gettext.put_locale(locale) conn |> put_resp_cookie "locale", locale, max_age: 365*24*60*60 end end
```

All in all, the logic remains the same: we fetch the locale, check it, and then either do nothing or store it as the current one.

Add two private functions to finalize this feature:

```
defp fetch_locale_from(conn) do (conn.params["locale"] || conn.cookies["locale"]) |> check_locale end defp check_locale(locale) when locale in @supported_locales, do: locale defp check_locale(_), do: nil
```

Here we are reading the locale from the either the GET param or cookie, and then checking if the desired language is supported. Then either return this language’s code, or just `nil`. Great job!

Another pretty common way of setting the locale is by using the `Accept-Language` HTTP header. If you would like to implement this mechanism, try utilizing [the code from the set_locale plug](https://github.com/smeevil/set_locale/blob/fd35624e25d79d61e70742e42ade955e5ff857b8/lib/headers.ex) that already provides all the necessary RegExs and other fancy stuff.

### Locale Switcher Control

So, the `SetLocale` plug is ready, but we still have not provided any controls to choose the website’s language. Therefore, let’s render two links at the top of the page. Define a new helper inside the `lib/views/layout_view.ex` file:

```
defmodule LokaliseDemoWeb.LayoutView do use LokaliseDemoWeb, :view def new_locale(conn, locale, language_title) do "<a href=\"#{page_path(conn, :index, locale: locale)}\">#{language_title}</a>" |> raw end end
```

Call this helper from the `templates/layout/app.html.eex` template:

```
<body> <div class="container"> <header class="header"> <%= new_locale @conn, :en, "English" %> <%= new_locale @conn, :ru, "Russian" %> </header> <!-- other stuff --> </div> </body>
```

Reload the page and try switching between locales. Everything should be working just fine, which means that the task is completed!

### Simplify Your Life With Lokalise

By now you are probably thinking that supporting multiple languages on a big website is probably a pain. And, honestly, you are right. Of course, the translations can be namespaced with the help of domains. But still you must make sure that all the keys are translated for each and every locale. Luckily, there is a solution to this problem: the Lokalise platform that [makes working with the localization files much simpler](https://lokalise.co/features). Let me guide you through the initial setup which is nothing complex really.

* To get started, [grab your free trial](https://lokalise.co/signup)
* Create a new project, give it some name, and set English as a base language
* Click “Upload Language Files”
* Upload PO files for all your languages
* Proceed to the project, and edit your translations as needed
* You may also contact professional translator to do the job for you
* Next simply download your PO files back and replace them inside the `priv/gettext` folder
* Profit!

Lokalise has many more features including support for dozens of platforms and formats, and even the possibility to upload screenshots in order to read texts from them. So, stick with Lokalise and make your life easier!

### Conclusion

In today’s tutorial we have seen how to perform localization of Phoenix applications with the help of Gettext. We have discussed what Gettext is and what goodies it has to offer. We have seen how to extract translations, generate templates, and create PO files based on these templates. You have also learned what domains are, and how to introduce support for pluralization. On top of that, we have successfully created our custom plug to fetch and persist the chosen locale based on the user’s preferences. Not bad for one article!

To learn more about Phoenix I18n, I encourage you to check out [the official guide](https://hexdocs.pm/gettext/Gettext.html) that provides both general explanations, as well as documentation for individual functions. To learn about the Gettext and its features in more detail, refer to the [GNU’s documentation](https://www.gnu.org/software/gettext/manual/gettext.html). And, of course, if you have any questions feel free to post them in the comments!

_Originally published at [blog.lokalise.co](https://blog.lokalise.co/localization-of-phoenix-applications/) on September 27, 2018._

