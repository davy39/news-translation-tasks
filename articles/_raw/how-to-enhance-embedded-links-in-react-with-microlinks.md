---
title: How to Enhance Embedded Links in React with Microlinks
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-06-18T02:56:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-enhance-embedded-links-in-react-with-microlinks
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/microl.jpg
tags:
- name: React
  slug: react
seo_title: null
seo_desc: The web has evolved from rigid color coding and 2D rendering to an era of
  complex, aesthetically pleasing animations and 3D rendering options. There have
  also been integrations with new technologies, such as virtual reality tools and
  frameworks, to i...
---

  
The web has evolved from rigid color coding and 2D rendering to an era of complex, aesthetically pleasing animations and 3D rendering options. There have also been integrations with new technologies, such as virtual reality tools and frameworks, to improve the user experience.

In this article, you'll learn how to optimize embedded links in your front-end development projects to meet your desired specifications. 

The inspiration for this article came from a problem I encountered while creating a portfolio site and having issues embedding external sites—until I discovered an efficient tool to help.

To fully grasp this tutorial, there are some of the prerequisites:

* A good knowledge of JavaScript.
* Familiarity with React JS and npm package installation.
* Proficiency in CSS.

Let's get started!

## The Concept of Micro-linking

Micro-linking entails embedding a link to an external website within a default web page. Embedding links are different from the default HTML  `“alt href”`  attributes commonly used by web developers.

This concept also entails extracting relevant site metadata, information and relevant images from the embedded external site link. This contributes to providing more knowledge about the external website in question.

This feature isn’t all new as it's commonly used among high-end blog posts, video streaming sites and e-commerce sites. This feature is also utilized by site owners to customize how their site information is viewed when embedded in advertisement sites.

## How Does Micro-linking Work?

Ordinarily, embedding a URL using plain HTML code doesn’t generate any image or text preview. However, this isn’t the case for micro-links. This occurs due to the use of an application programming interface to extract relevant info from the site being referenced and then outputting it to the developer in JSON format for easy customization and usage. 

There are quite a lot of micro-linking services available commercially. Some examples are [Embedly](https://embed.ly/), [Open Graph](https://ogp.me/) protocol, [microlink.io](https://microlink.io/), and so on.

## Introduction to the Microlink Package

In this tutorial, we'll create a site that uses a Node package known as Microlink to generate previews. Details regarding URL customization will also be illustrated. 

This is customization allows developers to easily extract relevant link previews from the Microlink site, skipping the hassle of interacting with the website interface. 

For further learning, the library has a rich documentation site which can be accessed [here](https://microlink.io/docs/sdk/integrations/react).

## How to Set Up Your Project

To build the link preview site, we'll utilize the React Vite tool. Entering the command `npm create-vite-app@latest links` immediately spins up a folder named `latest links` which we'll use in building this project.

Also, the `microlink` package needs to be installed. To do that, navigate to the command line and run the `npm i @microlinks/react` command.

## Demo Project

First of all, we'll be create the default JSX functional component for this project.

```
function App() {
return (
<>
</>
)
}
export default App

```

Next, we'll be import and initialize the installed `microlink` library:

```
import Microlink from '@microlink/react'

```

After that, we can initialize the package within the App function:

```
return (
<>
<Microlink
url= " https://tobilyn77.hashnode.dev/nodejs-clustering-and-load-balancing-comprehensive-overview "  />
</>
)

```

The URL variable I included is a link to an external site I intend to preview on my local site. This can be changed to whichever site you would like to preview.

On running this, you should see something similar to this.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/micro1-1.JPG)
_microlink project webpage_

  
We have successfully set up a micro-link in our application. But that’s not all, the power of the package is enormous, providing a level of flexibility in controlling the layout and size of the micro-links.

### Size Tweaking

Size tweaking simply involves adjusting the size or dimensions of a variable to suit different specifications. In this case, we'll adjust the size of the embedded links. 

```
<Microlink
url= "https://tobilyn77.hashnode.dev/nodejs-clustering-and-load-balancing-comprehensive-overview" />
<p></p>
<Microlink
url= "https://tobilyn77.hashnode.dev/nodejs-clustering-and-load-balancing-comprehensive-overview"  size="small"/>
<p></p>

```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/micro2.JPG)
_micro-links with different sizes_

The code above specifies the size of the micro-link to be rendered. If the size is indicated to be `small`, the dimension of the micro-link gets altered. It also allows for large and medium sizes, and by default, the medium size is what is usually seen when no size dimension is specified.

Also, the `microlink` self-enclosing tag allows for CSS styling. This can be achieved by including the style variable within the `microlink` tag.

```
<Microlink
url= "https://tobilyn77.hashnode.dev/nodejs-clustering-and-load-balancing-comprehensive-overview"
style= {{color: 'red'}} />

```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/micro3.JPG)
_micro-link with the color set to red_

As you can see in the code above, the `microlink` was styled with the color red and that reflected in the output. Other CSS styling can also be applied to give users an aesthetic feel to your site.

## Conclusion

With this, we have come to the end of the tutorial. We hope you’ve learned link previewing via the `microlink` package.

Feel free to drop any questions or comments in the comment box below. You can also interact with me on my blog and check out my other articles  [here](https://www.freecodecamp.org/news/p/cedba683-793c-4c78-85d9-c46647c75b71/linktr.ee/tobilyn77). Till next time, keep on coding!

