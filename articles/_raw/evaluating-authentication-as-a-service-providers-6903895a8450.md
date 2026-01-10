---
title: How to choose the best Authentication as a Service Provider for your company
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-14T23:43:50.000Z'
originalURL: https://freecodecamp.org/news/evaluating-authentication-as-a-service-providers-6903895a8450
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GiwpKyF5sjUV3ObYeEjkrg.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jeff Okawa

  Have you ever wondered how to choose an authentication service provider?

  We are amid a growing trend of using federated identifiers to provide authentication
  to the websites we use everyday.

  We can log in to countless applications using...'
---

By Jeff Okawa

Have you ever wondered how to choose an authentication service provider?

We are amid a growing trend of using federated identifiers to provide authentication to the websites we use everyday.

We can log in to countless applications using our social media accounts, our work accounts all have SSO capabilities, and we can even log into government websites using our online banking credentials.

Conceptually, authentication (and SSO) is simple, but it’s hard and costly to implement correctly. Though businesses have traditionally focused on building features, now in reality they also must focus on lowering user registration contention without exposing the application to vulnerabilities. Just like how cloud infrastructure platforms (like AWS) now allow businesses to focusing on building apps, we see the same happing with authentication.

Authentication as a Service (or authentication service providers) provide authentication and user management services for applications.

They are not just an identity provider, but provide configurable user login pages (or widgets), logout functionality, federated identities with social media accounts, user databases, and some degree of user management. They have out of the box capabilities to support common authentication protocols such as SAML and OpenID Connect.

Enterprise customers desiring SSO can often take advantage of easy one-click setups with third-party applications like JIRA, Office 365, and Salesforce though the use of SAML2.

#### What are your Goals?

At times, implementing authentication systems for an application can feel like reinventing the wheel. The concept of authentication as a service (AaaS) attempts to solve this problem, but there are things to consider before choosing a provider (or deciding to roll out a custom solution).

![Image](https://cdn-media-1.freecodecamp.org/images/690m1zOxXGxOynRY0yzJ23OehrWIdOoAWWok)

### Criteria

![Image](https://cdn-media-1.freecodecamp.org/images/BCWmPrRoCmu6GKPSRAXX-n0UBeG9muMmGHLM)

Once you’ve come up with a list of important considerations for your organization, it is time to start evaluating the authentication as a service providers (AaaSp’s) in the market. In the last few years, we’ve seen an number of AssSp’s enter and disappear. This makes choosing the right AaaSp that much more critical. They come in all shapes and sizes — from small firms with little clients to large established enterprise venders.

### Trust and Reputation

Entrusting something as important as authentication requires a considerable amount of confidence, so it’s important that the chosen vender should be **reputable** and a **trusted** **authority** in authentication. Consider if their architecture has been reviewed by other security experts and review any online commentary about the provider.

As we have seen with Stormpath (purchased by Okta in 2017, then dropped the Stormpath API), relaying on a third-party vendor opens the risk of _vender_ abandonment. In the worst case, as it was with the acquisition mentioned above, many were left with no migration path from Strompath to Okta and were required to roll out their own authentication systems.

Vender size, client list, and company profile are general guidelines that can be taken into consideration, but you are still taking a risk. Smaller start-up providers can offer significant incentives, but their ability to disappear quickly without proper notice can make them a risky choice. Alternately, larger providers can still shutter their services if that line of business becomes no longer profitable.

### Intended Users

Some AaaS providers, such as One Login, focus exclusively on B2E — providing an SSO experience for a company’s internal employees with their web-based services. Think of company portal pages with links to HR resources, the company Wiki, Sharepoint, and Salesforce. Auth0 and AWS Cognito are providers serving both B2E and B2C and explicitly support clients who have hundreds of thousands of customers.

### Vender Lock

Integrating with a AaaSp introduces a more significant amount of interdependence then just integrating an application stack onto a cloud-based solution, because provider-specific code **must** be written to complete the integration.

Not only does this have to be undone, but more integration code for the new provider will have to be written. Moving from an AaaS to rolling out a custom solution is even more costly, since everything would need to be written from scratch.

Unlike infrastructure changes, where mitigation stargates exist to reduce user interruption, swapping AaaS providers will almost always impact users. Remember, we’re changing components that directly interact with end-users.

**Data Import**  
Most AaaS providers define a mechanism of importing users into their system by bulk import (where users must go through a password reset flow) or gradual migration process. With the gradual migration, user credentials are first validated against the old database and then encrypted and stored in the new database. In this use case, users are not impacted by the migration.

**Data Export**  
This feature is especially important in the case where applications make use of the AaaS’s datastore. For security reasons, AaaS providers do not publish their password hashing algorithm. Therefore, when an export is required, all users must initiate a password reset flow.

If that doesn’t sound bad enough, many AaaS providers **DO NOT** provide a bulk data export feature, thus adding extra complexity and manual steps to migrate user data out of an AaaS.

**Sub Contractors**  
Some services offered by AaaS providers are fulfilled by yet another third-party service. 2fa/mfa and email are sometimes features which require separate registrations (and additional payment) with the third-party.

Taking 2FA as an example, some AaaS services do not allow you to choose the underlying 2FA provider and force you to use their preferred vender. Not only are you forced into a partnership with that vender, but you are also forced to pay their rates (where cheaper alternatives are sometimes available).

### Technology Support

**Protocols**  
Most AaaS providers support the major federated protocols (OpenID Connect and SAML). Others have additional connectors allowing for customized data sources (Microsoft AD or LDAP) and easy setups to third-party applications like JIRA, Office 365, and Salesforce though the use of SMAL.

**Integration**  
Integration of the AaaS’s service into your application can still be a significant task (especially if you are running a legacy application). Therefore, one consideration is to see if the AaaS offers libraries for your technology stack.

For example: Most major AaaS providers along with social media websites provide client libraries to request, consume, and validate various authentication tokens and documents. If you are running a Java stack, many services offer Java libraries to include with your project for any backend processing. If your stack is supported, the integration process can be as simple as dropping in a JS file, including a JAR, and filling out some values in a property value.

**Documentation**  
Ample, well-written documentation and community support will go a long way to make integration easier. Some providers offer seed and sample projects to get you started.

**Other Features**  
Many services offer add on features such as user profiling, email, and 2fa/mfa.

### Customizable User Interfaces and Flows

AaaS providers allow varying levels of customization for UI pages, widgets, and user attributes. In addition, some systems have “hooks” where customization of flows can take place (checkout Auth0 and AWS Cognito for more detail).

Depending on your specific organization, it can be difficult to strike the balance between meeting UX wants and what is customizable (within reason) by the provider. In some cases, business requested flows may not be supported by your chosen AaaS.

#### A note about customization:

Ready out-of-the-box authentication capabilities are one of the great benefits of using an AaaSp. When the pre-built components are used, integration is incredibly simple.

On the other hand, heavy customization of the UI and flows increases time and complexity. You may find yourself so heavily and extensively customizing the UI and authentication flows that you **must** question if it will be _cheaper_ to roll out a custom in-house solution (also considering the yearly cost). The answer might be **YES**.

My recommendation is to withhold as much customization as possible within the AaaS framework. This is especially the case when it comes to the authentication and password reset flows, as adding customization to these components tends to increase the complexity of integration and create vendor lock-in.

### Development and Testing Support

#### Development, QA, and Production Environments

Some companies have isolated development and QA environments. To support these requirements, _some_ AaaS providers allow a single account to have multiple identity databases. This unfortunately, is not a universal feature and multiple accounts with the AaaS may be required to support each testing environment.

#### Load Testing

All AaaS systems prohibit unauthorized load testing. This may be a problem if your application requires an end-to-end load test to be approved for production. In this case, some AaaS providers do allow load testing if it is pre-authorized prior to the test taking place. There are often stringent constraints and timeframes the test must be run under.

More realistically, you will probably have to implement a login by-pass mechanism for the application to support load tests.

### Pricing

Pricing models vary significantly between AaaS providers. Some providers have incentives for small start-up organizations and have a free or very affordable lowest tier. Generally speaking, expect to see a price/user graph like the following:

![Image](https://cdn-media-1.freecodecamp.org/images/IYF8Igkb7oZ3CSnlFjfhfYDl4i3T8varqj4L)

Price per user is initially very low (or $0), which is great for small organizations or start-ups with low volumes. However, as your user base grows, price/user stays consistent. Eventually it will start to decrease after a certain point, because you’ve either reached the highest usage tier or are in a position to negotiate prices.

The cost may seem reasonable as you start off, but once you are locked in, an application with 100,000 active users in a month could see a yearly bill of 150k to 200k!

If your application already has a user base of several hundred thousand users, it might be cheaper to roll out your own solution! In addition to the per-user fees, there are often fees for additional services you may incur (again, 2fa and email).

**B2C**  
Negotiate price if your application has heavy use periods. Some services have variable pricing per moth based on number of actual active users, while others fix the price per month based on an estimate of the heaviest month throughout the year (regardless of how many users actually use the system). The difference between these price plans can be significant.

**B2E**  
Prices are always set at an amount per employee account. Beware of minimum fees in the fine print!

#### User Management and Dashboard

Most AaaS’s have some form of basic user management built into their admin dashboards. In some cases, you can create non-admin accounts for your customer service reps or other associates to make changes to user identities.

Giving out full-admin accounts to employees simply so they can have access to the user management dashboard should be **avoided**. The admin account should only be in the hands of the appropriately trained employees, otherwise you run the risk of someone accidentally deleting your entire user database or exposing user identities.

Whether or not the built-in AaaS dashboard supports your needs is specific to the day-to-day user attribute changes your organization needs to make. Make sure the AaaS provides an appropriate audit tracking/logging trail as per your organization’s policies.

### SLA and Customer Service

A direct contact with an account manager of the provider is not offered across all AaaS providers. Free or low-usage tiers often only get access to community forums. Some providers offer paid support, dedicated servers, access to logs, and HIPAA/PCI compliance at an additional cost.

Most AaaSp offer the standard 99.9% to 99.995% SLA uptime, but this still allows for downtimes during the year. This can be of importance if your application **must** be up during critical periods. Some AaaSp’s offer enterprise solutions (custom deployments) to ensure some form of redundancy in case of a system failure.

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/H3CZpMrLwvZuPRuzkW1jyGYnok2JCK7luv8c)

For start-ups, AaaSp’s provide an affordable solution for authentication so you can focus on your product. For larger organizations with legacy applications and an established user base, you must take into consideration a much broader list of criteria to make sure you select the AaaS that suites your migration, auditing/logging, and budget needs.

As a follow-up, I’ve [written a introduction to federated identities and authentication](https://medium.com/@dev78digital/655a160d66cb).

