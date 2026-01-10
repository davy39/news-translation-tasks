---
title: How to Create a REST API Without a Server
subtitle: ''
author: Jakub T. Jankiewicz
co_authors: []
series: null
date: '2024-05-20T10:13:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-rest-api-without-a-server
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/cover-5.png
tags:
- name: React
  slug: react
- name: REST API
  slug: rest-api
seo_title: null
seo_desc: 'If you''re a Front-End developer and want to showcase your skills, it may
  be a problem if you use GitHub pages or Netlify to show your apps.

  Instead, you can create a REST API directly in the browser without the need of any
  server. With this, you can ...'
---

If you're a Front-End developer and want to showcase your skills, it may be a problem if you use GitHub pages or Netlify to show your apps.

Instead, you can create a REST API directly in the browser without the need of any server. With this, you can showcase your skills in applications that interact with a backend hosted in places where you can't access the server side.

Note that if you search for "API without a server" you may find articles about [serverless](https://en.wikipedia.org/wiki/Serverless_computing) (which is still a kind of [server](https://www.freecodecamp.org/news/web-servers-explained-by-running-a-microbrewery-d40b9824f882/)). This article is completely different and showcases a relatively new browser API. Read on if you're interested.

## Table of contents

* [What is a Service Worker?](#what-is-service-worker)
    
* [How to register a Service Worker?](#heading-how-to-register-a-service-worker)
    
* [How to create a basic HTTP response](#heading-how-to-create-a-basic-http-response)
    
* [How to create a base project](#heading-how-to-create-a-base-project)
    
    * [Set up Vite](#heading-set-up-vite)
        
    * [Use the Wayne library](#heading-use-the-wayne-library)
        
    * [Install the Service Worker](#heading-install-the-service-worker)
        
    * [Test on the Web Server](#heading-test-on-the-web-server)
        
* [How to add React authentication](#heading-how-to-add-react-authentication)
    
    * [Create a JWT token](#heading-create-a-jwt-token)
        
    * [Add authentication API](#heading-add-authentication-api)
        
    * [Add authentication to React](#heading-add-authentication-to-react)
        
* [Next steps](#heading-next-steps)
    
* [Fully working demo](#heading-fully-working-demo)
    

## What is a Service Worker?

The browser API that allows you to create pure in the browser HTTP responses to HTTP requests is called a Service Worker. This API was mostly created to intercept HTTP requests originated from the browser and serve them from cache.

This allows you to create applications called [PWA](https://www.freecodecamp.org/news/what-are-progressive-web-apps-pwa-guide/) that work when you don't have internet connection. So you can use them while on the train, where you may have unstable internet. When you're offline, the HTTP requests can be stored and sent to the real server when you get back online.

But this is not all what Service Workers can do. With them, you can create HTTP requests that never existed. It can intercept any HTTP requests, for example when you open an image in new tab or using AJAX (like with [fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)).

## How to Register a Service Worker?

Service worker needs to be written in a separate file (often called `sw.js`, but you can name it whatever you want).

The location of that file is important. It should be located in the root of your app, often in the root of the [domain](https://en.wikipedia.org/wiki/Domain_name).

To register a service worker, you need to execute this code:

```javascript
if ('serviceWorker' in navigator) {
  var scope = location.pathname.replace(/\/[^\/]+$/, '/')
  navigator.serviceWorker.register('sw.js', { scope })
    .then(function(reg) {
       reg.addEventListener('updatefound', function() {
         var installingWorker = reg.installing;
         console.log('A new service worker is being installed:',
                     installingWorker);
       });
       // registration worked
       console.log('Registration succeeded. Scope is ' + reg.scope);
    }).catch(function(error) {
      // registration failed
      console.log('Registration failed with ' + error);
    });
}
```

This will install a service worker that can start to intercept HTTP requests.

**NOTE:** The service worker works only with HTTPS and localhost.

## How to Create a Basic HTTP Response

The API of the Service Worker is very simple – you have an event called `fetch`  
and you can respond to that event with any response:

```javascript
self.addEventListener('fetch', event => {
    const url = new URL(event.request.url);
    if (url.pathname === '/api/hello/') {
        const headers = {
            'Content-Type': 'text/plain'
        };
        const msg = 'Hello, Service Worker!'
        event.respondWith(textResponse(msg, headers));
   }
});

function textResponse(string, headers) {
    const blob = new Blob([string], {
        type: 'text/plain'
    });
    return new Response(blob, { headers });
}
```

With this you code, you can open the URL `/api/hello/` and it will display the text `"Hello, Service Worker!"` as a text file.

Also, one important thing: if you want to use the Service Worker immediately after it's installed, you need to add this code:

```javascript
self.addEventListener('activate', (event) => {
  event.waitUntil(clients.claim());
});
```

Normally, the Service Worker intercepts requests only after you refresh the page. This code forces to accept requests immediately after installation.

**NOTE:** With service worker, you can also intercept request that are sent to different domains. If you have your app on GitHub pages, you can intercept the requests to any domain. Because there are no checks of the domain, this code:

```javascript
await fetch('https://example.com/api/hello').then(res => res.text())
```

will also return `Hello, Service Worker!`.

## How to Create a Base Project

You will create something more useful by creating a React project with very simple user authentication.

Note that this is not secure in any way, because user information and passwords will be visible in the code. But it can show that you know how to interact with an API in React.

### Set Up Vite

First, you need to set up a simple React application with [Vite](https://vitejs.dev/).

To use Vite, you need to have Node.js installed. If you don't have it, you can read how to install it from [this article](https://www.freecodecamp.org/news/how-to-install-node-in-your-machines-macos-linux-windows/).

Then, you need to run this command from the terminal:

```bash
npm create vite@latest
```

I've picked name `auth`, React, and JavaScript. This is the output I've got:

```python
✔ Project name: … auth
✔ Select a framework: › React
✔ Select a variant: › JavaScript

Scaffolding project in /home/kuba/auth...

Done. Now run:

  cd auth
  npm install
  npm run dev
```

Next is to modify `vite.config.js` file, so Vite will know how to build the service worker file/

This is the config file Vite created:

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})
```

You need to modify the config file to include this code:

```javascript
import { join } from "node:path";
import { buildSync } from "esbuild";

export default defineConfig({
  plugins: [
    react(),
    {
      apply: "build",
      enforce: "post",
      transformIndexHtml() {
        buildSync({
          minify: true,
          bundle: true,
          entryPoints: [join(process.cwd(), "src", "sw.js")],
          outfile: join(process.cwd(), "dist", "sw.js"),
        });
      },
    },
  ]
})
```

You need to include both imports and you can replace the existing config with the one above. You can also add the code in the curly braces into a plugin array.

### Use the Wayne library

Then, you need to create a Service Worker file named `sw.js`. You will use [Wayne library](https://github.com/jcubic/wayne) instead of writing the routes yourself. This will simplify the code.

First, you need to install Wayne:

```bash
npm install @jcubic/wayne
```

Then, you can create a file named `sw.js` (**Note:** you've put the `"src"` directory in the `vite.config.js` file, so you should save the file in that directory).

```javascript
import { Wayne } from '@jcubic/wayne';

const app = new Wayne();

app.get('/api/hello/', (req, res) => {
   res.text('Hello, Service Worker!');
});
```

This code will work exactly the same as our previous example.

### Install the Service Worker

Now, the last thing you need to do to set up your service worker is to register it. You could use the code that you saw earlier, but now you will use a library for this.

First, you need to install it:

```bash
npm install register-service-worker
```

And update `src/main.jsx` with this code:

```jsx
import { register } from "register-service-worker";

register(`./sw.js`);
```

The last thing is to build the project by executing:

```bash
npm run build
```

**NOTE**: the `dev` mode will not work with the service worker – you need to build the project.

The instructions setting up a Service Worker with Vite were based on [this articl](https://dev.to/reeshee/how-to-bundle-your-custom-service-worker-in-vite-without-using-pwa-4nk)e.

### Test on the Web Server

To test your project you can use this command:

```bash
npx http-server -p 3000 ./dist/
```

This will create a simple HTTP server where you can test your application.

**NOTE**: if you open the`index.html` file in a browser (like with drag and drop), the service worker will not work. This is because the `file://` protocol has a lot of restrictions. That's why you need a web server.

If you test the app in the browser by opening the URL: `http://127.0.0.1:3000`, it will run the code that registers the service worker, and you will immediately be able to access our fake HTTP endpoint: `http://127.0.0.1:3000/api/hello/`. It should display the text:

```python
Hello, Service Worker!
```

**NOTE**: to simplify testing, you can add `"http-server -p 3000 ./dist/"` to the package.json file into `scripts`:

```json
"serve": "http-server -p 3000 ./dist/",
```

Remember that `package.json` is a JSON file, so you can't put a trailing comma if this will be the last script.

To make it work, you need to install the package:

```bash
npm install http-server
```

Now you can run the server with `npm run serve`.

**NOTE**: if you access the URL: `http://127.0.0.1:3000/api/hello` (you can read what is 127.0.0.1 in [this article](https://www.freecodecamp.org/news/what-is-localhost/)), you will get an error from `http-server`. This is because the route you created in the service worker used a trailing slash. To fix this, you can add a redirect:

```javascript
app.get('/api/hello', (req, res) => {
   res.redirect(301, req.url + '/');
});
```

## How to Add React Authentication

Now, after you have set up everything, you can add a real authentication endpoint and connect it with your React app.

### Create a JWT token

We will use a popular JWT token for authentication. You can read more about them in [this article](https://www.freecodecamp.org/news/how-to-sign-and-validate-json-web-tokens/).

First, you need to install a JWT library:

```bash
npm install jose
```

Then, you need to create a new file named `jwt.js` in the `src` directory:

```javascript
import { SignJWT, jwtVerify } from 'jose';

const secret = new TextEncoder().encode(
  'cc7e0d44fd473002f1c42167459001140ec6389b7353f8088f4d9a95f2f596f2'
);

const alg = 'HS256';

const jwt = {
    sign: (payload) => {
        return new SignJWT(payload)
            .setProtectedHeader({ alg })
            .setIssuedAt()
            .setIssuer('https://freecodecamp.org')
            .setAudience('https://freecodecamp.org')
            .setExpirationTime('2h')
            .sign(secret)
    },
    verify: async (token) => {
        const { payload } = await jwtVerify(token, secret, {
            issuer: 'https://freecodecamp.org',
            audience: 'https://freecodecamp.org',
        });
        return payload;
    }
};

export default jwt;
```

This code is an [ES Module](https://www.freecodecamp.org/news/javascript-modules-beginners-guide/) that uses the [`jose` JWT token library](https://github.com/panva/jose) to create a new token, `jwt.sign`. It verifies that the token is correct with `jwt.verify`, and it also returns the payload, so you can extract anything you save in the token.

You can read more about the `jose` library from the documentation – the links to the [docs are in the README](https://github.com/panva/jose).

**NOTE**: Because of the limitation of Service Worker, we can't create a proper real life authentication, where the access token is stored in a cookie (Service Worker don't allow creating cookies) and use refresh tokens to update the access token.

### Add authentication API

Now, you can use the previous functions to create an API endpoint:

```javascript
import jwt from './jwt';

app.post('/api/login', async (req, res) => {
    const { username, password } = await req.json() ?? {};
    if (username === 'demo' && password === 'demo') {
        const token = await jwt.sign({ username });
        res.json({ result: token });
    } else {
        res.json({ error: 'Invalid username or password' });
    }
});
```

This code will verify that the username and password are correct (both equal to `"demo"`), ⁣and create a new JWT token. If the username or password are not correct, it will return an error.

### Add authentication to React

You created a React App with Vite, so you need to use JSX to add front-end authentication logic.

First, you create a helper function that will send an HTTP request to the `/api/login` endpoint with [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch):

```javascript
function login(username, password) {
    return fetch('/api/login', {
        method: 'post',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username,
            password
        })
    }).then(res => res.json());
}
```

Next, you need to create a basic form:

```html
<form>
  <div>
    <label for="user">username</label>
    <input id="user" />
  </div>
  <div>
    <label for="password">password</label>
    <input id="password" type="password" />
  </div>
  <button>login</button>
</form>
```

And a add bit of styling:

```css
form {
  display: inline-flex;
  flex-direction: column;
  gap: 10px;
  align-items: flex-end;
}

label::after {
  content: ":";
}

label {
  width: 100px;
  display: inline-block;
  text-align: right;
  margin-right: 10px;
}
```

Next, you need an authentication function that you will add to an `onSubmit` event. ⁣  
You will use two state variables for token and error:

```javascript
function App() {
  const [token, setToken] = useState(null);
  const [error, setError] = useState(null);

  async function auth(event) {
    event.preventDefault();

    const res = await login(username, password);
    if (res.result) {
      setToken(res.result);
    } else if (res.error) {
      setError(res.error);
    }
  }
```

To get the username and password from the form you can use refs. You can also display the form only when the token is not set:

```jsx
function App() {
  const [token, setToken] = useState(null);
  const [error, setError] = useState(null);
  const userRef = useRef();
  const passwordRef = useRef();

  async function auth(event) {
    event.preventDefault();
    const username = userRef.current.value;
    const username = passwordRef.current.value;

    const res = await login(username, password);
    if (res.result) {
      setToken(res.result);
    } else if (res.error) {
      setError(res.error);
    }
  }

  return (
    <div>
      <div className="card">
        {!token && (
          <form onSubmit={auth}>
            <div>
              <label for="user">username</label>
              <input id="user" ref={userRef}/>
            </div>
            <div>
              <label for="password">password</label>
              <input id="password" ref={passwordRef} type="password"/>
            </div>
            <button>login</button>
          </form>
        )}
        {error && <p className="error">{ error }</p>}
      </div>
    </div>
  );
}
```

Now you can test the App. If you type the username and password, they don't reset.

You can fix it by setting the ref value to an empty string at the end of the function:

```javascript
userRef.current.value = '';
passwordRef.current.value = '';
```

There is another error. If you put a wrong username or password, you will get an error. But then, if you type the correct password, the error is not removed. To fix this issue, you need to reset the error state when setting the token:

```javascript
  async function auth(event) {
    event.preventDefault();
    const username = userRef.current.value;
    const username = passwordRef.current.value;

    const res = await login(username, password);
    if (res.result) {
      setToken(res.result);
      setError(null);
    } else if (res.error) {
      setError(res.error);
    }
    userRef.current.value = '';
    passwordRef.current.value = '';
  }
```

Next thing that you can do is to extract the username from the token. This will also verify that the token is correct in your React app. You need to use the `useEffect` hook to run the code when the token changes:

```javascript
import jwt from './jwt';

  // ...
  const [username, setUsername] = useState(null);

  useEffect(() => {
    jwt.verify(token).then(payload => {
      const { username } = payload;
      setUsername(username);
    }).catch(e => {
      setError(e.message);
    });
  }, [token]);

  // ...
```

If you run this code, you will get an error: `Compact JWS must be a string or Uint8Array`.

The reason is that the `useEffect` hook will be triggered when the token is `null`. Before you verify, you need to check if the token was set:

```javascript
  useEffect(() => {
    if (token !== null) {
      jwt.verify(token).then(payload => {
        const { username } = payload;
        setUsername(username);
      }).catch(e => {
        setError(e.message);
      });
    }
  }, [token]);
```

Next, you can display the username after user login:

```jsx
{token && (
  <div>
    <p>Welcome {username}</p>
  </div>
)}
```

## Next Steps

The last thing we can do is to save the token in `localStorage` and add a logout button. But this is left as an exercise to the reader.

You can read about `localStorage` from [this freeCodeCamp article](https://www.freecodecamp.org/news/use-local-storage-in-modern-applications/).

You can improve this and add more endpoints, like getting real data that you will save in a `sw.js` file. You can store the data in IndexedDB, so it will be persistent like in in a real app. Read more about IndexedDB from [this article](https://www.freecodecamp.org/news/how-indexeddb-works-for-beginners/).

IndexedDB doesn't have a very nice API, but there are libraries that add abstraction on top of it. My favorite is the SQL library [AlaSQL](https://alasql.org/), and [idb](https://github.com/jakearchibald/idb) by [Jake Archibald](https://jakearchibald.com/).

## Fully working demo

The full source code is available on GitHub in the repository [jcubic/react-wayne-auth](https://github.com/jcubic/react-wayne-auth). You can test a working demo on [GitHub pages](https://jcubic.github.io/react-wayne-auth/).

If you like this article, you may want to follow me on Social Media: ([Twitter/X](https://x.com/jcubic) and/or [LinkedIn](https://www.linkedin.com/in/jakubjankiewicz/)) and you an also check my [personal website](https://jakub.jankiewicz.org/).
