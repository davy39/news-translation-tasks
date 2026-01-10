---
title: How to Use the SWR Library for Better Data Fetching in React
subtitle: ''
author: Furkan Emin Can
co_authors: []
series: null
date: '2023-12-05T21:59:00.000Z'
originalURL: https://freecodecamp.org/news/swr-library-for-data-fetching-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Cover.png
tags:
- name: hooks
  slug: hooks
- name: React
  slug: react
seo_title: null
seo_desc: 'React is un-opinionated about how you fetch and manage the remote data
  in your application.

  You may think of using the useEffect hook for simple fetching operations, but it
  will not help you with caching, request deduplication, always serving real-ti...'
---

React is un-opinionated about how you fetch and manage the remote data in your application.

You may think of using the `useEffect` hook for simple fetching operations, but it will not help you with caching, request deduplication, always serving real-time data, and so on.

Things will get more complicated when you try to implement them by yourself. But fortunately, the SWR library helps us solve some common problems and it also simplifies development.

## What is the SWR Library?

According to the [SWR documentation](https://swr.vercel.app):

> The name “SWR” is derived from `stale-while-revalidate`, a HTTP cache invalidation strategy popularized by [HTTP RFC 5861](https://tools.ietf.org/html/rfc5861).   
>   
> SWR is a strategy to first return the data from cache (stale), then send the fetch request (revalidate), and finally come with the up-to-date data.

With the help of this strategy, you can make sure to always display up-to-date data to your users.

So, SWR is a library built upon the `stale-while-revalidate` strategy, and it provides React hooks for data fetching.

Before moving on to the details, let's look at the two most important concepts of SWR.

### Caching

A cache stores data for a specified amount of time and serves this data to users who request it within that period of time.

The time can be a certain period like `5000ms` or can be an event like re-connecting to the Internet.

SWR automatically caches the fetched data, helping to quickly serve the data without making redundant network requests.

### Revalidation

When the valid time is exceeded, the data becomes stale. When a user requests this data you should revalidate it before serving it.

If the data is stale, SWR revalidates it (re-fetches from the server) to keep it fresh.

By default, SWR automatically revalidates the data (it assumes that the data is stale) in three cases:

1. Every time the component is mounted, even if there is data in the cache, it revalidates.
2. It revalidates when the window gets focused.
3. It revalidates when the browser regains its network connection.

## How to Use the `useSWR` Hook

The `useSWR` hook is the main hook of the library. In your projects, you'll almost always use this hook.

It accepts three parameters: `key`, `fetcher`, and `options`.

* `key` is a unique string for the request like an id.
* `fetcher` is an async function that accepts the `key` and returns the `data`. SWR automatically passes the `key` to the `fetcher` function when loading the data.
* `options` is an object of options available for the hook. For example, you can specify the cache time in the `options` object.

And it returns an object with `data`, `error`, `isValidating`, `isLoading`, and `mutate` properties.

* `data` is the variable returned from the `fetcher` function. During the first request, it will be `undefined`.
* `error` is the error thrown by the `fetcher` function. If there is no error, it will be `undefined`.
* `isLoading` is a boolean that indicates the **first** request's status. It is `true` during the first request, and it will always be `false` thereafter.
* `isValidating` is also a boolean that indicates the request's status. It is `true` during each request including the first one.
* `mutate` is a function for manually triggering a revalidation.

## How I Used SWR in My Project

The best thing about SWR is how easy it is to use. I tried out it in my first project for the [Front End Libraries Certification](https://www.freecodecamp.org/learn/front-end-development-libraries) of freeCodeCamp and liked it very much.

I used TypeScript for the project, but will give you examples with JavaScript. So, don't worry if you don't know TypeScript – I highly recommend giving it a try if you haven't yet.

Also, if you are interested, you can find the project's code in its [GitHub repository](https://github.com/femincan/quote-factory).

### How to Add the `swr` Dependency to the Project

To be able to use the library, you can install it via `npm`, `pnpm`, or `yarn`. I prefer using `pnpm` as the package manager for my project.

```bash
$ npm i swr
# or
$ pnpm add swr
# or
$ yarn add swr
```

### Create the `fetcher` Function

The goal of this function is to fetch the data by URL and return it. I will use the function with SWR.

```javascript
const fetcher = async (url) => {
  const { data } = await axios.get(url);

  return data;
};

```

The `fetcher` function:

* accepts a `url` parameter,
* fetches the data with the `get` method of Axios,
* returns the `data` returned from the request.

### Create a Hook That Fetches a Random Quote

Based on the [SWR documentation](https://swr.vercel.app/docs/getting-started#make-it-reusable), I created a hook called `useRandomQuote`. This hook is a wrapper for the `useSWR` hook. Thus, I can use the same data wherever needed.

```javascript
import useSWR from 'swr/immutable';

const useRandomQuote = () => {
  const { data, ...restSWR } = useSWR(
    'https://api.quotable.io/quotes/random',
    fetcher
  );

  return {
    ...restSWR,
    quote: data?.[0],
  };
};

export { useRandomQuote };

```

The hook fetches the data with `useSWR` and returns an object that contains the variables destructured from the `useSWR` hook and the `quote` property which is the only element in the returned array. I used the Quotable API for a random quote, and the API returns an array with one element which is the random quote.

If you noticed, I imported the `useSWR` hook from `swr/immutable` in the code snippet. It is auto-revalidation disabled version of the hook. I prefer to use it because I want to revalidate the data manually with the `mutate` function.

### How to Revalidate the Data Manually

If you want to manually revalidate the data, you can use the `mutate` function returned from the `useSWR` hook.

When the mutate function is called, SWR revalidates the data. During this process, the `data` variable remains the same (will not be undefined), and the `isValidating` variable becomes true.

The following diagram from the [SWR documentation](https://swr.vercel.app/docs/advanced/understanding#fetch-and-revalidate) visualizes the revalidation process:

![A diagram for the "Fetch and Revalidate" pattern in SWR](https://www.freecodecamp.org/news/content/images/2023/11/fetch-and-revalidate-pattern.png)
_A diagram for the "Fetch and Revalidate" pattern in SWR_

In my project, I have a `QuoteCard` component that displays the current quote. This component has a `New Quote` button that triggers retrieving a new random quote.

```javascript
const QuoteCard = () => {
  const { /* ... */, mutate } = useRandomQuote();

  return (
    {/* ... */}
    <button
      // ...
      onClick={() => mutate()}
    >
      New Quote
    </button>
    {/* ... */}
  )
}

```

In the code above, I used the `mutate` function in the `onClick` handler of the `New Quote` button.

### How to Handle Concurrent Requests

If the user initiates a new request alongside the ongoing one, this results in multiple concurrent requests. Each request waits for the previous one to complete before starting the process, resulting in unnecessary network usage and waiting time.

I faced the same issue in my project. When the user clicks the `New Quote` button while a request is still loading, the application triggers a new request alongside the existing one.

![Concurrent requests that being triggered by clicking the "New Quote" button continuously](https://www.freecodecamp.org/news/content/images/2023/11/illustration.gif)
_Concurrent requests that being triggered by clicking the "New Quote" button continuously_

As you see in the GIF above, when I click the "New Quote" button consecutively, I have to wait for all requests to be done to see a random quote because SWR only updates the data after the last request is completed.

As a result, I should cancel the ongoing previous request after a new request is initiated. Although I checked SWR's documentation, I couldn't find a built-in solution for this issue. I tried to use `AbortController` with SWR, but couldn't succeed.

As a workaround, I disabled the `New Quote` button during validation to be able to prevent multiple concurrent requests.

A little note: I also checked [React Query](https://tanstack.com/query/latest), and it has a built-in solution for that. I am planning to experiment with it in my next project involving remote data.

## Conclusion

React doesn't care how you fetch and manage remote data. In this tutorial, you have learned how to do this with SWR. Although it has a big drawback regarding canceling concurrent requests, you can usually work around this and benefit from its upsides.

If you haven't used SWR before, I highly recommend trying it out in your future projects. It saves you time and prevents you from experiencing many types of bugs.

Thank you for reading. You can connect with me on [Twitter](https://twitter.com/femincan) or explore more on [my personal website](https://femincan.dev). Feel free to reach out — I'd love to hear from you!

