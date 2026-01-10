---
title: How to Build Your Own E-Commerce Site with Medusa
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-02-27T15:36:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-e-commerce-site-with-medusa
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/medusa.png
tags:
- name: ecommerce
  slug: ecommerce
- name: node
  slug: node
seo_title: null
seo_desc: "In today's digital age, having an online presence is crucial for businesses\
  \ of all sizes. \nWhether you're an established retailer or an aspiring entrepreneur,\
  \ an ecommerce site can provide you with a platform to reach a global audience and\
  \ sell your ..."
---

In today's digital age, having an online presence is crucial for businesses of all sizes. 

Whether you're an established retailer or an aspiring entrepreneur, an ecommerce site can provide you with a platform to reach a global audience and sell your products or services around the clock.

Building an ecommerce site may seem like a daunting task, but with the right tools and guidance, anyone can create a professional and functional online store. 

In this tutorial, you'll learn how to build your own e-commerce site with Medusa.

## What is Medusa?

[Medusa](https://medusajs.com) is an _open source_, _composable_ commerce platform that's perfect for developers who want to create a customized ecommerce solution. With its flexible architecture and powerful features, Medusa offers a seamless and straightforward way to build a robust and scalable ecommerce site.

Medusa offers a variety of features, including order management with automated swaps, returns, and claims. It also enables customer management and assignment to customer groups, along with product customization and collection sorting. 

With the ability to manage multiple regions and currencies, users can integrate various plugins and third-party services, create advanced pricing and discount rules, configure taxes, and set up multiple sales channels. 

Additionally, Medusa offers bulk import and export strategies, and complete customization capabilities to create custom endpoints, services, subscribers, batch job strategies, and more.

In just over a year since its launch, this platform has quickly risen to become the [#1 Node.js ecommerce solution](https://medusajs.com/blog/nodejs-ecommerce-backend/), garnering over 17K+ stars on [GitHub](https://github.com/medusajs/medusa) due to its immense popularity.

## Architecture of Medusa

With a composable architecture, Medusa's frontend and backend components are loosely coupled. The platform consists of three different components: the **headless backend**, the **admin dashboard**, and the **storefront**.

You can choose to use the complete Medusa platform or just the parts that you require for your store. 

Additionally, with the backend decoupled from the frontend, developers can focus on their respective areas of expertise. Backend developers can concentrate on the Medusa server, while frontend developers can focus on either the storefront or admin.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/medusa-arch.png)
_Medusa Architecture_

In the upcoming sections, you will see how Medusa delivers most ecommerce store functionalities right out of the box, with the ability to configure these features to your specific use case.

### **Medusa Server**

The Medusa server, which is a Node.js ecommerce backend, serves as a core component of the platform. It contains all the store's data and logic, and the other two components use its REST APIs to create, retrieve, and modify data.

The server provides most of the features related to an ecommerce workflow. These functionalities include managing products, carts, and orders, as well as integrating with shipping and payment providers and managing users. 

In addition to that, you can configure your store including your store’s region, tax rules, discounts, gift cards, and more.

Since Medusa is highly extensible, it allows developers to build custom features such as [automating customer group assignments](https://medusajs.com/blog/customer-group-automation/) and [integrating ChatGPT to automate writing product descriptions](https://medusajs.com/blog/chatgpt-medusa/). 

In addition to that, you can also integrate third-party services into Medusa using [Plugins](https://docs.medusajs.com/advanced/backend/plugins/overview). You can find both official and community plugins to assist you with your common needs. Learn more about these plugins [here](https://docs.medusajs.com/advanced/backend/plugins/overview/).

Medusa also allows you to extend its functionalities with new endpoints, business logic, and database entities. Additionally, you can create subscribers that listen to events and trigger specific actions.

### Medusa Storefront

The storefront serves as the main presentation layer or frontend of your ecommerce store where customers can view and purchase your products. These storefronts can be in the form of progressive web applications or mobile apps.

Medusa offers two storefront starters built with [Next.js](https://docs.medusajs.com/starters/nextjs-medusa-starter) and [Gatsby](https://docs.medusajs.com/starters/gatsby-medusa-starter/), respectively. The storefront includes several features such as product listing and detail pages, customer authentication and profile functionalities, and a full checkout flow supporting shipping details and methods. It also comes with search capabilities ready for integration with top solutions like Algolia and MeiliSearch.

Below is a demonstration of what the Next.js storefront looks like:

%[https://youtu.be/TmV2xNbNs4w]

In addition to the provided storefront starters, you have the freedom to create your own custom storefront using the [Storefront REST APIs](https://docs.medusajs.com/api/store/).

### **Medusa Admin**

An ecommerce store's essential component is the Admin dashboard, which enables merchants to view, create, and modify data such as products and orders.

With the Medusa Admin dashboard, Medusa provides functionalities for store management, including product management, order management, and user management. You can manage your orders from various regions and channels using a single dashboard.

For merchants migrating their stores from other platforms, the admin dashboard provides easy import and export functionalities for large datasets of products, orders, and customers. The dashboard also offers customer-group functionality to create customized pricing lists, discounts, and gift cards.

This is what the Medusa Admin Dashboard looks like:

%[https://youtu.be/Z6uoN7TR0Z0]

However, if you are not satisfied with the existing admin dashboard, you can utilize the Admin REST APIs to extend it beyond.

## How to Set Up an Ecommerce Store Using Medusa

In this section, you'll set up the three components of your Medusa ecommerce store.

### Prerequisites

Before you get started with the tutorial, you should have installed:

* [Node.js(V14 or later)](https://docs.medusajs.com/tutorial/set-up-your-development-environment#nodejs)
* [Git](https://docs.medusajs.com/tutorial/set-up-your-development-environment/#git)
* [Medusa CLI](https://docs.medusajs.com/tutorial/set-up-your-development-environment#medusa-cli)

### How to Set Up the Medusa Server

Creating a new Medusa server is a simple process using the Medusa CLI. Navigate to the directory where you want to create your Medusa server and run the following command to create a new Medusa server with the name `my-medusa-store`:

```bash
medusa new my-medusa-store --seed
```

This command will create a new Medusa server with the specified name. The `--seed` option tells the Medusa CLI to seed the data after creating the server. The seed data includes sample data such as products, categories, and more.

Once the command finishes executing, navigate to the `my-medusa-store` directory and start the server by running the following command:

```bash
cd my-medusa-store
medusa develop
```

In a couple of minutes, the server will start running on the default `9000` port. You can test it out by sending a request using a tool like Postman or through the command line:

```bash
curl localhost:9000/store/products
```

If your server is successfully set up, you will see a list of products and other details as below:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/curl-output.png)
_Output of cURL command_

### How to Set Up the Next.js Storefront

Now that your Medusa server is up and running, it's time to configure your storefront. In this section, you'll set up the Next.js storefront.

Create a new Next.js project using the [Medusa Next.js starter template](https://github.com/medusajs/nextjs-starter-medusa):

```bash
npx create-next-app -e https://github.com/medusajs/nextjs-starter-medusa my-medusa-storefront
```

Navigate to the newly created directory `my-medusa-storefront` folder and rename the template environment variable file to use environment variables in development:

```bash
cd my-medusa-storefront
mv .env.template .env.local
```

Make sure the Medusa server is running, then run the local Next.js server:

```bash
npm run dev
```

Your Next.js storefront will now be running on its default port `8000`.

Note: Medusa also provides you with the [Gatsby starter template](https://docs.medusajs.com/starters/gatsby-medusa-starter/) to create the storefront.

### How to Set Up the Medusa Admin Dashboard

Since the Medusa Admin uses the Medusa server, make sure your server is up and running.

Start by cloning the [Admin GitHub repository](https://github.com/medusajs/admin):

```bash
git clone https://github.com/medusajs/admin my-medusa-admin
```

Navigate to the cloned `my-medusa-admin` folder and install all the dependencies:

```bash
cd my-medusa-admin
npm install
```

Run the development server:

```bash
npm run start
```

In a couple of minutes, the admin will start running on the default `7000` port. So, in your browser, go to `localhost:7000` to view your admin.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/medusa-admin.png)
_Medusa Admin Login_

If you had already seeded the data in your Medusa server, you can use the email `admin@medusa-test.com` and password `supersecret` to log in. If you hadn't, you can [create a new admin user](https://docs.medusajs.com/admin/quickstart#create-a-new-admin-user).

## How to Set Up Medusa with `create-medusa-app`

Up to this point, you have seen how to set up individual components of a Medusa project. But in this section, you will learn how to set up a complete Medusa project with all three components using a single command.

Medusa now provides you with a `create-medusa-app` command to set up a project. This command provides an interactive prompt that guides you through the setup process.

To use `create-medusa-app`, simply run the following command:

```bash
npx create-medusa-app
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/create-medusa-app.gif)
_Creating Medusa Project Using create-medusa-app_

In this interactive setup, you will be prompted to enter the name of the directory where you want to install the Medusa project. The default name is `my-medusa-store`, but you can choose to name it something else.

Next, you will be asked to select a Medusa server starter from the available options, which include the default starter, the Contentful starter, and the option to enter a custom starter URL. The server will be installed in the `backend` directory of your project, and a demo SQLite database will be created within it.

Following the Medusa server setup, you will be prompted to choose a storefront starter from the available options. If you choose to install a storefront, it will be installed in the `storefront` directory of your project. If you choose "None", no storefront will be installed.

The admin is set up automatically inside the `admin` directory of your project.

Once the setup is complete, you will receive instructions on how to start each component of the Medusa project.

```bash
Your project is ready. The available commands are:

Medusa API
cd my-medusa-store/backend
yarn start

Admin
cd my-medusa-store/admin
yarn start

Storefront
cd my-medusa-store/storefront
yarn develop # for Gatsby storefront
yarn dev # for Next.js storefront
```

Just keep in mind that the commands can differ based on your choices in previous prompts.

### Project Directory Structure

Inside the root project directory (which was specified at the beginning of the installation process – `my-medusa-store` in this case) you’ll find the following directory structure:

```bash
my-medusa-store
  ├── admin
  ├── backend
  └── storefront
```

## Conclusion

In this tutorial, we've explored Medusa, an open-source e-commerce platform that provides a robust set of features for building online stores. We've looked at the architecture of Medusa, its key features, and how to set up the server, admin dashboard, and storefront.

One of the strengths of Medusa is its flexibility and extensibility. With a variety of plugins and extensions, you can customize your e-commerce site to meet your specific needs. You can also create your own plugins or themes, making it easy to build a site that reflects your brand.

If you're looking to build an e-commerce site, Medusa is a solid choice that offers a lot of functionality out of the box. With its user-friendly interface, setting up an online store is a straightforward process. Plus, since it's an open-source platform, you have the freedom to modify and extend it as needed.

### Additional Resources

Here are some resources that you can use to extend the functionalities:

* Integrate [SendGrid](https://docs.medusajs.com/add-plugins/sendgrid) as a notification provider.
* Integrate [Stripe](https://docs.medusajs.com/add-plugins/stripe) as a payment provider.
* [Create a service](https://docs.medusajs.com/advanced/backend/services/create-service).

