---
title: How to manage file uploads in GraphQL mutations using Apollo/Graphene
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-13T12:00:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-file-uploads-in-graphql-mutations-using-apollo-graphene-b48ed6a6498c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xCKDdyMn2NKAiufB7jtTwg.png
tags:
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Lucas McGartland

  GraphQL is an amazing way to query and manipulate data. You describe your data,
  ask for what you want, and get predictable results. The problem is, GraphQL only
  handles serializable data out of the box—there’s no way to upload fil...'
---

By Lucas McGartland

GraphQL is an amazing way to query and manipulate data. You describe your data, ask for what you want, and get predictable results. The problem is, GraphQL only handles serializable data out of the box—there’s no way to upload files directly as part of your mutations.

But what if there were a way to combine the power of GraphQL with the ease of uploading files in a multi-part request? @jaydenseric has come up with a solution: [**graphql-multipart-request-spec**](https://github.com/jaydenseric/graphql-multipart-request-spec)

> If you just want the code to make this work, jump to the end of this article to find JavaScript and Python implementations of the spec for Apollo and Graphene.

### Handling File Uploads With GraphQL without Multipart Uploads (The Old Way)

Vanilla GraphQL doesn’t support throwing raw files into your mutations. The data you can request and manipulate is limited to what you can serialize over the network. In practice, this looks like basic types: **numbers, booleans, and strings**. These work great—you can build almost everything you need with basic data types.

But what if you need to run a mutation that takes a file as an argument? For example: uploading a new profile picture. Here’s how you could deal with the problem with ordinary GraphQL:

#### Option 1: Base64 Encoding

Base64 encode the image and send it over the wire as a string in your mutation. This has several disadvatanges:

1. A base64 encoded file will be approximately 33% larger than the original binary.
2. It’s more expensive operationally to encode and decode the file.
3. Complex to remember to encode and decode properly.

#### Option 2: Seperate Upload Requests

Run a seperate server (or API) for uploading files. Upload the file in the first request, and then pass the resulting storage URL as part of your mutation (the second request).

However if you have to upload several files, you would have to wait until all the uploads are done before you could pass the URLs (to identify them) in your mutation, forcing a synchronous and slow process. It also adds another layer of complexity to make it handle all these requests separately in your client.

1. It’s not asynchronous.
2. It’s complex to manage the other upload server.

> Wouldn’t it be cool to just pass a file in as part of the mutation parameters?

### Enter the Multipart Request Spec (The New Way)

This is where the multipart request spec comes in. This GraphQL extension specification allows you to nest files anywhere within GraphQL mutations like this:

```
{  query: `    mutation($file: Upload!) {      uploadFile(file: $file) {        id      }    }  `,  variables: {    file: File // somefile.jpg  }}
```

As you can see, adding in a file is as simple as adding in any other type of mutation parameter. To implement this spec, you have to install two parts: one that runs on the client, and another that runs on the server. Here’s what they do:

* The client spec defines how to map any file objects in a mutation into a key that locates where they are in a multipart request.
* The server spec defines how to parse that map, and make the files re-accessible based on the key provided in the map.

So in apollo-client, you can run a mutation that looks like this:

```
this.props.mutate({variables: {file: yourFile}})
```

### Multipart Request Spec Implementations

If you’re looking to implement the multipart request spec with Apollo, you can easily integrate it with these packages written by Jayden Seric. These are for the JavaScript and Apollo ecosystem.

[**jaydenseric/apollo-upload-client**](https://github.com/jaydenseric/apollo-upload-client)  
[_apollo-upload-client - Enhances Apollo Client for intuitive file uploads via GraphQL mutations._github.com](https://github.com/jaydenseric/apollo-upload-client)[**jaydenseric/apollo-upload-server**](https://github.com/jaydenseric/apollo-upload-server)  
[_apollo-upload-server - Enhances Apollo GraphQL Server for intuitive file uploads via GraphQL mutations._github.com](https://github.com/jaydenseric/apollo-upload-server)

If you run your GraphQL API through Graphene and Django, you can implement the spec in Python by replacing your GraphQL view with this package I wrote here:

[**lmcgartland/graphene-file-upload**](https://github.com/lmcgartland/graphene-file-upload)  
[_graphene-file-upload - Enhances Graphene Django GraphQL Server for intuitive file uploads via GraphQL mutations._github.com](https://github.com/lmcgartland/graphene-file-upload)

### Conclusion

This spec is an easy way to add file upload capability to your GraphQL application. Focus less on how to get your files, and more on what you get to do with them!

If you want to talk more, chat about GraphQL or great typefaces, **hit me up on twitter @[lucasmcgartland](https://twitter.com/lucasmcgartland).** Or find me elsewhere on the web below:

> [Website](http://www.lucasmcgartland.com) | [Email](mailto:luke@thebeeinc.com) | [LinkedIn](https://www.linkedin.com/in/lucasmcgartland/) | [Twitter](https://twitter.com/lucasmcgartland) | [Dribbble](https://dribbble.com/lucasmcgartland)

#### Further Reading:

* [https://medium.com/@danielbuechele/file-uploads-with-graphql-and-apollo-5502bbf3941e](https://medium.com/@danielbuechele/file-uploads-with-graphql-and-apollo-5502bbf3941e)

