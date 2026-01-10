---
title: How to use Google Sheets as a JSON Endpoint
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-21T23:26:00.000Z'
originalURL: https://freecodecamp.org/news/cjn-google-sheets-as-json-endpoint
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/0_kycb_xJ-enmTWhvL.png
tags:
- name: backend
  slug: backend
- name: google sheets
  slug: google-sheets
- name: json
  slug: json
seo_title: null
seo_desc: 'By Clark Jason Ngo

  UPDATE: 5/13/2020 - New Share Dialog Box steps available below.


  Thanks Erica H!


  Are you building a prototype dynamic web application and need to collaborate with
  non-developers?

  I have been to a hackathon before and experienced p...'
---

By Clark Jason Ngo

UPDATE: 5/13/2020 - [New Share Dialog Box](https://gsuiteupdates.googleblog.com/2020/04/new-file-sharing-dialog-google-drive.html) steps available below.

> Thanks Erica H!



Are you building a prototype dynamic web application and need to collaborate with non-developers?

I have been to a hackathon before and experienced participating with the knowledge on how to develop an application but lacked the skill or time to implement a full-stack web application in the 3-day sprint. That time may skill was way too low to even help out and was sidelined to watch tutorials and study HTML and CSS. 

The result? I have learned a lot but I wished I could've contributed more.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-125.png)

In one of the hackathons I have participated in recently, I encountered a similar problem. This time around I was not the newbie. I had non-engineers who wanted to help in building our prototype web application. Luckily, we stumbled upon a Google Spreadsheets as a way for our non-engineers to mock up our database and have the back-end developers connect to Google Sheets JSON Endpoint and parse it.

With this guide, you'll be able to:

1. Create a spreadsheet in Google Spreadsheets.
2. Publish the spreadsheet to the web.
3. Generate a JSON endpoint.
4. Open the spreadsheet for public collaboration.
5. Pass the JSON endpoint to your back-end developer.

After this tutorial, you'll be able to join teams and say, "I can help with the back-end!".

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-126.png)

### Section 1: Creating a Google Sheet

**Step 1:**

Go to [Google Sheets](https://docs.google.com/spreadsheets/u/0/)

**Step 2:**

Create a new spreadsheet

![Image](https://cdn-media-1.freecodecamp.org/images/1*2md2vMHKWXzXbWOwddzXPw.png)

### Section 2: Publishing your Google Sheets to the web

_Note: New Share Dialog Box update as of 5/13/2020, located after Step 2._

**Step 1:**

Click **_File_** _>_ **_Publish to the web…_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*XFtPyWBYh3JX6PdQUJ5j-w.png)

**Step 2:**

Click **_Publish_**, then **_OK_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*QtAY0n29zHviNXdsPJZaQQ.png)

**Step 3:**

No need to do anything here

![Image](https://cdn-media-1.freecodecamp.org/images/1*WenBwpAkxyDc4fhGPeC6Dw.png)

### UPDATE: 5/13/2020 - New Share Dialog Box

**Step 1:**  
Click Share

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-108.png)

**Step 2:**

Click "Change to anyone with the link"

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-107.png)

**Step 3:**

Click "Done"

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-109.png)



### Section 4: Using your Google Sheets as JSON endpoint

**Step 1:**

Copy the template URL and paste in the address bar:

[https://spreadsheets.google.com/feeds/cells/YOURGOOGLESHEETCODE/SHEETPAGENUMBER/public/full?alt=json](https://spreadsheets.google.com/feeds/cells/1g4FBktkm7al3ZkDI8LuFXuztTqK4nY-eUYMLep6BRuw/1/public/full?alt=json)

**Step 2:**

Go to your opened Google Sheets and check the address bar

![Image](https://cdn-media-1.freecodecamp.org/images/1*xRIMehCRmQxSQpAWi2bhlQ.png)
_Google Sheets url_

![Image](https://cdn-media-1.freecodecamp.org/images/1*AM6_ME5wgoQdtfMHFB_ipg.png)
_Google Sheets code_

**Step 3:**

Go to the template URL and replace

* **_YOURGOOGLESHEETCODE_** with **_1ifbWzueslEP5-_ysP6gg7o_NaHQmqF8LlXBfStCwFMs_**
* **_SHEETPAGENUMBER_** to **_1_**

**Step 4:**

Retrieve JSON URL

[https://spreadsheets.google.com/feeds/cells/1ifbWzueslEP5-_ysP6gg7o_NaHQmqF8LlXBfStCwFMs/1/public/full?alt=json](https://spreadsheets.google.com/feeds/cells/1ifbWzueslEP5-_ysP6gg7o_NaHQmqF8LlXBfStCwFMs/1/public/full?alt=json)

![Image](https://cdn-media-1.freecodecamp.org/images/1*SU97RXIK-rFaMWEfaP1kng.png)
_Result of JSON url_

### Section 5: Making your Google Sheets public (for collaboration and data entry)

#### Step 1:

On the top right, click **_Share_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*O2SCuizLuiLPFFBQVRL9vw.png)

**Step 2:**

Add a name, click **_Save_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*D6leg5gLfYpoTOXlrpFUcw.png)

**Step 3:**

Click **_Advanced_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*k7DGUBwGJnVIdZeuaQbGlA.png)

**Step 4:**

Click **_Change…_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*qkKSGYrYiNp861WQjaoUKg.png)

**Step 5:**

Click **_On — Public on the web_**, then **_Save_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*paO-_3OAzlhzW-oZQI9udw.png)

### **Common Gotchas:**

If you receive the response below, please check your URL and make sure you use the Google Sheets code in the address bar.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xrfoHNKtE4uld3IylAI1Lw.png)

If you receive the response below, please go back to Section 2: Publishing your Google Sheets to the web.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZL71DxnV5Rw6asXjpjjC1Q.png)

[**Clark Jason Ngo - Graduate Teaching Assistant - Technology Institute - City University of Seattle |…**](https://www.linkedin.com/in/clarkngo/)  
[_Join LinkedIn * Passionate to nurture new software developers. Technical Skills: Git, MVC, JavaScript, NodeJS, ReactJS…_www.linkedin.com](https://www.linkedin.com/in/clarkngo/)  

