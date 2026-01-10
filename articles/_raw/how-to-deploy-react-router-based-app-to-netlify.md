---
title: How to Deploy a React Router-Based Application to Netlify
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-04-19T21:38:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-react-router-based-app-to-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/routing.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Netlify
  slug: netlify
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: null
seo_desc: 'In this article, we''ll learn the most popular ways of deploying a React
  app to Netlify. We''ll also learn the configuration changes you''ll need to make
  to deploy a Routing-based React app.

  The thing I love about Netlify is that it provides a lot of us...'
---

In this article, we'll learn the most popular ways of deploying a React app to Netlify. We'll also learn the configuration changes you'll need to make to deploy a Routing-based React app.

The thing I love about [Netlify](https://www.netlify.com/) is that it provides a lot of useful features  
for free such as:

* A way to deploy a static website within seconds
* Continuous deployment, which means when you connect your Github/Gitlab/Bitbucket repository, it automatically triggers deployment when new commits are pushed to the repository
* Assurance that your website never goes down, even during new deployments
* Allows you to easily rollback to any previous working version of your site with a single click
* Lets you quickly preview any of the previously deployed versions of the app
* Change the domain or subdomain of your site instantly 

and much more.

So let's see how to deploy a React app to Netlify.

> Want to learn Redux from the absolute beginning and build a food ordering app from scratch? Check out the [Mastering Redux](https://master-redux.yogeshchavan.dev/) course.

## Drag and Drop the Build Folder in Netlify

The fastest and easy way to deploy a React application is just to drag and drop the build folder in Netlify.

To create a build folder, just execute the `npm run build` or `yarn build` command from the command line from your project folder.

Once the build folder is created, you just need to drop the folder in the drop area under the `sites` menu, as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/drag_drop.gif)

## How to Deploy an App to Netlify from a GitHub Repository

This is my favorite way of deploying applications on Netlify.

Because whenever you push any changes to the GitHub repository, it will automatically be deployed to Netlify. You can also see all deployed versions and easily roll back to any previously working version of code with just a single click.

If you already have a repository pushed to GitHub, then you just need to connect it.

Login to your Netlify account. In the dashboard, click on the `New site from Git` button.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/netlify_home.png)

Click on the `GitHub` button to connect your GitHub repository.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/git_provider.png)

It will open a new tab. Make sure the popup is enabled in your browser.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/select_repository.png)

Search for the GitHub repository in the `Search repos` search box. If your repository is not getting displayed then click on the `Configure the Netlify app on GitHub` button at the bottom of the page.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/configure_netlify.png)

Once clicked, scroll down on the page and click on the `Select repositories` dropdown and search for your repository and click on the `Save` button.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/select_repo.png)

You will be redirected to the previous page showing all the available repositories.

Search for the repository you want to deploy. For this article, I have selected the [react-book-management-app](https://github.com/myogeshchavan97/react-book-management-app) repository which we created in my [previous article](https://www.freecodecamp.org/news/react-crud-app-how-to-create-a-book-management-app-from-scratch/).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/find_repository-1.png)

Once you select the repository, you will see the following screen:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/deploy_repository.png)

For this application, we don't need to change anything.

Your `Build command` and `Publish directory` will be automatically populated. Make sure to enter these fields if you have a different command in `package.json` to build your app or those fields are not auto-populated. 

Now, click on the `Deploy site` button. Once clicked, you will see the `Site deploy in progress` message.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/deploying.png)

You'll have to wait a little bit while it's deploying. Once deployment is completed, you will see the following screen:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/deployed.png)

Open the link in the new tab and you will see your application deployed live.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/deployed_app.gif)

Awesome! Now, if you make any changes in the source code and push that change to GitHub, Netlify will detect that change and re-deploy your application with your latest changes.

If you check the application, you will see that the application works just fine with the navigation and you're able to add/edit/delete a book.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/working_app.gif)

**But there is one issue.** If you directly access the `/add` route or refresh the `/add` route page, you will get a page not found error as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/page_not_found.gif)

You will get the same error if you try to refresh the edit page route.

This is because when we access any route on our local machine, React Router handles the routing. But when we deploy the application on any server, directly accessing the route will send the request to the server itself (Netlify in our case).

But as there is no `/add` route handler on the server-side, you will see a page not found error. But Netlify provides a way to fix this.

Create a new file with the name `_redirects` inside the `public` folder of our project and add the following contents inside it:

```js
/* /index.html 200

```

Here, we're telling Netlify to redirect all the routes to the `index.html` file. 

The `index.html` file contains our entire React app code. It gets generated inside the `build` folder when the `yarn build` command is executed by Netlify while deploying the app.

And as routing is handled by our React app which is contained in the `index.html` file, our application will work without a page not found issue.

Now, push the changes to the GitHub repository so Netlify will deploy the app again with these changes.

And once deployed, if you check the deployed application, you will see that the application works fine and we don't get a page not found error.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/no_page_not_found.gif)

That's it! We're all done with deploying our application to Netlify.

## How to Easily Change a Site Name in Netlify

If you check the name of the deployed site you will see that it's not easy to remember, especially if you have lot of applications deployed. But Netlify provides a way to easily change that.

Click on the `Site settings` button displayed on the `Site overview` section.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/site_settings.png)

Then click on the `Change site name` button and enter a new name. Click on the `Save` button, and now you can access your application with the changed name.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/changed_site_name.gif)

> I usually like to give the same name as the repository name so it's easy to find a particular application if you have a lot of deployed applications on Netlify.

If you want to know how to deploy React + Node.js application to production, check out [this article](https://dev.to/myogeshchavan97/how-to-deploy-react-node-js-application-to-heroku-4jb4).

### Thanks for reading!

You can find the complete GitHub source code along with this redirection change in [this repository](https://github.com/myogeshchavan97/netlify-react-book-management-app).

**You can see the live demo of the deployed application [here](https://react-book-management-app.netlify.app/).**

Want to learn all ES6+ features in detail including let and const, promises, various promise methods, array and object destructuring, arrow functions, async/await, import and export and a whole lot more from scratch?

Check out my [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/) book. This book covers all the pre-requisites for learning React and helps you to become better at JavaScript and React.

> Check out free preview contents of the book [here](https://www.freecodecamp.org/news/learn-modern-javascript/).

Also, you can check out my **free** [Introduction to React Router](https://yogeshchavan1.podia.com/react-router-introduction) course to learn React Router from scratch.

Want to stay up to date with regular content regarding JavaScript, React, Node.js? [Follow me on LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

<a href="https://bit.ly/3w0DGum" target="_blank" rel="noreferrer noopener"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/c3e4265df4396d639a7938a83bffd570130483b1/banner.jpg"></a>


