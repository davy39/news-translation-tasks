---
title: What is DevSecOps? How to Secure Website or App
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-12-14T14:08:56.000Z'
originalURL: https://freecodecamp.org/news/what-is-devsecops
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/maxresdefault.jpeg
tags:
- name: Application Security
  slug: application-security
- name: Devops
  slug: devops
- name: youtube
  slug: youtube
seo_title: null
seo_desc: "Every day major companies have vulnerabilities exploited in their software.\
  \ It is important to learn how to protect your applications against data breaches.\
  \ \nIn this article you all about DevSecOps and web security.\nThere is a video\
  \ course that goes ..."
---

Every day major companies have vulnerabilities exploited in their software. It is important to learn how to protect your applications against data breaches. 

In this article you all about DevSecOps and web security.

There is a video course that goes along with this article. The article focuses on the definitions and theory. The video course will also show you how to take advantage of common web vulnerabilities, how to fix those vulnerabilities, and how to use DevSecOps tools to make sure your applications are secure. 

You can watch the video course below or [on the freeCodeCamp.org YouTube](https://youtu.be/F5KJVuii0Yw) channel.

%[https://youtu.be/F5KJVuii0Yw]

Thanks to [Snyk](https://snyk.io/) for providing a grant that made development of this tutorial and video course possible.

## What Is DevSecOps?

[DevSecOps](https://snyk.io/series/devsecops/) refers to the integration of security practices into a DevOps software delivery model. In a DevSecOps model, security objectives are integrated as early as possible in the life cycle of software development and security considerations are important throughout the lifecycle.

To really understand DevSecOps, it can be helpful to first understand DevOps and also vulnerabilities.

### Vulnerabilities

Let's start with vulnerabilities. The whole point of security is to protect against vulnerabilities so let's understand the different types and afterwards I'll discuss DevOps.

The average cost of a data breach in 2020 was $3.86 million and global cybercrime costs are expected to reach $6 trillion by the end of this year. It is estimated that 90% of web applications are vulnerable to hacking and 68% of those are vulnerable to the breach of sensitive data.

In 2020, there were over 1000 data breaches in the United State according to the Identity Theft Resource Center. Over 155.8 million individuals were affected by data exposures. 

![Image](https://www.freecodecamp.org/news/content/images/2021/11/statistic_id273550_cyber-crime_-number-of-breaches-and-records-exposed-2005-2020.png)

### Vulnerability vs. Exploit vs. Threat

When thinking about security, it is important to understand the difference between a vulnerability, an exploit, and a threat.

A **security vulnerability** is a software code flaw or a system misconfiguration that hackers can use to gain unauthorized access to a system or network. Once inside, the attacker can leverage authorizations and privileges to compromise systems and assets.

An **exploit** is the method hackers use to exploit a vulnerability. An exploit is typically a piece custom software or a sequence of commands. 

There are even exploit kits that can be embedded in compromised web pages where they continuously scan for vulnerabilities. As soon as a weakness is detected, the kit immediately attempts to deploy an exploit, such as injecting malware into the host system.

A **threat** is the actual or hypothetical _event_ in which one or more exploits use a vulnerability to mount an attack. 

![security vulnerabilities and exploits](https://res.cloudinary.com/snyk/images/w_550,h_438,c_scale/v1/wordpress-sync/Vuln-diagram-2-1-e1574424713592/Vuln-diagram-2-1-e1574424713592.png)

Only a small amount of known vulnerabilities will be used to hack into a system. Vulnerabilities that pose the highest risk are those that have a higher chance of being exploited and therefore should be the ones that are prioritized.

## Types of Security Vulnerabilities

Security vulnerabilities can be found in all different areas related to software. Here are some common security vulnerabilities in applications and websites.

There are two different important lists of weaknesses in web applications. The first list is created by the Open Web Application Security Project (OWASP). They have a popular list called the [OWASP Top 10](https://owasp.org/www-project-top-ten/) that features the most commonly exploited vulnerabilities.

The second list is [CWE](https://cwe.mitre.org/), or Common Weakness Enumeration, which is a “community-developed list of common software and hardware weakness types that have security ramifications.” This list is run by the MITRE Corporation, a not-for-profit company that operates federal government funded R&D centers. They create the CWE-25 which is their list of the 25 most dangerous software weaknesses.

In the CWE-25, there are 3 major types of application and website security weaknesses:

1. Porous defenses
2. Risky resource management
3. Insecure interaction between components

## 1. Porous Defenses

A porous defenses weakness is one that could allow users to bypass or spoof authentication and authorization processes. Authentication verifies the identity of someone trying to access a system while authorization is the set of access and usage permissions assigned to the user.

Porous defense weakness examples include:

* Weak password encoding
* Insufficiently protected credentials
* Missing or single-factor authentication
* Insecurely inherited permissions
* Sessions that don’t expire in a timely manner

All of these porous defense vulnerability types can allow hackers to successfully access sensitive resources.

Exploits that leverage these vulnerabilities may include:

* Credential stuffing attacks
* Hijacking of session IDs
* Stealing login credentials
* Man-in-the-middle attacks

## 2. Risky Resource Management

Another vulnerability category is risky management of resources such as memory, functions, and open-source frameworks. 

These vulnerabilities include:

* **Out-of-bounds write or read (aka buffer overflow):** The application can be tricked into writing or reading data past the end or before the beginning of the intended memory buffer.
* **Path traversal:** Allows attackers to get to pathnames that let them access files outside of restricted directories. I'll be showing an example of this later.

Exploiting these vulnerabilities allow hackers to gain control over an application, damage files, or access sensitive information.

## 3. Insecure Interaction Between Components

Many applications today send and receive data across a wide range of services, threads, and processes. The way different components intact with each other can introduce vulnerabilities.

Weaknesses that expose a web application or website in this manner include:

* **Cross-site scripting or XSS:** When user inputs are not handled securely, it opens up the possibility for XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users. This is a very common vulnerability.
* **Cross-site request forgery (CSRF):** Improper verification of whether a seemingly legitimate and authentic request was intentionally sent. These attacks are often mounted via social engineering vectors such as bogus emails that trick a user to click a link, which then sends a forged request to a site or server where the user has already been authenticated.

If apps and websites don't properly implement security controls for interaction between components, this leaves them vulnerable to backdoor attacks, scripting attacks, worms, trojan horses and other exploits that deploy malicious code to wreak havoc on infrastructure, data, and systems.

### Most Common Vulnerabilities

Between the OWASP-10 and CWE-25 lists, it is clear that Broken Access Control as the top vulnerability. 94% of applications have some some form of broken access control.

Access control makes sure that users cannot act outside of their intended permissions. If this is not set up properly it can lead to unauthorized information disclosure, modification, or even destruction of data.

### DevOps

Now let's talk about DevOps, which is an important part of DevSecOps.

DevOps is a concept that has been talked about and written about for long time, and many definitions of DevOps have emerged. 

DevOps is basically a set of practices that combines software development (Dev) and IT operations (Ops). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-59.png)
_DevOps Pipeline_

Most modern DevOps organizations will depend on some combination of continuous integration and continuous deployment/delivery systems, in the form of a [CI/CD pipeline](https://snyk.io/learn/what-is-ci-cd-pipeline-and-tools-explained/). As part of the lifecycle a variety of automated security testing and validation can be performed, without requiring the manual work of a human operator. And this is all part of the Software Development LifeCycle.

Here is an example of a common DevOps flow. First, a developer will write code and push it to a repo. At that point the CI/CD pipeline starts. There are automated tests, then a version is built eventually it deployed to production. There are tests at every step to assure code quality. In this model, security is sometimes only considered right before deploying to production.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-57.png)

DevSecOps follows a similar flow, but adds automated security considerations throughout the process. Security is integrated with the DevOps. DevSecOps codifies security objectives as part of the overall goal structure.

The shield represent all the places that we test for security. Different tools are used for different steps and I'll talk about some of the specific tools later.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-58.png)

DevSecOps should be thought of as the natural continuation of DevOps, rather than as a separate idea or concept. 

Activities designed to identify and ideally solve security issues are injected early in the lifecycle of application development, rather than after a product is released. This is accomplished by enabling development teams to perform many of the security tasks independently within the software development lifecycle (SDLC).

To integrate security objectives early in the development of an application, start before the first line of code is ever written. Security can integrate and begin effective threat modeling during the initial concept of the system, application, or individual user story. Static analysis, linters, and policy engines can be run any time a developer checks in code, ensuring that any low-hanging fruit is dealt with before the changes move further upstream. Later I'll be showing you how to use a tool to check code for security issues while you are writing it.

Software composition analysis can be applied to confirm that any open-source dependencies have compatible licenses and are free of vulnerabilities. I'll be showing you how to use a tool to check software dependencies for security issues. It can be very helpful to get immediate feedback on the relative security of the code you've written and this helps individual developers take ownership of security issues.

Once code is checked in, Static Application Security Testing (or [SAST](https://snyk.io/learn/application-security/static-application-security-testing)) tools can be used to identify vulnerabilities and perform software composition analysis. SAST tools should be integrated into post-commit processes to ensure that new code introduced is proactively scanned for vulnerabilities. Having a SAST tool integration in place enables remediation of vulnerabilities earlier in the software development lifecycle, and it reduces application risk and exposure.

After the code builds, you can start to employ security integration tests. Running the code in an isolated container sandbox allows for automated testing of things like network calls, input validation, and authorization. These tests are often part of Dynamic Application Scanning Tools (or DAST). These tests generate fast feedback, enabling quick iteration and triage of any issues that are identified, causing minimal disruption to the overall stream. If things like unexplained network calls or unsanitized input occur, the tests fail, and the pipeline generates actionable feedback in the form of reporting and notifications to the relevant teams.

Next, things like correct logging and access controls can be tested. Does the application log relevant security and performance metrics correctly? Is access limited to the correct subset of individuals (or prevented entirely)? 

Finally, the application makes its way to production. But security tests continue. Automated patching and configuration management ensure that the production environment is always running the latest and most secure versions of software dependencies. 

Special techniques and tools can be used to secure containers. Later, you will learn how to do this in a real-world environment.

Utilizing a DevSecOps CI/CD pipeline helps integrate security objectives at each phase, allowing the rapid delivery to be maintained.

The entire approach helps minimize vulnerabilities that reach production, thereby reducing the cost associated with fixing security flaws. DevSecOps aims to build security into every stage of the delivery process, from the requirement stage onwards, and establish a plan for security automation.

## Software Project Iceberg

When thinking about security you should remember that your code is just the tip of the iceberg.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-70.png)

In an average software project, only 10-20% of code is custom code. Yes, it is important to make sure your custom code is secure but there is a lot more to think about.

80-90% of many codebases consist of open source code, modules, and libraries. The frameworks and libraries that you import can themselves import more frameworks and libraries. This is code that you didn't actually write yourself. 

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-71.png)
_The node_modules directory of a project is often massive._

On average, 80% of vulnerabilities are found in direct dependencies. It doesn't matter how good you are with writing secure code if you import vulnerable dependencies.

Then there are containers. These often consist of hundreds of Linux packages inherited from public sources. Again, code that you didn't actually write yourself. 

And you can't forget about Infrastructure as Code. This opens up a bunch of new attack vectors for malicious actors. Misconfiguration is the number one cloud vulnerability.

DevSecOps properly implemented should cover all of these areas.

## The Importance of DevSecOps

### Why are DevSecOps practices important?

As companies get larger there is often more software, cloud technologies and DevOps methodologies.

More software means more of the organization’s risk becomes digital making it increasingly challenging to secure digital assets.

Cloud technologies means that many of the IT and infrastructure risks are moved to the cloud. This raises the importance of permission and access management since everything can be accessed from anywhere.

As you've seen DevSecOps brings security into DevOps, enabling development teams to secure what they build at their pace, while also creating greater collaboration between development and security practitioners. Security teams offer expertise and tooling to increase developer autonomy while still providing a level of oversight.

### 6 Benefits of the DevSecOps Model (compared to the traditional DevOps Model)

![6 Benefits of the DevSecOps Mode](https://snyk.io/wp-content/uploads/devsecops-benefits-1-1240x627.png)

1. **Faster delivery:** The speed of software delivery is improved when security is integrated in the pipeline. Bugs are identified and fixed before deployment, allowing developers to focus on shipping features.
2. **Improved security posture:** Security is a feature from the design phase onwards. A shared responsibility model ensures security is tightly integrated—from building, deploying, to securing production workloads.
3. **Reduced costs:** Identifying vulnerabilities and bugs before deploying results in an exponential reduction in risk and operational cost.
4. **Enhancing the value of DevOps:** Improving overall security posture as a culture of shared responsibility is created by the integration of security practices into DevOps. 
5. **Improving security integration and pace:** Cost and time of secure software delivery is reduced through eliminating the need to retrofit security controls post development.
6. **Enabling greater overall business success:** Greater trust in the security of developed software and embracing new technologies enables enhanced revenue growth and expanded business offerings.

## Conclusion

There are a bunch of tools that can help secure your apps and many of them are free. Learn more about how to use them in the video that goes along with this article.

%[https://youtu.be/F5KJVuii0Yw]


