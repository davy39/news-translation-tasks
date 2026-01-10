---
title: How to run Laravel on Google Cloud Run with Continuous Integration - a step
  by step guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-14T20:04:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-laravel-6-on-google-cloud-run-with-continuous-integration-ci-step-by-step
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/laravel6-on-gcr-f.jpg
tags:
- name: Devops
  slug: devops
- name: google cloud
  slug: google-cloud
- name: google cloud run
  slug: google-cloud-run
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: Software Engineering
  slug: software-engineering
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Geshan Manandhar

  Laravel has soared in popularity over the last few years. The Laravel community
  even says that Laravel has made writing PHP more enjoyable instead of a pain. Laravel
  6 has some interesting new features. Getting a super scaleable w...'
---

By Geshan Manandhar

Laravel has [soared](https://trends.google.com/trends/explore?date=2014-11-12%202019-11-12&q=laravel,symfony) in popularity over the last few years. The Laravel community even says that Laravel has made writing PHP more enjoyable instead of a pain. Laravel 6 has some interesting new [features](https://laracasts.com/series/whats-new-in-laravel-6). Getting a super scaleable working URL for your application takes hours if not days. Setting up something like Kubernetes is a huge task. This is where Google Cloud Run shines: you can get a working HTTPS URL for any of your containerized apps in minutes.

[Google Cloud Run](https://cloud.google.com/run/) is serverless and fully managed by Google. You get super scale, billing by the second, HTTPS URLs, and your own domain mapping. If you want to run stateless containers, Cloud Run is hands down the easiest way to do it. In this post, I will detail how to get your Laravel 6 app working on Google cloud run with Continuous Integration (CI).

## Prerequisites

* You are familiar with PHP/Composer and aware of Laravel (if you’ve landed here you are, I suppose)
* You know how to use Git from the CLI
* Your code is hosted on GitHub for CI/CD and you are familiar with GitHub
* Know a fair bit of Docker, maybe even multi-stage build
* Have a working Google cloud account (they give you [$300 credit](https://cloud.google.com/free/) free for 1 yr, no reasons not to have an account)

## **Why is Cloud Run a great option for beginners?**

For two main reasons:

1. Learn about the best practices and software like docker and CI/CD
2. Getting the basics going just involves clicking a button, selecting 2 things, waiting for 5 mins, and you get a working HTTPS URL. Can it be any easier than this? :)

## **Steps to deploy**

Below are the steps to set up and deploy Laravel 6 on Cloud Run:

### **1. Clone Laravel or new Laravel project**

Start by cloning Laravel or using composer or the Laravel CLI as indicated in the official [installation](https://laravel.com/docs/5.8/installation) guide. I am using composer to get the latest Laravel as below:

#### **Command**

I ran the following command to get the latest Laravel:

```bash
composer create-project --prefer-dist laravel/laravel laravel6-on-google-cloud-run

```

![Installing Laravel with composer](https://geshan.com.np/images/laravel6-on-google-cloud-run/01install-laravel.jpg)
_Creating a new Laravel Project with Composer_

### **2. Test it locally first**

Then run `cd laravel6-on-google-cloud-run` then `php artisan serve` to see if it is working. For me it was fine when I went to `http://localhost:8000` on a web browser. I had PHP 7.2 installed locally.

![Running Laravel locally](https://geshan.com.np/images/laravel6-on-google-cloud-run/02running-laravel.jpg)
_Laravel running locally without Docker_

### **3. Create a new GitHub repo**

Create a new repository on Github like below:

![Creating a repo for Laravel on Github](https://geshan.com.np/images/laravel6-on-google-cloud-run/03github-repo.jpg)
_Create a new public repo on Github_

You can use any Git hosting provider, but for this example I will be using [Github Actions](https://github.com/features/actions) to run tests (and Github is the most popular git hosting tool).

### **4. Add repo, push readme**

Now after you have the repo created, add it to your local Laravel copy and push the Readme file. To do this run the following commands on your CLI:

```
git init
code . # I used VS code to change the readme
git add readme.md
git commit -m "Initial commit -- App Readme"
git remote add origin git@github.com:geshan/laravel6-on-google-cloud-run.git
git push -u origin master

```

#### **After running the above commands I had this on my Github repo**

![After the first push, repo looks like this](https://geshan.com.np/images/laravel6-on-google-cloud-run/04initial-push.jpg)
_Repo after pushing the readme to master branch_

### **5. Add full Laravel, open a PR**

Now let’s add the whole app as a PR to the Github repo by executing the following commands:

```
git checkout -b laravel6-full-app
git add .gitignore
git add .
git commit -m "Add the whole Laravel 6 app"
git push origin laravel6-full-app

```

After that go and open a Pull Request (PR), on the repo like [this](https://github.com/geshan/laravel6-on-google-cloud-run/pull/1) one. You might be thinking I am the only one working on this, why do I need a PR? Well, it is always better to do things methodically even if it is just one person working on the project :).

After that merge your pull request.

### **6. Setup tests with [GitHub actions](https://github.com/features/actions)**

Now the fun part: after you merged your PR now Github knows that this is a Laravel project. Click on the  `Actions` tab on your repo page and you should be able to see something like below:

![Click Actions tab to view options](https://geshan.com.np/images/laravel6-on-google-cloud-run/05github-actions.jpg)
_Setup the CI workflow for Laravel with Github Actions_

Click the `Set up this workflow` under `Laravel` then on the next page click the `Start commit` button on the top right. After that add a commit message like below and click `Commit new file`.

![Add Laravel tests action](https://geshan.com.np/images/laravel6-on-google-cloud-run/06gh-actions-ci.jpg)
_Steps to setup the CI workflow with Github Actions_

There you go, you have your CI setup. Laravel default tests will run on each git push now. Wasn’t that easy? Thank Github for this great intelligence. No more creating `.myCIname.yml` files :).

### **7. Add docker and docker-compose to run app locally**

Now let’s add docker and docker-compose to run the app locally without PHP or artisan serve. 

We will need the container to run Laravel on Google Cloud Run too. This part is inspired by the [Laravel on Google Cloud Run](https://nsirap.com/posts/010-laravel-on-google-cloud-run/) post by Nicolas. If you want to learn more about [Docker](https://www.docker.com/) and Laravel please refer to this [post](https://geshan.com.np/blog/2015/10/getting-started-with-laravel-mariadb-mysql-docker/).

Run the following commands first to get your master up to date as we added the `workflow` file from Github interface:

```
git checkout master
git fetch
git pull --rebase origin master # as we added the workflow file from github interface
git checkout -b docker

```

Add a key to the `.env.example` file. Copy it from the `.env` file like below:

```
APP_NAME=Laravel
APP_ENV=local
APP_KEY=base64:DJkdj8L5Di3rUkUOwmBFCrr5dsIYU/s7s+W52ClI4AA=
APP_DEBUG=true
APP_URL=http://localhost

```

As this is just a demo this is ok to do. For a real app always be careful with secrets. For production-ready apps do turn of the debugging and other dev related things.

Add the following `Dockerfile` on the project root:

```
FROM composer:1.9.0 as build
WORKDIR /app
COPY . /app
RUN composer global require hirak/prestissimo && composer install

FROM php:7.3-apache-stretch
RUN docker-php-ext-install pdo pdo_mysql

EXPOSE 8080
COPY --from=build /app /var/www/
COPY docker/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY .env.example /var/www/.env
RUN chmod 777 -R /var/www/storage/ && \
    echo "Listen 8080" >> /etc/apache2/ports.conf && \
    chown -R www-data:www-data /var/www/ && \
    a2enmod rewrite

```

Then add the following file at `docker/000-default.conf`

```
<VirtualHost *:8080>

  ServerAdmin webmaster@localhost
  DocumentRoot /var/www/public/

  <Directory /var/www/>
    AllowOverride All
    Require all granted
  </Directory>

  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

```

After that add the following `docker-compose.yml`

```
version: '3'
services:
  app:
    build:
      context: ./
    volumes:
      - .:/var/www
    ports:
      - "8080:8080"
    environment:
      - APP_ENV=local

```

#### **Let's Boil down to main things**

If you try to understand everything here it might be overwhelming, so let me boil down the main parts:

1. We are using the official PHP Apache docker image to run Laravel, which has PHP version 7.3.
2. We are using a multistage build to get the dependencies with Composer then we're copying them to the main docker image that has PHP 7.3 and Apache.
3. As Google Cloud Run requires the web-server to be listening to port `8080` and we are using `000-default.conf` to configure this
4. To make things easy to run with the single command `docker-compose up` we are using docker-compose.
5. Now as you have read this far, run `docker-compose up` on your root and then after everything runs go to `http://localhost:8080` to see that Laravel 6 is running locally on Docker. Below is my `docker-compose up` output towards the end:

![Docker compose running Laravel with PHP 7.3 and Apache](https://geshan.com.np/images/laravel6-on-google-cloud-run/07docker-compose-output.jpg)
_Docker compose running successfully on local machine_

As Laravel is running fine with Docker, let’s open a PR like [this](https://github.com/geshan/laravel6-on-google-cloud-run/pull/2/files) one to add Docker to our project. I ran the following commands on the root of the project before opening the Pull Request (PR):

```
git status

```

It should give you something like below:

```
On branch docker
Untracked files:
  (use "git add <file>..." to include in what will be committed)

  Dockerfile
  docker-compose.yml
  docker/

nothing added to commit but untracked files present (use "git add" to track)

```

Now run the following commands:

```
git add .
git commit -m "Add docker and docker compose"
git push origin docker

```

As a bonus it will run the Laravel default test on the push, like you can see below:

![On each push PHP unit tests will run](https://geshan.com.np/images/laravel6-on-google-cloud-run/08test-running-gh.jpg)
_Default Laravel tests running with Github Actions_

Only the owner of the repo has access to the `Actions` tab so other people don’t necessarily need to know the results of your test builds :).

### **8. Add deploy to [Google Cloud button](https://github.com/GoogleCloudPlatform/cloud-run-button)**

Now let’s deploy this Laravel setup to Google Cloud Run the easy way. Given that you have merged your PR from the `docker` branch, let’s run the following commands:

```
git checkout master
git fetch
git pull --rebase origin master
git checkout -b cloud-run-button

```

Then add the following to your `readme.md` file:

```
### Run on Google cloud run

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/geshan/laravel6-on-google-cloud-run.git)

```

Be careful and replace the last part with your repo’s `HTTPs` URL. For example, if your repo is at `https://github.com/ghaleroshan/laravel6-on-google-cloud-run` it will be `https://github.com/ghaleroshan/laravel6-on-google-cloud-run.git`, then commit and push. Your PR should look something like [this](https://github.com/geshan/laravel6-on-google-cloud-run/pull/3/files) one.

### **9. Deploy on Google Cloud Run**

After you merge your Pull Request (PR), then go to your repo page and click on the `Run on Google Cloud` button.

![Click on the blue button to deploy the app](https://geshan.com.np/images/laravel6-on-google-cloud-run/09cloud-run-button.jpg)
_Github readme after adding the Run on Google Cloud button_

After that, if you are logged into your Google account and have Google cloud setup with 1 project, click “Proceed”. You might need to wait a bit, then

1. Choose the project – `Choose a project to deploy this application`
2. Choose the region – `Choose a region to deploy this application`, I usually go with `us-central-1`
3. Then wait for the container to be built and deployed. You can see my process below:

If everything goes fine on your `Google Cloud Shell`, you will see the HTTPS URL that you can hit to see your Laravel app running like below:

![Hit the given URL to see its running](https://geshan.com.np/images/laravel6-on-google-cloud-run/10laravel-running-gcr.jpg)
_Deploy screen of Google Cloud Shell for Laravel 6 on Cloud Run_

What just happened above is:

1. After choosing the region, the script built a docker container image from the `Dockerfile` in the repo
2. Then it pushed the built image to [Google Container Registry](https://cloud.google.com/container-registry/)
3. After that using the [gcloud](https://cloud.google.com/sdk/gcloud/) CLI it deployed the built image to Cloud Run, which gave back the URL.

### **10. Hurray, your app is working**

After you git the URL you should see your app working on Google Cloud Run like below:

![Laravel Running on Google Cloud Run](https://geshan.com.np/images/laravel6-on-google-cloud-run/11laravel-url.jpg)
_Laravel running on Google Cloud Run with Serverless HTTPS URL :)_

If you want to deploy another version you can merge your PR to master and click the button again to deploy.

## **More about Google Cloud Run**

The [pricing](https://cloud.google.com/run/pricing) for Google Cloud Run is very generous. You can run any containerized app or web app on Google cloud run. I ran a pet project that got ~ 1 request per minute and I did not have to pay anything.

Behind the scenes, it is using [Knative](https://cloud.google.com/knative/) and [Kubernetes](https://kubernetes.io/). It can also be run on your Kubernetes cluster but who would choose to manage a K8s cluster if you can just push and get a scaleable serverless fully managed app :).

## **TLDR**

To run Laravel 6 on Google Cloud Run quickly follow the steps below:

1. Make sure you are logged into your [Google Cloud Account](https://console.cloud.google.com/)
2. Go to [https://github.com/geshan/laravel6-on-google-cloud-run](https://github.com/geshan/laravel6-on-google-cloud-run)
3. Click the “Run On Google Cloud” blue button
4. Select your project
5. Select your region
6. Wait and get the URL of your Laravel App as below, Enjoy!

![Hit the given URL to see its running](https://geshan.com.np/images/laravel6-on-google-cloud-run/10laravel-running-gcr.jpg)
_Deploy log of Cloud Run button to deploy Laravel on Google Cloud Run_

---

![Laravel Running on Google Cloud Run](https://geshan.com.np/images/laravel6-on-google-cloud-run/11laravel-url.jpg)
_Laravel Running successfully on Google Cloud Run_

## **Conclusion**

There you go – running a Laravel app on Google cloud run was pretty easy. You have even got test running on Github with Github actions. Hope it helps. To do a CI/CD approach you can check out this [post](https://medium.com/google-cloud/simplifying-continuous-deployment-to-cloud-run-with-cloud-build-including-custom-domain-setup-ssl-22d23bed5cd6). It shows deployment using Cloud build. As the same container is running for local and production (Google Cloud Run) environment you don’t need to learn a new framework to go Serverless.

> Any containerized web app can be run on Google Cloud Run, it is a great service. You can read more at https://geshan.com.np

