---
title: How to make image upload easy with Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T15:07:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-image-upload-easy-with-angular-1ed14cb2773b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dxawCwfllIh8ljUcRtwnXg.png
tags:
- name: Angular
  slug: angularjs
- name: image
  slug: image
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Filip Jerga

  This is the second part of the tutorial on how to upload an image to Amazon S3.
  You can find the first part here. In this article, we will take a look at the Angular
  Part.

  You can also watch my step by step video tutorial of an image u...'
---

By Filip Jerga

This is the second part of the tutorial on how to upload an image to Amazon S3. You can find the first part [here](https://medium.freecodecamp.org/how-to-set-up-simple-image-upload-with-node-and-aws-s3-84e609248792). In this article, we will take a look at the Angular Part.

**You can also watch my step by step video tutorial of an image upload. The link is provided at the bottom of this article.**

### 1. Create a template first

First, we want to create a reusable component that will be easily pluggable into other components.

Let’s start with a simple HTML template for our input. Don’t forget to apply styles of your choice, or you can get them from my [GitHub repo](https://gist.github.com/Jerga99/7fe7b1942c6e5bbe4723f2369c760649).

```ts
<label class="image-upload-container btn btn-bwm">
  <span>Select Image</span>
  <input #imageInput
         type="file"
         accept="image/*"
         (change)="processFile(imageInput)">
</label>
```

Important here is a **type** of input, which is set to a **file.** The **Accept** attribute defines accepted files for input. **Image/*** specifies that we can choose images of any type by this input. **#imageInput** is a reference of input on which we can access uploaded files.

A **Change** event is fired when we select a file. So let’s take a look at the class code.

### 2. Don’t forget for Component Code

```ts
class ImageSnippet {
  constructor(public src: string, public file: File) {}
}

@Component({
  selector: 'bwm-image-upload',
  templateUrl: 'image-upload.component.html',
  styleUrls: ['image-upload.component.scss']
})
export class ImageUploadComponent {

  selectedFile: ImageSnippet;

  constructor(private imageService: ImageService){}

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', (event: any) => {

      this.selectedFile = new ImageSnippet(event.target.result, file);

      this.imageService.uploadImage(this.selectedFile.file).subscribe(
        (res) => {
        
        },
        (err) => {
        
        })
    });

    reader.readAsDataURL(file);
  }
}
```

Let’s break down this code. You can see in the **processFile** that we are getting an image input we sent from the **change** event. By writing **imageInput.files[0]** we are accessing the first **file**. We need a **reader** in order to access additional properties of a file. By calling **readAsDataURL,** we can get a base64 representation of an image in the callback function of the **addEventListener** we subscribed to before.

In a callback function, we are creating an instance of the **ImageSnippet. The first** value is a base64 representation of an image we will display later on the screen. **The second** value is a file itself, which we will send to the server for upload to Amazon S3.

Now, we just need to provide this file and send a request through a service.

### 3. We need a service as well

It wouldn’t be an Angular app without a service. The service will be the one responsible for sending a request to our Node server.

```ts
export class ImageService {

  constructor(private http: Http) {}


  public uploadImage(image: File): Observable<Response> {
    const formData = new FormData();

    formData.append('image', image);

    return this.http.post('/api/v1/image-upload', formData);
  }
}
```

As I told you in the previous lecture, we need to send an image as part of the **form data**. We will append the image under the key of an **image** to form data (same key we configured before in Node). Finally, we just need to send a request to the server with **formData** in a payload.

**Now we can celebrate. That’s it! Image sent to upload!**

In the next lines, I will provide some additional code for a better user experience.

### 4. Additional UX Updates

```ts
class ImageSnippet {
  pending: boolean = false;
  status: string = 'init';

  constructor(public src: string, public file: File) {}
}

@Component({
  selector: 'bwm-image-upload',
  templateUrl: 'image-upload.component.html',
  styleUrls: ['image-upload.component.scss']
})
export class ImageUploadComponent {

  selectedFile: ImageSnippet;

  constructor(private imageService: ImageService){}

  private onSuccess() {
    this.selectedFile.pending = false;
    this.selectedFile.status = 'ok';
  }

  private onError() {
    this.selectedFile.pending = false;
    this.selectedFile.status = 'fail';
    this.selectedFile.src = '';
  }

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', (event: any) => {

      this.selectedFile = new ImageSnippet(event.target.result, file);

      this.selectedFile.pending = true;
      this.imageService.uploadImage(this.selectedFile.file).subscribe(
        (res) => {
          this.onSuccess();
        },
        (err) => {
          this.onError();
        })
    });

    reader.readAsDataURL(file);
  }
}
```

We added new properties to the **ImageSnippet: Pending** and **Status. Pending** can be false or true, depending if an image is currently being uploaded. **Status** is the result of the uploading process. It can be **OK** or **FAILED.**

**OnSuccess** and **onError** are called after image upload and they set the status of an image.

Ok, now let’s take a look at the updated template file:

```ts
<label class="image-upload-container btn btn-bwm">
  <span>Select Image</span>
  <input #imageInput
         type="file"
         accept="image/*"
         (change)="processFile(imageInput)">
</label>


<div *ngIf="selectedFile" class="img-preview-container">

  <div class="img-preview{{selectedFile.status === 'fail' ? '-error' : ''}}"
       [ngStyle]="{'background-image': 'url('+ selectedFile.src + ')'}">
  </div>

  <div *ngIf="selectedFile.pending" class="img-loading-overlay">
    <div class="img-spinning-circle"></div>
  </div>

  <div *ngIf="selectedFile.status === 'ok'" class="alert alert-success"> Image Uploaded Succesfuly!</div>
  <div *ngIf="selectedFile.status === 'fail'" class="alert alert-danger"> Image Upload Failed!</div>
</div>
```

Here we are displaying our uploaded image and errors on the screen depending on the **state** of an **image**. When the image is pending, we also display a nice spinning image to notify the user of uploading activity.

### 5. Add some styling

Stylings are not the focus of this tutorial, so you can get all of the SCSS styles in this [link](https://gist.github.com/Jerga99/7fe7b1942c6e5bbe4723f2369c760649).

**Job done! :) That should be it for a simple image upload. If something is not clear, make sure you watched the first part of this tutorial first.**

If you like this tutorial, feel free to check my full course on Udemy **— [The Complete Angular, React & Node Guide | Airbnb style app](http://bit.ly/2NeWna4).**

**Completed Project:** [My GitHub repository](https://github.com/Jerga99/bwm-ng)

**Video Lecture**: [YouTube Tutorial](https://www.youtube.com/watch?v=wNqwExw-ECw)

Cheers,

Filip

