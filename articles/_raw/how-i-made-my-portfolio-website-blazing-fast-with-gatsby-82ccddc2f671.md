---
title: How I made my portfolio website blazing fast with Gatsby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T19:25:48.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-my-portfolio-website-blazing-fast-with-gatsby-82ccddc2f671
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lJOurCBMozvgBjmxG-Ljiw.jpeg
tags:
- name: GatsbyJS
  slug: gatsbyjs
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: Web Hosting
  slug: web-hosting
seo_title: null
seo_desc: "By Maribel Duran\nIf you are thinking of building a static site with React\
  \ and want it to perform as fast as a cheetah, you should consider using GatsbyJS.\
  \ \nI decided to try it out and was amazed with how easy it was to setup, deploy,\
  \ and how fast the..."
---

By Maribel Duran

If you are thinking of building a static site with React and want it to perform as fast as a cheetah, you should consider using GatsbyJS. 

I decided to try it out and was amazed with how easy it was to setup, deploy, and how fast the site loads now. Gatsby uses the best parts of other front end tools to make the development experience feel like you’re on vacation.

![Image](https://cdn-media-1.freecodecamp.org/images/drwxddrKcWMNLOQ0Vc0Th9-DH2BAtln6DfzA)
_After rebuilding my website with Gatsby and React ?_

### **Performance Issues With Original Website**

I had been meaning to optimize the images on my portfolio website, which was one of my first freeCodeCamp Frontend Development projects.

![Image](https://cdn-media-1.freecodecamp.org/images/ZAKgKErGeMpDsVyLQi9MUYZeV6nchQeK95Z3)
_Before the help of Gatsby -_-_

Ouch! A 33/100 Google optimization score was painful to see. Yup I needed some help from the optimization gods. My website contained at least 17 project screenshots. I didn’t want to have to compress each image, generate multiple sizes and resolutions of each image, and lazy-load them.

When I first created this website, the Bootstrap 3 `img-responsive` class took care of scaling the images to fit different screen sizes, but I didn’t think about the fact that it was still loading some of my screenshots that were around 1400 x 860 pixels on mobile devices!

My score was also low because I had not minified my CSS or setup browser caching for it, and was not async loading external CSS resources.

### **Gatsby To The Rescue**

I really wanted to rebuild this project using React. I could have used [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html) which provides an out-of-the box build script and development server, but this still didn’t take care of the long task of having to crop different image sizes for all of my images.

Fortunately I was listening to [Syntax’s](https://syntax.fm/), “Why Static Site Generators are Awesome” [episode](https://syntax.fm/show/034/why-static-site-generators-are-awesome), and they talked about a few static site generators on the [StaticGen.com](https://www.staticgen.com/) list. If you haven’t heard what static site generators do, they transform your site into a directory with a single HTML file and static assets. No database or server code needed.

Gatsby won me over due to the similarities it has with create-react-app, which includes hot reloading, easy dev environment setup, and a build script. Gatsby takes it further by offering server-side rendering, smart image loading, and dedication to performance.

Since Gatsby is built on the React, GraphQL, and Webpack stack, we can write our content as React components! Winning! Gatsby takes care of rendering at build time to the DOM as static HTML, CSS, and JavaScript.

### Gatsby-image Component is BAE

So now to what I’ve really been wanting to share with you. Gatsby-image! [Gatsby-image](https://www.gatsbyjs.org/packages/gatsby-image/), is a React component that was designed to work with Gatsby’s GraphQL queries to completely optimize image loading for sites.

The approach is to use GraphQL queries to get images of the optimal size and then display them with the gatsby-image component.

How did I use this component to automatically create 3 thumbnails for each of my 17 project images? Magic! Not really, but it feels like it!

In my src/pages/index.js file, I queried all of the project images and gave it an alias of **ProjectImgs.** Since the queried data is now accessible through the data object as a prop, I was able to pass the **projectImgData** data (which is a node list of my project images) to my `<Projects />` component:

```
//imports
const HomePage = ({ data }) => {
  const siteTitle = data.site.siteMetadata.title;
  console.log(data.ProjectImgs); 
  const { edges: projectImgData } = data.ProjectImgs;
  const { edges: iconImgData } = data.iconImgs;
  return (
    <div>
     <Helmet
      title={siteTitle}
      link={[{ rel: "icon", type: "image/png", href: `${favicon}`}]}
     />
     <Cover coverImg={data.coverImg} />
     <div className="container-fluid main">
      <Navigation />
      <AboutMe profileImg={data.profileImg} iconImgs={iconImgData} 
      />                
     <Projects projectImgs={projectImgData} />
     <Contacts />
     <Footer />
     </div>
    </div>
  );
};
export const query = graphql`
  query allImgsQuery {
    //additional queries
    ...
    ProjectImgs: allFile(
      sort: { order: ASC, fields: [absolutePath] }
      filter: { relativePath: { regex: "/projects/.*.png/" } }
    ) {
      edges {
        node {
          relativePath
          name
          childImageSharp {
            sizes(maxWidth: 320) {
              ...GatsbyImageSharpSizes
            }
          }
        }
      }
    }
//additional queries
...
  }
`;
```

> Note: I had some trouble getting my graphQL queries to work and had to do a little digging around to figure out how to query for multiple images within a folder. What helped me was looking at other portfolio sites made with Gatsby.

Using the console, we can see what `data.ProjectImgs` returns to give you a better idea of what I am receiving from the query and what I am passing to my Projects component:

`Console.log(data.ProjectImgs)` returns an array of edges:

```
{edges: Array(17)}
edges
:
(17) [{…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}]
__proto__
:
Object{edges: Array(17)}
```

Extending one of the edges shows a node object that contains a **childImageSharp** property. This contains a sizes object which holds the image’s thumbnail sources. This sizes object is what we ultimately want to pass to our gatsby-image’s `<Img />` component.

Extending an edge to show the information in a node:

```
{edges: Array(17)}
 edges: Array(17)
 0:
  node:
   childImageSharp: {sizes: {…}}
   name: "CamperLeaderboard"
   relativePath:"projects/CamperLeaderboard.png"
   __proto__:Object
   __proto__:Object
 1:{node: {…}}
//more nodes
...
```

In my `<Projects />` component, I receive the node list of project images as a prop and for each project, I extract the **childImageSharp.sizes** object (which is renamed to **imageSizes**), and pass it into the gatsby-image’s `<Img />` component:

```
import React, { Component } from "react";
import Img from "gatsby-image";
//more imports
...
class Projects extends Component {
  constructor(props) {
    super(props);
  this.state = {
      selectedType: "front-end"
   };
  this.onSelectChange = this.onSelectChange.bind(this);
  }
 
  onSelectChange(e) {
    this.setState({ selectedType: e.target.value });
 }
render() {
    const projectImgs = this.props.projectImgs;
    const { selectedType } = this.state;
    return (
      <section id="projects" className="section projects">
        <h2 className="text-center">PROJECTS</h2>
        <div className="section-content">
          <div className="subheader">
            <FormGroup controlId="formControlsSelect">
             ...
            </FormGroup>
          </div>
          <div className="project-list">
            {projectList.map(project => {
              const isSelectedType = selectedType === project.type;
              const singleCardClass = classNames("single-card", {
                hide: !isSelectedType
               });
              const image = projectImgs.find(n => {
                return n.node.relativePath === 
                       `projects/${project.img}`;       
              });
              const imageSizes = image.node.childImageSharp.sizes;
              return (
                <a
                  href={project.url}
                  key={project.url}
                  className={singleCardClass}
                  target="_blank"
                >
                  <div className="card-img">
                    <Img
                      title={project.name}
                      alt="Screenshot of Project"
                      sizes={imageSizes}
                      className="card-img_src center-block"
                    />
                  </div>
                  <div className="blue-divider" />
                  <div className="card-info">
                    <h4 className="card-name">{project.name}</h4>
                    <p>{project.description}</p>
                  </div>
                </a>
              );
            })}
          </div>
        </div>
      </section>
    );
  }
}
export default Projects;
```

And this is the end result:

![Image](https://cdn-media-1.freecodecamp.org/images/01dWYR9uwENmj6xQcoA-5uhSqdXywSDUMCyH)
_Example of lazy loading and blur effect using gatsby-image in a slow 3G network_

That’s it! The `<Img />` component takes care of using the correct image size, creating the blur up effects, and lazy loading my project images, since they are located further down the screen. The above querying was a bit more complex than querying a single image.

If you’re new to GraphQL, below are a few resources that better explain how to use GraphQL queries and the gatsby-image component:

* [Working with Images in Gatsby](https://www.gatsbyjs.org/docs/working-with-images/)
* [gatsby-image](https://www.gatsbyjs.org/packages/gatsby-image/)
* [Image Optimization Made Easy with Gatsby.js](https://medium.com/@kyle.robert.gill/ridiculously-easy-image-optimization-with-gatsby-js-59d48e15db6e)

### **Hosting To Netlify Was a Breeze**

Since Gatsby generates static files, you can pretty much use any hosting provider. I decided to change my hosting provider from Github Pages to Netlify. I had been hearing about how easy it is to deploy a website to Netlify and they were not lying. Their free tier provides awesome features that makes the deployment process and making a website secure a breeze. It provides one click HTTPS, global CDN, continuous deployment, and the list goes on.

The setup process was so simple. I logged into Netlify, clicked the “New site from Git” button on my dashboard, and chose the Git repository for this project. I configured the site to deploy from master and clicked “Deploy Site”. That was it! Netlify takes care of the build process and publishes it to the web.

As I mentioned, Netlify offers continuous deployment, so now whenever I push changes to my master branch on GitHub, this automatically triggers a new build on Netlify. Once the build is complete, my changes will be live on the web.

![Image](https://cdn-media-1.freecodecamp.org/images/sslrobbMI6Gv3V0fhuG0AQyX6wpBjKY9Fmqy)
_Deployment setting is set to auto publishing_

### **The Future Looks Bright**

By rebuilding my website with Gatsby, not only did I learn about the different image optimization techniques for future projects, I also learned a bit about GraphQL, practiced my React skills, and took the opportunity to try out a new hosting provider.

I am really excited for the future of Gatsby and similar front end tools that remove the complexities of configuring environments and build tools. Instead, we can focus our energy and time on our code to build awesome stuff for our users.

> If you liked this article, click the? below so other people will see it here on Medium.  
>   
> Let’s be friends on [Twitter](https://twitter.com/maribeldotduran). Happy Coding :)

