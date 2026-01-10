---
title: Amazon S3 — Stockage de fichiers dans le cloud pour la performance et les économies
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-12T08:21:40.000Z'
originalURL: https://freecodecamp.org/news/amazon-s3-cloud-file-storage-for-performance-and-cost-savings-8f38d7769619
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q6O661l2bPf6piXpVH6-ag.png
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Amazon S3 — Stockage de fichiers dans le cloud pour la performance et les
  économies
seo_desc: 'By Kangze Huang

  The Complete AWS Web Boilerplate — Tutorial 2


  Table of Contents


  Part 0: Introduction to the Complete AWS Web Boilerplate

  Part 1: User Authentication with AWS Cognito (3 parts)

  Part 2: Saving File Storage Costs with Amazon S3 (1 part...'
---

Par Kangze Huang

#### Le modèle AWS Web complet — Tutoriel 2

![Image](https://cdn-media-1.freecodecamp.org/images/Xs9mnmL9P2wrCfAP8717edF-jsLSFT6nraPn)

### Table des matières

> **Partie 0 :** [Introduction au modèle AWS Web complet](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.3eqpvcjsy)

> **Partie 1 :** [Authentification des utilisateurs avec AWS Cognito](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.cbkz7b2jp) (3 parties)

> **Partie 2 :** [Économiser les coûts de stockage de fichiers avec Amazon S3](https://medium.com/@kangzeroo/amazon-s3-cloud-file-storage-for-performance-and-cost-savings-8f38d7769619#.l9so2hk00) (1 partie)

> **Partie 3 :** [Envoyer des emails avec Amazon SES](https://medium.com/@kangzeroo/sending-emails-with-amazon-ses-7617e83327b6#.5nhcrr609) (1 partie)

> Partie 4 : Gérer les utilisateurs et les permissions avec AWS IAM **[À venir]**

> Partie 5 : Hébergement de serveur cloud avec AWS EC2 et ELB **[À venir]**

> Partie 6 : Le tueur de MongoDB : AWS DynamoDB **[À venir]**

> Partie 7 : Mise à l'échelle SQL sans douleur avec AWS RDS **[À venir]**

> Partie 8 : Architecture sans serveur avec Amazon Lambda **[À venir]**

Téléchargez le projet GitHub [ici](https://github.com/kangzeroo/Kangzeroos-AWS-S3-Boilerplate).

#### Introduction

Traditionnellement, les fichiers servis à une application étaient enregistrés dans le système de fichiers d'un serveur et l'architecture conçue par un développeur. Nous pouvons immédiatement voir que cela est coûteux en termes de main-d'œuvre et un risque commercial, car nous devons nous fier à l'expertise/conception d'un ou plusieurs développeurs. Cela est également coûteux en termes de bande passante, car chaque fichier doit être transféré du serveur au client. Si nous gardons le système de fichiers sur le serveur principal, cela ralentira le traitement de toutes les fonctionnalités principales. Si nous séparons le système de fichiers dans son propre serveur, nous devons payer supplémentaire pour le temps de fonctionnement de ce serveur, ainsi que concevoir un moyen d'accéder aux images de manière fiable même lorsque les URL changent. Et qu'en est-il des différents types de fichiers ? Nous devons écrire du code pour gérer les fichiers JPG, MP4, PDF, ZIP, etc. Et la sécurité et l'accès restreint uniquement aux utilisateurs autorisés ? La sécurité est une tâche monumentale en soi. Enfin, si nous voulons que tout cela soit évolutif, nous devrons payer très cher pour cela. Et si il existait un moyen d'atteindre toutes ces fonctionnalités de niveau production facilement et à moindre coût ?

Présentation d'Amazon Simple Storage Service (S3) — Un système de stockage de fichiers entièrement géré que vous pouvez utiliser de manière fiable à grande échelle, et sécurisé dès la sortie de la boîte. Vos fichiers sont automatiquement stockés dans plusieurs emplacements physiques pour une disponibilité garantie, même si un centre de stockage tombe en panne. Tout est géré pour vous afin que vous n'ayez qu'à fournir l'URL pour accéder à votre contenu (et être un utilisateur autorisé si applicable). S3 est une aubaine car la bande passante/stockage de S3 est beaucoup moins chère que celle d'EC2 : pour stocker 10 Go d'images avec 30 Go de transfert de données sortant et 1 million de requêtes GET, cela revient à un total mensuel de... 1,89 USD. Wow. Commençons.

### Installation initiale

![Image](https://cdn-media-1.freecodecamp.org/images/V1X3KLtOZhwZpjwCFWegeCn60PDn8Cnco5CT)

Cliquez sur l'icône de la console AWS (le cube) en haut à gauche et recherchez S3.

![Image](https://cdn-media-1.freecodecamp.org/images/iv1gbx6WF614u2eQuNDuExJPw3AMklTciXzp)

Sur la page S3, cliquez sur le bouton « Créer un bucket ». Donnez un nom unique à votre bucket S3, car vous ne pouvez pas avoir le même nom de bucket qu'un autre bucket S3 sur Internet. Choisissez également une région proche de l'endroit où vos utilisateurs résideront pour que les vitesses de connexion soient les plus rapides.

![Image](https://cdn-media-1.freecodecamp.org/images/z0nsib6ZgJxUNBjYVEWjQmQOIVk5Pwp2odJ5)

Sur l'écran de gestion S3 suivant, cliquez sur Permissions et « Ajouter plus de permissions ». Dans le menu déroulant, sélectionnez « Tout le monde ». Cela rendra votre bucket S3 et tout son contenu accessible au public.

![Image](https://cdn-media-1.freecodecamp.org/images/XWiGvyVRxeDP1lRkWLg5zwuGsuXBKQaZti6x)

Si nous voulons affiner qui a accès à notre bucket S3, nous pouvons créer une politique de bucket. Cliquez sur le bouton « Ajouter une politique de bucket » puis sur « Générateur de politiques AWS » en bas à gauche. Le texte de la politique que vous voyez ci-dessous est le résultat du générateur de politiques.

![Image](https://cdn-media-1.freecodecamp.org/images/nRtLmMlZHID2muu3PCg0l2nfF0Kz2JPu8Oml)

Deux choses à noter lors de la génération de votre politique. « Action » fait référence à une fonctionnalité autorisée à être effectuée sur ce bucket S3, dans ce cas, supprimer, créer et afficher des objets. « Principal » fait référence à l'entité autorisée à effectuer cette action, telle qu'un rôle IAM d'un utilisateur Cognito (l'exemple ici utilise le rôle `Cognito_App_UsersAuth_Role` créé dans mon tutoriel AWS Cognito). Le « Principal » est référencé par son identifiant ARN que vous pouvez trouver sur la page d'information de ce principal, et suit le format `arn:aws:<AWS_SERVICE>:::<UNIQUE_IDENTIFIER>`. Si vous regardez l'ARN pour le « Principal » ou la « Ressource », vous trouverez un motif similaire. Enfin, « Ressource » fait référence à l'objet du bucket S3 auquel cette politique s'applique, identifié à nouveau par son ARN. Dans ce cas, notre « Ressource » est notre bucket S3 `fo` suivi de /* pour indiquer tous les objets enfants de notre bucket S3. Vous pouvez toujours ajouter plus de règles de politique en ajoutant un autre objet de déclaration à l'intérieur du tableau Statement.

Une dernière chose que nous devons configurer est la configuration CORS du bucket S3. Si nous voulons que les sites web puissent accéder aux ressources de notre bucket S3 sans plaintes de sécurité, nous devons spécifier quelles actions http sont autorisées. Si vous ne savez pas ce qu'est CORS, lisez à ce sujet [ici](https://spring.io/understanding/CORS).

![Image](https://cdn-media-1.freecodecamp.org/images/DNZhevO5Epx6lXWqF9akDm9uGPbdbjBE6E0c)

C'est assez simple, `<AllowedOrigin>*</AllowedOrigin>` signifie que notre requête http peut provenir de n'importe où. Si nous voulions autoriser uniquement les requêtes provenant d'une certaine adresse IP (comme ce serait le cas en production), nous aurions `<AllowedOrigin>10.67.53.55</AllowedOrigin>`. Ensuite, `<AllowedMethod>GET</AllowedMethod>` spécifie que les requêtes GET sont autorisées. Nous pouvons spécifier plus de méthodes autorisées, ou si nous aimons vivre dangereusement, nous pouvons faire `<AllowedMethod>*</AllowedMethod>`. Enfin, `<AllowedHeaders>*</AllowedHeaders>` permet à tout en-tête, tel que OPTION, d'être une communication autorisée avec ce bucket S3. Si nous voulons ajouter plus de règles, ajoutez simplement un autre `<CORSRule></CORSRule>`. Simple, n'est-ce pas ? Si vous avez besoin de plus d'exemples, cliquez sur « Configurations CORS d'exemple » en bas à gauche.

D'accord, nous sommes presque prêts à plonger dans le code !

### Un bref aperçu de S3

Rappelons que seuls les utilisateurs authentifiés via AWS Cognito peuvent modifier (télécharger ou supprimer) des fichiers, tandis que tous les utilisateurs peuvent visualiser les fichiers. Ce modèle commence par le téléchargement de fichiers, après qu'un utilisateur authentifié se connecte à notre application via AWS Cognito. Si vous ne savez pas comment faire cela avec AWS Cognito, consultez les tutoriels précédents. Si votre cas d'utilisation permet à tous les utilisateurs de modifier des fichiers, assurez-vous simplement que vos permissions S3 correspondent à cela. Le code est sinon le même, alors commençons !

Amazon S3 est un stockage clé-valeur brut de fichiers, ce qui signifie que chaque fichier a un nom et une valeur de données brute pour ce nom. Techniquement, cela signifie que nous pouvons stocker n'importe quel type de fichier sur S3, mais il y a certaines limitations définies dans leur [Accord de licence des services Web Amazon](https://aws.amazon.com/agreement) qui sont principalement des restrictions concernant les activités malveillantes. La taille maximale d'un fichier individuel sur S3 est de 5 téraoctets, et la taille maximale d'une seule requête PUT est de 5 gigaoctets. À part cela, ce que nous pouvons stocker sur S3 est illimité. Dans S3, les dossiers sont également des objets mais avec une valeur nulle, car leur but est l'organisation. Les dossiers S3 ne peuvent pas être renommés, et s'ils sont changés de privé à public, ils ne peuvent pas être changés en retour. Contrairement à un système de fichiers typique, S3 a une hiérarchie plate, ce qui signifie qu'un fichier qui réside à l'intérieur d'un dossier est techniquement au même niveau que le dossier — tout est à un niveau de profondeur. S3 utilise simplement des préfixes de nom de fichier pour distinguer la hiérarchie des dossiers. Par exemple, un fichier appelé « panda.jpg » à l'intérieur du dossier « ChinaTrip » aura en réalité un nom de fichier « ChinaTrip/panda.jpg » dans S3. C'est la solution simple mais efficace d'Amazon pour avoir des hiérarchies de dossiers tout en conservant les avantages d'un stockage clé-valeur simple à un niveau de profondeur. C'est tout pour le briefing, commençons le code !

### Le Code

Dans le front-end du modèle, allez dans `App/src/api/aws/aws_s3.js`. Ce que nous remarquons d'abord, c'est que nous importons un nom de bucket S3 depuis `App/src/api/aws/aws_profile.js`. Assurez-vous dans `aws_profile.js` que vous exportez un nom de bucket comme suit :

`export const BUCKET_NAME = 'kangzeroos-s3-tutorial'`

Puis importons-le dans `App/src/api/aws/aws_cognito.js` comme suit :

```
import {BUCKET_NAME} from './aws_profile'
```

Maintenant, continuons dans `aws_cognito.js` et passons en revue la première fonction que nous allons utiliser.

#### Créer un album utilisateur

Imaginez que vos utilisateurs téléchargent des photos pour une raison quelconque. Vous voudriez organiser les images que vos utilisateurs téléchargent dans des dossiers représentant chaque utilisateur. C'est le but de `createUserS3Album()` qui crée un dossier S3 nommé à partir de son seul argument `albumName` — dans le cas de ce modèle et de son intégration avec AWS Cognito, le `albumName` sera l'email de l'utilisateur. Passons en revue la fonction.

```
export function createUserS3Album(albumName){ const p = new Promise((res, rej)=>{           AWS.config.credentials.refresh(function(){         const S3 = new AWS.S3()     if (!albumName) {         const msg = 'Veuillez fournir un nom d\'album valide'         rej(msg)         return      }     albumName = albumName.trim();     if (albumName.indexOf('/') !== -1) {         const msg = 'Les noms d\'album ne peuvent pas contenir de barres obliques.'         rej(msg)         return     }
```

```
     const albumKey = encodeURIComponent(albumName) + '/';     const params = {      Bucket: BUCKET_NAME,      Key: albumKey     }     S3.headObject(params, function(err, data) {       if (!err) {         const msg = 'L\'album existe déjà.'         res()         return       }       if (err.code !== 'NotFound') {          const msg = 'Il y a eu une erreur lors de la création de votre album : ' + err.message          rej()          return       }     if(err){        const albumParams = {         ...params,         ACL: "bucket-owner-full-control",         StorageClass: "STANDARD"        }        S3.putObject(params, function(err, data) {           if (err) {            const msg = 'Il y a eu une erreur lors de la création de votre album : ' + err.message             rej(msg)             return           }           res('Album créé avec succès.');        });     }     });  }) }) return p}
```

À un niveau élevé, voici le processus. Nous commençons par rafraîchir les informations d'identification Amazon fournies par AWS Cognito. Cela n'est nécessaire que si la sécurité de votre bucket S3 est configurée de manière à ce que seuls les utilisateurs connectés à AWS Cognito puissent télécharger des fichiers. Si votre cas d'utilisation permet à n'importe qui de poster, vous n'aurez pas besoin de rafraîchir les informations d'identification Amazon. Dans le modèle, `createUserS3Album()` est appelé chaque fois qu'un utilisateur se connecte.

Ensuite, nous instancions l'objet S3 et vérifions l'existence d'un `albumName`. Nous continuons en encodant l'`albumName` en `albumKey`, ce qui est nécessaire si `albumName` provient d'une adresse email, car S3 n'acceptera pas de caractères comme `/` et `@` dans un nom de fichier.

Enfin, nous pouvons prendre `albumKey` et `BUCKET_NAME` pour appeler `S3.headObject()`. À l'intérieur de `headObject()`, nous vérifions si `albumKey` existe déjà ou si nous obtenons un code d'erreur. Si tout est bon, nous appelons `S3.putObject()` avec `albumKey`. Après la création réussie de `albumKey`, nous pouvons résoudre la promesse et terminer la fonction.

#### Télécharger des fichiers vers S3

Maintenant, voyons comment télécharger des fichiers réels. Dans le modèle, nous utilisons des images, mais les mêmes concepts s'appliquent à n'importe quel fichier. La fonction nécessite 2 arguments : le `albumName` (qui dans le modèle est l'`email` d'un utilisateur) et un tableau des fichiers à télécharger. Passons en revue le processus.

```
export function uploadImageToS3(email, files){ const p = new Promise((res, rej)=>{    if (!files.length || files.length == 0) {      const msg = 'Veuillez choisir un fichier à télécharger d\'abord.'      rej(msg)    }  AWS.config.credentials.refresh(function(){    const S3 = new AWS.S3()
```

```
    const S3ImageObjs = []    let uploadedCount = 0
```

```
    for(let f = 0; f<files.length; f++){     const file = files[f];     const fileName = file.name;     const albumPhotosKey = encodeURIComponent(email) + '/';     const timestamp = new Date().getTime()/1000
```

```
     const photoKey = albumPhotosKey + "--" + timestamp + "--" + fileName;     S3.upload({       Bucket: BUCKET_NAME,         Key: photoKey,         Body: file,         ACL: 'public-read'     }, function(err, data) {         if (err) {            const msg = 'Il y a eu une erreur lors du téléchargement de votre photo : '+ err.message            rej(msg)            return         }         const msg = 'Photo téléchargée avec succès : ' + fileName
```

```
         S3ImageObjs.push({          photoKey: photoKey,          url: data.Location         })         uploadedCount++         if(uploadedCount==files.length){          res(S3ImageObjs)         }     })    }  }) }) return p}
```

D'abord, nous vérifions que `files` contient effectivement un tableau d'éléments. Ensuite, nous rafraîchissons à nouveau les informations d'identification AWS et instancions l'objet S3. Maintenant, nous utilisons une boucle for pour parcourir tous les `files` et les télécharger un par un vers S3. Au dernier fichier, nous résolvons la promesse avec un tableau de tous les fichiers téléchargés `S3ImageObjs`. Alors, que fait la boucle for ?

Chaque fichier est nommé avec `albumName` (qui dans ce cas est un `email` encodé en URI) comme préfixe, puis horodaté, et enfin suivi du nom de fichier original du fichier. Le nom final est le `photoKey`. Ensuite, nous appelons `S3.upload()` avec les paramètres corrects, et après un téléchargement réussi, nous ajoutons le résultat au tableau `S3ImageObjs`. Un téléchargement réussi retournera un objet avec une propriété `Location` qui est une URL de chaîne pour accéder à ce fichier. Si nous visitons l'URL `Location`, nous verrons nos images téléchargées. Une dernière chose à noter est la propriété `ACL` dans `S3.upload()`. `ACL` est défini sur 'public-read' pour que le fichier soit accessible publiquement par tous.

#### Le reste

Super, nous avons donc terminé la lecture et l'envoi de fichiers (GET & POST) pour notre modèle. Qu'en est-il de la mise à jour et de la suppression ? Eh bien, la mise à jour consiste à remplacer un fichier précédent et suit un processus POST similaire. La suppression est une simple question d'appeler `S3.deleteObject()` avec le `photoKey` et le nom du bucket.

```
const params = {      Bucket: 'STRING_VALUE',    Key: 'STRING_VALUE' }; 
```

```
s3.deleteObject(params, function(err, data) {      if (err)       console.log(err, err.stack); // une erreur s'est produite      else           console.log(data);           // réponse réussie });
```

Et c'est tout ! Les bases d'Amazon S3 avec une couverture sur la sécurité et l'intégration de l'authentification. Pour la majorité de vos cas d'utilisation, cela sera tout ce dont vous avez besoin. C'était assez simple, et nous obtenons beaucoup d'avantages en utilisant un stockage de fichiers brut par rapport aux systèmes de fichiers traditionnels sur notre serveur principal. J'espère que cet article vous a convaincu des avantages de S3 et de la manière de l'implémenter dans votre propre application.

À la prochaine dans le prochain article de cette série !

> Ces méthodes ont été partiellement utilisées dans le déploiement de [renthero.ca](http://renthero.ca)