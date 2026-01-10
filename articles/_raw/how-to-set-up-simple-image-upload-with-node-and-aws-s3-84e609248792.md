---
title: How to set up simple image upload with Node and AWS S3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T18:32:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-simple-image-upload-with-node-and-aws-s3-84e609248792
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yi56K1oYbapFszZA_N3uPg.jpeg
tags:
- name: AWS
  slug: aws
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Filip Jerga

  A step-by-step guide explaining how to upload an image or any file to Amazon S3
  service.


  This is the first part of a tutorial in which we will handle the server (Node.js)
  part of the code.

  I prepared a video tutorial on YouTube as wel...'
---

By Filip Jerga

#### A step-by-step guide explaining how to upload an image or any file to Amazon S3 service.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yi56K1oYbapFszZA_N3uPg.jpeg)

This is the first part of a tutorial in which we will handle the server (Node.js) part of the code.

I prepared a video tutorial on YouTube as well. You can find a link in the resources at the bottom of this article.

### 1. What we need to install & a short description.

**multer:** middleware for handling data files. Primarily used for uploading files. More info: [Npm Link](https://www.npmjs.com/package/multer)

**multer-s3:** multer extension for an easy file upload to Amazon S3 service. More info: [Npm Link](https://www.npmjs.com/package/multer-s3)

**aws-sdk:** necessary package to work with AWS(Amazon Web Services). In our case S3 service. More info: [Npm Link](https://www.npmjs.com/package/aws-sdk)

**Go to your projects and let’s install packages:**

```
npm install —-save multer multer-s3 aws-sdk
```

### 2. Signup for AWS

First, let’s create an account on [https://aws.amazon.com](https://aws.amazon.com/). Amazon offers an amazing free tier you can use for the 1st year. After login, search for S3 service.

Simply said, S3 is a cloud service to store files.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kL7kzofPaB83N7EmyV9P2g.png)
_Select S3_

We need to **create a Bucket**. You can imagine a bucket as a folder for your files. Choose a **bucket name** and the **Region**. Since this is a simple setup we are not interested in other configurations. (Default setup is ok — if something is not clear ask in comments). Click “**next**” until you are on **Review** and create your bucket.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ds5x2m5EbltvbBK6b-UJdQ.png)
_Bucket creation_

**Navigate to your created bucket** and check your **URL bar**. Remember your **bucket name** (for me “medium-test”) and **region** (for me “us-east”).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GYbZM5qHrPoto9Kgi7nryw.png)
_Check your Url bar._

Now, we need to get our **secure credentials**. Navigate through your account name to “**my security credentials**”. Then “**Access Keys**” and **Create New Access Key**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X5iF7gUqs_M2IzH2IwYC3Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*VAAk0eS8PyT-v-QdnGxoXg.jpeg)
_My security credentials and Access Keys_

![Image](https://cdn-media-1.freecodecamp.org/images/1*kZNeP9KvC9hJRLyh6a7Abg.jpeg)
_Create Access Key_

**Never share your keys with anyone!** Temporary save these keys to some file or download the Key File, because we need keys in order to set up a file upload.

**All right. Amazon Setup Done!**

### 3. Go to Your Coding Editor

**I will not explain the basics of Node or Express here.** This tutorial is focused only on the file upload. If you are interested in the whole project implementation, check my GitHub repository or watch the full tutorial. (You can find links at the end of this blog post).

1. Create your file-upload service with the following implementation (first part):

**Important note:** Never expose your secret credentials directly into file! Never share your secret credentials! Consider to setup environment variables in your local environment or in case of deployed projects, variables in your cloud provider. Best solution would be to use **aws-profiles**: [https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-shared.html](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-shared.html).

**First,** we are importing all our installed packages. The **second** part is to **configure our AWS**. We need to provide our **secret keys and region** from the URL bar I showed you before.

After AWS configuration, we can create an instance of our Amazon S3. We are still not quite done yet. Now, let’s see the second part of this implementation.

Now, we can set up a solution for a multer upload. We need to provide function to the multer object with the following properties.

1. **s3**: instance of Amazon S3 we created before.
2. **bucket**: name of our bucket (in my case: “medium-test”)
3. **acl**: access control for the file (‘public read’ means that anyone can view files), you can check all the available types here: [amazon link](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl)
4. **metada**: callback function to set metadata of uploaded files. Here, I am setting additional metadata for a **fieldName**. You can see this data on the image bellow.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NeYh6Kg4i3BAKD20_ZpfyQ.png)
_Metadata_

5. **key:** callback function to set the **key** property (under which key your file will be saved in your bucket). In our case, **we are making a timestamp of a current time** and saving this file under this name. This way our filename will always be unique, but you can choose whatever name you want.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vjRTskqhTeaGdVDNbtqWeQ.png)
_Uploaded file with a current time name_

After all the setup, we are exporting the **upload** object in order to use it in other files.

### 4. Setup a route to upload image

We are almost done, but users of our app still don’t have access to the image upload. We need to expose this functionality to them. Let’s create an endpoint to save a file.

We are exporting our upload object that we’ve created before and creating a new one from it. The new one is more specific with additional configuration for a **single image upload**. We are providing an ‘**image**’ value to it. **This value** is very important, because we will send our file to a server under this key.

**Second part is route itself. POST** endpoint to ‘**/image-upload**’. Inside we call **singleUpload**. Do not forget to **pass inside req and res,** because multer will get the file we are sending to the server from the req object.

We are checking for an error. If there is none, we are sending back JSON with the value of our file location, which is just an **URL to the file on Amazon**.

**Aaaaand that’s it!** We can upload files to Amazon S3 Now. Pretty simple, what do you think?

### 5. Let’s test it out in Postman.

To see the results of our hard work, we need to send a request to the server with an image we want to upload. In this part we will test it via Postman. In the next part of the tutorial, we will create an implementation in an Angular application.

If you don’t have **Postman,** you can simply download it as a Google Chrome extension. Just search for ‘**postman google chrome extension**’. Postman is an application to initialise, send, and test requests to the server in a simple matter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OQiXF-lDa8GUhcKh7nZDGw.png)
_Postman_

1. **Send a post request** to an endpoint we created before. In my case I specified in node path of **/image-upload**.
2. Select **Body** of **form-data**.
3. Provide the **key** of an **image.** You’ll notice that this is a **key** we set up before in our code. Check a file and choose some file from your computer.
4. **Send the request**.

You should get back JSON with the URL of your uploaded file.

**Voilà! That’s it guys. This is a simple file upload for Node.** In the next article, I will continue with a frontend implementation for Angular.

If you like this tutorial, feel free to check my full course on Udemy — [The Complete Angular, React & Node Guide | Airbnb style app](http://bit.ly/2NeWna4).

**Video Lecture:** [Youtube video](https://www.youtube.com/watch?v=ASuU4km3VHE&t=1047s)

**Completed Project:** [My github repository](https://github.com/Jerga99/bwm-ng)

Cheers,

Filip

