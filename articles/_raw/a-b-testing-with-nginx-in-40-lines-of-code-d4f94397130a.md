---
title: A/B testing with NGINX in under 40 lines of code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-14T20:26:42.000Z'
originalURL: https://freecodecamp.org/news/a-b-testing-with-nginx-in-40-lines-of-code-d4f94397130a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vW7X8V-kG0TVtdIwmHw7hQ.png
tags:
- name: nginx
  slug: nginx
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nitish Phanse

  A/B Testing, has enabled designers and product managers to get a deep insight into
  user behavioral patterns.

  On the one hand, it has allowed product managers more flexibility while conceptualizing
  user journeys. But on the other, it’...'
---

By Nitish Phanse

A/B Testing, has enabled designers and product managers to get a deep insight into user behavioral patterns.

On the one hand, it has allowed product managers more flexibility while conceptualizing user journeys. But on the other, it’s become a developer’s nightmare, being told to make two versions of the same component.

> “The general concept behind [A/B testing](https://en.wikipedia.org/wiki/A/B_testing) is to create an experiment with a control group and one or more experimental groups (called “cells” within Netflix) which receive alternative treatments. Each member belongs exclusively to one cell within a given experiment, with one of the cells always designated the “default cell”. This cell represents the control group, which receives the same experience as all Netflix members not in the test.”

> - Netflix blog

#### What does the present ecosystem offer?

A lot of companies like Mixpanel, VWO, and Optimisely provide client SDKs (JavaScript code) which have to be added in the `head` tag of the page HTML. The tests can then be created via a dashboard.

Although the above methods give you a lot of options when it comes to button colors, component height, and other CSS attributes, it doesn’t really allow you to create two separate flows altogether.

Also, some external libraries can really hamper your page load times and can create a jittery/laggy experience for users.

### Presenting NGINX

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lqqzohxt5sznYqtnrAh09w.png)

[Nginx](https://nginx.org/en/) is a light web server that offers a bunch of functionality like load balancing, reverse proxying, and HTML compression. It’s easy to setup and really offers a lot of control to developers.

NGINX is a terrific tool for distributing traffic for split tests.

It’s stable, it’s blazingly fast, and configurations for typical use cases are prevalent online. More complex configuration can be accomplished after just a couple hours exploring the documentation. Small companies may not have resources to spend on paid software for A/B testing, but NGINX provides an option to carry out some form of A/B testing.

For example, say you want to see which of the forms below will have better conversion:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ny7aOxNtdXE88Ax8Q7B8eA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*I6fuPkJm2zwhYcYDE-4f1w.png)
_Version A and Version B respectively_

Your hypothesis might be that fewer form fields imply less data being inputted by the user, thus leading to more conversions.

So we can define two buckets: Version A and Version B. The former is the control group, which is shown to 80% of the traffic. The latter is the test group, which forms the remaining 20% of the traffic.

Port 7770 will host one bucket of the code, whereas port 7777 will host the second bucket of the code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pficodfp_HU6MW87VL3N6g.jpeg)

### Code

Your nginx.conf file can be modified as shown below.

```
http {    # ...    # application version 1a    upstream version_a {        server server 127.0.0.1:7770; ## Can be an external ip too    }
```

```
    # application version 1b    upstream version_b {        server server 127.0.0.1:7777; ## Can be an external ip too    }
```

```
    split_clients "app${remote_addr}${http_user_agent}${date_gmt}"   $appversion {        80%     version_1a;        *       version_1b;    }
```

```
server {        # ...        listen 80;        location / {            proxy_set_header Host $host;            proxy_pass http://$appversion;        }    }}
```

Create two upstreams, one for each bucket.

The `split_client` directive helps us divert traffic along with the specified weightage to a particular upstream.

The `app${remote_addr}${http_user_agent}${date_gmt}appversion` creates a hash based on the above parameters and is used by nginx to log a request made to either bucket. Preferably these parameters are those which are pertaining solely to a user, like `user_agent`, `remote addr`.

Ok — so this will work, but it doesn’t give the user a persistent experience.

If I refresh my page, there is a chance I’ll switch between buckets, and this can be a horrid user experience.

Consider the above case: imagine trying to fill a six field form, and then suddenly, on refreshing, seeing a two field form. Confusing!

### A different approach

1. Proxy pass request to either bucket
2. Set a cookie with an expiration time equal to duration of test.
3. Check for cookie existence and proxy pass to correct bucket to ensure a uniform user experience.

We will use NGINX’s `map` directive and map the `$cookie_name` variable to different buckets that we have created.

```
http {    # ...    # application version a    upstream version_a {        server server 127.0.0.1:7770; ## Can be an external ip too    }
```

```
   # application version b    upstream version_b {        server server 127.0.0.1:7777; ## Can be an external ip too    }    split_clients "app${remote_addr}${http_user_agent}${date_gmt}"     $appversion {        80%     version_a;        *       version_b;    }
```

```
    map $cookie_split_test_version $upstream_group {        default $appversion;        "version_a" "version_a";        "version_b" "version_b";    }
```

```
server {        # ...        listen 80;        location / {            add_header Set-Cookie "split_test_version=$upstream_group;Path=/;Max-Age=518400;";
```

```
            proxy_set_header Host $host;
```

```
            if ($upstream_group = "version_a") {                proxy_pass http://127.0.0.1:7777;                break;            }
```

```
          if ($upstream_group = "version_b") {                proxy_pass http://127.0.0.1:7770;                break;            }
```

```
          proxy_pass http://$appversion;        }    }}
```

As it’s a little hard to format the above code…

![Image](https://cdn-media-1.freecodecamp.org/images/1*LekfEbjABlUcQ05aDIoAug.png)

### Conclusion

1. NGINX provides a very simple API to create an A/B test environment.
2. Allows for multiple buckets to be created. The example above shows two buckets, but we can split traffic and create more buckets.
3. As the same code is hosted on two ports, deployment can become tricky (presently I have two branches: a master and a test branch), whether done off a different branch or from the same one.
4. Carrying more than one A/B test can become tricky. Yes, you can use the `location` directive and set different cookies based on the required tests, but having two tests (_Test 1, Control: 80, Test 20 & Test 2 Control: 50, Test 50_) is impossible. That said, you should not have more than one A/B test at a time per page. Otherwise you will end up having 2^n versions of your page, where n is the number of tests, and tracking conversions will be hell.
5. Tracking can now be done at a very granular level as the code bases are effectively separate.

Do let me know if I’ve made any mistake in the above. Happy to correct and learn. Hope you liked the article.

**PS: Did anyone notice it is less than 40 lines of code?!**

