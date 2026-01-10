---
title: How Feature Flags and Role-Based Access Control Can Help Secure Your DevOps
  Process
subtitle: ''
author: Kayode Adeniyi
co_authors: []
series: null
date: '2024-04-22T21:26:27.000Z'
originalURL: https://freecodecamp.org/news/feature-flags-and-role-based-access-control-devops
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/pete-alexopoulos-IssFEVzKV1w-unsplash.jpg
tags:
- name: Devops
  slug: devops
- name: Security
  slug: security
seo_title: null
seo_desc: "These days, software is being developed and deployed at a very rapid pace.\
  \ It makes it easy to understand how the saying “move fast and break things” became\
  \ commonplace. \nIn an era where agile development is the go-to practice for quick\
  \ feature relea..."
---

These days, software is being developed and deployed at a very rapid pace. It makes it easy to understand how the saying “move fast and break things” became commonplace. 

In an era where agile development is the go-to practice for quick feature releases and feedback, it's easy for security and compliance to get overlooked. This may be securing CI/CD pipelines, protecting user data, or managing access to feature flagging in production environments. 

Though the tech industry is aware that strong security measures and compliance practices are essential in DevOps, sometimes these measures take a back seat behind the need to get code shipped to production.

Because of this, it's crucial that you understand the importance of security and compliance in DevOps. You should also learn how your team can leverage popular security concepts like Roll-Based Access Control (RBAC), which is what we'll focus on here. 

This is useful not only for DevOps teams (as a compliant practice for assigning access to teams), but also as a full-fledged feature that SaaS platforms such as [Flagsmith](https://www.flagsmith.com) (an open source feature flagging platform) provide to their customers.     
  
But you might ask – why is RBAC important? Well, we'll cover that and more in this tutorial.

## Table of Contents:

1. [Why is RBAC Important?](#heading-why-is-rbac-important)
2. [Feature Flagging and Flagsmith](#heading-feature-flagging-and-flagsmith)
3. [Understanding Users, Groups, Roles, and Permissions](#heading-understanding-users-groups-roles-and-permissions)  
– [Create the project](#heading-create-the-project)  
– [Create the group](#heading-create-the-group)  
– [Create an Editor role](#heading-create-an-editor-role)  
– [Assign permissions to the Editor role](#heading-assign-permissions-to-the-editor-role)  
– [Assign the Editor role to a group](#heading-assign-the-editor-role-to-a-group)  
– [Test the assigned permissions](#heading-test-the-assigned-permissions)
4. [Use Case: the Chaos at "NetGlobal Solutions"](#heading-use-case-the-chaos-at-netglobal-solutions)  
– [How to mitigate the issue](#heading-how-to-mitigate-the-issue)
5. [How to Establish a Standard DevOps Process](#heading-how-to-establish-a-standard-devops-process)
6. [Wrapping Up](#heading-wrapping-up)

## Why is RBAC Important?

Keeping it simple, role-based access control is a fundamental requirement for DevOps. If you don't implement RBAC, your user's data is at a much greater risk of compromise. This can lead to financial losses and damage to your site's reputation. 

So to reduce the attack surface and avoid damages, DevOps teams should leverage all security mechanisms at hand, [such as RBAC](https://www.redhat.com/en/topics/security/what-is-role-based-access-control). RBAC is pretty much what it sounds like: giving people on a team permissions based on the role they play within the organization.

This helps secure not only the lifecycle of a feature released in production but also how it is managed after the release – should it be enabled or disabled? Which users should be able to use it? And who will be responsible for performing this operation? 

This is where feature flagging and the need for a platform that manages these security concerns come into play.  
  
What is feature flagging anyway and why is RBAC important to manage it?

## Feature Flagging and Flagsmith

Feature flagging is a software development concept that involves enabling or disabling a feature independent of redeploys or source code changes. 

[Feature flags](https://www.martinfowler.com/articles/feature-toggles.html) are conditional statements in the application code that determine which section of code to execute on runtime based on a boolean value. They help deploy new features to production and provide granular control over their visibility to a user base or deployment environment.   
  
You can configure feature flag values by various methods, such as config files, request headers, or from the database. This means that there's a certain amount of necessary developer intervention in this process. And anyone with access to the code or database can enable or disable a feature in production. 

Although companies have compliance practices to handle feature flagging, there is always a chance of someone doing something that could harm production (intentionally or unintentionally). 

So, to give you and your team better visibility and fine-grained control over feature toggling, feature flagging tools such as Flagsmith help you address such security and permission issues. 

But you might be wondering – how does Flagsmith manage permissions and users? Enter **[RBAC](https://www.flagsmith.com/role-based-access-change-control-security)**, which is built into the Flagsmith toolset. This makes it easier for larger teams to collaborate across projects and environments, and for companies to manage access. Let's dive deeper to understand how it works.

## Understanding Users, Groups, Roles, and Permissions

Flagsmith has two primary roles in the RBAC system: organization administrator and simple users. 

Organization administrators enjoy the privilege of having superuser capabilities, whereas regular users require explicit permission to access the needed resources. Flagsmith also lets you control permissions for numerous users in a group. This makes access management easier for larger teams that are divided up based on responsibilities.  
  
There are also certain roles in Flagsmith RBAC that can have a permission set attached to them. This enables people with these roles to access particular features of Flagsmith. 

Roles come in handy especially when you need to assign bulk permissions to a group. In this case, you can create a role, assign permissions, and attach it to a group.   
  
If we look at permissions from a macro level, we can see that Flagsmith has divided the permission set into three different levels: Organization, Project, and Environment. 

For instance, we can manage permission sets for users to create projects at the organizational level. At the project level we can get access to environment creation, audit logs, and feature and segment management. Lastly, we can manage feature flags, segments, identities, and more on the environment level.

Before we move on to a case study, let's create an arbitrary project on Flagsmith and give permissions to a user so they can start creating feature flags for the project. We will perform the following actions:

* Create a project inside an organization
* Create a group “front_end_devs” and add users to this group
* Create an editor role
* Assign organization, project, and environment level permissions
* Assign the role to the newly created group
* Login in with the user account to test assigned permissions

### Create the Project

Click on the Create Project button after logging in with an owner account. We'll name this project **Dev Test.** 

![Image](https://lh7-us.googleusercontent.com/Gk4FaR8EecQ2vlUipL3KiIVENZnQuEkTX9n0FL9szgQJuHzXuZEfduIQ2oYnDst46yc0zVAubcgq0i0L32Q12jNEsbcIQep9X_5sVde_tXgJ8OcCbOCZOHDm3ThruWbEHZBXo2E9G7hiE0CpJgfiECM)
_Create the project_

### Create the Group

Navigate to the **Members** tab, click Create Group, then fill in the required details.

![Image](https://lh7-us.googleusercontent.com/gGa6rP_qH9pyoOL0vh3T5euQfpDUq7gmoPGnEJfBzlynt8rc1vTmfErCfgidTZrLfVCMeMhor69wrJKzqdqZpOx_bC6T2Wp9hkCo93zZvXElCplrgpCT6k-n9N8jq6nd9Ov7cwK3bLPvVk3aPn7tpWs)
_Enter the information for creating a group_

We created a group “**front_end_devs**” and made John Smith the group admin. Consider this as an inline permission while creating a group. John can now manage the users inside this group.

### Create an Editor Role

Click on **Roles** next to **Groups**, and create a role called “**Editor**”.

![Image](https://lh7-us.googleusercontent.com/5zlCc-KmGxUNu069Tv-WQeibL7P-gnAMnTO6JoswreHIAy-jZip4Ym5svznawtNQZIJS-Tkn6XiXyHi3hJehtGJN3QyOwzx82EMYF0WbpSo9kKawhcEroeKxoSkdNe9suxvIqmee9-JjPQFt1GCHbhw)
_Creating an editor role_

We created the role called Editor, so now let’s assign the appropriate permissions to this role. The Editor will be given permissions at all three levels – Organization, Project, and Environment.

### Assign Permissions to the Editor Role

To assign permissions, click the name of the role you just created. You will see a sidebar on the right side with a permissions tab. We'll assign permissions for all levels, starting from the Organization level.

![Image](https://lh7-us.googleusercontent.com/se3FjEfVwxJEAnOI2PZGFVcCUk9a1OhtUVWxnqOb2oPgwJV_m08fWZoHjanZkCUMqr_DFUHpIp4RTphmRBWAybeZpGX6asEKDIu8TD8LvQEnbSOkQhchMfygcdMwymQRV0DxSVjeS6y4YqUW7YmEJls)
_Assigning permissions starting at the Organization level_

This Editor role can now create projects in this organization and manage the groups and their members in this organization.

Next, we give it Project level permissions. Click on the project name under the Project tab, and do as shown in the screenshot below:

![Image](https://lh7-us.googleusercontent.com/WKCBnmjb_r458FNPXVt-7Lp9lAAJpwnl8q5YLXLU709HDMDa81b047oe-FPElWOz41Z5MwVP8wrO4LPXZYALEO2gc0p46lPhp9cp8yDJWYGzqb1KCs63Aq_dT57fIPEzM4ZOLe2N9-XbAfH61-7dRGE)
_Assigning project-level permissions_

As you can see, we assigned this role two project-level permissions: **View Project**, and **Create Feature**. So any user or a set of users with this role will only be able to view a project and create a feature.

Now for the most granular permissions, which are at the environment level. Click on the Environment tab, choose the Dev Test project from the dropdown, and click on the Development Environment.

![Image](https://lh7-us.googleusercontent.com/bX6kJwrSeL4EB_rfgwtF3FQlRFE3nqysci5BTEqwSS-i4ypmXUk4g2Dib1MrkMEsIjTYM8ClNT0y8NGa2p3-Q-R1afP4zvLuTtnN0NAoG9HXW8Vs2sx5tde44DJ9GuoaQX5Ucs6qdPZ5IY9plWWWScA)
_Handling Environment level permissions (the most granular)_

As you can see, we assigned this role two environment-level permissions: **View Environment**, and **Update Feature State.** Any user or a set of users with this role will only be able to view an environment and update its feature state value in the project.

### Assign the Editor Role to a Group

Now we will assign this role to the “**front_end_devs”** group. To do this, select the editor role, go to the Members tab, then click the text “**Assigned Groups**”. Enter the name of your group in the search bar, and select it.

![Image](https://lh7-us.googleusercontent.com/7-j0MWNj30Y4GEplEcCDKkuzrE4xBkwlckPvev5lMCHHWTwvyL6J6ulUNIiGTtREnWdkJIyi8PPa4ZAXFsjrxMadysh9-nmcT5rwJNux-14LCU-BP7gHhzJKMz75kY0yrFHCVZDqk9eklEYCSu7a_G4)
_Searching for groups to which to assign the Editor role_

### Test the Assigned Permissions

After going through the above steps, users in the “**front_end_devs”** group should only be able to perform the following operations

* Create a new project and manage its groups (Organizational level). Being the creator of a new project, the policies assigned to that user for another project will not be applicable here.
* Create and Delete Features in Dev Test Project
* Update feature state values in the Dev Test Project 

Now we log in from John Smith’s account, a testing user from the “**front_end_devs”** group, to verify the assigned permissions are working properly. 

First, we will check the organizational level permissions which lets us create a new project.

![Image](https://lh7-us.googleusercontent.com/97YU-J_iusUdPt_IR5KrKrxHqIMsATZ559sUykWlS2q1M_o2RAsUKWkeZaONNc606gsc4rTltj5bvGRaIcN_xAPQmo7IYxms5K2mxOoOE5lyrg1_WuvDZ6oLUysj26EqVzrulBUcAkMfjgvFXUvDS6o)
_Checking organizational level permissions_

You can see that the user was successfully able to create a new project. And since he is the creator of this project, John is the admin and has full authority to manage it. 

Now we can test the permissions for the Dev Test project. Just click on the project name from the left-hand dropdown list and switch between projects. You will surely notice that in the left menu bar, you only have access to the development environment. This is due to the environment-level permissions we assigned to the Editor role. 

To create the feature just click on the Create feature button, give the feature a name, and enter a value of your choice.

![Image](https://lh7-us.googleusercontent.com/JgFC5AAlw_KJy6vnKARWlCkugkiy79k2mB4QxkpRfE37DOfozKYhuNpInPnG0c8tEm6Tum70_ImXIcOGEJsXPRdsbs_6sD9Y8U5U1PtAzVzWEemZf5XWU18i1U84DtLPUzV-Grlf0vrbOP_XfPudjGY)
_Creating a feature_

You will see something like this after the feature creation:

![Image](https://lh7-us.googleusercontent.com/-YVJ1FAeV5LUuBe6myfqcwFgE3FufIdU56-7RwE-wml4ZD4tVY9UrMUsVW-daXuiAfA7xsp7oDuM0fcboHLN-A9dGxan47wgbaNL5bb91Mk2cn80QIggoF3QWfUHPBzx7tD_KCkzYFaszjjfp3MrtnU)
_After creating the feature called `johns_feature`_

Now you should have a basic understanding of how Flagsmith’s RBAC handles permission assignments and manages users, groups, and roles. 

To help you get a holistic view of things and understand how implementing Flagsmith for feature flagging can minimize chaotic incidents in production, let's consider a use case.

## Use case: The Chaos at “NetGlobal Solutions”

Let's hypothesize that there's a company called NetGlobal Solutions, a global giant in the network industry. They provide various networking solutions to their customers, such as CDN, DNS management, geo-location, cloud cybersecurity, and DDoS mitigation.  

They decided to introduce a new service, NetGlobal load balancing (a solution to manage huge amounts of web traffic) for their customers. 

NetGlobal policy dictates that a feature should be tested for at least 3 months with only 10% of their customers before fully exposing it to the rest of the users. So they decided to use feature flagging to test it in production with 10% of their customers – let's say 10,000 considering the large size of their customer base. 

The feature flag values are passed down to their code base from a central database table isolated from any relationships with other tables. The table has a boolean value that manages the visibility of the new feature, and Devin, the team lead for developing this feature, is responsible for its management and stability.

So, the time comes and Devin releases the feature in production. Two months go by and thousands of customers are using their load balancing service for their projects. 

A dev from Devin’s team, while working on the prod database, accidentally changes the feature flag value in the table. Due to this mistake, the load balancing service instantly goes down and users start to face traffic loss on their sites. 

The monitoring system triggers an alarm and the dev and DevOps teams spring into action. In about 10-15 minutes, they find the problem and resolve the issue. But because the user base is huge and the usage of the feature at the user end was quite technical, an impactful loss already happened.

### How to Mitigate the Issue

Now, let's consider how Devin's team could've mitigated this incident if they'd been using Flagsmith to create feature flagging. We'll also look at how its RBAC would have helped to secure the flag value access.

* **Flag value management:** By using [Flagsmith’s SDK](https://www.flagsmith.com/sdks) in the application code, the flag values could have been managed and passed to the application with clear visibility. 
* **Audit control:** By using Flagsmith’s audit log, the team could've had better accountability and transparency concerning changes made to feature flags.
* **RBAC:** it would have restricted access to unauthorized developers so that they couldn't change the feature flag values and provided granular control to the team lead, release managers, or DevOps engineers.

This hypothetical use case helps us get a basic understanding of the significance of a feature flagging tool for production releases. It also shows us why RBAC plays an important role in managing permissions and hierarchy in an ecosystem to help your team avoid downtime incidents. 

The key takeaway here is that it's important to establish a standard DevOps process and choose DevOps tools that become a compliant part of feature release and management.

## How to Establish a Standard DevOps Process

A standard DevOps process should be set in place for the lifecycle of a feature. It should address all the steps from the build stage to the production release. 

Most importantly, in the pursuit of quick releases, your team shouldn't ignore the importance of securing this process as I mentioned at the beginning of this article.   
  
A basic example of a standard DevOps process would start with establishing a strong **Continuous Integration workflow** with the following steps:

1. **Build and Scan:** Building artifacts and vulnerability scanning before pushing to artifact hubs.
2. **Perform Unit, End-to-End, and Integration testing:** Writing unit, end-to-end, and integration tests is paramount to testing the functionality of the application builds.

Then, you'd want to establish a solid **Continuous Deployment** **workflow** with the following steps:

1. **Separation of environments:** Separate dev, staging, and production environments for environment-specific testing.
2. **Rollout method selection:** Select rollout strategies depending on your needs, such as Rolling Updates, A/B Testing, Canary Deployments, and Feature Flagging.

Next, you should implement a robust **monitoring** mechanism for applications by leveraging monitoring systems such as Prometheus for monitoring, Grafana for visualization, and Grafana On Call for incident/on-call management tool.

And finally, after creating the above mechanism, the last step would be to use the provided **RBAC** systems in place. You'd start from cloud platforms and move on to DevOps tools being used implement the concept of least privilege on all levels and add them as a part of DevOps compliance practices.

## Wrapping up

In this article, we discussed the importance of RBAC in the world of DevOps and how teams can leverage it in the industry to secure production environments. 

We also discussed what feature flagging is, its importance for feature releases, and how it leverages RBAC to manage user permissions. 

For a better understanding, we discussed a use case in which we saw how implementing Flagsmith could have saved a downtime incident, and how a DevOps compliance process could give strength to feature releases in production.  
  
  
  
  


  

