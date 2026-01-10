---
title: How to Set Up Tailwind CSS with NextJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-07T21:37:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-tailwind-css-with-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Tutorials.png
tags:
- name: CSS
  slug: css
- name: Next.js
  slug: nextjs
- name: tailwind
  slug: tailwind
seo_title: null
seo_desc: "By Kelvin Moses\nTailwind CSS is a popular utility-first CSS framework\
  \ that offers a unique approach to building modern and responsive user interfaces.\
  \ \nUnlike traditional CSS frameworks that provide pre-designed components, Tailwind\
  \ CSS focuses on pr..."
---

By Kelvin Moses

Tailwind CSS is a popular utility-first CSS framework that offers a unique approach to building modern and responsive user interfaces. 

Unlike traditional CSS frameworks that provide pre-designed components, Tailwind CSS focuses on providing a comprehensive set of utility classes that you can directly apply to your HTML elements. 

When combined with Next.js, a powerful React framework for building server-side rendered applications, you can unlock a seamless development experience and create performant, scalable web applications. 

In this tutorial, I'll will walk you through the process of setting up Tailwind CSS with Next.js, so you can harness the power of Tailwind's utility classes in your Next.js projects. 


### Prerequisites

Before getting started, make sure you have the following prerequisites:

1. Node.js installed on your machine
2. Basic knowledge of JavaScript and React
3. Familiarity with Next.js


## How Tailwind CSS and Utility Classes Work

Tailwind CSS follows a utility-first approach to styling. It provides a vast collection of small, single-purpose utility classes that you can apply directly to your HTML elements. 

Each utility class represents a specific CSS property or combination of properties, making it easy to build complex UI components by composing these classes together. 

For example, instead of defining a custom CSS class for setting the color of a button, you can simply apply the "text-blue-500" utility class to achieve the desired effect.

The utility classes in Tailwind CSS are designed to be highly flexible and customizable. You can easily adjust properties such as margin, padding, font size, colors, and more by leveraging the intuitive naming conventions provided by Tailwind. 

This approach offers a fine-grained level of control over your styles, eliminating the need to write custom CSS for most common styling scenarios.

## Why Use Tailwind CSS with Next.js?

Next.js is a powerful framework for building server-side rendered React applications. It provides an excellent development experience and offers features such as automatic code splitting, server-side rendering, and static site generation. 

When you use Next together with Tailwind CSS, it enables you to effortlessly integrate Tailwind's utility classes into your application development workflow.

Next.js optimizes the delivery of CSS styles by automatically tree-shaking unused CSS during the build process. This means that even though Tailwind CSS provides an extensive set of utility classes, only the styles you actually use in your application will be included in the final bundle. This approach ensures that your application remains lightweight and performs efficiently.

By leveraging the combination of Tailwind CSS and Next.js, you can quickly prototype, design, and build responsive user interfaces while enjoying the benefits of a streamlined development process and optimized performance.

Now that you understand the benefits and synergy between Tailwind CSS and Next.js, let's dive into the step-by-step process of setting up Tailwind CSS with Next.js.

## Step 1: Create a New Next.js Project

To begin, let's create a new Next.js project. Open your terminal and run the following command:



``` bash 
npx create-next-app my-tailwind-project
```


This will create a new Next.js project named "my-tailwind-project" in a directory with the same name.

## Step 2: Install Tailwind CSS

Navigate to the project directory by running the following command:

``` bash 
cd my-tailwind-project
```

Next, install Tailwind CSS and its dependencies by running the following command:

``` bash 
    npm install tailwindcss postcss autoprefixer
```



## Step 3: Configure Tailwind CSS

After installing Tailwind CSS, we need to configure it to work with Next.js. Create a new file named postcss.config.js in the project's root directory and add the following code:

``` javascript 
module.exports = {
  plugins: [
    'tailwindcss',
    'postcss-flexbugs-fixes',
    'postcss-preset-env',
    [
      'postcss-normalize',
      {
        allowDuplicates: false,
      },
    ],
    [
      '@fullhuman/postcss-purgecss',
      {
        content: ['./pages/**/*.{js,jsx,ts,tsx}', './components/**/*.{js,jsx,ts,tsx}'],
        defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
      },
    ],
    'autoprefixer',
  ],
};


```

This configuration sets up Tailwind CSS, adds necessary PostCSS plugins, and includes PurgeCSS to remove unused CSS in production builds.

## Step 4: Create Tailwind CSS Configuration

Next, we need to generate a default configuration file for Tailwind CSS. This configuration file allows you to customize Tailwind CSS according to your project's specific needs. It defines the color palette, typography settings, spacing utilities, and more.

The tailwind.config.js file serves as the central configuration hub for Tailwind CSS. It provides a JavaScript object where you can define your customizations and extend the default configuration.

By generating the default configuration file, you have the flexibility to modify various aspects of Tailwind CSS, including theme customization, extending utility classes, and purging unused CSS during production builds.

Customizing the configuration file allows you to tailor the utility classes and overall design system to align with your application's requirements and branding guidelines.


Let's now generate the default configuration file for Tailwind CSS. Run the following command:

``` bash 
npx tailwindcss init
```

This will create a tailwind.config.js file in your project's root directory.

## Step 5: Customize Tailwind CSS



Open the tailwind.config.js file and customize Tailwind CSS according to your project's needs. Here's an example of what a customized tailwind.config.js file might look like:

``` javascript

module.exports = {
  purge: ['./pages/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  darkMode: false,
  theme: {
    extend: {
      colors: {
        primary: '#FF0000',
        secondary: '#00FF00',
      },
      fontFamily: {
        sans: ['Roboto', 'Arial', 'sans-serif'],
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};

```



In this example, we're customizing the Tailwind CSS configuration by:

* Specifying the files to be purged using the purge option. This ensures that only the CSS classes used in your project are included in the final build.
* Disabling the dark mode functionality by setting **darkMode** to **false**.
* Extending the color palette with two custom colors: **primary** and **secondary**.
* Adding a custom font family called **sans** that includes the fonts Roboto, Arial, and the generic sans-serif fallback.
* Keeping the **variants** and **plugins** sections empty for this basic configuration.


You can further customize Tailwind CSS by exploring other configuration options available in the official documentation. Tailwind CSS provides extensive flexibility, allowing you to tailor the framework to your project's specific design requirements.

Once you've customized the tailwind.config.js file, save it, and proceed to the next step.

## Step 6: Import Tailwind CSS Styles

To use Tailwind CSS styles in your Next.js project, import the styles into your pages/_app.js file. Open the file and add the following code:

``` javascript 
import 'tailwindcss/tailwind.css';

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

This imports the compiled Tailwind CSS styles and applies them to your entire application.

## Step 7: Start the Development Server

Now, you're ready to start the development server and see Tailwind CSS in action. Run the following command:

``` bash 
npm run dev
```

Visit `http://localhost:3000` in your browser, and you should see your Next.js application with Tailwind CSS styling applied.

This will generate a production-ready build of your application, including only the necessary CSS styles.

## Conclusion
Congratulations! You have successfully set up Tailwind CSS with Next.js. You can now start leveraging Tailwind's utility classes to rapidly build beautiful and responsive UI components in your Next.js projects. 

Feel free to explore the Tailwind CSS documentation to discover the wide range of utility classes available.


Remember to regularly update Tailwind CSS and its dependencies to benefit from the latest features and bug fixes.

Happy coding!😊
Let's connect [IamKelv](https://twitter.com/iam_kelvinjnr)


