---
title: Easy facial detection in your Laravel PHP application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T07:54:52.000Z'
originalURL: https://freecodecamp.org/news/easy-facial-detection-in-your-laravel-php-application-11664ac9c9b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6uFn3v0cRY3xlzbGxUyt0g.jpeg
tags:
- name: Laravel
  slug: laravel
- name: Machine Learning
  slug: machine-learning
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Darren Chowles

  Detect faces in images using the Google Cloud Vision API


  You’ve probably seen facial detection before. As soon as you upload that family
  photo to Facebook, you’ll notice the boxes around all detected faces. And with facial
  recognit...'
---

By Darren Chowles

#### Detect faces in images using the Google Cloud Vision API

![Image](https://cdn-media-1.freecodecamp.org/images/VnPML50ueenYtoyQkR3ysp29B8sCZWkEcjVw)

You’ve probably seen facial detection before. As soon as you upload that family photo to Facebook, you’ll notice the boxes around all detected faces. And with facial **recognition**, it sometimes even auto-tags the correct friend too. It’s not always 100% accurate, but it’s still some great engineering!

### Applications for facial detection

In this article, we’ll get up and running using the Google Cloud Vision API to detect faces. We’ll be using an existing image and we’ll draw a box around each detected face.

There are several real-world use cases for facial detection. Some of these include:

* detecting whether an uploaded image has any faces. This might be a screening step as part of a “know your customer” identification workflow.
* image moderation for applications that allow user-generated content.
* the ability to provide tagging, in the same way social networks do.

### Other functionality available in the Cloud Vision API

Facial detection is only one of the many functions available in this API. It supports the following additional functionality:

* detection of popular logos.
* the ability to detect all categories applicable to an image. For example, a photo of a cat might produce the categories: cat, mammal, vertebrate, and Persian.
* detecting popular natural and man-made landmarks.
* extracting text from images.
* running Safe Search Detection to flag images that contain adult content or violence.

### Google Cloud Platform setup

The first step involves creating a new project in the Google Cloud Platform console.

![Image](https://cdn-media-1.freecodecamp.org/images/kQJQiuCqrMNADYCOMlkELdp3GeTAlQDSklSa)

Head over to the dashboard and [create a new project](https://console.cloud.google.com/projectcreate).

![Image](https://cdn-media-1.freecodecamp.org/images/PHON06KcoAaQASLSaAKClQgTtT7Nc71bplbQ)

Once your project is created, keep the Project ID handy.

![Image](https://cdn-media-1.freecodecamp.org/images/Jc5LfR6-jxcRwOmVt5nvWURCQVvQYnJ2yNu-)

Follow these steps:

* once you have your project, go to the [Create service account key](https://console.cloud.google.com/apis/credentials/serviceaccountkey) page.
* ensure your Facial Detection project is selected at the top.
* under “Service account**”**, select “New service account”.
* enter a name in the “Service account name”.
* under “Role”, select “Project” > “Owner”.
* Finally, click “Create” to have the JSON credentials file downloaded automatically.

![Image](https://cdn-media-1.freecodecamp.org/images/Ty1vbdKD5bpsIwJ1wqTD6mBq13htpDsmYHkj)

You may also need to Enable the Cloud Vision API via the [API Library](https://console.developers.google.com/apis/library/vision.googleapis.com) section.

### Laravel project setup

The next step involves setting up a new Laravel project. If you have an existing Laravel project, you can skip this step.

I’m using Laravel 5.5 LTS for this article. In the command line, run the following Composer command to create a new project (you can also use the [Laravel installer](https://laravel.com/docs/5.5#installing-laravel)):

```
composer create-project --prefer-dist laravel/laravel sample "5.5.*"
```

If you used Composer, rename the **.env.example** file to **.env** and run the following command afterwards to set the application key:

```
php artisan key:generate
```

### Add the Google cloud-vision package

Run the following command to add the `google/cloud-vision` package to your project:

```
composer require google/cloud-vision
```

You can place the downloaded JSON credentials file in your application root. **Don’t** place it in your public directory. Feel free to rename it. **Don’t** commit this file to your code repo. One option is to add it to the server manually.

### Finally, let’s start coding!

Firstly, ensure you have the [GD library](http://php.net/manual/en/image.setup.php) installed and active. Most platforms have this enabled by default.

I’ll be adding the following route to my “routes/web.php” file:

```
Route::get('/', 'SampleController@detectFaces');
```

I’ve created a simple controller to house the code. I’ll be adding all the code within the controller. In a production application, I **strongly suggest** using separate service classes for any business logic. This way, controllers are lean and stick to their original intention: controlling the input/output.

We’ll start with a simple controller, adding a `use` statement to include the Google Cloud `ServiceBuilder` class:

```
<?php
```

```
namespace App\Http\Controllers;
```

```
use Google\Cloud\Core\ServiceBuilder;
```

```
class SampleController extends Controller{    public function detectFaces()    {        // Code will be added here    }}
```

The first thing we’ll do is create an instance of the `ServiceBuilder` class so we can specify our Project ID and JSON credentials.

```
$cloud = new ServiceBuilder([     'keyFilePath' => base_path('fda.json'),     'projectId' => 'facial-detection-app' ]);
```

You specify the location of the JSON file using the `keyFilePath` key. I’ve used the Laravel [base_path()](https://laravel.com/docs/5.5/helpers#method-base-path) helper to refer to the fully qualified app root path.

The next option is the `projectId`. This is the value you grabbed when you created the project in the GCP console.

Next, we’ll create an instance of the `VisionClient` class. The `ServiceBuilder` class makes it easy by exposing various factory methods which grant access to services in the API.

```
$vision = $cloud->vision();
```

Now that we have an instance of the class, we can start making use of the Vision API. We’ll be using the following image as the example. Feel free to download this image, name it “friends.jpg” and place it in your “public” folder.

![Image](https://cdn-media-1.freecodecamp.org/images/HU1KqsFMeLTJcMXm2sFaV4qiRJGfSNanuQ24)
_“Two girls looking happily at the camera.” by [Unsplash](https://unsplash.com/@matheusferrero?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Matheus Ferrero</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

We’ll first create a new image using the GD `imagecreatefromjpeg()` function. We’ll use the [public_path()](https://laravel.com/docs/5.5/helpers#method-public-path) Laravel helper to refer to our image placed in the “public” folder.

```
$output = imagecreatefromjpeg(public_path('friends.jpg'));
```

Next, we’ll create a Cloud Vision `Image` object with this same image and specify that we want to run facial detection:

```
$image = $vision->image(file_get_contents(public_path('friends.jpg')), ['FACE_DETECTION']);
```

You’ll notice a slight change here. Instead of providing the path to the image, we’re supplying the actual image as a string using `file_get_contents()`.

Then we run the `annote()` method on the image:

```
$results = $vision->annotate($image);
```

Now that we have the results, we simply need to loop through the found faces and draw boxes around the them using the vertices supplied in the result:

```
foreach ($results->faces() as $face) {    $vertices = $face->boundingPoly()['vertices'];
```

```
    $x1 = $vertices[0]['x'];    $y1 = $vertices[0]['y'];    $x2 = $vertices[2]['x'];    $y2 = $vertices[2]['y'];
```

```
    imagerectangle($output, $x1, $y1, $x2, $y2, 0x00ff00);}
```

Once this is done, we can output the image and destroy it to free up the memory:

```
header('Content-Type: image/jpeg'); imagejpeg($output); imagedestroy($output);
```

And this is the result:

![Image](https://cdn-media-1.freecodecamp.org/images/8dLhhJCpCUsq8c6rsXjBNRfvOKvVUkir7d0A)

Here is the final controller class code:

```
<?php
```

```
namespace App\Http\Controllers;
```

```
use Google\Cloud\Core\ServiceBuilder;
```

```
class SampleController extends Controller{    public function detectFaces()    {        $cloud = new ServiceBuilder([            'keyFilePath' => base_path('fda.json'),            'projectId' => 'facial-detection-app'        ]);
```

```
        $vision = $cloud->vision();
```

```
        $output = imagecreatefromjpeg(public_path('friends.jpg'));        $image = $vision->image(file_get_contents(public_path('friends.jpg')), ['FACE_DETECTION']);        $results = $vision->annotate($image);
```

```
        foreach ($results->faces() as $face) {            $vertices = $face->boundingPoly()['vertices'];
```

```
            $x1 = $vertices[0]['x'];            $y1 = $vertices[0]['y'];            $x2 = $vertices[2]['x'];            $y2 = $vertices[2]['y'];
```

```
            imagerectangle($output, $x1, $y1, $x2, $y2, 0x00ff00);        }
```

```
        header('Content-Type: image/jpeg');
```

```
        imagejpeg($output);        imagedestroy($output);    }}
```

### Additional functionality

In addition to grabbing the vertices, the response also includes a trove of useful information. This includes the locations of mouths, eyes, eyebrows, noses, etc. Simply `print_r()` the `$face` variable for a quick peek into the available data.

Another great feature is checking whether the detected face is happy, sad, angry, or surprised. You can even detect whether the face is blurry or underexposed, and whether they’re wearing headwear.

If you use this and end up doing something cool as a result, please let me know!

### Upgrade your web dev skills!

[Sign up to my newsletter](https://webdev.chowles.com/) where I’ll share insightful web development articles to supercharge your skills.

Originally published at [www.chowles.com](https://www.chowles.com/easy-facial-detection-in-your-laravel-php-application/) on July 6, 2018.

