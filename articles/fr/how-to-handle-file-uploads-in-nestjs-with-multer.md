---
title: Comment gérer les téléchargements de fichiers dans NestJS avec Multer
subtitle: ''
author: Abimbola Adedotun Samuel
co_authors: []
series: null
date: '2024-08-28T02:42:00.987Z'
originalURL: https://freecodecamp.org/news/how-to-handle-file-uploads-in-nestjs-with-multer
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724695369812/b0511a24-bbb6-4dae-9ccf-b511383b8f6a.png
tags:
- name: nestjs
  slug: nestjs
- name: Node.js
  slug: nodejs
seo_title: Comment gérer les téléchargements de fichiers dans NestJS avec Multer
seo_desc: Guide to implementing file uploads in NestJs using Multer. Create, configure,
  and test the feature step-by-step
---

Le téléchargement de fichiers est un besoin important dans de nombreuses applications. En utilisant Multer, vous pouvez mettre en place une fonctionnalité de téléchargement de fichiers dans NestJS de manière simple et directe.

Dans ce guide, nous allons parcourir les étapes pour créer une ressource dédiée au téléchargement de fichiers, garantissant ainsi que votre application peut gérer facilement les fichiers des utilisateurs. Vous configurerez votre application pour gérer les fichiers de manière sécurisée et fluide.

## Prérequis

C'est un guide pratique. Pour le suivre, vous devez disposer des éléments suivants :

* Node.js (v14 et supérieur)
    
* Un gestionnaire de paquets Node
    
* Une compréhension de base de Node.js et NestJS
    
* Un éditeur de code, comme VS Code
    
* NestJS CLI. Vous pouvez utiliser la commande `npm install -g @nestjs/cli` pour installer la CLI.
    

## Comment configurer le projet

Créez un nouveau projet NestJS :

```bash
$ nest new file-upload-example
```

Ensuite, accédez au répertoire de votre projet et exécutez :

```bash
$ cd file-upload-example
```

Ensuite, installez le paquet `multer` — le middleware qui gérera vos téléchargements de fichiers :

```bash
$ npm install @nestjs/platform-express multer
```

Enfin, installez les paquets `@types/express` et `@types/multer` :

```bash
$ npm install -save-dev @types/express @types/multer
```

Une fois le projet configuré et les dépendances installées, créons la ressource pour la fonctionnalité de téléchargement de fichiers.

## Comment créer une ressource pour le téléchargement de fichiers

En utilisant la NestJS CLI, générez la ressource pour gérer les téléchargements de fichiers :

```bash
nest generate resource file-upload
```

Cette commande crée une ressource `file-upload` dans le répertoire **src** : module, contrôleur et service, pour gérer les téléchargements de fichiers.

**file-upload.module.ts** organise la logique de téléchargement, **file-upload.controller.ts** gère les requêtes de téléchargement entrantes, et **file-upload.service.ts** gère les opérations de téléchargement de fichiers. La ressource étant créée, configurons le module, le service et le contrôleur.

## **Comment configurer la ressource de téléchargement de fichiers**

Dans cette section, nous allons configurer les fichiers **file-upload.module.ts**, **file-upload.controller.ts** et **file-upload.service.ts**.

**Configuration du module :**

```javascript
import { Module } from '@nestjs/common';
import { FileUploadService } from './file-upload.service';
import { FileUploadController } from './file-upload.controller';
import { MulterModule } from '@nestjs/platform-express';
import { diskStorage } from 'multer';
@Module({
  imports: [
    MulterModule.register({
      storage: diskStorage({
        destination: './uploads',
        filename: (req, file, cb) => {
          const filename = `${Date.now()}-${file.originalname}`;
          cb(null, filename);
        },
      }),
    }),
  ],
  controllers: [FileUploadController],
  providers: [FileUploadService],
})
export class FileUploadModule {}
```

Ci-dessus se trouve le fichier **file-upload.module.ts**, où nous avons configuré le `MulterModule` pour spécifier la destination de l'upload et comment il doit nommer le fichier.

**Configuration du contrôleur :**

```javascript
import {
  Controller,
  Post,
  UseInterceptors,
  UploadedFile,
} from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { FileUploadService } from './file-upload.service';

@Controller('file-upload')
export class FileUploadController {
  constructor(private readonly fileUploadService: FileUploadService) {}

  @Post('upload')
  @UseInterceptors(FileInterceptor('file'))
  uploadFile(@UploadedFile() file: Express.Multer.File) {
    return this.fileUploadService.handleFileUpload(file);
  }
}
```

Dans le fichier **file-upload.controller.ts** ci-dessus, une route `POST` est créée pour gérer les téléchargements de fichiers. La route écoute les téléchargements et transmet le fichier au service pour traitement.

**Configuration du service :**

```javascript
import { Injectable } from '@nestjs/common';

@Injectable()
export class FileUploadService {
  handleFileUpload(file: Express.Multer.File) {
    return { message: 'Fichier téléchargé avec succès', filePath: file.path };
  }
}
```

Le service traite le fichier et renvoie une réponse avec le chemin du fichier.

Maintenant que le module, le service et le contrôleur ont été configurés, nous pouvons ajouter une validation pour vérifier la taille et le type du fichier.

```javascript
import { BadRequestException, Injectable } from '@nestjs/common';

@Injectable()
export class FileUploadService {
  handleFileUpload(file: Express.Multer.File) {
    if (!file) {
      throw new BadRequestException('aucun fichier téléchargé');
    }

    // valider le type de fichier
    const allowedMimeTypes = ['image/jpeg', 'image/png', 'application/pdf'];
    if (!allowedMimeTypes.includes(file.mimetype)) {
      throw new BadRequestException('type de fichier invalide');
    }

    // valider la taille du fichier (ex : max 5 Mo)
    const maxSize = 5 * 1024 * 1024;
    if (file.size > maxSize) {
      throw new BadRequestException('le fichier est trop volumineux !');
    }

    return { message: 'Fichier téléchargé avec succès', filePath: file.path };
  }
}
```

Nous avons terminé les configurations nécessaires pour tester le téléchargement de fichiers.

## **Comment tester le téléchargement de fichiers**

Le test est une partie importante de la création de fonctionnalités. Dans cette section, nous allons tester la fonctionnalité de téléchargement en utilisant Postman, mais vous pouvez utiliser n'importe quel outil similaire pour tester le point de terminaison. Voyons notre API en action !

**Envoyez un fichier image avec le point de terminaison** `/file-upload/upload` :

![test postman pour le point de terminaison d'upload](https://cdn.hashnode.com/res/hashnode/image/upload/v1724616574064/c19015a7-5776-4148-838d-dd7acf5c3509.png align="center")

Après avoir envoyé la requête, vérifiez votre réponse pour vous assurer que le fichier a été téléchargé avec succès. Et pour confirmer davantage l'upload, vérifiez le projet **file-upload-example** et vous verrez que le répertoire **uploads** a déjà été créé avec le fichier que vous avez téléchargé.

## Conclusion

Félicitations, vous avez réussi à mettre en place une fonctionnalité de téléchargement de fichiers avec Multer et NestJS. Vous avez configuré le module, le contrôleur et le service pour gérer les fichiers de manière sécurisée, et vous avez testé le point de terminaison.

Il est important de comprendre que ce sont des étapes de base et essentielles pour l'upload de fichiers. Vous pouvez enrichir cela en créant des fonctionnalités plus complexes comme la gestion de téléchargements de fichiers multiples, le stockage dans des services cloud, etc.

J'ai beaucoup apprécié travailler sur cette démo et j'espère qu'elle vous sera utile. Pour votre commodité, le dépôt du projet est [disponible sur Github](https://github.com/dotun2203/nest-js-fileupload-demo). Vous pouvez également me contacter sur [Twitter](https://x.com/Adedot1Abimbola?t=2A7m7RbbIzJei3rrjxsVuA&s=09). J'aimerais avoir de vos nouvelles.