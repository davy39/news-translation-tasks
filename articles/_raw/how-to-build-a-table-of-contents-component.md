---
title: How to Build a Table of Contents Component for Your Blog
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-03T14:54:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-table-of-contents-component
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/toc.jpg
tags:
- name: blog
  slug: blog
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'By Caleb Olojo

  When you visit documentation sites, you''ll notice that many of them have a common
  component: the <TableOfContent /> component.

  The idea behind it is to give the reader a "heads-up" about the information they''re
  trying to consume.

  This ...'
---

By Caleb Olojo

When you visit documentation sites, you'll notice that many of them have a common component: the `<TableOfContent />` component.

The idea behind it is to give the reader a "heads-up" about the information they're trying to consume.

This feature, in turn, helps the reader go directly to the section that includes a solution to whatever bug or issue they're facing, without reading the whole article. It contributes to a good User Experience because you end up saving your audience the hassle of extra scrolling and searching.

I have a personal [blog](https://meje.dev/blog) that I dedicate a lot of my time to. And for a long time, I thought about adding this feature. It will help anyone visiting my site to enjoy their time and find what they need.

This article is a summary of my process, so you don't have to go through the issues I went through. If you're trying to add a Table of Contents feature to your blog, you can walk through it with me.

I shared a video of what the component looked like after completing it. You can take a look at it [here](https://twitter.com/calebolojo/status/1629113931066142720).

## **How to Get Heading Text from the Frontmatter**

To build a table of contents feature, I knew what I needed to do. Since the articles on my blog are written in markdown, I am just using a superset of markdown – MDX – which allows me to use React components in markdown files.

The first thing on my list was to get a way to render the heading text in a component. This way, when people clicked on the headings, the browser would scroll to that point in the article.

With HTML, you can achieve this by using the anchor tag and passing the value to an `href` attribute.

To have linked text pointing to a section, the ideal way of doing this would look like what's in the snippet below:

```html
<a href="#section-one">Go to section one</a>
<a href="#section-two">Go to section two</a>
<a href="#section-three">Go to section three</a>

<section id="section-one">some content</section>
<section id="section-two">yet, a content that seems weird</section>
<section id="section-three">some content, again</section>

```

In the snippet above, the anchor tags are tied to the sections with respect to their `id` attribute in the DOM. When you click on any text, it takes you to the respective section.

With this mental model, I thought of populating the frontmatter of each article with the headings in all the articles I've written. I knew it was going to be stressful, but I went with it anyway.

For context, this is what a frontmatter in a markdown file looks like. The frontmatter contains the metadata of all articles on my blog. Details like the title, date it was published, the tags or category that the article falls into, the description, a canonical URL, and any other thing you may feel like adding to improve your article's SEO.

This pattern is common when you're building blogs with Next.js and MDX (markdown in general). It has a YAML-like syntax too.

```bash
---
id: 20
title: Building a Table of Content component
publishedAt: '2023-02-28'
excerpt: description of the article
tags:
  - ux
  - nextjs
headings:
  - heading-one
  - heading-two
  - heading-three
cover_image: /img/covers/toc.jpg
---

```

The snippet above is what the frontmatter of this article looks like, but with the `headings` entry. I'm going to use that to explain my initial approach. If I go ahead and map through the frontmatter, I'll be able to retrieve the content from the headings array.

It's great because I'll be able to use the items in the `headings` array in the TableOfContent component. It felt surreal, and I was elated for a minute. The component looked like this:

```jsx
import React from 'react'
import { HeadingContainer } from './style/toc.styled'

export default function TableOfContents({ headings }) {
  return (
    <HeadingContainer>
      <p>In this article</p>
      <ul>
        {headings.map((item, index) => (
          <li key={index}>
            <a href={`#${item}`}>{item}</a>
          </li>
        ))}
      </ul>
    </HeadingContainer>
  )
}

```

The component above receives a headings prop alone, which in turn receives a value from the frontmatter through the Next.js `getStaticProps()` method.

```jsx
export default function Blog({
  post: {
    frontmatter: { title, headings },
  },
}) {
  return (
    <>
      <Head>
        <title>{title}</title>
      </Head>
      <TableOfContents headings={headings} />
    </>
  )
}

// destructuring params to get the unique slugs
export async function getStaticProps({ params }) {
  const { slug } = params
  const { frontmatter } = await getArticleFromSlug(slug)

  return {
    props: {
      post: {
        frontmatter,
      },
    },
  }
}

```

If everything in the snippets above seems a bit confusing, you can take a look at this article where I wrote about the [process of setting up a Next.js blog](https://meje.dev/blog/how-i-built-this-blog).

With that out of the way, the component rendered the list of items from the frontmatter, and it looked fine.

But, the moment I clicked on an item, hoping to be scrolled to that section, it did not work as expected. I ran into an error, which you'll see in the next section.

## **How to Use extract-md-headings**

I realized that when I clicked on an item in the component, the browser encoded the URL of the current slug with an encoding parameter for spaces – `%20%` – which in turn led to the issue.

Although, I realized that it also could be the way I was referencing the heading elements in the `frontmatter`. But that didn't end up mattering, because I found an alternative and it worked great.

After I made sure that it worked perfectly, I went on and published that alternative as a [package](https://npmjs.com/package/extract-md-headings) to the npm registery.

The package extends a function, `extractHeadings()`, that accepts a string, as a path, to where the markdown file is and extracts any text that matches how heading texts are written in markdown files. You can take a look at the source code [here](https://github.com/kaf-lamed-beyt/extract-md-headings/blob/834ad610c80db6a367260b3ec6927c9cd2099a5c/src/index.ts#L15-L36) if you want to see how it works under the hood.

With this tool in my arsenal, I modified the `getStaticProps` method to use the function. Why? you might ask me. Well, because the package depends solely on Node's `fs` module, which equates to a server-side scripting approach.

With Next.js we can perform server-side operations in the pages directory with any of the data-fetching methods, `getStaticProps`, `getStaticPaths`, and `getServerSideProps`:

```jsx
import React from 'react'
import { extractHeadings } from 'extract-md-headings'

export default function Blog({
  post: {
    fileContent,
    frontmatter: { title },
  },
}) {
  return (
    <>
      <Head>
        <title>{title}</title>
      </Head>
      <TableOfContents headings={fileContent} />
    </>
  )
}

export async function getStaticProps({ params }) {
  const { slug } = params
  const { frontmatter } = await getArticleFromSlug(slug)
  const mdxContent = extractHeadings(`/path/to/where/${slug}.mdx`)

  return {
    props: {
      post: {
        frontmatter,
        fileContent: mdxContent,
      },
    },
  }
}

```

The `[slug].js` page is now aware of the `fileContent` through the `heading` prop from the `TOC` component. So I need to modify it so it will accommodate the properties that the function returns.

```jsx
import React from 'react'
import { HeadingContainer } from './style/toc.styled'

export default function TableOfContents({ headings }) {
  return (
    <HeadingContainer>
      <p>In this article</p>
      <ul>
        {headings.map(({ slug, title, id }) => (
          <li key={id}>
            <a href={`#${slug}`}>{title}</a>
          </li>
        ))}
      </ul>
    </HeadingContainer>
  )
}

```

For now, the component just renders the list of items in the array that is returned from the function, with no interactivity, no way to track which element is active, and many more things that I haven't been able to add for now.

## **How to Add Click and Scroll-based States**

If there's anything I love about React, it is its ability to track state. I've seen how this works on other doc platforms – when you click on an item, it becomes active, when you scroll into the section where there's a heading tag, it becomes active.

A lot of people have different approaches to monitoring these states. I chose to go with the simplest one — changing the color — because, as usual, "I no like stress". The default text color in my component's UI is sorta "grey-ish", so when it is active, it becomes white.

I'll start with the snippets of the modification I made to the component with the `useState` hook, some DOM APIs, and the `getBoundingClientRect` web API. It's a lot – I know 😩. But, please stay with me, I'll try to break it down simply.

It is a common approach to have a default value — a boolean, string, or number — when we use the `useState` hook. In the snippet below, the component uses the `headings` prop to check if the length of the array isn't empty, is greater than zero, and sets the default state of the component to that of the first element.

```js
const [active, setActive] = React.useState(
  headings.length > 0 ? headings[0].slug : ''
)

```

If the array is empty, no element will have the active state style. For now, if you place an `onClick` attribute in the list element — like I did — and pass the `slug` as an argument, It'll toggle the style you have written in the `style` attribute.

```jsx
<li
  key={index}
  onClick={() => setActive(slug)}
  style={{
    color: active === slug ? '#fff' : '',
  }}
>
  <a href={`#${slug}`}>{title}</a>
</li>

```

Handling the scroll state would require the use of React's `useEffect` hook because it contains all the lifeCycle methods —  `componentDidMount()`, `componentDidMount()`, and `componentWillUnmount()`. Here, I decided to track the scroll state by listening to the native scroll event with the DOM `EventTarget` interface.

The function `handleScroll` below maps the result we're getting from the `extractHeadings()` function by destructuring the `slug` property from the object. It proceeds to return all the elements containing a proper `id` attribute with `getElementById` and assigns the value to `headingElements`.

```js
const handleScroll = () => {
  const headingElements = headings.map(({ slug }) =>
    document.getElementById(slug)
  )
  const visibleHeadings = headingElements.filter((el) =>
    isElementInViewport(el)
  )
  if (visibleHeadings.length > 0) {
    setActive(visibleHeadings[0].id)
  }
}

```

Still in this function, the `visibleElements` is filtered from the array of `headingElements`, and the `isElementInViewport` function is used to check which heading element is currently in the viewport — this is possible with `getBoundingClientRect`, I'll get to that soon. 

The function closes with a condition to set an active element if the length of the visible headings is greater than zero.

Now, I can go ahead to wrap this function in the Effect, initiate the cleanup of the scroll event, and pass the `headings` prop inside the dependency array. Then the Effect is only triggered when the `headings` prop changes.

```js
React.useEffect(() => {
  const handleScroll = () => {
    const headingElements = headings.map(({ slug }) =>
      document.getElementById(slug)
    )
    const visibleHeadings = headingElements.filter((el) =>
      isElementInViewport(el)
    )
    if (visibleHeadings.length > 0) {
      setActive(visibleHeadings[0].id)
    }
  }

  document.addEventListener('scroll', handleScroll)

  // clean up the effect by removing the event listener
  return () => {
    document.removeEventListener('scroll', handleScroll)
  }
}, [headings])

```

`isElementInViewport` is the cherry on top of this feature. The function accepts an element, `el` as an argument, and it checks if its bounding rectangle (this sorta proves the box principle on the web to be correct, again) is inside the viewport of the browser.

```js
const isElementInViewport = (el) => {
  const rect = el.getBoundingClientRect()
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <=
      (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  )
}

```

This is possible because of the `getBoundingClientRect` web API. The method returns an object containing the coordinates of the top, left, bottom and right edges of the element relative to the viewport.

When `getBoundingClientRect` is called, it returns an object containing the coordinates of the top, left, bottom, and right edges of a particular heading element relative to the viewport.

In the context of this feature, the element that is relative to the viewport is the heading element which is being retrieved using the `getElementById` method.

The function returns true if the top and left coordinates are greater than or equal to zero, and the bottom and right coordinates are less than or equal to the height and width of the viewport, respectively.

For the function to return `true`, we'd have to get the value of the viewport's height and width. That's why it is convenient to compare these values with `window.innerHeight` and `window.innerWidth` or `documentElement.clientHeight` and `documentElement.clientWidth`.

## **Why the Stress? IntersectionObserver Fixes This Issue**

I know that going the `intersectionObserver` route would've saved me a lot of stress. But, I chose this approach nonetheless, because I wanted to understand the inner workings of how this feature is built by other people.

I think there's an intersection observer package that you can use to monitor scroll events in React applications, too. So you may not even need to go this route. But I want to share some of the reasons I decided to use this API, instead of the `IntersectionObserver`.

In terms of Accuracy, `getBoundingClientRect` returns a more accurate position of the element relative to the viewport, while `IntersectionObserver` uses an approximation based on the element's bounding box.

This means that `getBoundingClientRect` can be more precise for certain use cases, such as when you need to trigger an action as soon as the element enters the viewport — just like we're changing the active state of the list item in the component.

In terms of Browser compatibility, `IntersectionObserver` is a relatively new API, and its support by other browsers may not be available. But, `getBoundingClientRect` on the other hand is widely supported by modern browsers.

One advantage that `IntersectionObserver` has over `getBoundingClientRect` is in terms of performance. This is because the API uses an optimized algorithm that minimizes the amount of work needed to detect the changes in the intersection state when you are tracking so many elements.

The `getBoundingClientRect` API cannot handle so many elements.

## **Wrapping Up**

I know that a lot of people would still prefer to use `intersectionObserver`. But, I decided to go with this other approach because it opened my eyes to how `intersectionObserver` itself works under the hood, and most importantly, it suited my use case.

This is what the logic of the TOC component looks like — without the markup. Copy it and use it if you want.

```jsx
import React from 'react'
import { HeadingContainer } from './style/toc.styled'

const TableOfContents = ({ headings }) => {
  const [active, setActive] = React.useState(
    headings.length > 0 ? headings[0].slug : ''
  )

  React.useEffect(() => {
    const handleScroll = () => {
      const headingElements = headings.map(({ slug }) =>
        document.getElementById(slug)
      )
      const visibleHeadings = headingElements.filter((el) =>
        isElementInViewport(el)
      )
      if (visibleHeadings.length > 0) {
        setActive(visibleHeadings[0].id)
      }
    }

    document.addEventListener('scroll', handleScroll)
    return () => {
      document.removeEventListener('scroll', handleScroll)
    }
  }, [headings])

  const isElementInViewport = (el) => {
    const rect = el.getBoundingClientRect()
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <=
        (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    )
  }

  return // component markup
}

export default TableOfContents

```

If you read up to this point, please share this article. Thanks as you do so. You can also read up on the [getBoundingClientRect() web API](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) if you want to get an in-depth understanding

