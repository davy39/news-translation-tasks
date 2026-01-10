---
title: What is HTTP? Protocol Overview for Beginners
subtitle: ''
author: Rufai Mustapha
co_authors: []
series: null
date: '2023-04-06T16:53:26.000Z'
originalURL: https://freecodecamp.org/news/what-is-http
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/http--5-.jpg
tags:
- name: http
  slug: http
- name: web
  slug: web
seo_title: null
seo_desc: "Without HTTP (Hypertext Transfer Protocol), the World Wide Web as we know\
  \ it today would not exist. HTTP is the protocol that enables the transfer of data\
  \ over the internet, allowing users to access websites and other online resources.\
  \  \nThere are va..."
---

Without HTTP (Hypertext Transfer Protocol), the World Wide Web as we know it today would not exist. HTTP is the protocol that enables the transfer of data over the internet, allowing users to access websites and other online resources.  
  
There are various ways to design web applications, including GraphQL, SOAP, Falcor, gRPC, WebSockets, and Serverless Functions, with REST being the most popular (according to the [2021 State-of-API](https://www.postman.com/state-of-api/2021/) survey by Postman). And at the heart of all these architectures is HTTP.

## What to Learn Along with HTTP

To understand HTTP, it is helpful to have a basic understanding of the following concepts:

1. Networking: Knowledge of how computers communicate with each other over networks is essential for understanding HTTP. This includes concepts such as IP addresses, DNS, and routing.
2. Web architecture: HTTP is a key part of web architecture, so understanding how web applications and websites are built can help you understand HTTP better. This includes concepts such as HTML, CSS, and JavaScript.
3. Server-side programming: HTTP is used to communicate between web browsers and servers, so understanding how servers work and how to build server-side applications can help you understand how HTTP works.
4. Client-side programming: HTTP is also used to communicate between web browsers and client-side applications, so understanding how to build client-side applications using JavaScript can also be helpful.

### What to Expect in This Article

* How the HTTP protocol works.
* How to make network requests with Chrome and Postman.
* How to upload data with the HTTP POST method in Postman.

By the end of the article, readers should have a basic understanding of HTTP, as well as the tools and resources available for testing and troubleshooting applications.

## Table of Contents

* [Introduction to HTTP](#heading-introduction-to-http)
* [What is the HTTP Request-Response Cycle?](#heading-what-is-the-http-request-response-cycle)
* [How to Create HTTP Requests](#heading-how-to-create-http-requests)
* [What is an HTTP Request URL?](#heading-what-is-an-http-request-url)
* [What Are HTTP Request Methods?](#heading-what-are-http-request-methods)
* [What Are HTTP Request Headers?](#heading-what-are-http-request-headers)
* [What is an HTTP Request Body?](#heading-what-is-an-http-request-body)
* [What is an HTTP Response?](#heading-what-is-an-http-response)

## Introduction to HTTP

HTTP (Hypertext Transfer Protocol) is a protocol used for exchanging information over the internet. HTTP is like the delivery system for information on the internet. It makes sure information goes from one place to another, like how ships carry goods across the ocean. It's the foundation of the World Wide Web.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/http-client-server.jpg)

HTTP is what makes the internet work. It's a way for web browsers and servers to talk to each other and send things like web pages back and forth. It's important for people who build websites and web applications to know how it works.  
  
Without HTTP, it would be difficult to imagine how the internet would work. There would be no web pages, no URLs, and no hyperlinks. Instead, users would need to know the exact IP address of the server hosting the information they want to access, and they would need to use a low-level protocol like TCP/IP to transfer data.

## What is the HTTP Request-Response Cycle?

Communication in HTTP centers around a concept called the Request-Response Cycle. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/http-client-server-RR.jpg)

  
The request-response cycle is the process by which a client (such as a web browser or a mobile app) communicates with a server to retrieve resources or perform actions. The cycle involves several steps:

1. The client initiates a request to the server by sending an HTTP request message, which contains information such as the requested resource and any additional parameters.
2. The server receives the request message and processes it, using its resources to generate a response message.
3. The server sends the response message back to the client, which typically contains the requested resource (such as a web page) and any additional information or metadata.
4. The client receives the response message and processes it, usually by rendering the content in a web browser or displaying it in an app.
5. The client may initiate additional requests to the server, repeating the cycle as needed.

## How to Create HTTP Requests

To create a valid HTTP request, you need the following:

* A URL.
* The HTTP method.
* A list of headers (request headers).
* The request body.

Here's an example of an HTTP request header, with three lines:

```http
GET /watch?v=8PoQpnlBXD0 HTTP/1.1
Host: www.youtube.com
Cookie: GPS=1; VISITOR_INFO1_LIVE=kOe2UTUyPmw; YSC=Jt6s9YVWMd4
```

1. The first line specifies the HTTP method, path, and protocol version. In this case, it is a `GET` request for the video located at the path `/watch?v=8PoQpnlBXD0` using the HTTP/1.1 protocol.
2. The second line specifies the host of the website, which is [`www.youtube.com`](http://www.youtube.com/).
3. The third line contains a cookie header, which is used for sending and storing small pieces of data on the client side. In this case, the cookie header contains three values: `GPS=1, VISITOR_INFO1_LIVE=kOe2UTUyPmw`, and `YSC=Jt6s9YVWMd4`. These values can be used by YouTube to track and personalize the user's experience.

## What is an HTTP Request URL?

![Image](https://www.freecodecamp.org/news/content/images/2023/04/url.jpg)

When a web browser attempts to access an image on the internet, it sends a request to the server using a URL. This URL is _unique_ and points to a specific _resource_ on the server.  

A resource can be anything that has a name and can be accessed with a unique identifier like a user, product, article, document, or image. You can think of resources as _nouns_.

## What Are HTTP Request Methods?

The request method tells the server what kind of action the client wants the server to take. The most common methods are:

<table>
<thead>
<tr>
<th>HTTP Methods</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>HEAD</td>
<td>Asks the server for status (size, availability)  of a resource.</td>
</tr>
<tr>
<td>GET</td>
<td>Asks the server to retrieve a resource.</td>
</tr>
<tr>
<td>POST</td>
<td>Asks the server to create a new resource.</td>
</tr>
<tr>
<td>PUT</td>
<td>Asks the server to edit/update an existing resource.</td>
</tr>
<tr>
<td>DELETE</td>
<td>Asks the server to delete a resource.</td>
</tr>
</tbody>
</table>

## What Are HTTP Request Headers?

HTTP request headers are additional pieces of information that are sent by the client as part of an HTTP request. They have a name/value format. That is:

```txt
Name: Value
```

These headers provide context and additional instructions to the server, which can be used to process the request or customize the response.

%[https://youtu.be/hqQR1O2H_ck]

Here's an example of an HTTP request header:

```http
GET /api/data HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36
Accept: application/json
Accept-Language: en-US,en;q=0.5
Authorization: Token abc123
Cache-Control: no-cache
Connection: keep-alive
Referer: https://www.google.com/
Pragma: no-cache
```

In this example, the `GET` method is used to send a request to the `/api/data` endpoint on the `example.com` server using HTTP/1.1 protocol. The request includes ten headers:

| Headers | Definition |
| ------- | ---------- |
| Host | This header specifies the hostname of the server that the client is trying to connect to. |
| User-Agent | This header provides information about the client that is making the request (in this case, a version of the Chrome browser). |
| Accept | This header specifies the MIME types of data that the client is willing to accept in the response. |
| Accept-Language | This header specifies the preferred language(s) for the response. |
| Authorization | This header provides an access token (in this case, Token abc123) for authentication purposes. |
| Cache-Control | This header specifies caching directives for both requests and responses. |
| Connection | This header specifies options for the connection handling between client and server. |
| Referer | This header specifies the URL of the page that linked to the current page. |
| Pragma | This header specifies implementation-specific directives that might apply to any agent along the request-response chain. |
| Content-Type | This header specifies the MIME type of the data that is being sent in the body of the request, but it is not used in this example because this is a GET request without a request body. |

%[https://youtu.be/Pjok-1Q6MOs]

## What is an HTTP Request Body?

In HTTP, the request body is the data that is sent from the client to the server as part of an HTTP request. The example below shows how to upload an image to the [Cat API Server](https://documenter.getpostman.com/view/5578104/RWgqUxxh#5a07d324-155b-487e-80a5-b1b9c1775339):

%[https://youtu.be/zAVCD0nLnjg]

And here's what the request looks like:

```http
POST /v1/images/upload HTTP/1.1
Host: api.thecatapi.com
x-api-key: API_KEY
Content-Length: 232
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="/C:/Users/USER/Downloads/cat1.jpg"
Content-Type: image/jpeg

(data)
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

The request includes these headers:

1. `Host`: This header specifies the hostname of the server that the client is trying to connect to.
2. `Content-Type`: The request is uploading an image file named `cat1.jpg` using a type of data called `multipart/form-data`. The image is in JPEG format and its content is included in the request body.
3. `x-api-key`: This header provides an API key for authentication purposes.
4. `Content-Length`: This header specifies the length of the request body in bytes. The value of this field is 232.

When the server receives this request, it will parse the request body and use it to create a new entry in the Cat API database. The server will then return a response that includes information about the new entry, such as the image URL and the database ID.

## What is an HTTP Response?

An HTTP response is the message that a server sends back to a client in response to an HTTP request. It usually consists of a status line, headers, and a message body:

```http
HTTP/1.1 200 OK
Date: Sun, 28 Mar 2023 10:15:00 GMT
Content-Type: application/json
Server: Apache/2.4.39 (Unix) OpenSSL/1.1.1c PHP/7.3.6
Content-Length: 1024

{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    }
}
```

The status line contains the HTTP version, a status code indicating the outcome of the request, and a corresponding message.

The headers provide additional information about the response, such as the content type of the message body or the date and time that the response was sent.

The message body contains the actual response data, such as HTML, JSON, or XML content.

Some common HTTP status codes include:


| Code | Meaning |
| ------ | ----------- |
| 100 | Continue |
| 101 | Switching Protocols |
| 200 | OK |
| 201 | Created |
| 202 | Accepted |
| 203 | Non-Authoritative Information |
| 404  | Not Found : The requested resource was not found on the server. |
| 500 | Internal Server Error : The server encountered an error while processing the request. |
| 301  | Moved Permanently: The requested resource has been permanently moved to a new URL. |

Here's an example of a JSON response from the Cat API:

```json
{
    "id": "ErDd1JRRT",
    "url": "https://cdn2.thecatapi.com/images/ErDd1JRRT.jpg",
    "width": 4282,
    "height": 6424,
    "original_filename": "cat1.jpg",
    "pending": 0,
    "approved": 1
}
```

This is a JSON response from a Cat API request that appears to provide metadata about an image that has been uploaded or retrieved from the API. Here's what each field means:

* `id`: A unique identifier for the image.
* `url`: The URL where the image can be accessed.
* `width`: The width of the image in pixels.
* `height`: The height of the image in pixels.
* `original_filename`: The original name of the file that was uploaded.
* `pending`: A flag indicating whether the image is still being processed by the API.
* `approved`: A flag indicating whether the image has been approved for public use by the API.

## Conclusion

HTTP (Hypertext Transfer Protocol) is a protocol used for exchanging information over the internet. It forms the foundation of the World Wide Web and allows communication between web browsers and servers.   
  
This article is a short introduction to HTTP. If you are interested in learning more, check out these textbook recommendations:

* "HTTP: The Definitive Guide" by David Gourley and Brian Totty - This book is widely regarded as the authoritative guide to HTTP. It covers the protocol in-depth and provides detailed information on its features and implementation.
* "HTTP Pocket Reference" by Clinton Wong - This book provides a concise and portable reference to the HTTP protocol. It covers the essentials of the protocol and is a great resource for developers who need quick access to HTTP information.
* "Web Performance Daybook Volume 2: Techniques and Tips for Optimizing Web Site Performance" edited by Stoyan Stefanov - This book is a collection of essays and articles on web performance, including a section on HTTP optimization. It provides practical advice on how to optimize HTTP for faster and more efficient web performance.


