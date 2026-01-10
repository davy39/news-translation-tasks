---
title: Why you should (almost) never use an absolute path to your APIs again
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-25T00:15:36.000Z'
originalURL: https://freecodecamp.org/news/never-use-an-absolute-path-for-your-apis-again-9ee9199563be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jimGwpz6a99t5R_GfP15lA.jpeg
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Vitaly Kondratiev

  Recent advances in web apps architecture show that a decoupled front-end provides
  more flexibility for development and operations. It


  lets you work on one end without depending on the other

  lets you build and deploy separately

  m...'
---

By Vitaly Kondratiev

Recent advances in web apps architecture show that a decoupled front-end provides more flexibility for development and operations. It

* lets you work on one end without depending on the other
* lets you build and deploy separately
* makes it easy to use different tools on each end

![Image](https://cdn-media-1.freecodecamp.org/images/Jqz03zZXEEbqT9zIoeVOdB6INAhaNScHYDpb)
_Decoupled front-end architecture_

### The problem

When an app is developed with this architecture in mind, the front-end needs to communicate to the back-end via APIs, generally [REST](https://developer.mozilla.org/en-US/docs/Glossary/REST). Often, the URL/port of the back-end server differs from the front-end’s one, given separate deployment paths. In this example, the URL to the front-end app is `https://www.appfocused.com` and the REST endpoint to send contact emails is served from `[https://api.appfocused.com](https://api.appfocused.com.)`[.](https://api.appfocused.com.)

An HTTP request from the front-end app to the back-end server will fail as it violates the [Same Origin Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy). In Chrome’s console it will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/d9KvUeWl2nx51a4qv75ehlWIjx8VpoEqv3QE)
_CORS error_

Browsers, for security reasons, restrict requests which are not from the same origin. This prevents attackers from injecting code into our app and stealing our sensitive information. Browsers append an `[origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin)` header on cross-origin requests to let the server know of a potential threat. The server then has the authority to either allow or reject these origins by providing specific response headers, which are parsed by the browsers.

There are two solutions to fix this small problem:

* hardcode absolute API URLs on the client and configure CORS headers on the server
* use relative API URLs on the client and use a reverse-proxy approach

In this post, I talk about why the former approach with CORS headers should be considered an anti-pattern for production-ready code. I also talk about how to configure the reverse-proxy approach on various setups:

* local devserver
* web server / app server
* serverless (CloudFront / S3 / Lambda)

### Rationale

The CORS headers scenario sounds like less pain to implement, and it is. However, there are a few concerns to consider that made me preach for the **reverse proxy approach** under almost any circumstances.

First and foremost, the back-end might not be owned by you and it might be impossible to make the change to the CORS headers.

If you are lucky enough to control the back-end **and** can configure CORS headers, you will need to maintain a whitelist of multiple web clients accessing the API server in order to give them access. Of course, wildcard is also an option, but it would be unreasonable to whitelist all the origins by setting `access-control-allow-origin` to `*` unless it is a public server.

Another common pattern, during development, is to run our UI application at `localhost:$port`. But whitelisting localhost to facilitate API calls is an anti-pattern and should be avoided for security reasons.

Last, but not least, I like my build to conform to the **Build Once, Deploy Many** principle. It is one of the fundamental principles of **continuous delivery**. The binary — in our case, static files for the web client — is built only once. Subsequent deployments, testing, and releases should never attempt to build the binary artifacts again. Instead, the already built binary should be reused.

In practice, hardcoded absolute URLs like `https://api.appfocused.com/email/send` in our client code will stop us from having a single artifact, because on development environment I want my web client to hit, say, `https://api-dev.appfocused.com/email/send`.

> **_Never hardcode an absolute API URL in your client code._**

This became a powerful mantra for me and helped me to overcome some challenges on the way.

### Solution

The relative URL `/email/send` can solve it once and for all on the client, making Build Once, Deploy Many possible. It is the proxy’s work to orchestrate the request further. It also deals with the restrictions imposed by the browser. The proxy server, in this case, handles our requests, responses, and makes the modifications necessary to facilitate cross-origin communication.

#### Reverse proxy with webpack-dev-server

When you are developing on your local machine, you want the same treatment for your API as on other environments. Webpack can be configured to proxy requests. An example “webpack.config.js” is:

```js
module.exports = {
  //...
  devServer: {
    proxy: {
      '/api': 'http://localhost:9000'
    }
  }
};
```

A request from the client to the relative path `/api/users` will now proxy the request to `http://localhost:9000/api/users`. Please check the W[ebpack documentation](https://webpack.js.org/configuration/dev-server/#devserver-proxy) if you want to configure URL rewrite scenarios or add secure protocol.

The proxy can also be configured for projects built on Webpack like [create-react-app](https://facebook.github.io/create-react-app/docs/proxying-api-requests-in-development#docsNav) or [Gatsby](https://www.gatsbyjs.org/docs/api-proxy/).

#### Reverse proxy with NGINX

[NGINX](https://www.nginx.com/) is a common component in production environment architecture. It has a number of advanced load balancing, security, and acceleration features that most specialized applications lack. Using NGINX as a reverse proxy enables you to add these features to any application.

The simplest reverse proxy config on NGINX will look like this, in “/etc/nginx/conf.d/app.conf”

```
server {
  listen 80;
  listen [::]:80;
  
  server_name appfocused.com;
  
  location /api {
      proxy_pass http://api.appfocused.com/;
  }
}
```

The `proxy_pass` directive makes this configuration a reverse proxy. It specifies that all requests which match the location block — in this case, `/api` path — should be forwarded to `http://api.appfocused.com`, where our back-end is running.

Check the [full docs](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) for some more elaborate scenarios.

#### Reverse proxy with serverless

We will look at the AWS platform for a serverless scenario. In one of my previous posts I explained how we use [serverless architecture to host our website](https://www.appfocused.com/blog/static-site-with-aws-cloud-front-gatsby/). AWS CloudFront is playing one of the key roles in it, acting as CDN and providing security at the edge for our static files stored on S3.

The first API that we had to integrate into this setup was a contact form. The brief for implementation was the following:

> _When a client posts to `https://www.appfocused.com/api/send/email`, the request needs to be routed to `https://api.appfocused.com/api/send/email` where our back-end API is deployed in the form of Lambda function._

It turns out that CloudFront supports multiple origin servers. It uses path patterns to determine which origin server to forward requests to. Multiple independent servers, even systems that aren’t inside AWS, can all “own” one or more paths under a single hostname. One of them is the default and owning all the paths not explicitly configured.

The concept is very similar to reverse proxies in NGINX or Apache. But the request routing is done by CloudFront, which connects to the appropriate back-end, sends the request, and returns — and possibly caches — the response. It does not redirect the request, so the URL address never changes for the consumer.

### CloudFront configuration example

Use the main site’s hostname, for example `www.appfocused.com`, as the origin. Configure the site’s domain name as an alternate domain name in CloudFront.

Next, add a second origin, with the destination being the hostname where the WP deployment can be reached. Create a behavior with a [path pattern](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesPathPattern) that matches `/blog*` and uses the second origin.

Our existing CloudFront distribution was set up to point to our static S3 bucket content generated by the great Gatsby. Remember **not** to use autosuggestion from AWS when creating a new distribution with integration to S3. Manually enter [website endpoints](https://github.com/awsdocs/amazon-s3-developer-guide/blob/master/doc_source/WebsiteEndpoints.md) similar to this format `[http://appfocused.s3-website.eu-west-1.amazonaws.com](http://appfocused.s3-website.eu-west-1.amazonaws.com).)`[.](http://appfocused.s3-website.eu-west-1.amazonaws.com).)

Next, we’ll add our second origin to serve REST requests from API Gateway. From the “Origins” tab select “Create Origin”. Enter the domain name and leave origin path empty. Make sure to select “HTTPS only” for “Origin Protocol Policy”.

![Image](https://cdn-media-1.freecodecamp.org/images/d1-jb6x0NPwljlX7bTp1j9NxfPccQKwzpzF4)
_Cloudfront: create origin_

Next go to the “Behaviors” tab and click “Create Behavior” to configure the path.

![Image](https://cdn-media-1.freecodecamp.org/images/oqM3FKso86smQBaaetMgSAtHGgup0uyMcSVI)
_Cloudfront: create behavior_

For “Path Pattern” we’ll use `api/*` . This will catch any request starting with `/api` such as `[https://www.appfocused.com/api/send/email](https://www.appfocused.com/api/send/email)`.

In the “Origin” dropdown select the Origin we just created. This will ensure that the request will be routed to `[https://api.appfocused.com/api/send/email](https://api.appfocused.com/api/send/email)`.

For “Viewer Protocol Policy” select “HTTPS only”.

For “Allowed HTTP methods” select “GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE”.

For “Cache Based on Selected Request Headers” select “Whitelist” and add required headers. This prevents the Host Header being passed through to the origin.

For “Object Caching” select “Use Origin Cache Headers”.

For “Forward Cookies” select “All”.

For “Compress Objects Automatically” select “Yes”. This will gzip responses.

CloudFront forwards very few headers to the origin by default. You can configure it to forward what you need, but every header you forward will **reduce** your cache hit ratio. Personally I’m passing through “Referer”, “Accept”, “Content-Type”, and “Authorization”.

There are some caveats, though, to the serverless proxy on AWS. CloudFront won’t strip paths.

If a request is sent to `https://www.appfocused.com/api/*` it will be routed to `[https://api.appfocused.com](https://api.appfocused.comwith)`[with](https://api.appfocused.comwith) the `/api` prefix, not to the root of the site.

This can become an issue if you don’t own back-end APIs or, for some reasons, these cannot be changed. If that’s the case, [Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) comes to the rescue. This service allows you to rewrite paths on the fly, as requests are processed. To configure Lambda@Edge go to CloudFront Behavior item and choose “Lambda Function Associations”.

### Conclusion

By implementing reverse proxy across environments we achieve:

* **Secure client-server communication**  
the identity of your back-end servers remains unknown. This is useful in case of DDoS attacks
* **Build Once, Deploy Many**  
with relative paths to APIs you can build once, and deploy the same artifact to multiple environments
* **Same Origin**  
a CORS headers configuration on the server is not required

My personal advice is: never hardcode absolute paths to your APIs again, unless it is a prototype. Spend a bit more time to configure a reverse proxy layer to make it right.

_This post was originally published on my company’s blog. Our mission at Appfocused is to help companies execute [great user experiences on the web](https://www.appfocused.com) by utilising our vast experience, knowledge of the modern UI trends, best practices, and code craftsmanship._

