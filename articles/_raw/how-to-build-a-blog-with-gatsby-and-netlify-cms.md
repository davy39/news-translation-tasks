---
title: How to Build a Blog with Gatsby and Netlify CMS – A Complete Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-06T15:16:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-blog-with-gatsby-and-netlify-cms
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c984e740569d1a4ca1946.jpg
tags:
- name: blog
  slug: blog
- name: cms
  slug: cms
- name: Gatsby
  slug: gatsby
- name: Netlify
  slug: netlify
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mohammed Asker

  In this article, we are going to build a blog with Gatsby and Netlify CMS. You will
  learn how to install Gatsby on your computer and use it to quickly develop a super
  fast blog site.

  You are also going to learn how to add Netlify CM...'
---

By Mohammed Asker

In this article, we are going to build a blog with Gatsby and Netlify CMS. You will learn how to install Gatsby on your computer and use it to quickly develop a super fast blog site.

You are also going to learn how to add Netlify CMS to your site by creating and configuring files, then connecting the CMS to your site through user authentication. 

And finally, you'll learn how to access the CMS admin so that you can write your first blog post.

The complete code for this project can be found [here](https://github.com/mohammedasker/foodblog).

Here's a brief introduction to these tools.

## What is Gatsby?

[Gatsby](https://www.gatsbyjs.com/) is a free and open-source framework based on React that helps you build fast websites and web apps. It is also a static site generator like Next.js, Hugo, and Jekyll.

It includes SEO (Search Engine Optimization), accessibility, and performance optimization from the get-go. This means that it will take you less time to build production-ready web apps than if you were building with React alone.

## What is Netlify CMS?

[Netlify CMS](https://www.netlifycms.org/) is a CMS (Content Management System) for static site generators. It is built by the same people who made [Netlify](https://www.netlify.com/). It allows you to create and edit content as if it was WordPress, but it's a much simpler and user-friendly interface.

The main benefit of Netlify CMS is you don't have to create markdown files every time you want to write a post. This is useful for content writers who don't want to deal with code, text editors, repositories, and anything to do with tech - they can just focus on writing articles.

Alright, without any further ado, let's start building the blog!

**But before we get going, a quick heads up**: This guide requires prior knowledge of JavaScript and React. If you are not comfortable with these tools yet, I've linked the resources at the end of the article to help you brush up on those skills. 

Even if you're new to those technologies, I tried to make this guide as simple as I was able so you can follow along.

## How to set up the environment

Before we can build Gatsby sites, we have to make sure that we have installed all the right software required for the blog.

### Install Node.js

Node.js is an environment that can run JavaScript code outside of a web browser.

It is a tool that allows you to write backend server code instead of using other programming languages such as Python, Java, or PHP. Gatsby is built with Node.js and that's why we need to install it on our computer.

To install Node.js, go to the [download page](https://nodejs.org/en/download/) and download it based on your operating system. 

When you are done following the installation prompts, open the terminal and run `node -v` to check if it was installed correctly. Currently, the version should be 12.18.4 and above.

### Install Git

Git is a free and open-source distributed version control system that helps you manage your coding projects efficiently. 

Gatsby starter uses Git to download and install its required files and that's why you need to have Git on your computer.

To install Git, follow the instructions based on your operating system:

* [Install Git on Mac OS](https://www.atlassian.com/git/tutorials/install-git#mac-os-x)
* [Install Git on Windows](https://www.atlassian.com/git/tutorials/install-git#windows)
* [Install Git on Linux](https://www.atlassian.com/git/tutorials/install-git#linux)

### Install Gatsby CLI

Gatsby CLI (Command Line Interface) is the tool that lets you build Gatsby-powered sites. By running this command, we can install any Gatsby sites and the plugins we want.

To install Gatsby CLI, open the terminal and run this command:

```
npm install -g gatsby-cli

```

Once everything is set up successfully then we are ready to build our first Gatsby site.

## How to build a Gatsby site

In this guide, we're going to use the default Gatsby starter theme, but you're free to choose any themes on the [Gatsby starter library](https://www.gatsbyjs.com/starters/?v=2). I personally use the [Lekoart theme](https://github.com/LekoArts/gatsby-starter-minimal-blog) because the design is minimalist and beautiful, and it has a dark mode.

In the terminal, run this command to install the new Gatsby blog:

```
gatsby new foodblog https://github.com/gatsbyjs/gatsby-starter-blog

```

**Note for Windows users**: If you encounter "Error: Command failed with exit code 1: yarnpkg" while creating Gatsby site, see [this page](https://github.com/gatsbyjs/gatsby/issues/26804) to troubleshoot it. You may have to clean up dependencies of old yarn installations or follow the Gatsby on Windows instructions.

What's does this command line mean exactly? Let me explain.

* **new** - This is the command line that creates a new Gatsby project
* **foodblog** - This is the name of the project. You can name it whatever you want here. I named this project _foodblog_ as an example only.
* **The URL** ([https://github.com/gatsbyjs/gatsby-starter-blog](https://github.com/gatsbyjs/gatsby-starter-blog)) - This URL specified points to a code repository that holds the starter code you want to use. In other words, I picked the theme for the project.

Once the installation is complete, we'll run the `cd foodblog` command which will take us to the location of our project file.

```
cd foodblog

```

Then we'll run `gatsby develop` that will start running on the local machine. Depending on the specs of your computer, it will take a little while before it is fully started.

```
gatsby develop

```

Open a new tab in your browser and go to `http://localhost:8000/`. You should now see your new Gatsby site!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--33-.png)
_How a Gatsby starter blog homepage looks_

Now that we've created the blog, the next step is to add Netlify CMS to make writing blog posts easier.

## How to add Netlify CMS to your site

Adding Netlify CMS to your Gatsby site involves 4 major steps:

* app file structure, 
* configuration, 
* authentication, and 
* accessing the CMS.

Let's tackle each of these stages one at a time.

### How to set up the app's file structure

This section deals with the file structure of your project. We are going to create files that will contain all Netlify CMS codes.

When you open your text editor, you will see a lot of files. You can read [this article](https://github.com/gatsbyjs/gatsby-starter-blog#-whats-inside) if you are curious about what each of these files does.

```
├── node_modules
├── src
├── static
├── .gitignore
├── .prettierrc
├── gatsby-browser.js
├── gatsby-config.js
├── gatsby-node.js
├── gatsby-ssr.js
├── LICENSE
├── package-lock.json
├── package.json
└── README.md

```

Do not worry about all these files — we are going to use very few of them here. 

What we are looking for is the `static` folder. This is the folder where it will form the main structure of the Netlify CMS. 

If your project does not have `Static` folder, then create the folder at the root directory of your project.

Inside the `static` folder, create an `admin` folder. Inside this folder, create two files `index.html` and `config.yml`:

```
admin
 ├ index.html
 └ config.yml

```

The first file, `index.html`, is the entry point to your CMS admin. This is where Netlify CMS lives. You don't need to do styling or anything as it is already done for you with the script tag in the example below:

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Content Manager</title>
</head>
<body>
  <script src="https://unpkg.com/netlify-cms@^2.0.0/dist/netlify-cms.js"></script>
</body>
</html>

```

The second file, `config.yml`, is the main core of the Netlify CMS. It's going to be a bit complicated as we are going to write backend code. We'll talk more about it in the configuration section.

### How to configure the back end

In this guide, we are using Netlify for hosting and authentication and so the backend configuration process should be relatively straightforward. Add all the code snippets in this section to your `admin/config.yml` file.

We'll begin by adding the following codes:

```yml
backend:
  name: git-gateway
  branch: master

```

**Heads up**: This code above works for GitHub and GitLab repositories. If you're using Bitbucket to host your repository, follow these [instructions](https://www.netlifycms.org/docs/bitbucket-backend/) instead.

The code we just wrote specifies your backend protocol and your publication branch (which is branch: master). Git Gateway is an open-source API that acts as a proxy between authenticated users of your site and your site repository. I'll explain more what this does in the authentication section.

Next up, we will write `media_folder: "images/uploads"`. This will allow you to add media files like photos directly to your CMS. Then you won't need to use a text editor to manually add media and all that.

```yml
media_folder: "images/uploads"

```

Make sure you created a folder called `images` in the `admin` folder. Inside the `images` folder, create an `uploads` folder as this is the place where you'll host your images.

### Configure Collections

The collections will define the structure for the different content types on your static site. As every site can be different, how you configure the collection's settings will differ from one site to another.

Let's just say your site has a blog, with the posts stored in `content/blog`, and files saved in a date-title format, like `2020-09-26-how-to-make-sandwiches-like-a-pro.md`. Each post begins with settings in the YAML-formatted front matter in this way:

```md
---
layout: blog
title: "How to make sandwiches like a pro"
date: 2020-09-26 11:59:59
thumbnail: "/images/sandwich.jpg"
---

This is the post body where I write about how to make a sandwich so good that will impress Gordon Ramsay.

```

With this example above, this is how you will add `collections` settings to your Netlify CMS `config.yml` file:

```yml
collections:
  - name: "blog"
    label: "Blog"
    folder: "content/blog"
    create: true
    slug: "{{year}}-{{month}}-{{day}}-{{slug}}"
    fields:
      - {label: "Layout", name: "layout", widget: "hidden", default: "blog"}
      - {label: "Title", name: "title", widget: "string"}
      - {label: "Publish Date", name: "date", widget: "datetime"}
      - {label: "Body", name: "body", widget: "markdown"}

```

Let's examine what each of these fields does:

* `name`:  This one is used in routes like /admin/collections/blog
* `label`: This one is used in the UI (User Interface). When you are in the admin page, you will see a big word "Blog" on the top of the screen. That big word "Blog" is the label.
* `folder`: This one points to the file path where your blog posts are stored.
* `create`: This one lets the user (you or whoever has admin access) create new documents (blog posts in this case) in these collections.
* `slug`: This one is the template for filenames. `{{year}}`, `{{month}}`, and `{{day}}` which are pulled from the post's date field or save date. `{{slug}}` is a URL-safe version of the post's title. By default it is `{{slug}}`.

The fields are where you can customize the content editor (the page where you write the blog post). You can add stuff like ratings (1-5), featured images, meta descriptions, and so on.

For instance, in this particular code, we add curly braces `{}`. Inside them we write `label` with the value "Publish Date" which will be the label in the editor UI. 

The `name` field is the name of the field in the front matter and we name it "date" since the purpose of this field is to enter the date input.

And lastly, the widget determines how the UI style will look and the type of data we can enter. In this case, we wrote `"datetime"` which means we can only enter the date and time.

```yml
- {label: "Publish Date", name: "date", widget: "datetime"}

```

You can check the list right [here](https://www.netlifycms.org/docs/widgets/) to see what exactly you can add. If you want, you can even create your own widgets, too. For the sake of brevity, we'll try to keep things simple here.

### Enable Authentication

At this point, we are nearly done with the installation and configuration of Netlify CMS. Now it's time to connect your Gatsby site to the CMS by enabling authentication. 

We'll add some HTML code and then activate some features from Netlify. After that, you are on the way to creating your first blog post.

We are going to need a way to connect a front end interface to the backend so that we can handle authentication. To do that, add this HTML script tag to two files:

```html
<script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>

```

The first file to add this script tag is the `admin/index.html` file. Place it between the `<head>` tags. And the second file to add the tag is the `public/index.html` file. This one also goes in between the `<head>` tags.

When a user logs in with the Netlify Identity widget, an access token directs them to the site homepage. In order to complete the login and get back to the CMS, redirect the user back to the `/admin/` path.

To do this, add the following code before the closing `body` tag of the `public/index.html` file:

```html
<script>
  if (window.netlifyIdentity) {
    window.netlifyIdentity.on("init", user => {
      if (!user) {
        window.netlifyIdentity.on("login", () => {
          document.location.href = "/admin/";
        });
      }
    });
  }
</script>

```

With this, we are now done writing the code and it's time to visit Netlify to activate authentication.

Before we move on, you should Git commit your changes and push them to the repository. Plus, you will have to deploy your site live so you can access the features in the Enable Identity and Git Gateway section.

## Deploy your site live with Netlify

We are going to use Netlify to deploy our Gatsby site live. The deployment process is pretty straightforward, quick, and most importantly, it comes with a free SSL (Secure Sockets Layer). This means your site is protected (you can tell by looking at the green lock on the browser search).

If you haven't signed up for the platform, you can do it [right here](https://app.netlify.com/signup?_ga=2.69477016.986166254.1601369549-1254573554.1571849986). When you've finished signing up, you can begin the deployment process by following these 3 steps.

1. Click the "New site from Git" button to create a new site to be deployed. Choose the Git provider where your site is hosted. My site is hosted on GitHub so that's what I will choose.
2. Choose the repository you want to connect to Netlify. The name of my Gatsby site is "foodblog" but you have to pick your own project name.
3. The last one asks how you would like Netlify to adjust your builds and deploy your site. We are going to leave everything as it is and we will click the "Deploy site" button. This will begin deploying your site to live.

Once the deployment is complete, you can visit your live site by clicking the green link that has been generated for you on the top left of the screen. Example: `https://random_characters.netlify.app`.

With this, the world can now view your site. You can replace the weird URL with your custom domain by reading this [documentation](https://docs.netlify.com/domains-https/custom-domains/#definitions).

### How to enable Identity and Git Gateway

Netlify's Identity and Git Gateway services help you manage CMS admin users for your site without needing them to have an account with your Git host (Like GitHub) or commit access on your repository.

To activate these services, head to your site dashboard on Netlify and follow these steps:

1. Go to **Settings** > **Identity**, and select **Enable Identity** service.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--34-.png)
_In the Overview page of your site, click the "Settings" link._

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--36-.png)
_After clicking "Settings", scroll down the left sidebar and click the "Identity" link._

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--37-.png)
_Click the "Enable Identity" button to activate the Identity feature._

2. Under **Registration** preferences, select **Open** or **Invite only**. Most of the time, you want only invited users to access your CMS. But if you are just experimenting, you can leave it open for convenience.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--38-.png)
_Under the Identity submenu, click the "Registration" link and you'll be taken to the registration preferences._

3. Scroll down to **Services** > **Git Gateway**, and click **Enable Git Gateway**. This authenticates with your Git host and generates an API access token. 

In this case, we're leaving the **Roles** field blank, which means any logged-in user may access the CMS.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--40-.png)
_Under the Identity submenu, click the "Services" link._

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--41-.png)
_Click the "Enable Git Gateway" button to activate the Git Gateway feature._

With this, your Gatsby site has been connected with Netlify CMS. All that is left is to access the CMS admin and write blog posts.

## How to access the CMS

All right, you are now ready to write your first blog post!

There are two ways to access your CMS admin, depending on what accessing options you chose from the Identity.

If you selected **Invite only**, you can invite yourself and other users by clicking the Invite user button. Then an email message will be sent with an invitation link to login to your CMS admin. Click the confirmation link and you'll be taken to the login page.

Alternatively, if you selected **Open**, you can access your site's CMS directly at `yoursite.com/admin/`. You will be prompted to create a new account. When you submit it, a confirmation link will be sent to your email. Click the confirmation link to complete the signup process and you'll be taken to the CMS page.

**Note**: If you cannot access your CMS admin after clicking the link from the email, the solution is to copy the link in the browser starting with `#confirmation_token=random_characters` and paste the link after the hashtag "#", like this: `https://yoursite.com/admin/#confirmation_token=random_characters`. This should fix the problem.

If everything goes well, you should see your site's admin dashboard:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot--42-.png)
_Netlify CMS admin._

You can create your new post by clicking the "New post" button.

When you're ready to publish your post, you can click the "Publish Now" button to publish it immediately.

When you hit the publish button, the post file is automatically created. Then it will add to the changes with the commit message based on the name of the post along with the date and time of publishing. Finally, it will be pushed to the host repository, and from there your post will be seen live.

You can view the changes by looking at the commit message in your host repository.

After waiting for a few minutes, your new post should be live.

### One more thing

The last thing to do is clean up the sample articles. To delete these posts, go to the blog files in your text editor and delete them one by one. Make sure you check your terminal when deleting them so that there will be no issues on your site.

Once all the sample posts are cleared out, commit these changes and push them to the repository.

And now, you are all done! You can now create your new posts from the comfortable CMS dashboard and share your stories to the world.

## Summary

In this guide you have learned how to:

* Create a Gatsby blog site
* Added the Netlify CMS to your Gatsby site by creating and configuring files
* Enable user authentication by activating Identity and Git Gateway
* Access your site's CMS admin
* Publish your first post powered by Gatsby and Netlify CMS

By the end of this guide, you should now be able to enjoy writing blog posts with a fast website and simple content editor. And you probably don't have to touch the code unless it needs further customization.

There is still more to cover about Gatsby and Netlify CMS. One of the best ways to learn about them is to go through their documentation.

I hope you found this guide beneficial, and happy posting!

[Check out my blog](https://www.mohammedasker.com/) to learn more tips, tricks, and tutorials about web development.

Cover photo by [NeONBRAND](https://unsplash.com/@neonbrand?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/blogging?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

### Resources for JavaScript and React

Here are some resources that may help you to learn JavaScript and React:

**JavaScript**

* [Official JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [freeCodeCamp](https://www.freecodecamp.org/)
* [W3Schools: JavaScript Tutorial](https://www.w3schools.com/js/)
* [JavaScript.info](https://javascript.info/)

**React**

* [Official React Documentation](https://reactjs.org/docs/getting-started.html)
* [Complete React Developer in 2020 (w/ Redux, Hooks, GraphQL)](https://www.udemy.com/course/complete-react-developer-zero-to-mastery/)
* [Scrimba: Learn React for free](https://scrimba.com/learn/learnreact)
* [Flavio Copes: The React Handbook](https://flaviocopes.com/page/react-handbook/)

