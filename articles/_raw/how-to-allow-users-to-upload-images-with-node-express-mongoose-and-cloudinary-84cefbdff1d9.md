---
title: How to allow users to upload images with Node/Express, Mongoose, and Cloudinary
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-23T14:36:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-allow-users-to-upload-images-with-node-express-mongoose-and-cloudinary-84cefbdff1d9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ETsmhAGOpiWfK06i
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: mongoose
  slug: mongoose
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Glyn Lewington

  Are you building a full-stack app and want to let users upload an image but you’re
  not sure how? In my experience, this is always achieved by having users input a
  link and saving this string to your database. This works great and is...'
---

By Glyn Lewington

Are you building a full-stack app and want to let users upload an image but you’re not sure how? In my experience, this is always achieved by having users input a link and saving this string to your database. This works great and is quick and easy, but it’s also kind of cheating. What kind of app makes you first go to another site and upload your image, and then come back and link to it?

So, what’s the solution?

Allow the user to input a file, then on your server, upload this file to a cloud service and save this in your database. Cloudinary is great for this. It’s dedicated to media uploads. It has great documentation. It allows for transformations. **And** has a huge free plan (10 GB storage). You can sign up for [Cloudinary here](https://cloudinary.com/invites/lpov9zyyucivvxsnalc5/yytj9stwvdsschwyccf8) (I get nothing for this).

### Let’s get started on the front-end

```html
<form action='/api/images' method="post" enctype="multipart/form-data">
  <input type='file' name='image' />
</form>
```

This should look familiar. All you need is a form which will submit the information to the server. Enctype is required for submitting files to the server.

That’s the front-end solved.

### The back-end

Now, the back-end is where all the magic happens. You will need all the usual dependencies for working with **Express** and **Mongoose**. In addition, we will utilise **Multer**, **Cloudinary**, and **multer-storage-cloudinary**. Multer will allow access to files submitted through the form. Cloudinary is used for configuration and uploading. multer-storage-cloudinary will make the process of combining these easy.

```js
const multer = require("multer");
const cloudinary = require("cloudinary");
const cloudinaryStorage = require("multer-storage-cloudinary");
```

Once the dependencies are required you need to configure them. When you sign up to Cloudinary, you will be provided your API credentials. I recommend storing these in a “.env” file to keep them secure.

Below we are also:

* setting a folder to keep all the images organised on Cloudinary for this project
* ensuring only “.jpg” and “.png” files are uploaded
* adding a transformation to keep the height and width consistent and to manage file size.

There’s a lot more you can do in regards to transformations — you can take a look [here](https://cloudinary.com/documentation/image_transformations) if you are interested.

```js
cloudinary.config({
cloud_name: process.env.CLOUD_NAME,
api_key: process.env.API_KEY,
api_secret: process.env.API_SECRET
});
const storage = cloudinaryStorage({
cloudinary: cloudinary,
folder: "demo",
allowedFormats: ["jpg", "png"],
transformation: [{ width: 500, height: 500, crop: "limit" }]
});
const parser = multer({ storage: storage });
```

Now that your server is all set up to receive and process these images, we can move onto setting up the route.

In your post route, you simply add the parser we set up before as a middleware. This will take in the file, upload it to Cloudinary, and return an object with the file information. You can access this information in the request object.

I like to extract just the information I want from this, to keep my database organised. At the least, you will want:

* the URL which can be used to display the image on the front-end
* the public_id which will allow you to access and delete the image from Cloudinary.

```js
app.post('/api/images', parser.single("image"), (req, res) => {
  console.log(req.file) // to see what is returned to you
  const image = {};
  image.url = req.file.url;
  image.id = req.file.public_id;
  Image.create(image) // save image information in database
    .then(newImage => res.json(newImage))
    .catch(err => console.log(err));
});
```

Your image will probably be part of a larger object in your database. The image URL and id can be saved as strings as a part of this.

_*Image is an example placeholder for your database collection. Substitute it for your own._

### Displaying the image

When you want to display the image on the front-end, perform a database query, and then use the URL inside your image tags `<img src=imageURL` />.

I hope this will help you in adding that little extra to your websites. It’s not that difficult once you break down each step in the process. It will give your website the professional touch and will make it stand out.

If you have any questions, please ask in the comments.

