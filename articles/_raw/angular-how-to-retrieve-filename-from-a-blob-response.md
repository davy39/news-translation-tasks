---
title: Angular - How to Retrieve Filename From a Blob Response
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:16:00.000Z'
originalURL: https://freecodecamp.org/news/angular-how-to-retrieve-filename-from-a-blob-response
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa3740569d1a4ca26cc.jpg
tags:
- name: Angular
  slug: angular
- name: how-to
  slug: how-to
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "If you're new to Angular, you might be wondering how to retrieve a filename\
  \ from an API response.\nImagine you have a method that makes a POST request to\
  \ a remote API and receives a Blob containing a file:\npublic downloadExcel(data):\
  \ void {\n  const ur..."
---

If you're new to Angular, you might be wondering how to retrieve a filename from an API response.

Imagine you have a method that makes a POST request to a remote API and receives a `Blob` containing a file:

```ts
public downloadExcel(data): void {
  const url: string = '[api endpoint here ]';
  this.http.post(url, data.body, { responseType: 'blob' })
    .subscribe((response: Blob) => saveAs(response, data.fileName + '.xlsx'));
}
```

According to MDN, `Blob` objects only contain a size and type, so you'll need another way to get the actual filename.

But since `data` is passed as a parameter to your function, it's possible that it also includes the payload from the server. Log it to the console and see what information is included.

## Reading the response headers

Another possible option is to read the HTTP response headers themselves. 

Since you're fetching data from an API, it's likely that you're using `httpClient` to make the request. Often API responses include helpful information in the header.

One thing to look at is the `X-Token` entry. But keep in mind that not all headers can be accessed from the client side, so `access-control-expose-headers` will need to be set from the server side.

If `X-Token` is exposed, you can use the HTTP method `{ observe: 'response' }` to get the full response, then log `X-Token` to the console:

```ts
http
  .get<any>('url', { observe: 'response' })
  .subscribe(resp => {
    console.log(resp.headers.get('X-Token'));
  });
```

It's also worth reading up on [response headers](https://developer.mozilla.org/en-US/docs/Web/API/Response/headers) in general.

