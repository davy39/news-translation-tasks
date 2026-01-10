---
title: How to better protect your secrets in Logic Apps using Key Vault connector
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-30T08:46:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-better-protect-your-secrets-in-logic-apps-using-key-vault-connector
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/secret-banner.png
tags:
- name: Azure
  slug: azure
- name: Logic Apps
  slug: logic-apps
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Nadeem Ahamed

  One of the key challenges that users face while using Logic Apps is managing secret
  values. This used to be handled by passing the secrets through ARM templates, which
  is not an out of the box solution.

  Before the availability of the...'
---

By Nadeem Ahamed

One of the key challenges that users face while using [Logic Apps](https://www.serverless360.com/azure-logic-apps) is managing secret values. This used to be handled by passing the secrets through ARM templates, which is not an out of the box solution.

Before the availability of the Key Vault connector in Logic Apps, [one of the ideal workarounds](https://www.serverless360.com/blog/managing-secrets-in-azure-logic-apps-using-managed-identities) was using an HTTP action available in logic apps and leveraging the Managed Identity authentication mode. Even this workaround has a few considerations as follows:

1. Logic App run history contains the secret values which cannot be hidden
2. Currently, we can only have 10 logic apps that have system-assigned managed identities

Let us explore how to better protect your secrets in your Logic Apps using the new Key Vault connector.  Also, I will show you how the above issue can be addressed with the Key vault Connector.

## Design your sample Logic App

Follow the steps below to create your sample logic app in the designer page.

1. Add an “Http request” trigger to the logic app. Later we will call this logic app via a rest client.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p1.png)

2.   Then, search for the key vault actions and add the “Get Secret” action to the logic   app. Now, you have a couple of options here to authenticate: either you can use **Azure AD** or [**Service Princip**](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal)**al**. In this example, I am going ahead with Azure AD service.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p2.png)

3.   Sign-in with your account. This account should have enough permission to access your Key Vault. Otherwise you should manually provide access through **Access policies.**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p3.png)

4.   Fill in the required field with the “<secret name>”. If you don’t already have one in place, then you can create one by heading to the Key Vault menu. There you can find the “secrets” option in the left pane.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p4.png)

> _Note: If you are provisioning the Key Vault itself for the first time, then remember: sometimes you may need to register the Key Vault service to your Subscription manually. (I encountered this issue when I did it for the first time)._

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p5.png)

5.   Now, add the “Http response” action to the logic app. Fill in the following fields as below:  
  
**Status Code**: 200  
**Body**: <add the dynamic expression: The Secret>

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p6.png)

6.   Save the Logic App.

## Testing the Logic App

Now, copy the HTTP post URL from the Logic App trigger and head to [reqbin](https://reqbin.com/) (online REST client). Paste the URL in the address field and change the default method from **GET** to **POST** and click Send. 

The logic app would have gotten triggered and sent back the response code 200 along with the secret value as shown in the picture below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p7.png)

## Inspecting the Run History

On inspecting the run history of the logic app, we notice that the secret values are visible in plain text. 

Do you remember the same problem we encountered in the classic method? As I have already said this can be easily addressed through the Key Vault connector settings by following the below steps:

1. Head back to the designer and click on the settings option under the “more options” menu in the Key Vault connector.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p8.png)

2.  Now, in the settings for “Get Secret” action, enable the Secure **Inputs** and **Outputs** option and click Done.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p9.png)

3.   Once again save the logic app and call it through the rest client (reqbin.com). You will get the same response in the Request Bin, but the run history doesn’t contain the secret values in the plain text format. Rather it shows as “Content not shown due to security configuration”.  


![Image](https://www.freecodecamp.org/news/content/images/2020/03/p10.png)

We have now addressed the first concern in the classic method. The second concern was that we can only have 10 logic apps that have system-assigned managed identities.

We have also overcome this issue by not using the Managed Identity mode of authentication in the connector. Rather it authenticates through Azure Active Directory or Service Principal (which has a downside of rotating secrets, though). 

Once the user gets enough permissions to the Key vault through Access Policy they will be able to access the Key Vault in any number of Logic Apps.

## Expanded Feature Set

While digging more into the Logic Apps Key Vault actions, I found some more interesting use cases that can be achieved through Encryption and Decryption actions.

If the user is more concerned about their data, then they can use the Encryption and Decryption action to keep the values more secure.

To do this, create an encryption key in the Key Vault.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p11.png)

Using the Encrypt and Decrypt actions in the Key vault connectors you can encrypt the data and decrypt it again. As seen above, we can even enable the Secure Inputs and Outputs option in the settings to make it more securable.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p12.png)

## Manage and Monitor Logic Apps using Serverless360

[Serverless360](https://www.serverless360.com/) is one platform to manage and monitor all your Azure Serverless resources with focus to help your operations and support your team on a day to day basis.

_Consider the above workflow of a business application defined using multiple Azure Logic Apps._ 

Different stakeholders of the business application will have different needs as they [manage and monitor the Azure Logic Apps](https://www.serverless360.com/azure-logic-apps-monitoring-management). 

Some key requirements which are hard to achieve through the Azure portal are:

* auto-correcting the Logic App state when found to be not as expected
* instant reflection of the warning and error state of the Logic App in a service map view
* near real time detection of failure
* automation in re-submission of specific failed run actions
* end to end tracking on the message flowing through the Logic Apps, and 
* evaluation on the consumption, performance and reliability. 

These requirements cannot be achieved directly through the Azure portal. But [Serverless360](https://www.serverless360.com/) can come in as a complement to the Azure portal, as it is crafted with capabilities to address the gaps in the Azure portal.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Topology.png)
_Service Map in Serverless360_

## Wrap-up

In this blog, we have seen the classic and latest methods of protecting your secrets in Logic Apps. Also, I hope this blog has given you a clearer understanding of the Key Vault connector that is now currently available.

Lastly, I have covered the extended feature sets of the Logic Apps Key Vault connector, Encryption and Decryption actions.

I hope you enjoyed reading this article. Happy Learning!

