---
title: How to deploy infinitely scalable applications to AWS in minutes with Up &
  Semaphore CI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-04T20:29:43.000Z'
originalURL: https://freecodecamp.org/news/deploy-infinitely-scalable-applications-in-minutes-with-up-semaphore-ci-c2a60f821207
coverImage: https://cdn-media-1.freecodecamp.org/images/1*giDY-7KKIxxiVMdXh_fIpg.jpeg
tags:
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By TJ Holowaychuk

  Many Apex Up users have been asking about integration with continuous integration
  platforms, this post walks through staging and deploying Up to production using
  Semaphore CI.

  Serverless Up applications typically deploy in a few sec...'
---

By TJ Holowaychuk

Many [Apex Up](https://github.com/apex/up) users have been asking about integration with continuous integration platforms, this post walks through staging and deploying Up to production using [Semaphore CI](https://semaphoreci.com/).

Serverless Up applications typically deploy in a few seconds from a laptop, however with a poor network connection you may want to consider CI, not only to improve workflow and testing, but for the improved upload speed.

Semaphore is my CI of choice — it has a clean design, lets you easily encrypt the env variables, schedule timed builds, and doesn’t require you to litter your repositories with dotfiles. With that said as long as you can define environment variables, you can choose whichever CI platform you prefer.

### The Application

For this example we’ll be deploying a minimal [Koa](http://koajs.com/) Node.js application. Create a new repository in your GitHub, and add `app.js` with the following code:

```
const Koa = require('koa')const app = new Koaconst { PORT = 3000 } = process.env
```

```
app.use(function *() {  this.body = "Hello\n"})
```

```
app.listen(PORT)
```

You can add the dependencies via npm or yarn, whichever you prefer. Deploy the app to AWS and check out that glorious “Hello”:

```
$ up$ curl `up url`Hello
```

Now let’s set up CI.

### Setup

To get started in Semaphore, you’ll first need to create a new project:

![Image](https://cdn-media-1.freecodecamp.org/images/AAlXwpQb3HFUWlplzxX9nujLZij7j-R19ofd)

And find the repository you created earlier in GitHub:

![Image](https://cdn-media-1.freecodecamp.org/images/DTOBiQIoSHp8dH0UBYuSX9nsljsAjFw1Gm0T)

Now on to the good stuff — configuring the build!

### Configuring the Jobs

One of the things I really like about Semaphore is that you don’t have to use dotfiles in your repository, simply define the jobs and commands required in the UI. If your use-case allows for it, you can even run jobs in parallel to speed things up.

The “Setup” job will install NPM packages for the application, adjust the owner of `/usr/local/bin` since this is where Up will be installed by default, and then finally install Up itself. Up is distributed as binaries, so this process takes only a few seconds.

```
npm installsudo chown -R $(whoami) /usr/local/bincurl -f https://up.apex.sh/install | sh
```

You can define and re-order the commands, however, if you click “Edit Job” you can copy-and-paste the commands above as text. The second job in this case is used to deploy to development (`up` ).

![Image](https://cdn-media-1.freecodecamp.org/images/w-gqSlUmkoNDXHmFsqDkrcsUd81ns0hlwi7F)

In scenarios where you run into permission issues installing to /usr/local/bin, or simply prefer to avoid this, you may provide an install path with `BINDIR`:

```
curl -sf https://up.apex.sh/install | BINDIR=. sh
```

Note that if you’re running Node.js using Up, you’ll want to specify **6.10.3**, as this is the “native” version of Node.js supported by [AWS Lambda](https://aws.amazon.com/lambda/).

### Configuring your AWS Credentials

After the jobs are configured just select your branch and click “Start”.

![Image](https://cdn-media-1.freecodecamp.org/images/Ch9LA9g3ZBQCPOLkmCfb4nwF8q5eUaMvDgGd)

The first thing you’ll see is that `up` fails! This is because we haven’t provided any AWS credentials, so Up doesn’t know where to deploy, and is not authorized to do so.

![Image](https://cdn-media-1.freecodecamp.org/images/XhKBFTrr-KTwbMxabpG-y0odBYHnoSVpu1JF)

If you head over to the “Environment Variables” tab in the sidebar, you can add plain text or encrypted env vars. You’ll need two variables, the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_KEY_ID` . The first may be plain text, however the second should be encrypted, when in doubt, just encrypt.

![Image](https://cdn-media-1.freecodecamp.org/images/B56aGYdcVJtL3IFIJW3ibFmdRfX2VoPV7l8b)

Now when you perform a new build you should have a passing CI pipeline!

![Image](https://cdn-media-1.freecodecamp.org/images/8oeJIvWWzvjbVS9uhqHTNIQfzOnvaZzWxfAO)

> You can read more the options for AWS credentials in the [Up documentation](http://up.docs.apex.sh/#aws_credentials). Also make sure to never use your root credentials in external services such as CI.

### Deploying to Production with Up Pro

The [Pro version of Up](https://github.com/apex/up#pro-features) is in early-access — only $10/mo with the discount for unlimited use in your organization — providing encrypted env variables, alerting, and more goodies soon!

After [subscribing to Up Pro](http://up.docs.apex.sh/#guides.subscribing_to_up_pro) you’ll need to authenticate in order to install the Pro binary. Run the following command to copy the credentials to your clipboard.

```
$ up team ci --copy
```

Add a new encrypted environment variable named `UP_CONFIG` :

![Image](https://cdn-media-1.freecodecamp.org/images/MCi78yihSturQkKdPCg1vu5s5kd6efUo3qrg)

Next you’ll need to add `up upgrade` after the installation of Up, this will install the Pro version, as it detects `UP_CONFIG` . Note that the “Deploy” job has been changed to deploy to production rather than development. Changing this command allows you to map GIT branches to the various stages, so you can utilize CI for pushing to development, staging, or production.

Note you may upgrade to a specific version of Up via `up upgrade -t 0.5.4` to “lock” the version.

![Image](https://cdn-media-1.freecodecamp.org/images/w-oaM4NS85gdr2iv8btyob96EJYxrtuHD5Rg)

Try changing the “Hello\n” string in app.js to “Hello from Semaphore CI\n” and push the commit to GitHub.

```
app.use(function *() {  this.body = "Hello from Semaphore CI\n"})
```

In a minute or less you should see the lovely leafy green of success! There is no remote build on the AWS side, once it’s green, your application is live and serving requests, in under a minute.

![Image](https://cdn-media-1.freecodecamp.org/images/-uMNtZ7IC5fxZst3PNXqbGjG5rfERr3ZpGG8)

If deploying apps, apis, and sites to your own AWS account in a single command sounds helpful, take a look at [Apex Up](https://github.com/apex/up) — and check out [Semaphore CI](https://semaphoreci.com/) for creating organization-wide continuous integration workflows.

**EDIT**: Note that with recent versions of Up you may also upgrade the binary in-place, as to avoid permission issues or changes to `/usr/local/bin` , and optionally pass a specific version to “pin” the version of **Up Pro** via `-t x.x.x`

```
curl -f https://up.apex.sh/install | BINDIR=. sh./up upgrade -t 0.5.8./up production
```

I reached out to Semaphore CI and they offered to provide a 30% discount for the first 3 months to Up users, using the coupon “**SEMAPHORE330**”. Note that it’s redeemable until the 31st of December.

