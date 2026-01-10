---
title: How to Scale Elm Views with Master View Types
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2019-07-18T07:29:29.000Z'
originalURL: https://freecodecamp.org/news/scaling-elm-views-with-master-view-types
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/2014-Haute-Route-Imperiale51.JPG
tags:
- name: ELM
  slug: elm
- name: scaling
  slug: scaling
seo_title: null
seo_desc: 'A concept to help Elm Views scale as applications grow larger and more
  complicated.

  In Elm, there are a lot of great ways to scale the Model, and update, but there
  is more controversy around scaling the view. A lot of the debate is around Reusable
  Vi...'
---

A concept to help Elm Views scale as applications grow larger and more complicated.

In Elm, there are a lot of great ways to scale the `Model`, and `update`, but there is more controversy around scaling the `view`. A lot of the debate is around [Reusable Views versus Components](https://gist.github.com/rofrol/fd46e9570728193fddcc234094a0bd99#reusable-views-instead-of-nested-components). Components are not recommended, but a lot of people are still advocating for them.  This article presents an idea that hopefully strengthens the argument for Resuable Views.

In almost all cases, the scaling problem comes down to enforcing consistency, which usually means allowing child views to make some adjustments to the master view, while at the same time not allowing child views to make a mess.

I will be using Richard Feldman's excellent [Real World app](https://github.com/rtfeldman/elm-spa-example) (specifically written to demonstrate scaling in Elm) as an example, as it is contains a lot of current best practice techniques, it is well known (2000+ stars and 300+ forks) and Richard is a well known Elm expert. 

I will be suggesting some improvements to this code, so I want make a clear at this point that I mean no disrespect by this (I would bet large sums of money that he did it in about one tenth of the time it would have taken me!). You could also argue that the problems are small and not worth fixing. Ultimately, this decision is yours, but by the end of the article I hope to persuade you that there are problems, and that they are fixable if you think it is worthwhile.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/ski-touring.jpeg)

## Master view functions with conditionals

One option is to define a master view function. This function takes care of shared concerns, like the header bar and overall layout. Then it calls child view functions depending on the current view and / or has parameters to control child specific behaviour.

This works, but can quickly lead to:

* An explosion of parameters, potentially forcing your child views to return a lot of things they don't care about.
* A mixing of responsibilities between master and child views.
* Extra code and duplication.

In the Real World App, a parameter of type `Page` is passed to the master view so that it can render a navbar link as active. There is a [large case statement](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page.elm#L113) that uses this parameter to work out what which link is active, and it would be a lot easier for the child just to specify this.

The [line below](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Main.elm#L85) shows the master view passing `Page.Home`, which has to match up with `Home.view home`. This is easy to get wrong, there is no help from the compiler or type system, and really it is the responsibility of the child view the specify this.

`viewPage Page.Home GotHomeMsg (Home.view home)`

There is some duplication when [creating the NavBarLink Html](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page.elm#L62), and the `linkTo` function will accept any Html, although only very particular Html is valid.

## Convention and trust

Another possibility is for child views to be responsible for keeping shared elements consistent, by convention and trust. 

Arguably this also happens in the Real World App. The [Home](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page/Home.elm#L146), [Article](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page/Article.elm#L119) and [Profile](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page/Profile.elm#L197) views all have the concept of a banner. The banner is different in each view, but presumably is meant to be a consistent and recognisable visual element (essentially, it's the title / header for the view). The views don't share any code for these banners, and as a result of this they are not the same size or colour. You could theoretically try and enforce a convention using tests, but it would be difficult, and probably not worthwhile.

## Helper functions

Another possibility is for child views to be responsible for keeping shared elements consistent, but by using some helper functions. This is definitely a step forward, and is probably the most common solution I see in the wild. The functions can go in the same file and be next to each other. This makes it easier to see that they are related and are representing the same visual element, and easier to make them consistent. 

However, there are still some drawbacks. The main one is that the child views have to know to use the helper functions, and there is nothing enforcing this. This isn't a huge deal when you only have one shared element and one function to call, but as applications get bigger, you end up with a combinatorial explosion of differences in the shared visual elements. Most people tame this by providing a number of small, focused functions for the various differences. Then the child view has to know about all these functions, and how to compose them, and there no help from the compiler. 

Again, this arguably occurs in the Real World App: for example in [this part of the Profile.view function](https://github.com/rtfeldman/elm-spa-example/blob/b5064c6ef0fde3395a7299f238acf68f93e71d03/src/Page/Profile.elm#L211), which needs to know how to use the `viewTabs`, `Feed.viewArticles` and `Feed.viewPagination` helper functions, and what Html they need to be contained in.

## Scaling with Master View Types

In order to overcome these problems, I propose using a `Type` to define your site structure (I rather pompously call this a "Master View Type"). Child views then return this type, and the master view takes it as a parameter and returns the html. 

For the Real World App examples we have been looking at, the Master View Type is below (`Viewer` is the person viewing the page in the Real World App). You could arguably have more general banner types here, such as AvatarBanner, or even IconBanner (instead of ViewerBanner) depending on your domain.

```elm
type alias Page =
    {   activeNavBarLink: NavBarLink
		, banner: Banner
        , body: Html Msg
    }
	
type Banner =
    TextBanner TextBannerProperties
    | ViewerBanner Viewer
    | ArticleBanner Viewer ArticlePreview

type NavBarLink =
    NavBarLink NavBarLinkProperties

```

To demonstrate this, I have create a repository with just the [Header and Banner parts of the Real World App](https://github.com/ceddlyburge/elm-without-master-view-types)  and then created a new repository after refactoring to use a  [Master Page Type](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/Page.elm), [NavBarLink Type](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/NavBarLink.elm) and [Banner Type](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/Banner.elm). You can peruse the code to get a feel for how it works.

To my mind, using a Master Page Type has the following benefits:

* Writing the master view code is easier
* Writing the child view code is easier
* Communication and understanding are improved, as UI concepts now have names
* Theming / redesigning a site is a lot easier
* Elm packages can provide UI templates

The master view can precisely define what it will accept / support via the types, with [union types](https://guide.elm-lang.org/types/custom_types.html) and [opaque types](https://medium.com/@ckoster22/advanced-types-in-elm-opaque-types-ec5ec3b84ed2). Non supported combinations can be made unrepresentable or uncreatable. 

In my example repository the [NavBarLink type is opaque](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/NavBarLink.elm), so it is only possible to create supported NavBarLinks (`home`, `article` and `viewer`). In a similar way [Banner is a union type](https://github.com/ceddlyburge/elm-master-view-types/blob/master/src/Banner.elm), which means that only supported variants can be represented. 

It would be possible for a programmer to simply change these files, but a proficient programmer would recognise the patterns and follow them. If this isn't enough and you are feeling paranoid, then you can require stricter code review on such files, potentially taking advantage of [CODEOWNERS](https://help.github.com/en/articles/about-code-owners) functionality on GitHub and GitLab. In the extreme you can  provide the modules via an elm package, and restrict push access to the underlying repository.

Child views don't have to do anything more than create an instance of the types. The helper functions all return types, so it's easy to see which functions can be used in a particular context, and is impossible to use functions in the wrong context. For example, if a function returns a `HeaderBarLink`, it is impossible to mistakenly use this function to create a link in the `FooterBar`, or elsewhere on the page. Child views can also leave some of the complexity to the master view. For example, the child view can define a list of options to choose from, and the master view can render this using buttons, a drop down list or an autocomplete list, depending on the number of options. 

The master page type also provides names for UI concepts, which can then be discussed. For example, a designer could say "Let's move the NavBarLinks to the left hand side", and everybody would know what they meant. A product owner could say "Let's create a new page with an IconBanner, and we'll use the current weather api for the icon" and again, everybody would know what they mean. You can look at this [excellent thoughtworks article](https://www.thoughtworks.com/insights/blog/ui-components-design) for more details of this.

Since the responsibility for turning the Master View Type in to html is all in the same place, it is easy to make drastic changes to the look and feel of a website, and to do theming. These changes and themes can alter the Css _and the Html_, which is something that the normal theming techniques just can't do. Pragmatically, your Master View Type will often have a `body: Html Msg` property (to allow child views complete flexibility on the child specific parts of the page) so there would still be some sprawling code to fix up, but it will definitely be a lot easier.

Finally, it opens up possibility of providing ready made themes and site layouts as packages. This would allow you to just do the following to get a working app, complete with layout and styling:

* `create-elm-app`
* `elm install elm-bootstrap-starter-template`
* Write some code to create the Master Page Type
* `elm-app start`

Companies could create packages like these to ensure a consistent look and feel across their applications. Open source designs and layouts could emerge and become commonplace, similar to the way that Bootstrap has revolutionised html and css design. Developers with limited design skills (like me) could concentrate on the the bits they are best at (the logic), but still produce produce elegant websites using these packages.

To demonstrate this I have created a [bootstrap starter master view package](https://package.elm-lang.org/packages/ceddlyburge/elm-bootstrap-starter-master-view/latest/). It mimics the layout and design of the [bootstrap starter template](https://getbootstrap.com/docs/4.0/examples/starter-template/). I have then used this package in a demo elm application. You can [browse the demo application](https://elm-bootstrap-starter.netlify.com/) to see how it looks, and [view the source](https://github.com/ceddlyburge/elm-bootstrap-starter-demo) to see how it works.

All these advantages come at a small to negative cost. There is a little more code for the new types, but some duplication is removed. You can view the source of the Real World App repositories [from before](https://github.com/ceddlyburge/elm-without-master-view-types) and [after refactoring to use a Master Page Type](https://github.com/ceddlyburge/elm-master-view-types) for the full details.

## Conclusions

Master View Types bring a lot of benefits (view code is easier to write and maintain, UI concepts are named and UI packages are possible) for little or no cost. They should improve the code of any Elm application that has issues around enforcing consistency (while allowing flexibility) in their view code, which in my experience is most medium and large applications.

