---
title: How to implement runtime environment variables with create-react-app, Docker,
  and Nginx
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-12T22:57:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-runtime-environment-variables-with-create-react-app-docker-and-nginx-7f9d42a91d70
coverImage: https://cdn-media-1.freecodecamp.org/images/0*auL6Qm-oQV0NC_pU.png
tags:
- name: Docker
  slug: docker
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Krunoslav Banovac

  There are many ways to configure your React application. Let’s use an approach which
  respects Twelve-Factor App methodology. This means it enforces reconfiguration during
  runtime. Therefore no build per environment would be requi...'
---

By Krunoslav Banovac

There are many ways to configure your React application. Let’s use an approach which respects [**Twelve-Factor App methodology.**](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology) This means it enforces reconfiguration during runtime. Therefore no build per environment would be required.

![Image](https://cdn-media-1.freecodecamp.org/images/0*auL6Qm-oQV0NC_pU.png)

### ? What do we want to achieve?

We want to be able to run our React application as a Docker container that is built once. It runs everywhere by being configurable **during runtime.** The output should be a lightweight and performant container which serves our React application as static content, which we achieve by using Ngnix Alpine. Our application should allow configuration within docker-compose file such as this:

```yml
version: "3.2"
services:
  my-react-app:
    image: my-react-app
    ports:
      - "3000:80"
    environment:
      - "API_URL=https://production.example.com"
```

_We should be able to configure our React application using `-e` flag (environment variables) when using `Docker run` command._

> _On first glance, this approach may seem to bring too small of a benefit for the extra work it requires for initial setup. But once setup is done, environment specific configurations and deployment will be way easier to handle. So for anyone targeting dynamic environments or using orchestration systems, this approach is definitely something to consider._

### ? The problem

First of all, it must be clear that there is no such thing as environment variables inside the browser environment. Whichever solution we use nowadays is nothing but a fake abstraction.

But, then you might ask, what about `.env` files and `REACT_APP` prefixed environment variables which come [straight from documentation](https://facebook.github.io/create-react-app/docs/adding-custom-environment-variables)? Even inside the source code, these are used as `process.env` just like we use environment variables inside Node.js.

In reality, the object `process` does not exist inside the browser environment, it’s Node-specific. CRA by default doesn’t do server-side rendering. It can’t inject environment variables during content serving (like [Next.js](https://github.com/zeit/next.js) does). **During transpiling**, Webpack process replaces all occurrences of `process.env` with a string value that was given. This means **it can only be configured during build time**.

#### ? Solution

The specific moment when it is still possible to inject environment variables happens when we start our container. Then we can read environment variables from inside the container. We can write them into a file which can be served via Nginx (which also serves our React app). They are imported into our application using `<script>` tag inside the head section of `index.html`. So at that moment, we run a bash script which creates JavaScript file with environment variables assigned as properties of the global `window` object. Injected to be globally available within our application the browser way.

![Image](https://cdn-media-1.freecodecamp.org/images/0*mqvCYhYLV_KN3VzY.png)
_You will find a link to the GitHub repository at the end of the article._

### ? Step by step guide

Let’s start with a simple `create-react-app` project and create `.env` file with our first environment variable that we want to expose.

```sh
# Generate React App
create-react-app cra-runtime-environment-variables
cd cra-runtime-environment-variables

# Create default environment variables that we want to use
touch .env
echo "API_URL=https//default.dev.api.com" >> .env
```

Then let’s write a small bash script which will read`.env` file and extract environment variables that will be written into the file. If you set an environment variable inside the container, its value will be used, otherwise, it will fall back to the default value from .env file. It will create a JavaScript file which puts environment variable values as an object which is assigned as a property of `window` object.

```sh
#!/bin/bash

# Recreate config file
rm -rf ./env-config.js
touch ./env-config.js

# Add assignment 
echo "window._env_ = {" >> ./env-config.js

# Read each line in .env file
# Each line represents key=value pairs
while read -r line || [[ -n "$line" ]];
do
  # Split env variables by character `=`
  if printf '%s\n' "$line" | grep -q -e '='; then
    varname=$(printf '%s\n' "$line" | sed -e 's/=.*//')
    varvalue=$(printf '%s\n' "$line" | sed -e 's/^[^=]*=//')
  fi

  # Read value of current variable if exists as Environment variable
  value=$(printf '%s\n' "${!varname}")
  # Otherwise use value from .env file
  [[ -z $value ]] && value=${varvalue}
  
  # Append configuration property to JS file
  echo "  $varname: \"$value\"," >> ./env-config.js
done < .env

echo "}" >> ./env-config.js
```

We need to add the following line to `<head>` element inside `index.html`which then imports the file created by our bash script.

```html
<script src="%PUBLIC_URL%/env-config.js"></script>
```

Let’s display our environment variable within the application:

```jsx
<p>API_URL: {window._env_.API_URL}</p>
```

#### ? Development

During development, if we don’t want to use Docker, we can run bash script via `npm script` runner by modifying `package.json`:

```json
  "scripts": {
    "dev": "chmod +x ./env.sh && ./env.sh && cp env-config.js ./public/ && react-scripts start",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "build": "react-scripts build'"
  },
```

And if we run `yarn dev` we should see output like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*e4ugnbph1YnN3uVbH2QNZA.png)
_Using default API_URL value from .env file_

There are two ways to reconfigure environment variables within dev. Either change the default value inside `.env` file or override defaults by running `yarn dev`command with environment variables prepended:

```sh
API_URL=https://my.new.dev.api.com yarn dev
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*MHnRJn_JkV33mmK6Yh1raw.png)
_Using API_URL value which was passed via CLI_

And finally, edit `.gitignore` so that we exclude environment configurations out of the source code:

```
# Temporary env files
/public/env-config.js
env-config.js
```

As for the development environment, that’s it! We are half-way there. We haven’t made a huge difference at this point compared to what CRA offered by default for the development environment. The true potential of this approach shines in production.

#### ? Production

Now we are going to create minimal Nginx configuration so that we can build an optimized image which serves the production-ready application.

```sh
# Create directory for Ngnix configuration
mkdir -p conf/conf.d
touch conf/conf.d/default.conf conf/conf.d/gzip.conf
```

The main configuration file should look somewhat like this:

```
server {
  listen 80;
  location / {
    root   /usr/share/nginx/html;
    index  index.html index.htm;
    try_files $uri $uri/ /index.html;
    expires -1; # Set it to different value depending on your standard requirements
  }
  error_page   500 502 503 504  /50x.html;
  location = /50x.html {
    root   /usr/share/nginx/html;
  }
}
```

It’s also useful to enable gzip compression so that our assets are more lightweight during network transition:

```
gzip on;
gzip_http_version  1.0;
gzip_comp_level    5; # 1-9
gzip_min_length    256;
gzip_proxied       any;
gzip_vary          on;

# MIME-types
gzip_types
  application/atom+xml
  application/javascript
  application/json
  application/rss+xml
  application/vnd.ms-fontobject
  application/x-font-ttf
  application/x-web-app-manifest+json
  application/xhtml+xml
  application/xml
  font/opentype
  image/svg+xml
  image/x-icon
  text/css
  text/plain
  text/x-component;
```

Now that our Nginx configuration is ready, we can finally create Dockerfile and docker-compose files:

```sh
touch Dockerfile docker-compose.yml
```

Initially, we use `node:alpine` image to create an optimized production build of our application. Then, we build a runtime image on top of `nginx:alpine` .

```dockerfile
# => Build container
FROM node:alpine as builder
WORKDIR /app
COPY package.json .
COPY yarn.lock .
RUN yarn
COPY . .
RUN yarn build

# => Run container
FROM nginx:1.15.2-alpine

# Nginx config
RUN rm -rf /etc/nginx/conf.d
COPY conf /etc/nginx

# Static build
COPY --from=builder /app/build /usr/share/nginx/html/

# Default port exposure
EXPOSE 80

# Copy .env file and shell script to container
WORKDIR /usr/share/nginx/html
COPY ./env.sh .
COPY .env .

# Add bash
RUN apk add --no-cache bash

# Make our shell script executable
RUN chmod +x env.sh

# Start Nginx server
CMD ["/bin/bash", "-c", "/usr/share/nginx/html/env.sh && nginx -g \"daemon off;\""]
```

Now our container is ready. We can do all the standard stuff with it. We can build a container, run it with inline configurations and push it to a repository provided by services such as [Dockerhub](https://hub.docker.com/).

```sh
docker build . -t kunokdev/cra-runtime-environment-variables
docker run -p 3000:80 -e API_URL=https://staging.api.com -t kunokdev/cra-runtime-environment-variables
docker push -t kunokdev/cra-runtime-environment-variables
```

The above `docker run` command should output application like so:

![Image](https://cdn-media-1.freecodecamp.org/images/1*kK7Ss5ODlukXgsLNuYh0Lg.png)
_Using API_URL which was provided via environment variable flag to docker run command_

Lastly, let’s create our docker-compose file. You will usually have different docker-compose files depending on the environment and you will use `-f` flag to select which file to use.

```yml
version: "3.2"
services:
  cra-runtime-environment-variables:
    image: kunokdev/cra-runtime-environment-variables
    ports:
      - "5000:80"
    environment:
      - "API_URL=production.example.com"
```

And if we do `docker-compose up` we should see output like so:

![Image](https://cdn-media-1.freecodecamp.org/images/1*7TBDwzS_otshjMhQqvycmg.png)
_Using API_URL which was provided via docker-compose environment property_

Great! We have now achieved our goal. We can reconfigure our application easily in both development and production environments in a very convenient way. We can now finally build only once and run everywhere!

**If you got stuck or have additional ideas, access the [source code on GitHub](https://github.com/kunokdev/cra-runtime-environment-variables).**

#### ? Next steps

The current implementation of the shell script will print all variables included within the .env file. Most of the time we don’t want to expose all of them. You could implement filters for variables you don’t want to expose using prefixes or a similar technique.

#### ? Alternative solutions

As noted above, the build time configuration will satisfy most use cases. You can rely on the default approach using .env file per environment and build a container for each environment and inject values via CRA Webpack provided environment variables.

You could also have a look at this [CRA GitHub repository issue](https://github.com/facebook/create-react-app/issues/2353) which covers this problem. By now, there should be more posts and issues which cover this topic. Each offers a similar solution as above. It’s up to you to decide how are you going to implement specific details. You might use Node.js to serve your application which means that you can also replace shells script with Node.js script. Note that Nginx is more convenient to serve static content.

_If you have any questions or want to offer feedback; feel free to open issue on [GitHub.](https://github.com/kunokdev/cra-runtime-environment-variables) Optionally follow me for further posts related to web technologies._

