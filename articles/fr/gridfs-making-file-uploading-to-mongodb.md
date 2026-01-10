---
title: 'Guide GridFS : Comment téléverser facilement des fichiers et des images vers
  MongoDB avec Node'
date: '2020-05-04T23:35:41.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/gridfs-making-file-uploading-to-mongodb
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/adobe-spark-post.png
tags:
- name: MongoDB
  slug: mongodb
- name: node
  slug: node
seo_desc: 'By Tarique Ejaz

  File storage is an important feature required in multiple processes across various
  types of applications. The existence of processes like Content Delivery Networks
  (CDNs), set up through third-party cloud options like Amazon Web Servi...'
---


Par Tarique Ejaz

<!-- more -->

Le stockage de fichiers est une fonctionnalité importante requise dans de multiples processus à travers divers types d'applications. L'existence de processus tels que les réseaux de diffusion de contenu (`Content Delivery Networks` ou `CDNs`), configurés via des options cloud tierces comme Amazon Web Services, et les options de stockage de fichiers locaux ont toujours facilité la mise en œuvre d'une telle fonctionnalité.

Cependant, le concept de stockage de fichiers directement dans une base de données via un seul appel API m'intriguait depuis un certain temps. C'est là que GridFS est entré en jeu pour moi.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/gridfs.png) _Probablement pas la meilleure façon de mettre en œuvre un système de stockage de fichiers_

## GridFS - Comprendre le concept simplement

MongoDB dispose d'une spécification de pilote pour téléverser et récupérer des fichiers appelée [GridFS][1]. GridFS vous permet de stocker et de récupérer des fichiers, y compris ceux dépassant la limite de taille des documents BSON de **16 Mo**.

GridFS prend essentiellement un fichier et le divise en plusieurs morceaux (chunks) qui sont stockés en tant que documents individuels dans deux collections :

-   _la collection `chunk`_ (stocke les parties du document), et
-   _la collection `file`_ (stocke les métadonnées supplémentaires correspondantes).

Chaque morceau est limité à une taille de 255 Ko. Cela signifie que le dernier morceau est normalement soit égal, soit inférieur à 255 Ko. Cela semble plutôt ingénieux.

Lorsque vous lisez depuis GridFS, le pilote réassemble tous les morceaux selon les besoins. Cela signifie que vous pouvez lire des sections d'un fichier en fonction de votre plage de requête. Par exemple, écouter un segment d'un fichier audio ou récupérer une section d'un fichier vidéo.

**Note :** Il est préférable d'utiliser GridFS pour stocker des fichiers dépassant normalement la limite de taille de 16 Mo. Pour les fichiers plus petits, il est recommandé d'utiliser le format BinData pour stocker les fichiers dans des documents uniques.

Ceci résume le fonctionnement général de GridFS. Il est temps de passer à la pratique avec du code et de voir comment implémenter un tel système.

## Trêve de bavardages, place au code

Nous utilisons Node.js avec un accès à une instance cloud de MongoDB pour notre configuration. Vous pouvez trouver le dépôt de code pour l'application d'exemple ici.

[https://github.com/tarique93102/gridfs-file-storage][2]

Nous allons nous concentrer entièrement sur les segments de code relatifs aux fonctionnalités de GridFS. Nous apprendrons comment le configurer et l'utiliser pour stocker des fichiers, récupérer des fichiers ou un fichier particulier, et supprimer un fichier spécifique. Commençons donc.

### Initialiser le moteur de stockage

Les paquets nécessaires pour initialiser le moteur sont [`multer-gridfs-storage`][3] et [`multer`][4]. Nous utilisons également le middleware `method-override` pour activer l'opération de suppression des fichiers. Le module npm `crypto` est utilisé pour chiffrer les noms de fichiers lors de leur stockage et de leur lecture dans la base de données.

Une fois que le moteur de stockage utilisant GridFS est initialisé, il vous suffit de l'appeler en utilisant le middleware multer. Il est ensuite transmis à la route respective exécutant les diverses opérations de stockage de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/server-app-1.png)

### Initialiser le flux GridFS

Nous initialisons un flux (stream) GridFS comme on peut le voir dans le code ci-dessous. Le flux est nécessaire pour lire les fichiers de la base de données et également pour aider à l'affichage d'une image dans un navigateur si besoin.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/server-app-2.png)

### Téléverser un seul fichier ou une image

Nous réutilisons le middleware d'upload que nous avons créé précédemment.

**Note :** Le nom `file` est utilisé comme paramètre dans `upload.single()` car nous avons la clé portant le même nom contenant le fichier envoyé par le client.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/server-app-4.png)

### Téléverser plusieurs fichiers ou images

Nous pouvons également téléverser plusieurs fichiers à la fois. Au lieu de `upload.single()`, il suffit d'utiliser `upload.multiple(<nombre de fichiers>)`.

**Note :** Le nombre de fichiers téléversés peut être inférieur au nombre de fichiers défini.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/server-app-5.png)

### Récupérer tous les fichiers de la base de données

En utilisant le flux initialisé, nous pouvons récupérer tous les fichiers de la base de données concernée en utilisant `gfs.find().toArray(...)`. Une fois les fichiers obtenus, nous les mappons dans un tableau et envoyons la réponse.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/server-app-6.png)

### Récupérer un seul fichier par son nom

Il est extrêmement simple d'interroger GridFS pour un seul fichier basé sur un attribut spécifique comme `filename`. En utilisant le flux GridFS, vous pouvez interroger la base de données via la fonction `gfs.find({<ajouter la requête ici>})`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/server-app-7.png)

### Afficher une image récupérée dans le navigateur

C'est une partie légèrement plus délicate car vous devez non seulement récupérer un fichier de la base de données, mais aussi l'afficher en tant qu'image sur le navigateur respectif. Nous récupérons le fichier normalement. Aucun changement dans ce processus.

Ensuite, à l'aide de la méthode `openDownloadStreamByName()` sur le flux gfs, nous pouvons facilement afficher une image car elle renvoie un flux lisible (readable stream). Cela fait, nous pouvons utiliser la méthode `pipe()` de JavaScript pour diffuser la réponse.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/server-app-8.png)

### Supprimer un fichier spécifique par son Id

Supprimer un fichier est tout aussi direct. Nous utilisons la méthode de flux `delete()` avec le paramètre `_id` pour interroger et supprimer le fichier concerné.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/server-app-9.png)

Ce sont là les principales fonctionnalités offertes par la conception du moteur de stockage. J'ai exploité les fonctionnalités GridFS abordées pour créer une application simple de téléversement d'images. Vous pouvez approfondir le code dans le [dépôt][5].

## Conclusion

Il m'a fallu un certain temps et pas mal d'efforts pour comprendre comment utiliser GridFS pour un projet personnel. Pour cette raison, je voulais m'assurer qu'au moins une autre personne n'ait pas à investir la même quantité de temps.

Cela dit, je recommanderais d'utiliser GridFS avec prudence. Ce n'est pas une solution miracle pour tous vos besoins de stockage de fichiers. Néanmoins, c'est une spécification ingénieuse à connaître et dont il faut être conscient.

Si vous avez des questions ou des préoccupations, vous pouvez commenter l'article ou me contacter sur [`LinkedIn`][6].

En attendant, continuez à coder.

[1]: https://docs.mongodb.com/manual/core/gridfs/
[2]: https://github.com/tarique93102/gridfs-file-storage
[3]: https://www.npmjs.com/package/multer-gridfs-storage
[4]: https://www.npmjs.com/package/multer
[5]: https://github.com/tarique93102/gridfs-file-storage
[6]: https://www.linkedin.com/in/tarique-ejaz/