---
title: How to Build a RAG Chatbot with Agent Cloud and Google Sheets
subtitle: ''
author: Ankur Tyagi
co_authors: []
series: null
date: '2024-06-26T14:43:10.000Z'
originalURL: https://freecodecamp.org/news/build-a-rag-chatbot-agent-cloud-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Orange---Yellow-Gradient-Make-Design-Blog-Banner--73-.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: 'LLM''s '
  slug: llms
seo_title: null
seo_desc: 'Today''s companies are data factories. Every interaction, transaction,
  and internal process generates a constant stream of information.

  This data holds immense value, promising to improve decision-making, streamline
  operations, and unlock deep custome...'
---

Today's companies are data factories. Every interaction, transaction, and internal process generates a constant stream of information.

This data holds immense value, promising to improve decision-making, streamline operations, and unlock deep customer insights. 

But data often remains siloed and inaccessible. It may be spread across different departments and systems, and it can be challenging to understand and utilize effectively.

This is where the concept of Retrieval-Augmented Generation ([RAG](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)) technology comes in. By combining the power of retrieval-based techniques and modern generative AI tools, you can build Retrieval-Augmented Generation (RAG) chat applications that allow you to interact with your data using a simple chat interface. 

![Conceptual flow of using RAG with LLMs.](https://www.freecodecamp.org/news/content/images/2024/05/image-57.png)
_What is Retrieval-Augmented Generation (RAG)?_

But before you can chat about your data, a lot of “legwork” is involved. Setting up the infrastructure – the pipeline, vector database, message broker, and knowledge retrieval – is a complex and time-consuming process. This is where the open source tool [Agent Cloud](https://theankurtyagi.com/what-is-agent-cloud/) comes in.

In this guide, you'll learn all about Agent Cloud and what it can do. We'll start by looking at some background info and the current problems we're dealing with. Then, we'll see how Agent Cloud can help solve them.

## How I Started Working with Agent Cloud

I'm passionate about new technology and [developer tools](https://theankurtyagi.com/blog/), and I sit somewhere between Product Marketing, Growth, and Developer Advocacy. I specialize in the creation of high-quality, technical written content for educational purposes. 

I've been involved with the web for ~14 years, the last 4 of which have been documented in punishing detail on my [website](https://theankurtyagi.com/).

I liked being a Software Engineer but, what I really **love** to do is code, design, develop, and then write.

Earlier this year I met [Andrew](https://www.linkedin.com/in/andrewnada/) (founder of Agent cloud) in a private Slack group. He was seeking someone who could not only write about the product but also discuss and teach people about what they're building. I reached out to him, and after two rounds of discussions, we began working together.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-35.png)

I started with building some cool RAG chatbots in my local and later wrote a couple of comprehensive guides on "[How to Build a RAG Chatbot with Agent Cloud](https://www.agentcloud.dev/blog)".

In this article, I'll teach you how to build a RAG chat app using Agent Cloud to privately and securely talk with your Google Sheets data. I'll also talk about why I think Agent Cloud is good open source developer tool.

## Table of Contents:

* [What is Agent Cloud](#heading-what-is-agent-cloud)?
* [What is RAG](#heading-what-is-retrieval-augmented-generation)?
* [Challenges of Building a RAG Chatbot Without Agent Cloud](#heading-challenges-of-building-a-rag-chatbot-without-agent-cloud)
* [Prerequisites](#heading-prerequisites)
* [How to Set Up Agent Cloud via Docker](#heading-how-to-set-up-agent-cloud-via-docker)
* [How to Add Models in Agent Cloud](#heading-how-to-add-models-in-agent-cloud)
* [How to Create Your GCP Service Account Key](#heading-how-to-create-your-gcp-service-account-key)
* [How to Enable Google Sheets API](#heading-how-to-enable-google-sheets-api)
* [How to Set Up your Data Sources](#heading-how-to-set-up-your-data-sources)
* [How to Set Up tools](#heading-how-to-set-up-tools)
* [How to Set Up an Agent](#heading-how-to-set-up-an-agent)
* [How to Create a Task](#heading-how-to-create-a-task)
* [How to Set Up your App](#heading-how-to-set-up-your-app)
* [Conclusion](#heading-conclusion)

## What is Agent Cloud?

[Agent Cloud](https://www.agentcloud.dev) is an open-source platform that lets you build private, secure chat applications powered by large language models (think ChatGPT). 

It streamlines this process by providing a "RAG as a service" offering and a built-in pipeline that allows you to split, chunk, and embed data from over 300 sources (including [Google Sheets](https://www.agentcloud.dev/integrations/google-sheets), Salesforce, Atlassian Confluence, [BigQuery](https://dev.to/agentcloud/how-to-build-a-rag-chat-app-with-agent-cloud-and-bigquery-15b), [MongoDB](https://dev.to/agentcloud/how-to-build-a-rag-chatbot-with-agentcloud-and-mongodb-4la7), [Postgres Data](https://dev.to/agentcloud/how-to-build-a-chat-app-with-your-postgres-data-using-agent-cloud-33hk), SharePoint, and OneDrive).

![List of data sources agentcloud supports](https://lh7-us.googleusercontent.com/mCVaA9lJyTTTLY7YNebA8AyR5Tj_iQ3werHlAERD9-NgHPQ6BXUo42NMIm9HwnIXni-iWaTrjVtROtmx8XhY7RXF_wh2LnYAifRDnP7GYFl9EAvP83EuEtoHa7BM4OZBjCokVzYwBF-4Nrd8TlG-JvQ)
_Data sources_

## What is Retrieval-Augmented Generation?

RAG is a process for enhancing the accuracy of large language models. It does this through the on-demand retrieval of external data and by injecting context into the prompt, at runtime. 

This data can come from various sources, such as your customers' documentation/web pages (through scraping), and data or documents from dozens (if not hundreds) of 3rd party applications like their Databases, Google BigQuery, HubSpot, Google Ads, Google Analytics 4 (GA4) and so on.

For those who want to dive deeper into Retrieval-Augmented Generation and understand its broader applications and significance, I highly recommend reading this comprehensive [blog by NVIDIA](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/). It offers valuable insights and context that complement the practical aspects covered in this article.

## Challenges of Building a RAG Chatbot Without Agent Cloud

If you're working with these AI tools on a daily basis, it becomes easy to understand the value they bring and realize the significance of Agent Cloud in simplifying the chatbot development process. 

But to fully appreciate its benefits, you should understand how chatbot development was handled before such tools were available.

Before tools like Agent Cloud, creating a RAG (Retrieval-Augmented Generation) chatbot was a daunting and resource-intensive task. You had to manually integrate various components, which required significant expertise in multiple areas. 

Here are some challenges faced and the solutions the Agent Cloud team had to devise:

### Data Retrieval and Management:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-36.png)
_List of data sources_

* **Problem:** Ensuring that the chatbot could efficiently retrieve and manage data from sources like Google Sheets, Databases, and so on. 
* **Without Agent Cloud:** Developers had to write custom scripts for data retrieval, often using APIs to fetch data from Google Sheets. This involved handling data formatting, error checking, and real-time updates manually. It was a time-consuming process prone to errors.
* **Agent Cloud's Solution:** Automates data retrieval and management, ensuring seamless and accurate integration with minimal manual intervention.

### Natural Language Processing (NLP):

* **Problem:** Implementing NLP to understand user queries and generate human-like responses.
* **Without Agent Cloud:** Developers needed to integrate standalone NLP engines such as TensorFlow. This required training models on vast datasets, fine-tuning them for accuracy, and constantly updating them to handle new queries effectively.
* **Agent Cloud's Solution:** Offers built-in NLP capabilities, significantly reducing setup time and providing high-quality language understanding out of the box.

### Scalability and Maintenance:

* **Problem:** Ensuring the chatbot could handle increasing data loads and user interactions.
* **Without Agent Cloud:** Building a scalable architecture meant investing in robust server infrastructure, writing efficient code, and continuously monitoring and maintaining the system to handle growth.
* **Agent Cloud's Solution:** Designed to scale effortlessly, allowing developers to focus on improving functionality rather than managing infrastructure.

### User Interaction and Experience:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-37.png)
_Agent cloud app UI_

* **Problem:** Creating an engaging and user-friendly interface.
* **Without Agent Cloud:** Developers had to build custom interfaces, often from scratch, which required additional design and development resources. Ensuring smooth interactions and responsiveness was a major challenge.
* **Agent Cloud's Solution:** Provides pre-built templates and easy integration options, enhancing the user experience with minimal effort.

By understanding these challenges, you can see how a tool like Agent Cloud helps the process of building RAG chatbots. It addresses the pain points of manual data handling, complex NLP integration, scalability issues, and user interface design, providing an all-in-one solution that saves time and resources.

## Prerequisites

You don't need any prior knowledge of RAG chat apps or Google Sheets to follow along because Agent Cloud handles the data splitting, encoding, storage, and synchronization. This allows you to focus on talking to your data and interpreting the results.

## How to Set Up Agent Cloud via Docker

First, you'll need to install Docker on your system if you don't have it already. [Docker](https://docs.docker.com/get-docker/) is a platform for running containerized applications.

Open your terminal and run the following command to clone the Agent Cloud repository from GitHub:

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#002b36;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#b58900;background-color:#002b36;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">git</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#839496;background-color:#002b36;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> clonehttps://github.com/rnadigital/agentcloud.git</span></p></td></tr></tbody></table>

Use the following command to move into the newly cloned `agentcloud` directory:

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#002b36;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#b58900;background-color:#002b36;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">cd</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#839496;background-color:#002b36;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> agentcloud</span></p></td></tr></tbody></table>

To run Agent Cloud locally, execute this command:

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#002b36;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#b58900;background-color:#002b36;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">chmod</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#839496;background-color:#002b36;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> +x install.sh &amp;&amp; ./install.sh</span></p></td></tr></tbody></table>

This command will grant executable permissions to the install.sh script and then run it. The script will download the necessary Docker images and start the Agent Cloud containers within your Docker environment.

![Image](https://lh7-us.googleusercontent.com/IJP_WeswIONKA5EsL87jVisv0mZRsk__P5BajAlXZU3fQW8Fif6mdjqW0t-NTCkU_ZNHAk6PJ4U5UthUmDFOsOQhnmQyY6HwMxHEDIxfqy-VfZODKOq7jFv9OpAlXkR1AszdYK0gkn0RDEut3Y7U7K4)
_local dev setup- agent cloud_

Once the installation script finishes successfully, you can view the running Agent Cloud containers in the Docker application.

![Image](https://lh7-us.googleusercontent.com/oZ4mwbfNiCtFcv4scaILguo5QYVR_cwU5mpJqEzDzq-2gMHtyrD-XbZJnMiloPDFmVcFaUc6KQLyBWw6SnnSlVrTU-IcBIspkIELSZaGJ3M-9bRaq7H9NX94tdug39a98p0XQfa3RNmCYsxiSlTQDUA)
_local docker services_

Once everything is up and running, you can access the Agent Cloud user interface in your web browser. 

Navigate to the URL:

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#002b36;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#839496;background-color:#002b36;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">http://localhost:3000/register</span></p></td></tr></tbody></table>

This will typically open the registration page where you can create an account to use Agent Cloud. 

![Image](https://lh7-us.googleusercontent.com/-o54n5I5Z_6RByvP6IaDXyDC5hlLgkRMFCEHlvJukZ5RWMV31G0ty2NZC09xA-O2-wslq_BUWCxGMcWRX1RT-ed5D75MFqOvNZR5-qA1Dg_lDChV-BGnrdNgq4epGxGGWmgSfT0qLvxq8J80tgAG64Q)
_signup- page- agent cloud_

You can now log in using the credentials you created during signup.

Once you've successfully registered and logged in, you'll be greeted by the Agent Cloud user interface. This interface provides a central hub for managing your data sources, agents, tasks, models, applications, credentials, and so on.

![Image](https://lh7-us.googleusercontent.com/zEAo52ay_80MFLRDZPeRUgMCgx0VtPhOzX_68BSkO0Bkh9-66sAtrVYRTig15imqVFTAHs6OZ0fijXYrZxUMgeExMkRFyTEI9OvKijZWBZKzaQcYrBl0dfJ-MH5E5_5G-IpcTs-312lIdq77INYDk00)
_Home screen - agent cloud_

Congratulations! You've successfully set up Agent Cloud. Now let's move on to the next step and build our RAG chat application using Google Sheets as the data source.

## How to Add Models in Agent Cloud

Go to the Models tab in Agent Cloud. Click the Add Models button to add two types of models. 

* A fast embed model is a lightweight model that runs locally on your machine. It splits and chunks your data before embedding it.
* OpenAI is a popular cloud-based LLM provider.

![Image](https://lh7-us.googleusercontent.com/SlXyhi9xFjz8o1dsMnNApxNDJ8G-NEppj6jfP1TkyaNjU3X6Ewt5NuKQ4mj9SKYxsQOMJ650ErJVvJWR9w4WbNfPRtb26pXnjzoUEsOX6jN7foDbiaM_U6jUJE9HSKqQpSDK54QKjLyI_T9yr2xTGDs)
_Models screen- agent cloud_

## How to Create Your GCP Service Account Key

Agent Cloud offers two authentication methods for accessing your Google Sheets data:

* Google (Auth) – This method involves directly authorizing Agent Cloud through your Google account.
* Service Key Account – This approach utilizes a service key, a credential specifically created for application access to Google Cloud Platform (GCP) services, including Google Sheets.

For this guide, I'll focus on the service key account method, which is generally considered a more secure and streamlined approach for application-to-application communication.

**Here is what you’ll need:**

* A Google Cloud Platform (GCP) project with the Google Sheets API enabled.
* A service account key is created within your GCP project. This key will be used to authenticate Agent Cloud.

I'll walk you through creating a service account key in your GCP project and configuring Agent Cloud to use it to access your Google Sheets data.

First, create a Google Cloud Platform account. Then create a new project. You can give your project any name that you prefer.

![Image](https://lh7-us.googleusercontent.com/s1m6tovJn9Hv7NsWNat4-0AKU_PzwiO6oujqSFwG0Yj-lEyVFbwBMrNIWd-h6ill46ZbHqmdrBH8_xTxXWRP-I6G33n2qB9jhYqCNvtQiYqmc15rSJ7jgP9Qw4y4CfaWDkHfNVl_cb4qHa5HhfyTnns)
_How to Create a GCP Account_

Navigate to the "IAM & Admin" section and select "Service Accounts."

![Image](https://lh7-us.googleusercontent.com/jObPCuwTVS1B9-z5yy4rX4Xi775Ur2AGz8B8k-dISs92F-0Ww5Nk4i3m77VzwvKT5w8pjtpHvEBqfvPlKQf6HC_hF4ghh6mQmeAj_BQm7qH3DJeF_tUFZU2lrDvZ5jB3taEpmQu5kn4cWM_W8mWbA_M)
_IAM and Admin Screen_

Click "Create Service Account" and provide a name and description.

![Image](https://lh7-us.googleusercontent.com/un89_I_sIaEsLrROHvoZF10CYb0KeOrRjhzcm_kregQD-4v7-7Tg0xkhVOqqTNwPcaE0xvio_SL9OD4JFxxwql_T_YIbazfAUADcwh-tkM8FZ8YNwiDiEgTqA-zELb4kIILxFYGDw6t4Vc8qYD7UFPI)
_How to add service account_

Enter your service account name and unique service ID, then click **Done**.

![Image](https://lh7-us.googleusercontent.com/pKIZ1n1-dTCXB0Lzqb5unx-ChrghpEVp8z_zC0Cv6N5PhN2oaHKtgBjsutM_YvynvtSO17cq89uIB6koyktx0W-vxGy_xIyr_nOlwDe_jcvU4ZtU1fGKDG7lMxPvgMZgjkgMO6odWV56gR3BAKWq53I)
_How to create a service account in GCP_

Under the actions tab, click the manage keys option.

![Image](https://lh7-us.googleusercontent.com/ju2mGTR2qMExBbW1vt8budeR1MeA9uNZddtx-IJhFAUaV-bw0GlVJUny9kdXJWndgWA4VXpl70DtYMpXCKQj7-zLus_3iJkl430EoIIcNtBfe2FThCFwQirwlCb0YJwJHb5z54HVKbuw4WlC8PY-HyE)
_Project_

  
Click the **ADD KEY** button and select the Create Key option.

Select JSON as the key type, then click on Create New Key. 

![Image](https://lh7-us.googleusercontent.com/cynXfWX4n8ngRB-mB_CTLvUC1xA4ZqmSnaYtv6K3haSgJyAGlTk-l__J2LXZhupGJpJcZ9LW6NDlw6l05YlKev6sYVsXC9vMjCD3LgPGcCX9O405L-Ixn-LV8jmJbiRcd97y2TfL3zvezgZMi4eNYKw)
_Add keys in GCP_

Select JSON as the key type, then click on Create. Your service account JSON or key JSON will automatically download.

![Image](https://lh7-us.googleusercontent.com/RmAJh50XGOSlSbK-hqWveHc4GozeFZSTsB3oU7y7d4nJ-tiEbfdcyQDdrUOfJonS-8w2GAw30vF1AlII8SOEPHSGz7Ip2Xdc60ypSi_gfljQJa_w84UoyfakUM_U-DcbcOlujk4uN0rrFDXG19aW0Rc)
_Create private key in GCP_

Keep this file safe we will use it later for authentication. 

## How to Enable Google Sheets API

You'll also need to enable the Google Sheets API in your Google Cloud project.

Open the left navigation menu and navigate to "APIs & Services" and then "Library."

![Image](https://lh7-us.googleusercontent.com/1wVRoIvsYl6cYlaxeck2Ob2EviXaktCRdI68xVMjwSbXfABsYWTAkCHNEW7kwc2Ww2MoBop8-3-vS9s_1FIGuM7lq1E5cmp02dZ4ApPdbasZ6SneopXV5PGaiGF5AnVUVV9LVTdMQW8qSpOCzzfMs40)
_APIs and Services in GCP_

Type "Google Sheets API" in the search bar and press Enter.

The Google Sheets API will appear in the search results. Click on it.

![Image](https://lh7-us.googleusercontent.com/TUq6HeWJfhZkZaAHQRst9cZKKlG3zbQkU8NBfl5tEZ43pgBbyYPDiLpHUt9yu1xF1-e8XWUp2isXS7zRcYonVlOwoEj2KJn2PZbK65UmA1KWv2y9AcoCxIaTuCaq5pJ2rrCo1wiZbwL1nDnBhsjPzec)
_Google Sheets API_

On the API details page, click the "**ENABLE**" button.

![Image](https://lh7-us.googleusercontent.com/Rh0qrd79Yqlw1YF5JZ_CSJwvO8ZpnytUs0392Y3OBEmmpLar1JyuOggQo-qms4qWtv9ZPLS69uiNmn4Hi4fSneAQZRIR-eRxWtbagqwNrf0q5qNGIxKJNAnjNk1uDziRLlzny4ZWZL0zeljWkmFT-7E)
_Enable- Google Sheets API_

## How to Set Up your Data Sources

Agent Cloud empowers you to process data from a wide range of sources. 

In this guide, I'll use Google Sheets as the data source. Sheets is a popular web-based spreadsheet application included in Google Workspace. Google Sheets allows you to create, edit, and collaborate on spreadsheets in real-time. 

For this example, I'll be working with a financial consumer complaints dataset stored in a Google Sheet. 

This dataset contains several columns representing key sales stages and details, potentially including:

* Complaint ID
* Submitted Via
* Date Submitted
* Date Received
* State
* Product
* Sub-product
* Issue
* Sub-issue
* Company
* Public Response
* Company Response to Consumer
* Timely Response?

Here's how to connect your Google Sheets data:

Navigate to the Data Sources tab within the Agent Cloud interface.

Click the button labeled **New Connection**. This will initiate the process of adding a new data source.

![Image](https://lh7-us.googleusercontent.com/Tr8WlGVlJTmef0xrTvAxjLeTHCpLua_VDxZ9jamnlXQDY8wKsPf0skYQ_b1PFE0d9K13ndHS-piLpDKu16ikxLL9-AUb4lpgFw2pA6-TOI0lRwLQR5KBPbus5FDqJNkbKQYXdf2s4daLRHP4gPci0Ec)
_Data Sources- Screen- Agent Cloud_

Search and select “Google sheets” as the data source.

![Image](https://lh7-us.googleusercontent.com/aNI6G2gH3HNF4XqibSxNOHjXWwW7X_jgtyK79B0k46LJUL1j_1G9vgYOtUdgT__6mjet3AMXEosqRLsrXZHZsf2rW3UhKPKdpAO2v6RFl8acpdINe6l6-1Y4ZGP52oP4xQVrm1XBlpHVuZVYLfx6-M0)
_Create a Datasource_

I've named our data source **Financial Consumer Complaints**, which you can name however you want. Add a clear and concise description. The data sync will be manual. This means you'll need to initiate the data refresh process whenever you want the latest information from your Google Sheets to be reflected in Agent Cloud.

Enter the appropriate row batch size. Row batch size means how many rows are processed from the Google sheet. For example, the default value 200 would process rows 1-201, then 201-401, and so on. 

Choose the authentication method as “**Service Account Key Authentication**”.

Enter the JSON key **we downloaded earlier above** under the Service Account Information field.

Enter the link to the Google spreadsheet you want to sync. To copy the link, click the 'Share' button in the top-right corner of the spreadsheet, then click 'Copy link'.

![Image](https://lh7-us.googleusercontent.com/L9rtuBctsZISgx997WPk-zW25t46yJEvTMg7-wOCE7yBYPrd6l58BkPRFSWIErEf-1QR8v_6QHWQMtOlMyjOVfPPUUiE6yTOSg5BV5DexE3Jw_fANfmPSQRQqueAYJ3ODS3HRFzmA19PN8JYtOTXbi4)
_Adding details under datasource_

Click the submit button.

Select the collection and fields you want to sync to the vector database and enter their descriptions.

![Image](https://lh7-us.googleusercontent.com/oPDKJbdi5uWh4q0staVJA4gTUytt_EVxCPBeIhV8VUGBsShtYeH9OJ_1R1uvN6HJYcgBvX64DHKt4qxNggdV6bx0filBtMdsuDo_xyhJjmipgIO52dzNmy-ABAtOwi-x-l7hCJoo6lFITMOpSDz83eo)
_Model pop-up_

Click continue and Choose the field you want to embed then choose the model. 

![Image](https://lh7-us.googleusercontent.com/fa8oHY4rDm9SHQ4La-FM5c8BuWq1eWOsTzAhyq-IgMBaGIXR5crLog7gQ3Ziq0X_cngVy5J9yCF6Ld8u-Py6ByQI_S72jB4a5An8BHES6lng2675hjQeyP-ai0_zBY5pmTmX1LgRDI1qLPGsQ3Ws0QA)
_Data sources_

The connection to your Google Sheet is now established. 

During the initial run, Agent Cloud will process your spreadsheet data and convert it into a format suitable for efficient retrieval. This processed data will then be stored within Agent Cloud's vector store.

![Image](https://lh7-us.googleusercontent.com/DWPrunB5TnUXQg7E0gV_XwoETIGO-Qo7cBpN8oYUl9Up--j3_roKiNS6--3CZZADnSeQWfjtO-j3r9RfQsVxQBsZ_NZvhq5Ahnkik2fGPaz0B6bDDVUJRq5rVXDxEkZ0fIIxMxRjqRdxZOIAM3SXiug)
_New- datasource- screen_

If you're comfortable with technical details, you can verify the data's presence in the Qdrant vector store running locally on port 6333. 

This can be accessed through: http://localhost:6333/dashboard#/collections.

Look for a new collection corresponding to your Google Sheet data.

![Image](https://lh7-us.googleusercontent.com/gEdkROWowqm1Xr8Q0ixb65CVZB-UNrzLnNh6KPXkPhAZaP5vHIOSJMeK28nyXye2I846SbMhfo9qG9I2qp67r6BNJLHJDM_z9kYc-KSoN0bUpfUS0CIoQBV_qQcVeXm5mqbIxclnM4VCN4pmc_w1u1k)
_collection-screen_

You can click the collection to view the payloads and the fields populated in the collection.

![Image](https://lh7-us.googleusercontent.com/kQtXRqdF1VR_4UmJUqYGcNMcoVrx9kj1Ncrkgvgb3nzEX7s8UvHscOkYEx18P1qxYy6U04UjLDz-SqjVtTsvjHjxajx5qwsAsVkRPXy1nFBAtjELcht8cSL1vE4jVl49J39KHZuIohiNkAFscO9H4m0)
_Payload_

## How to Set Up Tools

Tools play a crucial role in facilitating effective interaction between the AI agent and its environment, enabling seamless information processing and action execution aligned with its objectives. 

These tools can include functions, APIs, data sources, and resources tailored to empower the agent to autonomously and efficiently undertake diverse tasks. While you have the flexibility to craft your own tools as per their requirements, Agent Cloud also streamlines the process by automatically generating a tool upon the addition of a new data source, 

Click the Tools tab tools to switch to the Tools page and click the **New** button.

Enter the tools' names and add a description. A verbose and detailed description helps agents better understand when to use each tool.

Choose the data source and click the Save button.

![Image](https://lh7-us.googleusercontent.com/URmNamQ6ccOn5FbABAaBo7tfSjAmxZZgT_sN5W8aNrzdfFPbMCMcRwUk6X5YNL_CKTctP-cQxUURBwCADnGQyALwEUmmoQgBBUAsdtEDUWkWxH9oRp15pKHFcnObNpCkjw_eEdSiGnZbdVZodNraQ5Y)
_Edit tool screen_

## How to Set Up an Agent

AI Agents are intelligent systems that excel at handling routine or repetitive tasks by perceiving their environment, collecting data, and using that data to make decisions. 

Click the Agents tab and then click on the New Agent button.

![Image](https://lh7-us.googleusercontent.com/5JrsomIfl-WKZ2hOLW-MZ34xhRpJdhx9hzKwAz2Ab0kDtCVTnZy_rsgjoreGuS533ZCgq125n11M9siNy_AlFHTuMXOHhCSkFGzbE6gNSCQ7YMxw4-Sut1f_-ydDeKchOJjeAtcKxUVoSBmattKAiIg)
_New Agent Screen_

Define an Agent's **Name**, **Role**, **Goal**, and **Backstory** as shown below.

In the "Model" section, choose the AI engine to power your agent's reasoning capabilities.  For this example, we've selected  "OpenAI GPT-4" as both the Model and Function Calling Model.

Choose the tool we set up earlier under Tools (Optional).

![Image](https://lh7-us.googleusercontent.com/d_NajepTkSjuk-tkpiuWcdupeY02HU5nYatqyfjMgj6WXXvBJTgYuStRoSgCFAqNpU4WK8MIarqLJY5MvytjkuQWI4CFyBvTvDsylYEAWgKS8p9f-EbO6LvHYnRFwBd5yQjDvt6XGlriuEfGkicVi-g)
_Adding Details in Agent Screen_

If "OpenAI GPT-4" isn't already configured within Agent Cloud, you can easily add it. Click on the "Model" field and select "Add new model." A new window will appear, allowing you to define the model's name, type, credentials (your OpenAI API key), and the specific LLM model.  

![Image](https://lh7-us.googleusercontent.com/0M9gkgwNfR-2VPGdgVN75Aqh-_aZuotKjasIVbiuOEaV6Wf8O-rQZo3bwk8-ZdHv8tfgRywXnlSy57An1rndCfzmfExx4K7nZ_UXpqDOJ_x1q0IUEnYaMRWqI6EzoEWcDzwx4CsFeWncc2bIiI82uOA)
_Model- popup_

Click the Save button. Once you save this information, "GPT-4" will be available for future agent creation.

![Image](https://lh7-us.googleusercontent.com/3qE96774xn2RHAecevtTlCQ4GUv_WcC6r3sFZFdPNGUNCafENkdQ5SaONMSLzwwIsFyjIgLyp-XlVU-ZijHBybv_ay2KCICrxcR71w7GgqCuklvXK5znfIoRtM03Wd9pSdXFUEWVKnrYnjaGv__l8kk)
_Agents-Screen_

## How to Create a Task

Tasks are specific actions assigned to agents for completion. To create a new task, navigate to the Tasks tab and click the "Add Task" button.

![Image](https://lh7-us.googleusercontent.com/wN1Wy93IPaxiU6NdElwizuJ4e6meqz4-jMiibnKN02WZqNikxMPWOZKsWDNVSlGU-X7IpY1cqPPAlF13aVKSVBGyw-ImPGKYXH2XH-1Yjg3FjI66mBrU-_hrPfbTntKJ1JZ4keZ5X06jnK06-ikwNdE)
_Create Tasks Screen_

Enter the following details in the below pop-up window. 

* **Task name**: Give your task a clear and concise title that reflects its purpose.
* **Detailed description** of what the task entails.
* Choose the tool we created earlier, which is “**Financial Consumer Complaint**” in my case.
* Select the preferred Agent we created earlier we named it “**Customer Complaints Agent**”

![Image](https://lh7-us.googleusercontent.com/RujrqL0gjUYk31aJSYKQYyY55T_nIy-PdSdm8uhcodHGcs8lsHyctuJLnkI4COAL34tXHFjnsjRvypzRaThbIkVEhlTU2quvmaA5cxihN_MHGfg6QaB1i7oBgtXx2Bwa5hEQLbdtEM8Za70JgLRuONI)
_Adding Details in Tasks Screen_

Click the **Save** button to save the task.

## How to Set Up Your App

Now, buckle up because we're about to embark on the exciting part: creating a conversational app. This app will transform our data source into a chat partner, allowing you to have interactive conversations and unlock insights through natural language.

So far, we've laid the foundation for our app. We've created:

* A data source.
* A data retrieval tool.
* An Agent.
* Tasks.

Click the Apps tab and then click the **New App** Button, and then enter the details below:

![Image](https://lh7-us.googleusercontent.com/jBOcimMYi1-HQGbpUXJYFLho-5LGKGKVJJ5E9OnNpy83PzSX0RINP0DN6oK_9p9LztvSm5yQdMSDqmLqY_fvmC_3pREpO2f9h_zRmPGwaYdr9TwLmcWzWhZSRPMlWDK15x9cEdMz6gNwyL4uYnB0Pyc)
_New App Screen_

* App name – Enter the name you’d like to give to your app.
* Enter a description of what our App.
* Select a Tasks
* Select an Agent
* Choose a Chat Manager Model – Pick the Open AI model we configured earlier.

![Image](https://lh7-us.googleusercontent.com/1SMFU6auHKUZgxZGUQ9yJQzKuqDwtU4KbZBJGweDPaJBW_Oc6plMrcror2o2dWindixOWu6bGyYNGg6eUB5TS2iYYmOzP9FHFIvacZTle32ZqL7Gylxxy1XlZLR9YivE3KDHBXxJ1_dvO-aVHWbc2Mo)
_App Screen_

Now, let's test our app. 

Clicking the play button will open a chat window for us where we can have a conversation.

![Image](https://lh7-us.googleusercontent.com/ju-0a5CRhaHgVEqFZkDhdlPkCBqtwOM0Mjnsaz2D7ftl5Hsfku49pkBFYyY9DBr41Rzbwqm90vf8pirBzz2hsUBnsM6YOwjPoCmGhzkm6OQefP_jNNIdOGKx9geEibQLQv_ZzGsaN8AhuXIBl-F9P64)
_Play Button in App Screen_

A chat interface window should be opened for us where we can chat with our data. For instance, with the data I have used, I can prompt the app to summarize some of the issues raised by customers related to the Mortgage product.

![Image](https://lh7-us.googleusercontent.com/tfEGreNRfDRwyiJs0ZomrjfRmSQajuMSYzqL-uxa8tULoso0d56mwE-JiNpLEiv0-x0dnN9XgpajdiwW9aa-dvfnF47dmhW4daQkJ21JYYmC25svAfd3PBXdm9HrmC6tVFAlZ04-H0PLf1B5GfOsqHc)
_Live Chat with Data_

Or I can have it summarize company responses related to different issues.

![Image](https://lh7-us.googleusercontent.com/KpGoDKLffAOcUzFdN7_tJwMved1uDklnP5XQAkaLbwhn1hTlnOgI7Br8QmaPfGUgaK8hLvW958KIyZfDI577PB2aTHgSEHQjBFRN7TeOAgQA0cYjds4R5evGbuMfNXBJOl5x-7Uur0akvOsWgNjI4V4)
_Answer Screen_

## Conclusion

In this tutorial, we explored building a RAG chat application using Agent Cloud and Google Sheets. 

We covered setting up Google Sheets as a data source, embedding the data for efficient retrieval, and storing it within a vector store like Qdrant. We also learned how to create tools for Agents (chatbot components) and build an app chat interface where users can interact with the data without writing a single line of code.

If you want to read more interesting articles about developer tools, React, Next.js, AI and more, then I'll encourage you to checkout my [blog](https://theankurtyagi.com/). 

Some of the fresh articles I've written this year. 

* [How I Build a Blog with Next.js and Firebase](https://theankurtyagi.com/how-to-create-blog-with-nextjs-and-firebase/)
* [How I Build a Task Management App with React and Appwrite](https://theankurtyagi.com/appwrite/)
* [How I Build a Notes App Using React and Supabase – The Complete Guide](https://theankurtyagi.com/notes-app-react-supabase/)
* [How I Build a RAG Chat App With Agent Cloud and BigQuery](https://dev.to/agentcloud/how-to-build-a-rag-chat-app-with-agent-cloud-and-bigquery-15b)

You can get in touch if you have any questions or corrections. I’m expecting them.

And if you found this tutorial useful, please share it with your friends and colleagues who might benefit from it as well. Your support enables me to continue producing useful content for the tech community.

Now it’s time to take the next step by subscribing to my **[newsletter](https://bytesizedbets.com/)** and following me on [**Twitter**](https://twitter.com/theankurtyagi).

  
  
  
  
  
  
  
  
  


  

