---
title: Comment télécharger des fichiers vers Azure en utilisant NestJS et typeORM
  avec MySQL
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2022-10-21T23:13:08.000Z'
originalURL: https://freecodecamp.org/news/upload-files-to-azure-using-nestjs-and-typeorm-with-mysql
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-panumas-nikhomkhai-1148820.jpg
tags:
- name: Azure
  slug: azure
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: nestjs
  slug: nestjs
seo_title: Comment télécharger des fichiers vers Azure en utilisant NestJS et typeORM
  avec MySQL
seo_desc: 'Images and videos are examples of huge files that might be stored in your
  database. And this might impact the performance of your applications because of
  the amount of space that those files can take up.

  Also, it expands the database, which makes bac...'
---

Les images et les vidéos sont des exemples de fichiers volumineux qui pourraient être stockés dans votre base de données. Et cela pourrait impacter les performances de vos applications en raison de l'espace que ces fichiers peuvent occuper.

De plus, cela étend la base de données, ce qui rend les sauvegardes plus grandes et plus lentes. Par conséquent, ce n'est pas considéré comme une bonne pratique. Au lieu de cela, utiliser un système distribué pour sauvegarder les fichiers et ajouter une référence à ces fichiers dans notre base de données est un bon choix.

Dans cet article, vous apprendrez comment télécharger ces fichiers vers les services distribués dans le cloud Azure et les supprimer d'Azure en utilisant NestJS, un framework Node populaire.

## Table des matières

* [Qu'est-ce qu'un système distribué dans le cloud](#heading-quest-ce-quun-systeme-distribue-dans-le-cloud) ?
  
* [Qu'est-ce qu'Azure](#heading-quest-ce-quazure) ?
  
* [Prise en main](#heading-prise-en-main)
  
* [Comment se connecter à Azure](#heading-comment-se-connecter-a-azure)
  
* [Comment configurer NestJS et la base de données MySQL](#heading-comment-configurer-nestjs-et-la-base-de-donnees-mysql)
  
* [Comment se connecter à Azure Blob via le SDK](#how-to-connect-to-azure-blob-through-sdk)
  
* [Comment télécharger l'image via l'API](#heading-comment-telecharger-limage-via-lapi)
  
* [Comment créer un endpoint pour télécharger des images](#heading-comment-creer-un-endpoint-pour-telecharger-des-images)
  
* [Comment supprimer des fichiers](#heading-comment-supprimer-des-fichiers)
  
* [Résumé](#heading-resume)
  

## Qu'est-ce qu'un système distribué dans le cloud ?

Un système distribué est composé de plusieurs parties indépendantes réparties sur plusieurs appareils. Ils communiquent entre eux via des messages pour atteindre des objectifs communs.

En conséquence, pour l'utilisateur final, le système distribué apparaîtra comme une seule interface ou un seul ordinateur. Ensemble, le système est censé maximiser l'utilisation des informations et des ressources tout en prévenant les erreurs, car même si un système tombe en panne, le service restera disponible.

## Qu'est-ce qu'Azure ?

Azure est une plateforme de cloud computing public qui offre des solutions pour l'analyse, le calcul virtuel, le stockage, la mise en réseau et bien plus encore.

Ces solutions incluent l'Infrastructure en tant que Service (IaaS), la Plateforme en tant que Service (PaaS) et le Logiciel en tant que Service (SaaS). Vous pouvez compléter ou remplacer vos serveurs sur site avec celui-ci.

Les blobs, les tables et les files d'attente sont les trois principaux services de données fournis par Azure. Ces services sont tous largement distribués, hautement scalables et fiables. Nous utiliserons l'un de ces services dans cet article.

## Prise en main

Avant de commencer à suivre ce tutoriel, assurez-vous d'avoir les éléments suivants prêts :

* Un abonnement Azure – Vous pouvez [vous inscrire](https://azure.microsoft.com/en-us/free/?WT.mc_id=academic-75638-bethanycheum) pour un compte Azure gratuit si vous n'en avez pas déjà un.
  
* Des connaissances de base et des installations de NestJS et de la base de données serveur MySQL. En savoir plus dans la [documentation NestJS](https://docs.nestjs.com/).
  

## Comment se connecter à Azure

L'une des solutions de stockage d'objets basées sur le cloud de Microsoft est appelée Blob. Le stockage blob est idéal pour le stockage de données non structurées à grande échelle. Les données non structurées, telles que le texte ou les données binaires, sont des données qui ne suivent pas un modèle ou une description de données spécifique.

### Comment créer un stockage blob

**Étape 1** : Le tableau de bord Azure est visible une fois que vous avez créé un compte et que vous êtes connecté au site Azure. Sélectionnez `Comptes de stockage` dans le menu ou utilisez la barre de recherche.

![création d'un stockage blob étape 1](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-15-20-52-47-2.png align="left")

*Création d'un stockage blob étape 1*

**Étape 2** : Choisissez `créer` ou `Créer un compte de stockage` si vous n'avez pas de compte de stockage existant dans le menu de la boîte suivante.

![création d'un stockage blob étape 2](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-15-20-54-28-2.png align="left")

*Création d'un stockage blob étape 2*

**Étape 3** : Dans cette fenêtre, nous devons remplir l'abonnement, le groupe de ressources, le nom du compte de stockage, la région, la performance et la redondance.

![création d'un stockage blob étape 3](https://www.freecodecamp.org/news/content/images/2022/10/screencapture-portal-azure-2022-10-15-20_55_56-4.png align="left")

*Création d'un stockage blob étape 3*

* L'`Abonnement` permet à Azure de suivre où facturer pour la ressource utilisée. Vous pouvez utiliser votre abonnement gratuit ici.
  
* Un `groupe de ressources` est un regroupement central pour votre/vos ressource(s). Il vous aide à structurer et organiser vos ressources Azure en fonction de vos besoins.
  
* Le `Nom du compte de stockage` doit être un nom **unique** au niveau mondial.
  
* `Performance` vous offre différents types de stockage tels que HDD et SSD. Ici, nous utilisons Standard.
  
* `Redondance` aide à protéger votre stockage contre les défaillances de centre de données ou de région en dupliquant votre ressource vers d'autres régions.
  

**Étape 4** : Ensuite, cliquez sur `réviser` pour valider vos options. Après avoir terminé la validation, vous pouvez cliquer sur le bouton `Créer` pour créer le compte de stockage. (Notez ici que nous avons laissé toutes les autres options par défaut.)

![création d'un stockage blob étape 4](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-15-20-59-35-3.png align="left")

*Création d'un stockage blob étape 4*

Lorsque la création est réussie, la fenêtre suivante devrait apparaître :

![création d'un stockage blob étape 5](https://www.freecodecamp.org/news/content/images/2022/10/screencapture-portal-azure-2022-10-15-21_01_08-2.png align="left")

*Création d'un stockage blob étape 5*

**Étape 5** : Ensuite, sélectionnez `Aller à la ressource` pour être redirigé vers le tableau de bord du compte de stockage. La barre latérale gauche est alors visible et contient plusieurs options. Choisissez l'option `conteneurs`, qui se trouve dans la section Stockage de données.

![création d'un stockage blob étape 5](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-15-21-02-50-3.png align="left")

*Création d'un stockage blob étape 5*

**Étape 6** : dans le tableau de bord des conteneurs, cliquez maintenant sur `+ Conteneur`, puis un formulaire apparaîtra sur le côté droit. Remplissez le formulaire en donnant le **nom** et le **niveau d'accès public** (vous pouvez utiliser n'importe quelle option selon vos besoins) pour le conteneur. Vous pouvez créer n'importe quel nombre de conteneurs sous un compte de stockage.

![création d'un stockage blob étape 6](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-15-21-04-07-3.png align="left")

*Création d'un stockage blob étape 6*

![création d'un stockage blob étape 6](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-15-21-04-57-2.png align="left")

*Création d'un stockage blob étape 6*

Cliquez sur le bouton créer une fois que vous avez terminé de remplir le formulaire.

**Étape 7** : Copiez les identifiants depuis le portail Azure.

Vous devez avoir une autorisation avant d'envoyer des requêtes au stockage Azure. Azure propose deux clés à cet effet, chacune contenant une chaîne de connexion. Par conséquent, vous aurez besoin de ces identifiants sous forme de chaîne de connexion pour l'application NestJS.

L'une des chaînes de connexion est disponible pour être copiée dans la zone des clés d'accès du menu `Sécurité + réseau` à gauche. (Nous ajouterons celles-ci à notre fichier .env de NestJS.)

![création d'un stockage blob étape 7](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-15-21-57-01-2.png align="left")

*Création d'un stockage blob étape 7*

Super ! Vous avez configuré votre stockage blob Azure. L'étape suivante consiste à configurer et lier votre application NestJS avec le stockage blob.

## Comment configurer NestJS et la base de données MySQL

Comme mentionné précédemment, nous utiliserons NestJS comme serveur et la base de données MySQL pour sauvegarder une référence au fichier enregistré sur le système distribué Azure.

Tout d'abord, vous devez avoir NestJS et le serveur MySQL installés sur votre système. Ensuite, exécutez la commande NestJS suivante pour démarrer un nouveau projet. Appelons notre projet `nestjs-file-upload-azure` :

```js
nest new nestjs-file-upload-azure
```

![Comment créer un nouveau projet dans nestjs](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-15-05-18-05-3.png align="left")

*Comment créer un nouveau projet dans Nestjs*

Avant de commencer à créer nos ressources, installons les dépendances nécessaires :

```js
yarn add mysql2 @nestjs/typeorm @nestjs/config typeorm
```

Pour configurer votre base de données MySQL avec NestJS, ouvrez le fichier `app.module.ts` à l'intérieur du dossier `src` et ajoutez le code suivant :

```javascript

import { Module } from '@nestjs/common'; 
import { ConfigModule, ConfigService } from '@nestjs/config'; 
import { TypeOrmModule } from '@nestjs/typeorm'; 
import { FileModule } from './modules/files/file.module'; 
import { UserModule } from './modules/users/user.module'; 

@Module({ 
    imports: [ 
        ConfigModule.forRoot({ 
            envFilePath: '.env', 
            isGlobal: true, 
        }), 
        TypeOrmModule.forRootAsync({ 
            imports: [ConfigModule], 
            inject: [ConfigService], 
            useFactory: (config: ConfigService) => ({ 
                type: 'mysql', 
                host: 'localhost', 
                port: 3306, 
                username: config.get('DB_USERNAME'), 
                password: config.get('DB_PASSWORD'), 
                database: 'azure_upload', 
                entities: [__dirname + '/**/*.entity{.ts,.js}'], 
                synchronize: true, 
            }), 
        }), 
        UserModule, 
        FileModule, 
    ], 
    controllers: [], 
    providers: [], 
}) 

export class AppModule {}
```

Dans les `imports`, configurez une base de données MySQL simple avec `TypeOrmModule.forRootAsync()` appelée `azure_upload` localement. Elle injecte `ConfigService` pour nous permettre d'utiliser des variables d'environnement (dans ce cas, le nom et le mot de passe de votre base de données).

Pour une application basée sur la production, vous devez définir `synchronize` sur false et utiliser `migration` afin de garder vos données de base de données en sécurité.

Maintenant, la base de données est connectée avec succès, grâce au package TypeORM que nous avons installé. Vous pouvez vérifier en exécutant `yarn start:dev` dans votre terminal ou `npm run start:dev` si vous utilisez npm comme gestionnaire de paquets.

## Comment se connecter à Azure Blob via le SDK

En utilisant le stockage `@azure/storage-blob`, nous pouvons nous connecter à Azure. Nous aurons toujours besoin du package Multer pour gérer les opérations de gestion de fichiers, et nous utiliserons UUID pour générer un nom unique pour chaque blob.

Installons-les d'abord.

* `yarn add @azure/storage-blob uuidv4 @types/multer` ou
  
* `npm install @azure/storage-blob uuidv4 @types/multer`
  

Maintenant, ajoutons la chaîne de connexion que nous avons sauvegardée précédemment à notre fichier **.env**

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-15-22-06-39-2.png align="left")

## Comment télécharger l'image via l'API

Puisque nous avons configuré la connexion Azure, nous pouvons procéder au téléchargement de nos fichiers. Pour commencer, créons une entité et un service de fichier.

### Comment créer un service Azure

Le service Azure nous aidera à cartographier la logique pour télécharger, télécharger et supprimer des fichiers de notre compte de stockage Azure que nous avons créé.

Pour générer un service, nous utiliserons l'interface de ligne de commande NestJS. Ouvrez le `terminal` et exécutez `nest g service files modules/files --no-spec --flat`.

Ajoutez ce qui suit aux fichiers de service générés :

###### src/modules/files/files.service.ts

```javascript

import { BlobServiceClient, BlockBlobClient } from '@azure/storage-blob'; 
import { Injectable } from '@nestjs/common'; 
import { ConfigService } from '@nestjs/config'; 
import { uuid } from 'uuidv4'; 

@Injectable() export class FilesAzureService { 
    constructor(private readonly configService: ConfigService) {} 
    private containerName: string; 

	private async getBlobServiceInstance() { 
        const connectionString = this.configService.get('CONNECTION_STRING'); 
        const blobClientService = await BlobServiceClient.fromConnectionString( connectionString, ); 
        return blobClientService; 
    } 

	private async getBlobClient(imageName: string): Promise<BlockBlobClient> {
        const blobService = await this.getBlobServiceInstance(); 
		const containerName = this.containerName; 
		const containerClient = blobService.getContainerClient(containerName); 
		const blockBlobClient = containerClient.getBlockBlobClient(imageName); 

		return blockBlobClient; 
	} 
    
    public async uploadFile(file: Express.Multer.File, containerName: string) { 
        this.containerName = containerName; 
        const extension = file.originalname.split('.').pop(); 
        const file_name = uuid() + '.' + extension; 
        const blockBlobClient = await this.getBlobClient(file_name);
        const fileUrl = blockBlobClient.url; 
        await blockBlobClient.uploadData(file.buffer); 
        
        return fileUrl; 
    } 
}
```

Les fonctions privées créent une instance de notre stockage blob Azure avec les chaînes de connexion en utilisant les méthodes azure-sdk `BlobServiceClient.fromConnectionString()`. Elle attend également le `nom du conteneur` que nous avons donné à notre conteneur blob précédemment lors de la création du stockage azure en utilisant `getContainerClient` et `getBlockBlobClient()`.

La fonction `uploadFile()` est une fonction publique que le service utilisateur peut appeler pour télécharger des images vers Azure. Cette fonction utilise l'instance azure et les fonctions privées pour télécharger le fichier et retourne l'URL du fichier.

## Comment créer un endpoint pour télécharger des images

Il est temps de créer nos ressources utilisateur qui fournissent un endpoint pour créer (télécharger) des images vers Azure, visualiser l'image et supprimer l'image.

### Comment créer une ressource utilisateur

L'interface de ligne de commande NestJS est un outil puissant qui aide à échafauder notre ressource en créant des composants de base comme vous les connaissez. Pour créer facilement une ressource, dans le terminal, tapez la commande suivante et suivez les instructions pour les API REST :

```js
nest generate resource users modules/users --no-spec --flat
```

L'option `--no-spec` ignore les fichiers de test et `--flat` crée la ressource directement dans un dossier `modules/users`.

La commande ci-dessus a ajouté les dossiers `dto` et `entities` et les fichiers `user.controller.ts`, `user.module.ts` et `user.service.ts` à l'intérieur du fichier `src`. Elle a également effectué toutes les mises à jour nécessaires pour se synchroniser avec `app.module.ts`.

![ressources utilisateur créées](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-17-22-46-33-2.png align="left")

*Ressources utilisateur créées*

### Comment créer une entité utilisateur

En enregistrant l'URL de l'image directement dans la base de données, nous pouvons accéder très rapidement au fichier public.

###### src/modules/users/users.entity.ts

```javascript

import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm'; 

@Entity() export class User { 
	@PrimaryGeneratedColumn() 
    id: number; 
    
    @Column() 
    image_url: string; 
 }
```

### Comment créer un service utilisateur

Le service utilisateur aide à se connecter à la base de données et à enregistrer l'URL de l'image téléchargée, d'où la fonction `saveUrl()`.

###### src/modules/users/users.service.ts

```javascript
import { Injectable } from '@nestjs/common'; 
import { InjectRepository } from '@nestjs/typeorm'; 
import { Repository } from 'typeorm'; 
import { User } from './entities/user.entity'; 

@Injectable() export class UserService { 
    constructor( 
    	@InjectRepository(User) private readonly userRepository: Repository<User>, 
    ) {} 
    
    async saveUrl(file_url: string) { 
        await this.userRepository.save({ image_url: file_url }); 
    } 
}
```

### Comment créer un contrôleur utilisateur

Cela définit l'endpoint pour qu'un utilisateur public puisse télécharger un fichier. Pour ce faire, nous suivons la [documentation NestJS](https://docs.nestjs.com/techniques/file-upload) et utilisons le `FileInterceptor` qui utilise [`multer`](https://www.npmjs.com/package/multer) en interne.

###### src/modules/users/users.controllers.ts

```javascript

import { Controller, Post, UseInterceptors, UploadedFile, } from '@nestjs/common'; 
import { UserService } from './user.service'; 
import { FilesAzureService } from '../files/file.azure.service'; 
import { FileInterceptor } from '@nestjs/platform-express';

@Controller('user') export class UserController { 
	constructor( 
    	private readonly userService: UserService, 
        private readonly fileService: FilesAzureService 
    ) {} 
    
    @Post('upload') 
    @UseInterceptors(FileInterceptor('image')) 
    async create(@UploadedFile() file: Express.Multer.File) { 
    	const containerName = 'fileupload'; 
        const upload = await this.fileService.uploadFile(file, containerName) 
        this.userService.saveUrl(upload); 
        return { upload, message: 'uploaded successfully' } 
    } 
}
```

Nous pouvons tester avec Postman :

![Test endpoint de téléchargement depuis postman](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-16-22-52-06-1.png align="left")

*Test endpoint de téléchargement depuis Postman*

Et confirmer sur Azure :

![Confirmer l'image sur le portail azure](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-16-22-50-31-2.png align="left")

*Confirmer l'image sur le portail Azure*

## Comment supprimer des fichiers

Nous avons également besoin d'un moyen de supprimer les fichiers après les avoir soumis. Nous supprimerons les fichiers des deux emplacements pour maintenir la cohérence entre notre base de données et le stockage Azure. Ajoutons d'abord la méthode au service de fichiers :

**src/modules/files/files.service.ts**

```javascript
async deleteFile(file_name: string, containerName: string) { 
	try { 
    	this.containerName = containerName; 
        const blockBlobClient = await this.getBlobClient(file_name);
        await blockBlobClient.deleteIfExists(); 
    } catch (error) { 
    	console.log(error); 
    } 
}
```

Nous devons maintenant l'appliquer à notre service utilisateur. Un ajout crucial est que nous supprimons le fichier précédent lorsqu'un utilisateur en télécharge un alors qu'il en a déjà un et en faisant un endpoint de téléchargement par ID d'utilisateur.

**src/modules/users/users.service.ts**

```javascript
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { FilesAzureService } from '../files/file.azure.service';
import { User } from './entities/user.entity';

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User) private readonly userRepository: Repository<User>,
    private readonly fileService: FilesAzureService,
  ) {}

  async saveUrl(id, file_url: string, containerName: string): Promise<void> {
    const user = await this.userRepository.findOne({
      where: { id },
    });
    const file_image = user?.image_url;
    let getfile = '';

    if (file_image) {
      getfile = file_image.split('/').pop();
    }
    await this.userRepository.save({
      ...user,
      image_url: file_url,
    });
    await this.fileService.deleteFile(getfile, containerName);
  }

  async getimage(id: number): Promise<any> {
    const user = await this.userRepository.findOne({
      where: { id },
    });

    return user;
  }

  async remove(id: number, containerName: string): Promise<User> {
    try {
      const user = await this.userRepository.findOne({
        where: { id },
      });
      const file_url = user?.image_url;
      if (file_url) {
        await this.userRepository.update(id, {
          ...user,
          image_url: '',
        });

        const file_ = file_url.split('/').pop();

        await this.fileService.deleteFile(file_, containerName);
      }

      return user;
    } catch (error) {
      console.log(error);
      return error;
    }
  }
}
```

Inclure un endpoint où les utilisateurs peuvent envoyer une image est le composant final. Pour y parvenir, nous utilisons le `FileInterceptor`, qui utilise en interne `multer`, conformément à la documentation NestJS.

**src/modules/users/users.controller.ts**

```javascript
Controller('user')
export class UserController {
  constructor(
    private readonly userService: UserService,
    private readonly fileService: FilesAzureService
  ) {}

  @Post('/:id/upload')
  @UseInterceptors(FileInterceptor('image'))
  async create(@UploadedFile() file: Express.Multer.File, @Param('id') id) {
    const containerName = 'fileupload';
    const upload = await this.fileService.uploadFile(file, containerName)
    this.userService.saveUrl(id, upload, containerName);
    return {
      upload,
      message: 'uploaded successfully'
    }
  }

  @Get('/:id')
  async getimage(@Param('id') id) {
    const image = await this.userService.getimage(id);
    return {
      image,
      message: 'get image successfully'
    }
  }

  @Delete('remove/:id')
  @UseInterceptors(FileInterceptor('image'))
  async remove(@UploadedFile() file: Express.Multer.File , @Param('id') id) {
    const containerName = 'fileupload';
    const user = await this.userService.remove(id, containerName);
    return {
      user,
      message: 'deleted successfully'
    }
  }
}
```

Celles-ci se synchronisent avec votre stockage Azure pour supprimer les téléchargements de fichiers inutilisés.

Vous pouvez trouver le [dépôt de code complet sur **GitHub**](https://github.com/Caesarsage/nest-file-upload-azure).

## Nettoyage

Pour éviter de payer les coûts de stockage Azure sous-jacents, vous devez nettoyer vos ressources si elles ne sont pas utilisées.

Pour nettoyer vos ressources Azure, dans le portail Azure, allez dans ou recherchez le groupe de ressources, trouvez celui que vous venez de créer et supprimez-le. Cela supprimera toutes les ressources du groupe de ressources.

## Résumé

Dans cet article, nous avons appris les bases du stockage Blob Azure et comment l'utiliser dans notre API NestJS.

Pour y parvenir, nous avons fourni les identifiants nécessaires au SDK Azure, et par conséquent, nous avons pu télécharger et supprimer des fichiers vers Azure.

Pour suivre nos fichiers, nous avons également gardé notre base de données MySQL synchronisée avec un conteneur blob Azure. Nous avons utilisé le FileInterceptor, qui est alimenté par Multer, pour télécharger des fichiers en utilisant l'API.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).