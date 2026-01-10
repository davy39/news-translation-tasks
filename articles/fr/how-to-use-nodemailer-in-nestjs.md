---
title: Comment envoyer des emails avec Nodemailer dans NestJS
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
seo_title: Comment envoyer des emails avec Nodemailer dans NestJS
seo_desc: 'By Okure U. Edet

  While learning Nestjs, I wanted to be able to send test emails with Nodemailer but
  I had difficulty doing this in the context of a NestJS application. I searched the
  internet for a solution and after much research, I found one. It tu...'
---

Par Okure U. Edet

En apprenant NestJS, je voulais pouvoir envoyer des emails de test avec Nodemailer, mais j'ai eu du mal à le faire dans le contexte d'une application NestJS. J'ai recherché une solution sur Internet et, après beaucoup de recherches, j'en ai trouvé une. Il s'est avéré que c'était vraiment simple.

Dans cet article, je vais partager ma solution afin que vous puissiez l'utiliser dans vos projets NestJS.

## Table des matières
- [Comment configurer un projet NestJS](#heading-comment-configurer-un-projet-nestjs)
- [Comment configurer Nodemailer dans votre application](#heading-comment-configurer-nodemailer-dans-votre-application)
- [Comment envoyer des emails avec Nodemailer](#heading-comment-envoyer-des-emails-avec-nodemailer)
- [Conclusion](#heading-conclusion)

### Comment configurer un projet NestJS

Idéalement, lorsqu'un utilisateur clique sur un lien de mot de passe oublié, un lien doit être envoyé à l'email de l'utilisateur, et via ce lien, l'utilisateur doit pouvoir réinitialiser son mot de passe. Cet article démontrera un scénario de test de la manière dont cela fonctionne en utilisant Nodemailer.

Ouvrez votre IDE préféré ou naviguez vers le terminal et collez la commande suivante :

```
$ npm i -g @nestjs/cli
$ nest new nodemailer-app
```

Les commandes ci-dessus génèrent un nouveau projet appelé `nodemailer-app`.

Après avoir fait cela, naviguez vers votre dossier de projet et installez les packages Nodemailer, `npm i --save @nestjs-modules/mailer nodemailer` et les types, `npm i --save-dev @types/nodemailer`.

### Comment configurer Nodemailer dans votre application

Avant de continuer, assurez-vous d'avoir un compte sur [mailtrap.io](https://mailtrap.io/). Si vous en avez un, connectez-vous simplement et naviguez vers **Email Testing**. Créez votre propre boîte de réception si vous n'en avez pas. Naviguez vers la boîte de réception et vous devriez voir vos identifiants qui seront utilisés pour configurer Nodemailer dans votre application.

Dans votre répertoire de projet, allez dans le fichier de module de l'application et configurez le package :

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

Dans le code ci-dessus, vous avez importé le `MailerModule` depuis `@nestjs-modules/mailer`. Ensuite, vous avez appelé une méthode `forRoot()` sur celui-ci. À l'intérieur de la méthode `forRoot()`, vous avez spécifié une propriété transport qui contient les propriétés host et auth.

N'oubliez pas d'obtenir l'hôte, le port, le nom d'utilisateur et le mot de passe à partir de vos identifiants dans votre boîte de réception sur [mailtrap.io](https://mailtrap.io/).

Vous pouvez créer un fichier `.env` qui contiendra tous vos détails d'identification. Il est conseillé de le faire. Pour pouvoir charger le fichier `.env` approprié dans NestJS, installez ceci :

```
$ npm i --save @nestjs/config
```

Ensuite, dans votre fichier `app.module.ts`, importez un `ConfigModule` :

```
import { ConfigModule } from '@nestjs/config';
```

Toujours dans votre fichier `app.module.ts`

```
// inclure le module de configuration dans votre tableau d'imports

@Module({
  imports: [
    ConfigModule.forRoot({ envFilePath: '.env', isGlobal: true }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
```


### Comment envoyer des emails avec NodeMailer

Après avoir configuré Nodemailer, il est temps d'envoyer des emails avec celui-ci.

Dans votre fichier `app.service.ts`, collez le code suivant :

```
import { MailerService } from '@nestjs-modules/mailer';
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  constructor(private readonly mailService: MailerService) {}

  sendMail() {
    const message = `Vous avez oublié votre mot de passe ? Si vous n'avez pas oublié votre mot de passe, veuillez ignorer cet email !`;

    this.mailService.sendMail({
      from: 'Kingsley Okure <kingsleyokgeorge@gmail.com>',
      to: 'joanna@gmail.com',
      subject: `Comment envoyer des emails avec Nodemailer`,
      text: message,
    });
  }
}

```

Dans le fichier `app.service.ts`, le `MailerService` est injecté puis utilisé dans la classe pour envoyer l'email. À l'intérieur de la classe, le `MailerService` dispose d'une fonction `sendMail` qui prend un objet en tant que paramètre. L'objet contient les propriétés `from`, `to`, `subject` et `text`.

Une fois que vous avez fait cela, dans le fichier `app.controller.ts`, collez le code suivant :

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

Tout ce qui est fait dans le contrôleur est de créer une requête `Get` qui appellera la fonction `sendMail` que vous avez créée dans le service.

Idéalement, dans une application réelle, tout cela sera fait dans une fonction de mot de passe oublié. Et un email sera envoyé à l'utilisateur une fois qu'il clique sur un lien de mot de passe oublié.

Pour tester cette petite configuration, ouvrez votre Postman et allez sur localhost:3000 et envoyez.

Ensuite, allez dans votre boîte de réception [mailtrap.io](https://mailtrap.io/inboxes/2445842/messages) et voyez votre message.


### Conclusion

Dans cet article, vous avez appris comment envoyer des emails avec Nodemailer, un logiciel conçu pour aider les développeurs à envoyer des emails à plusieurs personnes à la fois.

Vous avez également appris comment le configurer et le mettre en place dans le contexte d'une application NestJS.

Si vous souhaitez me contacter, vous pouvez me suivre sur [Twitter](https://twitter.com/itzz_okure) ou sur [Linkedin](https://www.linkedin.com/in/okure/)