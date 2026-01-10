---
title: 'Clerk vs Kinde vs Better Auth: How to Choose the Right Next.js Authentication
  Library'
subtitle: ''
author: Andrew Baisden
co_authors: []
series: null
date: '2025-09-23T02:34:54.472Z'
originalURL: https://freecodecamp.org/news/how-to-choose-the-right-nextjs-authentication-library
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758594098828/8b2e3142-9067-4a02-b1e5-63319dde45de.png
tags:
- name: Next.js
  slug: nextjs
- name: authentication
  slug: authentication
seo_title: null
seo_desc: Authentication is an important aspect when building applications, especially
  if they hold financial information or require users to sign into accounts. Building
  an auth library can be a lot of work, and there is no need to reinvent the wheel
  when so ...
---

Authentication is an important aspect when building applications, especially if they hold financial information or require users to sign into accounts. Building an auth library can be a lot of work, and there is no need to reinvent the wheel when so many efficient libraries already exist.

In this article, we’ll compare some libraries that you can use for authentication in your Next app. They include: [Clerk](https://clerk.com/), [Kinde](https://kinde.com/) and [Better Auth](https://www.better-auth.com/). You’ll learn how to set up these tools in a Next.js application, with the goal of creating at least one authenticated, protected page route.

The aim here is simply to see how each tool works when it comes to speed of setup and ease of use.

## Table of Contents

* [What are Clerk, Kinde and Better Auth?](#heading-what-are-clerk-kinde-and-better-auth)
    
* [Prerequisites](#heading-prerequisites)
    
* [How to Set Up Authentication Using Clerk](#heading-how-to-set-up-authentication-using-clerk)
    
* [How to Set Up Authentication Using Kinde](#heading-how-to-set-up-authentication-using-kinde)
    
* [How to Set Up Authentication Using Better Auth](#heading-how-to-set-up-authentication-using-better-auth)
    
* [When To Use Each Library](#heading-when-to-use-each-library)
    
* [Conclusion](#heading-conclusion)
    

## What are Clerk, Kinde and Better Auth?

Clerk, Kinde and Better Auth are basically modern authentication providers, much like [Auth.js](https://authjs.dev/), which have been built with developers in mind. Although they share similarities, they have certain aspects that differentiate them from each other.

To begin with, Clerk is more full-featured. It's more of a hosted solution that offers components which are ready-made, as well as user management and other integrations, which allow you to get up and running pretty quickly.

Kinde, on the other hand, is more of a developer platform, which has authentication, feature flags and team management all in one place.

Better Auth is more of an open-source and code-first place that gives developers the building blocks to create authentication without having to be locked into an ecosystem.

## Prerequisites

The prerequisites for this tutorial are minimal, and the databases and Prisma ORM are only required for Better Auth. Alternatively, you can use any of the databases inside a Docker container instead of installing them locally, but that is outside of the scope of this tutorial.

You’ll need these to follow along:

* Node and npm installed
    
* [Prisma ORM](https://www.prisma.io/)
    
* SQLite, PostgreSQL, or MySQL database set up locally
    
* Code editor/IDE
    

Let's see how to set up authentication with all three auth platforms in a Next.js application. We’ll use separate Next.js applications to set up each library so that the codebase will remain clean, and you can experience what it's like to set them up from scratch.

First, decide on a location for your project, like on the desktop and then use the command `npx create-next-app@latest` to set up a Next.js project. You can just use the default configuration. These are the settings I used:

✔ What is your project named? … my-app  
✔ Would you like to use TypeScript? … No / **Yes**  
✔ Which linter would you like to use? › ESLint  
✔ Would you like to use Tailwind CSS? … No / **Yes**  
✔ Would you like your code inside a `src/` directory? … No / **Yes**  
✔ Would you like to use App Router? (recommended) … No / **Yes**  
✔ Would you like to use Turbopack? (recommended) … No / **Yes**  
✔ Would you like to customize the import alias (`@/*` by default)? … **No** / Yes

We are creating three apps, so it's up to you if you want to duplicate the codebases now and give them different names like `my-app`, `my-app2` and `my-app3` or do them later when we reach each section.

## How to Set Up Authentication Using Clerk

With your Next.js project set up, `cd` into the `my-app` folder or whatever name you gave the project and run the following command to install the Next.js SDK for Clerk:

```shell
npm install @clerk/nextjs
```

Now we need to create a middleware file that will grant us access to user authentication throughout our entire app.

Create a `middleware.ts` file with this code inside the `/src` folder:

```typescript
import { clerkMiddleware } from '@clerk/nextjs/server'

export default clerkMiddleware()

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```

With this file, authentication is set up for different page routes.

All that's left is to add the `<ClerkProvider>` component to your app's `layout.tsx` file so that authentication is available throughout your entire app.

Just replace all of the code inside of `src/app/layout.tsx` with this code here:

```typescript
import type { Metadata } from 'next';
import { Geist, Geist_Mono } from 'next/font/google';
import './globals.css';
import {
  ClerkProvider,
  SignInButton,
  SignUpButton,
  SignedIn,
  SignedOut,
  UserButton,
} from '@clerk/nextjs';

const geistSans = Geist({
  variable: '--font-geist-sans',
  subsets: ['latin'],
});

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body
          className={`${geistSans.variable} ${geistMono.variable} antialiased`}
        >
          <header className="flex justify-end items-center p-4 gap-4 h-16">
            <SignedOut>
              <SignInButton />
              <SignUpButton>
                <button className="bg-[#6c47ff] text-white rounded-full font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 cursor-pointer">
                  Sign Up
                </button>
              </SignUpButton>
            </SignedOut>
            <SignedIn>
              <UserButton />
            </SignedIn>
          </header>
          {children}
        </body>
      </html>
    </ClerkProvider>
  );
}
```

What we did was to import the `ClerkProvider`, as well as the buttons for signing in and out using Clerk authentication. These additions have been added to the `layout.tsx` file which means that they are available throughout our entire application. So every page should display the sign in flow at the top of the page.

The `ClerkProvider` component is needed for integrating Clerk inside of our application, so now we can use session and user context with Clerks hooks and components.

Now you can run your Next.js app with `npm run dev`, and you should see the homepage, as well as a sign-in and sign-up button at the top of the page, as shown here:

![Next.js homepage with Clerk authentication setup](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428533274/31f43e8f-7826-4d4c-bf10-99b5ea7d8a76.png align="center")

Clicking the signup button will take you to a sign-up form where you can use an email address or sign in with Google, which is pretty easy.

![Clerk Sign up form](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428605871/94e754e7-897f-42f2-84df-361d97226617.png align="center")

When you have signed in, you should see your profile picture and account information in the top right-hand corner of the screen. That's the hard part done - all that's left is to create a page and then make the route protected so that only a signed-in user can access it.

To begin with, lets update our `middleware.ts` file with some code which lets us protect a route:

```typescript
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isProtectedRoute = createRouteMatcher(['/dashboard(.*)'])

export default clerkMiddleware(async (auth, req) => {
  if (isProtectedRoute(req)) await auth.protect()
})

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```

We added some new imports for `createRouteMatcher`, which is a Clerk helper function that gives us the power to protect multiple routes. In this case, the dashboard page route in our application requires a user to be signed in to access the route. Now we need create a dashboard page. Create this folder and file inside the `app` folder: `dashboard/page.tsx`. Then complete the page by giving it some code like below:

```typescript
export default function Dashboard() {
  return (
    <>
      <h1>Dashboard Page</h1>
    </>
  );
}
```

We created a simple page which has a heading that says Dashboard Page.

Congratulations, you have successfully added authentication to your Next app and protected a page route, and it only took a few steps! When you navigate to [http://localhost:3000/dashboard](http://localhost:3000/dashboard) as a non-signed-in user, you should be redirected to a sign-in form as shown below:

![Clerk sign in form page](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428660606/5ac6984d-7f8c-46e2-bd0b-732920d5743e.png align="center")

If you are already signed in, then you should see the Dashboard page. You can learn more using the [Clerk official documentation](https://clerk.com/docs).

## How to Set Up Authentication Using Kinde

Create another Next.js application for this project if you have not done so already. Kinde will require you to create an account on their platform before using their authentication library. Let's go through the sign-up process.

Firstly, go to the [Kinde](https://kinde.com/) website, and you should see a button that says "Start for free" or similar.

![Kinde website homepage](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428704023/dd6bf59e-2858-4f0a-8aa4-90645641ebe8.png align="center")

Clicking that button should take you to a page where you can create an account:

![Kinde create your account](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428737190/0cd172f6-ed9a-4a54-b599-182a8becfcfa.png align="center")

An email code verification may be required:

![Kinde email code verification](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428803166/8a883160-6e95-4611-91d3-efbabd74653c.png align="center")

On the next screen, you should be able to enter your business details, which can be anything you want. Every time you set up authentication for an app, you will have to create an application for it on your account. Give it any name you want, like `app-clerk-test3272346214`. The same name will be used for the business and the domain.

![Kinde form business and domain](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428845977/7d365554-9c15-41e0-b317-a12d58f3e7a6.png align="center")

On the next screen, we’ll choose to use an existing codebase because we have a local project:

![Kinde existing codebase select](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428896749/cd468f14-1b36-4025-8459-b51509519fa0.png align="center")

The codebase is in Next.js, so select it from the list:

![Kinde select tech stack](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428936691/cf13041f-bc74-4432-a7ba-4234daf7c2a3.png align="center")

The next important step is choosing how users are going to sign in. I chose email and Google. You can select whichever options you desire:

![Kinde user sign in form](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428976433/2885ed25-d4d0-496e-ac46-2f8b96c35a20.png align="center")

Now, on the last screen, choose to explore at your own pace.

![Kinde explore at own pace screen](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429011937/23a9d95f-2935-4a9c-947f-91d7adaf452e.png align="center")

And finally, we’ve reach the dashboard screen.

![Kinde dashboard screen](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429051925/2250e252-e84d-4ae9-bff8-a9e687692f70.png align="center")

Viewing details lets you see your app keys and environment variables, among other useful information.

That's the long part out of the way, let's get to some code. Navigate to your project folder and then install the package for Kinde:

```shell
npm i @kinde-oss/kinde-auth-nextjs
```

Now, create a `.env.local` file and put it in the root folder of your project with your environment variables. You can find your environment variables in the Quick Start page of your application.

Here's an example:

```shell
KINDE_CLIENT_ID=<your_kinde_client_id>
KINDE_CLIENT_SECRET=<your_kinde_client_secret>
KINDE_ISSUER_URL=https://<your_kinde_subdomain>.kinde.com
KINDE_SITE_URL=http://localhost:3000
KINDE_POST_LOGOUT_REDIRECT_URL=http://localhost:3000
KINDE_POST_LOGIN_REDIRECT_URL=http://localhost:3000/dashboard
```

Next, you need to create the following API endpoint and folder structure and files as shown here `src/app/api/auth/[kindeAuth]/route.ts`.

This is the code needed for the `route.ts` file:

```shell
import {handleAuth} from "@kinde-oss/kinde-auth-nextjs/server";

export const GET = handleAuth();
```

With this code, Kinde can now handle auth endpoints inside our application.

Once again, you’ll need a `middleware.ts` file so that authentication can be set up properly in your app. The file should be in the root directory and needs this code added to it:

```typescript
import { withAuth } from "@kinde-oss/kinde-auth-nextjs/middleware";

export default function middleware(req) {
  return withAuth(req);
}

export const config = {
  matcher: [
    // Run on everything but Next internals and static files
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
  ]
};
```

Like before, we can now protect page routes with this file. Your app has to be wrapped in a Kinde Auth Provider so that you can access the data throughout your app.

Create an `AuthProvider.tsx` file inside the `app` directory with this code:

```typescript
"use client";
import {KindeProvider} from "@kinde-oss/kinde-auth-nextjs";

export const AuthProvider = ({children}) => {
  return <KindeProvider>{children}</KindeProvider>;
};
```

Kinde uses a React Context Provider to maintain its internal state throughout our application by using the `KindeProvider` component.

Next, replace and update the `layout.tsx` file, so it is wrapped in the Auth Provider:

```typescript
import type { Metadata } from 'next';
import { Geist, Geist_Mono } from 'next/font/google';
import './globals.css';
import { AuthProvider } from './AuthProvider';
import {
  RegisterLink,
  LoginLink,
  LogoutLink,
} from '@kinde-oss/kinde-auth-nextjs/components';

const geistSans = Geist({
  variable: '--font-geist-sans',
  subsets: ['latin'],
});

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <AuthProvider>
      <div className="grid grid-flow-col gap2">
        <LoginLink>Sign in</LoginLink>
        <RegisterLink>Sign up</RegisterLink>
        <LogoutLink>Log out</LogoutLink>
      </div>
      <html lang="en">
        <body
          className={`${geistSans.variable} ${geistMono.variable} antialiased`}
        >
          {children}
        </body>
      </html>
    </AuthProvider>
  );
}
```

In this file, we also added buttons for signing up, signing in, and logging out which will be displayed at the top of every page as this is the main `layout.tsx` file. Our `AuthProvider` component is wrapped around our application which means we can now use Kinde throughout it.

The basic setup is now complete! Run the usual command to start the Next.js app, and you should see the sign-in flow buttons at the top of the screen.

You should be able to sign up and create an account. Doing so will redirect you to the dashboard screen, which shows a 404 error page. This is because we have not created a dashboard page yet.

This is what the Kinde register form looks like:

![Kinde Register form](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429157871/c7344f32-cf4e-48d3-b43e-225f81912988.png align="center")

And this is what the Kinde sign-in form looks like:

![Kinde sign in form](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429447577/3d30476a-9269-49a9-811c-dff0c16225d9.png align="center")

Only one step remains now: creating a protected route for your authentication.

Create the following file structure and file for your dashboard page: `src/app/dashboard/page.tsx`.

Then add this code to the file:

```typescript
'use client';

import { useKindeBrowserClient } from '@kinde-oss/kinde-auth-nextjs';
import { LoginLink } from '@kinde-oss/kinde-auth-nextjs/components';

export default function Dashboard() {
  const { isAuthenticated, isLoading } = useKindeBrowserClient();

  if (isLoading) return <div>Loading...</div>;

  return isAuthenticated ? (
    <div>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ut
        ante enim. Maecenas ut eros nec diam vulputate sollicitudin. Cras ut
        quam leo. Pellentesque semper, lacus sodales gravida suscipit, metus
        quam congue eros, nec sagittis est dolor eu turpis. Nulla congue
        tristique venenatis. Donec ac venenatis mauris. Donec commodo cursus
        magna, vitae tincidunt magna vestibulum eget.
      </p>
    </div>
  ) : (
    <div>
      You have to <LoginLink>Login</LoginLink> to see this page
    </div>
  );
}
```

This page file checks to see if the user is authenticated and signed in. If they are signed in, they see the Lorem ipsum text, and if they are not signed in, they will see a message telling them that they have to log in to see the page.

All you have to do is go to the [dashboard route](http://localhost:3000/dashboard) as a signed-in or signed-out user to see it for yourself. And that's pretty much the basics of authentication using the Kinde platform. See the [online documentation](https://docs.kinde.com/) to learn everything there is to know about it.

## How to Set Up Authentication Using Better Auth

And lastly, let's create a project that uses Better Auth. Better Auth requires a database to store user data, so the setup will require a few more steps. You can find the installation guide [here](https://www.better-auth.com/docs/installation), but, we’ll also go through it here.

Ok, just like before, create a Next.js project if you have not done so yet and then install the `better-auth` package with this command:

```shell
npm install better-auth
```

Next, you have to set up your environment variables, so create a `.env` file with these values:

```shell
BETTER_AUTH_SECRET= #Create your own secret key!
BETTER_AUTH_URL=http://localhost:3000 # Base URL of your app
```

Make sure that you create a secret key, as if you were generating a secure password with uppercase and lowercase letters and numbers.

Let's get our Prisma package and PostgreSQL database set up, so run these scripts to initialise them:

```shell
npm install prisma --save-dev
npx prisma init
npm install @prisma/client
```

In the next step, we have to create a better auth instance. In this case, we will put the file in the `src/lib/auth.ts`.

So create an `auth.ts` file with this code:

```typescript
import { betterAuth } from 'better-auth';
import { anonymous } from 'better-auth/plugins';
import { prismaAdapter } from 'better-auth/adapters/prisma';
// If your Prisma file is located elsewhere, you can change the path
import { PrismaClient } from '@/generated/prisma';

const prisma = new PrismaClient();
export const auth = betterAuth({
  database: prismaAdapter(prisma, {
    provider: 'postgresql', // or "mysql", "postgresql", ...etc
  }),
  plugins: [anonymous()],
});
```

In this file, we have configured Better Auth to use Prisma ORM for our database connection, and we will be connecting to a PostgreSQL database. If you want, you can change it to a different database, but the setup might be different, so bear that in mind. You could also use Docker if you know how to set it up. Anonymous sign-in is the default for users.

Now we need to create our database tables for saving user information, so use this command in the terminal to do that:

```shell
npx @better-auth/cli generate
```

You might see this warning, just select yes with "y":

```shell
prisma:warn In production, we recommend using `prisma generate --no-engine` (See: `prisma generate --help`)
✔ The file ./prisma/schema.prisma already exists. Do you want to overwrite the schema to the file? … yes
```

For handling API requests, we must have a route handler set up on our server. Create a folder structure and file for the `route.ts` file, like shown here `/app/api/auth/[...all]/route.ts`.

Add this code to the file:

```typescript
import { auth } from '@/lib/auth'; // path to your auth file
import { toNextJsHandler } from 'better-auth/next-js';

export const { POST, GET } = toNextJsHandler(auth);
```

This file lets you handle POST and GET requests for your auth file.

Lastly, we have to create a `lib/auth-client.ts` file. This file allows you to interact with the auth server, and it has a plugin so users can sign in anonymously.

And here is the code to put inside this file:

```typescript
import { createAuthClient } from 'better-auth/react';
import { anonymousClient } from 'better-auth/client/plugins';
export const authClient = createAuthClient({
  /** The base URL of the server (optional if you're using the same domain) */
  baseURL: 'http://localhost:3000',
  plugins: [anonymousClient()],
});
```

With this file, it's possible for users to sign in anonymously without having to even create an account or use social sign-in, thanks to the plugin.

All that remains is to create another dashboard page, which has authentication like before. Create another dashboard page with this structure: `app/dashboard/page.tsx`, and then add this code to the file:

```typescript
'use client';

import { useState, useEffect } from 'react';
import { authClient } from '@/lib/auth-client';

type User = {
  id: string;
  email: string;
  emailVerified: boolean;
  name: string;
  createdAt: Date;
  updatedAt: Date;
  image?: string | null;
  isAnonymous?: boolean | null;
};

export default function Dashboard() {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isSigningIn, setIsSigningIn] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const session = await authClient.getSession();
        if (session.data?.user) {
          setUser(session.data.user);
        }
      } catch (err) {
        console.error('Auth check error:', err);
      } finally {
        setIsLoading(false);
      }
    };

    checkAuth();
  }, []);

  const handleAnonymousSignIn = async () => {
    try {
      setIsSigningIn(true);
      setError(null);

      const result = await authClient.signIn.anonymous();

      if (result.data) {
        setUser(result.data.user);
        console.log('Anonymous user signed in:', result.data.user);
      } else if (result.error) {
        setError(result.error.message || 'Failed to sign in anonymously');
      }
    } catch (err) {
      setError('An unexpected error occurred');
      console.error('Anonymous sign-in error:', err);
    } finally {
      setIsSigningIn(false);
    }
  };

  const handleSignOut = async () => {
    try {
      await authClient.signOut();
      setUser(null);
    } catch (err) {
      console.error('Sign out error:', err);
    }
  };

  if (isLoading) {
    return (
      <div className="max-w-4xl mx-auto p-6">
        <div className="flex items-center justify-center min-h-[400px]">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
            <p className="text-gray-600">Checking authentication...</p>
          </div>
        </div>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="max-w-4xl mx-auto p-6">
        <div className="text-center">
          <h1 className="text-3xl font-bold mb-6">Access Required</h1>
          <p className="text-gray-600 mb-8">
            You need to be signed in to access our dashboard. Choose an option
            below to continue.
          </p>

          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6 max-w-md mx-auto">
              {error}
            </div>
          )}

          <div className="bg-gray-50 p-8 rounded-lg border max-w-md mx-auto">
            <h2 className="text-xl font-semibold mb-4 text-black">
              Sign In Options
            </h2>

            <button
              onClick={handleAnonymousSignIn}
              disabled={isSigningIn}
              className="w-full bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300 text-white px-6 py-3 rounded font-medium mb-4"
            >
              {isSigningIn ? 'Signing in...' : 'Sign In Anonymously'}
            </button>

            <p className="text-sm text-gray-500 mb-4">
              Anonymous access allows you to use our dashboard without creating
              an account. You can always link your account later.
            </p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg font-semibold text-green-800">
              Welcome, {user.isAnonymous ? 'Anonymous User' : user.name}!
            </h2>
            <p className="text-sm text-green-600">
              {user.isAnonymous
                ? 'You are signed in anonymously'
                : `Signed in as ${user.email}`}
            </p>
          </div>
          <button
            onClick={handleSignOut}
            className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded text-sm"
          >
            Sign Out
          </button>
        </div>
      </div>

      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

      {process.env.NODE_ENV === 'development' && (
        <div className="mt-8 bg-gray-100 p-4 rounded-lg">
          <h3 className="font-semibold mb-2 text-black">Debug Info:</h3>
          <pre className="text-xs text-gray-600 overflow-auto">
            {JSON.stringify(user, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
```

This code creates a dashboard page which requires a user to be authenticated and signed in to use it. After a user signs in anonymously, they can view some debug info about their profile. So basically, this page is an authentication flow for our dashboard view which integrates with our custom `authClient`. This page also handles loading error state and sign out for anonymous users.

Ok, now we probably need to reset our Prisma database again, or we could get schema and table errors.

First, make sure that your Prisma development database is running with this command:

```shell
npx prisma dev
```

And then run these commands to reset the database and apply the new migrations for the schema:

```shell
npx prisma migrate reset
npx prisma migrate dev
```

You might need to restart the Prisma development server and then run it with the command `npx prisma dev`.

Our Better Auth app needs two servers to be running.

1. The Prisma development server
    
2. The Next.js application
    

With the Prisma development server running, you can now start the Next.js app with the usual command `npm run dev`.

If you encounter any problems with the Prisma ORM or database, like tables missing or schema mismatches, then here are some useful commands which could hopefully resolve them.

```shell
# ⚠️ WARNING: This will drop the database, recreate it, and apply all migrations from scratch.
npx prisma migrate reset

# Applies any new migrations that haven’t been run yet (or creates a new one if your schema changed).
npx prisma migrate dev

# Starts Prisma Studio (a GUI for exploring and editing your database).
npx prisma dev

# Runs Better Auth CLI migrations (sets up any database tables/changes required for authentication).
npx @better-auth/cli migrate
```

These commands are self-explanatory and let us run migrations on our database when there are changes, and we can see our database inside of Prisma Studio.

This is what the dashboard page looks like when a user is not signed in:

![Better Auth app Dashboard page](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429500439/9c0846fc-cfc5-4232-9a02-4e313c2c4698.png align="center")

Signing in will show the dashboard screen. To learn more about Better Auth, you can read their [official documentation](https://www.better-auth.com/).

## When To Use Each Library

Each of these authentication libraries have their pros and cons, and can suit various needs depending on your project. Knowing when to use each one can better prepare you for real-world conditions and when building for production, so let's go through them and see how they compare.

### When to Use Clerk

Clerk excels when you need to use auth quickly without worrying about managing multiple servers, and when you need to have pre-made interfaces and management systems. It's great for startups and teams that want to prioritize developer experience and fast implementation.

It has a streamlined and user-friendly setup, which is still able to support the bare minimum essentials, so it's a really good option for small teams and projects that must have an easy implementation. If you are building a SaaS that needs a good interface and components from the start, or if you require social logins without a ton of code, then it's a very good solution, especially if you want speed and cost effectiveness in a smaller project.

### When to Use Kinde

Kinde is a fantastic choice when you are keen on having transparent pricing and quick auth integration in more frameworks. Kinde has been designed to be a cost-effective alternative to Clerk and offers more transparent pricing and a more generous, free tier.

It's great for teams that need to have a reliable authentication option but want lower costs and better framework support. Kinde is effective when used in medium-sized projects that need more than a basic authentication system, but also don't have the need to have enterprise-grade tooling.

### When to Use Better Auth

Better Auth is a great solution when you have a need for an expansive set of features out of the box. It is also worth noting that Better Auth has a plugin ecosystem that can simplify adding more advanced functionalities with only a few lines of code. Of all the options discussed in this article, Better Auth is by far the cleanest; however, it requires more coding knowledge and skills.

It's a good option if you are building a TypeScript application and want to have full control over the customization and auth data flows. The framework is agnostic and has features such as 2FA, multi-tenant support and other complex features so developers can get the best out of the tool, as there is no vendor lock-in. Functionality can easily be expanded with the plugin ecosystem, so developers can tailor it to their needs.

## Conclusion

All three platforms are fairly good at their job, and I do not doubt that they are going to remain popular options for adding authentication to our applications. Auth.js is one of the most well-known out there; however, Clerk, Kinde and Better Auth also appear to have growing followings, and judging by conversations on socials, they appear to be the first choice for many developers at the moment.

After experiencing what it's like to set them up for the first time, I would have to say that Clerk is the easiest to set up because you don't have to create an account, and you can get the authentication working fairly quickly with little troubleshooting. Kinde would be the second easiest to set up, in my opinion. You do have to register for an account to use the platform; however, the setup was also pretty easy and did not need any troubleshooting.

Better Auth is a great platform, but the setup requires a bit more work because a database is required for storing users' information, which makes the process slightly more difficult. I also found it easier to create authenticated routes with the other two auth options. However, the fact that the platform is open-source with no vendor lock-in works in its favour because developers can self-host and it's completely free, which means no paid plans.
