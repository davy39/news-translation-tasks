---
title: 'HTTP Error 403 Forbidden: What It Means and How to Fix It'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-14T00:45:34.000Z'
originalURL: https://freecodecamp.org/news/http-error-403-forbidden-what-it-means-and-how-to-fix-it
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb4740569d1a4ca3e9f.jpg
tags:
- name: error handling
  slug: error-handling
- name: http
  slug: http
seo_title: null
seo_desc: 'By Jackson Bates

  Receiving any error code while online can be a frustrating experience. While we''ve
  become accustomed to 404 Not Found pages, even to the extent that it''s become common
  to see cute placeholder pages to entertain us whenever we get los...'
---

By Jackson Bates

Receiving any error code while online can be a frustrating experience. While we've become accustomed to 404 Not Found pages, even to the extent that it's become common to see [cute](https://toggl.com/404) placeholder pages to [entertain](https://weemss.com/page-not-found/) us whenever we get [lost](http://www.limpfish.com/404), one of the more puzzling errors is the 403: Forbidden response.

## What does it mean?

Simply put: the server has determined that you are not allowed access to the thing you've requested.

According to [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.3):

> The 403 (Forbidden) status code indicates that the server understood the request but refuses to authorize it...If authentication credentials were provided in the request, the server considers them insufficient to grant access.

The 403 response belongs to the 4xx range of HTTP responses: Client errors. This means either you, or your browser, did something wrong.

If you encounter this it usually means that you have already authenticated yourself with the server, i.e. you've logged in, but the resource you have requested expects someone with higher privileges.

Most commonly, you might be logged in as a standard user, but you are attempting to access an admin page.

## How do you fix it?

As a user without access to the server, you really only have a few options:

### Authenticate yourself with a more appropriate account

Again, according to [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.3):

> If authentication credentials were provided in the request, the server considers them insufficient to grant access.  The client SHOULD NOT automatically repeat the request with the same credentials.  The client MAY repeat the request with new or different credentials.

This is the only one that gives you any immediate power to rectify the issue. 

If you have multiple accounts for a site and you are attempting to do something you can usually do, but this time are forbidden from doing, this is the option you should try. Log in with your other account.

You may find that this option also requires clearing your cache or cookies, just in case logging in as another user doesn't sufficiently flush the previous authentication tokens. But this is usually unnecessary.

As a desperate move, you could also try disabling browser extensions that might be interfering with your use of the site. However, this is unlikely, since a 403 implies you are authenticated, but not authorized. 

### Notify the site owner that a 403 is being returned when you'd expect otherwise

If you fully expect that you should be able to access the resource in question, but you are still seeing this error, it is wise to let the team behind the site know - this could be an error on their part.

Once more from [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.3):

> However, a request might be forbidden for reasons unrelated to the credentials.

A common cause for this happening unintentionally can be that a server uses allow- or deny-lists for particular IP addresses or geographical regions.

They might have a good reason for blocking your access outside of their strictly defined parameters, but it could also just be an oversight.

### Give up.

Maybe you just aren't supposed to be able to access that resource. It happens. It's a big internet and it's reasonable to expect that there are some areas off limits to you personally.

You could visit [http.cat](https://http.cat) instead while ruminating on why your original request was [forbidden](https://http.cat/403).

---

As a reader of freeCodeCamp News, you are almost certainly not forbidden from following [@JacksonBates](https://twitter.com/jacksonbates) on Twitter for more tech and programming related content.

