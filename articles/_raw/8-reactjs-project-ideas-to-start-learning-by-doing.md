---
title: 8 React.js Project Ideas to Help You Start Learning by Doing
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-08-12T17:31:37.000Z'
originalURL: https://freecodecamp.org/news/8-reactjs-project-ideas-to-start-learning-by-doing
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/50-react-projects.jpg
tags:
- name: projects
  slug: projects
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "One of the best ways to learn is by doing. But often developers struggle\
  \ with the big question \"what should I build?\" \nHere are 8 project ideas, complete\
  \ with project briefs and layout ideas, to get you started learning by doing.\n\n\
  Business & Real-Wor..."
---

One of the best ways to learn is by doing. But often developers struggle with the big question "what should I build?" 

Here are 8 project ideas, complete with project briefs and layout ideas, to get you started learning by doing.

* [Business & Real-World: Map Statistics Dashboard](#heading-map-statistics-dashboard)
* [Fun & Interesting: Musical Instrument](#heading-musical-instrument)
* [Personal & Portfolio: Blog](#heading-blog)
* [Productivity: Notebook](#heading-notebook)
* [Puzzles & Games: Space Invaders](#heading-space-invaders)
* [Tools & Libraries: Framework Theme](#heading-framework-theme)
* [Project Add-Ons: Webmentions](#heading-webmentions)
* [Clones: Product Hunt](#heading-product-hunt)

_This is a preview of the free ebook [50 Projects for React & the Static Web](https://50reactprojects.com/). You can find the full 50 project ideas including these 8 at [50reactprojects.com](https://50reactprojects.com/)._

## Map Statistics Dashboard

**Category: Business & Real-World**

Create a map dashboard that shows statistics and geographic information about COVID-19.

### Brief

Dealing with a global pandemic means that viruses like the Coronavirus impact the world differently based on geographic location. 

Having a map with a breakdown of each country’s statistics is a useful way of being able to determine things like which countries have been impacted the most.

### Level 1

The easiest way to see statistics country to country is to have a map that you can browse with each country’s statistics available next to that country.  
  
Create a mapping app that uses the disease.sh Coronavirus API to add markers to the map for each country along with the number of COVID-19 cases.

### Level 2

While having the statistics for each country is helpful, it might be useful to be able to compare those statistics to the number of cases in the entire world.  
  
Add a statistics dashboard that shows the number of COVID-19 cases around the world as well as any other useful statistics from the API.

### Level 3

Getting current statistics is a good way to understand the current state of the world, but how does that compare historically?  
  
Use the historical data API to show graphs on the dashboard that provide context to the growth and spread of the virus.

### To Do

* Create a new map app
* Fetch API countries data
* Add markers to map
* Add statistics to markers
* Fetch API global data
* Create a stats dashboard
* Add global stats
* Fetch API historical data
* Add graphs to map

### Toolbox

* [Open Disease Data API](https://disease.sh/) (disease.sh)
* [React Leaflet](https://react-leaflet.js.org/) (react-leaflet.js.org)
* [Gatsby Leaflet Starter](https://github.com/colbyfayock/gatsby-starter-leaflet) (github.com)

### Tutorials

* [How to create a Coronavirus (COVID-19) Dashboard & Map App in React with Gatsby and Leaflet](https://www.freecodecamp.org/news/how-to-create-a-coronavirus-covid-19-dashboard-map-app-in-react-with-gatsby-and-leaflet/) (freecodecamp.org)
* [How to add Coronavirus (COVID-19) case statistics to your React map dashboard with Gatsby](https://www.freecodecamp.org/news/how-to-add-coronavirus-covid-19-case-statistics-to-your-map-dashboard-in-gatsby-and-react-leaflet/) (freecodecamp.org)
* [Mapping with React Leaflet](https://egghead.io/playlists/mapping-with-react-leaflet-e0e0?af=atzgap) (egghead.io)

### Inspiration

* [COVID-19 Dashboard by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University (JHU)](https://coronavirus.jhu.edu/map.html) (coronavirus.jhu.ed)
* [Coronavirus (COVID-19) Dashboard Demo](https://coronavirus-map-dashboard.netlify.app/) (coronavirus-map-dashboard.netlify.app)

### Layout Idea  


![Image](https://www.freecodecamp.org/news/content/images/2020/08/Coronavirus---Layout.jpg)
_Map Statistics Dashboard Layout Idea_

## Musical Instrument

**Category: Fun & Interesting**

Create an interactive piano that you can use to play music with your keyboard.

### Brief

Not everyone has the luxury of owning a musical instrument, but maybe those people have a laptop, phone, or tablet. Having a piano is a powerful way to let people play music even if they didn’t have the opportunity before.

### Level 1

Using the browser and web audio APIs, we can create sounds that, when put together, can actually sound like music.  
  
Create a set of buttons that play notes of a scale when clicked.

### Level 2

While not everyone’s played an instrument before, the concept and interface of an instrument like a piano is generally more intuitive than a bunch of buttons.  
  
Create a piano layout using buttons that work by either clicking the button or using the physical keyboard.

### Level 3

We might have limited space in the browser, but there’s a wide range of notes, scales, and sounds an electric keyboard might be able to make with some added effects.  
  
Create effect toggles that change the sound of the notes when toggled on.

### To Do

* Create buttons
* Play sound when clicked
* Arrange notes in a scale
* Create piano layout
* Set keyboard events
* Create effects layout
* Toggle audio effects

### Toolbox

* [React HotKeys](https://github.com/greena13/react-hotkeys) (github.com)

### Tutorials

* [Building a Piano with React Hooks](https://dev.to/ganeshmani/building-a-piano-with-react-hooks-3mih) (dev.to)
* [How to Build a Piano Keyboard Using Vanilla JavaScript](https://www.freecodecamp.org/news/javascript-piano-keyboard/) (freecodecamp.org)
* [Building a piano with tone.js!](https://dev.to/shimphillip/building-a-piano-with-tone-js-5c2f) (dev.to)
* [How I Made a Piano in only 1kb of JavaScript](https://frankforce.com/?p=7617#pianostory) (frankforce.com)

### Inspiration

* [React Guitar](https://react-guitar.com/) (react-guitar.com)

### Layout Idea

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Musical-Instrument---Layout.jpg)
_Musical Instrument Layout Idea_

## Blog

**Category: Personal & Portfolio**

Create a blog that you can use to share your career experiences and projects.

### Brief

With any career, having a blog to share your experiences is a good way let people know what you’re working on and help others learn from your experiences. 

It’s also a way to reinforce what you’ve learned so you can reference it in the future.

### Level 1

To be able to share your experiences, you need a website structure that will allow you to create new content and manage existing content. 

One way to do this is by creating markdown files that your website sources to create new pages and display the posts.  
  
Create a blog using markdown files as the content source.

### Level 2

Having your content in markdown files is a good way to manage static content, but you might not want to have to edit code every time you write or edit a post.  
  
Integrate a content management system that allows you to add new content or edit existing with a nice user interface.

### Level 3

If you’re sharing code on your blog, HTML natively supports the code and pre tags that help you format code in a readable way. But that doesn’t include syntax highlighting that helps improve readability.  
  
Integrate a syntax highlighter that makes code blocks more readable.

### To Do

* Create a blog
* Add first static content
* Source static content
* Integrate CMS
* Add code to content
* Add syntax highlighting

### Toolbox

* [Netlify CMS](https://www.netlifycms.org/) (netlifycms.org)
* [Prism.js](https://prismjs.com/) (prismjs.com)

### Tutorials

* [Making a Gatsby Blog with Netlify CMS](https://www.gatsbyjs.org/tutorial/blog-netlify-cms-tutorial/) (gatsbyjs.org)
* [How to Build Your Coding Blog From Scratch Using Gatsby and MDX](https://www.freecodecamp.org/news/build-a-developer-blog-from-scratch-with-gatsby-and-mdx/) (freecodecamp.org)

### Inspiration

* [Gatsby Netlify CMS Starter](https://gatsby-netlify-cms.netlify.app/) (gatsby-netlify-cms.netlify.app)

### Layout Idea

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Blog---Layout.jpg)
_Blog Layout Idea_

## Notebook

**Category: Productivity**

Create a notebook app to add, manage, and organize a group of notes.

### Brief

Taking notes is a great way to make sure we keep track of our thoughts or remember the important takeaways from a meeting. Being able to easily manage them and organize them is important for finding them later!

### Level 1

The first requirement of a notebook is being able to take notes. This can be pretty simple to start, where really you need some sort of input that collects what you write and stores it somewhere for later.  
  
Create a form to add new notes and view them in a list.

### Level 2

In order to find your notes later, you want some way of organizing those notes and a way to look them up. That includes adding categories or a tagging system as well as a UI to make searches from.  
  
Add the ability to tag or categorize notes and an input to search through them.

### Level 3

Whether we realize it or not, we can find connections between our thoughts and more importantly our notes, where we can take advantage of that network of thoughts for our notebook.  
  
Add Roam Research-inpsired linking of notes to create a network of thoughts.

### To Do

* Create a form
* Store new notes
* List notes
* Add tags or categories
* Add note search
* Add note network

### Toolbox

* [Gatsby Brain Theme](https://github.com/aengusmcmillin/gatsby-theme-brain) (github.com)
* [Fuse.js](https://fusejs.io/) (fusejs.io)

### Tutorials

* [How to Add Search to a React App with Fuse.js](https://www.freecodecamp.org/news/how-to-add-search-to-a-react-app-with-fuse-js/) (freecodecamp.org)

### Inspiration

* [Foam](https://foambubble.github.io/foam/) (foambubble.github.io)
* [Roam Research](https://roamresearch.com/) (roamresearch.com)
* [Gatsby Garden Theme](https://github.com/mathieudutour/gatsby-digital-garden) (github.com)

### Layout Idea

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Notebook---Layout.jpg)
_Notebook Layout Idea_

## Space Invaders

**Category: Puzzles & Games**

Create a space invaders spacecraft shooter game to shoot multiple waves of enemy ships.

### Brief

Space Invaders is an arcade classic that puts you in a spacecraft up against an alien invasion. As you try to shoot them down, they’re firing back, and you only have a limited amount of protection before you’re open to being hit.

### Level 1

The core part of the game is that you’re moving around a spacecraft trying to hit a bunch of aliens with your weapons. While there’s one of you, there’s many of them.  
  
Create a spacecraft that can move around and shoot aliens that are not moving.

### Level 2

What makes the game tricky, is that the aliens are constantly moving. Every time they hit the edge of the play area, they drop down and speed up, getting closer to your ship.  
  
Add movement to the aliens going side to side on the play area. Every time the aliens reach one side they should drop down a level. They should also speed up at certain intervals.

### Level 3

You’re on your own, but luckily you can get some protection. You have shields that you can hide behind that help protect you while they last.  
  
Create several shields in front of the player spacecraft that can take a limited amount of damage.

### To Do

* Create a new game
* Create static aliens
* Create a player spacecraft
* Add spacecraft controls
* Add spacecraft weapon
* Configure alien damage
* Make aliens shoot back
* Make aliens move
* Add alien intervals
* Add shields

### Tutorials

* [Learn JavaScript by building 7 games](https://www.freecodecamp.org/news/learn-javascript-by-building-7-games-video-course/) (freecodecamp.org)

### Inspiration

* [Space Invaders](https://codepen.io/adelciotto/pen/BHuGL) (codepen.io)

### Layout Idea

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Space-Invaders---Layout.jpg)
_Space Invaders Layout Idea_

## Framework Theme

**Category: Tools & Libraries**

Create a Gatsby theme that sets up a project with the Tailwind CSS framework.

### Brief

As developers, we commonly have to do a bunch of similar steps any time we create a new project. But tools like themes let us abstract those steps and package them in an easy to use way that can work for any new project.

### Level 1

Gatsby themes are a plugin-like system where we can take advantage of the Gatsby pipeline to share functionality as a package on npm. 

This opens the door to really doing anything we would do in a Gatsby site, but making it reusable to any Gatsby site.  
  
Create a new Gatsby theme that, when used, creates a new a style guide page on any project it’s added to.

### Level 2

The goal of themes isn’t just to create pages, but to add functionality that makes us productive. This includes things like frameworks and project configurations.  
  
Add a CSS framework to the Gatsby theme that lets the project it’s added to use that framework.

### Level 3

Sometimes themes are better only as tools, sometimes it’s helpful to be opinionated. One way to add useful functionality to a CSS framework is to create stock components.  
  
Create reusable React components using the CSS framework that can be used in the project the theme’s added to.

### To Do

* Create a new theme
* Add to example project
* Create new style page
* Add CSS framework
* Use CSS in example
* Create components
* Use components

### Toolbox

* [Gatsby Themes](https://www.gatsbyjs.org/docs/themes/) (gatsbyjs.org)
* [Tailwind](https://tailwindcss.com/) (tailwindcss.com)

### Tutorials

* [Building a Theme](https://www.gatsbyjs.org/tutorial/building-a-theme/) (gatsbyjs.org)
* [What is Tailwind CSS and How Can I Add it to my Website or React App?](https://www.freecodecamp.org/news/what-is-tailwind-css-and-how-can-i-add-it-to-my-website-or-react-app/) (freecodecamp.org)

### Inspiration

* [Gatsby Tailwind Theme](https://github.com/talensjr/gatsby-theme-tailwindcss) (github.com)

### Layout Idea

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Framework-Theme---Layout.jpg)
_Framework Theme Layout Idea_

## Webmentions

**Category: Project Add-Ons**

Add webmentions integration to a website that shows Twitter interactions with the website.

### Brief

Social interaction is an impactful way to bring more of an audience and conversation to topics we write about. 

Having something on a website shows that interaction can be helpful to both inspire people to want to get involved or let people feel like they can be part of it.

### Level 1

In order to make use of Webmentions, a website needs to be configured with meta tags to provide information.  
  
Add the proper meta tags to a website and validate its use with webmention.io.

### Level 2

The Webmentions API is a way to programmatically see connections in social interactions from a URL of your website. It lets you get the type of interaction and even the person’s profile avatar.  
  
Connect a website to Webmentions and add a list of social interactions to blog post pages.

### Level 3

Now that the website is showing all of the interactions, there should be an easy way to join the conversation.  
  
Add a social link that, when clicked, creates a tweet with a link to the page.

### To Do

* Add meta tags to website
* Validate meta tags
* Connect to Webmention
* Connect social to Bridgy
* List interactions
* Add tweet button

### Toolbox

* [Webmention.io](https://webmention.io/) (webmention.io)
* [Bridgy](https://brid.gy/) (brid.gy)
* [Gatsby Plugin Webmention](https://github.com/ChristopherBiscardi/gatsby-plugin-webmention) (github.com)

### Tutorials

* [Indieweb pt2: Using Webmentions in Eleventy](https://mxb.dev/blog/using-webmentions-on-static-sites/) (mxb.dev)
* [Clientside Webmentions](https://www.swyx.io/writing/clientside-webmentions/) (swyx.io)
* [Getting started with Webmentions in Gatsby](https://www.knutmelvaer.no/blog/2019/06/getting-started-with-webmentions-in-gatsby/) (knutmelvaer.no)
* [Building Gatsby Plugin Webmentions](https://www.christopherbiscardi.com/post/building-gatsby-plugin-webmentions) (christopherbiscardi.com)

### Inspiration

* [Knut Melvær](https://www.knutmelvaer.no/blog/) (knutmelvaer.no)
* [Swyx](https://swyx.io/) (swyx.io)

### Layout Idea

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Webmentions---Layout.jpg)
_Webmentions Layout Idea_

## Product Hunt

**Category: Clones**

Create a Product Hunt clone that lets people post a new product with ratings.

### Brief

We all live for products, whether it’s our mobile phones or the apps we use on our laptops. 

While there are tons of products in the world, it can be hard to navigate through the good and the bad. Tools like Product Hunt provide a platform to learn about new tools and get reactions and reviews from others.

### Level 1

The most important part about learning about new products is the product itself. We want to know what the product is, what it looks like, and how it works.  
  
Create a page that lets you add a new product to a website with a title, picture, and description.

### Level 2

When learning about products, reviews are a way we can trust a product before we purchase it. It helps us gain confidence in what we’re about to spend our money or time on.  
  
Add the ability for people to add reviews about each product.

### Level 3

People love products, so there are tons of them in the world. There are way too many to try to sort through manually, so we need a mechanism to search and browse with.  
  
Add the ability to search products and browse by category.

### To Do

* Create product website
* Create database
* Add product form
* Add product to database
* Request product for page
* Add review form
* Add reviews to database
* Add reviews to product
* Add product search
* Add product categories

### Toolbox

* [Hasura](https://hasura.io/) (hasura.io)

### Tutorials

* [Building a Product Hunt clone app using Hasura and Next.js](https://blog.logrocket.com/building-a-product-hunt-clone-app-using-hasura-and-next-js/) (logrocket.com)
* [How to build a basic version of Product Hunt using React](https://www.freecodecamp.org/news/how-to-build-a-basic-version-of-product-hunt-using-react-f87d016fedae/) (freecodecamp.org)

### Layout Idea

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Product-Hunt---Layout.jpg)
_Product Hunt Layout Idea_

## More Projects

If you want more project ideas, check out [50 Projects for React & the Static web](https://50reactprojects.com/)!

<p style="text-align: center;">
    <a href="https://50reactprojects.com/">
    	<img src="https://www.freecodecamp.org/news/content/images/2020/08/Twitter-Post---1.jpg" alt="Stop asking yourself what should I build?" style="
		    max-width: 840px;
		    border: solid 5px #0A64EC;
		">
    	<button style="
    		background-color: #9162BB;
	    	color: white;
		    font-weight: bold;
    		padding: .5em 1em;
    		border-radius: .2em;
		    box-shadow: 0 2px 4px rgba(0,0,0,.25);
		">Download Free at 50reactprojects.com</button>
    </a>
</p>



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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

