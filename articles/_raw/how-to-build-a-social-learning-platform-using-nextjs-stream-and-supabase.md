---
title: How to Build a Social Learning Platform using Next.js, Stream, and Supabase
subtitle: Learn how to build a social learning platform that connects students with
  professionals across various fields.
author: David Asaolu
co_authors: []
series: null
date: '2025-03-03T15:10:15.095Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-social-learning-platform-using-nextjs-stream-and-supabase
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741009946459/dba65929-1b65-4278-9601-4d047042753a.png
tags:
- name: React
  slug: reactjs
- name: Next.js
  slug: nextjs
- name: Web Development
  slug: web-development
- name: Tutorial
  slug: tutorial
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: Social media and real-time communication have transformed how people interact,
  making it easier to share ideas, collaborate, and learn from others, regardless
  of location. From professional networks to online study groups, these platforms
  allow vario...
---

Social media and real-time communication have transformed how people interact, making it easier to share ideas, collaborate, and learn from others, regardless of location. From professional networks to online study groups, these platforms allow various forms of communication such as instant messaging, video calls, and content sharing.

In this tutorial, you'll learn how to build a social learning platform that connects students with professionals across various fields. The platform enables users to:

* Schedule video conferencing sessions that students can join,
    
* Share posts or announcements about trending tools and upcoming sessions, and
    
* Create community channels where students can engage with one another.
    

The [Stream Video & Audio SDK](https://getstream.io/video/sdk/) and [Stream Chat SDK](https://getstream.io/chat/sdk/) will enable us to integrate video calls and community channels easily into the application.

![Cartoon person with pink hair and green glasses holding a smartphone, which displays heart, poop, and smiley face emojis on the screen.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740662075821/1a004f19-4889-4b57-921b-062cf1927261.gif align="center")

## Table of Contents

* [App Overview](#heading-app-overview)
    
* [Prerequisites](#heading-prerequisites)
    
* [How to Set up Server-Side Authentication with Supabase](#heading-how-to-set-up-server-side-authentication-with-supabase)
    
    * [How to Configure Supabase Authentication in a Next.js application](#heading-how-to-configure-supabase-authentication-in-a-nextjs-application)
        
    * [Student Authentication with Supabase](#heading-student-authentication-with-supabase)
        
    * [Instructor Authentication with Supabase](#heading-instructor-authentication-with-supabase)
        
* [The Application Database Design](#heading-the-application-database-design)
    
    * [Access Policy for the Announcements Table](#heading-access-policy-for-the-announcements-table)
        
    * [Access Policy for the Instructors Table](#heading-access-policy-for-the-instructors-table)
        
    * [Access Policy for the Students Table](#heading-access-policy-for-the-students-table)
        
* [How to Add a Video Conferencing Feature with Stream](#heading-how-to-add-a-video-conferencing-feature-with-stream)
    
    * [Setting Up Stream Video & Audio SDK in Next.js](#heading-setting-up-stream-video-amp-audio-sdk-in-nextjs)
        
    * [Creating and Scheduling Calls with Stream](#heading-creating-and-scheduling-calls-with-stream)
        
    * [Joining Stream Video Calls](#heading-joining-stream-video-calls)
        
    * [Stream Call UI Components](#heading-stream-call-ui-components)
        
* [How to Integrate a Group Chat Feature Using Stream Chat Messaging](#heading-how-to-integrate-a-group-chat-feature-using-stream-chat-messaging)
    
    * [Setting Up the Stream Chat SDK in Next.js](#heading-setting-up-the-stream-chat-sdk-in-nextjs)
        
    * [Stream Chat UI Components](#heading-stream-chat-ui-components)
        
* [Next Steps](#heading-next-steps)
    

## App Overview

The application consists of two types of users (students and instructors), each with access to specific features:

Students can do the following:

* View an activity feed with posts from instructors and react to them.
    
* Follow instructors in their field of interest.
    
* Join upcoming video sessions and community channels.
    
* Each student has an interest attribute that helps match them with relevant instructors.
    

Instructors can also:

* Access a dashboard showing their follower count and post activity.
    
* Schedule video conferences for students to join.
    
* Make announcements or share posts.
    
* Create community channels (if they haven't already).
    
* The platform suggests instructors to students based on shared career interests.
    

Here is an image showing the various functions that the users can perform:

![Flowchart titled "User Functions" showing a hierarchy. "Users" split into "Students" and "Instructors". Students can "Follow Instructors", "Join Video Sessions", "Join Community Channels", and "Read and React to Posts". Instructors can "View Dashboard", "Create Posts", "Schedule Video Sessions", and "Create Community Channels".](https://cdn.hashnode.com/res/hashnode/image/upload/v1740723106527/fd8af07a-1919-42f0-9e9a-ed380a0b77cc.png align="center")

## Prerequisites

To fully understand this tutorial, you need to have a basic understanding of React or Next.js.

We will use the following tools:

* [Supabase](https://supabase.com/docs): a Backend-as-a-service platform that makes it easy to integrate authentication, database, real-time communication, file storage, and edge functions within your software applications. It also supports multiple programming languages.
    
* [Stream Chat](https://getstream.io/chat/docs/sdk/react/) and [Audio & Video SDK](https://getstream.io/video/docs/react/): a real-time communication platform that enables you to add video, chat, and various types of communication to your application.
    
* [Shadcn UI](https://ui.shadcn.com/docs/installation/next): a UI component library that provides customizable, beautifully designed, and accessible UI components for your applications.
    

Create a Next.js project by running the following code snippet:

```bash
npx create-next-app stream-lms
```

Install the package dependencies for the project:

```bash
npm install @supabase/supabase-js @supabase/ssr @stream-io/node-sdk @stream-io/video-react-sdk stream-chat stream-chat-react @emoji-mart/data @emoji-mart/react
```

To install the Shadcn UI library, follow [the installation guide.](https://ui.shadcn.com/docs/installation/next)

Once everything is set up, your Next.js project is ready. Now, let's start building! 🚀

## How to Set up Server-Side Authentication with Supabase

Here, you'll learn how to configure Supabase, add server-side authentication, and protect pages from unauthorized users in a Next.js application. You'll also learn how to handle the authentication logic efficiently using [Next.js server actions](https://nextjs.org/docs/13/app/api-reference/functions/server-actions#with-client-components).

### How to Configure Supabase Authentication in a Next.js application

First, create a [Supabase account](https://supabase.com/) and an organization that will contain your various Supabase projects.

![Screenshot of a form on the Supabase website to create a new organization. It includes fields for organization name, type, and plan, with options such as "Personal" and "Free - $0/month." There are buttons for "Cancel" and "Create organization."](https://cdn.hashnode.com/res/hashnode/image/upload/v1740653729412/35339612-4688-489e-b9d2-2cc825962519.png align="center")

Add a new Supabase project to the organisation and copy the following credentials on your dashboard into a `.env.local` file at the root of your project:

```bash
NEXT_PUBLIC_SUPABASE_ANON_KEY=<anon_key_from_Supabase_dashboard>
NEXT_PUBLIC_SUPABASE_URL=<supabase_project_url>
```

Create a `utils/supabase` folder at the root of the Next.js project and add the following files to the folder: `client.ts`, `middleware.ts`, and `server.ts`.

```bash
mkdir utils && cd utils
mkdir supabase && cd supabase
touch client.ts middleware.ts server.ts
```

Copy the following code into `utils/supabase/client.ts`. This initializes a Supabase browser client to interact with Supabase on client-side routes:

```typescript
import { createBrowserClient } from "@supabase/ssr";

export function createClient() {
	return createBrowserClient(
		process.env.NEXT_PUBLIC_SUPABASE_URL!,
		process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
	);
}
```

Next, copy the following code into `utils/supabase/server.ts`. This creates a Supabase server client for handling authentication and interacting with Supabase in server-side requests:

```typescript
import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";

export async function createClient() {
	const cookieStore = await cookies();

	return createServerClient(
		process.env.NEXT_PUBLIC_SUPABASE_URL!,
		process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
		{
			cookies: {
				getAll() {
					return cookieStore.getAll();
				},
				setAll(cookiesToSet) {
					try {
						cookiesToSet.forEach(({ name, value, options }) =>
							cookieStore.set(name, value, options)
						);
					} catch {
						// The `setAll` method was called from a Server Component.
						// This can be ignored if you have middleware refreshing
						// user sessions.
					}
				},
			},
		}
	);
}
```

Now, copy the following code into `utils/supabase/middleware.ts`. This middleware creates authentication cookies and protects pages from unauthorized access:

```typescript
import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

export async function updateSession(request: NextRequest) {
	let supabaseResponse = NextResponse.next({
		request,
	});
	//👇🏻 creates the Supabase cookie functions
	const supabase = createServerClient(
		process.env.NEXT_PUBLIC_SUPABASE_URL!,
		process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
		{
			cookies: {
				getAll() {
					return request.cookies.getAll();
				},
				setAll(cookiesToSet) {
					cookiesToSet.forEach(({ name, value }) =>
						request.cookies.set(name, value)
					);
					supabaseResponse = NextResponse.next({
						request,
					});
					cookiesToSet.forEach(({ name, value, options }) =>
						supabaseResponse.cookies.set(name, value, options)
					);
				},
			},
		}
	);

	// 👉🏻 placeholder for protected route controller
}
```

To enforce authentication, add the following code inside the placeholder in `middleware.ts`**.** This checks if a user is signed in and redirects unauthenticated users to the login page:

```typescript
//👇🏻 gets current user
const {
	data: { user },
} = await supabase.auth.getUser();

//👇🏻 declares protected routes
if (
	!user &&
	request.nextUrl.pathname !== "/" &&
	!request.nextUrl.pathname.startsWith("/instructor/auth") &&
	!request.nextUrl.pathname.startsWith("/student/auth")
) {
	//👇🏻 Redirect unauthenticated users to the login page
	const url = request.nextUrl.clone();
	url.pathname = "/student/auth/login"; // 👈🏼 redirect page
	return NextResponse.redirect(url);
}
//👇🏻 returns Supabase response
return supabaseResponse;
```

Add another `middleware.ts` file to the root of the Next.js project and copy the following code into the file:

```typescript
import { type NextRequest } from "next/server";
import { updateSession } from "./utils/supabase/middleware";

export async function middleware(request: NextRequest) {
	return await updateSession(request);
}

export const config = {
	matcher: [
		/*
		 * Match all request paths except for the ones starting with:
		 * - _next/static (static files)
		 * - _next/image (image optimization files)
		 * - favicon.ico (favicon file)
		 * Feel free to modify this pattern to include more paths.
		 */
		"/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
	],
};
```

Finally, create an [**auth/confirm**](https://github.com/dha-stix/stream-lms/blob/main/src/app/auth/confirm/route.ts) route and [**error**](https://github.com/dha-stix/stream-lms/blob/main/src/app/error/page.tsx) page within the Next.js app folder.

You've successfully [configured authentication in your Next.js project](https://supabase.com/docs/guides/auth/server-side/nextjs) using Supabase.

### Student Authentication with Supabase

In this section, you will learn how to create the signup and login functions for the students within the application.

First, create an **actions** folder in the root of your Next.js project and add an `auth.ts` file inside it. This file will contain all Supabase authentication functions.

Add the following imports to the top of the `auth.ts` file:

```typescript
"use server";
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { createClient } from "../utils/supabase/server";
```

Next, you need to create the server functions that accept form data from the client and sign users up or log them in as students.

Copy the following code snippet into the `actions/auth.ts` file to create the user sign-up function:

```typescript
export async function studentSignUp(formData: FormData) {
	const supabase = await createClient();

	//👇🏻 Extract form data
	const credentials = {
		email: formData.get("email") as string,
		password: formData.get("password") as string,
		interest: formData.get("interest") as string,
		name: formData.get("name") as string,
	};

	//👇🏻 Supabase sign up function (options attribute :- for user metadata)
	const { data, error } = await supabase.auth.signUp({
		email: credentials.email,
		password: credentials.password,
		options: {
			data: {
				interest: credentials.interest,
				name: credentials.name,
			},
		},
	});

	//👉🏻 return user or error object
}
```

The code snippet above accepts the form credentials such as email, password, interest, and name, and signs the user up as a Supabase user.

Modify the function to return the user or error object.

```typescript
export async function studentSignUp(formData: FormData) {
	//...form inputs and supabase functions

	if (error) {
		return { error: error.message, status: error.status, user: null };
	} else if (data.user?.identities?.length === 0) {
		return { error: "User already exists", status: 409, user: null };
	}

	revalidatePath("/", "layout");
	return { error: null, status: 200, user: data.user };
}
```

Create the student login function as shown below:

```typescript
export async function studentLogIn(formData: FormData) {
	const supabase = await createClient();

	const credentials = {
		email: formData.get("email") as string,
		password: formData.get("password") as string,
	};
	const { data, error } = await supabase.auth.signInWithPassword(credentials);

	if (error) {
		return { error: error.message, status: error.status, user: null };
	}
	//👇🏻 only instructors have an image attribute
	if (data && data.user.user_metadata.image) {
		return { error: "You are not a student", status: 400, user: null };
	}

	//👉🏻 create a student row and add to the database

	revalidatePath("/", "layout");
	return { error: null, status: 200, user: data.user };
}
```

The code above takes the student's email and password to log them into the application.

* If an error occurs, it returns an error message.
    
* If the user object includes an image attribute (indicating that they are an instructor), they are prevented from logging in.
    

Once the student is signed in, you must store their details in a Supabase table. This allows you to add a `following_list` column that tracks the instructors they follow. The list will be updated whenever the student follows or unfollows an instructor.

```typescript
export async function studentLogIn(formData: FormData) {
	//...other functions

	const { data: existingUser } = await supabase
		.from("students")
		.select()
		.eq("email", credentials.email)
		.single();

	//👇🏻 if student doesn't exist
	if (!existingUser) {
		const { error: insertError } = await supabase.from("students").insert({
			email: credentials.email,
			name: data.user.user_metadata.name,
			interest: data.user.user_metadata.interest,
			id: data.user.id,
			following_list: [] as string[],
		});

		if (insertError) {
			return { error: insertError.message, status: 500, user: null };
		}
	}

	revalidatePath("/", "layout");
	return { error: null, status: 200, user: data.user };
}
```

Every time a student logs in, the code checks if they already exist in the `students` table.

* If the student is found, no new entry is created.
    
* If the student is not found, a new row with their details is added.
    

Each student’s data includes two primary keys: `id` and `email` and additional columns: `interest`, `name`, and `following_list`.

![Student registration form with fields for full name, email address, interest, and password. Includes a "Register" button and a sign-in option for existing accounts. The browser tab shows the URL "localhost:3000".](https://cdn.hashnode.com/res/hashnode/image/upload/v1740654932982/724fcf11-55e3-4163-9a6e-0b2771d0874c.gif align="center")

### Instructor Authentication with Supabase

The instructor's user object is quite different from the student's. It includes data such as email, password, name, interest, occupation, bio, URL, and image.

Add the following function to `actions/auth.ts` to handle instructor sign-ups:

```typescript
export async function instructorSignUp(formData: FormData) {
	const supabase = await createClient();

	//👇🏻 get user credentials from the form
	const credentials = {
		email: formData.get("email") as string,
		password: formData.get("password") as string,
		interest: formData.get("interest") as string,
		name: formData.get("name") as string,
		occupation: formData.get("occupation") as string,
		bio: formData.get("bio") as string,
		url: formData.get("url") as string,
		image: formData.get("image") as File,
	};

	//👉🏻 following code snippet below
}
```

Next, upload the image to Supabase Storage and retrieve its download URL before signing up the user as an instructor. Update the `instructorSignUp` function to show this:

```typescript
export async function instructorSignUp(formData: FormData) {
	//👇🏻 upload instructor's image
	const { data: imageData, error: imageError } = await supabase.storage
		.from("headshots")
		.upload(`${crypto.randomUUID()}/image`, credentials.image);

	if (imageError) {
		return { error: imageError.message, status: 500, user: null };
	}
	//👇🏻 get the image URL
	const imageURL = `${process.env.STORAGE_URL!}${imageData.fullPath}`;

	//👇🏻 authenticate user as instructor
	const { data, error } = await supabase.auth.signUp({
		email: credentials.email,
		password: credentials.password,
		options: {
			data: {
				interest: credentials.interest,
				name: credentials.name,
				occupation: credentials.occupation,
				bio: credentials.bio,
				url: credentials.url,
				image: imageURL,
			},
		},
	});

	//👇🏻 return user or error object
	if (error) {
		return { error: error.message, status: error.status, user: null };
	}

	revalidatePath("/", "layout");
	return { error: null, status: 200, user: data.user };
}
```

Finally, an [instructor login function](https://github.com/dha-stix/stream-lms/blob/main/actions/auth.ts) that authenticates the user, similar to the student login function, should be created. It should check whether the instructor already exists in the `instructors` table. If the instructor does not exist, execute the function to add the instructor's user object to the database table.

Here is the Supabase function for adding an instructor to the table:

```typescript
const { error: insertError } = await supabase.from("instructors").insert({
	email: credentials.email,
	name: data.user.user_metadata.name,
	occupation: data.user.user_metadata.occupation,
	bio: data.user.user_metadata.bio,
	url: data.user.user_metadata.url,
	image: data.user.user_metadata.image,
	id: data.user.id,
	interest: data.user.user_metadata.interest,
	followers: [],
});
```

The `instructors` table includes an additional `followers` attribute, which stores an array of student IDs following the instructor. You can find the [complete code on GitHub](https://github.com/dha-stix/stream-lms/blob/main/actions/auth.ts).

Additionally, authentication functions like [**getUserSession**](https://github.com/dha-stix/stream-lms/blob/main/actions/auth.ts) and [**logOut**](https://github.com/dha-stix/stream-lms/blob/main/actions/auth.ts) must be created. These functions will retrieve the current user's object and allow them to log out when necessary, such as when clicking a logout button.

![Instructor login page with fields for email and password, a "Sign in" button, and a link to create an account. A sidebar on the left displays "LinkedUp" with a "Student Sign-in" link.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740655472825/4c038412-fe6d-4449-b2a9-d9d3649da2f8.gif align="center")

## The Application Database Design

In the previous section, we created two database tables: `instructors` and `students`, which store instructors and students separately. Instructors can also upload headshot images to [Supabase Storage](https://supabase.com/docs/guides/storage/quickstart).

In this section, you'll learn how to create these tables, define their access policies, and retrieve or modify data within the tables.

| **Announcements (data type)** | **Instructors (data type)** | **Students (data type)** |
| --- | --- | --- |
| id (int8) | id (uuid) | id (uuid) |
| created\_at (timestamptz) | created\_at (timestamptz) | created\_at (timestamptz) |
| author\_name (text) | name (text) | email (text) |
| interest (text) | email (text) | name (text) |
| author\_title (text) | occupation (text) | interest (text) |
| author\_id (uuid) | bio (text) | following\_list (uuid\[\]) |
| content (text) | url (text) |  |
| likes (uuid \[\]) | interest (text) |  |
| author\_image (text) | image (text) |  |
|  | followers (uuid\[\]) |  |

**Note:** The `instructors` table includes an `image` column that stores the instructor's headshot URL. You can obtain this by creating a Supabase bucket named `headshot` and uploading the image when the instructor signs up.

The `instructors` and `students` tables have two primary keys: `id` and `email`.

Supabase allows you to define policies for your tables, controlling the operations different users can perform within the application.

Next, let’s create the access policies for each table.

### Access Policy for the Announcements Table

The `announcements` table has four access policies:

* Enable delete operation for users based on their user ID.
    
    ```sql
    alter policy "Enable delete for users based on user_id"
    on "public"."announcements"
    to public
    using (
      (( SELECT auth.uid() AS uid) = author_id)
    );
    ```
    
* Enable insert operation for authenticated users only.
    
    ```sql
    alter policy "Enable insert for authenticated users only"
    on "public"."announcements"
    to authenticated
    with check (
      true
    );
    ```
    
* Enable read access for all users.
    
    ```sql
    alter policy "Enable read access for all users"
    on "public"."announcements"
    to public
    using (
      true
    );
    ```
    
* Enable update operation for authenticated users only.
    
    ```sql
    alter policy "Enable update for authenticated users"
    on "public"."announcements"
    to authenticated
    using (
      (auth.role() = 'authenticated'::text)
    );
    ```
    

### Access Policy for the Instructors Table

The `instructors` table has three policies:

* Allow only authenticated users to update the `instructors` table.
    
    ```sql
    alter policy "Allow only authenticated users"
    on "public"."instructors"
    to authenticated
    using (
      (auth.role() = 'authenticated'::text)
    );
    ```
    
* Enable insert operation for authenticated users only.
    
    ```sql
    alter policy "Enable insert for authenticated users only"
    on "public"."instructors"
    to authenticated
    with check (
      true
    );
    ```
    
* Enable read access for all users.
    
    ```sql
    alter policy "Enable read access for all users"
    on "public"."instructors"
    to public
    using (
      true
    );
    ```
    

### Access Policy for the Students Table

The `students` table has three access policies:

* Enable insert operation for authenticated users only.
    
    ```sql
    alter policy "Enable insert for authenticated users only"
    on "public"."students"
    to authenticated
    with check (
      true
    );
    ```
    
* Enable update operation for authenticated users only.
    
    ```sql
    alter policy "Enable update for only authenticated users"
    on "public"."students"
    to authenticated
    using ((auth.role() = 'authenticated'::text))
    ```
    
* Enable read access for authenticated users only.
    
    ```sql
    alter policy "Read access for only authenticated users"
    on "public"."students"
    to authenticated
    using (
      true
    );
    ```
    

## How to Add a Video Conferencing Feature with Stream

In this section, I'll walk you through adding a video conferencing feature to the application using the [Stream Audio & Video SDK](https://getstream.io/video/docs/react/). This will enable instructors to schedule educational sessions and allow students to join the meetings.

### Setting Up Stream Video & Audio SDK in Next.js

Create a [Stream account](https://getstream.io/) and a new organization that holds all your apps.

![Form for creating an organization, with fields for organization name, e-mail address, and website URL, and buttons labeled "Cancel" and "Submit".](https://cdn.hashnode.com/res/hashnode/image/upload/v1740657831403/ba044353-b0f4-4380-82cf-5abeedd68ac9.png align="center")

Add a new app to the organization and copy the Stream API and Secret key into the `.env.local` file.

```bash
NEXT_PUBLIC_STREAM_API_KEY=<paste_from_Stream_app_dashboard>
STREAM_SECRET_KEY=<paste_from_Stream_app_dashboard>
```

![Dashboard interface displaying chat overview with key metrics like Monthly Active Users (4 MAUs), Max Concurrent Connections (2), and Message Volume (3). Includes app access keys created on February 17th, 2025.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740658025617/e8fb8a44-0a16-4730-875a-be3c2255276f.png align="center")

Create a new file named `stream.action.ts` inside the `actions` folder at the root of your Next.js project. This is the same folder where the authentication server actions for Supabase are stored. Then, copy the following code snippet into the file:

```typescript
"use server";

import { getUserSession } from "./auth";
import { StreamClient } from "@stream-io/node-sdk";

const STREAM_API_KEY = process.env.NEXT_PUBLIC_STREAM_API_KEY!;
const STREAM_API_SECRET = process.env.STREAM_SECRET_KEY!;

export const tokenProvider = async () => {
	const { user } = await getUserSession();

	if (!user) throw new Error("User is not authenticated");
	if (!STREAM_API_KEY) throw new Error("Stream API key secret is missing");
	if (!STREAM_API_SECRET) throw new Error("Stream API secret is missing");

	const streamClient = new StreamClient(STREAM_API_KEY, STREAM_API_SECRET);

	const expirationTime = Math.floor(Date.now() / 1000) + 3600;
	const issuedAt = Math.floor(Date.now() / 1000) - 60;

	const token = streamClient.generateUserToken({
		user_id: user.id,
		exp: expirationTime,
		validity_in_seconds: issuedAt,
	});

	return token;
};
```

* From the code snippet above,
    
    * The **getUserSession** function returns the Supabase user object for the current user.
        
    * The **tokenProvider** function generates an authentication token for the user, enabling Stream to identify and manage users during real-time communication.
        

Create a `providers` folder containing a `StreamVideoProvider` component within the Next.js app folder and copy the following code snippet into the file:

```typescript
"use client";
import { createClient } from "../../../utils/supabase/client";
import { tokenProvider } from "../../../actions/stream.action";
import { StreamVideo, StreamVideoClient } from "@stream-io/video-react-sdk";
import { useState, ReactNode, useEffect, useCallback } from "react";
import { Loader2 } from "lucide-react";

const apiKey = process.env.NEXT_PUBLIC_STREAM_API_KEY!;

export const StreamVideoProvider = ({ children }: { children: ReactNode }) => {
	const [videoClient, setVideoClient] = useState<StreamVideoClient | null>(
		null
	);
	const supabase = createClient();

	const getUser = useCallback(async () => {
		//👉🏻 get user object from Supabase
		//👉🏻 set Stream user data
		// 👉🏻 initialize Stream video client using the Stream API key, Stream user data, and token Provider
	}, [supabase.auth]);

	useEffect(() => {
		getUser();
	}, [getUser]);

	if (!videoClient)
		return (
			<div className='h-screen flex items-center justify-center'>
				<Loader2 size='32' className='mx-auto animate-spin' />
			</div>
		);

	return <StreamVideo client={videoClient}>{children}</StreamVideo>;
};
```

The `StreamVideoProvider` component is initialized and manages Stream’s video functionality across the application. It wraps all pages that require access to Stream's real-time video features. This includes:

* `instructor/[id]` – displays an instructor’s upcoming sessions.
    
* `instructor/dashboard` – allows instructors to schedule new video calls.
    

Update the `getUser` function as shown below:

```typescript
const getUser = useCallback(async () => {
	const { data, error } = await supabase.auth.getUser();
	const { user } = data;
	if (error || !user || !apiKey) return;
	if (!tokenProvider) return;

	let streamUser;

	if (user.user_metadata?.image) {
		streamUser = {
			// 👇🏻 user is an instructor
			id: user.id,
			name: user.user_metadata?.name,
			image: user.user_metadata?.image,
		};
	} else {
		// 👇🏻 user is a student
		streamUser = {
			id: user.id,
			name: user.user_metadata?.name,
		};
	}

	//👇🏻 create s Stream video client
	const client = new StreamVideoClient({
		apiKey,
		user: streamUser,
		tokenProvider,
	});

	setVideoClient(client);
}, [supabase.auth]);
```

The `getUser` function retrieves the current user's data from Supabase Auth, sets up the Stream user, and initializes a Stream video client using the Stream API key, the user’s object and the token.

### Creating and Scheduling Calls with Stream

Here, you will learn how to allow instructors to schedule calls using the Stream Video & Audio SDK.

Before we proceed, create a `hooks` folder within the Next.js app folder and add these files:

```bash
cd app && mkdir hooks
cd hooks
touch useGetCallById.ts useGetCalls.ts
```

The `useGetCallById` file defines a React hook that fetches details of a specific Stream call via its ID, while the `useGetCalls` hook retrieves all calls created by a particular Stream user.

Let's create these custom React hooks.

Copy the following code snippet into the `useGetCallById.ts` file:

```typescript
import { useEffect, useState } from "react";
import { Call, useStreamVideoClient } from "@stream-io/video-react-sdk";

export const useGetCallById = (id: string | string[]) => {
	const [call, setCall] = useState<Call>();
	const [isCallLoading, setIsCallLoading] = useState(true);

	const client = useStreamVideoClient();

	useEffect(() => {
		if (!client) return;

		const loadCall = async () => {
			try {
				// https://getstream.io/video/docs/react/guides/querying-calls/#filters
				const { calls } = await client.queryCalls({
					filter_conditions: { id },
				});

				if (calls.length > 0) setCall(calls[0]);

				setIsCallLoading(false);
			} catch (error) {
				console.error(error);
				setIsCallLoading(false);
			}
		};

		loadCall();
	}, [client, id]);

	return { call, isCallLoading };
};
```

Add the following to the `useGetCalls.ts` file:

```typescript
import { useEffect, useState } from "react";
import { Call, useStreamVideoClient } from "@stream-io/video-react-sdk";
import { useParams } from "next/navigation";

export const useGetCalls = () => {
	const client = useStreamVideoClient();
	const [calls, setCalls] = useState<Call[]>();
	const [isLoading, setIsLoading] = useState(false);
	const { id } = useParams<{ id: string }>();

	useEffect(() => {
		const loadCalls = async () => {
			if (!client || !id) return;

			setIsLoading(true);

			try {
				const { calls } = await client.queryCalls({
					sort: [{ field: "starts_at", direction: 1 }],
					filter_conditions: {
						starts_at: { $exists: true },
						$or: [{ created_by_user_id: id }, { members: { $in: [id] } }],
					},
				});

				setCalls(calls);
			} catch (error) {
				console.error(error);
			} finally {
				setIsLoading(false);
			}
		};

		loadCalls();
	}, [client, id]);

	const now = new Date();
	//👇🏻 upcoming calls
	const upcomingCalls = calls?.filter(({ state: { startsAt } }: Call) => {
		return startsAt && new Date(startsAt) > now;
	});
	//👇🏻 ongoing calls
	const ongoingCalls = calls?.filter(
		({ state: { startsAt, endedAt } }: Call) => {
			return startsAt && new Date(startsAt) < now && !endedAt;
		}
	);

	return { upcomingCalls, isLoading, ongoingCalls };
};
```

The **useGetCalls** hook retrieves all calls where the instructor is either the creator or a participant, returning both current and upcoming calls. It also returns an **isLoading** state to indicate when data is being fetched, allowing for conditional rendering.

Add the function below to the instructor's dashboard to allow instructors to create or schedule calls. This function accepts a call description along with the scheduled date and time.

```typescript
//👇🏻 imports
import { useStreamVideoClient, Call } from "@stream-io/video-react-sdk";
const client = useStreamVideoClient();
//👇🏻 Form states
const [description, setDescription] = useState<string>("");
const [dateTime, setDateTime] = useState<string>("");

const handleScheduleMeeting = async (e: React.FormEvent<HTMLFormElement>) => {
	e.preventDefault();
	if (!client || !user) return;

	try {
		const id = crypto.randomUUID();
		const call = client.call("default", id);
		if (!call) throw new Error("Failed to create meeting");
    //👇🏻 create Stream call
		await call.getOrCreate({
			data: {
				starts_at: new Date(dateTime).toISOString(),
				custom: {
					description,
				},
			},
		});

		//👇🏻 Call object
		console.log({ call });
	} catch (error) {
		console.error(error);
	}
};
```

The code snippet above initializes a Stream video call with a default call type. It assigns the call a unique ID, sets the scheduled date and time, and includes a custom description.

**Note:** Ensure that the `<StreamVideoProvider>` component wraps the instructor's dashboard where the video call is being created. You can achieve this by adding a `layout.tsx` file to the dashboard page and wrapping all child elements with `<StreamVideoProvider>`.

![Dashboard interface titled "LinkedUp" with sections for followers, announcements, and options to make an announcement, schedule a call, or access the community channel. Logout button is visible at the top right.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740658849436/109c53d7-c818-4d79-8bd7-19c3c0ae62a2.gif align="center")

### Joining Stream Video Calls

The `instructor/[id]` page displays detailed information about a specific instructor from Supabase and lists of their current and upcoming calls. This allows students to view scheduled meetings and join them when they start.

![Screenshot of a profile page for Carl John, a UI Designer, on a platform called LinkedUp. It includes a profile picture, a button for joining a community channel, announcements with delete options, and upcoming meetings with join and copy link options.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740659135003/0c53b3b6-fa91-4d28-81cf-89e8c90b7e02.gif align="center")

To implement this functionality, we will use the `MeetingsBox` component within the instructor's profile page and create a dedicated `calls/[id]` page route for joining calls.

First, create a `(stream)` folder and add a `calls/[id]` page route. Then, create a `layout.tsx` file within the `(stream)` folder and insert the following code:

```typescript
import { StreamVideoProvider } from "../providers/StreamVideoProvider";
import type { Metadata } from "next";

export const metadata: Metadata = {
	title: "Calls & Chat | LinkedUp",
	description: "Generated by create next app",
};

export default function AuthLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return <StreamVideoProvider>{children}</StreamVideoProvider>;
}
```

The `layout.tsx` file ensures that the `StreamVideoProvider` component wraps all pages inside the `(stream)` folder, enabling access to Stream's video and audio features across these pages.

Next, render the calls within the [MeetingsBox component](https://github.com/dha-stix/stream-lms/blob/main/src/app/instructor/%5Bid%5D/\(components\)/MeetingsBox.tsx) and and let students join meetings.

```typescript
"use client";
import { formatDateTime } from "@/lib/utils";
import { Call } from "@stream-io/video-react-sdk";
import { useRouter } from "next/navigation";

export default function MeetingsBox({
	upcomingCalls,
	isLoading,
	ongoingCalls,
}: {
	upcomingCalls: Call[] | undefined;
	isLoading: boolean;
	ongoingCalls: Call[] | undefined;
}) {
	const router = useRouter();

	if (isLoading || !upcomingCalls || !ongoingCalls) {
		return <p className='text-xs opacity-60'>Fetching calls...</p>;
	}

	if (upcomingCalls.length === 0) {
		return <p className='text-xs  opacity-60'>No upcoming meetings</p>;
	}

	return {
		// --- upcoming and ongoing calls display elements ---
	};
}
```

Return the following UI elements from the component to allow everyone to see the instructor's current and upcoming meetings.

```typescript
return (
	<div className='space-y-4'>
		// --- ongoing calls ---
		{ongoingCalls.map((call) => (
			<div className='bg-white p-2 rounded-md' key={call.id}>
				<h3 className='text-sm font-bold text-gray-500 mb-2'>
					{call.state.custom.description}
				</h3>
				<p className='text-xs'>
					Started: {formatDateTime(call.state?.startsAt?.toLocaleString())}
				</p>
				<div className='flex items-center space-x-4'>
					<button
						className='bg-blue-500 text-white px-4 py-2 text-xs rounded-md mt-2'
						onClick={() => handleJoinCall(call)}
					>
						Join In
					</button>

					<button
						className='bg-gray-500 text-white px-4 py-2 text-xs rounded-md mt-2'
						onClick={() => handleCopyLink(call)}
					>
						Copy Link
					</button>
				</div>
			</div>
		))}
		// --- upcoming calls ---
		{upcomingCalls.map((call) => (
			<div className='bg-white p-2 rounded-md' key={call.id}>
				<h3 className='text-sm font-bold text-gray-500 mb-2'>
					{call.state.custom.description}
				</h3>

				<div className='flex items-center space-x-4'>
					<button
						className='bg-blue-500 text-white px-4 py-2 text-xs rounded-md mt-2'
						disabled={true}
					>
						{formatDateTime(call.state?.startsAt?.toLocaleString())}
					</button>

					<button
						className='bg-gray-500 text-white px-4 py-2 text-xs rounded-md mt-2'
						onClick={() => handleCopyLink(call)}
					>
						Copy Link
					</button>
				</div>
			</div>
		))}
	</div>
);
```

The `MeetingsBox` component renders the instructor's current and upcoming calls, allowing users to copy the call link and join meetings.

![Profile page for Carl John, a UI Designer, featuring announcements and upcoming meetings. Links to "Join my Community Channel" and meeting details are shown.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740659373366/9150c744-7bb0-4e1f-99f5-b6b89d2bc488.png align="center")

Execute the `handleJoinCall` function to redirect the user to the call page. This allows them to confirm the action before joining the call. The `handleCopyLink` function copies the call link to the clipboard.

```typescript
const handleJoinCall = (call: Call) => {
	router.push(`/call/${call.id}`);
};

const handleCopyLink = (call: Call) => {
	navigator.clipboard.writeText(
		`${process.env.NEXT_PUBLIC_PAGE_URL!}/call/${call.id}`
	);
	console.log({
		title: "Link copied to clipboard",
		description: "You can now share the link with interested participants",
	});
};
```

Now, create the `call/[id]/page.tsx` component and copy the following code into the file:

```typescript
"use client";
import { useParams } from "next/navigation";
import { useEffect, useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import { User } from "@supabase/supabase-js";
import { createClient } from "../../../../../utils/supabase/client";

export default function CallPage() {
	const { id } = useParams<{ id: string }>();
	const [user, setUser] = useState<User | null>(null);
	const router = useRouter();

	const authenticateUser = useCallback(async () => {
		const supabase = createClient();
		const { data } = await supabase.auth.getUser();
		const userData = data.user;
		if (!userData) {
			return router.push("/student/auth/login");
		}
		setUser(userData);
	}, [router, call, camMicEnabled]);

	useEffect(() => {
		authenticateUser();
	}, [authenticateUser]);

	return {
		// -- Conditionally render Stream Call component --
	};
}
```

The code snippet authenticates the user to ensure they are signed in.

Next, fetch the call details using the call ID from the page route via the `useParams` hook.

```typescript
"use client";
//..other imports
import { useGetCallById } from "@/app/hooks/useGetCallById";
import { StreamCall, StreamTheme } from "@stream-io/video-react-sdk";

export default function CallPage() {
	//..other states
	const { call, isCallLoading } = useGetCallById(id);
	const [confirmJoin, setConfirmJoin] = useState<boolean>(false);
	const [camMicEnabled, setCamMicEnabled] = useState<boolean>(false);

	const handleJoin = () => {
		//👇🏻 Stream join call function
		call?.join();
		setConfirmJoin(true);
	};

	if (isCallLoading) return <p>Loading...</p>;

	if (!call) return <p>Call not found</p>;

	return (
		<main className='min-h-screen w-full items-center justify-center'>
			<StreamCall call={call}>
				<StreamTheme>
					{confirmJoin ? (
						<MeetingRoom call={call} />
					) : (
						<div className='flex flex-col items-center justify-center gap-5 h-screen w-full'>
							<h1 className='text-3xl font-bold'>Join Call</h1>
							<p className='text-lg'>
								Are you sure you want to join this call?
							</p>
							<div className='flex gap-5'>
								<button
									onClick={handleJoin}
									className='px-4 py-3 bg-blue-600 text-blue-50'
								>
									Join
								</button>
								<button
									onClick={() => router.back()}
									className='px-4 py-3 bg-red-600 text-red-50'
								>
									Cancel
								</button>
							</div>
						</div>
					)}
				</StreamTheme>
			</StreamCall>
		</main>
	);
}
```

In the code snippet above,

* The [**StreamCall** component](https://getstream.io/video/docs/react/ui-components/core/stream-call/) wraps the entire call page, allowing access to various audio and video calling features. It accepts the **call object** as a prop.
    
* The [**StreamTheme** component](https://getstream.io/video/docs/react/ui-components/video-theme/) provides UI styling for the call, enabling you to use different themes.
    
* The `confirmJoin` state is initially set to `false`. When the user clicks the **Join** button, it triggers the `handleJoin` function, which joins the call and updates `confirmJoin` to `true`.
    
* When `confirmJoin` is `true`, the component renders the `MeetingRoom` component, which includes all prebuilt and customizable UI elements for the call provided by Stream.
    

Finally, update the `authenticateUser` function to prompt the Stream user to enable or disable the camera and microphone immediately after joining a call.

```typescript
//👇🏻 call & camera disable/enable state
const [camMicEnabled, setCamMicEnabled] = useState<boolean>(false);

const authenticateUser = useCallback(async () => {
	const supabase = createClient();
	const { data } = await supabase.auth.getUser();
	const userData = data.user;
	if (!userData) {
		return router.push("/student/auth/login");
	}
	setUser(userData);
	//👇🏻 Enable camera and microphone
	if (camMicEnabled) {
		call?.camera.enable();
		call?.microphone.enable();
	} else {
		call?.camera.disable();
		call?.microphone.disable();
	}
}, [router, call, camMicEnabled]);

useEffect(() => {
	authenticateUser();
}, [authenticateUser]);
```

### Stream Call UI Components

Stream makes setting up a call page easy using minimal UI components. It provides two prebuilt [call layouts](https://getstream.io/video/docs/react/ui-components/core/call-layout/) (**PaginatedGridLayout** and **SpeakerLayout)** and a customizable [**CallControls** component.](https://getstream.io/video/docs/react/ui-cookbook/replacing-call-controls/)

* PaginatedGridLayout and SpeakerLayout define how call participants are displayed on the call page.
    
* CallControls provides essential call functionalities such as toggling video and audio, sharing the screen, leaving the call, and more.
    

![Video call interface with a person in a small window. The microphone is muted, indicated by a crossed-out microphone icon. Other controls and a red "End Call for Everyone" button are visible at the bottom.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740659807590/b3e24561-60fc-4e0d-8054-a02d78a745a2.gif align="center")

Create the **MeetingRoom** component as follows:

```typescript
const MeetingRoom = ({call} : {call: Call}) => {
	const [layout, setLayout] = useState<CallLayoutType>("grid");
	const router = useRouter();

//👇🏻 allows members to leave the call
	const handleLeave = () => {
        if (confirm("Are you sure you want to leave the call?")) {
            router.push("/");
        }
	};

//👇🏻 describes the call layout
	const CallLayout = () => {
		switch (layout) {
			case "grid":
				return <PaginatedGridLayout />;
			case "speaker-right":
				return <SpeakerLayout participantsBarPosition='left' />;
			default:
				return <SpeakerLayout participantsBarPosition='right' />;
		}
	};

  return (
    //  -- Stream call UI component--
  )
}
```

The `handleLeave` function enables call participants to leave the call and the `CallLayout` component determines how they are laid out on the screen.

Return the following from the `MeetingRoom` component:

```typescript
return (
	<section className='relative min-h-screen w-full overflow-hidden pt-4'>
		<div className='relative flex size-full items-center justify-center'>
			<div className='flex size-full max-w-[1000px] items-center'>
				<CallLayout />
			</div>
			<div className='fixed bottom-0 flex w-full items-center justify-center gap-5'>
				<CallControls onLeave={handleLeave} />
			</div>

			<div className='fixed bottom-0 right-0 flex items-center justify-center gap-5 p-5'>
				<EndCallButton call={call} />
			</div>
		</div>
	</section>
);
```

The CallLayout and CallControls components are rendered on the page, allowing users to communicate, share their screen, turn their camera on or off, and engage in conversations through reactions.

Finally, create the **EndCallButton** component to enable the host (instructor) to end the call for everyone.

```typescript
//👇🏻 Stream call hook
import { useCallStateHooks } from "@stream-io/video-react-sdk";

const EndCallButton = ({ call }: { call: Call }) => {
	const { useLocalParticipant } = useCallStateHooks();
	const localParticipant = useLocalParticipant();
	const router = useRouter();

	const participantIsHost =
		localParticipant &&
		call.state.createdBy &&
		localParticipant.userId === call.state.createdBy.id;

	if (!participantIsHost) return null;

	const handleEndCall = () => {
		call.endCall();
		console.log({
			title: "Call Ended",
			description: "The call has been ended for everyone",
		});
		router.push("/");
	};

	return (
		<button
			className='bg-red-500 text-white px-4 py-2 rounded-md mt-2'
			onClick={handleEndCall}
		>
			End Call for Everyone
		</button>
	);
};
```

The code snippet above ensures that only the call host can end the call for all participants. It first checks if the current user is the host before displaying the ["End Call for Everyone" button](https://getstream.io/video/docs/api/calls/#ending-calls).

![Profile page of a UI Designer named Carl John. The page includes an announcement section with posts, an upcoming meetings section with join and copy link options, and a log out button. A button to join a community channel is also present.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740660039466/1851aba0-6961-4b54-87cf-54a3a98bb61a.gif align="center")

## How to Integrate a Group Chat Feature Using Stream Chat Messaging

In this section, you will learn how to integrate a community chat feature into the application. Each instructor will create a group chat for their followers (students). The chat will allow students to interact with one another and share documents, video links, text, images, and so on using the [Stream Chat Messaging SDK](https://getstream.io/chat/docs/sdk/react/).

### Setting Up the Stream Chat SDK in Next.js

Add the following code snippet to the `stream.action.ts` file:

```typescript
import { StreamChat } from "stream-chat";
import { getUserSession } from "./auth";

//👇🏻 creates a StreamChat instance
const serverClient = StreamChat.getInstance(STREAM_API_KEY, STREAM_API_SECRET);

//👇🏻 creates a token
export async function createToken(): Promise<string> {
	const { user } = await getUserSession();
	if (!user) throw new Error("User is not authenticated");
	return serverClient.createToken(user.id);
}
```

The code snippet above initializes a Stream Chat instance using its API key and secret key. It also includes a function that generates and returns a token based on the current user's ID.

To ensure that only instructors can create a community channel, follow these steps:

1. Retrieve all the channels where the instructor is a member.
    
2. If no channels are found (i.e., the returned array is empty), the instructor can create a new channel.
    
3. An error message is displayed if a channel already exists, informing the instructor that they can only have one community channel.
    
    ```typescript
    export async function createChannel({
    	userId,
    	data,
    }: {
    	userId: string;
    	data: { name: string; imageUrl: string };
    }) {
    	try {
    		//👇🏻 retrieve channel list
    		const channels = await serverClient.queryChannels(
    			{
    				members: { $in: [userId] },
    				type: "messaging",
    			},
    			{ last_message_at: -1 }
    		);
    		//👇🏻 instructor already has a channel
    		if (channels.length > 0) {
    			return {
    				success: false,
    				error: "You already have an existing channel",
    				id: channels[0].id,
    			};
    		}
    		//👇🏻 declare channel type
    		const channel = serverClient.channel("messaging", `channel-${userId}`, {
    			name: data.name,
    			image: data.imageUrl,
    			members: [userId],
    			created_by_id: userId,
    		});
    		//👇🏻 create a channel
    		await channel.create();
    		return { success: true, error: null, id: channel.id };
    	} catch (err) {
    		return { success: false, error: "Failed to create channel", id: null };
    	}
    }
    ```
    

The code snippet above [creates a public channel](https://getstream.io/chat/docs/react/creating_channels/), meaning anyone can join at any time. Also, the channel name is linked to the instructor's ID, ensuring it remains unique to that instructor.

To retrieve the instructor's channel link, add a function inside the `stream.action.ts` file. This function should return the channel URL (channel ID), allowing members to access the channel whenever needed. Then, you can display this link on the instructor's profile for easy access.

```typescript
export async function getInstructorChannel(userId: string) {
	try {
		const channels = await serverClient.queryChannels(
			{
				members: { $in: [userId] },
				type: "messaging",
			},
			{ last_message_at: -1 }
		);
		return `/chat/${channels[0].id}`;
	} catch (err) {
		return null;
	}
}
```

Finally, to grant users access to the channel page, check if the user is already a member. If not, add the student as a member before rendering the chat page. This ensures that only authorized users can participate in the conversation.

```typescript
export async function addUserToChannel(channelId: string, userId: string) {
	try {
		//👇🏻 check if student is already a member
		const channels = await serverClient.queryChannels(
			{
				members: { $in: [userId] },
				type: "messaging",
				id: channelId,
			},
			{ last_message_at: -1 }
		);
		//👇🏻 student already a member (success - show chat page)
		if (channels.length > 0) {
			return {
				success: true,
				message: "Already a member",
				id: channels[0].id,
				error: null,
			};
		}
		//👇🏻 get channel by ID (student not a member)
		const channel = serverClient.channel("messaging", channelId);
		//👇🏻 add student to channel as a member
		await channel.addMembers([userId]);
		//👇🏻 student now a member (success - show chat page)
		return {
			success: true,
			error: null,
			id: channel.id,
			message: "Member just added",
		};
	} catch (error) {
		console.error("Error adding user to channel:", error);
		return {
			success: false,
			error: "Failed to add user to channel",
			id: null,
			message: null,
		};
	}
}
```

![The Stream Chat page using the Stream Call UI components](https://cdn.hashnode.com/res/hashnode/image/upload/v1740660564180/474b342a-7d07-415e-b1d7-a213ed807b67.gif align="center")

### Stream Chat UI Components

Inside the `(stream)` folder, create a `chat/[id]/page.tsx` file. This page retrieves the channel ID from the page route and checks whether the user is already a channel member. If not, the user is automatically added as a member before displaying the chat interface.

Copy the following code snippet into the `chat/[id]/page.tsx` file:

```typescript
"use client";
import { useCallback, useEffect, useState } from "react";
import StreamChat from "./../(components)/StreamChat";
import { useParams } from "next/navigation";
import { useRouter } from "next/navigation";

export default function ChatPage() {
	const [userData, setUserData] = useState<UserData | null>(null);
	const [joinChannel, setJoinChannel] = useState<boolean>(false);
	const params = useParams<{ id: string }>();
	const router = useRouter();

	const fetchUserData = useCallback(async () => {
		// 👉🏻 get user object & channel id from useParams
		// 👉🏻 execute the addUserToChannel() function declared in the previous section
		// 👉🏻 update the joinChannel React state
	}, [params.id, router]);

	useEffect(() => {
		fetchUserData();
	}, [fetchUserData]);

	if (!userData) {
		return null;
	}

	return (
		<>{joinChannel ? <StreamChat user={userData} /> : <ConfirmMember />}</>
	);
}

function ConfirmMember() {
	return (
		<div className='flex flex-col items-center justify-center h-screen'>
			<h1 className='text-2xl font-bold mb-4 text-blue-500'>
				You are not a member of this channel
			</h1>
			<p className='text-lg mb-4'>
				Please wait while we add you to the channel
			</p>

			<div className='loader'>
				<Loader2 size={48} className='animate-spin' />
			</div>
		</div>
	);
}
```

This code snippet ensures that a user is either already a member of the channel or is added before displaying the chat interface. The **StreamChat** component is a custom React component that contains all the Stream Chat UI elements. The **ConfirmMember** component shows a loading message while the user is added to the channel.

Create a StreamChat component and add the following imports to the file:

```typescript
"use client";
import { useCallback } from "react";
//👇🏻 -- Stream chat UI components
import {
	Chat,
	Channel,
	ChannelList,
	Window,
	ChannelHeader,
	MessageList,
	MessageInput,
	useCreateChatClient,
} from "stream-chat-react";
// -- end of Stream chat UI components

//👇🏻 -- allows members to send emoji within the chat
import { EmojiPicker } from "stream-chat-react/emojis";
import { init, SearchIndex } from "emoji-mart";
import data from "@emoji-mart/data";
init({ data });
// -- end of emoji imports
//👇🏻 -- create token server action
import { createToken } from "../../../../../actions/stream.action";
```

Declare the StreamChat component as follows:

```typescript
export default function StreamChat({ user }: { user: UserData }) {

	const tokenProvider = useCallback(async () => {
		return await createToken();
	}, []);

	const filters = { members: { $in: [user.id] }, type: "messaging" };
	const options = { presence: true, state: true };

	const client = useCreateChatClient({
		apiKey: process.env.NEXT_PUBLIC_STREAM_API_KEY!,
		tokenOrProvider: tokenProvider,
		userData: { id: user.id, name: user.name, image: user.image },
	});

	if (!client) return <div>Loading...</div>;

  return (
    // -- Stream Chat UI components --
  )
```

The **useCreateChatClient** hook creates a Stream chat client using the Stream API key, the user's data, and the token created using the `createToken()` function declared earlier in this section.

Finally, return the chat UI from the StreamChat component:

```typescript
return (
	<Chat client={client}>
		<div className='chat-container'>
			{/* -- Channel List -- */}
			<div className='channel-list'>
				<ChannelList
					sort={{ last_message_at: -1 }}
					filters={filters}
					options={options}
				/>
			</div>

			{/* -- Messages Panel -- */}
			<div className='chat-panel'>
				<Channel EmojiPicker={EmojiPicker} emojiSearchIndex={SearchIndex}>
					<Window>
						<ChannelHeader />
						<MessageList />
						<MessageInput />
					</Window>
				</Channel>
			</div>
		</div>
	</Chat>
);
```

* From the code snippet above:
    
    * [**Chat** component](https://getstream.io/chat/docs/sdk/react/components/core-components/chat/) initializes the Stream Chat client and wraps the entire Chat page.
        
    * [**ChannelList**](https://getstream.io/chat/docs/sdk/react/components/core-components/channel_list/) shows available chat channels.
        
    * [**Channel**](https://getstream.io/chat/docs/sdk/react/components/core-components/channel/) sets up an active chat session.
        
    * **Window** contains the message display and input areas.
        
    * **ChannelHeader**, [**MessageList**](https://getstream.io/chat/docs/sdk/react/components/core-components/message_list/), and **MessageInput** provide a fully functional chat interface.
        

![A screenshot of a group chat named "UI Design Students" with 2 members, showing a brief conversation with messages "Hello" and "Hi," timestamped at 11:33 AM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740660921805/65b237a8-584a-4d71-88ed-fe7edc68b737.png align="center")

Congratulations! You've completed this tutorial. The [source code for this article is also available on GitHub](https://github.com/dha-stix/stream-lms).

## Next Steps

So far, you've learned how to build a full-stack social learning platform using Stream and Supabase. This platform enables users to interact with one another through real-time chat powered by Stream.

Stream helps you build engaging apps that scale to millions with performant and flexible Chat, Video, Voice, Feeds, and Moderation APIs and SDKs powered by a global edge network and enterprise-grade infrastructure.

Here are some useful resources to help you get started:

* [Stream Chat Documentation](https://getstream.io/chat/docs/)
    
* [Stream Video and Audio Documentation](https://getstream.io/video/)
    
* [Stream Activity Feeds](https://getstream.io/activity-feeds/)
    

Thank you for reading! 🎉
