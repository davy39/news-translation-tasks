---
title: 'Gatsby Starter Blog: How to Add Header Images to Posts with Support for Twitter
  Cards'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-29T00:33:15.000Z'
originalURL: https://freecodecamp.org/news/gatsby-blog-header-image-twitter-card
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/freeCodeCamp-GatsbyBlogImageTwitterCard-5.png
tags:
- name: blog
  slug: blog
- name: Gatsby
  slug: gatsby
- name: GraphQL
  slug: graphql
- name: open graph
  slug: open-graph
- name: Twitter
  slug: twitter
seo_title: null
seo_desc: "By David Good\nIf you're like me, you used Gatsby Starter Blog to kickstart\
  \ your personal blog, made a few customizations, and then just rolled with it. \n\
  Adding new posts in the form of markdown is great. But it also means you rarely\
  \ have a reason to ..."
---

By David Good

If you're like me, you used [Gatsby Starter Blog](https://www.gatsbyjs.com/starters/gatsbyjs/gatsby-starter-blog) to kickstart your personal blog, made a few customizations, and then just rolled with it. 

Adding new posts in the form of markdown is great. But it also means you rarely have a reason to look at the code. So when I decided to add header images to my posts with support for [Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards), I felt lost.

My requirements were to be able to add a large header image with a caption to a post as you can see here:

%[https://davidagood.com/dynamodb-enhanced-client-java-heterogeneous-item-collections/]

Furthermore, a tweet which contains a link to the post should "expand" into [Twitter's Summary Card with Large Image](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image), like this:

%[https://twitter.com/helloworldless/status/1336323721254948864]

And finally, for posts which do not specify an image, a default image should be shown using [Twitter's Summary Card](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary). Here's what that looks like where I've used my website logo as the default image:

%[https://twitter.com/helloworldless/status/1338482084445347844]

**Note:** Twitter's docs state that a website logo should not be used for a card image (see `twitter:image` section [here](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary#reference)). I'll leave it to you to decide whether it makes sense to use a fixed image as a fallback like I have here.

## Getting Started

Here are the five high-level steps which I will be guiding you through. I'll attempt to explain everything in depth and provide links to other resources along the way. That way you will build up your knowledge of Gatsby which you can draw from to tackle the later, more complicated steps.

1. Add Document Metadata Tags
2. Source Default Image using GraphQL
3. Source Post-Specific Image Properties using GraphQL
4. Add Header Image to Blog Post Template
5. Add New Properties to Post's Frontmatter

The tools which we'll be using to accomplish this all come out of the box with [Gatsby Starter Blog](https://www.gatsbyjs.com/starters/gatsbyjs/gatsby-starter-blog)!

* [React Helmet](https://github.com/nfl/react-helmet) - Used in the `SEO` component to add meta tags to the document head to support Twitter Cards and other [Open Graph](https://ogp.me/) tags
* [Gatsby Source Filesystem](https://www.gatsbyjs.com/plugins/gatsby-source-filesystem/) - A "plugin for sourcing data into your Gatsby application from your local filesystem", images in our case
* [Gatsby Image](https://www.gatsbyjs.com/plugins/gatsby-image/) - "a React component specially designed to work seamlessly with Gatsby’s GraphQL queries. It combines [Gatsby’s native image processing](https://image-processing.gatsbyjs.org/) capabilities with advanced image loading techniques to easily and completely optimize image loading for your sites. `gatsby-image` uses [gatsby-plugin-sharp](https://www.gatsbyjs.com/packages/gatsby-plugin-sharp/) to power its image transformations."
* [Gatsby Plugin Sharp](https://www.gatsbyjs.com/plugins/gatsby-plugin-sharp/) - "Exposes several image processing functions built on the [Sharp image processing library](https://github.com/lovell/sharp)". We use this for resizing images.

## How to Add Document Metadata Tags

First, we will wire up the HTML metadata tags which can be read by Twitter and any other platform or tool which understands [Open Graph](https://ogp.me/) such as Google, Facebook, and WhatsApp. 

Learn more about document metadata here: [What’s in the head? Metadata in HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML).

Open the `SEO` component in `src/components/seo.js`. The first thing to notice is that this is using [React Helmet](https://github.com/nfl/react-helmet), and it already has many Open Graph and Twitter meta tags like `og:title`, `twitter:description`. It even has a `twitter:card` tag with a value of "summary" which enables a basic Twitter Summary Card with no image:

```js
// src/components/seo.js
const SEO = ({ description, lang, meta, title }) => { 
// Details omitted for brevity 
return ( 
    <Helmet 
        htmlAttributes={{ lang }} 
        title={title} 
        titleTemplate={`%s | ${site.siteMetadata.title}`} 
        meta={[ 
            { name: `description`, content: metaDescription, }, 
            { property: `og:title`, content: title, }, 
            { property: `og:description`, content: metaDescription, }, 
            { property: `og:type`, content: `website`, }, 
            { property: `twitter:card`, content: `summary`, }, 
            { property: `twitter:creator`, 
              content: site.siteMetadata.social.twitter, }, 
            // ...
```

Let's update this component:

1. Add `imageUrl` and `imageAlt` parameters. These will be passed as props by the `BlogPostTemplate` component as we will see later. Note that that I've used "URL" in the prop name to convey the fact that this must be a fully-qualified URL. Relative paths are not supported for the OG image!
2. Construct the default image URL, `defaultImageUrl`. I've written a tiny utility function, `constructUrl`, to concatenate a base URL with a relative path. We will see where `data.ogImageDefault` comes from in the next section.
3. Add an `ogImageUrl` variable which takes the `imageSrcUrl` prop or, if that's not provided, defaults to `defaultImageUrl`.
4. Add objects to the `meta` array passed to the `Helmet` component: `og:image`, `twitter:card`, and `twitter:image:alt`

A few things to note here:

1. Twitter does have its own `twitter:image` meta tag, but per the [docs](https://developer.twitter.com/en/docs/twitter-for-websites/cards/guides/getting-started#twitter-cards-and-open-graph), we don't need to add both the `og:image` and the `twitter:image` tag since Twitter's parser will fall back to the Open Graph tags.
2. Open Graph specifies the `meta` attributes `property` and `content` whereas Twitter specifies `name` and `content`, respectively. But again, the Twitter docs state that their parser will fall back to the Open Graph attributes. This is nice because we can maintain consistency and don't need a bunch of repetitive properties with the same values which we have to keep in sync.
3. Notable exceptions to using the `property` attribute on `meta` tags are any non-Open Graph tags like `description` which must use the `name` attribute. I encourage you to use [Lighthouse](https://developers.google.com/web/tools/lighthouse) which will identify basic issues with your SEO.

```js
// util.js
export const constructUrl = (baseUrl, path) =>
  (!baseUrl || !path) ? null : `${baseUrl}${path}`;

// src/components/seo.js
// Step 1: Add props
const SEO = ({ description, lang, meta, title, imageUrl, imageAlt }) => { 
    
    const data = useStaticQuery(
        // This is explained next
    );
                                
    // Step 2: Construct default image URL
    // ogImageDefault is explained next
    const defaultImageUrl = constructUrl(data.site.siteMetadata.siteUrl, data.ogImageDefault?.childImageSharp?.fixed?.src)
    
    // Step 3: Add this
    const ogImageUrl = imageUrl || defaultImageUrl; 
    
    return ( 
        // Step 4: Add new meta objects
        <Helmet 
            htmlAttributes={{ lang }} 
            title={title} 
            titleTemplate={`%s | ${site.siteMetadata.title}`} 
            meta={[
                { property: `og:image`, content: ogImageUrl, }, 

                // If a post has an image, use the larger card. 
                // Otherwise the default image is just 
                // a small logo, so use the smaller card.
                { property: `twitter:card`, content: imageUrl ? `summary_large_image` : `summary`, }, 

                // Add image alt text
                // Falls back to default which describes the site logo
                { property: `twitter:image:alt`, content: imageAlt || "davidagood.com logo", }, 
                // ...
```

## How to Source Default Image using GraphQL

This is where Gatsby's filesystem and image processing capabilities come into play. Below is the `useStaticQuery` call GraphQL query from the `SEO` component. I've added the `ogImageDefault` portion and the `siteUrl` which is needed for the `constructUrl` call shown above.

```js
// src/components/seo.js
const data = useStaticQuery(
    graphql`
      query {
        site {
          siteMetadata {
            title
            description
            social {
              twitter
            }
            # Add this
            siteUrl
          }
        }
        # Add this
        ogImageDefault: file(relativePath: {eq: "icon.png"}) { 
          childImageSharp {
            fixed(height: 260, width: 260) {
              src
            }
          }
        }
      }
    `,
);
```

### GraphQL File and Image Processing Query Explained

The top level node is `ogImageDefault`. This is a [GraphQL alias](https://graphql.org/learn/queries/#aliases) for the `file` query which is applying a filter to find a file with relative path equal to `icon.png`. The name I've chosen, `ogImageDefault`, is completely arbitrary.

One key thing to understand here is what the `relativePath` is relative to. In other words, where is this file, `icon.png`? 

Let me start by telling you the location of the file relative to the project root: `./content/assets/icon.png`. In the query, I haven't specified any relative path, just the filename. So how does Gatsby know where to find it? 

Enter `[gatsby-source-filesystem](https://www.gatsbyjs.com/plugins/gatsby-source-filesystem/)`. If you look in `gatsby-config.js` you will see some config like this:

```js
// gatsby-config.js 
module.exports = { 
    // siteMetadata: {...}, 
    plugins: [ 
        // Other plugins omitted 
        { 
            resolve: `gatsby-source-filesystem`, 
    	    options: { 
                path: `${__dirname}/content/blog`, 
                name: `blog`, 
            }, 
        }, 
        { 
            resolve: `gatsby-source-filesystem`, 
            options: { 
                path: `${__dirname}/content/assets`, 
                name: `assets`, 
            }, 
        }, 
    	// ...
```

What this is doing is registering these paths as "content roots" and giving them a name. So the name `blog` refers to `./content/blog` relative to the project root. And the name `assets` refers to `./content/assets` relative to the project root. You can use these names in queries by filtering on `sourceInstanceName`:

```graphql
# http://localhost:8000/___graphql 
{ 
    allFile(filter: {sourceInstanceName: {eq: "blog"}}) { 
        edges { 
            node { 
                absolutePath 
                publicURL 
                sourceInstanceName 
            } 
        } 
    } 
}
```

The result of this query:

```js
// Result of allFiles query with sourceInstanceName filter 
{ 
    "data": { 
        "allFile": { 
            "edges": [{ 
                "node": { 
                    "absolutePath": "/home/dgood/IdeaProjects/davidagood.com/content/blog/clean-code-and-architecture/index.md", 
                    "publicURL": "/static/40bb02d938c4faf7f977dd66c1a399d2/index.md", 
                    "sourceInstanceName": "blog" 
                } 
            }, 
            // additional results...
```

So back to `ogImageDefault`: the `relativePath` we provided was just `icon.png`, but the file is actually located at `./content/assets/icon.png`. 

Gatsby was able to resolve to the file because we configured a "content root" at `./content/assets`. We could have specified the `sourceInstanceName` to remove any ambiguity as to which "content root" this file is located in. 

In fact, I'm not sure how Gatsby would behave if the same relative path existed in multiple "content roots". 

This would be a good opportunity to dig into the Gatsby's source code to understand how this all works, but I'll leave that to you!

Next up: what is `childImageSharp`? "Child" refers to this being a child node of a `File` node. "Image" is just like it sounds. "Sharp" is referring to the [Sharp](https://github.com/lovell/sharp) image processing tool and corresponding Gatsby plugin, [gatsby-plugin-sharp](https://www.gatsbyjs.com/plugins/gatsby-plugin-sharp/), which enables these image processing features.

`fixed` means we want transform the image into an image of a fixed size. We specify the dimensions by passing parameters like this: `fixed(height: 260, width: 260)`. There are a few alternatives to `fixed` which we could use, one of which we will see below.

Finally, we only need the `src` property for the purposes of the Open Graph image meta tag.

## How to Source Post-Specific Image Properties using GraphQL

Following from above, we must update the `BlogPostTemplate` component to pass the `imageUrl` and `imageAlt` props to the `SEO` component. Again, we use the `constructUrl` utility to convert the relative path, `src`, into a URL. I explain the origin of these props' values below.

```js
// util.js
export const constructUrl = (baseUrl, path) =>
  (!baseUrl || !path) ? null : `${baseUrl}${path}`;

// src/templates/blog-post.js
const BlogPostTemplate = ({ data, pageContext, location }) => { 
    // Details omitted for brevity
    return ( 
        <Layout location={location} title={data.site.siteMetadata.title}> 
            <SEO 
                title={data.markdownRemark.frontmatter.title} 
                description={data.markdownRemark.frontmatter.description || data.markdownRemark.excerpt} 
                imageUrl={
                    constructUrl(
                        data.site.siteMetadata.siteUrl, data.markdownRemark.frontmatter.image?.childImageSharp?.fixed?.src
                )} 
                imageAlt={data.markdownRemark.frontmatter.imageAlt} />
        // ...
```

Sourcing the image alt text is straightforward: we add `imageAlt` as a property to the `frontmatter` portion of our `BlogPostTemplate` component's GraphQL query. This query is exported as a GraphQL tagged template. 

The name of the exported constant is arbitrary. In my case it's `const pageQuery`. 

This query gets executed for us by Gatsby, and the results are passed to the `BlogPostTemplate` component in the `data` prop. 

This is explained in the Gatsby docs here: [Querying Data in Pages with GraphQL](https://www.gatsbyjs.com/docs/how-to/querying-data/page-query/).

In order to source the actual image, we use `childImageSharp` again but in a slightly different way than we saw above:

```js
// src/templates/blog-post.js
export const pageQuery = graphql`
    query BlogPostBySlug($slug: String!) {
      site {
        siteMetadata {
          title
          siteUrl
        }
      }
      markdownRemark(fields: {slug: {eq: $slug}}) {
        id
        excerpt(pruneLength: 160)
        html
        frontmatter {
          title
          date(formatString: "MMMM DD, YYYY")
          description
          # Add this
          image {
            childImageSharp {
              fixed(height: 600, width: 1200) {
                src
              }
              fluid(maxWidth: 700, maxHeight: 500) {
                ...GatsbyImageSharpFluid
              }
            }
          }
          # Add these
          imageAlt
          imageTitleHtml
        }
      }
    }
`;
```

Here, `image` must match the name of the property we intend to set in the post's frontmatter. And the value of this property must be a path to a file **relative to the post markdown file**. 

This is similar to what we did above using a GraphQL alias and the `file` query, but here it's implicit and being handled behind the scenes by Gatsby.

We specify the dimensions in the parameters to the `fixed` field. When choosing the dimensions, make sure any image you use is at least as big as the dimensions you specify here, and use these guideline from the [docs](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image#reference):

> Images for this Card support an aspect ratio of 2:1 with minimum dimensions of 300x157 or maximum of 4096x4096 pixels

We have also added the `fluid` property and a [GraphQL fragment](https://graphql.org/learn/queries/#fragments), `...GatsbyImageSharpFluid`, which retrieves all of the properties available on this node without having to enumerate them one by one. 

The Gatsby Image component is [designed to be used this way](https://www.gatsbyjs.com/docs/reference/built-in-components/gatsby-image/#images-that-stretch-across-a-fluid-container) in order to provide a responsive image experience using [HTML's native responsive image capabilities](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images).

## How to Add a Header Image to your Blog Post Template

With the GraphQL query updated and the results being passed to our component by Gatsby, we're ready to add the Gatsby Image import and the JSX for the header image and caption:

```js
// src/templates/blog-post.js
import Image from "gatsby-image";

// Details omitted for brevity

{data.markdownRemark.frontmatter.image?.childImageSharp?.fluid &&
    <>
        <Image
            fluid={data.markdownRemark.frontmatter.image.childImageSharp.fluid}
            alt={data.markdownRemark.frontmatter.imageAlt} 
        />
        <div
            style={{
                textAlign: "center",
                fontSize: "14px",
                lineHeight: "28px",
            }}
            dangerouslySetInnerHTML={{ 
                __html: data.markdownRemark.frontmatter.imageTitleHtml 
            }} 
        />
    	<br/>
        <br/>
    </>
}
```

If the `image` or `imageAlt` properties are not set in a post's frontmatter, it won't cause any issues. Those properties will just be `null` in the post's `data` prop, for example `data.markdownRemark.frontmatter.image` and `data.markdownRemark.frontmatter.imageAlt`. 

For that reason, I've used [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining) when passing the `imageUrl` prop to the `SEO` component: `data.markdownRemark.frontmatter.image?.childImageSharp?.fixed?.src` and when optionally adding the header image component tree: `data.markdownRemark.frontmatter.image?.childImageSharp?.fluid`.

## How to Add New Properties to a Post's Frontmatter

Now all that's left is to add the actual image file, typically in the same directory as the markdown where we want to use it. Then we add the `image`, `imageAlt`, and `imageTitleHtml` properties to the post's frontmatter. 

I've taken the suggested attribution HTML directly from [Unsplash](https://unsplash.com/) and used it for the `imageTitleHtml`.

Remember: in this case, the image path is relative to the post markdown file.

```md
--- 
title: "Working with Heterogeneous Item Collections in the DynamoDB Enhanced Client for Java" 
date: "2020-12-07T01:51:34.815Z"
description: "Working with heterogeneous item collections with the Java SDKs can be tricky. Here we see how to handle 
them with the AWS SDK v2 for Java's Enhanced Client."
image: "./kevin-mueller-gGUiw8GNIFE-unsplash.jpg"
imageAlt: "Water droplets on black background"
imageTitleHtml: '<span>Photo by <a href="https://unsplash.com/@kevinmueller?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Kevin Mueller</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>'

--- 

// Markdown here...
```

## Conclusion

That's it – you did it! We covered quite a few concepts in this article. You should now be able to add header images to your blog posts and get nice Open Graph-based preview experiences on Twitter, Facebook, Google, WhatsApp, and more.

You can find the completed code on GitHub here:

* [SEO](https://github.com/helloworldless/davidagood.com/blob/55164811e2265de754940c8432c58c2bceec8e43/src/components/seo.js)
* [BlogPostTemplate](https://github.com/helloworldless/davidagood.com/blob/55164811e2265de754940c8432c58c2bceec8e43/src/templates/blog-post.js)
* [Example post markdown](https://github.com/helloworldless/davidagood.com/blob/55164811e2265de754940c8432c58c2bceec8e43/content/blog/dynamodb-enhanced-client-java-heterogeneous-item-collections/index.md)

Once you've implemented this and deployed it, you can use the [Twitter Card Validator](https://cards-dev.twitter.com/validator) to test the behavior before actually tweeting a link.

Coincidentally, I did experience some issues with cards not being displayed in tweets even though the Validator showed that they were working. 

In one case, I tweeted a link in a reply, and there was no card at all—just the raw link. The next day, I tweeted the same link, and this time the card worked fine! 

In another case, I was looking at my Twitter Profile page, and several of my tweets had the cards but the image was not being displayed. So I opened a Chrome Incognito window, and in that window the images were displayed as expected.

