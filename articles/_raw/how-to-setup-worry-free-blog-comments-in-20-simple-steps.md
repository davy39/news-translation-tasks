---
title: Brilliant Add-on For Static Sites That Will Make You Dance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-08T12:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-worry-free-blog-comments-in-20-simple-steps
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Copy-of-Static-Site-Docker-Recipes-2.jpg
tags:
- name: blog
  slug: blog
- name: Docker compose
  slug: docker-compose
- name: nginx
  slug: nginx
- name: oauth
  slug: oauth
- name: Static Site Generators
  slug: static-site-generators
seo_title: null
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  Privacy.

  Performance.

  Brilliant looks.

  Can you have all three?

  (Of course!)

  Having a statically generated blog is great. Many folks use services like Disqus
  and Google Analytics to make t...'
---

By Jared Wolff

**This post is originally from [www.jaredwolff.com](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/)**

Privacy.

Performance.

Brilliant looks.

Can you have all three?

(Of course!)

Having a statically generated blog is great. Many folks use services like Disqus and Google Analytics to make them even better. Not surprising if you were one of them!  Privacy concerns are are the forefront of everyone’s attention. So, rather than keeping the status quo, it’s time to do something about it!

**If you've been looking to protect your site visitor's privacy and improve performance this blog post is for you.**

In this article we'll be using DigitalOcean’s Docker droplet. It allows you to host several different applications/services on one (virtual) machine. By the end of it you'll know how to run your own comments server using Commento. Plus i’ll share a few tricks i’ve learned along the way to make it much easier for you.

Leeeets go!

## Reverse Proxy

One of the most important aspects of this setup is the reverse proxy. A reverse proxy acts like a router. Requests come in for a certain domain.  That request is then routed to the service associated with that domain.

Here’s a diagram from the Nginx Reverse Proxy + Let’s Encrypt Helper documentation. It'll help illustrate the idea.

![Nginx Reverse Proxy with Let's Encrypt](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/webproxy-1f1c7540-4b86-4478-bb3e-f05043d671a5.jpg)

Another benefit is that there’s an extra layer of protection to the outside world. Your websites run in a private network and the only access is through the Nginx reverse proxy. Point your DNS to the server and Nginx handles all the magic.

Here's how to get it setup:

1. Go ahead and set up your Digital Ocean Droplet. [All the info you need is right here](https://marketplace.digitalocean.com/apps/docker). The $5 version is more than sufficient.
2. [Go here to clone the repository.](https://github.com/evertramos/docker-compose-letsencrypt-nginx-proxy-companion) You can also run this in your terminal. Make sure you SSH into your Digital Ocean droplet first!

        git clone git@github.com:evertramos/docker-compose-letsencrypt-nginx-proxy-companion.git

3. Change directories to the cloned repository.
4. Copy `.env.sample` to `.env` and update the values inside. I had to change the `IP` value to the IP of my Digital Ocean Droplet. I left all the other ones alone.
5. Run `docker-compose up -d` to start everything. (you can run without the `-d` option to make sure everything starts ok. Or you can attach the log output using `docker container logs -f <container name`

When pointing your sub-domains to this server, make sure you use an A record. Here's an example of mine:

![NS1 A Record Configuration](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-9c0432cd-4d40-4c89-88f3-24037d915eaf.52.32_PM.png)

Depending on your DNS provider, you'll have to figure out how to set an A record. That is beyond the purpose of this article though!

## Setting Up Commento with Docker Compose

![Commento Logo with Docker Logo](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Compose-1c868832-6819-43e2-8696-ab698a10dbee.jpg)

Here is the current docker compose file i'm using for Commento. It includes a few more environment variables for configuring Github, Gitlab and Google. It also includes the environment variables for setting the SMTP settings. These parameters are important. Otherwise you can't receive password reset or moderation emails!

    version: '3'

    services:
      commento:
        image: registry.gitlab.com/commento/commento
        container_name: commento
        restart: always
        environment:
          COMMENTO_ORIGIN: https://${COMMENTS_URL}
          COMMENTO_PORT: 8080
          COMMENTO_POSTGRES: postgres://postgres:postgres@postgres:5432/commento?sslmode=disable
          COMMENTO_SMTP_HOST: ${SMTP_HOST}
          COMMENTO_SMTP_PORT: ${SMTP_PORT}
          COMMENTO_SMTP_USERNAME: ${SMTP_USERNAME}
          COMMENTO_SMTP_PASSWORD: ${SMTP_PASSWORD}
          COMMENTO_SMTP_FROM_ADDRESS: ${SMTP_FROM_ADDRESS}
          COMMENTO_GITHUB_KEY: ${COMMENTO_GITHUB_KEY}
          COMMENTO_GITHUB_SECRET: ${COMMENTO_GITHUB_SECRET}
          COMMENTO_GITLAB_KEY: ${COMMENTO_GITLAB_KEY}
          COMMENTO_GITLAB_SECRET: ${COMMENTO_GITLAB_SECRET}
          COMMENTO_GOOGLE_KEY: ${COMMENTO_GOOGLE_KEY}
          COMMENTO_GOOGLE_SECRET: ${COMMENTO_GOOGLE_SECRET}
          COMMENTO_TWITTER_KEY: ${COMMENTO_TWITTER_KEY}
          COMMENTO_TWITTER_SECRET: ${COMMENTO_TWITTER_SECRET}
          VIRTUAL_HOST: ${COMMENTS_URL}
          VIRTUAL_PORT: 8080
          LETSENCRYPT_HOST: ${COMMENTS_URL}
          LETSENCRYPT_EMAIL: ${EMAIL}
        depends_on:
          - postgres
        networks:
          - db_network
          - webproxy

      postgres:
        image: postgres
        container_name: postgres
        environment:
          POSTGRES_DB: commento
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        networks:
          - db_network
        volumes:
          - postgres_data_volume:/var/lib/postgresql/data

    networks:
      db_network:
      webproxy:
        external: true

    volumes:
      postgres_data_volume:

To set the environment variables, put them inside an `.env` file. Make sure the `.env` file is in the same directory as `docker-compose.yml`. When you run `docker-compose up` it will apply the variables set in the `.env` file. Nothing gets set if they're left blank.

Set the required `COMMENTS_URL` and `EMAIL` or you may run into problems. The best way to set these is by pacing them in the `.env` file. Here is an example:

    COMMENTS_URL=comments.your.url
    EMAIL=you@your.url

## Getting OAuth Key & Secret

Commento works with most popular OAuth providers. Thus visitors can leave comments without making an account.

The instructions are similar for each. I've outlined the steps for all of them below.

### Twitter

1. Login to [Twitter.com](http://twitter.com) and apply for a developer account: [https://developer.twitter.com/en/application/use-case](https://developer.twitter.com/en/application/use-case)

    ![Twitter API Access](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-4171cdf7-6c2b-408b-bb64-57822ede91cb.26.08_PM.png)

2. Describe how you'll use the API. You can use what I wrote.

    ![How will you use the API?](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-4c0aecf2-c020-4005-bd5f-81e3b4ac6b8f.28.43_PM.png)

3. Double check your entry and click **Looks Good!**

    ![Is everything correct?](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-ade63510-86d3-48a4-a121-221f6e14cd96.28.50_PM.png)

4. Agree to the terms of service.

    ![Agree to Developer Agreement](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-2e8e3089-bd51-4d27-8573-6987aafc663e.28.59_PM.png)

    ![You did it!](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-145b1bfd-9fc7-4ea6-ba5f-032e59d7fe8d.41.47_PM.png)

5. They'll tell you to check your email for a confirmation. Confirm your email and you should be able to create your first app!
6. Once approved to to **Get started** click **Create an app**.

    ![Create an app](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-640686b8-15c6-4af0-b9df-65ce15ae0fe7.29.22_PM.png)

7. Next screen, again click **Create an app**

    ![Create an app](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-de2b85d5-8bb7-428f-bfd1-2a23d0b7d4e0.29.26_PM.png)

8. Enter all the appropriate details. For the callback URL, use [`https://<your URL>/api/oauth/github/callback`](https://comments.jaredwolff.com/api/oauth/google/callback) where [`<your URL>`](https://comments.jaredwolff.com/api/oauth/google/callback) is your Commento subdomain.

    ![App details](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-91acb343-9dee-4917-be77-9704fe439722.32.44_PM.png)

9. Finally, once you're done filling out the information to go the **Keys and Token**s area. Save both the key and token. Enter them into the `.env` file. You can use `COMMENTO_TWITTER_KEY` and `COMMENTO_TWITTER_SECRET`

    ![Get oauth key and secret](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-b910e9ff-dc34-45e8-94df-affb06702617.33.07_PM.png)

### Gitlab

1. Login to [Gitlab.com](http://gitlab.com) and go to to top right and click **Settings**
2. Then click on **Applications**

    ![Gitlab profile](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-c6da9d02-2052-4fa4-89de-d5212b8f49ca.56.47_PM.png)

3. Enter a name for your app. I put **Commento**.
4. Set the Redirect URI to [`https://<your URL>/api/oauth/gitlab/callback`](https://comments.jaredwolff.com/api/oauth/google/callback)
5. Select the **read_user** scope.

    ![Gitlab add application](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-e616c338-6144-4704-93c6-914db6fad5f6.59.15_PM.png)

6. Click the green **Save Application** button
7. Copy the **Application ID** and **Secret** and place them in your `.env` file using `COMMENTO_GITLAB_KEY` and `COMMENTO_GITLAB_SECRET`

    ![Application key and secret](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_1-a4f4ab4a-9fd6-423f-821c-6ff2f174e589.04.10_PM.png)

### Github

1. To get your OAuth key and secret, you'll need to go to this URL: [https://github.com/settings/developers](https://github.com/settings/developers)
2. Once there, click on **New OAuth App**

    ![Add OAuth application](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_9-18bf8f23-916f-476b-8c25-3377de931fe3.15.33_AM.png)

3. Enter your details. For the callback URL, use [`https://<your URL>/api/oauth/github/callback`](https://comments.jaredwolff.com/api/oauth/google/callback) where [`<your URL>`](https://comments.jaredwolff.com/api/oauth/google/callback) is your Commento subdomain.

    ![Register new OAuth application](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_9-6e616334-7123-4de4-a4fd-f2fe319b1971.28.24_AM.png)

    *Note: Make sure you include `https` in your URLs.*

4. Grab the **Client ID** and **Client secret** and put that into your `.env` file using `COMMENTO_GITHUB_KEY` and `COMMENTO_GITHUB_SECRET`

    ![Application created successfully](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_9-7505a3ef-386a-4b75-a7dc-1dd3e22d0baf.29.28_AM.png)

### Google

Setting up Google is just about as tedious to set up as Twitter. Despite how scary I just made it out to be, it's completely doable. Here are the steps.

1. Go to this URL: [Google Developer Console](https://console.developers.google.com/cloud-resource-manager?previousPage=%2Fapi)
2. Create a new project

    ![Create a new project](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-f3793926-cc54-4345-b81c-5ec0f4631a35.42.48_AM.png)

3. Click the **GoogleAPIs logo** in the top left corner to go back once you have a project. (Make sure the dropdown next to the **GoogleAPIs logo** is the same as your new project!)
4. Then, click **Credentials** on the left side.
5. Update the **Application Name** and **Authorized Domains** in the **OAuth consent screen**

    ![Setup application](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-d839a5c9-3368-4f18-b674-73b6e4e7c17c.47.15_AM.png)

6. Click **Create credentials** then **OAuth client ID**

    ![Setup credentials](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-201545f9-4d47-4e0c-ae9a-b40efdc35a4b.44.36_AM.png)

7. On the **Create OAuth client ID** enter the subdomain associated with Commento to **Authorized Javascript origins.** Then, enter the full callback URL. For example [`https://comments.jaredwolff.com/api/oauth/google/callback`](https://comments.jaredwolff.com/api/oauth/google/callback). Make it yours by replacing `comments.jaredwolff.com` with your URL.

    ![Create OAuth Client ID](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-fdba3491-d562-41f3-acff-2857ea816cec.52.15_AM.png)

    Once entered, click the **create** button.

8. Grab the **client ID** and **client secret**

    ![OAuth Credentials](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-0c3f2895-0cb9-4b3a-a154-a3d80fd9716a.57.40_AM.png)

9. Update your `.env` file using `COMMENTO_GOOGLE_KEY` and `COMMENTO_GOOGLE_SECRET`

## Install your application

You've entered your OAuth Credentials email, domain and SMTP credentials. It's time to wrap this show up!

1. Once you're done editing your `.env` file. Run `docker-compose up` (For files not named `docker-compose.yml`, use the `-f` flag. Example: `docker-compose -f commento.yml up`
2. Watch the output for errors. If it looks good you may want to kill it (**CTRL+C**) and run with the `-d` flag
3. On first start, Commento will prompt you with a login screen.

    ![Commento Login](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-d5a1ca53-93b3-49c5-a3a7-e8b728259e2d.11.29_PM.png)

4. Create a new account by clicking **Don't have an account yet? Sign up.**
5. Enter your information and click **Sign Up**
6. Check your email and click the included link:

    ![Validation email with link](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-e263aa4f-201b-42ac-986c-b28c5f003f38.12.48_PM.png)

7. Log in with your freshly made account.
8. Then, click **Add a New Domain.**

    ![Add new domain](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-46acfe9c-f3f4-4d3e-b8fb-97fbff643a86.10.47_PM.png)

9. Once created go to **Installation Guide.**  Copy the snippet and place it where ever you want your comments to live. In my case, I put the snippet in an area just after my `<article>` tag.

    ![Code snippet](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-f78f36c5-f3f7-45ec-971d-9bf0bf7b7d1f.36.35_PM.png)

10. Re-compile your site and check for success!

    ![Blog comment section with checkmarks](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-8f7ffbdc-c49f-49bc-95bb-1f53a926f361.30.27_PM.png)

    Checkmark! Finally, I recommend you try logging in with each individual OAuth configuration. That way you know it working for your website visitors. ?

## Alternatives

I spent a good chunk playing around with some of the alternatives. This is by no means a definitive guide on what will work best for your site. Here are some of the top ones as of this writing:

[https://utteranc.es/#configuration](https://utteranc.es/#configuration)

[https://github.com/netlify/gotell](https://github.com/netlify/gotell)

[https://github.com/eduardoboucas/staticman](https://github.com/eduardoboucas/staticman)

[https://posativ.org/isso/](https://posativ.org/isso/)

[https://www.remarkbox.com](https://www.remarkbox.com/)

[https://www.vis4.net/blog/2017/10/hello-schnack/](https://www.vis4.net/blog/2017/10/hello-schnack/)

[https://github.com/gka/schnack](https://github.com/gka/schnack)

There's also a huge thread over at the Hugo blog which has a ton more links and resources as well:

[https://discourse.gohugo.io/t/alternative-to-disqus-needed-more-than-ever/5516](https://discourse.gohugo.io/t/alternative-to-disqus-needed-more-than-ever/5516)

## Conclusion

Congrats! You are now hosting your own comments server! ?

In this article you've learned how to harness the power of Docker and a Nginx Reverse Proxy. As an added bonus, you know how to  set up OAuth credentials! That way future setup will be easy peasy.

By the way, this is only the tip of the iceberg. You can set up the same server for analytics, data collection and more. [All the example code including code for other applications can be found here.](https://www.jaredwolff.com/files/host-your-comments/)

Finally, if you're looking pay for Commento head to [www.commento.io](http://www.commento.io) and sign up for the service. You'll be supporting awesome open source software!

If you have comments and questions let's hear em'. Start the conversation down below. ???


