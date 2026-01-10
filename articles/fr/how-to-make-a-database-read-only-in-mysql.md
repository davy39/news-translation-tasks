---
title: Comment rendre une base de données en lecture seule dans MySQL
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-06-22T22:49:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-database-read-only-in-mysql
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/altumcode-dMUt0X3f59Q-unsplash.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: Comment rendre une base de données en lecture seule dans MySQL
seo_desc: "If you are learning MySQL, then you are likely enjoying executing different\
  \ commands and checking the results afterward. \nBut you may be working on a project\
  \ where you have modified your database to an acceptable state and you're worried\
  \ about alteri..."
---

Si vous apprenez MySQL, alors vous aimez probablement exécuter différentes commandes et vérifier les résultats ensuite. 

Mais vous travaillez peut-être sur un projet où vous avez modifié votre base de données à un état acceptable et vous craignez de la modifier par erreur. Cela pourrait arriver lorsque vous travaillez dans la base de données, ou lorsque d'autres personnes ayant accès à votre ordinateur y accèdent.

Eh bien, ne craignez rien ! Dans MySQL, vous pouvez restreindre la base de données pour assurer sa sécurité. Je suppose que vous êtes un débutant en SQL, donc je ne vais pas vous ennuyer avec des choses difficiles. La chose la plus simple est de rendre la base de données **LECTURE SEULE**. Après cela, personne ne peut modifier la base de données de quelque manière que ce soit s'ils ne sont pas familiers avec certaines commandes MySQL.

### Si vous souhaitez suivre le processus étape par étape dans une vidéo, voici :

%[https://youtu.be/7kFzNo6tD-k]

## Comment rendre une base de données en LECTURE SEULE

Supposons que vous êtes déjà dans votre éditeur SQL (d'où vous pouvez exécuter vos commandes MySQL). Gardez à l'esprit que généralement, lorsque nous créons une base de données, elle vient avec un accès en lecture-écriture par défaut. 

Donc pour l'instant, supposons que le statut par défaut d'une base de données nouvellement créée est LECTURE-ÉCRITURE activée. 

Pour convertir la base de données en un état LECTURE SEULE, utilisez cette commande :

```sql
ALTER DATABASE database_name READ ONLY = 1;
```

Laissez-moi vous expliquer chaque partie du code maintenant.

Comme vous voulez changer quelque chose dans les données, vous dites à la base de données, 
"hey, je veux modifier quelque chose". Donc vous avez utilisé la commande `ALTER`. 

Ensuite vient la partie où vous lui dites quelle chose vous voulez modifier, car il pourrait y avoir plusieurs tables ou bases de données. Donc vous devez lui dire quelle chose vous voulez modifier. Donc, vous avez indiqué `DATABASE` pour préciser que vous voulez réellement modifier une base de données.

Dans votre client (MySQL Workbench/XAMPP, et ainsi de suite), il pourrait y avoir plusieurs bases de données. Donc MySQL ne serait-il pas confus sur exactement quelle base de données vous voulez modifier ? Vous ne voulez pas le confondre, n'est-ce pas ? C'est pourquoi vous devez spécifier le nom de la base de données. 

Après cela, vous lui dites exactement quelle modification vous voulez qu'il fasse. Vous voulez changer le statut `READ ONLY` à `1`. Cela signifie que **READ ONLY** est activé.

Après cela, personne ne pourra faire aucun type d'altération ou de changements (mise à jour/suppression/ajout) à cette base de données spécifique en LECTURE SEULE. Personne ne pourra même supprimer la base de données !

## Comment rendre une base de données en LECTURE-ÉCRITURE

Que faire si vous devez revenir en arrière pour pouvoir faire des mises à jour de la base de données ? Vous devez changer le statut **READ ONLY** à 0 pour indiquer que vous voulez que le statut **READ ONLY** soit désactivé (ou non en bref).

Utilisez simplement la commande suivante pour cela :

```sql
ALTER DATABASE database_name READ ONLY = 0;
```

Après cela, n'importe qui pourra faire des changements à la base de données ou même supprimer la base de données s'ils le souhaitent.

## Conclusion

N'est-ce pas un truc court mais beau ? Profitez de votre voyage de codage !

De plus, si vous aimez le contenu lié à la programmation, assurez-vous de [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) où je publie régulièrement du contenu lié à la programmation !

De plus, vous pouvez me suivre sur [GitHub](https://github.com/FahimFBA) et [Twitter](https://twitter.com/Fahim_FBA). Vous pouvez également consulter mon site web : [https://fahimbinamin.com/](https://fahimbinamin.com/)

Si vous voulez m'endosser pour des compétences pertinentes, alors faites-le en utilisant [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Image de couverture : Photo par [AltumCode](https://unsplash.com/@altumcode?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/photos/dMUt0X3f59Q?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)