---
title: How to Send Emails With Nodemailer in NestJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-04-10T11:52:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-nodemailer-in-nestjs
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/joanna-kosinska-uGcDWKN91Fs-unsplash.jpg
tags:
- name: email
  slug: email
- name: nestjs
  slug: nestjs
- name: projects
  slug: projects
seo_title: null
seo_desc: 'By Okure U. Edet

  While learning Nestjs, I wanted to be able to send test emails with Nodemailer but
  I had difficulty doing this in the context of a NestJS application. I searched the
  internet for a solution and after much research, I found one. It tu...'
---

By Okure U. Edet

While learning Nestjs, I wanted to be able to send test emails with Nodemailer but I had difficulty doing this in the context of a NestJS application. I searched the internet for a solution and after much research, I found one. It turned out to be really simple.

In this article, I will share my solution so you can use it in your NestJS projects.

## Table of Contents
- [How to Set Up a NestJS Project](#heading-how-to-set-up-a-nestjs-project)
- [How to Configure Nodemailer in Your App](#heading-how-to-configure-nodemailer-in-your-app)
- [How to Send emails with Nodemailer](#heading-how-to-send-emails-with-nodemailer)
- [Conclusion](#heading-conclusion)

### How to Set Up a NestJS Project

Ideally, when a user clicks on a forget password route, a link should be sent to the user's email, and through that link, the user should be able to reset their password. This article will demonstrate a test case scenario of how this works using Nodemailer.

Open your favorite IDE or navigate to the terminal and paste the following command:

```
$ npm i -g @nestjs/cli
$ nest new nodemailer-app
```

The above commands generates a new project called  `nodemailer-app`. 

After doing this, navigate to your project folder and install the Nodemailer packages, `npm i --save @nestjs-modules/mailer nodemailer` and types, `npm i --save-dev @types/nodemailer`.

### How to Configure Nodemailer in Your App

Before moving on, make sure you have an account on [mailtrap.io](https://mailtrap.io/). If you do, just login and navigate to **Email Testing**. Create your own inbox if you don't have one. Navigate to the inbox and you should see your credentials which will be used to configure Nodemailer in your application.

In your project directory, go to the app module file and configure the package:

```
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { MailerModule } from '@nestjs-modules/mailer';

@Module({
  imports: [
    AuthModule,
    MailerModule.forRoot({
      transport: {
        host: process.env.EMAIL_HOST,
        auth: {
          user: process.env.EMAIL_USERNAME,
          pass: process.env.EMAIL_PASSWORD,
        },
      },
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

```

In the above code, you imported the `MailerModule` from `@nestjs-modules/mailer`. Then you called a `forRoot()` method on it. Inside the `forRoot()` method, you specified a transport property which contains the host and auth properties.

Do not forget to get the host, port, username and password from your credentials in your inbox on [mailtrap.io](https://mailtrap.io/).

You can create a `.env` file which would house all your credential details. It is advisable to do so. To be able to load the appropriate `.env` file in NestJS, install this:

```
$ npm i --save @nestjs/config
```

Then in your `app.module.ts` file, import a `ConfigModule`:

```
import { ConfigModule } from '@nestjs/config';
```

Still in your `app.module.ts`

```
// include the config module in your imports array

@Module({
  imports: [
    ConfigModule.forRoot({ envFilePath: '.env', isGlobal: true }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
```


### How to Send Emails with NodeMailer

After configuring Nodemailer, it is time to send emails with it.

In your `app.service.ts` file, paste the following code:

```
import { MailerService } from '@nestjs-modules/mailer';
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  constructor(private readonly mailService: MailerService) {}

  sendMail() {
    const message = `Forgot your password? If you didn't forget your password, please ignore this email!`;

    this.mailService.sendMail({
      from: 'Kingsley Okure <kingsleyokgeorge@gmail.com>',
      to: 'joanna@gmail.com',
      subject: `How to Send Emails with Nodemailer`,
      text: message,
    });
  }
}

```

In the `app.service.ts` file, the `MailerService` is injected and then used in the class to send the email. Inside the class, the `MailerService` has a `sendMail` function which takes in an object as a parameter. The object contains a `from`, `to`, `subject` and `text` property.

Once you have done this, in the `app.controller.ts` file, paste the following code:

```
import { Controller, Get, Res } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  sendMailer(@Res() response: any) {
    const mail = this.appService.sendMail();

    return response.status(200).json({
      message: 'success',
      mail,
    });
  }
}

```

All that is done in the controller is to create a `Get` request which will call the `sendMail` function you have created in the service.

Ideally, in a real world application, all this will be done in a forgot password function. And an email will be sent to the user once they click on a forgot password route.

To test this little setup, open your Postman and go to localhost:3000 and hit send.

Then go to your [mailtrap.io](https://mailtrap.io/inboxes/2445842/messages) inbox and see your message.


### Conclusion

In this article, you have learned how to send emails with Nodemailer, a software designed to help developers send emails to multiple people at once. 

You have also learned how to configure and set it up in the context of a NestJs application.

If you want to connect with me, you can follow me on [Twitter](https://twitter.com/itzz_okure) or on [Linkedin](https://www.linkedin.com/in/okure/)

