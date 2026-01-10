---
title: How to Organize and Sync SVG Files with Iconset
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-09-08T15:47:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-organize-and-sync-svg-files-with-iconset
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/iconset.jpg
tags:
- name: Icons
  slug: icons
- name: Productivity
  slug: productivity
- name: SVG
  slug: svg
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "SVG is an awesome way to bring vector images into a design and development\
  \ workflow. But collecting and organizing SVG files on your computer can be challenging.\
  \ \nHow can Iconset help take away the pain and get us more productive?\n\nWhat\
  \ is SVG?\nWhat ..."
---

SVG is an awesome way to bring vector images into a design and development workflow. But collecting and organizing SVG files on your computer can be challenging. 

How can Iconset help take away the pain and get us more productive?

* [What is SVG?](#heading-what-is-svg)
* [What is Iconset?](#heading-what-is-iconset)
* [What are we going to learn?](#heading-what-are-we-going-to-learn)
* [Part 1: Getting started with Iconset](#heading-part-1-getting-started-with-iconset)
* [Part 2: Adding icons to Iconset](#heading-part-2-adding-icons-to-iconset)
* [Part 3: Using Iconset with design software like Figma](#heading-part-3-using-iconset-with-design-software-like-figma)
* [Part 4: Using Iconset in development like with React](#part-4-using-iconset-in-development-like-react)
* [Part 5: Syncing Iconset across multiple computers with Dropbox](#heading-part-5-syncing-iconset-across-multiple-computers-with-dropbox)

%[https://youtu.be/KXBf5l4rbL4]

## What is SVG?

[SVG](https://developer.mozilla.org/en-US/docs/Web/SVG) is a nearly 20 year old image file format. And while it’s been around for a while, it has only recently been gaining momentum in the development  community.

SVG is great for a number of reasons. First of all, it’s a vector format, meaning it scales as big or small as you want. 

But it’s also flexible in that you can use SVG right in your development project with a typically small file size and infinite scale. You can even [animate it](https://frontend.horse/issues/6/#slash)!

But trying to collect and organize a bunch of files can be challenging. What do you name them? Do you have a computer that can easily preview them? What about search?

## What is Iconset?

[Iconset](https://iconset.io/) is a free cross-platform tool that allows you to collect and manage all of your SVG files in one place.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-font-awesome.jpg)
_Iconset library_

Love to quickly move between [Font Awesome](https://fontawesome.com/) and [heroicons](https://heroicons.com/) but don’t want to keep switching libraries? You can use Iconset to make a quick search and drag it right into your project.

If you’re planning on using it for a [React](https://reactjs.org/) project, you can even copy the file as JSX and dump it right into your project!

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-copy-as.jpg)
_Iconset "Copy As"_

## What are we going to learn?

We’re going to walk through a few different scenarios that'll show us how Iconset is useful. 

We’re also going to walk through how you can easily manage Iconset between different computers or environments so you can have the same great library anywhere you work.

## Part 1: Getting started with Iconset

To get started, you’ll need to first install Iconset locally. It should be a similar installation process as any other application.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-no-icons.jpg)
_Iconset with no icons_

Once it’s ready and available locally, you should be able to open it up and see a UI with No Icons, which is expected, as it doesn’t come with any icons out of the box.

## Part 2: Adding icons to Iconset

Adding icons to Iconset is as easy as dragging in, but you have a few options during the process.

To get started, let’s download the free icon set [heroicons](https://heroicons.com/).

Download at: [https://heroicons.com/](https://heroicons.com/).

On the heroicons website, you should see a big Download all button, which will download a zip file including all of the files.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/download-heroicons.jpg)
_Downloading heroicons_

If you navigate to the optimized folder, you’ll see that there are two different versions: solid and outline.

Now to get these into Iconset, select each folder individually and drag it right into Iconset.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-drag-in-icons.gif)
_Dragging heroicons into Iconset_

Once there, you have a few options.

* **Set:** Since this is our first set, you’ll automatically be creating a new one. If you had existing sets, you could import into those sets.
* **Set Name:** Here we can name the set something that we’ll remember. For this, I recommend naming it “heroicons - Outline”.
* **Import Options:** these are optional settings, but I typically select the optimize and clean option to make sure any icons are immediately ready to get working with.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-heroicons.jpg)
_Iconset with heroicons set_

And once you click Import, it will do it’s thing, and you’ll now have your first set of icons in Iconset!

You can go ahead and do the same thing with the solid directory so then we’ll now have our two sets ready to go.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-heroicons-solid-outline.jpg)
_Iconset with Outling and Solid sets of heroicons_

At this point, you can use Iconset to search through your icons and see all of your files currently available in your collection.

## Part 3: Using Iconset with design software like Figma

The great thing about Iconset is how easy it is to use it with design software like [Figma](http://figma.com/).

If I wanted to add an envelope icon to my website so people could contact me, I could search for the mail icon, and simply drag it onto my canvas:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-drag-icon-into-figma.gif)
_Dragging mail icon into Figma_

I can then treat it like any other vector design element and immediately use it in my project.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/svg-icon-in-figma.jpg)
_SVG Mail icon in Figma_

## Part 4: Using Iconset in development like with React

Another cool thing is how easy it is to use in a project like React.

Out of the box, you get a few different ways you can copy the file and use it in development like copying it as JSX.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/nextjs-starter-sass.jpg)
_Next.js Sass Starter_

If I feel like my [Next.js Sass Starter](https://github.com/colbyfayock/next-sass-starter) could use some icons on the page, I can right-click any icon I want and under Copy As select JSX I can paste it right into my project!

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-copy-icon-as-jsx.gif)
_Copying icon from Iconset as JSX_

And while it will need some styling once you drop it in just like any other image or icon, it’s immediately ready to go.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/svg-icon-nextjs-project.jpg)
_Using icon JSX in Next.js React app_

## Part 5: Syncing Iconset across multiple computers with Dropbox

With Iconset, you have the ability to switch between different libraries. But importantly, you can also set the location of your library.

When Iconset creates your library, it stores everything as files and a database on your computer.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-location.jpg)
_Iconset library folder_

And inside the Iconset UI, we can both Move and Switch the location we use.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-settings.jpg)
_Iconset library settings_

If this is your first time setting up Iconset, you can start by clicking Move and then selecting the location you want to sync it to.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-move-location.jpg)
_Moving Iconset library location_

And once you click Move, it will move it to that directory, like a folder on Dropbox, and sync to the cloud like any other folder and file.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-sync-to-dropbox.jpg)
_Syncing Iconset library with Dropbox_

Alternatively, if you already have a shared Iconset library or if you’re setting this up on a new computer, you can use the Switch option, and select that option right from Dropbox.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-switch-locations.jpg)
_Switching Iconset location_

And once you hit Switch, you’ll now load up your shared library and be ready to get productive.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/iconset-full-library.jpg)
_Iconset with full library_

## What else can you do?

### Publish and share icon sets

Another cool feature is that you can export sets and share them. If you’ve spent a lot of time on a collection and want to share it with others, export it, publish it, and share it with the community!

### More organization

Iconset also supports features like Folders and Favorites. This makes it even easier to group and collect the icons however it makes sense to you to keep you productive.

It also supports tagging, making it even easier to search.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsor Me</a>
    </li>
  </ul>
</div>

