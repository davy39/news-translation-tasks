---
title: How to Use Cookies to Customize a Web Page's Content
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2023-05-30T22:04:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-cookies-to-customize-web-page-content
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/vyshnavi-bisani-z8kriatLFdA-unsplash.jpg
tags:
- name: cookies
  slug: cookies
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "If you develop websites or web apps, someday you’ll have to deal with cookies.\
  \ That’s why I decided to write this tutorial on how to use cookies to customize\
  \ a web page according to the previous web page the user comes from. \nI wrote this\
  \ tutorial us..."
---

If you develop websites or web apps, someday you’ll have to deal with cookies. That’s why I decided to write this tutorial on how to use cookies to customize a web page according to the previous web page the user comes from. 

I wrote this tutorial using PHP, but you can set cookies also by using other popular programming languages such as Java, Python, and others.

Before going deep with the details, let's go through a brief introduction and some recommendations.

## What are Cookies?

Cookies play a vital role in how websites function. They can also enhance a user's browsing experience. 

In simple terms, a cookie is a small file that websites store on a user's computer or device while they navigate through various web pages. These files contain data that are utilized by websites to remember certain information and settings, ultimately improving the performance and customization of the website for the user.

When a user visits a website, the site's server sends a cookie to the user's browser, which then stores it on their computer or device. The next time the user visits the same website, the browser sends the stored cookie back to the server. This enables the website to recognize the user, remember their preferences, and provide personalized content.

Cookies serve various functions, such as remembering login information, language preferences, and shopping cart contents. 

For example, when you visit an online shopping website and add items to your cart, cookies help in retaining those items even if you navigate to other pages. Cookies can also remember your login details, so you don't have to re-enter them every time you visit a website.

Cookies can also be used for tracking user behavior and gathering information about website usage. This information is often anonymous and helps website owners analyze traffic patterns, identify popular pages, and improve their website's design and functionality. 

Advertisers also use cookies to deliver targeted advertisements based on users' browsing habits and interests. This enables them to show relevant ads that are more likely to be of interest to the user.

### A Note about Cookies and User Privacy

Cookies are designed to be a tool for enhancing user experience and improving website functionality. But concerns about privacy and security have led to the development of regulations and guidelines for using cookies. Many websites now provide cookie consent notices, allowing users to choose whether they want to accept or reject cookies.

Over the past few decades, the use of cookies has been subject to extensive discussion by regulatory bodies, emphasizing the significance of ensuring users are fully informed about their implementation. 

Progress has been made in this direction, including the introduction of the General Data Protection Regulation (GDPR) by the European Union (EU). For more comprehensive information, you can get detailed insights from the official web portal of the EU. 

If you are considering the integration of cookies into your application, I highly recommend discussing the implications with the legal department of your company or consulting with legal professionals who possess expertise in this domain. By doing so, you can ensure compliance with the legal and regulatory frameworks governing the use of cookies, safeguarding user privacy in the process.

## Let’s Get Started

Let’s assume I’m running a pet lovers e-commerce site, and I’m implementing a content marketing strategy to attract new customers. 

I create one informational page for cats lovers and another one for dogs lovers. Both pages point to the same page where I give further details about having pets. 

I want this page to show specific (targeted) ads according to the page the user comes from: if they visited the page about cats, I want them to see ads about cat food. If they visited the one about dogs, I want them to see ads about dog food.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-124.png)

## Let’s Code

I’m building three pages:

1. Cat's lovers page: mainPageCat.php (screenshot below)

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-125.png)

2. Dog's lover page: mainPageDog.php

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-126.png)

3. The target page: cookieTest.php

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-127.png)

While building pages 1 and 2, I set cookies using the PHP `setcookie()` function. For the page about cats, I pass the function these parameters:

```php
<?php
$cookie_name = "cat";
$cookie_value = "catFoodAds";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
?>
```

For the page about dogs, I pass these parameters:

```php
<?php
$cookie_name = "dog";
$cookie_value = "dogFoodAds";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
?>
```

For the “further information” page I add some logic. If the cat cookie is stored, I add a CSS class to the dog ads card to hide it. I do the same with the cat ads card if the cookie stored is the one from the dog page.

```php
<div class="row">
			<div class="col-md-3">
				<div class="card <?php if(isset($_COOKIE['dog'])) echo ' cookieClass'; ?>" style="width: 18rem;">
					<img class="card-img-top" src="https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDl8fHxlbnwwfHx8fA%3D%3D&w=1000&q=80" alt="Card image cap">
					<div class="card-body">
						<h5 class="card-title">Buy Food for Cats</h5>
						<h6 class="card-subtitle mb-2 text-muted">Excellent Food</h6>
						<p class="card-text">Don't know what else I could say about cat food.</p>
						<a href="#" class="card-link">Buy</a>
					</div>
				</div>
			</div>
			<div class="col-md-3">
				<div class="card ml-5 <?php if(isset($_COOKIE['cat'])) echo ' cookieClass'; ?>" style="width: 18rem;">
					<img class="card-img-top" src="https://images.unsplash.com/photo-1561037404-61cd46aa615b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxjb2xsZWN0aW9uLXBhZ2V8MXwxMTU1Mjc2N3x8ZW58MHx8fHw%3D&w=1000&q=80" alt="Card image cap">	
					<div class="card-body">
						<h5 class="card-title">Buy Food for Dogs</h5>
						<h6 class="card-subtitle mb-2 text-muted">Excellent Food</h6>
						<p class="card-text">Don't know what else I could say about dog food.</p>
						<a href="#" class="card-link">Buy</a>
					</div>
				</div>
			</div>
		</div>
```

## Let’s see how it works

I test the flow as a user who wants to visit the page about cats. I type in my browser URL bar:

https://<base_url>/mainPageCat.php

As you can see, I see the page I built and the cookie is stored in my browser

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-128.png)

If I click the call to action (blue button), I see the further details page with cat food ads only:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-129.png)

Let’s now test the flow for dog lovers. First I delete cookies from my browser (or use the incognito mode) and then I visit this URL:

https://<base_url>/mainPageDog.php

This is what I see:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-130.png)

As we can see again, I see the page I built and the cookie is stored in my browser

If I click the call to action (blue button), I see the further details page with dog food ads only.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-131.png)

Done! This is a simple and quick example of how you can use cookies to customize the content of your web pages. You can find the Github repo [here](https://github.com/mventuri/cookiesPhp) with the full code.


