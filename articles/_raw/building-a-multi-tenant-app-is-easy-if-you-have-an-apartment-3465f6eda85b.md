---
title: Building a multi-tenant app is easy…if you have an apartment!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T16:17:55.000Z'
originalURL: https://freecodecamp.org/news/building-a-multi-tenant-app-is-easy-if-you-have-an-apartment-3465f6eda85b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WXq8WqcR24xYG9PlOdwktw.jpeg
tags:
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: SaaS
  slug: saas
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Igor Petrov

  These days, more and more startups are appearing on the SaaS market. For their apps,
  they have several development approaches to choose from. And one of the technical
  models is the multi-tenancy or multi-tenant app. If you’re going to ...'
---

By Igor Petrov

These days, more and more startups are appearing on the _SaaS_ market. For their apps, they have several development approaches to choose from. And one of the technical models is the _multi-tenancy_ or _multi-tenant_ app. If you’re going to share all your software with your startup customers — either with the ability to have separate data/content and URLs (say, _SaaS_), or just part of it — you need a _multi-tenant_ app.

This is not the only choice: I should mention other approaches, but let’s just mention them — a comparison of different approaches could be a good topic for the next article.

Here is my list (ordered by implementation complexity):

* URL path-based _SaaS_. Easiest one. Single domain, single DB, etc. Application-level restrictions for data.
* Multi-tenant _SaaS_. Medium complexity. Subdomain-based or domain-based. Multiple databases or schemas. Database-level restrictions for data.
* Virtualization-based _SaaS_ (thanks to _Docker_ and friends!). High level of complexity. Subdomain/domain-based. Multiple apps and DB copies. Virtualization-level restrictions for data.

### Multi-tenancy

So what is _multi-tenancy_? _Multi-tenancy_ is a software development architecture approach in which each client gets their own app configuration and data (strictly or softly isolated from other clients). Each “instance” is called a “_tenant._”

Over the past few years, I’ve worked on several multi-tenant apps (I mostly did _multi-tenancy_ from scratch). And even now, I’m working on two _multi-tenant_ apps.

Let’s move on from the introduction and theory to the practice, and look at what could be used for _multi-tenant_ apps in the world of _Ruby on Rails_.

### Apartment

This is number one for _Ruby on Rails_ apps. Let’s add it to _Gemfile_:

```
gem ‘apartment’
```

After `bundle install` you need to run a generator so you’ll get some basic configuration templates:

```
bundle exec rails generate apartment:install
```

Now you have `config/initializers/apartment.rb` where you can tweak how you want to use _Apartment_. The most important things that should be configured are: how “_apartment_” will know how to identify your tenants for storing data (we’ll assume it’s a _PostgreSQL_ database where each _PostgreSQL_ schema is a separate tenant), and how to show data depending on _HTTP_ requests.

Ok, in one app I’m developing I have a `Website` _ActiveRecord_ model with `slug` field. Therefore, the first setting looks like this, and each website is a _tenant_:

```
config.tenant_names = lambda { Website.pluck(:slug) }
```

Let’s say I decided to treat any subdomain as the website’s slug. So if I have a `Website` with `my-awesome-website` slug, then `my-awesome-website.example.com` will serve data from `my-awesome-data` DB schema. To have this behavior we need:

```
# require 'apartment/elevators/subdomain'
```

```
...Rails.application.config.middleware.use Apartment::Elevators::Subdomain
```

The third setting you might need is excluding some models that should be shared across all _tenants_. Like `Website` itself from my example:

```
config.excluded_models = %w{ Customer Website Plan Feature PlanFeature }
```

### **Advanced tips**

#### Custom Elevator Class

Ok, we’ve built a subdomain-based _multi-tenant_ app, but what if we need a custom domains feature for our customers? But it still should be accessible from the subdomain as well. Then we need a custom elevator class — similar to what we’ve used above — `Apartment::Elevators::Subdomain` .

Elevator class should decide, based on the current request, what _tenant_ (database/schema) should be used. In case we have a `domain` field on the `Website` model:

![Image](https://cdn-media-1.freecodecamp.org/images/V8XTwU6cnTD4964hPCl0IOI0t1ANiMOx152I)

Here we’ve created a custom elevator class (in `lib/apartment/elevators/active_website.rb`) inherited from `Subdomain` elevator and overridden by `parse_tenant_name` that should return tenant name based on a request. So first we call `super` and save the result in `tenant` variable. If we have a website with the domain set up as a requested domain, we’ll return such a slug (_tenant_). Otherwise, we fall back to subdomain.

#### Not Found Page for incorrect tenants

Task #2: what if some non-existent tenant was requested? Someone makes a request to `no-such-tenant.example.com`, but we don’t have such a database schema. The best thing we could do is to respond with some 404 page. This task is not about `apartment` directly, but is closely related.

We’ll enhance our elevator class like this:

![Image](https://cdn-media-1.freecodecamp.org/images/zq3Kl4ZPYlbhj0SVRjyHgoPTsTx6ptXYNL8v)

What is `::NotFound` you may ask? This is a simple middleware that I use for this purpose. Placed in `app/middlewares` it’s written as below:

![Image](https://cdn-media-1.freecodecamp.org/images/3mHqiBZYHRzFTZWBcUbX02vDi0f-i9wNbBrK)

Task solved — client is happy!

#### Excluded Subdomains

If you need one or several subdomains to treat as a public _tenant_ (not a client’s) and not to switch on requests for it, you would use the `excluded_subdomains` option. This option is available for `Subdomain` elevator and its subclasses of course:

```
Apartment::Elevators::ActiveWebsite.excluded_subdomains = ['app']
```

#### Seeding data

If your _tenants_ are already created, you could initialize them with data using `db/seeds.rb`. With `rails db:seed` it will be applied to each tenant.

But what if you need to initialize a just-created _tenant_ (via `Apartment::Tenant.create`) with some data programmatically? Well, you could still do this by switching to _tenant_ and creating some models (or executing the _Rake_ task programmatically).

Look how `spree_shared` gem does this for popular `spree` gem (the code below is an updated version because `spree_shared` doesn’t work with the current _Spree_ version):

![Image](https://cdn-media-1.freecodecamp.org/images/MQ895qx1DCMfsbdtQD5JGI14gmnQZCCozCWe)

If you need seeds to be applied to each _tenant_, you might write it this way (again, a modified example from `spree_shared`):

![Image](https://cdn-media-1.freecodecamp.org/images/8iKqTff27RWVTIQqIQGZbq-blm0ItibiulKL)

#### Wrapping tenant creation into transaction

The next step is wrapping the _tenant_ creation into the transaction block, because we know that every _tenant_ has a corresponding database model (`Website` or `Customer` ), and we want to make sure both the model instance and the _tenant_ were created. This will make our app more transactional, and we won’t have a DB _tenant_ without the corresponding model instance or vice versa.

_Service Objects_ comes to the rescue! For our hosted websites app, we might write something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/XYHmkWvcrpBMdkIT-6rZ8a0wpnKUK-TPLU51)

We need to handle possible exceptions: if a record or _tenant_ wasn’t created for some reason.

### Conclusion

Well, as you may see, developing _multi-tenant_ apps is easy enough if you have good tools like the `apartment` gem. Let me know in the comments your cases of `apartment` appliance. Especially non-standard ones.

