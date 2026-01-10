---
title: How to Deploy a Next.js Blog on Sevalla
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-07-09T15:43:22.921Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-nextjs-blog-on-sevalla
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752075758399/7d8a494b-a5f0-4fb7-841b-8758d1cbc94d.png
tags:
- name: Next.js
  slug: nextjs
- name: Blogging
  slug: blogging
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In this tutorial, I’ll teach you how to use Next.js and Sevalla to build
  and deploy your own Next.js blog.

  But first, let me answer your likely question: “Why host a blog yourself when there
  are hundreds of blogging platforms available? “

  One answer:...'
---

In this tutorial, I’ll teach you how to use Next.js and Sevalla to build and deploy your own Next.js blog.

But first, let me answer your likely question: “Why host a blog yourself when there are hundreds of blogging platforms available? “

One answer: [Next.js](https://nextjs.org/).

## Table of Contents

* [What is Next.js?](#heading-what-is-nextjs)
    
* [What is Sevalla?](#heading-what-is-sevalla)
    
* [Building and Deploying a Next.js Blog](#heading-building-and-deploying-a-nextjs-blog)
    
    * [Building the blog](#heading-building-the-blog)
        
    * [Deploying the blog](#heading-deploying-the-blog)
        
    * [Adding a custom domain](#heading-adding-a-custom-domain)
        
* [Conclusion](#heading-conclusion)
    

## **What is Next.js?**

![Next.js Framework](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871450742/adc4f876-dbad-41a3-b310-6c8f3e470c20.webp align="center")

Next.js is a web development framework built on top of React. While React is a library for building user interfaces, Next.js adds extra features to make building websites and web applications easier and faster.

Next.js gives you full control. You own your content, your design, and your SEO strategy. Unlike Medium or Substack, you’re not limited by platform rules or branding. You can optimise every part of your blog, from how fast it loads to how it looks on Google search.

Next.js isn’t just a tool to build a blog. It’s a platform to build your entire brand. That’s why developers and [indie hackers](https://www.indiehackers.com/post/why-next-js-is-perfect-for-saas-development-27f98e471b) love it.

## **What is Sevalla?**

[Sevalla](https://sevalla.com/) is a Platform-as-a-service provider that I have recently fallen in love with. Built by the team behind [Kinsta](https://kinsta.com/), the popular WordPress hosting platform, Sevalla combines powerful features with a smooth developer experience. They offer application hosting, database, object storage, and static site hosting for your projects.

Unlike platforms like Heroku, which provide almost all features via additional integrations, Sevalla gives you exactly what you need to build and deploy an app to your users.

![Sevalla Admin Panel](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871511816/7de2c52f-da06-4891-a62d-dad4eb4ca57a.webp align="center")

Imagine if someone took just the essential features from cloud platforms like AWS or Azure and put them into a single, easy-to-use dashboard. That’s exactly what the Sevalla admin panel has. A clean, simple interface with everything you need, and nothing you don’t.

In a nutshell, Sevalla handles all the heavy lifting of deploying and scaling your app, so you can focus entirely on building it.

## **Building and Deploying a Next.js Blog**

Now let’s build and deploy our Next.js blog. We don't have to build one from scratch – there are many templates available for us to use, [like this one](https://github.com/sevalla-templates/nextjs-blog).

We will do three things.

* Clone the repository and set up the blog on our local machine.
    
* Deploy the site to Sevalla
    
* Add a custom domain.
    

### Building the blog

First, fork the Next.js blog repository.

![Fork Repository](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871568856/84bb32da-25b9-4a0b-8170-658914a643fe.webp align="center")

Once you have forked it, clone it to your local machine.

![Clone repository](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871607179/716dfc07-d0c8-4ab5-9c45-8ee72fca3f09.webp align="center")

```plaintext
git clone <repository url>
```

Once you have cloned the repository, go into the directory and run `npm install` . Make sure you have the latest [Node.js](https://nodejs.org/en) and Next.js installed on your machine.

Now let’s run the blog on our machine. The command is `npm run dev` . Once the server is running, go to `localhost:3000` to view the site.

![Demo Next.js blog](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871654364/b738b6f7-b272-4b75-bf5b-b2af40ccd035.webp align="center")

You should see the above page. Now let's add our own blog post to it. Go to the `content/blog` directory. Every page in the content directory is your blog post, and you can use [Markdown](https://www.markdownguide.org/basic-syntax/) to style it. Save the file with the extension `.mdx`

Add the following text (the first part is the metadata for the blog to understand the title and date of publication):

```plaintext
---
title: "My New Post"
date: 2025-07-07
---

Welcome to my first blog post using Next.js and MDX!
```

Reload the home page, and you should now see two posts – the default post and your new post.

![New post in Next.js blog](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871689247/e3ec1407-33d7-4c9c-9032-3e2e36b189a7.webp align="center")

So every time you want to publish a new article, you create a new page using Markdown. It's that simple.

Commit this new file and push it to your repository.

```plaintext
git add .
git commit -m "new post"
git push origin main
```

### Deploying the blog

Now create an account on Sevalla (use GitHub login so that you don't have to re-authenticate again).

Once you log in to Sevalla, you’ll see the Static site option. Click on it to create a static site.

Like other hosting providers, not all Sevalla products are free, but it comes with generous free credits. Unless you have a reasonable number of users that access your blog, you will not incur any costs for blogs/small projects. But when it comes to static sites, you can host up to 100 sites completely for free.

![Sevalla Dashboard](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871726773/aaee5778-f9c8-4454-9349-154aa4d291d3.webp align="center")

Select the repository from the list. Check the “Automatic deploy on commit” option. So every time you push code, Sevalla will automatically deploy your new post to the server.

![Create Static Site](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871773521/44aafcba-a5cf-4017-b28e-f3271414f8c8.webp align="center")

In the “build settings” page, keep the defaults. Click “Create site”. In a few minutes, the app will be pulled from GitHub, deployed to a server, and you should see the button `visit site` .

![Deployment success](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871809727/1658eca6-9f0e-4a7d-94c8-4519491940be.webp align="center")

If you visit the site, you should see the below page:

![Live blog](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871841987/f9e9784a-bcac-4265-b060-2894fcc7fb16.webp align="center")

Yay! Your blog is live. You can also see detailed build logs under the “deployments” tab and see if there are any issues deploying your app.

![Sevalla Deployment Logs](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871895728/00d0c956-991b-42e1-bafe-1bde592009f2.webp align="center")

### Adding a custom domain

Great. For the last step, let's add a custom domain to our blog.

Go to the “domains” tab, and click “add domain” under custom domains. I'll be using a subdomain `next` from my private domain [`manishshivanandhan.com`](http://manishshivanandhan.com), but the instructions are the same for root domains as well.

![Add custom domain](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871942423/faba7435-4f1e-4565-8f41-ac9f41257532.webp align="center")

Once you click “add domain”, Sevalla will give you the instructions to add the TXT records for verification and CNAME/A records for pointing the new site to your domain.

Once these are done on your domain provider, check back after a few minutes.

![Custom Domain Verified](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871974507/fbf19bd2-b862-4bab-bd0b-ff2d83e133eb.webp align="center")

Hooray! You’ve created your own Next.js blog. Here is the sample site I built for this project – [http://next.manishshivanandhan.com](http://next.manishshivanandhan.com/)

## **Conclusion**

And that’s it! Your very own Next.js blog is now live on Sevalla.

In just a short time, you’ve gone from cloning a template to publishing your first post and deploying it to the world with a custom domain. With Next.js, you get full control over your content and brand, and with Sevalla, deployment becomes effortless and smooth.

Remember, every time you want to publish a new article, all it takes is creating a simple markdown file and pushing your code. Sevalla handles the rest, so you can focus on what truly matters: writing great content and building your personal brand.

Hope you enjoyed this article! I’ll be back soon with more tutorials on building with Next.js. Feel free to [connect with me on LinkedIn](https://www.linkedin.com/in/manishmshiva/) to stay in touch.
