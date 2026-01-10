---
title: How you can set up face detection with feature identification in your app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-22T15:39:31.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-set-up-face-detection-with-feature-identification-in-your-app-1d6f1c14c79
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YnsDJKmh013JSYBVXZ7KDg.jpeg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Rohit Ramname

  Find the faces with Microsoft Cognitive Services, Azure, and JavaScript


  _Photo by [Unsplash](https://unsplash.com/photos/mMolCwtrEss?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" ...'
---

By Rohit Ramname

#### Find the faces with Microsoft Cognitive Services, Azure, and JavaScript

![Image](https://cdn-media-1.freecodecamp.org/images/K1PR2n3zSKsdfQH-BlnQD9S2XtC7rzu7O57f)
_Photo by [Unsplash](https://unsplash.com/photos/mMolCwtrEss?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Vanessa Serpas</a> on <a href="https://unsplash.com/search/photos/face?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### What is face detection?

You have probably seen face detection in action many times now, in different applications — for example in your phone, in photos on Facebook. Face detection results in faces having rectangles around them. So, as the name suggests, it’s simply detecting a face in an image. This is also a type of **machine learning** use case.

In this tutorial, we will be learning how to perform face detection using Microsoft **Cognitive Services** provided by **Azure,** and simple **JavaScript** and **CSS**.

### What will I learn from this tutorial?

By the end of this tutorial, we should be able to achieve the result below.

![Image](https://cdn-media-1.freecodecamp.org/images/iXj0mo7EbVzNGkwwejoymi4vMpkPeoT0W0Qs)

Please notice that, along with face detection, Azure also gives us the approximate age and if the person is wearing glasses, features that can be requested in the URL.

This tutorial will ensure that we are set up with an Azure subscription and we are getting the required results back.

**This exercise assumes that you have a Microsoft Azure subscription.** If you don’t have one, you can create it for free by going to Microsoft’s Azure [website](https://azure.microsoft.com/en-us/free/). It will ask you for credit card information but your card is never charged unless paid services are purchased (which is not required for this demo).

### Let’s start

First, we login to our Microsoft Azure subscription.

Go to “Portal.azure.com” and login with your ID.

Click “Create Resource” and search for “Face”.

![Image](https://cdn-media-1.freecodecamp.org/images/pWBktCmM22poTQCu9O0ffDJ-XwuzXFR278oG)

From the search results, select Face (Category : “AI + Machine Learning”).

Click **Create.**

You will have to complete a simple form which will ask you to:

* give a name to your resource
* select your subscription
* select your geolocation where your user base will mostly reside
* select your pricing plan (there is a free plan that you can select for trial purposes).
* then click “Create New”

Once you follow these steps, Azure will deploy your services and create subscription keys.

Open your subscription by clicking on it and go to the “Overview” section.

![Image](https://cdn-media-1.freecodecamp.org/images/F9qllAlSy-VV235jE3cTsPqJYZU7yqpFKPqp)

This is the place where you can find your subscription keys and access keys. You will need to send an access key with each API call header for authentication.

That’s it for the setup.

### Let’s test it

Now, we can test if our API is working using a tool called [Postman](https://www.getpostman.com/apps).

**Postman is very popular tool to test the API calls.**

Open Postman and the use the End Point in your Azure subscription as the URL. Make sure the operation selected in the dropdown is “POST”.

![Image](https://cdn-media-1.freecodecamp.org/images/hP4vpX4xQ03JOgvGod30j4cdzkVbwa8bd3lQ)

In the “Headers” tab, add:

* the “Key” “Ocp-Apim-Subscription-Key” with “Value” [your Azure subscription keys]
* the “Key” “Content-Type” with Value “application/octet-stream”

![Image](https://cdn-media-1.freecodecamp.org/images/tO2WWVz38lE8fLJcy1qLH8BUihdabaNUiSOR)

In the “Body” tab, choose “binary” and click “Choose Files” to select a picture with a human face.

![Image](https://cdn-media-1.freecodecamp.org/images/pgpPb-EfwRP6-GYOnLG27UNY-Q7qT5fazD5g)

Click “Send”.

You should see a response like below from the Azure Cognitive Services API calls.

```
[ { “faceId”: “4f3df6bb-83d9–45ea-bac5-d60cac5a1623”, “faceRectangle”: { “top”: 456, “left”: 475, “width”: 330, “height”: 330 } }]
```

Azure automatically assigns an ID to each face it can detect, and gives the co-ordinates of the face on that picture.

You can can ask Azure for different face attributes. For the complete list of attributes, please refer to the [Microsoft Website](https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236).

For example, to request if a person is wearing sunglasses and to get an estimated age, you can send the query string: [https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceAttributes=age,glasses](https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceAttributes=age,glasses,emotion). For this request, Azure will send the estimated age, type of glasses (or no glasses), and emotion analysis.

```
[ { “faceId”: “f8721afb-f9d8–4372-ab43–23fd429aafbf”, “faceRectangle”: { “top”: 640, “left”: 297, “width”: 202, “height”: 202 }, “faceAttributes”: { “age”: 31, “glasses”: “Sunglasses”, “emotion”: { “anger”: 0, “contempt”: 0.001, “disgust”: 0, “fear”: 0, “happiness”: 0, “neutral”: 0.998, “sadness”: 0, “surprise”: 0 } } }]
```

Great. Looks like we have a basic setup ready.

But before you stop reading this article and close the window…

### Lets get to the interesting stuff:

We will hook all this up to a webpage to see the results.

We will need a simple HTML page with **File Upload Control** so that we can select an image file.

```
<div id=”containerDiv”> <div id=”titleDiv”> Welcome </div> <div id=”content”> <div id=”btnUpload”> <div class=”upload-btn-wrapper”> <button class=”btn” >Upload a file</button> <input type=”file” name=”myfile” id=”upload” /> </div></div> <div id=”features”> </div> <div id=”imgDiv”><img id=”imgx” class=”imageContainer” ><div id=”face”></div></div></div> </div>
```

Let’s break it down to understand what this is.

This page has two sections: the title and the content.

Title `<d`iv> is quite simple. It is just a title of the app with an ID.

Content `<d`iv> has three sections:

* upload `<butt`on>, which is the main feature button of this app
* features `<d`iv>, which will contain features of the face image
* image `<d`iv>, which will render the selected image

Further down, Image div has two components.

* image id `=“imgx”`, which is the actual image selected, and
* `<d`iv> `with id=`“face”, which is the face identification rectangle.

That’s it for the HTML part.

### Now the core part — the JavaScript call

#### Code

First, add a listener to the “File Selected” event when a file is selected.

`document.getElementById(‘upload’).addEventListener(‘change’, fileChange, false);`

Add the `fileChange` event function:

```
function fileChange(event){ if(event.target.files && event.target.files.length >= 0) { var file1= event.target.files[0]; var reader = new FileReader(); reader.onload = (event) => { document.getElementById(“imgx”).src=event.target.result; getFaceDetails(file1); } } reader.readAsDataURL(event.target.files[0]); }
```

When the event is raised, that is, the file is selected:

* the event details are read`var file1= event.target.files[0];`
* a new instance object of FileReader class is created`var reader = new FileReader();`
* the content of the file selected in the event is read `reader.readAsDataURL(event.target.files[0]);`

Now, when the file is loaded completely, the `src` property of the `imgx` element is set:

```
document.getElementById(“imgx”).src=event.target.result;
```

and it calls the function which will internally get the face information from the image:

```
getFaceDetails(file1);
```

Let’s look at the `getFaceDetails` function:

```
function getFaceDetails(file){ var xmlHttp = new XMLHttpRequest(); var url=”https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceAttributes=age,glasses"; xmlHttp.open(“POST”,url,true); xmlHttp.setRequestHeader(“Content-Type”, “application/octet-stream”);
```

```
xmlHttp.setRequestHeader(“Ocp-Apim-Subscription-Key”, “[Azure Face API subscription key]”); xmlHttp.send(file); xmlHttp.onreadystatechange = function (response) { if (this.readyState == 4 && this.status == 200) { let face=JSON.parse(this.responseText) var oleft = document.getElementById(“imgx”).offsetLeft; var otop = document.getElementById(“imgx”).offsetTop; document.getElementById(“face”).style.left=oleft+face[0].faceRectangle.left+”px”; document.getElementById(“face”).style.top=otop+face[0].faceRectangle.top+”px”; document.getElementById(“face”).style.width=face[0].faceRectangle.width+”px”; document.getElementById(“face”).style.height=face[0].faceRectangle.height+”px”; document.getElementById(“features”).innerText=”Age: “+face[0].faceAttributes.age +” Glasses:”+face[0].faceAttributes.glasses ; } }}
```

**WHOA…**!! That looks dirty.

#### Explanation

Yes… it is… a bit! But let me explain.

The first few lines of this function is just opening a JavaScript `XMLHttpRequest` with URL and request headers. The URL is the Azure URL that you provided above in Postman — or you can get in from the Azure portal.

```
var xmlHttp = new XMLHttpRequest(); var url=”https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceAttributes=age,glasses"; xmlHttp.open(“POST”,url,true);
```

We then added two request headers. The first is the `Ocp-Apim-Subscription-Key` and your Azure subscription key. The second is the `Content-Type` key with the `application/octet-stream` value. Since we are going to send an image in a request, `application/octet-stream` is the type for binary data.

```
xmlHttp.setRequestHeader(“Ocp-Apim-Subscription-Key”, “[Azure Face API subscription key]”);
```

```
xmlHttp.setRequestHeader(“Content-Type”, “application/octet-stream”);
```

And then we make the call:

```
xmlHttp.send(file);
```

When the request is completed, this has a ready state of 4. We get the coordinates of the face portion of the image in JSON format along with the features.

```
xmlHttp.onreadystatechange = function (response) { if (this.readyState == 4 && this.status == 200) { let face=JSON.parse(this.responseText)
```

Since we are going to render the image at the center, we need the left and top coordinates of the rendered image. This enables us to position our Face Rectangle `<d`iv> accordingly.

```
var oleft = document.getElementById(“imgx”).offsetLeft;var otop = document.getElementById(“imgx”).offsetTop;
```

And now we just have to draw a rectangle (“face” `<d`iv>) around the face on the rendered image.

```
document.getElementById(“face”).style.left=oleft+face[0].faceRectangle.left+”px”; document.getElementById(“face”).style.top=otop+face[0].faceRectangle.top+”px”; document.getElementById(“face”).style.width=face[0].faceRectangle.width+”px”; document.getElementById(“face”).style.height=face[0].faceRectangle.height+”px”;
```

And read feature attributes as well in the features `<d`iv>.

```
document.getElementById(“features”).innerText=”Age: “+face[0].faceAttributes.age +” Glasses:”+face[0].faceAttributes.glasses ;
```

And that concludes the JS part.

Below is the basic CSS styling for rendering purposes. **Please note** that we are using CSS grid.

```
#containerDiv{ display:grid; grid-template-areas:  “title” “content”}
```

```
#imgDiv{ background-repeat: no-repeat; border: 1px solid #bbb; border: solid; grid-area:image;}#face{ position:absolute; border:solid; border-style: ridge; border-color: cornsilk;}#features{ grid-area:features}#titleDiv{ height: 100px; display: flex; justify-content: center; align-items: center; font-size: -webkit-xxx-large; background-color: black; color: sandybrown; font-family: sans-serif; grid-area:title;}
```

```
#content{ display:grid; justify-items:center; grid-area:content; grid-template-areas:  “upload” “features” “image”}#btnUpload{ grid-area:upload;}.upload-btn-wrapper { position: relative; overflow: hidden; display: inline-block; padding: 2%; width: 100vw; display: flex; justify-content: center; } .btn { border: 2px solid gray; color:white; background-color:cornflowerblue; padding: 8px 20px; border-radius: 8px; font-size: 20px; font-weight: bold; }  .upload-btn-wrapper input[type=file] { font-size: 100px; position: absolute; left: 0; top: 0; opacity: 0; }
```

It’s **very important** to keep the **position** of the image control (`imgx`) and `Face` `<d`i`v> ab`solute for proper rendering. Other`wise, Face` <div> will not be rendered over the image. It will be somewhere on the side as an inline effect.

### There we go…

Now you can open the webpage, select the image with human face in it, and see the results.

The face detection can be further improved by requesting additional features in the URL from Azure. For example, you can add sentiment display.

I hope you found this tutorial exciting and will build some **cool stuff** with it.

Happy Learning!

