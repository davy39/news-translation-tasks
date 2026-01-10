---
title: How to use AWS Amplify and Angular to Build Cloud Enabled JavaScript Applications
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-24T21:01:47.000Z'
originalURL: https://freecodecamp.org/news/building-cloud-enabled-javascript-applications-with-aws-amplify-angular-682547fc6477
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EB-8t3dR5qMQYNXyqgM2wQ.png
tags:
- name: Angular
  slug: angular
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: serverless
  slug: serverless
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nader Dabit

  AWS Amplify helps you add functionality like storage, GraphQL, authentication, analytics,
  pub-sub, and internationalization to your JavaScript applications.

  While you can integrate AWS Amplify into any JavaScript framework, Angular com...'
---

By Nader Dabit

[AWS Amplify](https://aws.github.io/aws-amplify/?utm_source=blog&utm_campaign=amplify_angular_medium_nader) helps you add functionality like storage, GraphQL, authentication, analytics, pub-sub, and internationalization to your JavaScript applications.

While you can integrate AWS Amplify into _any_ JavaScript framework, Angular components have recently been added making it easier than before to get up and running with cloud services in an Angular application.

In this post, we’ll take a look at how to get up and running with AWS Amplify in an Angular application.

### Getting Started

#### Installing dependencies

To get started, we need in install a couple of dependencies: AWS Amplify and AWS Amplify Angular:

```bash
$ npm install --save aws-amplify
$ npm install --save aws-amplify-angular
```

#### Creating a new AWS Mobile Project

If you already have an AWS project you would like to use, you can skip this step. If not, you you will learn how we can use the AWS Mobile Hub to quickly get up and running with AWS services like Amazon Cognito for authentication, Amazon Pinpoint for analytics, AWS AppSync for managed GraphQL, and Amazon S3 for storage.

The next thing we need to do here is install the AWS Mobile CLI:

```bash
npm i -g awsmobile-cli
```

Next, we will need to configure the AWS Mobile CLI to use your preferred IAM credentials.

> If you are new to AWS and would like to see how to set this up for the first time, check out [this](https://www.youtube.com/watch?v=MpugaNKtw3k) video.

```bash
awsmobile configure
```

Now, ourAWS Mobile CLI is ready to go and we can create a new project.

Let’s create a new project that has analytics, storage, and authentication enabled:

```bash
awsmobile init

awsmobile user-signin enable
awsmobile user-files enable
awsmobile push
```

After creating your backend, the configuration file is copied to `/awsmobilejs/#current-backe`

#### Viewing your project in the AWS Console

Now that you’ve created your project from the CLI, you can view your project in AWS Mobile hub by visiting [https://console.aws.amazon.com/mobilehub/home](https://console.aws.amazon.com/mobilehub/home?region=us-east-1) and clicking on the name of your project.

### Working in Angular

To import the configuration file to your Angular app, you will need to rename `aws_exports.js` to `aws_exports.ts`.

To import the configuration file to your Angular app, you will need to rename `aws_exports.js` to `aws_exports.ts`.

```js
import Amplify from 'aws-amplify'
import awsmobile from './aws-exports'
Amplify.configure(aws_exports)
```

When working with underlying `aws-js-sdk`, the “node” package should be included in _types_ compiler option. Make sure that you edit the `tsconfig.app.json` file in your source file folder, e.g. `_src/tsconfig.app.json_`.

```json
"compilerOptions": {
  "types" : ["node"]
}
```

#### Importing Amplify

In your [root module](https://angular.io/guide/bootstrapping) `src/app/app.module.ts`, you can import AWS Amplify modules as following:

```ts
import { AmplifyAngularModule, AmplifyService } from 'aws-amplify-angular'

@NgModule({
  ...
  imports: [
    ...
    AmplifyAngularModule
  ],
  ...
  providers: [
    ...
    AmplifyService
  ]
  ...
})
```

> The service provider is optional. You can import the core categories normally i.e. `import { Analytics } from 'aws-amplify'` or create your own provider. The service provider does some work for you and exposes the categories as methods. The provider also manages and dispatches authentication state changes using observables which you can subscribe to within your components (see below).

#### Using the AWS Amplify Service

AmplifyService is a provider in your Angular app, and it provides AWS Amplify core categories through dependency injection.

To use _AmplifyService_ with [dependency injection](https://angular.io/guide/dependency-injection-in-action), inject it into the constructor of any component or service, anywhere in your application.

```ts
import { AmplifyService } from 'aws-amplify-angular';

...
constructor(
    public navCtrl:NavController,
    public amplifyService: AmplifyService,
    public modalCtrl: ModalController
) {
    this.amplifyService = amplifyService;
}
...
```

#### Using AWS Amplify Categories

You can access and work directly with AWS Amplify Categories via the built-in service provider:

```ts
import { Component } from '@angular/core';
import { AmplifyService }  from 'aws-amplify-angular';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  
  constructor( public amplify:AmplifyService ) {
      
      this.amplifyService = amplify;

      /** now you can access category APIs:
       * this.amplifyService.auth();          // AWS Amplify Auth
       * this.amplifyService.analytics();     // AWS Amplify Analytics
       * this.amplifyService.storage();       // AWS Amplify Storage
       * this.amplifyService.api();           // AWS Amplify API
       * this.amplifyService.cache();         // AWS Amplify Cache
       * this.amplifyService.pubsub();        // AWS Amplify PubSub
     **/
  }
  
}
```

#### Usage Example: Subscribe to Authentication State Changes

Import AmplifyService into your component and listen for auth state changes:

```ts
import { AmplifyService }  from 'aws-amplify-angular';

  // ...
constructor( public amplifyService: AmplifyService ) {

    this.amplifyService = amplifyService;

    this.amplifyService.authStateChange$
        .subscribe(authState => {
        this.signedIn = authState.state === 'signedIn';
        if (!authState.user) {
            this.user = null;
        } else {
            this.user = authState.user;
            this.greeting = "Hello " + this.user.username;
        }
        });

}
```

#### View Components

AWS Amplify also provides components that you can use in your Angular view templates, including an authenticator component, a photo picker component, and an Amazon S3 album component.

**Authenticator**

Authenticator component creates an out-of-the-box signing/sign-up experience for your Angular app. To use Authenticator, just add the `amplify-authenticator` directive in your .html view:

```ts
<amplify-authenticator></amplify-authenticator>
```

**Photo Picker**

Photo Picker component will render a file upload control that will allow choosing a local image and uploading it to Amazon S3. Once an image is selected, a base64 encoded image preview will be displayed automatically.

To render photo picker in an Angular view, use the _`amplify-photo-picker`_ component:

```ts
<amplify-photo-picker 
    (picked)="onImagePicked($event)"
    (loaded)="onImageLoaded($event)">
</amplify-photo-picker>
```

The component will emit two events:

* `(picked)` - Emitted when an image is selected. The event will contain the `File` object which can be used for upload.
* `(loaded)` - Emitted when an image preview has been rendered and displayed.

**Uploading an image**

Use `onImagePicked(event)` to upload your photo to Amazon S3 using AWS Amplify Storage category:

```ts
onImagePicked( file ) {

    let key = `pics/${file.name}`;
    
    this.amplify.storage().put( key, file, {
      'level': 'private',
      'contentType': file.type
    })
    .then (result => console.log('uploaded: ', result))
    .catch(err => console.log('upload error: ', err));
  
}
```

#### S3 Album

The Amazon S3 Album component displays a list of images from the connected S3 bucket.

To render the album, use the `_amplify-s3-album_` component in your Angular view:

```ts
<amplify-s3-album
  path="pics" (selected)="onAlbumImageSelected($event)"
>
</amplify-s3-album>
```

`(selected)` event can be used to retrieve the URL of the clicked image on the list:

```ts
onAlbumImageSelected( event ) {
      window.open( event, '_blank' );
}
```

**Custom Styles**

You can use custom styling for AWS Amplify components. Just import your custom _styles.css_ that overrides the default styles which can be found in `/node_modules/aws-amplify-angular/theme.css`.

### Conclusion

AWS Amplify is open source and actively being developed, and we’d love any feedback and / or issues from customers or users to help us in our future roadmap.

Feel free to check out the docs [here](https://aws.github.io/aws-amplify/), or the GitHub repo [here](https://github.com/aws/aws-amplify).

My Name is [Nader Dabit](https://twitter.com/dabit3) . I am a Developer Advocate at [AWS Mobile](https://aws.amazon.com/mobile/) working with projects like [AWS AppSync](https://aws.amazon.com/appsync/) and [AWS Amplify](https://aws.github.io/aws-amplify/?utm_source=blog&utm_campaign=amplify_angular_medium_nader), and the founder of [React Native Training](http://reactnative.training/).

