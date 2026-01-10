---
title: How to Build a Portfolio Site with Sanity and Next.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-28T16:30:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-portfolio-site-with-sanity-and-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Sanity-1.png
tags:
- name: headless cms
  slug: headless-cms
- name: Next.js
  slug: nextjs
- name: portfolio
  slug: portfolio
seo_title: null
seo_desc: "By Victor Eke\nKnowing how to handle content is important when creating\
  \ a personal website for yourself or a client. \nThis is because maintaining and\
  \ updating a site can result in substantial expenses if you don't do it correctly.\
  \ This is even more th..."
---

By Victor Eke

Knowing how to handle content is important when creating a personal website for yourself or a client. 

This is because maintaining and updating a site can result in substantial expenses if you don't do it correctly. This is even more the case if you're building for someone with a non-technical background.

To address this, you can integrate your website with a [headless CMS](https://www.sanity.io/headless-cms) service that offers an API for content management and updates. In this case, we will utilize [Sanity](https://sanity.io) for this purpose.

## Table of Contents:

1. [What is Sanity?](#heading-what-is-sanity)
2. [Step 1: Install Next.js](#heading-step-1-install-nextjs)
3. [Step 2: Setup Sanity Studio](#heading-step-2-setup-sanity-studio)
4. [Step 3: Mount Sanity Studio into Next.js](#heading-step-3-mount-sanity-studio-into-nextjs)
5. [Step 4: Create Content Schemas](#heading-step-4-create-content-schemas)
6. [Step 5: Query Data using GROQ](#heading-step-5-query-data-using-groq)
7. [Step 6: Display Content in your Next.js App](#heading-step-6-display-content-in-your-nextjs-app)
8. [Fix Studio Layout](#heading-fix-studio-layout)
9. [Step 7: Deployment](#heading-step-7-deployment)
10. [Setup Sanity Webhooks for Studio Update](#heading-setup-sanity-webhooks-for-studio-update)
11. [What Next?](#heading-what-next)

## What is Sanity?

Sanity is a headless CMS framework for managing content. It provides tools to leverage APIs to connect to your web app providing instantaneous, rich and automated infrastructure for managing content on the cloud.

With Sanity, you can hook up pages or content that require regular updating to the studio and manage them from the content lake without having to touch code frequently. This makes the content creation and management process accessible to more people regardless of their technical background.

In this post, you'll learn how to use Sanity as a data source to build a portfolio site with Next.js 13 and Tailwind CSS. You'll also learn how to host it on [Vercel](https://vercel.com) and set-up webhooks to trigger deployments.

Here is a screenshot of what the portfolio site will look like. Some of the designs for this site were inspired by [Tailwind's Spotlight Portfolio Template](https://tailwindui.com/templates/spotlight).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/final-result-3.png)
_Finished personal project_

Want to play around with it? Check out the [live demo](https://sanity-nextjs-site.vercel.app). Also, you can find the source code for the project on [GitHub](https://github.com/Evavic44/sanity-nextjs-site).

## Step 1: Install Next.js

Open a terminal and run this command to install the latest version of Next.js:

```bash
npx create-next-app@latest
```

Select all your preferred install options. Except for the project name, I'll go with the default options.

```bash
√ What is your project named? ... sanity-nextjs-site
√ Would you like to use TypeScript with this project? ... Yes
√ Would you like to use ESLint with this project? ... Yes
√ Would you like to use Tailwind CSS with this project? ... Yes
√ Would you like to use `src/` directory with this project? ... No
√ Would you like to use App Router? (recommended) ... Yes
√ Would you like to customize the default import alias? ... No
```

This should install all the required dependencies, including Tailwind CSS into the project folder. To see it live run the command below:

```bash
cd sanity-nextjs-site

npm run dev
```

Visit [http://localhost:3000](https://localhost:3000) to see the site.

## Step 2: Setup Sanity Studio

Sanity studio is Sanity's open source single-page app for managing your data and operations. This is the interface from which you can create, delete, and update your data within Sanity.

### Install Sanity Studio

Open up a new terminal outside of your Next.js application and type the commands below:

```bash
mkdir sanity-studio

cd sanity-studio

npm create sanity@latest
```

Once your run the command in your terminal, you'll be prompted to select a login provider from the list of options. If you already have an account, it will authenticate your account and automatically log you in or else you can create a new account on Sanity.

Once your account has been successfully authenticated, more prompts will be provided in the terminal to configure your project. Here are the options set for the studio:

```bash
$ Project name: Sanity Next.js Site
$ Use the default dataset configuration?: Yes
$ Project output path: C:\Users\USER\Desktop\sanity-studio
$ Select project template: Clean project with no predefined schemas
$ Do you want to use TypeScript? Yes
$ Package manager to use for installing dependencies?: npm
```

Once completed, this should install Sanity studio locally. To see the studio, run `npm run dev` and visit [localhost:3333](http://localhost:3333), log into your account using the same method used in creating your account, and you should see the studio running locally.

## Step 3: Mount Sanity Studio into Next.js

You can choose to host your studio separately, but in this tutorial you'll be mounting it together with your Next.js application using the [next-sanity](https://github.com/sanity-io/next-sanity) toolkit. 

End the server running your Next app and run this command:

```bash
npm install sanity next-sanity
```

And then on the `sanity-studio` directory running the studio locally, copy the `schema` folder and `sanity.config.ts` file and paste into the root of your Next.js app.

The folder structure should look like this:

```bash
├── .next
├── app/
├── node_modules/
├── public/
├── schemas/
│   └── index.ts
├── .eslintrc.json
├── .gitignore
├── next-env.d.ts
├── next.config.js
├── package-lock.json
├── package.json
├── postcss.config.js
├── README.md
├── sanity.config.ts
├── tailwind.config.js
└── tsconfig.json
```

Next, inside the `sanity.config.ts` file, add a `basePath` key and give it a value of `/studio` or any valid URL path where you would like your studio to live.

```js
// sanity.config.ts

import { defineConfig } from "sanity";
import { deskTool } from "sanity/desk";
import { schemaTypes } from "./schemas";

export default defineConfig({
  name: "sanity-nextjs-site",
  title: "Sanity Next.js Site",
  projectId: "ga8lllhf",
  dataset: "production",
  basePath: "/studio",
  plugins: [deskTool()],
  schema: { types: schemaTypes },
});

```

Here's a breakdown of each property:

* `name`: Used to differentiate workspaces. Not compulsory for single workspace setup.
* `title`: Title of your project. This will show up on the Studio.
* `projectId`: This is a unique ID that points to the Sanity project you're working with.
* `dataset`: The name of the dataset to use for your studio. Common names are _production_ and _development_.
* `basePath`: This is the URL path where your studio will be mounted.
* `schema`: The object where your schema files will be defined.

### Create the Studio Component

This is where the studio page will be mounted within your Next app. You can name this file whatever you prefer, but it must match with the `basePath` key specified inside the `sanity.config.ts` file. In my case, the file name will be `studio`.

To create the studio route, we'll utilize Next.js dynamic segments. Inside the app directory, create a `studio/[[...index]]/page.tsx` file. 

```bash
app/
└── studio/
    └── [[...index]]/
         └── page.tsx
```

With this, when you visit any route that matches with `/studio`, the studio component `page.tsx` will be rendered.

To complete this setup, paste this code inside the component:

```js
// app/studio/[[...index]]/page.tsx

"use client";

import { NextStudio } from "next-sanity/studio";
import config from "@/sanity.config";

export default function Studio() {
  return <NextStudio config={config} />;
}

```

First, `NextStudio` is imported from the `next-sanity` library and the configuration file is imported from the `sanity.config.ts` file you created earlier.

Now run `npm run dev` and visit `localhost:3000/studio`. You will get a prompt to add `localhost:3000` as a CORS origin to your Sanity project. Just click continue to add the URL. 

Once added, log into your Sanity account using the same method you used in creating your account and you should see the Studio mounted into your Next.js application as shown in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sanity-studio-admin-page-3.png)

With the studio now running in your Next.js app, you don't need the separate `sanity-studio` directory anymore. You can delete or close it.

By default, the studio will be blank because you haven't created any schemas files. Let's do that in the next section.

## Step 4: Create Content Schemas

Schemas are essentially a way of organizing datasets in a database depending on what type of content you need. 

Since we're building a portfolio site, we'll create schemas to handle projects, profile, and so on. To be more specific, you'll create three schemas files for this portfolio project:

* `profile:` Schema file for defining your personal information like name, about, skills, and so on.
* `project:` Schema file for your projects.
* `work:` Schema file for defining your work experience.

Let's start with the profile schema.

### Profile Schema

Inside the schemas directory, create a `profile.ts` file. 

```bash
touch schemas/profile.ts
```

Let's start by defining the basic properties of a schema file.

```js
// schemas/profile.ts

import { defineField } from "sanity";
import { BiUser } from "react-icons/bi";

const profile = {
  name: "profile",
  title: "Profile",
  type: "document",
  icon: BiUser,
  fields: [],
};

export default profile;

```

Each schema file must contain a `name`, `title`, and `type` property. Here's a brief breakdown of the function of each property:

* The `name` key is the property that is used to reference a schema in the query language. The value must be a [unique value](https://www.sanity.io/help/schema-object-fields-invalid) to avoid conflating schemas.
* `title` defines what the schema type is called in the Studio UI.
* `type` defines what schema type you're working with. The `document` value will tell the studio that it should make it possible to make new documents.
* The `icon` is an optional property you can add alongside the `title`. To use the icon, install the [react-icons](https://react-icons.github.io/react-icons) library with the command `npm install -D react-icons`
* The `fields` array, is where the individual input fields will be defined. Here are the fields for the profile schema:

```js
fields: [
    defineField({
      name: "fullName",
      title: "Full Name",
      type: "string",
      validation: (rule) => rule.required(),
    }),
    defineField({
      name: "headline",
      title: "Headline",
      type: "string",
      description: "In one short sentence, what do you do?",
      validation: (Rule) => Rule.required().min(40).max(50),
    }),
    {
      name: "profileImage",
      title: "Profile Image",
      type: "image",
      description: "Upload a profile picture",
      options: { hotspot: true },
      fields: [
        {
          name: "alt",
          title: "Alt",
          type: "string",
        },
      ],
    },
    {
      name: "shortBio",
      title: "Short Bio",
      type: "text",
      rows: 4,
    },
    {
      name: "email",
      title: "Email Address",
      type: "string",
    },
    {
      name: "location",
      title: "Location",
      type: "string",
    },
    {
      name: "fullBio",
      title: "Full Bio",
      type: "array",
      of: [{ type: "block" }],
    },
    {
      name: "resumeURL",
      title: "Upload Resume",
      type: "file",
    },
    {
      name: "socialLinks",
      title: "Social Links",
      type: "object",
      description: "Add your social media links:",
      fields: [
        {
          name: "github",
          title: "Github URL",
          type: "url",
          initialValue: "https://github.com/",
        },
        {
          name: "linkedin",
          title: "Linkedin URL",
          type: "url",
          initialValue: "https://linkedin.com/in/",
        },
        {
          name: "twitter",
          title: "Twitter URL",
          type: "url",
          initialValue: "https://twitter.com/",
        },
        {
          name: "twitch",
          title: "Twitch URL",
          type: "url",
          initialValue: "https://twitch.com/",
        },
      ],
      options: {
        collapsed: false,
        collapsible: true,
        columns: 2,
      },
    },
    {
      name: "skills",
      title: "Skills",
      type: "array",
      description: "Add a list of skills",
      of: [{ type: "string" }],
    },
 ],
```

To understand how fields work, visualize each field object as a HTML `<input>` that will be available in the studio. The value in each input will be exported to a JSON object you can use to inject your data. You can add as many fields, but each must contain a `name`, `title`, and `type` property.

The `defineField()` helper function helps enable auto-completion of field types in your schema file.

Sanity comes with its own built-in schema types: `number`, `datetime`, `image`, `array`, `object`, `string`, `url`, and more. You can check out the full list of [schema types here](https://www.sanity.io/docs/schema-types).

To expose this newly created schema file to the Studio, you need to import it into the schemas array inside the `schemas/index.ts` file:

```js
// schemas/index.ts

import profile from "./profile";

export const schemaTypes = [profile];

```

Now you can start working with it from within the studio. Visit your studio at `localhost:3000/studio` or whatever path you used to mount it. Then click on the Profile tab and select the edit button on the top corner to start editing the fields.

This is what that looks like:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/profile-schema-filled.png)

Fill in all the fields and click publish once completed. This will append the data into a parsed JSON document. To view this JSON output, click the menu button on the top right corner and hit "Inspect" or simply hold down `Ctrl Alt I` on your keyboard.

Here's what the structure for the profile schema looks like:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/inspect-schema-types-3.png)
_Inspect schema document_

With this, you can easily query the data to fetch the exact content you need in your front-end. Let's do that in the next section.

## Step 5: Query Data using GROQ

[GROQ (Graph-Relational Object Queries)](https://www.sanity.io/docs/groq) is Sanity's query language designed to query collections of largely schema-less JSON documents. The idea behind the query language is to be able to describe exactly what information you need from your schema, or filter certain data, and return only specific elements from your data

To start using GROQ, first create a `sanity/sanity.client.ts` file in your project root directory.

```bash
mkdir sanity && touch sanity/sanity.client.ts
```

Paste the code into this file:

```js
// sanity/sanity.client.ts

import { createClient, type ClientConfig } from "@sanity/client";

const config: ClientConfig = {
  projectId: "ga8lllhf",
  dataset: "production",
  apiVersion: "2023-07-16",
  useCdn: false,
};

const client = createClient(config);

export default client;
```

* `apiVersion`:  The version of the Sanity API you're using. For the latest API version, use your current date in this format `YYYY-MM-DD`.
* `useCdn` is used to disable edge cases

What this file does is provide a few configurations that will be defined in each query so this is just to avoid repeating it every time. Now for the main query, create a `sanity/sanity.query.ts` file.

```bash
touch sanity/sanity.query.ts
```

Note: There is not clear-cut way to arrange or name these files so feel free to change it up as needed.

Here's the basic query for the profile schema:

```js
// sanity/sanity.query.ts

import { groq } from "next-sanity";
import client from "./sanity.client";

export async function getProfile() {
  return client.fetch(
    groq`*[_type == "profile"]{
      _id,
      fullName,
      headline,
      profileImage {alt, "image": asset->url},
      shortBio,
      location,
      fullBio,
      email,
      "resumeURL": resumeURL.asset->url,
      socialLinks,
      skills
    }`
  );
}

```

Here we created an exported async function called `getProfile()` that returns a groq fetch query wrapped with the client config created in the first step.

The groq query starts with an asterisk (`*`) which represents every document in your dataset followed by a filter in brackets. The filter above returns the schema that has a `_type` of "profile".

![Image](https://www.freecodecamp.org/news/content/images/2023/07/profile-type-1.png)
_Schema JSON showing profile schema _type_

The filter is followed by curly braces which contains specific content from the dataset needed like: `fullName`, `headline`, `profileImage` and so on. This is called [projections](https://www.sanity.io/docs/how-queries-work#727ecb6f5e15) in the Sanity docs and it returns the entire data as an array.

If you want to learn more about querying using GROQ, I suggest you go through the [how queries work](https://www.sanity.io/docs/how-queries-work) section in the documentation. For syntax highlighting of your GROQ query, install the [sanity.io extension](https://marketplace.visualstudio.com/items?itemName=sanity-io.vscode-sanity) available on the Visual Studio Code marketplace.

We're done with the configuration you need to start using your content. Let's look at how to display this content in your Next application.

## Step 6: Display Content in your Next.js App

This section is broken down into two separate parts: Displaying the hero section, and about page content.

### Add Types to Data Content

Since you're using TypeScript for this project, it is important to first provide the types for the data coming from the studio.

Create a `types/index.ts` file in the root directory and add the profile type below:

```js
// types/index.ts

import { PortableTextBlock } from "sanity";

export type ProfileType = {
  _id: string,
  fullName: string,
  headline: string,
  profileImage: {
    alt: string,
    image: string
  },
  shortBio: string,
  email: string,
  fullBio: PortableTextBlock[],
  location: string,
  resumeURL: string,
  socialLinks: string[],
  skills: string[],
};
```

`PortableTextBlock` is a unique type coming from Sanity that properly defines the data type for the rich text editor.

Now you've defined the types for your content, it's easier to visualize the data you're expecting in your studio.

### Display Hero Section

First, remove all the styling inside the `global.css` file, except for the necessary Tailwind imports at the top. Then clear everything inside the root `page.tsx` file of your Next.js app and paste the following code inside:

```js
// app/page.tsx

import { getProfile } from "@/sanity/sanity.query";
import type { ProfileType } from "@/types";
import HeroSvg from "./icons/HeroSvg";;

export default async function Home() {
  const profile: ProfileType[] = await getProfile();

  return (
    <main className="max-w-7xl mx-auto lg:px-16 px-6">
      <section className="flex xl:flex-row flex-col xl:items-center items-start xl:justify-center justify-between gap-x-12 lg:mt-32 mt-20 mb-16">
        {profile &&
          profile.map((data) => (
            <div key={data._id} className="lg:max-w-2xl max-w-2xl">
              <h1 className="text-3xl font-bold tracking-tight sm:text-5xl mb-6 lg:leading-[3.7rem] leading-tight lg:min-w-[700px] min-w-full">
                {data.headline}
              </h1>
              <p className="text-base text-zinc-400 leading-relaxed">
                {data.shortBio}
              </p>
              <ul className="flex items-center gap-x-6 my-10">
                {Object.entries(data.socialLinks)
                  .sort()
                  .map(([key, value], id) => (
                    <li key={id}>
                      <a
                        href={value}
                        rel="noreferer noopener"
                        className="flex items-center gap-x-3 mb-5 hover:text-purple-400 duration-300"
                      >
                        {key[0].toUpperCase() + key.toLowerCase().slice(1)}
                      </a>
                    </li>
                  ))}
              </ul>
            </div>
          ))}
        <HeroSvg />
      </section>
    </main>
  );
}
```

* First the `getProfile` query is imported from the `sanity.query.ts` file which is a filtered-down version of our data coming from the schema.
* `ProfileType` is imported to add types to the data.
* The `profile` array is mapped inside the component to return the `headline`, `shortBio`, and `socialLinks`.
* `<HeroSvg />` is essentially an `svg` element imported as a react component added just for UI aesthetics. You can download the [HeroSVG icon component](https://github.com/Evavic44/sanity-nextjs-site/blob/main/app/(site)/icons/HeroSvg.tsx).

Here's the resulting output:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/hero-section-content-result-2.png)
_hero section output_

To speed things up, I've created the navbar and footer navigation components. Simply [download the directory](https://github.com/Evavic44/sanity-nextjs-site/tree/main/app/(site)/components/global) and import them into the `layout.tsx` file like so:

```js
// app/layout.tsx

import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Navbar from "./components/global/Navbar";
import Footer from "./components/global/Footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Sanity Next.js Portfolio Site",
  description: "A personal portfolio site built with Sanity and Next.js",
  openGraph: {
    images: "add-your-open-graph-image-url-here",
  },
};

export default function RootLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-zinc-900 text-white`}>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  );
}
```

With these components, the home page should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/hero-section-with-component-2.png)
_home page with navbar and footer components_

### Display About Page

Let's build the about page using content from the `getProfile` query as well. In this section you'll need to install a React library called `PortableTextBlock` by Sanity. This library will allow you easily de-structure the block content of the rich text editor.

To install this package run `npm install -D @portabletext/react` and I'll explain how to use it later on. 

Create an `about` folder inside the `app` directory and add a `page.tsx` file inside this new folder. You can also do this quickly using the following command:

```js
mkdir app/about && touch app/about/page.tsx
```

Here's the code snippet for the about page:

```js
// app/about/page.tsx

import Image from "next/image";
import { getProfile } from "@/sanity/sanity.query";
import type { ProfileType } from "@/types";
import { PortableText } from "@portabletext/react";
import { BiEnvelope, BiFile } from "react-icons/bi";

export default async function About() {
  const profile: ProfileType[] = await getProfile();

  return (
    <main className="lg:max-w-7xl mx-auto max-w-3xl md:px-16 px-6">
      {profile &&
        profile.map((data) => (
          <div key={data._id}>
            <section className="grid lg:grid-cols-2 grid-cols-1 gap-x-6 justify-items-center">
              <div className="order-2 lg:order-none">
                <h1 className="lg:text-5xl text-4xl lg:leading-tight basis-1/2 font-bold mb-8">
                  I&apos;m {data.fullName}. I live in {data.location}, where I
                  design the future.
                </h1>

                <div className="flex flex-col gap-y-3 text-zinc-400 leading-relaxed">
                  <PortableText value={data.fullBio} />
                </div>
              </div>

              <div className="flex flex-col lg:justify-self-center justify-self-start gap-y-8 lg:order-1 order-none mb-12">
                <div>
                  <Image
                    className="rounded-2xl mb-4 object-cover max-h-96 min-h-96 bg-top bg-[#1d1d20]"
                    src={data.profileImage.image}
                    width={400}
                    height={400}
                    quality={100}
                    alt={data.profileImage.alt}
                  />

                  <a
                    href={`${data.resumeURL}?dl=${data.fullName}_resume`}
                    className="flex items-center justify-center gap-x-2 bg-[#1d1d20] border border-transparent hover:border-zinc-700 rounded-md duration-200 py-2 text-center cursor-cell font-medium"
                  >
                    <BiFile className="text-base" /> Download Resumé
                  </a>
                </div>

                <ul>
                  <li>
                    <a
                      href={`mailto:${data.email}`}
                      className="flex items-center gap-x-2 hover:text-purple-400 duration-300"
                    >
                      <BiEnvelope className="text-lg" />
                      {data.email}
                    </a>
                  </li>
                </ul>
              </div>
            </section>

            <section className="mt-24 max-w-2xl">
              <h2 className="font-semibold text-4xl mb-4">Expertise</h2>
              <p className="text-zinc-400 max-w-lg">
                I&apos;ve spent few years working on my skills. In no particular
                order, here are a few of them.
              </p>

              <ul className="flex flex-wrap items-center gap-3 mt-8">
                {data.skills.map((skill, id) => (
                  <li
                    key={id}
                    className="bg-[#1d1d20] border border-transparent hover:border-zinc-700 rounded-md px-2 py-1"
                  >
                    {skill}
                  </li>
                ))}
              </ul>
            </section>
          </div>
        ))}
    </main>
  );
}

```

* Similar to the home page, we're also fetching the data from the `getProfile` query and assigning the `ProfileType` for type safety.
* The profile data is also mapped to get the individual properties: `fullName`, `location`, `fullBio`, `profileImage`, `resumeURL`, `email`, and `skills` array.
* The portable text editor was de-structured using the `<PortableText />` component which takes in a value prop that receives the content of the rich text editor.

Adding the image from Sanity's CDN should throw an error in Next.js since you haven't added Sanity's image source hostname in your `next.config.ts` file. Here's how to do it in Next.js 13:

```js
// next.config.ts

/** @type {import('next').NextConfig} */
const nextConfig = {};

module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "cdn.sanity.io",
        port: "",
      },
    ],
  },
};

```

Here's the resulting output:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/about-3.png)
_About page_

### Work Experience

In a typical portfolio site, you may need to create a list of past work experience. This is what the schema would look like:

Create a `schemas/job.ts` file and paste the following code:

```js
// schemas/job.ts

import { BiBriefcase } from "react-icons/bi";

const job = {
  name: "job",
  title: "Job",
  type: "document",
  icon: BiBriefcase,
  fields: [
    {
      name: "name",
      title: "Company Name",
      type: "string",
      description: "What is the name of the company?",
    },
    {
      name: "jobTitle",
      title: "Job Title",
      type: "string",
      description: "Enter the job title. E.g: Software Developer",
    },
    {
      name: "logo",
      title: "Company Logo",
      type: "image",
    },
    {
      name: "url",
      title: "Company Website",
      type: "url",
    },
    {
      name: "description",
      title: "Job Description",
      type: "text",
      rows: 3,
      description: "Write a brief description about this role",
    },
    {
      name: "startDate",
      title: "Start Date",
      type: "date",
    },
    {
      name: "endDate",
      title: "End Date",
      type: "date",
    },
  ],
};

export default job;

```

To expose this new schema file to the studio, add it to the `schemaTypes` array inside the `schemas/index.ts` and you should see it in your studio. 

Here's the resulting output:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/job-schema-7.png)
_job schema fields in sanity studio_

Click the create button and add as many records as you want. Now you can move on to querying the data. 

Similar to how the `profile` schema was queried inside the `sanity.query.ts` file, you will do that for the job schema too: 

```js
// sanity/sanity.query.ts

export async function getJob() {
  return client.fetch(
    groq`*[_type == "job"]{
      _id,
      name,
      jobTitle,
      "logo": logo.asset->url,
      url,
      description,
      startDate,
      endDate,
    }`
  );
}
```

Next add the types for the returned dataset:

```js
// types/index.ts

export type JobType = {
  _id: string;
  name: string;
  jobTitle: string;
  logo: string;
  url: string;
  description: string;
  startDate: Date;
  endDate: Date;
};
```

And then to display it in your front-end, create a `Job.tsx` file inside the `components` directory and add the following code:

```js
// app/components/Job.tsx

import Image from "next/image";
import { getJob } from "@/sanity/sanity.query";
import type { JobType } from "@/types";

export default async function Job() {
  const job: JobType[] = await getJob();

  return (
    <section className="mt-32">
      <div className="mb-16">
        <h2 className="font-semibold text-4xl mb-4">Work Experience</h2>
      </div>

      <div className="flex flex-col gap-y-12">
        {job.map((data) => (
          <div
            key={data._id}
            className="flex items-start lg:gap-x-6 gap-x-4 max-w-2xl relative before:absolute before:bottom-0 before:top-[4.5rem] before:left-7 before:w-[1px] before:h-[calc(100%-50px)] before:bg-zinc-800"
          >
            <a
              href={data.url}
              rel="noreferrer noopener"
              className="min-h-[60px] min-w-[60px] rounded-md overflow-clip relative"
            >
              <Image
                src={data.logo}
                className="object-cover"
                alt={`${data.name} logo`}
                fill
              />
            </a>
            <div className="flex flex-col items-start">
              <h3 className="text-xl font-bold">{data.name}</h3>
              <p>{data.jobTitle}</p>
              <small className="text-sm text-zinc-500 mt-2 tracking-widest uppercase">
                {data.startDate.toString()} - {data.endDate.toString()}
              </small>
              <p className="text-base text-zinc-400 my-4">{data.description}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
```

To view the component, you can import it into the home page:

```js
// Note: This is a truncated version of the home page (app/page.tsx) file to illustrate how the Job component is declared.

import { getProfile } from "@/sanity/sanity.query";
import type { ProfileType } from "@/types";
import HeroSvg from "./icons/HeroSvg";
import Job from "./components/Job"; // import job component

export default async function Home() {
  const profile: ProfileType[] = await getProfile();

  return (
    <main className="max-w-7xl mx-auto lg:px-16 px-6">
      <section> // code truncated for brevity
        <HeroSvg />
      </section>
      <Job /> // declare job component
    </main>
  );
}
```

Here's the resulting output:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/job-description-result-output-3.png)
_work experience section_

By now, you should have a clear understanding of the necessary steps to showcase content with Sanity: **Create schema file, > Query the dataset > Display the content in your application**. 

Let's now focus on configuring data for dynamic routes in your application and leveraging it to construct the projects page.

### Project Schema

As always, you'll start by creating the schema file:

```bash
touch schemas/project.ts
```

Here's the code for the schema fields:

```js
import { BiPackage } from "react-icons/bi";
import { defineField } from "sanity";

const project = {
  name: "project",
  title: "Project",
  description: "Project Schema",
  type: "document",
  icon: BiPackage,
  fields: [
    {
      name: "name",
      title: "Name",
      type: "string",
      description: "Enter the name of the project",
    },
    defineField({
      name: "tagline",
      title: "Tagline",
      type: "string",
      validation: (rule) => rule.max(60).required(),
    }),
    defineField({
      name: "slug",
      title: "Slug",
      type: "slug",
      description:
        "Add a custom slug for the URL or generate one from the name",
      options: { source: "name" },
      validation: (rule) => rule.required(),
    }),
    {
      name: "logo",
      title: "Project Logo",
      type: "image",
    },
    {
      name: "projectUrl",
      title: "Project URL",
      type: "url",
    },
    {
      name: "coverImage",
      title: "Cover Image",
      type: "image",
      description: "Upload a cover image for this project",
      options: { hotspot: true },
      fields: [
        {
          name: "alt",
          title: "Alt",
          type: "string",
        },
      ],
    },
    {
      name: "description",
      title: "Description",
      type: "array",
      description: "Write a full description about this project",
      of: [{ type: "block" }],
    },
  ],
};

export default project;

```

Next, expose the schema to the `schemaTypes` array:

```js
import job from "./job";
import profile from "./profile";
import project from "./project";

export const schemaTypes = [profile, job, project];
```

Visit your studio, click the project schema, and add as many projects as you want. You can download the [asset files](https://github.com/Evavic44/sanity-nextjs-site/tree/main/public) used for each project from the repository.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/project-schema-3.png)
_Sanity studio showing project schema fields_

Here's the query to get all the projects:

```js
// sanity/sanity.query.ts

export async function getProjects() {
  return client.fetch(
    groq`*[_type == "project"]{
      _id, 
      name,
      "slug": slug.current,
      tagline,
      "logo": logo.asset->url,
    }`
  );
}
```

Next, add the types.

```js
// types/index.ts

export type ProjectType = {
  _id: string;
  name: string;
  slug: string;
  tagline: string;
  projectUrl: string;
  logo: string;
  coverImage: {
    alt: string | null;
    image: string;
  };
  description: PortableTextBlock[];
};
```

And then display the content in your front-end.

```bash
mkdir app/projects && touch app/projects/page.tsx
```

This will create a `page.tsx` file inside a directory called project. Here's the code for the projects:

```js
// app/projects/page.tsx

import Image from "next/image";
import Link from "next/link";
import { getProjects } from "@/sanity/sanity.query";
import type { ProjectType } from "@/types";

export default async function Project() {
  const projects: ProjectType[] = await getProjects();

  return (
    <main className="max-w-7xl mx-auto md:px-16 px-6">
      <section className="max-w-2xl mb-16">
        <h1 className="text-3xl font-bold tracking-tight sm:text-5xl mb-6 lg:leading-[3.7rem] leading-tight">
          Featured projects I&apos;ve built over the years
        </h1>
        <p className="text-base text-zinc-400 leading-relaxed">
          I&apos;ve worked on tons of little projects over the years but these
          are the ones that I&apos;m most proud of. Many of them are
          open-source, so if you see something that piques your interest, check
          out the code and contribute if you have ideas for how it can be
          improved.
        </p>
      </section>

      <section className="grid xl:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-5 mb-12">
        {projects.map((project) => (
          <Link
            href={`/projects/${project.slug}`}
            key={project._id}
            className="flex items-center gap-x-4 bg-[#1d1d20] border border-transparent hover:border-zinc-700 p-4 rounded-lg ease-in-out"
          >
            <Image
              src={project.logo}
              width={60}
              height={60}
              alt={project.name}
              className="bg-zinc-800 rounded-md p-2"
            />
            <div>
              <h2 className="font-semibold mb-1">{project.name}</h2>
              <div className="text-sm text-zinc-400">{project.tagline}</div>
            </div>
          </Link>
        ))}
      </section>
    </main>
  );
}
```

Here's the resulting output:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/project-page-4.png)
_project page_

### Display Dynamic Routes

Each project card is wrapped in a link that points to their respective page based on the slug: `/projects/${project.slug}`. With this, the dynamic component can be easily created in next.js

Create a folder called `[project]` (wrapped in square brackets) inside the projects directory, and add a `page.tsx` file.

You can also do this via the terminal:

```bash
mkdir app/projects/[project] && touch app/projects/[project]/page.tsx
```

This folder enclosed in square brackets is known as a [dynamic segment](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention) in Next.js, and it allows the component to be mounted based on the params property. 

Since you've already created the project schema type, all that's left is to query the dataset to fetch single projects.

Here's the query to get single projects:

```js
// sanity/sanity.query.ts

export async function getSingleProject(slug: string) {
  return client.fetch(
    groq`*[_type == "project" && slug.current == $slug][0]{
      _id,
      name,
      projectUrl,
      coverImage { alt, "image": asset->url },
      tagline,
      description
    }`,
    { slug }
  );
}
```

To fetch the slug from the route, we've added a parameter called `slug` into the function, which will allow the `getSingleProject` function to be called with the respective slug using the Next.js [params property](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#context-parameter).

```js
// app/projects/[project]/page.tsx

import Image from "next/image";
import { Metadata } from "next";
import { getSingleProject } from "@/sanity/sanity.query";
import type { ProjectType } from "@/types";
import { PortableText } from "@portabletext/react";
import fallBackImage from "@/public/project.png";

type Props = {
  params: {
    project: string;
  };
};

// Dynamic metadata for SEO
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const slug = params.project;
  const project: ProjectType = await getSingleProject(slug);

  return {
    title: `${project.name} | Project`,
    description: project.tagline,
    openGraph: {
      images: project.coverImage?.image || "add-a-fallback-project-image-here",
      title: project.name,
      description: project.tagline,
    },
  };
}

export default async function Project({ params }: Props) {
  const slug = params.project;
  const project: ProjectType = await getSingleProject(slug);

  return (
    <main className="max-w-6xl mx-auto lg:px-16 px-8">
      <div className="max-w-3xl mx-auto">
        <div className="flex items-start justify-between mb-4">
          <h1 className="font-bold lg:text-5xl text-3xl lg:leading-tight mb-4">
            {project.name}
          </h1>

          <a
            href={project.projectUrl}
            rel="noreferrer noopener"
            className="bg-[#1d1d20] text-white hover:border-zinc-700 border border-transparent rounded-md px-4 py-2"
          >
            Explore
          </a>
        </div>

        <Image
          className="rounded-xl border border-zinc-800"
          width={900}
          height={460}
          src={project.coverImage?.image || fallBackImage}
          alt={project.coverImage?.alt || project.name}
        />

        <div className="flex flex-col gap-y-6 mt-8 leading-7 text-zinc-400">
          <PortableText value={project.description} />
        </div>
      </div>
    </main>
  );
}
```

Since the data coming from the dataset is a single project and not an array, no de-structuring is required.

Here's the resulting output:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/dynamic-project-page-2.gif)
_Dynamic project page_

### Add Loading States

Next.js 13 introduced a special file `loading.js` that helps you create an instant loading state from the server while the content of a route segment loads. This helps users understand the app is responding and provides a better user experience.

With this special file, you can create a loading state that mimics the UI of the single project page easily.

Create a `loading.tsx` file inside the `[project]` directory and add the code snippet:

```js
// projects/[project]/loading.tsx

export default function Loading() {
  return (
    <div className="max-w-3xl mx-auto lg:px-0 px-8">
      <div className="flex items-center justify-between mb-6">
        <span className="w-52 h-11 bg-[#1d1d20] rounded-sm animate-pulse"></span>
        <span className="w-20 h-11 bg-[#1d1d20] rounded-sm animate-pulse"></span>
      </div>
      <div className="w-full h-96 mb-8 bg-[#1d1d20] rounded-sm animate-pulse"></div>
      <div className="flex flex-col gap-y-2">
        <span className="w-full h-5 bg-[#1d1d20] rounded-sm animate-pulse"></span>
        <span className="w-full h-5 bg-[#1d1d20] rounded-sm animate-pulse"></span>
      </div>
    </div>
  );
}
```

Here's the resulting output:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/loading-state-2.gif)
_dynamic project page showing next.js instant loading state_

## Fix Studio Layout

You may have noticed the `navbar` and `footer` components are showing up in the studio route. This is because these components we're defined in the root layout —which applies to all routes in the application.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/studio-component-ui-error-2.png)
_navbar and footer components in studio page_

To fix this, you'll have to create a separate `layout.tsx` file for the studio component:

Create two folders wrapped in parenthesis inside the `app` directory. Name one folder `(site)`, and the other `(studio)`. These folders are wrapped in parenthesis to prevent Next.js from mounting them as routes.

Move all the files in the app directory that relates to the next app except the `studio` folder, `global.css` and `favicon.ico` into the `(site)` directory, and then move the studio folder inside the `(studio)` directory.

The only files that will live in the app root is `global.css` and `favicon.ico`.

Here's what your new folder structure should look like:

```bash
app/
├── (site)/
│   ├── about/
│   ├── components/
│   ├── icons/
│   ├── projects/
│   ├── layout.tsx
│   └── page.tsx
├── (studio)/
│   └── studio/
├── favicon.ico
└── global.css
```

Once completed, create a `layout.tsx` file inside the `(studio)` directory and paste the following code snippet inside:

```js
import "../globals.css";

export default function StudioLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

```

Update all the imports that may have changed, run your server again and you should see your studio up and running, without the components.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sanity-studio-without-navbar-components-1.png)
_Studio page without navbar and footer components_

## Step 7: Deployment

Deploying a Sanity powered Next.js application is a pretty straightforward process. Follow this guide to [set-up your account and deploy with Vercel](https://vercel.com/docs/getting-started-with-vercel/import).

After successfully deploying your site, visit the studio route; `your-site-name/studio`, and you should get a prompt to add the URL to the CORS setting in Sanity:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/add-hosted-site-URL-to-sanity-cors-settings.png)
_Sanity CORS settings prompt_

Simply click "continue" and follow the on-screen instructions to do so. If successful, you should be able to see your studio.

## Setup Sanity Webhooks for Studio Update

Updates made to your site would be triggered only on build time. What this means is that if you update a field in your studio using the hosted link, you would have to manually trigger a deployment on Vercel to see the changes.

Having to trigger the deployment server each time can be a cumbersome task, especially when building for a client. 

In this section, I'll guide you through the steps to manually deploy your site whenever a change is made to your studio using Sanity [GROQ-powered Web Hooks](https://www.sanity.io/docs/webhooks).

### Create a Deploy Hook on Vercel

First, you will need the URL endpoint from your hosting service to trigger the deployment.

Navigate to your project settings on Vercel and click the **Git** tab. Under the **Deploy Hooks** section, choose a name for your hook and the select the branch that will be deployed when the generated URL is requested.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/create-hook-endpoint-on-vercel-1.png)
_creating the hook_

Submit the form and copy the URL endpoint generated by Vercel.

### Trigger Hook Using Sanity GROQ-powered Webhooks

Visit [sanity.io/manage](https://www.sanity.io/manage), pick your project, navigate to the **API** section and click on the "Create webhook" button.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sanity-api-tab-1.png)
_Sanity GROQ-powered Webhooks_

Fill in the form with information about the hook you want to create. 

* `Name`:  Portfolio Deployment.
* `Description`: Trigger rebuild when portfolio content is created, updated, and deleted.
* `URL`: [Paste the URL endpoint generated by Vercel here].
* `Dataset`: The dataset to apply the hook to.
* `Trigger on`: Check the **"create"**, **"update"**, and **"delete"** boxes.

Leave `filter` and `projection` inputs blank so the hook will be applied to all documents, and for the rest of the fields, leave it as is and hit save.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sanity-groq-powered-hook-created-2.png)
_sanity groq powered hook created_

Now visit your hosted studio and update any document. Once you click publish, this should trigger the deploy hook and update your site when completed.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sanity-hook-trigger-build-on-vercel-2.png)
_deploy hook triggering deployment on Vercel_

Another good alternative to setting up live updates in your Sanity/Next.js app is using [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/pages/building-your-application/data-fetching/incremental-static-regeneration), which is a better option if you're building a large scale application.

And that's it! You can see the [Live Preview here](https://sanity-nextjs-site.vercel.app) and find the [GitHub URL here](https://github.com/Evavic44/sanity-nextjs-site).

## What Next?

Although this tutorial covered a lot of useful information, there are still many more possibilities with Sanity that you can explore. 

You can customize your studio, integrate third-party APIs, build a storefront with Shopify, and much more.

If you found this article enjoyable and want to dive deeper into the world of Sanity, I recommend checking out the following resources:

* [Customizing the Portable Text Editor](https://www.sanity.io/docs/customizing-the-portable-text-editor)
* [How to Create a Singleton Document](https://www.sanity.io/guides/singleton-document)
* [Syntax Highlight Code Block](https://www.sanity.io/plugins/code-input)

Thanks for reading. Share, and subscribe to my blog for future updates.

[GitHub](https://github.com/Evavic44) | [Twitter](https://twitter.com/victorekea) | [Blog](https://eke.hashnode.dev) | [LinkedIn](https://www.linkedin.com/in/victorekeawa/)

