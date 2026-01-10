---
title: How to Extend Your Login Flow With Auth0 Actions
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2021-12-22T15:46:00.000Z'
originalURL: https://freecodecamp.org/news/intro-to-auth0-actions
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/rohit-code-idk-2400-x-1260.jpg
tags:
- name: Auth0
  slug: auth0
- name: authentication
  slug: authentication
seo_title: null
seo_desc: "I recently attended a training session with the Auth0 Dev Rel team to learn\
  \ about a cool new feature called Auth0 Actions. \nIn this article, I am going to\
  \ explain what Auth0 Actions are, why you'd want to use them, and how to set one\
  \ up.\nWhat are Aut..."
---

I recently attended a training session with the Auth0 Dev Rel team to learn about a cool new feature called Auth0 Actions. 

In this article, I am going to explain what Auth0 Actions are, why you'd want to use them, and how to set one up.

## What are Auth0 Actions?

Actions are secure, tenant-specific, versioned functions written in Node.js that execute at certain points during the Auth0 runtime. Actions are used to customize and extend Auth0's capabilities with custom logic.

!["Sample Actions Flow"](https://cdn.hashnode.com/res/hashnode/image/upload/v1639214635781/VFyOmuqRg.png)

Above you can see a sample flow. In it, once the user logs into the system, you add a trigger to verify the user's identity using Onfido and then confirm consent using OneTrust before completing the login flow and issuing the token.

In brief, an action is a programmatic way to add custom business logic into your login flow.

## Why use Auth0 Actions? 🤔

**Extensibility** – they're built to give developers more tooling and a better experience in their login workflows.

**Drag N Drop Functionality** – The flow editor lets you visually build custom workflows with drag and drop Action blocks for complete control.

**Monaco Code Editor** – Designed with developers in mind, you can easily write JavaScript functions with validation, intelligent code completion, and type definitions with TypeScript support.

**Serverless Environment** – Auth0 hosts your custom Action functions and processes them when desired. The functions are stored and run on their infrastructure.

**Version Control** – You have the ability to store a history of individual Action changes and the power to revert back to previous versions as needed.

**Pre-Production Testing** – Your personal Actions can be drafted, reviewed, and tested before deploying into production

## How to Set Up Auth0 Actions 

For the purposes of this demo, we are going to be creating an action to enforce Multi-Factor Authentication (MFA) for a specific role. I will take you through the process of:

1. Creating a role
2. Adding users
3. Setting up a demo application
4. Creating an Action to enforce MFA
5. Testing the code

Let's get started:

### 1) Login to Your Auth0 Account

The first step to secure your application is to access the Auth0 Dashboard in order to create your Auth0 application. 

If you haven’t created an Auth0 account, you can [sign up for a free one now](https://a0.to/signup-for-auth0).

### 2) Create an Application

Once in the dashboard, move to the Applications tab in the left sidebar.

![Application Page](https://cdn.hashnode.com/res/hashnode/image/upload/v1639214927748/WpImjm7mg.png)

Click on Create Application.

Provide a friendly name for your application (like Test Actions App) and choose Single Page Web Applications as an application type.

![Create Application Page](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215005392/uhXHjQpPZ.png)

From the quick start tab choose React. Download the sample app. This will have most of the necessary details already in place.

![Quick Start Sample](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215038833/KmbmIA1nt.png)

We also need to set up a few settings for this application. Choose the Settings tab (next to quick start). Add your localhost URL to the following places:

1. Allowed Callback URLs
2. Allowed Logout URLs
3. Allowed Web Origins

![Update Application Settings](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215091880/cwD9fJnFd.png)

### 3) Setup Application

Unzip the code we downloaded in a location of your choice. Then open it in the code editor of your choice.

Cross verify that the details of your application are correctly configured in `src/auth_config.json`.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-16-at-7.56.39-PM.png)

We will run this code locally, so install the dependencies and run it in dev mode (so we have hot reload enabled). To do this, `npm install & npm run dev`.

Once the application starts you should be shown an SPA like below. If you click on Log In it will take you to your login box.

![Sample Application](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215261508/-E672eefw.png)

### 4) Setup Users and Roles

Click on the User Management tab in the left sidebar.

Go to the Users tab and click on the Create User button. We need to create 2 users:

1. Admin User
2. Test User

Remember these credentials as these are the test users we will use for this demo.

![User Creation](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215392817/I51zfr-Ov.png)

Go to the Roles tab and click on the Create Role button. Call the role `Admin` and, once it's created, go to the user tab and assign it to your Admin user.

Once this is done go back to your locally running SPA and try logging in with one credential. You should be able to access a user portal like below:

![Initial Login](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215500834/SgGX7vE_5.png)

### 5) Setup Actions

Click on the Actions Tab in the left sidebar. Then go to the Flows category.

Select the Login Flow. This will run the flow of an action once the login process in your login box is complete.

![Login Flow](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215815525/N-h2y-tlI.png)

Click on the `+` button in Add Action and select Build Custom.

Name it MFA for Role and leave the rest as is.

![Action Creation Flow](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215793963/Rj2rC2T6f.png)

Once created, you'll come to a screen as follows:

![Action Code Editor](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215844044/VrPsqFVBz.png)

Add the below code into the `onExecutePostLogin` function:

```
  if (event.authorization != undefined && event.authorization.roles.includes("Admin")) {
      api.multifactor.enable("any");
  };

```

![Action Code](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215869129/2ELHfGy5s.png)

On the left side you can see a play button. This is your testing environment inside the actions editor. You will find the [event](https://auth0.com/docs/actions/triggers/post-login/event-object) object in which you can test the actions flow by adding `Admin` to the `authorization.roles` array.  
  
When you add the `Admin` role you should see a response with MFA like below. When it's not present you should get an empty array.

![Action Test Case](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215931493/zai-96biU.png)

Click on save draft and deploy. 

Go to the flow now and click on the custom actions tab on the right and you should be able to drag and drop the `MFA for Roles` action into the flow. Click on Apply so that this new flow will work with your login box.

![Action Flow](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215949399/nK49n1ZHZ.png)

You will also need to enable MFA on the Auth0 dashboard. 

Open the Securities tab and choose multi-factor auth. In the next screen, enable One-time Password. This will let users use an application like Google Authenticator for a one-time password. 

There are other factors you can enforce as well, like SMS or Email-based OTP, but for this demo we will be using just the one-time password.  
  
In the policies section leave everything as is and save your changes.

![MFA Screen](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216209703/f54daE0Jo.png)

### 6) Testing With Your Application

Now when you go to login on the locally running application, you should be triggered to do a MFA for the admin user. So let's test that.

Click on login and redirect to your login box. If you are logged in already, log out and then do the same.

Enter your admin users credentials:

![Admin Login](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216252587/jyNxUdkU9.png)

Once the login goes through, you will be prompted to authenticate with your preferred authenticator app. I used google authenticator and entered my OTP.

![Admin MFA](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216272416/9BGhY_91S.png)

You will then be asked to consent to share your user data with the application.

![MFA Consent](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216291893/v2IITRcrF.png)

Once you accept the above, you should be logged in.

![Admin Logged In](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216404160/YnZZikEzZ.png)

If you try the same flow with the test user, you will notice that you are directly logged in after the consent page and no MFA request was triggered. 

This is because in our actions code, as shown below, you can see that we check to see if the user roles have the Admin role. If so, then we ask Auth0 to trigger am MFA workflow with any of the enabled MFA use cases of the tenant.

```
  if (event.authorization != undefined && event.authorization.roles.includes("Admin")) {
      api.multifactor.enable("any");
  };

```

## Conclusion

Congrats! You have just created a custom Auth0 Actions flow and tested it. This was a simple example to help you understand what Auth0 Actions are, and how they can be built and used in your workflows. 

There are many more complex flows you can build, and you can find some examples provided by Auth0 below. Just click on the trigger and you will find specific examples.

[Sample Actions Code](https://auth0.com/docs/actions/triggers/)

Thanks for reading! I really hope that you find this article useful. If so, please share it so others can see it.

Thanks for reading! :)

P.S Do feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/rohitjmathew) or [Twitter](https://twitter.com/iamrohitjmathew)

## Appendix

The following sources were really helpful in writing this article:

* [Introducing Auth0 Actions - Auth0](https://auth0.com/blog/introducing-auth0-actions/)
* [Auth0 Actions - Auth0 Docs](https://auth0.com/docs/actions)

