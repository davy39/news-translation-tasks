---
title: Comment configurer le téléchargement d'images simple avec Node et AWS S3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T18:32:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-simple-image-upload-with-node-and-aws-s3-84e609248792
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yi56K1oYbapFszZA_N3uPg.jpeg
tags:
- name: AWS
  slug: aws
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment configurer le téléchargement d'images simple avec Node et AWS S3
seo_desc: 'By Filip Jerga

  A step-by-step guide explaining how to upload an image or any file to Amazon S3
  service.


  This is the first part of a tutorial in which we will handle the server (Node.js)
  part of the code.

  I prepared a video tutorial on YouTube as wel...'
---

Par Filip Jerga

#### Un guide étape par étape expliquant comment télécharger une image ou tout fichier vers le service Amazon S3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yi56K1oYbapFszZA_N3uPg.jpeg)

Il s'agit de la première partie d'un tutoriel dans lequel nous allons gérer la partie serveur (Node.js) du code.

J'ai également préparé un tutoriel vidéo sur YouTube. Vous pouvez trouver un lien dans les ressources en bas de cet article.

### 1. Ce que nous devons installer et une courte description.

**multer :** middleware pour gérer les fichiers de données. Principalement utilisé pour télécharger des fichiers. Plus d'informations : [Lien Npm](https://www.npmjs.com/package/multer)

**multer-s3 :** extension multer pour un téléchargement facile de fichiers vers le service Amazon S3. Plus d'informations : [Lien Npm](https://www.npmjs.com/package/multer-s3)

**aws-sdk :** package nécessaire pour travailler avec AWS (Amazon Web Services). Dans notre cas, le service S3. Plus d'informations : [Lien Npm](https://www.npmjs.com/package/aws-sdk)

**Allez dans vos projets et installons les packages :**

```
npm install --save multer multer-s3 aws-sdk
```

### 2. Inscription à AWS

Tout d'abord, créons un compte sur [https://aws.amazon.com](https://aws.amazon.com/). Amazon offre une incroyable couche gratuite que vous pouvez utiliser pendant la 1ère année. Après la connexion, recherchez le service S3.

En termes simples, S3 est un service cloud pour stocker des fichiers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kL7kzofPaB83N7EmyV9P2g.png)
_ Sélectionnez S3 _

Nous devons **créer un Bucket**. Vous pouvez imaginer un bucket comme un dossier pour vos fichiers. Choisissez un **nom de bucket** et la **Région**. Puisque cela est une configuration simple, nous ne sommes pas intéressés par les autres configurations. (La configuration par défaut est correcte — si quelque chose n'est pas clair, demandez dans les commentaires). Cliquez sur « **suivant** » jusqu'à ce que vous soyez sur **Review** et créez votre bucket.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ds5x2m5EbltvbBK6b-UJdQ.png)
_Création de bucket_

**Accédez à votre bucket créé** et vérifiez votre **barre d'URL**. Retenez votre **nom de bucket** (pour moi « medium-test ») et votre **région** (pour moi « us-east »).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GYbZM5qHrPoto9Kgi7nryw.png)
_Vérifiez votre barre d'URL._

Maintenant, nous devons obtenir nos **identifiants sécurisés**. Naviguez via le nom de votre compte vers « **mes identifiants de sécurité** ». Ensuite, « **Clés d'accès** » et **Créer une nouvelle clé d'accès**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X5iF7gUqs_M2IzH2IwYC3Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*VAAk0eS8PyT-v-QdnGxoXg.jpeg)
_Mes identifiants de sécurité et clés d'accès_

![Image](https://cdn-media-1.freecodecamp.org/images/1*kZNeP9KvC9hJRLyh6a7Abg.jpeg)
_Créer une clé d'accès_

**Ne partagez jamais vos clés avec qui que ce soit !** Enregistrez temporairement ces clés dans un fichier ou téléchargez le fichier de clés, car nous avons besoin des clés pour configurer le téléchargement de fichiers.

**Très bien. Configuration Amazon terminée !**

### 3. Allez dans votre éditeur de code

**Je n'expliquerai pas les bases de Node ou Express ici.** Ce tutoriel se concentre uniquement sur le téléchargement de fichiers. Si vous êtes intéressé par la mise en œuvre complète du projet, consultez mon dépôt GitHub ou regardez le tutoriel complet. (Vous pouvez trouver les liens à la fin de cet article de blog).

1. Créez votre service de téléchargement de fichiers avec la mise en œuvre suivante (première partie) :

**Note importante :** Ne exposez jamais vos identifiants secrets directement dans un fichier ! Ne partagez jamais vos identifiants secrets ! Envisagez de configurer des variables d'environnement dans votre environnement local ou, dans le cas de projets déployés, des variables dans votre fournisseur cloud. La meilleure solution serait d'utiliser **aws-profiles** : [https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-shared.html](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-shared.html).

**Premièrement**, nous importons tous nos packages installés. La **deuxième** partie consiste à **configurer notre AWS**. Nous devons fournir nos **clés secrètes et la région** à partir de la barre d'URL que je vous ai montrée précédemment.

Après la configuration AWS, nous pouvons créer une instance de notre Amazon S3. Nous n'avons pas encore tout à fait terminé. Maintenant, voyons la deuxième partie de cette mise en œuvre.

Maintenant, nous pouvons configurer une solution pour un téléchargement multer. Nous devons fournir une fonction à l'objet multer avec les propriétés suivantes.

1. **s3** : instance d'Amazon S3 que nous avons créée précédemment.
2. **bucket** : nom de notre bucket (dans mon cas : « medium-test »)
3. **acl** : contrôle d'accès pour le fichier ('public read' signifie que n'importe qui peut voir les fichiers), vous pouvez vérifier tous les types disponibles ici : [lien amazon](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl)
4. **metada** : fonction de rappel pour définir les métadonnées des fichiers téléchargés. Ici, je définis des métadonnées supplémentaires pour un **fieldName**. Vous pouvez voir ces données sur l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NeYh6Kg4i3BAKD20_ZpfyQ.png)
_Métadonnées_

5. **key** : fonction de rappel pour définir la propriété **key** (sous quelle clé votre fichier sera enregistré dans votre bucket). Dans notre cas, **nous créons un timestamp de l'heure actuelle** et enregistrons ce fichier sous ce nom. De cette façon, notre nom de fichier sera toujours unique, mais vous pouvez choisir le nom que vous voulez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vjRTskqhTeaGdVDNbtqWeQ.png)
_Fichier téléchargé avec un nom d'heure actuelle_

Après toute la configuration, nous exportons l'objet **upload** afin de l'utiliser dans d'autres fichiers.

### 4. Configurer une route pour télécharger une image

Nous avons presque terminé, mais les utilisateurs de notre application n'ont toujours pas accès au téléchargement d'images. Nous devons exposer cette fonctionnalité à eux. Créons un endpoint pour enregistrer un fichier.

Nous exportons notre objet upload que nous avons créé précédemment et en créons un nouveau. Le nouveau est plus spécifique avec une configuration supplémentaire pour un **téléchargement d'image unique**. Nous lui fournissons une valeur 'image'. **Cette valeur** est très importante, car nous allons envoyer notre fichier à un serveur sous cette clé.

**La deuxième partie est la route elle-même. L'endpoint POST** vers '/image-upload'. À l'intérieur, nous appelons **singleUpload**. N'oubliez pas de **passer req et res à l'intérieur**, car multer obtiendra le fichier que nous envoyons au serveur à partir de l'objet req.

Nous vérifions s'il y a une erreur. S'il n'y en a pas, nous renvoyons un JSON avec la valeur de l'emplacement de notre fichier, qui est simplement une **URL vers le fichier sur Amazon**.

**Et voilà !** Nous pouvons maintenant télécharger des fichiers vers Amazon S3. Plutôt simple, non ?

### 5. Testons-le dans Postman.

Pour voir les résultats de notre travail acharné, nous devons envoyer une requête au serveur avec une image que nous voulons télécharger. Dans cette partie, nous allons le tester via Postman. Dans la prochaine partie du tutoriel, nous créerons une mise en œuvre dans une application Angular.

Si vous n'avez pas **Postman**, vous pouvez simplement le télécharger en tant qu'extension Google Chrome. Recherchez simplement 'postman google chrome extension'. Postman est une application pour initialiser, envoyer et tester des requêtes au serveur de manière simple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OQiXF-lDa8GUhcKh7nZDGw.png)
_Postman_

1. **Envoyez une requête post** à un endpoint que nous avons créé précédemment. Dans mon cas, j'ai spécifié dans le chemin node de **/image-upload**.
2. Sélectionnez **Body** de **form-data**.
3. Fournissez la **clé** d'une **image**. Vous remarquerez que c'est une **clé** que nous avons configurée précédemment dans notre code. Vérifiez un fichier et choisissez un fichier de votre ordinateur.
4. **Envoyez la requête**.

Vous devriez recevoir un JSON avec l'URL de votre fichier téléchargé.

**Voilà ! C'est tout les gars. Il s'agit d'un téléchargement de fichier simple pour Node.** Dans le prochain article, je continuerai avec une mise en œuvre frontend pour Angular.

Si vous aimez ce tutoriel, n'hésitez pas à consulter mon cours complet sur Udemy — [The Complete Angular, React & Node Guide | Airbnb style app](http://bit.ly/2NeWna4).

**Conférence vidéo :** [Vidéo YouTube](https://www.youtube.com/watch?v=ASuU4km3VHE&t=1047s)

**Projet terminé :** [Mon dépôt github](https://github.com/Jerga99/bwm-ng)

À votre santé,

Filip