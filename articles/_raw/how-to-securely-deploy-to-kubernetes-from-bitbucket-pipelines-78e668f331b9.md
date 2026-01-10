---
title: How to securely deploy to Kubernetes from Bitbucket Pipelines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T18:56:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-securely-deploy-to-kubernetes-from-bitbucket-pipelines-78e668f331b9
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca305740569d1a4ca58a3.jpg
tags:
- name: Bitbucket
  slug: bitbucket
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dane Stevens


  Over 100,000 GitHub repos have leaked API or cryptographic keys - ZDNet

  Hands up if this has happened to you. You''re reading a well-written article on
  one of countless topics, and you get to the line that goes something like this:

  //...'
---

By Dane Stevens

![Locking it down](https://cdn.tueri.io/274877906995/lock-it-down.jpg)

[Over 100,000 GitHub repos have leaked API or cryptographic keys - ZDNet](https://www.zdnet.com/article/over-100000-github-repos-have-leaked-api-or-cryptographic-keys/)

Hands up if this has happened to you. You're reading a well-written article on one of countless topics, and you get to the line that goes something like this:

```javascript
// DO NOT DO THIS IN A PRODUCTION APP
const API_KEY = '<api-key-displayed-in-plain-text>'

```

Ok, so how should you be doing this? Unfortunately, there isn't a one-size-fits-all approach to securing your secrets. Different programming languages deployed in different environments all handle secrets in their own way.

Suffice it to say that you should never store secrets in your code or repository. Secrets should be passed into your app through environment variables at the last possible moment.

## Bitbucket Pipelines - Continuous Delivery

I have been using [Bitbucket Pipelines](https://medium.com/r/?url=https%3A%2F%2Fbitbucket.org%2Fproduct%2Ffeatures%2Fpipelines%3Futm_source%3DMedium%26utm_medium%3DPost%26utm_campaign%3DTueri%26utm_content%3DKubernetes) since it was in Alpha and I have to say, it's fantastic. It has to be the quickest and easiest way to setup continuous delivery right from your repo.

Pipelines are configured with YAML files and can be very simple or extremely complex depending on your needs.

### Pipelines Configuration

I like to break up my build jobs into steps for a couple of reasons:

* If a step fails, you can re-run individual steps.
* Each step is isolated from the others. Only your base repo and any "artifacts" you declare will be passed to the next step.

Here is a 3-step bitbucket-pipelines.yml file that takes a create-react-app site, packages it as a Docker image and deploys it to a Kubernetes cluster:

```yaml
options:
  # Enable docker for the Pipeline
  docker: true

pipelines:
  branches:
    master:
      - step:
          name: Build app for Production (create-react-app)
          image: mhart/alpine-node:10
          caches:
            - node
          script:
            # Install Dependencies
            - npm install
            # Run our Tests
            - npm run test
            # Package App for Production
            - npm run build
          artifacts:
            # Pass the "build" Directory to the Next Step
            - build/**
      - step:
          name: Build Docker Image
          script:
            # NOTE: Set $DOCKER_HUB_USERNAME and $DOCKER_HUB_PASSWORD as environment SECRETS in Bitbucket repository settings
            # Use $BITBUCKET_COMMIT to tag our docker image
            - export IMAGE_NAME=<docker-username>/<docker-image>:$BITBUCKET_COMMIT
            # Build the Docker image (this will use the Dockerfile in the root of the repo)
            - docker build -t $IMAGE_NAME .
            # Authenticate with the Docker Hub registry
            - docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_PASSWORD
            # Push the new Docker image to the Docker registry
            - docker push $IMAGE_NAME
      - step:
          # trigger: manual
          name: Deploy to Kubernetes
          image: atlassian/pipelines-kubectl
          script:
            # NOTE: $KUBECONFIG is secret stored as a base64 encoded string
            # Base64 decode our kubeconfig file into a temporary kubeconfig.yml file (this will be destroyed automatically after this step runs)
            - echo $KUBECONFIG | base64 -d > kubeconfig.yml
            # Tell our Kubernetes deployment to use the new Docker image tag
            - kubectl --kubeconfig=kubeconfig.yml --namespace=<namespace> set image deployment/<deployment-name> <deployment-name>=<docker-username>/<docker-image>:$BITBUCKET_COMMIT


```

_bitbucket-pipelines.yml_

```dockerfile
FROM mhart/alpine-node:10
WORKDIR /app
EXPOSE 5000

# Install http server
RUN yarn global add serve

# Bundle app source
COPY build /app/build

# Run serve
CMD [ "serve", "-n", "-s", "build" ]

```

_Dockerfile_

Here's the important part of all that:

```yaml
- echo $KUBECONFIG | base64 -d > kubeconfig.yml

```

Our kubeconfig file is stored as a Base64 encoded string in a Bitbucket secret named `$KUBECONFIG`.

_Bitbucket secrets are stored encrypted, and decrypted when you call the variable in pipelines._

We decode the `$KUBECONFIG` variable and store it in a temporary file called kubeconfig.yml which is automatically deleted as soon as this step completes.

## Breaking it Down

### Step 1

1. Install dependencies
2. Run tests
3. Build
4. Pass build directory to Step 2

### Step 2

1. Name Docker image
2. Build Docker image
3. Push image to Docker Hub

### Step 3

1. Decode kubeconfig
2. Set deployment image

## Build Performance

This entire build takes less than 1 minute 40 seconds and using Alpine Node the Docker image is just 29 MB.

## Conclusion

Securing your secrets isn't hard, but it starts with knowing where to look.

Some tips for securing secrets in different Node.js environments:

* Node.js (Development): use .env files and .gitignore to keep .env files out of your repository.
* Node.js (Production): use Kubernetes Secrets, Docker Secrets and pass as environment variables into the container.

### Remember this one rule:

* Don't store secrets in your code, your repository or your docker image.

Happy coding!

---

_Originally published at [Tueri.io](https://tueri.io/blog/2019-04-04-how-to-securely-deploy-to-kubernetes-from-bitbucket-pipelines/?utm_source=FreeCodeCamp&utm_medium=Post&utm_campaign=Continuous%20Deployment)_

