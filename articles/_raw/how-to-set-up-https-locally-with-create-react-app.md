---
title: How to Setup HTTPS Locally with create-react-app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-21T16:12:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-https-locally-with-create-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/react-https.png
tags:
- name: create-react-app
  slug: create-react-app
- name: how-to
  slug: how-to
- name: http
  slug: http
- name: https
  slug: https
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: "By Braedon Gough\nRunning HTTPS in development is helpful when you need\
  \ to consume an API that is also serving requests via HTTPS. \nIn this article,\
  \ we will be setting up HTTPS in development for our create-react-app with our own\
  \ SSL certificate. \nThi..."
---

By Braedon Gough

Running HTTPS in development is helpful when you need to consume an API that is also serving requests via HTTPS. 

In this article, we will be setting up HTTPS in development for our create-react-app with our own SSL certificate. 

This guide is for macOS users and requires that you have `[brew](https://brew.sh/)` installed. 

## Adding HTTPS

In your `package.json`, update the **start** script to include https: 

```json
"scripts": {
    "start": "HTTPS=true react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
```

Running `yarn start` after this step will show you this screen in your browser:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/privacy-error.png)

At this stage, you're already set to go with `https`. But you don't have a valid certificate, so your connection is assumed to be insecure. 

## Creating a SSL Certificate

The easiest way to obtain a certificate is via `[mkcert](https://github.com/FiloSottile/mkcert)`.

```bash
# Install mkcert tool
brew install mkcert

# Install nss (only needed if you use Firefox)
brew install nss

# Setup mkcert on your machine (creates a CA)
mkcert -install
```

After running the above commands, you'll have created a **[certificate authority](https://en.wikipedia.org/wiki/Certificate_authority)** on your machine which enables you to generate certificates for all of your future projects. 

From the root of your `create-react-app` project, you should now run:

```bash
# Create .cert directory if it doesn't exist
mkdir -p .cert

# Generate the certificate (ran from the root of this project)
mkcert -key-file ./.cert/key.pem -cert-file ./.cert/cert.pem "localhost"
```

We'll be storing our generated certificates in the `.cert` directory. These should not be committed to version control, so you should update your `.gitignore` to include the `.cert` directory. 

Next, we need to update the `start` script again to include our newly created certificate:

```json
  "scripts": {
    "start": "HTTPS=true SSL_CRT_FILE=./.cert/cert.pem SSL_KEY_FILE=./.cert/key.pem react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
```

When you run `yarn start` again, you should now see that your connection is secure. 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/secure.png)

Don't be a stranger! Feel free to write if you have any questions - [connect with me on Linkedin](https://www.linkedin.com/in/braedon-gough-ba92a048/) or [follow me on Twitter](https://twitter.com/bbbraedddon).

