---
title: How to Build a YouTube Clone with React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-02-10T16:55:49.000Z'
originalURL: https://freecodecamp.org/news/build-youtube-with-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/how-to-build-youtube-with-react.png
tags:
- name: React
  slug: react
- name: Web Applications
  slug: web-applications
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'In this tutorial, you will get an in-depth overview of how you can build
  a complete YouTube clone using React in 10 steps.

  I will lay out how I built a clone of the YouTube web app and the concrete steps
  you can take in order to build your own along ...'
---

In this tutorial, you will get an in-depth overview of how you can build a complete YouTube clone using React in 10 steps.

I will lay out how I built a clone of the YouTube web app and the concrete steps you can take in order to build your own along with other video-based apps like it.

Through this guide, we will cover how to build powerful web apps with React and Node using a stack of essential technologies, along with how each tool contributes to creating our overall app functionality. 

Let's get started!

## Step 1: Model our Data and Create our Database

Our application consists of two major parts, our Node backend and our React frontend.

Our backend is going to be responsible for things like authentication and authorization to log in users and make sure they can access the right content. It will also be responsible for providing our video data (like the video itself and whether we have liked or disliked it) and user-related data (like each user's profile). 

The backend is going to do all these things by interacting with our database. The database that we're going to be using is the SQL database Postgres. A tool called Prisma is going to be responsible for modeling that data (for telling our database what data it is going to store).

> Prisma is what's known as an **ORM** or an object relational mapper. It does the work of managing how our data is structured in our database, including the relationships all of our data shares with each other through **models**.

Our app will consist of six primary data models: `User`, `Comment`, `Subscription`, `Video`, `VideoLike`, and `View` data.

You can see the final version of our schema below:

```js
// prisma.schema

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id           String         @id @default(uuid())
  createdAt    DateTime       @default(now())
  username     String
  email        String         @unique
  avatar       String         @default("https://reedbarger.nyc3.digitaloceanspaces.com/default-avatar.png")
  cover        String         @default("https://reedbarger.nyc3.digitaloceanspaces.com/default-cover-banner.png")
  about        String         @default("")
  videos       Video[]
  videoLikes   VideoLike[]
  comments     Comment[]
  subscribers  Subscription[] @relation("subscriber")
  subscribedTo Subscription[] @relation("subscribedTo")
  views        View[]
}

model Comment {
  id        String   @id @default(uuid())
  createdAt DateTime @default(now())
  text      String
  userId    String
  videoId   String
  user      User     @relation(fields: [userId], references: [id])
  video     Video    @relation(fields: [videoId], references: [id])
}

model Subscription {
  id             String   @id @default(uuid())
  createdAt      DateTime @default(now())
  subscriberId   String
  subscribedToId String
  subscriber     User     @relation("subscriber", fields: [subscriberId], references: [id])
  subscribedTo   User     @relation("subscribedTo", fields: [subscribedToId], references: [id])
}

model Video {
  id          String      @id @default(uuid())
  createdAt   DateTime    @default(now())
  title       String
  description String?
  url         String
  thumbnail   String
  userId      String
  user        User        @relation(fields: [userId], references: [id])
  videoLikes  VideoLike[]
  comments    Comment[]
  views       View[]
}

model VideoLike {
  id        String   @id @default(uuid())
  createdAt DateTime @default(now())
  like      Int      @default(0)
  userId    String
  videoId   String
  user      User     @relation(fields: [userId], references: [id])
  video     Video    @relation(fields: [videoId], references: [id])
}

model View {
  id        String   @id @default(uuid())
  createdAt DateTime @default(now())
  userId    String?
  videoId   String
  user      User?    @relation(fields: [userId], references: [id])
  video     Video    @relation(fields: [videoId], references: [id])
}
```

Each of these models includes various properties with their associated data types. 

In the first column of each model are the different fields or individual properties that each model consists of, such as the `id` or unique identifier or `createdAt` timestamp when the database created a given entry. 

> You can think of each model as a special type of JavaScript object with special properties that we are creating in our schema.

If we look at the second column, we can see what the data type of each field must be. These values largely correspond to normal JavaScript types: strings, integers and dates.

Associated types can also be different data models. For example, looking at our `User` model, we see it has a `videos` field, which has a data type of `Video[]`, which means it is an array of data type `Video`. 

This makes sense – every user can logically have multiple videos that they've created. The same applies for their likes, comments, subscribers, users to which they've subscribed, and their video views. 

## Step 2: Create Auth, Video, and User Routes

Now that we have our schema created, we can create the business logic for our backend. 

We're going to be using Node with the library Express to build our backend. Express makes it very easy to build powerful APIs, which is exactly what we need for our YouTube app. 

The largest part of our API will be the routes, or individual endpoints to which our React app will be making requests for data. We will have separate routing for authentication, video, and user-related resources that will begin as follows:

```
http://localhost:3001/api/v1/auth
http://localhost:3001/api/v1/videos
http://localhost:3001/api/v1/users
```

I won't go through all of the individual routes that we need to create, but just to give you an idea of what one of them looks like, let's take a look at the video-related routes. 

```js
// server/src/routes/video.js

import { PrismaClient } from "@prisma/client";
import express from "express";

const prisma = new PrismaClient();

function getVideoRoutes() {
  const router = express.Router();

  router.get("/", getRecommendedVideos);
  router.get("/trending", getTrendingVideos);
   
  // ... many more routes omitted

  return router;
}

export async function getVideoViews(videos) {
  for (const video of videos) {
    const views = await prisma.view.count({
      where: {
        videoId: {
          equals: video.id,
        },
      },
    });
    video.views = views;
  }
  return videos;
}

async function getRecommendedVideos(req, res) {
  let videos = await prisma.video.findMany({
    include: {
      user: true,
    },
    orderBy: {
      createdAt: "desc",
    },
  });

  if (!videos.length) {
    return res.status(200).json({ videos });
  }

  videos = await getVideoViews(videos);

  res.status(200).json({ videos });
}

async function getTrendingVideos(req, res) {
  let videos = await prisma.video.findMany({
    include: {
      user: true,
    },
    orderBy: {
      createdAt: "desc",
    },
  });

  if (!videos.length) {
    return res.status(200).json({ videos });
  }

  videos = await getVideoViews(videos);
  videos.sort((a, b) => b.views - a.views);

  res.status(200).json({ videos });
}
```

We use `express.Router` to append all of our subroutes to the main route (`/api/v1/videos`) using the function `getVideoRoutes`. We create an individual route by specifying what type of request can be made to it with the appropriate method: `get`, `post`, `put`, or `delete`.

We pass to that method which endpoint we want our frontend to make the request to as well as a function to handle any incoming requests to that endpoint.

> These functions below our routes which are used to handle requests for each of our API endpoints are commonly known as **controllers**.

You can see some of the controllers that we're using here, such as `getRecommendedVideos` or `getTrendingVideos`. Their names make clear what function they perform.

For example, if our React app makes a GET request to `/api/v1/videos/`, our controller responds with the user's recommended videos. 

> Note that within each controller, we are using `PrismaClient` to interact with our database, which was generated based off of the `prisma.schema` file we created.

For our `getRecommendedVideos` controller, we use the `findMany` method to get many videos (an array of them), where the user data for each video is included (with the `include` operator for the `user` field).

And we are ordering the results by the `createdAt` field from newest to oldest (with `desc` or in descending order).

## Step 3: Protect Auth Routes with Middleware

In addition to our controllers, there is some important middleware that we need to associate with some of our routes. 

> What is middleware? **Middleware** are functions that are used to run before another function to provide a value or perform an action. In our case, middleware will run before our controller function for each route.

When a user wants to get videos that they've liked, we first need to write some middleware that will get the current user before our controller attempts to respond with the user data. 

```js
// server/src/routes/user.js

import { PrismaClient } from "@prisma/client";
import express from "express";
import { protect } from "../middleware/authorization";

const prisma = new PrismaClient();

function getUserRoutes() {
  const router = express.Router();

  router.get("/liked-videos", protect, getLikedVideos);
    
  return router;
}
```

The `protect` middleware is placed before `getLikedVideos`, which means it will run first.

The code for the `protect` function is provided below:

```js
// server/src/middleware/authorization.js

import { PrismaClient } from "@prisma/client";
import jwt from "jsonwebtoken";

const prisma = new PrismaClient();

export async function protect(req, res, next) {
  if (!req.cookies.token) {
    return next({
      message: "You need to be logged in to visit this route",
      statusCode: 401,
    });
  }

  try {
    const token = req.cookies.token;
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    const user = await prisma.user.findUnique({
      where: {
        id: decoded.id,
      },
      include: {
        videos: true,
      },
    });

    req.user = user;
    next();
  } catch (error) {
    next({
      message: "You need to be logged in to visit this route",
      statusCode: 401,
    });
  }
}
```

In our `protect` middleware function, if we don't have a user or if user has an invalid JSON Web Token, we use the `next` function to respond to the client with a 401 error. 

> A 401 error code means the current user is not authorized to access a particular resource they are requesting. 

Otherwise, if user does have a valid token, we fetch them with our Prisma Client and pass it along to our `getLikedVideos` controller. We can do so by adding a property to the request or `req` object and then calling the `next` function (which is also a middleware function).

Middleware is essential in our application primarily for things like authorization to get our currently authenticated user as well as protecting endpoints that include secure information.

Middleware is also helpful for handling errors in our backend, so that we recover from them successfully and ensure our application doesn't break when there is an error.

## Step 4: Create React Client Pages and Styles

Moving on to the React frontend, we can easily create our React app to consume our Node API with the help of Create React App. 

[To get started with Create React App](https://reedbarger.com/create-react-app-10-steps), you can simply run the command in the root of your project folder:

```bash
npx create-react-app client
```

After the installation is finished, we will have a React app placed in the folder `client`, right next to our server code in the `server` folder.

The first step with our React app is to set up all the individual routes for our application. These will be placed in the App.js component and correspond with the routes that YouTube has for their app:

```js
// client/src/App.js

import React from "react";
import { Route, Switch } from "react-router-dom";
import MobileNavbar from "./components/MobileNavbar";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import { useLocationChange } from "./hooks/use-location-change";
import Channel from "./pages/Channel";
import History from "./pages/History";
import Home from "./pages/Home";
import Library from "./pages/Library";
import LikedVideos from "./pages/LikedVideos";
import NotFound from "./pages/NotFound";
import SearchResults from "./pages/SearchResults";
import Subscriptions from "./pages/Subscriptions";
import Trending from "./pages/Trending";
import WatchVideo from "./pages/WatchVideo";
import YourVideos from "./pages/YourVideos";
import Container from "./styles/Container";

function App() {
  const [isSidebarOpen, setSidebarOpen] = React.useState(false);
  const handleCloseSidebar = () => setSidebarOpen(false);
  const toggleSidebarOpen = () => setSidebarOpen(!isSidebarOpen);
  useLocationChange(handleCloseSidebar);

  return (
    <>
      <Navbar toggleSidebarOpen={toggleSidebarOpen} />
      <Sidebar isSidebarOpen={isSidebarOpen} />
      <MobileNavbar />
      <Container>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/watch/:videoId" component={WatchVideo} />
          <Route path="/channel/:channelId" component={Channel} />
          <Route path="/results/:searchQuery" component={SearchResults} />
          <Route path="/feed/trending" component={Trending} />
          <Route path="/feed/subscriptions" component={Subscriptions} />
          <Route path="/feed/library" component={Library} />
          <Route path="/feed/history" component={History} />
          <Route path="/feed/my_videos" component={YourVideos} />
          <Route path="/feed/liked_videos" component={LikedVideos} />
          <Route path="*" component={NotFound} />
        </Switch>
      </Container>
    </>
  );
}
```

For our Router and all of our Routes, we are using the library `react-router-dom`, which will also give us some helpful React hooks to access values like route params (`useParams`) and navigate our user programmatically around the app (`useHistory`).

When it comes to building out the appearance of our application, we're going to be using a library called `styled-components`. What's very useful about styled components is that it is a **CSS-in-JS** library. 

> The benefit of a CSS-in-JS library is that we can write CSS styles in our .js files. It allows us to use React and JavaScript features that we wouldn't be able to use in a normal CSS stylesheet. 

We can pass certain values as props to our styled components just like we would a normal react component. 

So here's a look at one of our styled components, where we are conditionally setting several styles' rules based off of the value of the prop `red`.

As you might have guessed, by passing the prop blue with a value of true to our styled Button component, it makes our button the YouTube red color.

```js
// client/src/styles/Button.js

import styled, { css } from "styled-components";

const Button = styled.button`
  padding: 10px 16px;
  border-radius: 1px;
  font-weight: 400;
  font-size: 14px;
  font-size: 0.875rem;
  font-weight: 500;
  line-height: 1.75;
  text-transform: uppercase;
  letter-spacing: 0.02857em;

  ${(props) =>
    props.red &&
    css`
      background: ${(props) => props.theme.darkRed};
      border: 1px solid ${(props) => props.theme.darkRed};
      color: white;
    `}
`;

export default Button;
```

Here is how we would use the `Button` styled component we created above with the `red` prop passed to it:

```js
// example usage:
import React from "react";
import Button from "../styles/Button";
import Wrapper from "../styles/EditProfile";

function EditProfile() {
  return (
    <Wrapper>
      <div>
        <Button red onClick={() => setShowModal(true)}>
          Edit Profile
        </Button>
      </div>
    </Wrapper> 
  );
```

Another benefit of using styled components is that it gives us **scoped styles**. 

In other words, styles written within a styled component will be applied only to the component they are used in and nowhere else in our application. 

This is very different compared to normal CSS style sheets, where if you include them in their application they are global, they're applied to the entire app. 

## Step 5: Add Client Authentication with Google OAuth

The next step is to add authentication with the help of Google OAuth. 

This is something that's very easy to set up with the help of a library called `react-google-login`. It gives us both a custom hook as well as a special React component that we can use to log in our user if they have a Google account.

Below is the code used for the `GoogleAuth` component which a user can press to login immediately using a popup modal from Google:

```js
// client/src/components/GoogleAuth.js

import React from "react";
import Button from "../styles/Auth";
import { SignInIcon } from "./Icons";
import { GoogleLogin } from "react-google-login";
import { authenticate } from "../utils/api-client";

function GoogleAuth() {
  return (
    <GoogleLogin
      clientId="your-client-id-from-google-oauth"
      cookiePolicy="single_host_origin"
      onSuccess={authenticate}
      onFailure={authenticate}
      render={(renderProps) => (
        <Button
          tabIndex={0}
          type="button"
          onClick={renderProps.onClick}
          disabled={renderProps.disabled}
        >
          <span className="outer">
            <span className="inner">
              <SignInIcon />
            </span>
            sign in
          </span>
        </Button>
      )}
    />
  );
}

export default GoogleAuth;
```

## Step 6: Easily Fetch Data using React Query

Once we're able to authenticate our users, we can move on to creating our pages or page content and start making requests to our API endpoints. 

One of the most fully-featured and simple libraries for making HTTP requests is called `axios`. Additionally, the way to most easily make requests across React components is with a special library called `react-query`. 

What is very helpful about React Query is its custom React hooks. They make it possible not only to request data, but they allow us to cache (save) the results of each query we make, so we don't have to refetch data if it is already in our local cache. 

In other words, React Query is a powerful data fetching and state management library rolled into one. 

Here's a quick example of how I used React query to request all the recommended videos for users on the homepage. 

```js
// client/src/pages/Home.js

import axios from "axios";
import React from "react";
import { useQuery } from "react-query";
import ErrorMessage from "../components/ErrorMessage";
import VideoCard from "../components/VideoCard";
import HomeSkeleton from "../skeletons/HomeSkeleton";
import Wrapper from "../styles/Home";
import VideoGrid from "../styles/VideoGrid";

function Home() {
  const {
    data: videos,
    isSuccess,
    isLoading,
    isError,
    error,
  } = useQuery("Home", () =>
    axios.get("/videos").then((res) => res.data.videos)
  );

  if (isLoading) return <HomeSkeleton />;
  if (isError) return <ErrorMessage error={error} />;

  return (
    <Wrapper>
      <VideoGrid>
        {isSuccess
          ? videos.map((video) => <VideoCard key={video.id} video={video} />)
          : null}
      </VideoGrid>
    </Wrapper>
  );
}

export default Home;
```

If we're in a loading state, we show a loading skeleton like the YouTube app does. If there is an error, we show an error message within the page. 

Otherwise, if the request was successful, we show the videos that our backend recommends to our user.

## Step 7: Upload and Play User Videos

For uploading our videos, we will use the library Cloudinary. 

We can upload a video from React to Cloudinary by using a file input, with which we'll select our video file from our computer and then make a request to the Cloudinary API. It will then give us back a URL once the video is uploaded to its servers. 

From there, the user will be able to provide their video information. Once they hit publish we can save their video information in our database. 

When it comes to displaying videos that users have created, we're going to be using an open source library called `video.js`. 

To watch an individual video, we will need to fetch the video according to its id. After that we'll pass the URL to the video.js player, which will give the user the ability to scroll through the video, make it fullscreen, and change the volume. 

```js
// client/src/components/VideoPlayer.js

import React from "react";
import videojs from "video.js";
import "video.js/dist/video-js.css";
import { addVideoView } from "../utils/api-client";

function VideoPlayer({ video }) {
  const videoRef = React.useRef();

  const { id, url, thumbnail } = video;

  React.useEffect(() => {
    const vjsPlayer = videojs(videoRef.current);

    vjsPlayer.poster(thumbnail);
    vjsPlayer.src(url);

    vjsPlayer.on("ended", () => {
      addVideoView(id);
    });
  }, [id, thumbnail, url]);

  return (
    <div data-vjs-player>
      <video
        controls
        ref={videoRef}
        className="video-js vjs-fluid vjs-big-play-centered"
      ></video>
    </div>
  );
}

export default VideoPlayer;
```

Underneath the video, the user will be able to add comments, like and dislike the video, as well as subscribe to the video author's channel. 

All of these different features are going to be made possible by making network requests to our appropriate API endpoints (again, using `axios`).

## Step 8: Protect Auth Actions with a Custom Hook

Once we've created a lot of this functionality, we need to lock down some actions for users that are not authenticated.

We do not want unauthorized users to be able to attempt to login, create a comment or like a video, and so on. These are all actions that only certain authenticated users should be able to perform. 

As a result, we can create a custom hook in order to protect an authenticated action. The reason for creating this hook is to allow easy reuse across our many components that use authenticated actions within them.

This custom hook will be called `useAuthAction`.

```js
// client/src/hooks/use-auth-action.js

import { useGoogleLogin } from "react-google-login";
import { useAuth } from "../context/auth-context";
import { authenticate } from "../utils/api-client";

export default function useAuthAction() {
  const user = useAuth();
  const { signIn } = useGoogleLogin({
    onSuccess: authenticate,
    clientId: "your-client-id",
  });

  function handleAuthAction(authAction, data) {
    if (user) {
      authAction(data);
    } else {
      signIn();
    }
  }

  return handleAuthAction;
}
```

The `handleAuthAction` function is going to be returned from our hook and will accept a function that we want to execute as an argument, such as the functions to like or dislike a video. 

`handleAuthAction` will accept the function's argument as its second argument:

```js
// client/src/pages/WatchVideo.js

function WatchVideo() {
  const handleAuthAction = useAuthAction();

  function handleLikeVideo() {
    handleAuthAction(likeVideo, video.id);
  }

  function handleDislikeVideo() {
    handleAuthAction(dislikeVideo, video.id);
  }

  function handleToggleSubscribe() {
    handleAuthAction(toggleSubscribeUser, video.user.id);
  }

// rest of component
}
```

If an unauthenticated user attempts to log in or create a comment, instead of making requests to our API to create a comment, they will be automatically logged in via the `useGoogleLogin` hook from the `react-google-login` library.

## Step 9: Change User Channel Data

At this point we have displayed all of the videos that our users liked, their watch history, the channels that they are following, the trending videos, and much more. 

Finally, we are also going to display each user's channel and make it possible for them to change their user information such as their username, bio, avatar, and cover image. 

These image uploads are going to be performed once again with Cloudinary. Users will be able to select the image that they want to make as their cover avatar images. We're going to make requests to the Cloudinary API to give us a URL that we will then take and update our users' information with. 

All of these changes are going to be made possible with a modal that we're going to create. We'll create it with the package `@reach/dialog` which is going to give us a modal that is made with accessibility in mind and that we can style as we like.

Here is the code we will use inside our modal to upload our user's images and update their channel.

```js
// client/src/components/EditChannelModal.js

import React from "react";
import { useSnackbar } from "react-simple-snackbar";
import Button from "../styles/Button";
import Wrapper from "../styles/EditChannelModal";
import { updateUser } from "../utils/api-client";
import { uploadMedia } from "../utils/upload-media";
import { CloseIcon } from "./Icons";

function EditChannelModal({ channel, closeModal }) {
  const [openSnackbar] = useSnackbar();
  const [cover, setCover] = React.useState(channel.cover);
  const [avatar, setAvatar] = React.useState(channel.avatar);

  async function handleCoverUpload(event) {
    const file = event.target.files[0];

    if (file) {
      const cover = await uploadMedia({
        type: "image",
        file,
        preset: "your-cover-preset",
      });
      setCover(cover);
    }
  }

  async function handleAvatarUpload(event) {
    const file = event.target.files[0];

    if (file) {
      const avatar = await uploadMedia({
        type: "image",
        file,
        preset: "your-avatar-preset",
      });
      setAvatar(avatar);
    }
  }

  async function handleEditChannel(event) {
    event.preventDefault();
    const username = event.target.elements.username.value;
    const about = event.target.elements.about.value;

    if (!username.trim()) {
      return openSnackbar("Username cannot be empty");
    }

    const user = {
      username,
      about,
      avatar,
      cover,
    };

    await updateUser(user);
    openSnackbar("Channel updated");
    closeModal();
  }

  return (
    <Wrapper>
      <div className="edit-channel">
        <form onSubmit={handleEditChannel}>
          <div className="modal-header">
            <h3>
              <CloseIcon onClick={closeModal} />
              <span>Edit Channel</span>
            </h3>
            <Button type="submit">Save</Button>
          </div>

          <div className="cover-upload-container">
            <label htmlFor="cover-upload">
              <img
                className="pointer"
                width="100%"
                height="200px"
                src={cover}
                alt="cover"
              />
            </label>
            <input
              id="cover-upload"
              type="file"
              accept="image/*"
              style={{ display: "none" }}
              onChange={handleCoverUpload}
            />
          </div>

          <div className="avatar-upload-icon">
            <label htmlFor="avatar-upload">
              <img src={avatar} className="pointer avatar lg" alt="avatar" />
            </label>
            <input
              id="avatar-upload"
              type="file"
              accept="image/*"
              style={{ display: "none" }}
              onChange={handleAvatarUpload}
            />
          </div>
          <input
            type="text"
            placeholder="Insert username"
            id="username"
            defaultValue={channel.username}
            required
          />
          <textarea
            id="about"
            placeholder="Tell viewers about your channel"
            defaultValue={channel.about}
          />
        </form>
      </div>
    </Wrapper>
  );
}

export default EditChannelModal;
```

## Step 10: Publish our App To The Web

Once we've added all the functionality that we want, we are going to [use Heroku to deploy our React and Node app](https://reedbarger.com/react-app-node-backend) to the web. 

First we need to add a postinstall script to our Node package.json file that will tell Heroku to automatically build our React app upon deployment:

```json
{
  "name": "server",
  "version": "0.1.0",
  "scripts": {
    "start": "node server",
    ...
    "postinstall": "cd client && npm install && npm run build"
  }
}

```

To be able to tell our Node backend that we want to deploy it along with a React frontend on the same domain, we need to add the following bit of code to where our Express app is created, after all the middleware:

```js
// server/src/start.js

if (process.env.NODE_ENV === "production") {
    app.use(express.static(path.resolve(__dirname, "../client/build")));

    app.get("*", function (req, res) {
      res.sendFile(path.resolve(__dirname, "../client/build", "index.html"));
    });
}
```

The above code says: if a GET request is made to our application, but not handled by our API, respond with the built version of our React client. 

In other words, if we're not requesting data from the backend, send the built React client to our users.

## Conclusion

Hopefully this tutorial gave you some ideas about how to structure your next React project, especially if you want to build impressive apps like YouTube.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

