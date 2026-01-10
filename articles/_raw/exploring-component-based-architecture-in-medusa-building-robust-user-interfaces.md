---
title: Component-Based Architecture in Medusa – How to Build Robust User Interfaces
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-05-18T18:22:11.000Z'
originalURL: https://freecodecamp.org/news/exploring-component-based-architecture-in-medusa-building-robust-user-interfaces
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-18-21-05-01.png
tags:
- name: components
  slug: components
- name: ecommerce
  slug: ecommerce
- name: User Interface
  slug: user-interface
seo_title: null
seo_desc: "Medusa is a modern JavaScript framework that makes it easy to build robust\
  \ user interfaces. \nIt is built around a component-based architecture, which is\
  \ a design pattern that breaks down a UI into smaller, reusable components. This\
  \ makes it easier to..."
---

Medusa is a modern JavaScript framework that makes it easy to build robust user interfaces. 

It is built around a component-based architecture, which is a design pattern that breaks down a UI into smaller, reusable components. This makes it easier to maintain and update the UI, as well as to create new features.

Medusa is like a LEGO set for building user interfaces. Just as LEGO bricks can be assembled and combined to create various structures, Medusa allows you to build robust UIs by assembling and combining reusable components.

In this article, we'll explore the component-based architecture in Medusa. We will start by discussing the benefits of using this architecture, and then we will provide some code examples to show how you can use it to build user interfaces.

## Benefits of Component-Based Architecture

There are many benefits to using the component-based architecture in Medusa. Some of the most important benefits include:

* **Reusability:** Components can be reused in multiple places throughout the UI, which can save time and effort.
* **Maintainability:** Components are isolated from each other, which makes it easier to maintain and update the UI.
* **Scalability:** Components can be easily added to or removed from the UI, which makes it easy to scale the UI as needed.
* **Testability:** Components can be easily tested in isolation, which makes it easier to ensure that they are working properly.

## Understanding the Medusa Framework

Medusa is a comprehensive framework and toolset for building e-commerce applications. It provides the necessary components and infrastructure to develop, deploy, and manage online stores.

### The Medusa Backend

The backend of Medusa focuses on server-side operations and manages the core functionalities of the e-commerce application. It includes components such as:

* **Server**: Medusa provides a server that handles the logic and data management of the application. It facilitates communication between the frontend and various services, such as databases and payment gateways.
* **APIs**: The backend exposes a set of APIs (Application Programming Interfaces) that allow the frontend and other applications to interact with the server. These APIs define the endpoints and data structures for performing actions like fetching products, processing orders, and managing user accounts.
* **Business Logic**: The backend of Medusa implements the business rules and workflows specific to the e-commerce domain. It handles tasks such as inventory management, order processing, payment handling, and applying discounts or promotions.
* **Database Integrations**: The backend interacts with a database to store and retrieve data related to products, orders, customers, and other entities. Medusa supports various databases, including PostgreSQL and MySQL, and provides an abstraction layer to simplify database operations.

The Medusa backend contains the following directories and files:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-07-44-27.png)
_Medusa backend_

### The Medusa Frontend

The frontend of Medusa is responsible for the user-facing part of the e-commerce application. It focuses on providing an interactive and engaging interface for customers to browse products, add items to their cart, and complete the purchase. The frontend includes:

* **The Storefront**: The storefront component represents the application where users interact with the e-commerce store. It includes product listings, search functionality, product details, shopping cart, and checkout flow. The frontend is responsible for rendering these components and handling user interactions.
* **The User Interface (UI)**: The frontend defines the visual layout, design, and user experience of the e-commerce application. It utilizes HTML, CSS, and JavaScript to create responsive and user-friendly interfaces. Medusa provides UI components and templates that can be customized and extended to match the branding and requirements of the online store.
* **Integration with Backend APIs**: The frontend interacts with the backend APIs provided by the Medusa server. It communicates with the server to fetch product data, submit orders, update user information, and perform other operations. The frontend consumes the data returned by the backend APIs and uses it to render dynamic content on the user interface.

The Medusa frontend contains the following directories and files:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-07-45-21.png)
_Medusa storefront_

Medusa is written in TypeScript and uses React as its frontend framework. Medusa is divided into three main parts: the `server`, the `storefront`, and the `admin` panel. 

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-07-33-22.png)

Medusa is a complete e-commerce solution that includes various tools and components:

### Server

Medusa provides a server that handles the core functionalities of an e-commerce application, such as managing product catalogs, handling orders and payments, and managing user accounts.

Here is how to access the backend:

```
cd my-medusa-store/backend
yarn start
```

To get started with Medusa, you can check out [this article](https://gatwirival.hashnode.dev/what-is-medusajs-and-why-use-it).

When we run `yarn start` in the backend, by default, [localhost:9000](localhost:9000) is used.

Navigate to [localhost:9000/store/products](localhost:9000/store/products) in your browser to view a JSON collection of items. Because the seeder only inserts one product, it will only contain one item in the JSON object.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-10-50-50-1.png)

### Storefront

Medusa offers a storefront component, which is the user-facing part of the application. It includes the website or interface where customers browse products, add items to their cart, and proceed with the purchasing process.

```
cd my-medusa-store/storefront
yarn develop # for Gatsby storefront
yarn dev # for Next.js storefront
```

Since I'm using Next.js in my store front, I'll be using `yarn dev`.When we run `yarn dev` in the storefront, by default, [localhost:8000](localhost:8000) is used.

Here's what the storefront should look like:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-11-58-02.png)

### Admin Panel

Medusa provides an admin panel that enables the store owners or administrators to manage the e-commerce operations. It allows them to add and update products, process orders, handle inventory, configure shipping options, and perform other administrative tasks.

## How to Set Up the Medusa Admin Dashboard

To set up the Medusa admin dashboard, follow these steps:

To install the package, you'll have to navigate to the directory of your Medusa backend and run the following command to install the admin dashboard:

```
yarn add @medusajs/admin
```

If you use npm, you can use the command below:

```
npm install @medusajs/admin
```

### How to Enable the Admin Plugin in the Medusa Configuration File

To enable the admin plugin, open the `medusa-config.js` file in your project and locate the `plugins` array, then add the following lines:

```
const plugins = [
  // ...
  {
    resolve: "@medusajs/admin",
    /** @type {import('@medusajs/admin').PluginOptions} */
    options: {
      // ...
    },
  },
]
```

The admin plugin accepts various options for customization:

* `serve` (default: `true`): A boolean indicating whether to serve the admin dashboard when the Medusa backend starts. Set it to `false` if you prefer to serve the admin dashboard separately using the `yarn dev` command.
* `path` (default: `"app"`): A string indicating the path on which the admin server should run. It should not be prefixed or suffixed with a slash ("/"), and it cannot be one of the reserved paths: `"admin"` and `"store"`.
* `outDir`: Optional path specifying where to output the admin build files.
* `autoRebuild` (default: `false`): A boolean indicating whether the admin UI should be automatically rebuilt if there are any changes or if a missing build is detected when the backend starts. If not set, you must manually build the admin dashboard.

You can enable `autoRebuild`  by setting it to `true` in the plugin options to build the admin UI.

Run the admin dashboard using the `yarn dev` command. 

This command starts both the Medusa Backend and the admin dashboard:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-13-23-52.png)

By default, the admin dashboard will be accessible at [localhost:9000/app](localhost:9000/app). If you have set a custom `path` option, the admin will be available at `localhost:9000/<PATH>`, with `<PATH>` being the value of the `path` option. You can learn more [here](https://docs.medusajs.com/admin/quickstart).

Make sure to adjust the configurations and paths according to your specific setup.

By following these steps, you should be able to successfully set up and access the Medusa admin dashboard.

## Understanding Medusa's Component-Based Architecture

Medusa uses a component-based architecture to make it easy to extend and customize. Each component is self-contained and can be reused in other parts of the app. This makes it easy to add new features or change the look and feel of the app without affecting other parts of the codebase.

Here is an example of a component from the Medusa starter app located in the `storefront/src/modules/components/empty-cart-message` folder:

```js
import UnderlineLink from "@modules/common/components/underline-link"

const EmptyCartMessage = () => {
  return (
    <div className="bg-amber-100 px-8 py-24 flex flex-col justify-center items-center text-center">
      <h1 className="text-2xl-semi">Your shopping bag is empty</h1>
      <p className="text-base-regular mt-4 mb-6 max-w-[32rem]">
        You don&apos;t have anything in your bag. Let&apos;s change that, use
        the link below to start browsing our products.
      </p>
      <div>
        <UnderlineLink href="/store">Explore products</UnderlineLink>
      </div>
    </div>
  )
}

export default EmptyCartMessage
```

This component renders a message when the shopping cart is empty. The message includes a link to the store so that users can start browsing products.

Here is a breakdown of the code:

The `import UnderlineLink from "@modules/common/components/underline-link"` statement imports the `UnderlineLink` component from the `@modules/common/components` module. This component will be used to render the link to the store.

The `const EmptyCartMessage = () => {` statement defines the `EmptyCartMessage` component. This component takes no props and returns a `div` element with the following attributes: `className="bg-amber-100 px-8 py-24 flex flex-col justify-center items-center text-center"`.

The `return` statement returns the `div` element with the following content:

* An `h1` element with the text "Your shopping bag is empty".
* A `p` element with the text "You don't have anything in your bag. Let's change that, use the link below to start browsing our products.".
* A `div` element with the `UnderlineLink` component that links to the store.

## Medusa vs Shopify

Medusa is an open-source alternative to Shopify. Here are some comparisons between the two products:

### Customization and Flexibility

Medusa offers a high level of customization and flexibility. It allows developers to create highly tailored e-commerce applications that align with specific business requirements. With Medusa, developers have full control over the application's codebase and can customize various aspects, including the frontend and backend functionalities.

Shopify provides a less granular level of customization compared to Medusa. It operates as a hosted platform, meaning that the core infrastructure and backend are managed by Shopify. While Shopify offers a theme customization system and an app ecosystem to extend functionality, it may have limitations when it comes to implementing highly custom features.

### Hosting and Infrastructure

Medusa is a self-hosted framework, which means that developers need to set up their own hosting environment and manage the infrastructure themselves. This provides more control and scalability, but also requires additional technical expertise and resources.

Shopify is a fully hosted platform, meaning that hosting and infrastructure management are handled by Shopify. This eliminates the need for developers to set up and maintain hosting environments, making it more accessible to non-technical users.

### Pricing

As an open-source framework, Medusa is free to use, and there are no licensing fees. However, since it requires self-hosting, there may be associated costs for hosting services and infrastructure management.

Shopify operates on a subscription-based pricing model. It offers different pricing plans with varying features and transaction fees. The subscription fees cover hosting, security, and support services.

### Ecosystem and App Integrations

Medusa has a growing ecosystem of extensions and integrations, allowing developers to leverage third-party tools and services to enhance their e-commerce applications. While the ecosystem may not be as extensive as Shopify's, Medusa's open-source nature enables developers to create custom integrations as needed.

Shopify has a vast ecosystem of apps and integrations available through the Shopify App Store. These apps can add functionality, extend features, and integrate with various services such as marketing, analytics, and shipping providers. The extensive app ecosystem of Shopify is one of its major strengths.

### Target Audience

Medusa is suited for businesses that require advanced customization and flexibility in their e-commerce applications. It is a suitable choice for developers and businesses with technical expertise looking for full control over their e-commerce infrastructure.

Shopify is designed to cater to a wide range of users, including small to medium-sized businesses and individuals, who want a user-friendly and hassle-free e-commerce solution. It is suitable for users with limited technical knowledge or resources who prioritize ease of use and convenience.

## Conclusion

The component-based architecture is a powerful design pattern that can be used to build robust user interfaces in Medusa. By using components, you can create reusable, maintainable, scalable, and testable UIs.

Medusa is a comprehensive e-commerce framework that includes a server, a storefront component, and an admin panel. It provides developers with the necessary tools to build customizable and scalable e-commerce applications, tailored to specific business needs.

I hope this article has been helpful. Please let me know if you have any questions. 

