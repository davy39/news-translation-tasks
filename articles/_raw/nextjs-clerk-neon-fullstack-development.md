---
title: Full Stack Development with Next.js, Clerk, and Neon Postgres
subtitle: ''
author: Ankur Tyagi
co_authors: []
series: null
date: '2024-07-10T15:31:12.000Z'
originalURL: https://freecodecamp.org/news/nextjs-clerk-neon-fullstack-development
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Orange---Yellow-Gradient-Make-Design-Blog-Banner--77-.png
tags:
- name: database
  slug: database
- name: full stack
  slug: full-stack
- name: Next.js
  slug: nextjs
seo_title: null
seo_desc: 'Full stack development is constantly evolving, with new developer tools
  and products being introduced that allow us to build secure and reliable applications
  more efficiently.

  In this tutorial, I’ll walk you through how to build highly performant web...'
---

Full stack development is constantly evolving, with new developer tools and products being introduced that allow us to build secure and reliable applications more efficiently.

In this tutorial, I’ll walk you through how to build highly performant web applications with [Neon – a serverless PostgreSQL](https://neon.tech) database designed for the cloud. You'll also learn how to perform CRUD (Create, Read, Update, and Delete) operations with Neon.

By the end of this tutorial, you will have the basic knowledge required to start building advanced and scalable web applications with Neon.

## **Table of Contents:**

* [What is Neon?](#heading-what-is-neon)
* [Why Neon?](#heading-why-neon)
* [How to add Neon to a Next.js app](#heading-how-to-add-neon-to-a-nextjs-app)
* [How to set up Neon Serverless Driver with Drizzle ORM in Next.js](#heading-how-to-set-up-neon-serverless-driver-with-drizzle-orm-in-nextjs)
* [How to Build the Application Interface with Next.js](#heading-how-to-build-the-application-interface-with-nextjs)
* [How to Authenticate Users with Clerk](#heading-how-to-authenticate-users-with-clerk)
* [CRUD Operations with the Neon Database](#heading-crud-operations-with-the-neon-database)
* [Conclusion](#heading-conclusion)
* [Next Steps](#heading-next-steps)

## What is Neon?

[Neon](https://github.com/neondatabase/neon) is an open-source, scalable, and efficient Postgres DB that separates compute from storage. This means that database computation processes (queries, transactions, and so on) are handled by one set of resources (compute), while the data itself is stored on a separate set of resources (storage). 

This architecture allows for greater scalability and performance, making Neon a solid choice for modern web applications.

![Neon - a serverless Postgres database](https://lh7-us.googleusercontent.com/docsz/AD_4nXcT4hh-liS2uYYcatl8jC6h9gFqArEw113_WaPzoTFxeps_G97JIVhJKVSQq5DC52NJ0GOoQm4sYL5QhyLhC_e_xocDjSp7iks6j8kv6WSnhRzLVy8TxftshzFnwK238QuVsGdnnBpL_nLDmXju3klwlB6T?key=4GdX_KHTwBEvJEyZsT7b3Q)
_[Neon - a serverless Postgre](https://neon.tech)s database_

### 3 Things to Remember About Neon:

* 🐘 **Postgres**: Neon is built on the foundation of Postgres. It supports the same extensions, drivers, and SQL syntax as Postgres, ensuring familiarity and ease of use.
* ☁️ **Serverless**: Neon operates on a serverless model. Your database is represented as a simple URL, and Neon automatically scales up and down based on workload demands. Say goodbye to over-provisioning.
* 🌱 **Branching**: Just like version control for code, Neon allows you to create instant, isolated copies of your data. This feature is invaluable for development, testing, and maintaining separate environments.

## Why Neon?

Neon brings the serverless experience to Postgres. Developers can build faster and scale their products effortlessly, without the need to dedicate big teams or big budgets to the database.

Neon supports [multiple languages and frameworks](https://neon.tech/docs/introduction#framework-and-language-quickstarts) – but what are the unique features that make Neon stand out?

### Instant branching and auto-scaling

[Neon](https://neon.tech/blog/why-you-want-a-database-that-scales-to-zero) allows you to [create database branches instantly](https://neon.tech/branching) for testing, development, and staging environments. This lets you experiment without affecting the production database. 

It also provides an [auto-scaling capability](https://neon.tech/docs/introduction/autoscaling) that automatically adjusts resources based on the application's workload, ensuring optimal performance and cost-efficiency.

![Neon DB Main Branch Dashboard](https://lh7-us.googleusercontent.com/docsz/AD_4nXc1HSzmptXUYsu49JPbWSizwp64G-JVME-7kmmwSKNYLcc1wUmwWXvBa6kuVxncpyazqSPgj_N4ABZddjNG2rDTHE8MFIGm3yKy1DPpiV6C7GZ1tOcTzOFkvtDwpleeJZC--V4efudtYnPe-XKs8K2P740R?key=4GdX_KHTwBEvJEyZsT7b3Q)
_Neon DB Main Dashboard_

### Support for AI applications

Neon [supports AI and machine learning applications](https://neon.tech/ai) by providing a high-performance and scalable infrastructure. It enables you to perform semantic and similarity searches in Postgres and handles complex queries and large datasets efficiently, making it ideal for AI or LLM applications.

### Open-source

Neon is backed by a [vibrant community](https://github.com/neondatabase/neon) of Postgres hackers, systems engineers, and cloud engineers who are all huge fans of Postgres. 

As an open-source platform, Neon offers transparency and flexibility. You can also reach out to the team and contributors to ask questions, contribute, and help improve the software.

### Serverless Architecture

[Neon](https://neon.tech/blog/architecture-decisions-in-neon) eliminates the need for manual server management, allowing you to focus on building applications rather than maintaining infrastructure. Its serverless nature provides on-demand scalability, ensuring that your application can handle varying loads without manual intervention.

### Built upon Postgres

Postgres is one of the most reliable open-source relational [database](https://neon.tech/blog/get-page-at-lsn) systems. Neon inherits all the advanced features, stability, and performance optimizations of Postgres, including support for ACID transactions, advanced SQL, and NoSQL/JSON, to create a cheaper and more efficient database for cloud environments.

## How to Add Neon to a Next.js App

Neon supports multiple frameworks and libraries and provides clear and detailed documentation on adding Neon to them. The Neon serverless driver enables us to connect and interact with Neon in a Next.js application.

Before we proceed, let’s [create a Neon account and project](https://neon.tech/docs/guides/nextjs).

![Neon DB Projects Overview](https://lh7-us.googleusercontent.com/docsz/AD_4nXeLMMmCdF3yK_mflMt4mqz3woiTLibcrGCMK5-AE1f2KftVKYduH39BybuVdu68G2am8uwDWHJUyisFittXeqCmcgxNyhcZXIiXHjxIIu-eymmM_-VVdAMW0LWTVA7NrXI-QXNEYso3Sj1FrLX0tvSP6yNK?key=4GdX_KHTwBEvJEyZsT7b3Q)
_Neon DB Projects Overview: View and manage all your projects in one place._

Within your project dashboard, you'll find a database connection string. You'll use this to interact with your Neon database.

![Neon DB Project Dashboard](https://lh7-us.googleusercontent.com/docsz/AD_4nXfpIPj10xMleoJEKIMFghRGp2ofgC0zJEA0C2ExMr2ijz673RM_45Kuh1RXVKkEn_uW-hU6-YIPd35C73gYMZtN_7lvChQ4MSK47CIWovh8MyUzRQluguEhAEXdvRZ8wxpOLINIyVfp50u1gIOf3foBAzg3?key=4GdX_KHTwBEvJEyZsT7b3Q)
_Neon DB Project Dashboard: Manage database settings with ease from the project dashboard._

Create a TypeScript Next.js project by running the following code snippet in your terminal:

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npx create-next-app neon-blog-with-clerk</span></p></td></tr></tbody></table>

Next, install the Neon Serverless package:

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npm install @neondatabase/serverless</span></p></td></tr></tbody></table>

Create a .env.local file and copy your database connection string into the file:

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">NEON_DATABASE_URL=</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"postgres://&lt;user&gt;:&lt;password&gt;@&lt;endpoint_hostname&gt;.neon.tech:&lt;port&gt;/&lt;dbname&gt;?sslmode=require"</span></p></td></tr></tbody></table>

Create a 'db' folder containing an index.ts file within the Next.js app directory and copy the code snippet below into the file:

```javascript
import { neon } from '@neondatabase/serverless';

if (!process.env.NEON_DATABASE_URL) {
  throw new Error('NEON_DATABASE_URL must be a Neon postgres connection string')
}

export const getDBVersion = async() => {
    const sql = neon(process.env.NEON_DATABASE_URL!);
    const response = await sql`SELECT version()`;
    return { version: response[0].version }
}
```

Convert the app/page.tsx file to a server component and execute the `getDBVersion()` function:

```javascript
import { getDBVersion } from "./db";

export default async function Home() {
    const { version } = await getDBVersion();
    console.log({version})
    
   return (<div>{/** — UI elements — */}</div>)

}
```

The `getDBVersion()` function establishes a connection with the Neon database and allows us to run SQL queries using the Postgres client. This function returns the database version, which is then logged to the console.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">{</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp; version: </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">'PostgreSQL 16.3 on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit'</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">}</span></p></td></tr></tbody></table>

Congratulations – you’ve successfully added Neon to your Next.js application.

But interacting with the Neon database by writing SQL queries directly can require extra learning or introduce complexities for developers who are not familiar with SQL. It can also lead to errors or performance issues when performing complex queries. 

This is why Neon supports database ORMs such as Drizzle ORM, which provide a higher-level interface for interacting with the database. [Drizzle ORM](https://orm.drizzle.team/docs/overview) enables you to write complex query functions and interact with the database easily using TypeScript.

## How to Set Up Neon Serverless Driver with Drizzle ORM in Next.js

[Drizzle ORM](https://orm.drizzle.team/docs/overview) lets you query data and perform various operations on the database using simple TypeScript query commands. It is lightweight, typesafe, and easy to use.

First, you'll need to install the [Drizzle Kit](https://orm.drizzle.team/kit-docs/overview) and the [Drizzle ORM](https://orm.drizzle.team/docs/overview) package.

Drizzle Kit lets you manage the database schema and migrations.

```bash
npm i drizzle-orm
npm i -D drizzle-kit
```

Inside the db folder, add an actions.ts, and schema.ts file:

```bash
cd db
touch actions.ts schema.ts
```

Add the code snippet below into the db/schema.ts file. It contains the database schema.

```javascript
import {  text, serial, pgTable, timestamp } from "drizzle-orm/pg-core";

export const postsTable = pgTable("posts", {
    id: serial("id").primaryKey().notNull(),
    content: text("content").notNull(),
    author: text("author").notNull(),
    author_id: text("author_id").notNull(),
    title: text("title").notNull(),
    created_at: timestamp("created_at").defaultNow(),
    slug: text("slug").notNull(),
});
```

Update the db/index.ts file to connect to the Neon database and export the Drizzle instance (db). This will be used to execute typesafe SQL queries against your Postgres database hosted by Neon.

```javascript
import { neon } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';
import { postsTable } from './schema';


if (!process.env.NEON_DATABASE_URL) {
  throw new Error('DATABASE_URL must be a Neon postgres connection string')
}
const sql = neon(process.env.NEON_DATABASE_URL!);

export const db = drizzle(sql, {
  schema: { postsTable }
});
```

Next, create a drizzle.config.ts file at the root of the Next.js folder and add the following configuration:

```javascript
import type { Config } from 'drizzle-kit';
import * as dotenv from "dotenv";

dotenv.config();

if (!process.env.NEON_DATABASE_URL) throw new Error('NEON DATABASE_URL not found in environment');

export default {
  schema: './src/app/db/schema.ts',
  out: './src/app/db/migrations',
 dialect: "postgresql",
  dbCredentials: {
    url: process.env.NEON_DATABASE_URL,
 },
  strict: true,
} satisfies Config;
```

The drizzle.config.ts file contains all the information about your database connection, migration folder, and schema files. 

Finally, update the package.json file to include the Drizzle Kit commands for generating database migrations and updating the tables.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">{</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> "scripts" : {</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp; "migrate": </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"npx drizzle-kit generate -- dotenv_config_path='.env.local'"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">,</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp; "db-create": </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"npx drizzle-kit push -- dotenv_config_path='.env.local'"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> }</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">}</span></p></td></tr></tbody></table>

![Neon DB Tables Dashboard](https://www.freecodecamp.org/news/content/images/2024/07/image-8.png)
_Neon DB Tables Dashboard: Effortlessly manage your database tables and view all data._

## How to Build the Application Interface with Next.js

In this section, you’ll learn how to build a blog application that allows users to read posts and authenticate authors, enabling them to create and delete posts from the Neon database. 

The application is divided into 3 pages:

* Home Page: displays all the available blog posts.
* Post Details Page (/posts/[slug]): displays the content of a particular blog post.
* Create Post Page (/posts/create): allows authors to create new blog posts.

Install the following packages:

```javascript
npm install date-fns react-simplemde-editor easymde react-markdown remark-gfm dotenv


```

The [Date Fns package](https://github.com/date-fns/date-fns) allows us to convert the posts' timestamps to human-readable forms for display within the application. The [React SimpleMDE Editor](https://www.npmjs.com/package/react-simplemde-editor) provides a WYSIWYG editor for creating content in markdown formats using an interactive editor, and the [React Markdown package](https://www.npmjs.com/package/react-markdown) converts the markdown texts to their corresponding plain formats.

Next, create a utils.ts file within the Next.js app folder and copy the code snippet below into the file:

```javascript
import { format } from "date-fns";

export const formatDateString = (dateString: Date | null): string => {
    if (!dateString) return "";
    const date = new Date(dateString);
    const formattedDate = format(date, "MMMM do yyyy, h:mma");
    return formattedDate;
};

export const slugifySentences = (sentence: string): string => {
    const slug = sentence
 .toLowerCase()
 .replace(/[^a-z0-9\s-]/g, "")
 .replace(/\s+/g, "-");

    // Generate 5 random letters
    const randomLetters = Array.from({ length: 5 }, () =>
        String.fromCharCode(97 + Math.floor(Math.random() * 26))
 ).join("");

    return `${slug}-${randomLetters}`;
};
```

The `formatDateString` function accepts a Date object and returns the date and time in a human-readable format using the date-fns package. The `slugifySentences` function creates a slug for each post using the post's title, which is useful for implementing the routes for each post.

Copy the code snippet below into the app/page.tsx file:

```javascript
import Link from "next/link";
import { formatDateString, slugifySentences } from "./utils";

interface Post {
    author_id: string;
    title: string;
    content: string;
    author: string;
    slug: string;
    id: number | null;
    created_at: Date | null;
}

export default async function Home() {
    // dummy posts
    const posts: Post[] = [
        {
            author_id: "1",
            title: "Welcome to Neon Tutorial",
            content: "This is a test post",
            author: "John Doe",
            slug: slugifySentences("Welcome to Neon Tutorial"),
            id: 1,
            created_at: new Date(),
        },
        {
            author_id: "1",
            title: "Hello World",
            content: "This is a test post",
            author: "Jane Doe",
            slug: slugifySentences("Hello World"),
            id: 2,
            created_at: new Date(),
        },
    ];

    // shorten posts with longer title
    const shortenText = (text: string): string => {
        return text.length <= 55 ? text : text.slice(0, 55) + "...";
    };

    return (
        <div>
            <main className='md:px-8 py-8 px-4 w-full bg-white'>
                {posts?.map((post) => (
                    <Link
                        href={`/posts/${post.slug}`}
                        className='rounded w-full border-[1px] p-4 text-blue-500 hover:bg-blue-50 hover:drop-shadow-md transition-all duration-200 ease-in-out flex items-center justify-between gap-4 mb-4'
                        key={post.id}
                    >
                        <h3 className='text-lg font-semibold'>{shortenText(post.title)}</h3>
                        <div className='flex items-center justify-between'>
                            <p className='text-xs text-gray-500'>
                                {formatDateString(post?.created_at)}
                            </p>
                        </div>
                    </Link>
                ))}
            </main>
        </div>
    );
}

```

The app/page.tsx file represents the home page of the application and displays all the available posts.

![blog-app](https://www.freecodecamp.org/news/content/images/2024/07/image-5.png)
_It's live - see the power of serverless PostgreSQL and Next.js_

Next, add the routes for creating posts and reading the contents of each post. Within the Next.js app folder, create a posts directory containing /posts/create and /posts/[slug] subdirectories.

Create a page.tsx file within the /posts/create folder and copy the code snippet below into the file:

```javascript
use client";
import { useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import SimpleMDE from "react-simplemde-editor";
import "easymde/dist/easymde.min.css";
import { slugifySentences } from "@/app/utils";

export default function PostCreate() {
    const [publishing, setPublishing] = useState<boolean>(false);
    const [content, setContent] = useState<string>("");
    const [title, setTitle] = useState<string>("");
    const router = useRouter();

    const onChangeContent = useCallback((value: string) => {
        setContent(value);
    }, []);

    const handleCreatePost = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log({ title, content });
        router.push("/");
    };

    return (
        <div className='min-h-[100vh]'>
            <main className='md:px-8 py-8 px-4 w-full'>
                <form className='flex flex-col w-full' onSubmit={handleCreatePost}>
                    <label htmlFor='title' className='text-sm text-blue-600'>
                        Title
                    </label>
                    <input
                        type='text'
                        name='title'
                        id='title'
                        value={title}
                        required
                        onChange={(e) => setTitle(e.target.value)}
                        className='px-4 py-3 border-2 rounded-md text-lg mb-4'
                    />

                    <label htmlFor='content' className='text-sm text-blue-600'>
                        Content
                    </label>
                    <SimpleMDE value={content} onChange={onChangeContent} id='content' />

                    <button
                        type='submit'
                        disabled={publishing}
                        className='bg-blue-600 mt-2 text-white py-3 rounded-md'
                    >
                        {publishing ? "Publishing....please wait" : "Publish Post"}
                    </button>
                </form>
            </main>
        </div>
    );
}

```

The /posts/create page renders a form that accepts the title and content of the post, allowing authors to create new blog posts.

![How to Create a Post in Blog App](https://lh7-us.googleusercontent.com/docsz/AD_4nXed0zewJjjPH6pDp2z4E1dZ-F2d717R5LJuqqrqC-8pzv_PAHcNWem1q_19NgnpUoM9hgBa7MhHtFs0fn_kaEMQOXaRHGPPdoIi1qiOovdTbiPSPlut1EX3Yo-2APt3wvwW08K2BrjJ6rx-R3EDEdxfyNwu?key=4GdX_KHTwBEvJEyZsT7b3Q)
_Create your next blog post with ease_

Finally, update the /posts/[slug] page to display each post's content and include a button that allows only the posts' authors to delete posts. (You'll learn how to implement this later in the tutorial.)

```javascript
use client";
import { useRouter, useParams } from "next/navigation";
import ReactMarkdown from "react-markdown";
import { useEffect, useState, useCallback } from "react";
import remarkGfm from "remark-gfm";
import { formatDateString } from "@/app/utils";

export default function Post() {
    const router = useRouter();
    const [loading, setLoading] = useState<boolean>(true);
    const [post, setPost] = useState<Post | null>(null);
    const params = useParams<{ slug: string }>();

    const deletePost = async () => {
        if (confirm("Are you sure you want to delete this post?")) {
            alert(`Delete ${params.slug}`);
            router.push("/");
        }
    };

    return (
        <div>
            <main className='w-full md:px-8 px-4'>
                <header className='mb-6 py-4'>
                    <div className='flex items-center justify-between mb-2'>
                        <h2 className='text-3xl text-blue-700 font-bold'>{post?.title}</h2>

                        <div className='flex items-center'>
                            <button
                                className='px-4 py-2 rounded text-xs bg-red-200 hover:bg-red-40 mr-3'
                                onClick={() => deletePost()}
                            >
                                Delete
                            </button>
                        </div>
                    </div>

                    <div className='flex'>
                        <p className='text-red-500 mr-8 text-sm'>
                            Author: <span className='text-gray-700'>{post?.author}</span>
                        </p>
                        <p className='text-red-500 mr-6 text-sm'>
                            Posted on:{" "}
                            <span className='text-gray-700'>
                                {formatDateString(post?.created_at!)}
                            </span>
                        </p>
                    </div>
                </header>

                <div className='text-sm text-justify'>
                    <ReactMarkdown remarkPlugins={[remarkGfm]}>
                        {post?.content!}
                    </ReactMarkdown>
                </div>
            </main>
        </div>
    );
}

```

The /posts/[slug] page accepts the unique slug for each blog post, fetches the post's content, and allows post authors to delete their own posts.

![Blog Post ](https://www.freecodecamp.org/news/content/images/2024/07/image-4.png)
_Blog Post_

Congratulations! You've completed the user interface for the application.

## How to Authenticate Users with Clerk

[Clerk](https://github.com/clerkinc) is a complete user management platform that enables you to add various forms of authentication to your software applications. It provides easy-to-use, flexible UI components and APIs that can be integrated seamlessly into your application.

Install the [Clerk Next.js SDK](https://clerk.com/docs/quickstarts/nextjs) by running the following code snippet in your terminal.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npm install @clerk/nextjs</span></p></td></tr></tbody></table>

Create a middleware.ts file within the Next.js src folder and copy the code snippet below into the file:

```javascript
import { clerkMiddleware, createRouteMatcher } from "@clerk/nextjs/server";


// the createRouteMatcher function accepts an array of routes to be protected
const protectedRoutes = createRouteMatcher(["/posts/create"]);

// protects the route
export default clerkMiddleware((auth, req) => {
    if (protectedRoutes(req)) {
        auth().protect();
 }
});

export const config = {
    matcher: ["/((?!.*\\..*|_next).*)", "/", "/(api|trpc)(.*)"],
};
```

The `createRouteMatcher` function accepts an array containing routes to be protected from unauthenticated users and the `clerkMiddleware()` function ensures the routes are protected.

Next, import the following Clerk components into the app/layout.tsx file and update the RootLayout function as shown below:

```javascript
import {
    ClerkProvider,
    SignInButton,
    SignedIn,
    SignedOut,
    UserButton,
} from "@clerk/nextjs";
import Link from "next/link";

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <ClerkProvider>
            <html lang='en'>
                <body className={inter.className}>
                    <nav className='w-full py-4 border-b-[1px] md:px-8 px-4 text-center flex items-center justify-between sticky top-0 bg-white z-10 '>
                        <Link href='/' className='text-xl font-extrabold text-blue-700'>
                            Neon Blog
                        </Link>

                        <div className='flex items-center gap-5'>
                            {/*-- if user is signed out --*/}
                            <SignedOut>
                                <SignInButton mode='modal' />
                            </SignedOut>
                            {/*-- if user is signed in --*/}
                            <SignedIn>
                                <Link href='/posts/create' className=''>
                                    Create Post
                                </Link>
                                <UserButton showName />
                            </SignedIn>
                        </div>
                    </nav>

                    {children}
                </body>
            </html>
        </ClerkProvider>
    );
}

```

When a user is not signed in, the [Sign in button](https://clerk.com/docs/components/unstyled/sign-in-button) component is rendered. 

![Clerk UI](https://www.freecodecamp.org/news/content/images/2024/07/image-3.png)
_Seamless sign-ups redefined with Clerk UI_

Then, after signing into the application, the Clerk [User Button component](https://clerk.com/docs/components/user/user-button) and a link to create a new post are displayed.

![Clerk's User Button component](https://www.freecodecamp.org/news/content/images/2024/07/image-17.png)
_After sign-in: Use Clerk's User Button to create a new post_

Next, create a [Clerk account](https://clerk.com/) and add a new application project.

![Clerk's sleek UI dashboard](https://www.freecodecamp.org/news/content/images/2024/07/image-7.png)
_Clerk's sleek UI dashboard_

Select username as the authentication method and create the Clerk project.

![clerk-dashboard](https://www.freecodecamp.org/news/content/images/2024/07/image-6.png)
_Clerk's sleek UI dashboard_

Finally, add your Clerk publishable and secret keys into the .env.local file.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=&lt;your_publishable_key&gt;</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">CLERK_SECRET_KEY=&lt;your_secret_key&gt;</span></p></td></tr></tbody></table>

Clerk provides various ways to [read user's data](https://clerk.com/docs/references/nextjs/read-session-data) on the client and the server, which is essential for identifying users within the application.

## CRUD Operations with the Neon Database

In this section, you’ll learn how to perform CRUD (Create, Read, Update, Delete) operations with the Neon database. These fundamental operations are essential for interacting with and managing data within any application. 

The db/actions.ts file will contain the CRUD operations. Add the following code snippet to the file:

```javascript
import { db } from ".";
import { postsTable } from './schema';
import { desc, eq } from "drizzle-orm";

// add a new row to the posts table
export const createPost = async (post: Post) => {
    await db.insert(postsTable).values({
        content: post.content,
        author: post.author,
        author_id: post.author_id,
        title: post.title,
        slug: post.slug,
    });
};

// get all the posts
export const getAllPosts = async () => {
    return await db.select().from(postsTable).orderBy(desc(postsTable.created_at));
};

// get a post using its slug
export const getSinglePost = async (slug: string) => {
    return await db.query.postsTable.findFirst({
        where: (post, { eq }) => eq(post.slug, slug)
    });
};

// delete a post
export const deletePost = async (id: number) => {
    await db.delete(postsTable).where(eq(postsTable.id, id));
};

// update a post's content
export const updatePost = async (content: string, id: number) => {
    await db.update(postsTable)
        .set({ content: content })
        .where(eq(postsTable.id, id));
};

```

From the code snippet above:

* This `createPost` function takes a post object as an argument and inserts a new row into the `postsTable` with the specified post content, author, author ID, title, and slug.
* The `getAllPosts` function retrieves all the posts from the `postsTable` and sorts them in descending order by their creation date (created_at).
* This `getSinglePost` function takes a slug as an argument and retrieves the first post that matches the given slug from the `postsTable`. The slug is unique, so it will return a single object.
* This `deletePost` function takes an id as an argument and deletes the post with the matching ID from the `postsTable`.
* This `updatePost` function accepts `content` and a post's `id` as arguments and updates the post's content with the matching ID in the `postsTable`.

Finally, you can execute the CRUD functions on the server via API endpoints or [Next.js server fetch requests](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating#fetching-data-on-the-server-with-fetch). 

For instance, you can fetch all the existing blog posts within the Neon database and display them within the application using the Next.js server data fetching method:

```javascript
import { getAllPosts } from "./db/actions";

const getPosts = async () => await getAllPosts()

export default async function Home() {
    const posts = await getPosts()

    return (<div>{/** -- UI elements --*/}</div>)
}
```

You can also create a Next.js API endpoint that returns all the available blog posts. Create a /api/posts/all endpoint that returns the posts:

```javascript
import { getPosts } from "@/app/db/actions";
import { NextRequest, NextResponse } from "next/server";

export async function POST() {


    try {
        const data = await getPosts()
        return NextResponse.json({ message: "Post fetched", data }, { status: 200 });
 } catch (err) {
        return NextResponse.json(
 { message: "Post not available", err },
 { status: 400 }
 );
 }
}
```

Congratulations! You’ve completed the project for this tutorial.

You can find the code for the app we built [here](https://github.com/tyaga001/serverless-postgres-nextjs-handbook).

## Conclusion

In this tutorial, you’ve learned what a Neon database is, how to create one, and how to perform CRUD operations with Neon and Drizzle ORM in a Next.js application.

Neon's serverless architecture, combined with its scalability and performance optimizations, makes it an excellent choice for modern web applications. Neon also provides a smooth developer experience and a community of passionate individuals ready to help you achieve your application goals. Thank you for reading.

## Next Steps

By now, you should have a good understanding of how to build full-stack applications with Neon and Next.js.

If you'd like to learn more about how you can leverage Neon to build advanced and scalable applications, you can check out the following resources:

* [Neon documentation](https://neon.tech/docs/introduction)
* [Neon example projects](https://github.com/neondatabase/examples)
* [How to integrate Neon with Vercel](https://neon.tech/docs/guides/vercel)
* [How to import your data from a Postgres database to Neon](https://neon.tech/docs/import/import-from-postgres)

%[https://youtu.be/j4Vak4J10KU?si=pqZIR6gOgD5OgBfB]

## **Thanks for Reading!**

That's it for this tutorial. I hope you learned something new today.

If you did, please share so that it reaches others as well.

You can connect with me on [Twitter](https://twitter.com/TheAnkurTyagi) or subscribe to my [newsletter](https://bytesizedbets.com/). 

### **Want to read more interesting blog posts?**

You can read more tutorials like this one on my **[blog](https://theankurtyagi.com/).**

