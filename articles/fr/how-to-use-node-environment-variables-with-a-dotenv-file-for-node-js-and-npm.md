---
title: Comment utiliser les variables d'environnement Node avec un fichier DotEnv
  pour Node.js et npm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-25T00:48:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-node-environment-variables-with-a-dotenv-file-for-node-js-and-npm
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/node-env-variables.jpg
tags:
- name: node
  slug: node
- name: node js
  slug: node-js
- name: npm
  slug: npm
seo_title: Comment utiliser les variables d'environnement Node avec un fichier DotEnv
  pour Node.js et npm
seo_desc: "By Veronica Stork\nEnvironment variables are variables that are set outside\
  \ of a program, often through a cloud provider or operating system. \nIn Node, environment\
  \ variables are a great way to securely and conveniently configure things that don't\
  \ chan..."
---

Par Veronica Stork

Les variables d'environnement sont des variables définies à l'extérieur d'un programme, souvent via un fournisseur de cloud ou un système d'exploitation. 

Dans Node, les variables d'environnement sont un excellent moyen de configurer de manière sécurisée et pratique des éléments qui ne changent pas souvent, comme les URL, les clés d'authentification et les mots de passe.

## Comment créer des variables d'environnement

Les variables d'environnement sont supportées nativement par Node et sont accessibles via l'objet `env` (qui est une propriété de l'objet global `process`). 

Pour voir cela en action, vous pouvez créer votre propre variable d'environnement directement dans le REPL de Node en ajoutant une variable directement à l'objet `process.env`. 

Par exemple, pour créer une variable d'environnement afin de stocker la [combinaison de ma valise](https://www.youtube.com/watch?v=a6iW-8xPw3k), je pourrais assigner la variable comme ceci : `process.env.LUGGAGE_COMBO="12345"`.

(Petite parenthèse : par convention, les variables d'environnement sont généralement écrites tout en majuscules.)

Bien qu'il s'agisse d'une expérience intéressante, vous n'utiliseriez pas le REPL de Node de cette manière dans une application. Pour créer des variables d'environnement dans votre application Node, vous voudrez probablement utiliser un package comme DotEnv. 

## Comment utiliser DotEnv

[DotEnv](https://www.npmjs.com/package/dotenv) est un package npm léger qui charge automatiquement les variables d'environnement d'un fichier `.env` dans l'objet `process.env`.

Pour utiliser DotEnv, installez-le d'abord à l'aide de la commande : `npm i dotenv`. Ensuite, dans votre application, appelez et configurez le package comme ceci : `require('dotenv').config()`. 

Notez que certains packages tels que Create React App incluent déjà DotEnv, et les fournisseurs de cloud peuvent avoir des moyens totalement différents de définir les variables d'environnement. Assurez-vous donc de consulter la documentation de tous les packages ou fournisseurs que vous utilisez avant de suivre les conseils de cet article. 

## Comment créer un fichier .env

Une fois que vous avez installé et configuré DotEnv, créez un fichier nommé `.env` à la racine de votre structure de fichiers. C'est ici que vous créerez toutes vos variables d'environnement, écrites au format `NOM=valeur`. Par exemple, vous pourriez définir une variable de port à 3000 comme ceci : `PORT=3000`. 

Vous pouvez déclarer plusieurs variables dans le fichier `.env`. Par exemple, vous pourriez définir des variables d'environnement liées à une base de données comme ceci :

```
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=password
```

Il n'est pas nécessaire d'entourer les chaînes de caractères par des guillemets. DotEnv le fait automatiquement pour vous.

Une fois ce fichier créé, n'oubliez pas que vous ne devez pas le pousser sur GitHub car il peut contenir des données sensibles comme des clés d'authentification et des mots de passe. Ajoutez le fichier au .gitignore pour éviter de le pousser accidentellement vers un dépôt public.

## Comment accéder aux variables d'environnement

Accéder à vos variables est super facile ! Elles sont attachées à l'objet `process.env`, vous pouvez donc y accéder en utilisant le modèle `process.env.KEY`.  

Si jamais vous avez besoin de changer la valeur de l'une de vos variables d'environnement, il vous suffit de modifier le fichier `.env`.

## Conclusion

Les variables d'environnement rendront votre code plus facile à maintenir et plus sécurisé. Elles sont faciles à mettre en place avec Dotenv et simples à utiliser dans Node. 

Maintenant que vous savez comment faire, vous pouvez créer vos propres variables d'environnement pour votre application Node. Profitez-en !