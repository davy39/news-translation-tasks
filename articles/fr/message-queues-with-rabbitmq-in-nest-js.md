---
title: Comment configurer des files d'attente de messages pour les tâches asynchrones
  avec RabbitMQ dans les applications Nest.js
subtitle: ''
author: Okoye Chukwuebuka Victor
co_authors: []
series: null
date: '2023-12-14T01:20:25.000Z'
originalURL: https://freecodecamp.org/news/message-queues-with-rabbitmq-in-nest-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/articlePhoto.png
tags:
- name: nestjs
  slug: nestjs
- name: performance
  slug: performance
- name: queue
  slug: queue
- name: web performance
  slug: web-performance
seo_title: Comment configurer des files d'attente de messages pour les tâches asynchrones
  avec RabbitMQ dans les applications Nest.js
seo_desc: 'When you''re developing programs, certain services can block or slow down
  the speed of your application. For example, CPU-intensive tasks like audio transcribing
  or file processing.

  So you might wonder – how do you make sure your application runs with...'
---

Lorsque vous développez des programmes, certains services peuvent bloquer ou ralentir la vitesse de votre application. Par exemple, des tâches intensives en CPU comme la transcription audio ou le traitement de fichiers.

Vous vous demandez peut-être comment vous assurer que votre application fonctionne sans interruption. Pour gérer cela, vous pouvez envoyer des tâches à une file d'attente en dehors du flux de votre application.

## Qu'est-ce qu'une file d'attente de messages ?

Une file d'attente de messages est un outil qui facilite la communication et le transfert de données entre les services au sein d'une seule application (ou externement). Elle stocke ces données ou messages en utilisant le principe First-In-First-Out (FIFO). Cela signifie que les anciennes données passées dans ces files d'attente sont traitées avant les nouvelles données.

Différents composants constituent une file d'attente de messages, tels que :

* **Messages** : Ce sont les données envoyées à la file d'attente. Elles sont souvent appelées jobs.
* **Files d'attente** : Ce sont les structures de données utilisées pour stocker les messages.
* **Producteurs** : Ce sont les services qui envoient des messages ou des données dans le système de file d'attente.
* **Consommateurs** : Ce sont les services qui écoutent la file d'attente et exécutent les messages qui y sont passés.

### Outils de mise en file d'attente de messages

Il existe divers outils de mise en file d'attente de messages que vous pouvez utiliser dans les systèmes asynchrones, comme les suivants :

* **RabbitMQ** : une option fiable et flexible pour implémenter des files d'attente de messages dans les applications.
* **Apache Kafka** : un outil efficace de mise en file d'attente de messages, également très bon pour le traitement de flux d'événements.
* **Redis** : un magasin en mémoire utilisé pour la mise en file d'attente de messages, la mise en cache et le traitement de données.

Notez que certains de ces outils ne sont pas limités à la mise en file d'attente de messages mais peuvent être utilisés à d'autres fins, comme le traitement de flux.

Dans cet article, vous allez créer un projet Nest.js simple qui utilisera RabbitMQ comme fournisseur de services de file d'attente de messages.

Le tutoriel sera divisé en 3 parties :

* [Comment configurer un projet Nest.js pour un flux d'inscription d'utilisateur de base](#heading-comment-configurer-un-projet-nestjs-pour-un-flux-dinscription-dutilisateur-de-base)
* [Comment configurer un service d'email pour l'inscription d'utilisateur](#heading-comment-configurer-un-service-demail-pour-linscription-dutilisateur)
* [Comment intégrer un service de file d'attente en utilisant RabbitMQ](#heading-comment-integrer-un-service-de-file-dattente-en-utilisant-rabbitmq)

### Prérequis

* Vous devez avoir Node installé sur votre système. Si ce n'est pas le cas, voici son site officiel : [https://nodejs.org/en](https://nodejs.org/en).
* Vous devez avoir Node Package Manager (NPM) installé, que vous pouvez télécharger ici si vous ne l'avez pas : [https://docs.npmjs.com/downloading-and-installing-node-js-and-npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
* Vous devez avoir installé RabbitMQ. Voici où vous pouvez l'obtenir au cas où vous ne l'auriez pas encore : [https://www.rabbitmq.com/download.html](https://www.rabbitmq.com/download.html)
* Vous devez avoir un éditeur de texte. Pour cet article, j'utiliserai VSCode. Vous pouvez le télécharger ici : [https://code.visualstudio.com/download](https://code.visualstudio.com/download) ou utiliser l'éditeur de code de votre choix.

## Comment configurer un projet Nest.js

Créer une application Nest.js est rapide et simple si vous utilisez le CLI Nest. Ouvrez votre terminal et entrez la commande suivante pour installer le CLI :

```bash
 $ npm install -g @nestjs/cli
```

Cela installe le CLI Nest.js globalement sur votre système, ce qui signifie que vous pouvez appeler les commandes CLI indépendamment du répertoire dans lequel vous vous trouvez.

Pour créer un projet d'API REST simple, vous allez entrer la commande suivante :

```bash
nest new simple-queue
```

Simple-queue est le nom du répertoire qui sera créé. En entrant cette commande, vous obtenez une invite pour sélectionner un gestionnaire de paquets.

Une fois cela fait, naviguez jusqu'au répertoire créé et ouvrez-le dans votre éditeur de texte en entrant cette commande :

```bash
cd simple-queue && code .
```

Cela ouvre votre éditeur de texte. Nous voulons travailler sur un projet qui montrera au mieux comment une file d'attente de messages peut être utilisée dans un scénario réel, alors configurons un formulaire d'inscription d'utilisateur de base. Une fois les données saisies avec succès, il envoie un email à l'utilisateur, mais vous gérerez le service d'email séparément en le passant dans une file d'attente pour améliorer les performances.

Pour cela, nous allons utiliser une base de données SQLite, TypeOrm, class-validators et le package dotenv afin que vous puissiez sécuriser vos variables de configuration. Allez-y et installez-les en tapant cette commande dans votre terminal :

```bash
npm install --save @nestjs/typeorm typeorm sqlite3 class-validator dotenv
```

Une fois l'installation terminée, allez dans votre module d'application racine, puis incluez la configuration TypeOrm pour votre base de données.

SQLite est une base de données SQL légère qui nous permet de rapidement démarrer et tester des données. Elle est optimale pour ce cas d'utilisation et nous allons maintenant la configurer.

### Configurer la base de données SQLite

```typescript
import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { AppController } from "./app.controller";
import { AppService } from "./app.service";

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type:'sqlite',
      database: 'mini-db.sqlite',
      entities: [__dirname + '/**/*.entity{.ts,.js}'],
      synchronize: true,  
  })],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

Félicitations ! Vous avez connecté avec succès une base de données à votre projet. Il est maintenant temps de créer les services qui géreront l'inscription des utilisateurs.

Pour ce faire, vous devrez revenir à votre cher ami, le CLI Nest. Là, vous entrerez une commande différente pour aider à générer un dossier de ressource pour l'utilisateur, qui contiendra l'entité, le service, le dto et le contrôleur.

Pour ce faire, ouvrez votre terminal et entrez cette commande :

```bash
nest generate resource users
```

Une invite pour sélectionner votre couche de transport sera affichée. Sélectionnez la première, qui est `REST API`. Ensuite, une autre invite vous demandera si vous souhaitez générer des endpoints CRUD, vous pouvez taper Oui. Ensuite, vous pouvez faire des modifications selon vos besoins.

Pour continuer, vous devez d'abord définir quelles informations chaque utilisateur doit avoir. Tout d'abord, créez une entité Utilisateur. Vous pouvez le faire en naviguant vers le fichier d'entité utilisateur dans le sous-dossier d'entité créé dans le dossier utilisateur. Ensuite, définissez les données utilisateur comme ceci :

```typescript
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity('users')
export class User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ length: 100, unique: true })
  username: string;

  @Column({ length: 100, unique: true })
  email: string;
}
```

Pour ce mini-projet, vous utiliserez des données utilisateur de base pour rendre le processus plus rapide. Les champs username et email ont été définis pour être uniques, ce qui signifie qu'il n'y aura pas de doublon de l'instance de données passée pour cette table utilisateur.

Maintenant que cela est fait, modifiez le fichier create user dto qui a été généré comme ceci :

```typescript
import { IsNotEmpty, IsString, IsEmail } from "class-validator";

export class CreateUserDto {
    @IsNotEmpty()
    @IsString()
    username: string;
  
    @IsNotEmpty()
    @IsString()
    @IsEmail()
    email: string;
  }
```

Cela a été créé pour valider la charge utile qui sera envoyée dans votre demande en utilisant le package class-validator.

Maintenant, modifiez la méthode `create` dans le fichier de service utilisateur.

```typescript
import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { CreateUserDto } from "./dto/create-user.dto";
import { User } from "./entities/user.entity";

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private readonly userRepository: Repository<User>
  ) {}
  async create(createUserDto: CreateUserDto): Promise<User> {
    const newUser = this.userRepository.create(createUserDto);
    return await this.userRepository.save(newUser);
  }
}
```

Ensuite, vous allez modifier le fichier contrôleur. Vous avez déjà défini le point de terminaison `create`, donc vous devrez simplement nettoyer les autres points de terminaison qui ne sont pas nécessaires.

```typescript
import { Controller, Post, Body } from "@nestjs/common";
import { CreateUserDto } from "./dto/create-user.dto";
import { UsersService } from "./users.service";

@Controller('users')
export class UsersController {
 constructor(private readonly usersService: UsersService) {}
  @Post()
  create(@Body() createUserDto: CreateUserDto) {
    return this.usersService.create(createUserDto);
  }
}
```

Ouvrez le fichier de module utilisateur et faites quelques ajustements en ajoutant le champ d'importation au décorateur Module et en utilisant la propriété TypeOrmModule.

```typescript
import { Module } from '@nestjs/common';
import { UsersService } from './users.service';
import { UsersController } from './users.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from './entities/user.entity';

@Module({
  imports: [TypeOrmModule.forFeature([User])],
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}
```

Ensuite, démarrez votre serveur en entrant cette commande sur votre terminal : `npm run start:dev`. Une fois le serveur démarré et en cours d'exécution, ouvrez votre client API de choix. Pour cet article, nous utiliserons Postman. Ensuite, faites une requête POST à l'endpoint, qui sera `localhost:3000/users`, en fournissant les données de charge utile requises.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1696695190655/b8b3b246-0961-4655-aaee-081b9ecff35e.png)
_Une requête a été faite et une instance utilisateur a été créée._

Ensuite, il s'agit d'ajouter un service d'email à votre projet qui aidera à notifier les nouveaux utilisateurs qui s'inscrivent.

## Comment configurer un service d'email pour l'inscription d'utilisateur

Pour cela, vous allez utiliser certains packages nécessaires pour créer un service d'email. Ouvrez votre terminal et entrez la commande suivante pour installer ces packages :

```bash
npm install --save @nestjs-modules/mailer nodemailer
```

Une fois ces packages installés, vous pouvez maintenant implémenter le service de messagerie. En utilisant le CLI Nest, créez un module et un service de messagerie en entrant cette commande dans votre terminal :

```bash
nest generate module email && nest generate service email
```

Une fois cela fait, ouvrez le fichier de module nouvellement créé dans le dossier de messagerie. Vous allez utiliser la propriété MailerModule du package `@nestjs-modules/mailer` pour configurer votre service de messagerie ici. Il nécessite un client SMTP dont les clés vous devrez configurer ce MailerModule.

Pour cela, vous pouvez utiliser [https://app.elasticemail.com](https://app.elasticemail.com/api/) pour obtenir ces clés SMTP. Inscrivez-vous et connectez-vous à l'API SMTP. Vous recevrez alors des clés pour votre usage privé.

Notez que ce mode gratuit du client SMTP a des limitations et qu'il ne peut pas envoyer à toutes les adresses email, vous devriez donc utiliser un service d'email de test.

### Comment configurer le module Mailer

Une fois que vous avez configuré cela, retournez à votre application et créez un fichier **.env**. Définissez vos secrets pour les clés SMTP. Ensuite, configurez votre MailerModule comme ceci :

```typescript
import { Global, Module } from "@nestjs/common";
import { EmailService } from "./email.service";
import { MailerModule } from "@nestjs-modules/mailer";

require('dotenv').config();
@Global()
@Module({
  imports: [
    MailerModule.forRoot({
      transport: {
        service: 'QueueTest',
        host: process.env.SMTP_HOST,
        port: process.env.SMTP_PORT,
        auth: {
          user: process.env.SMTP_USER,
          pass: process.env.SMTP_PASSWORD,
        },
      },
      defaults: {
        from: process.env.FROM_EMAIL,
      },
    }),
  ],
  providers: [EmailService]
})
export class EmailModule {}
```

Le décorateur global a été défini afin de s'assurer que le MailModule peut être appelé n'importe où dans votre application. Assurez-vous que vos secrets sont correctement chargés et que vous avez un email valide défini dans **from: process.env.FROM_EMAIL.**

Vérifiez que le EmailModule est également importé dans le module racine App Module de la même manière que votre UsersModule a été importé dans le tableau Imports du App Module.

Ensuite, ouvrez votre fichier de service d'email, vous devrez apporter quelques modifications à la classe EmailService. Ajoutez un constructeur et appelez la propriété MailService du package `@nestjs-modules/mailer`. Ensuite, créez une fonction qui gérera l'envoi des emails.

Voici une classe et une méthode qui font cela :

```typescript
import { MailerService } from '@nestjs-modules/mailer';
import { HttpException, HttpStatus, Injectable } from '@nestjs/common';

@Injectable()
export class EmailService {
  constructor(private mailerService: MailerService) {}
  async sendEmail(options: { email: string; subject: string; html: string;
  }) {
    try {
      const message = {
        to: options.email,
        subject: options.subject,
        html: options.html
      };
      const emailSend = await this.mailerService.sendMail({
        ...message,
      });
      return emailSend;
    } catch (error) {
      throw new HttpException('Error', HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }
}
```

Maintenant, vous avez défini la méthode pour envoyer un email. Vous avez également mis en place un gestionnaire d'exceptions pour une meilleure gestion des erreurs.

Il est maintenant temps d'ajouter ce nouveau service à votre flux d'inscription d'utilisateur.

Naviguez jusqu'à votre fichier de service utilisateur et ajoutez le service de messagerie à votre constructeur en tant que fournisseur. Ensuite, appelez le service dans votre méthode `create user` comme ceci :

```typescript
@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private readonly userRepository: Repository<User>,
    private emailService: EmailService
  ) {}
  async create(createUserDto: CreateUserDto): Promise<User> {
    const newUser = this.userRepository.create(createUserDto);
    const user =  await this.userRepository.save(newUser);
      const emailData = {
        email: user.email,
        subject: 'Bienvenue dans notre communauté',
        html: `<p>Bonjour ${user.username},</p>
        <p>Bienvenue dans notre communauté ! Votre compte est maintenant actif.</p>
        <p>Profitez de votre temps avec nous !</p>`,
      };
      await this.emailService.sendEmail(emailData)
    return user
  }
}
```

Assurez-vous de modifier vos modules afin de corriger toute erreur d'injection de dépendances. Dans votre fichier de module d'email, ajoutez le EmailService au tableau des exports :

```typescript
 providers: [EmailService],
 exports: [EmailService]
```

Ajoutez-le sous vos fournisseurs pour exporter le Email Service afin qu'il puisse être accessible dans d'autres modules. Ensuite, importez le EmailModule dans votre fichier de module utilisateur et ajoutez-le à votre tableau d'importation comme ceci :

```typescript
@Module({
  imports: [TypeOrmModule.forFeature([User]), EmailModule],
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}
```

Il est maintenant temps de le tester. Obtenez un compte gratuit sur n'importe quelle plateforme de test d'email en ligne et ouvrez Postman. Faites une requête à l'endpoint `create user` avec votre email valide. Vous devriez recevoir une réponse par email comme ceci :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1696695108644/25aa9e76-da00-436b-9e43-f0c978f87c6f.png)
_Réponse par email que vous devriez recevoir_

## Comment intégrer un service de file d'attente en utilisant RabbitMQ

Pour commencer, vous devrez installer certains packages qui vous permettent d'implémenter des files d'attente en utilisant RabbitMQ. Entrez la commande suivante pour installer ces packages :

```bash
npm install --save amqplib @types/amqplib amqp-connection-manager
```

### Configurer le service producteur

Une fois l'installation terminée, il est temps de configurer RabbitMQ. Vous allez créer un nouveau dossier dans votre répertoire src et le nommer queues. Ensuite, créez le fichier producteur de file d'attente. Importez ces packages et configurez-les comme ceci :

```typescript
import { HttpException, HttpStatus, Injectable, Logger } from '@nestjs/common';
import amqp, { ChannelWrapper } from 'amqp-connection-manager';
import { Channel } from 'amqplib';

@Injectable()
export class ProducerService {
  private channelWrapper: ChannelWrapper;
  constructor() {
    const connection = amqp.connect(['amqp://localhost']);
    this.channelWrapper = connection.createChannel({
      setup: (channel: Channel) => {
        return channel.assertQueue('emailQueue', { durable: true });
      },
    });
  }

  async addToEmailQueue(mail: any) {
    try {
      await this.channelWrapper.sendToQueue(
        'emailQueue',
        Buffer.from(JSON.stringify(mail)),
        {
          persistent: true,
        },
      );
      Logger.log('Envoyé à la file d\'attente');
    } catch (error) {
      throw new HttpException(
        'Erreur lors de l\'ajout du mail à la file d\'attente',
        HttpStatus.INTERNAL_SERVER_ERROR,
      );
    }
  }
}
```

La connexion AMQP a été établie et fonctionne sur localhost avec le port par défaut de RabbitMQ qui est 5432. Vous avez également établi un canal sur cette connexion avec une option d'entrée qui est exécutée chaque fois qu'un nouveau canal est créé. Cela aide si vous avez une configuration pour ce canal.

Vous avez également créé une `emailQueue` avec la propriété assertQueue qui vérifie qu'une file d'attente avec ce nom n'existe pas déjà. Si elle existe, elle n'a aucun effet, donc elle est idempotente.

Ensuite, vous avez créé une option `durable: true` pour vous assurer que la file d'attente survivra à un redémarrage du serveur.

Ensuite, vous avez défini la méthode pour ajouter les données d'email à une file d'attente. Cela appelle la propriété `sendToQueue` du channelWrapper, en passant le nom de la file d'attente à laquelle vous souhaitez envoyer les données. Idéalement, il devrait s'agir du même nom que celui que vous avez défini avec la propriété assertQueue.

Le deuxième argument est les données de mail, mais d'abord vous les avez converties en une chaîne JSON puis en un Buffer. Vous faites cela parce que les messages dans RabbitMQ sont principalement transmis sous forme de données binaires.

Vous pouvez ensuite définir une option `persistent: true` pour vous assurer que les données envoyées à la file d'attente ne seront pas perdues si le serveur tombe en panne. Ensuite, avec une gestion des erreurs et la méthode pour envoyer des messages à la file d'attente, c'est prêt à partir.

### Configurer le service consommateur

Maintenant que vous avez configuré le service producteur, il est temps de configurer le service consommateur.

Créez un autre fichier dans le sous-dossier de la file d'attente. C'est assez similaire, mais dans ce cas, vous allez consommer les données de la file d'attente. Voici la configuration pour le service consommateur :

```typescript
import { Injectable, OnModuleInit, Logger } from '@nestjs/common';
import amqp, { ChannelWrapper } from 'amqp-connection-manager';
import { ConfirmChannel } from 'amqplib';
import { EmailService } from 'src/email/email.service';

@Injectable()
export class ConsumerService implements OnModuleInit {
  private channelWrapper: ChannelWrapper;
  private readonly logger = new Logger(ConsumerService.name);
  constructor(private emailService: EmailService) {
    const connection = amqp.connect(['amqp://localhost']);
    this.channelWrapper = connection.createChannel();
  }

  public async onModuleInit() {
    try {
      await this.channelWrapper.addSetup(async (channel: ConfirmChannel) => {
        await channel.assertQueue('emailQueue', { durable: true });
        await channel.consume('emailQueue', async (message) => {
          if (message) {
            const content = JSON.parse(message.content.toString());
            this.logger.log('Message reçu :', content);
            await this.emailService.sendEmail(content);
            channel.ack(message);
          }
        });
      });
      this.logger.log('Service consommateur démarré et à l\'écoute des messages.');
    } catch (err) {
      this.logger.error('Erreur lors du démarrage du consommateur :', err);
    }
  }
}

```

Tout d'abord, vous avez défini votre classe consommateur. Pour cela, elle implémente l'interface `onModuleInit` qui est fournie par `@nestJs/common`. Cela spécifie que la classe définie doit avoir une méthode nommée `onModuleInit()`.

Comme le nom l'indique, la méthode sera appelée automatiquement lors de l'initialisation du module, c'est-à-dire lorsque le module contenant cette classe est chargé.

Dans le constructeur de la classe, vous avez ajouté le `emailService` car vous allez utiliser la méthode `sendEmail` de cette classe.

Dans la méthode `onModuleInit()`, vous avez défini un canal. Cela est nécessaire car vous avez besoin d'un canal pour consommer des messages d'une file d'attente.

À partir de cela, le canal est ensuite utilisé pour affirmer une file d'attente qui devrait être similaire en nom et en options à ce que vous avez sur votre service producteur. Si ce n'est pas le cas, vous ne pourrez pas écouter la file d'attente créée sur le service producteur.

Ensuite, vous avez utilisé la méthode consume du canal pour écouter et exécuter le message provenant de la file d'attente que vous avez enregistrée.

Rappelez-vous qu'avant, vous deviez convertir le message en Buffer afin de l'envoyer dans une file d'attente. Maintenant, vous devez le convertir en un objet JavaScript. Ensuite, appelez la méthode emailService pour envoyer un email et passez l'objet JavaScript converti comme argument de cette méthode.

Enfin, vous avez appelé la méthode `ack` qui est utilisée pour informer la file d'attente que le message a été reçu et traité avec succès afin qu'il soit supprimé de la file d'attente.

Maintenant que vous avez défini ces services, créez un fichier de module et placez-les dans le tableau des fournisseurs. Ensuite, exportez le service producteur car vous allez l'appeler dans un autre module.

```typescript
import { Module } from '@nestjs/common';
import { ConsumerService } from './consumer.file';
import { ProducerService } from './producer.file';

@Module({
  providers: [ProducerService, ConsumerService],
  exports: [ProducerService],
})
export class QueueModule {}

```

Ensuite, il faut ajouter les emails envoyés lors de l'inscription des utilisateurs au service de file d'attente que vous venez de créer.

Retournez à votre fichier de service utilisateur et apportez quelques modifications : remplacez le service d'email par le service producteur en tant que fournisseur dans le constructeur, puis appelez le service et la méthode pour ajouter à la file d'attente d'email comme montré ci-dessous :

```typescript
import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { CreateUserDto } from "./dto/create-user.dto";
import { User } from "./entities/user.entity";
import { ProducerService } from "src/queues/producer.file";

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private readonly userRepository: Repository<User>,
    private producerService: ProducerService,
  ) {}
  async create(createUserDto: CreateUserDto): Promise<User> {
    const newUser = this.userRepository.create(createUserDto);
    const user = await this.userRepository.save(newUser);
    const emailData = {
      email: user.email,
      subject: 'Bienvenue dans notre communauté',
      html: `<p>Bonjour ${user.username},</p>
        <p>Bienvenue dans notre communauté ! Votre compte est maintenant actif.</p>
        <p>Profitez de votre temps avec nous !</p>`,
    };
    await this.producerService.addToEmailQueue(emailData);
    return user;
  }
}
```

De plus, dans le fichier de module utilisateur, remplacez le EmailModule par celui du QueueModule pour éviter les erreurs d'injection de dépendances lorsque vous démarrez votre serveur.

```typescript
import { Module } from '@nestjs/common';
import { UsersService } from './users.service';
import { UsersController } from './users.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from './entities/user.entity';
import { QueueModule } from 'src/queues/queue.module';

@Module({
  imports: [TypeOrmModule.forFeature([User]), QueueModule],
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}
```

Maintenant, il est enfin temps de tester à nouveau le flux d'inscription des utilisateurs. Retournez donc à Postman et entrez un email et un nom d'utilisateur valides, puis appuyez sur Entrée. Dans le terminal de votre serveur en cours d'exécution, vous verrez des logs qui ont été définis afin de suivre la manière dont le message a été envoyé et comment il a été reçu et exécuté.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1696982914939/7f28f0e3-22e3-462c-8956-0bd2156d4c10.png)
_Logs qui vous aident à suivre le message_

Vous pouvez également ouvrir le tableau de bord de RabbitMQ pour visualiser l'activité des files d'attente sur [http://localhost:15672](http://localhost:15672/). Par défaut, l'utilisateur est "guest", donc entrez `guest` pour le nom d'utilisateur et le mot de passe.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1702377899227/4158d8b2-2b9b-424e-bd0b-a4203648eb50.png)
_Files d'attente et flux RabbitMQ_

Voici le lien vers le [dépôt GitHub](https://github.com/ChuloWay/article-nestjs-queue). N'hésitez pas à le consulter chaque fois que vous êtes bloqué.

## Conclusion

Dans cet article, vous avez appris ce qu'est une file d'attente de messages ainsi que certains composants majeurs de leur fonctionnement. Vous avez également construit un mini-projet Nest.js et implémenté un service d'email. Enfin, vous avez intégré le service de file d'attente dans votre projet, montrant comment il fonctionne dans un scénario réel.

Comprendre les comportements et les modèles de file d'attente de messages est une compétence essentielle lors du développement d'applications scalables. Cela aide à réduire le lag et améliore la vitesse et l'efficacité de vos applications.

J'espère que vous avez apprécié la lecture de cet article. Vous pouvez me suivre sur [Twitter](https://twitter.com/OkoyeVictorr).