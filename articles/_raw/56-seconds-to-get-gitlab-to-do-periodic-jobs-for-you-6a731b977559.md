---
title: How to get GitLab to do periodic jobs for you in under a minute
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-06T00:15:49.000Z'
originalURL: https://freecodecamp.org/news/56-seconds-to-get-gitlab-to-do-periodic-jobs-for-you-6a731b977559
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HHVkCUSmaGkFPTx06jjZKw.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: GitLab
  slug: gitlab
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Moe Ibrahim

  What would technology be without a computer doing periodic work?

  Whether it’s your phone constantly checking your inbox for you, or getting timely
  alerts for weather or flight delays.

  What about a bitcoin vs Canadian dollar price servi...'
---

By Moe Ibrahim

What would technology be without a computer doing periodic work?

Whether it’s your phone constantly checking your inbox for you, or getting timely alerts for weather or flight delays.

What about a bitcoin vs Canadian dollar price service, in just 56 seconds? No _IFTTT_, no _Zapier_, but no programming languages either — and no frameworks, no server or docker configuration, no Raspberry Pi, no AWS and no tests!

To make the example as universal as possible, we will only use 2 command lines:

* one to GET the bitcoin price from an API
* and another to POST it to another service.

Of course you can make this more useful by posting the price to Twitter, Twilio, Telegram, Slack and so on. But here we will simply post it to putsreq.com so we can inspect the POST request.

Then we will use GitLab-CI to schedule it to run everyday.

> **Level** : All levels

> **Requirements** : Any web browser

Let’s get you started :

1. **Create a free account** at [gitlab.com](https://gitlab.com/users/sign_in) (20 seconds)

2. **Create a new Project :** Click on the **_New Project_** button to create a new repo, and in the name field type _periodic-job_ or any other name. (9 seconds)

![Image](https://cdn-media-1.freecodecamp.org/images/erHlPeiJTmeTnQ4GoFSMtoYLR5V0zseO60H8)

Then save it by clicking on **_Create Project_** (1 second).

![Image](https://cdn-media-1.freecodecamp.org/images/bzyB3KG6wmQ9Jc01n1FhAdyF6BBhCjC9pATv)

3. **Create a .gitlab-ci.yml file in this new project:** Click on **_New File_**, copy and paste the following snippet into the .gitlab-ci.yml file, then click save (5 seconds)

![Image](https://cdn-media-1.freecodecamp.org/images/ojeKxdcQUHLAGUO0y8g517nuss9rsKANxpt-)

![Image](https://cdn-media-1.freecodecamp.org/images/sFPB53USK5EYEvXza-ZyruSj0c9Qp3fx5-1R)

```
test:
```

```
 script:
```

```
 - btc=$(curl https://min-api.cryptocompare.com/data/price?fsym=BTC\&tsyms=CAD)
```

```
- curl -i -X POST https://putsreq.com/wkDdMQWhaOyalisaIe49 — data ‘price=CA$ ‘“${btc//[0-9\.]/}”
```

These are basically two simple commands. Here we can go further and add

[_if [ $btc -ge 15000 -a $btc -lt 7000 ]; then_](https://hackernoon.com/71-seconds-to-build-your-free-custom-webhook-illustrated-step-by-step-7a09b9e240ba)

conditions, or even run a full bash script file, but let’s keep it simple.

Click on the **_Commit changes_** button, and this will trigger it to build and run.

4. **Schedule it to run everyday:** click on the CI/CD icon to expand the menu, and select Schedules to set up a name and a timer for your periodic job to trigger. (11 seconds)

![Image](https://cdn-media-1.freecodecamp.org/images/LPe0diYgDp3FtDob-daYQgz9yQp3NIbpcaB8)

![Image](https://cdn-media-1.freecodecamp.org/images/myy9E9YueotL6uCnQzIj64S7WvNZgH0nSvI9)
_click on **New schedule** button_

![Image](https://cdn-media-1.freecodecamp.org/images/hORLN61TKEGqsCLm4Dus6l0mC0hEp1kDxc7i)
_Type in a name for the new schedule **daily-bitcoin-price-job**, select to run it daily then click **Save**_

![Image](https://cdn-media-1.freecodecamp.org/images/2dK2LU1YHfEwHK3Mhzs82VpHdR3uXncbyG-L)
_Your scheduled job has been saved_

5. Congrats! You’re done. Go to to [this link in putsreq.com](https://putsreq.com/wkDdMQWhaOyalisaIe49/inspect) to see it in action. (10 seconds)

![Image](https://cdn-media-1.freecodecamp.org/images/Yhx54rH7S8jocMDTd8NB0F6-RwySKIoDLT5Y)

This job will run everyday as long as your free 2000/month build minutes do not run out.

We haven’t even scratched the surface of what we can do with GitLab-CI — just think of all the possibilities of using it to create webhooks or [connecting it to IFTTT](https://medium.com/@YYC_Ninja/99-seconds-to-make-bitcoin-call-your-phone-number-a8cbd9740f76) and Zapier, which in turn would connect it to hundreds of services.

In [the next article](https://medium.com/@YYC_Ninja/71-seconds-to-build-your-free-custom-webhook-illustrated-step-by-step-7a09b9e240ba) we will go through what we have just done, and how we can take it up a notch and create a webhook and use it to post to social media.

You can find the [sample code here](https://gitlab.com/ninjayoto/my-periodic-jobs/tree/master), and you can read the [build logs here](https://gitlab.com/ninjayoto/my-periodic-jobs/-/jobs).

