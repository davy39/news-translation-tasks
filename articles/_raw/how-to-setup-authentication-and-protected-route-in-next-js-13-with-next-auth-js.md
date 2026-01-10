---
title: How to Setup Authentication and Protected Routes in Next.js 13 with next-auth.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-09T17:54:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-authentication-and-protected-route-in-next-js-13-with-next-auth-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/pexels-pixabay-277576.jpg
tags:
- name: Application Security
  slug: application-security
- name: authentication
  slug: authentication
- name: Next.js
  slug: nextjs
seo_title: null
seo_desc: 'By Olasunkanmi Balogun

  This guide demonstrates the straightforward process of incorporating authentication
  into your Next.js app using the next-auth.js library. While the library provides
  numerous options (providers), this tutorial focuses on the imp...'
---

By Olasunkanmi Balogun

This guide demonstrates the straightforward process of incorporating authentication into your `Next.js` app using the [`next-auth.js`](https://next-auth.js.org/) library. While the library provides numerous options (providers), this tutorial focuses on the implementation using the Google Provider.

You'll also gain insight into effortlessly setting up protected routes within your application, a task made easy by the `next-auth.js` library.

When you are ready, let's dive in.

## How to Set Up the `next-auth.js` Library

Once your `Next.js` application is up and running, we're ready to dive in.

Quick note: I'll be referencing the "app" directory consistently in this guide. If this term is new to you, take a moment to consult the [`Next.js`](https://nextjs.org/) documentation for clarity. If you're utilizing the "pages" directory, fear not, as the implementation is almost identical.

Install the `next-auth.js` library with the following command:

```npm
npm install next-auth
```

Having completed the installation, create an `api` folder in your root app folder, and inside it create an `auth` folder. Finally, create a `[...nextauth]` folder inside the `auth` folder.

Inside the `[...nextauth]` folder, create two files named `route.ts` and `options.ts`.

Your folder structure up to this point should look like this:

![Folder structure image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot--187-.png)

Afterwards, in the `options.ts` file, insert the following code:

```ts
import type { NextAuthOptions } from 'next-auth'
import GoogleProvider from "next-auth/providers/google";

export const options: NextAuthOptions = {
    providers: [
  GoogleProvider({
    clientId: process.env.GOOGLE_CLIENT_ID as string,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET as string,
  })
]
}
```

We imported the `NextAuthOptions` type to ensure the `options` variable is type-safe. 

In order to use Google Provider, we imported `GoogleProvider` from `next-auth` as illustrated above.

The [`options`](https://next-auth.js.org/configuration/options#options) variable is where we embed whichever provider we intend to use from `next-auth.js`. 

Notice that we exported the `options` variable, enabling us to use it throughout the application (although we mostly need it the `route.ts` file). As we delve into the implementation in the `route.ts` file, we'll explore how it is utilized.

To use the Google Provider effectively, you need to get your `clientId` and `clientSecret` properties. Rest assured, we'll delve into this shortly. First, create an `.env` file where you'll assign values to both properties.

`env` files are always at the root folder of your application:

![env file location in the project](https://www.freecodecamp.org/news/content/images/2023/11/2-1.png)

Now, we'll see how you can now get your `clientId` and `clientSecret`. 

Assuming you already have a Google account, follow these easy steps:

1. Visit [Google Cloud Platform](https://cloud.google.com), and click the console button at the top right corner of the navbar.
   
![GCP navbar](https://www.freecodecamp.org/news/content/images/2023/11/3.png)

2. You'll be directed to your console dashboard. On the top left, right after the Google Cloud logo, click the dropdown menu to create a new project:
   
![dropdown menu illustration](https://www.freecodecamp.org/news/content/images/2023/11/4.gif)

3. Assign your project any name you prefer, and then click the "Create" button. Mine will be "Next-auth Tutorial".

4. You will return to your console dashboard, and the same dropdown menu should now display the project you recently created. If it doesn't, click on it and select the project.

5. Assuming everything is in order, scroll down to the "Quick Access" section and choose the "API & Services" card. This action will lead you to the "API & Services" page. In the sidebar of this page, select the "Credentials" option:

![Credentials option](https://www.freecodecamp.org/news/content/images/2023/11/5.png)

6. You will be directed to the "Credentials" page. Here, click the "CONFIGURE CONSENT SCREEN" button:
  
![consent screen button](https://www.freecodecamp.org/news/content/images/2023/11/6.png)

7. This will take you to the consent screen configuration page, where you will determine how you want to configure and register your app. Opt for the "External" option and proceed by clicking the "Create" button:

![consent screen config](https://www.freecodecamp.org/news/content/images/2023/11/7.png)
  
8. Following this, you'll find yourself on the "OAuth Consent Screen" page. Proceed by completing these four steps:

Beginning with the "OAuth Consent Screen" tab, you'll be prompted to modify your app information. The key sections to focus on are "App Information" and "Developer Contact Information." After filling these fields, click the "SAVE AND CONTINUE" button.

You will then transition to the "Scopes" tab. Here, once again, click the "SAVE AND CONTINUE" button.

Next up is the "Test Users" tab. Likewise, proceed by clicking the "SAVE AND CONTINUE" button.

And finally, you'll reach the last tab, the summary tab. Scroll down and select the "BACK TO DASHBOARD" button. 

Upon completing these steps, your dashboard should resemble the following:

![dashboard page](https://www.freecodecamp.org/news/content/images/2023/11/8.png)
   
9. Return to the "Credentials" page, and there, click the "Create Credentials" button. A dropdown menu will appear. Choose the "OAuth Client ID" option:
   
![OAuth Client ID](https://www.freecodecamp.org/news/content/images/2023/11/9-1.gif)  

10. This action will take you to the page where you'll craft your `client ID`. On this page, you'll see a single dropdown field for your application type, which will reveal additional fields based on your selection. Select the "Web Application" option from this dropdown:
    
![web application](https://www.freecodecamp.org/news/content/images/2023/11/10.gif)
   
Scroll down to the "Authorized redirect URI" section and paste the following URI: http://localhost:3000/api/auth/callback/google. Afterwards, hit the "CREATE" button.

11. Lastly, a modal will emerge, displaying your unique `Client ID` and `Client Secret`. Keep in mind that both values are confidential, specific to each user, and must be kept secure. For privacy reasons, both values are blurred in the image below:

![Client ID and Client Secret](https://www.freecodecamp.org/news/content/images/2023/11/11.png)
    
Once you've completed these steps, go back to your code editor and paste the appropriate values of each variable in the `.env` file:

```env
GOOGLE_CLIENT_ID = client ID value
GOOGLE_CLIENT_SECRET = client secret value
```

You'll also need to generate a `NEXT_AUTH_SECRET` key to enhance the security of the authentication process in `next-auth.js`. Generate your secret key by executing the following command in your terminal:

```
openssl rand -base64 32
```

This command will generate a 32-character string. Copy this string and paste it as the value for the `NEXTAUTH_SECRET` variable in your `.env` file. Your final `.env` file should resemble the following:

```env
GOOGLE_CLIENT_ID = client ID value
GOOGLE_CLIENT_SECRET = client secret value
NEXT_AUTH_SECRET = next auth secret
```

After you have successfully implemented your .env variables, paste the following code into your route.ts file:

```ts
import NextAuth from "next-auth/next";
import { options } from "./options";

const handler = NextAuth(options);

export { handler as GET, handler as POST };
```

This ensures that GET and POST requests sent to this endpoint (`api/auth/[...nextauth]`) will be handled by the `next-auth` library.

To conclude, restart your application. It's important to note that the `next-auth.js` library won't be actively engaged at this point. The reason is that you haven't yet implemented protected routes for it to safeguard your pages. We'll explore this aspect next.

## How to Implement Protected Routes with `next-auth.js`

With the use of `Next.js`'s [middleware](https://nextjs.org/docs/pages/building-your-application/routing/middleware), protecting routes is very easy. 

Begin by creating a `middleware.ts` file in the root `src` folder.

![middleware.ts file location](https://www.freecodecamp.org/news/content/images/2023/11/12.png)

To protect all your pages uniformly, insert the following code snippet:

```ts!
export { default } from 'next-auth/middleware'
```

Alternatively, you can selectively secure specific pages by utilizing a `matcher`. For instance, protecting only home and about page would be implemented as follows:

```ts
export { default } from 'next-auth/middleware'

export const config = { matcher: ['/', '/about'] }
```

Now, when you visit both pages on your localhost, they will present an authentication prompt inviting you to "Sign in with Google," instead of displaying the regular content:

![13](https://www.freecodecamp.org/news/content/images/2023/11/13.png)

## Conclusion

In this tutorial, we've covered the essential steps to implement authentication and protected routes in your `Next.js` application using the `next-auth.js` library with the Google Provider. 

By following these steps, you've laid a solid foundation for integrating authentication into your Next.js application, bolstering its security and enhancing the user experience. 

With the knowledge gained here, you can now confidently develop applications that offer secure access control and personalized content based on user authentication.

It's also worth noting that `next-auth.js` provides multiple providers you can employ to implement authentication, not just Google Provider. 



