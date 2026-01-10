---
title: The OWASP Top 10 – A Technical Deep-Dive into Web Security
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-02T15:40:01.000Z'
originalURL: https://freecodecamp.org/news/technical-dive-into-owasp
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/New-Project.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: 'By Dipto Karmakar

  In terms of security, there are many vulnerabilities that need to be treated and
  prevented, but some need more attention than others. Without question, the best
  guide to help you address these security issues is The Open Web Applica...'
---

By Dipto Karmakar

In terms of security, there are many vulnerabilities that need to be treated and prevented, but some need more attention than others. Without question, the best guide to help you address these security issues is The Open Web Application Security Project. 

[OWASP](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/) started as a simple project to raise awareness among developers and managers about the most common web security problems. And nowadays it has become a standard in application security.

In this article, we’ll give a more in-depth technical overview of some of the vulnerabilities listed in the OWASP project and how to mitigate them. We will do bad code - good code examples side by side to help you better understand and prevent these types of attacks and to improve your [web application security.](https://en.wikipedia.org/wiki/Web_application_security)

## Injection

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FYrozLEA.png)

This type of vulnerability happens when a program allows an attacker to supply untrusted/malicious input data. This causes the interpreter to execute unexpected commands, usually to reveal data that should otherwise be inaccessible or to bypass some security implementation.

The most common cause of injection vulnerabilities results from a software’s failure to **filter**, **validate** or **sanitize** a user’s input.

Let’s take a look at two “wrong code implementations” which allow injection attacks to happen.

### Bad code example 1:

Let’s say you have a login route that receives an email and for whatever reason, it receives the password already hashed.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/79C3zK_C.png)
_Bad code example 1_

If we know a user’s email address, for example _myemail@email.com_, then we can effortlessly bypass this login system by sending the following JSON object, which creates a NoSQL injection.

```json

{
        "email": "myemail@email.com",
        "password": { "$ne": "" }
}
```

This object will instruct the MongoDb to find a user with the email “myemail@email.com” and with a password different from an empty string.

This example may be a little far-fetched, but take a look at the following code and see if you can spot the problem.

### Bad code example 2:

For this example we have a registration form on the interface with the following code on the back-end:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/5i2HmYIn-1.png)
_Bad example 2_

![Image](https://www.freecodecamp.org/news/content/images/2020/04/qmPOUeDN-1.png)
_Sign up view_

How we can exploit this code? Very simple: let’s say for this example that the User Schema looks like this:

```javascript
export const UserSchema = new mongoose.Schema({
    email: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    admin: {
        type: Boolean,
        default: false
    },
    accountConfirmed: {
        type: Boolean,
        default: false
    },
}, 
);
```

Now just send the following POST request with Postman or any other tool that you prefer to use:

```json
{
    "email": "my-email",
    "password": "123321",
    "admin": "true",
    "accountConfirmed": "true"
}
```

And now you have successfully registered on this website – not as a simple user but with a confirmed admin account.

The problem here is that if we just simply use:

```javascript
{ ...req.body }
```

​​then we will create a new user object with all the properties inside the object _body,_ so here we can inject anything we want.

### Refactoring

Let’s refactor the code from both examples to prevent this kind of attack.

For the first example, we can check the expected type for both email and password. In our case we are waiting for a string in both fields:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/-4b0HFdz.png)

If we supply the same parameters again:

```json
{
	"email": "myemail@email.com",
	"password": { "$ne": "" }
}
```

We will receive a **400 Bad Request** response. We can go even further and check if the email is actually an email and not just a simple string, but this is out of our scope for now.

For the second one, we can use “whitelist” server-side input validation by stripping off unwanted properties:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mHTYhaTW.png)

These examples were for NoSQL injection, but this technique can be extended for [SQL injection](https://github.com/qazbnm456/awesome-web-security#sql-injection) as well.

## Using Components with Known Vulnerabilities

![Image](https://www.freecodecamp.org/news/content/images/2020/04/mUl2Q-DQ-1.png)

Above we saw some poorly implemented security standards which resulted from our mistakes. However there are situations when the problem is not from the code that we wrote, but from the open-source code that we use in our project.

An attacker can exploit the vulnerabilities of these components to execute malicious code or to make the program behave in an unwanted manner.

Even though this seems to be out of your hands, it is not. There are steps we can take to prevent this kind of problem.

For example, we can do a continuous inventory for component versions of both the client-side and server-side and remove unused dependencies and / or features.

We can monitor sources for vulnerabilities in the components.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/-pKYG90o-1.png)
_White Source Dashboard_

To ensure that your components are safe you should check vulnerability databases regularly and apply security patches promptly. This will help you to stay protected.

## Broken Authentication

![Image](https://www.freecodecamp.org/news/content/images/2020/04/S1l6-xYY.png)

This vulnerability comes into play when web apps implement authentication/session management techniques poorly. This is because it gives attackers access to accounts that they otherwise shouldn’t be authorized to access.

This security issue is most widespread in the form of brute force attacks and when session-ids / tokens are exposed in such a form that they can be easily stolen.

### Bad code example 1:

Let’s take the example from the previous code snippet. We tweaked it a little bit to send a **401** (Unauthorized) response when no user is found with a given email and password.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/XkdI14FZ.png)

Even though this is the refactored code, it is still vulnerable to Broken Auth. Here, if we use a wrong password, we get a 401 response. But if the password is weak we can brute force it until we guess it.

### Refactoring

We can prevent brute force attacks by simply using a rate limit on our route. Now the user has 3 chances to authenticate, after which they will no longer be able to send requests on this route for the next 15 minutes (and will get a response of **429 Too many requests**).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/g37VnwlN.png)

The next type of vulnerability on this topic has to do especially with the poorly JSON web token management.

### Bad code example 2:

The next example is very frequently found in login systems:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/NawbB50i.png)

Most of the time, a login system using JWT is implemented in this way. After the user sends the right credentials a token is generated using their **id** or another **unique** value. Then the token is sent to the front-end where it will be saved inside the application. Or if a persistent authentication is needed it will be saved inside cookies or local storage.

The problem with this approach is that the token that should be secured can now be accessed through the front-end code, thus making it vulnerable. Malicious code injected into the front-end JavaScript could access cookies or local storage and steal this token.

### Refactoring

This problem can be overcome with the next implementation.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/wcKOH3Gm.png)

This time the token is also saved in cookies, but it is saved from the back-end code with the **httpOnly** property. This means that it cannot be accessed from any code running on the front end. 

To make it more secure, the token is saved with the **signed** property, which causes the cookies to be signed with a secret key.

You can go even further and block the **http** protocol with the **secure flag** which forces the cookie to be sent over **https**.

## Sensitive Data Exposure

![Image](https://www.freecodecamp.org/news/content/images/2020/04/H_NQWQ7g.png)

As the name indicates, this vulnerability fires when a web application fails to sufficiently protect sensitive data.

While recent legal changes such as [GDPR](https://www.ncsc.gov.uk/information/GDPR) should ensure that sensitive data is not exposed, a significant percentage of web applications fail to meet these requirements.

This usually happens when data is transmitted in clear text using HTTP, SMTP and FTP, or when weak/old cryptographic algorithms are used.

A likely scenario can be the following:

A web site doesn’t use or enforce TLS for all pages. An attacker monitors network traffic, downgrades connections from HTTPS to HTTP, intercepts requests, and steals the information sent. Maybe they even steal the user’s session cookie, thus, accessing or modifying the user’s private data.

Another scenario can be:

Passwords are stored inside the database unsalted or as simple and weak hashes. A file upload flaw or any other attack allows an attacker to retrieve the password database. After that, all the hashes can be exposed with a rainbow table of pre-calculated values, thus giving to the attacker the actual plain password of the users.

