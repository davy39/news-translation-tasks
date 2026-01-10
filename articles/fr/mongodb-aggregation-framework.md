---
title: Comment gérer le traitement avancé des données avec le Framework d'Agrégation
  de MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-14T21:27:59.000Z'
originalURL: https://freecodecamp.org/news/mongodb-aggregation-framework
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/thumbx.jpg
tags:
- name: database
  slug: database
- name: MongoDB
  slug: mongodb
seo_title: Comment gérer le traitement avancé des données avec le Framework d'Agrégation
  de MongoDB
seo_desc: "By Mehul Mohan\nMongoDB has come a long way. Even though there are many\
  \ NoSQL databases out there, MongoDB is the first database that comes to mind when\
  \ talking about NoSQL databases. \nAlthough there always has been a bit of heat\
  \ between people who li..."
---

Par Mehul Mohan

MongoDB a parcouru un long chemin. Même s'il existe de nombreuses bases de données NoSQL, MongoDB est la première base de données qui vient à l'esprit lorsque l'on parle de bases de données NoSQL. 

Bien qu'il y ait toujours eu un peu de tension entre les personnes qui aiment SQL et celles qui préfèrent NoSQL, la vérité est que des bases de données comme MongoDB résolvent un problème différent. 

Et elles peuvent être vraiment utiles lorsque l'on manipule des données non structurées où manipuler rapidement et efficacement la forme des données (et les transformer en connaissances pertinentes) est plus utile que les performances solides fournies par les bases de données SQL traditionnelles.

MongoDB vient avec un framework puissant pour faire cela – c'est-à-dire manipuler les données directement sur le serveur : le Framework d'Agrégation. Plongeons-nous dedans et couvrons quelques points rapides à son sujet, ce qu'il est et pourquoi il est important.

## Qu'est-ce que le Framework d'Agrégation ?

Le Framework d'Agrégation est simplement un moyen d'interroger des documents dans une collection dans MongoDB. Ce framework existe parce que lorsque vous commencez à travailler avec et à manipuler des données, vous avez souvent besoin de regrouper des collections, de les modifier, d'extraire des champs, de renommer des champs, de les concaténer, de regrouper des documents par champ, d'éclater des tableaux de champs dans différents documents, et ainsi de suite. 

Cela ne peut pas être fait par le système de requêtes traditionnel que MongoDB propose (c'est-à-dire la requête find ou update, ou toute autre requête que vous auriez pu utiliser).

L'ensemble de requêtes simple dans MongoDB ne vous permet que de récupérer des documents individuels en entier ou en partie. Ils ne vous permettent pas vraiment de manipuler les documents sur le serveur et ensuite de les retourner à votre application. 

C'est là que le framework d'agrégation de MongoDB intervient. Ce n'est rien d'externe, car l'agrégation est intégrée à MongoDB. Vous pouvez apprendre à travailler avec le framework d'agrégation MongoDB en utilisant cette [playlist YouTube gratuite que j'ai créée](https://www.youtube.com/playlist?list=PLYxzS__5yYQmr3HQQJMPBMbKtMY37sdsv).

## Pipeline

Le Framework d'Agrégation repose sur le concept de pipeline. Regardons une image qui l'explique de manière plus claire :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/pipeline.png)

Ici, comme vous pouvez le voir, nous prenons une collection et la passons à travers un pipeline. Ce pipeline se compose de certaines étapes où certains **opérateurs** modifient les documents dans la collection en utilisant diverses techniques. Enfin, le résultat est retourné à l'application appelant la requête.

Comparez-le avec une simple requête, comme find. Bien sûr, elle fonctionne dans la plupart des cas, mais elle n'est pas vraiment utile lorsque vous voulez modifier les données tout en les récupérant. 

Soit vous devrez récupérer les documents et les modifier en conséquence dans l'application sur le serveur, soit, pire, vous les enverrez au client et laisserez le code frontal les modifier pour vous. 

Dans les deux cas, vous gaspillez des ressources et de la bande passante. Ainsi, le framework d'agrégation résout élégamment ce problème. Voyons comment il le fait avec les opérateurs.

## Opérateurs de Pipeline

Dans MongoDB, le pipeline est un tableau composé de divers opérateurs, qui prennent un ensemble de documents et renvoient des documents modifiés selon les règles spécifiées par le programmeur. L'opérateur suivant prend les documents renvoyés par l'opérateur précédent, d'où le nom de pipeline. 

Vous pouvez avoir de nombreux opérateurs dans un pipeline, et ces opérateurs peuvent également être répétés, contrairement aux requêtes MongoDB régulières.

Examinons quelques opérateurs de pipeline courants dans MongoDB.

### $group

Cet opérateur vous permet de regrouper un ensemble de documents sur la base d'un certain champ dans les documents. Il peut également être utilisé pour regrouper les divers champs dans les documents ensemble. 

Je suis un grand croyant dans le dicton qu'une image vaut mille mots. Une vidéo vaut mille images (eh bien, techniquement beaucoup plus d'images, mais bon), alors regardons une vidéo rapide à ce sujet :

%[https://youtu.be/zwjRdEhn2xs]

### $match

L'opérateur de pipeline match fonctionne de manière très similaire à l'opérateur find régulier. Le bon côté de cela, cependant, est qu'il peut être utilisé plusieurs fois parce que vous êtes dans un environnement de pipeline ! Cela le rend puissant. 

Voyons comment il est utilisé sur une collection :

%[https://www.youtube.com/watch?v=uQ2Kom7Z9Ug#&list=PLYxzS__5yYQmr3HQQJMPBMbKtMY37sdsv&index=7&t=0s]

### $limit

L'opérateur de pipeline $skip saute les N premiers documents et passe le reste des documents à l'opérateur suivant. Regardons un exemple rapide :

%[https://youtu.be/Wvy_njVn7x8]

### $skip

L'opérateur de pipeline $skip saute les N premiers documents et passe le reste des documents à l'opérateur suivant. Regardons un exemple rapide :

%[https://youtu.be/eZ8_khznKkk]

### $unwind

Cet opérateur est personnellement mon préféré. $unwind prend un champ de tableau et l'explose en plusieurs sous-documents N avec le i-ème document contenant la i-ème valeur particulière du tableau comme valeur du nom du champ. 

Combiné avec d'autres opérateurs comme $group et $match, cela devient très puissant pour le traitement des données. Cela semble confus ? Regardons un exemple simple :

%[https://youtu.be/V4UoZvb-YW8]

### $project

L'opérateur project vous permet d'extraire un ensemble de champs de chaque document et de jeter le reste. Non seulement cela, mais vous pouvez également renommer les champs extraits, concaténer des chaînes, extraire des sous-chaînes et bien plus encore ! 

Voyons comment cela fonctionne en un clin d'œil :

%[https://youtu.be/k_lBewsUMGg]

## Bonnes pratiques pour utiliser le Framework d'Agrégation

Un grand pouvoir implique de grandes responsabilités. Vous pouvez facilement exploiter le framework d'agrégation pour effectuer des requêtes simples également, il est donc important de vous assurer que vous n'écrivez pas de mauvaises requêtes de base de données. 

Pour commencer, gardez à l'esprit les points suivants :

1. MongoDB rejettera tout opérateur qui prend plus de 100 Mo de RAM et générera une erreur. Assurez-vous donc de réduire vos données dès que possible, car un seul opérateur ne doit pas prendre plus de 100 Mo de mémoire.
2. L'ordre compte ! Mettre $match en premier réduira le nombre de documents passés au reste du pipeline. Mettre $project ensuite réduira davantage la taille d'un document individuel en se débarrassant des champs.
3. Enfin, assurez-vous de faire tout le travail qui nécessite l'utilisation de champs indexés (tri, correspondance, etc.) avant d'utiliser des opérateurs comme $project ou $unwind. Cela est dû au fait que ces opérateurs créent de nouveaux documents qui n'ont pas les index du document original.

## Conclusion

MongoDB est un excellent outil de base de données et peut être vraiment utile pour les petites startups et les entreprises qui veulent itérer rapidement. Cela est en partie dû à ses restrictions souples et à sa nature tolérante.

J'utilise moi-même MongoDB sur [codedamn](https://codedamn.com) - une plateforme pour les développeurs comme vous où tout le monde apprend et se connecte !

Paix !