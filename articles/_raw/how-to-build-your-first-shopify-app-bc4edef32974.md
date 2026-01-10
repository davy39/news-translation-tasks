---
title: How to build your first Shopify app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-01T19:25:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-first-shopify-app-bc4edef32974
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5rTl2RMivof-SHDDYPsN6A.jpeg
tags:
- name: ecommerce
  slug: ecommerce
- name: React
  slug: react
- name: Ruby on Rails
  slug: ruby-on-rails
- name: shopify
  slug: shopify
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Igor Petrov

  Why build a Shopify App?

  I have always been excited about how the e-commerce market is growing, and have
  made various attempts to dive into this world. About five years ago, a partner and
  I built an e-commerce website selling and deliv...'
---

By Igor Petrov

### Why build a Shopify App?

I have always been excited about how the e-commerce market is growing, and have made various attempts to dive into this world. About five years ago, a partner and I built an e-commerce website selling and delivering flowers, a soft toy, and a greeting card packaged together as a gift. This was an idea validation attempt, and we didn’t take it seriously. So it ended soon.

Later, we tried to sell floor tiles (partnering with a guy who had worked in that area for several years) and it didn’t go well, either. Mostly, the reason was the same: it was a side project for us, and we knew nothing about the floor tile market.

But, during this time, we developed a lot of e-commerce websites for our agency’s clients. Most of these websites were built using **Ruby on Rails** and specifically **Spree**. And this direction was successful — we learned a lot about e-commerce website development and typical development problems (as well as marketing, shipping, and different business problems).

This year I’m working with a new partner who had good experience with the **Shopify** platform. We talked a lot and came up to an idea of developing a [**Shopify** app](https://apps.shopify.com/influencify). This platform is growing fast, and there’s a big demand on the market for extending platform possibilities.

Building a product, rather than doing custom development for someone, was exciting for me, too. So these two things — e-commerce and product development — have naturally combined into the idea of a [**Shopify** app](https://apps.shopify.com/influencify).

### Understanding app building complexity

So you’ve come up with an idea for your application. Now you need to decide if your app will interact with merchants’ storefronts by extending templates or injecting some scripts. Or maybe you need to work with some third-party API and integrate it into your app, or extend a **Shopify** Admin.

Each part can be complex enough. So if you just need to do something with **Shopify** store data and output something in the Admin section, you are dealing with 1 type or 1 point of complexity. If you need to work with external APIs and still have some section in Admin, you have 2 points of complexity. And so on.

### Start development with a boilerplate

Well, we can see that our app is quite complex (though for customers it looks like an easy one). Since we agreed on app idea and initial **MVP**, I started to research and found that **Shopify** has a great `shopify_app` **Ruby** gem.

This is a pretty cool stuff that saves you a lot of time: it generates for you a **Shopify** app framework without the need to setup **OAuth** flow manually. Other things to note:

* Generated Shop model
* Simple Webhooks and ScriptTags registering
* Authentication approaches
* App Proxy verification (for your storefront customizations)

I’ve launched a blank app in minutes, not hours.

### Use recommended tools

Next, I have researched how to approach Admin UI in your app. I found out that **Shopify** simplifies this task for you as well with the power of their design framework [**Shopify Polaris**](https://polaris.shopify.com/).

[**Polaris**](https://polaris.shopify.com/) is a **React.js** components library, and this is the recommended way for extending the **Shopify** Admin section. Your app will look like a native **Shopify** app with admin sections like “Products” or “Orders” (**Shopify** uses it too, I guess).

You should use it instead of some custom theme, because it’s well documented, supported, and has guidelines.

### Extending Shopify Admin

After a successful installation of **Shopify Polaris** into the project with the help of **Webpacker** or **Yarn,** you’ll be able to extend the **Shopify** Admin section.

For the welcome page (one that merchants will see after app installation with no data set up yet), then you’ll do these things:

* Add a route:

```
get ‘/welcome’ => ‘home#index’
```

* Create a **Rails** controller:

```
class HomeController < BaseAuthenticatedController def index endend
```

* Add a view template that just renders **React** component with the help of `react-rails` gem:

```
# home/index.html.erb<%= react_component("Welcome", {  apiKey: ShopifyApp.configuration.api_key,  shopOrigin: "https://#{ @shop_session&.url }",  debug: Rails.env.development?,  forceRedirect: !Rails.env.development? && !Rails.env.test?}) %>
```

* Create a **React** component that renders some **Shopify Polaris** components (like `EmptyState`, for example).

The first step is quite clear for everyone who’s ever worked with **Ruby on Rails**. The second step should be as well, except the fact that you need to inherit your admin controllers from `ShopifyApp::AuthenticatedController` so every request will be authorized. I’ve created a subclass of this class for all future admin controller classes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2BYWJpAZHNIzSgtICBCQFA.png)

The third step is about rendering. I’ve installed the `react-rails` gem which comes with a nifty `react_component` helper, and I’ve added a rendering of a welcome component passing all necessary properties. For Embedded Apps (those that extend **Shopify** Admin) you should pass at least `apiKey` and `shopOrigin` options to utilize [embedded components](https://polaris.shopify.com/components/get-started#using-embedded-components) coming with **Shopify Polaris**. These [embedded components](https://polaris.shopify.com/components/get-started#using-embedded-components) are just **React** wrappers around the **Shopify** Embedded App SDK.

And finally, I’ve written a `Welcome` component and placed it into the `app/javascript/components` folder according to `config/webpacker.yml`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HL9JrMwbbqMo_i81DxJmMw.png)

Note that I’ve extracted some boilerplate, like the definition of `shopOrigin` and `apiKey` properties, into the `BasePage` component which is going to be a parent component for each app page. `InfluencifyApp` is a component that renders the Polaris `AppProvider` component, `Page`, inside it, and any children with `{this.props.children}` inside the `Page`.

With this setup, I’ve created other components with `InfluencifyApp` as a root component for each app page.

### Storefront customization

There’s a good option in **Shopify** that allows you to customize a merchant’s storefronts: Script Tags. They are JavaScript files that will be injected into the storefront template.

You can register them easily using the `shopify_app` gem. Here is how I’ve registered a script for [Influencify](https://apps.shopify.com/influencify) app (at `config/initializers/shopify_app.rb`):

```
# to include asset_url helperinclude ActionView::Helpers::AssetUrlHelper...config.scripttags = [    {event: 'onload', src: -> (domain) { asset_url('influencify.js', host: ENV['APP_DOMAIN']) } }]
```

Note that your scripts should be publicly accessible for all merchants across any of your deployments. I mean in terms of Rails, you shouldn’t have a digest in your script’s filename like `influencify-dd432js....js` , but instead, put the compiled version into a `public` folder or upload to CDN.

The second option is that you can have entire pages or parts of pages served by your app. That is, in case you need to display something or fetch some data from your injected script, you can register which URLs for merchants will be served by your app. This feature is known as [Application Proxies](https://help.shopify.com/en/api/guides/application-proxies). Again, to implement this in your app is way easier with the help of the `shopify_app` gem — just follow their [guides](https://github.com/Shopify/shopify_app#app-proxy-controller-generator).

### Testing

Testing a **Shopify** app may be a little tricky, but it’s familiar for anyone who’s ever worked with third-party APIs and tested via tools like `localtunnel` or `ngrok`. So each time you’re going to test your app, just launch your favorite tunneling tool and update the “Whitelisted redirection URL(s)” field on your app settings page with a URL to your authentication callback that looks like this: `[https://myapp.localtunnel.me/auth/shopify/callback](https://myapp.localtunnel.me/auth/shopify/callback)`.

To test your App Proxies endpoints for storefront customizations, you need to update this URL setting as well under the “Extensions” section.

Of course, to test an app you also need a test development store.

### Deployment

There’s nothing special about deployment, since this is just a regular **Ruby on Rails** application. I’ve deployed my app to the **Heroku** platform with the **Puma** and **Sidekiq** processes specified via the Procfile.

Also, you need to set the environment variables that you are going to use in your app via `ENV['SOMETHING']`.

One more thing to notice is I’ve added a **Node.js** buildpack, because had issues with building via **Webpack**:

```
git:(master) heroku buildpacks     === influencify Buildpack URLs1. https://github.com/heroku/heroku-buildpack-ruby2. https://github.com/heroku/heroku-buildpack-nodejs
```

### Going further

Well, as you can see, building an app the way it’s recommended by **Shopify** includes many different steps, and it may turn out to be a complex task for a non-experienced developer.

Of course, building an app is only the tip of the iceberg. The next steps in a **Shopify** app building venture are making good promo materials, submitting it to the App Store, marketing, and customer support/development after it has been approved.

_If you liked this post, please click on_ ✋ _to spread the word._

