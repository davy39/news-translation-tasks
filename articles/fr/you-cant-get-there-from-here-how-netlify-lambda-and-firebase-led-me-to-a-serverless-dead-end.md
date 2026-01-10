---
title: 'On ne peut pas y arriver d''ici : comment Netlify Lambda et Firebase m''ont
  conduit à une impasse sans serveur'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-18T23:37:48.000Z'
originalURL: https://freecodecamp.org/news/you-cant-get-there-from-here-how-netlify-lambda-and-firebase-led-me-to-a-serverless-dead-end
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/randy-laybourne-Ens_NuuHVO4-unsplash.jpg
tags:
- name: aws lambda
  slug: aws-lambda
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
- name: Netlify
  slug: netlify
seo_title: 'On ne peut pas y arriver d''ici : comment Netlify Lambda et Firebase m''ont
  conduit à une impasse sans serveur'
seo_desc: 'By Jeff M Lowery

  [Update: Apparently you can get there from here! That is, if you use firebase-admin
  instead of @google-cloud/firestore.  I''ll have more on this in the future, but
  the gist of it is summarized here.]

  A while back I was exploring Netli...'
---

Par Jeff M Lowery

[**Mise à jour :** Apparemment, on _**peut**_ y arriver d'ici ! C'est-à-dire, si vous utilisez `firebase-admin` au lieu de `@google-cloud/firestore`. J'aurai plus d'informations à ce sujet dans le futur, mais l'essentiel est résumé [ici](https://github.com/arjunyel/firestore-apollo-graphql#graphql).]

[Il y a quelque temps](https://www.freecodecamp.org/news/how-to-use-faunadb/), j'explorais [le support de Netlify pour FaunaDB](https://www.netlify.com/blog/2019/09/10/announcing-the-faunadb-add-on-for-netlify/) : une base de données NoSQL orientée documents avec des fonctionnalités spéciales pour [gérer les transactions sur des serveurs de base de données dispersés](https://fauna.com/blog/consistency-without-clocks-faunadb-transaction-protocol). J'ai décidé de l'essayer car c'était un choix pratique, puisque il y avait [du code exemple](https://github.com/netlify/netlify-faunadb-example) avec lequel je pouvais commencer. L'exemple utilisait des [fonctions lambda](https://docs.netlify.com/functions/overview/) comme interface pour la base de données.

![fauna avec lambda](https://user-images.githubusercontent.com/532272/42067494-5c4c2b94-7afb-11e8-91b4-0bef66d85584.png)

J'ai modifié les fonctions lambda originales pour qu'elles communiquent avec l'API GraphQL de FaunaDB (au lieu de [FQL](https://docs.fauna.com/fauna/current/api/fql/)). Bien que [cela ait fonctionné](https://www.freecodecamp.org/news/how-to-use-faunadb/), j'ai finalement estimé que le support de GraphQL par Fauna n'était pas tout à fait mûr, alors j'ai cherché des alternatives.

J'ai finalement opté pour [Cloud Firestore](https://firebase.google.com/docs/firestore/rtdb-vs-firestore). J'ai basé ce nouveau projet sur l'exemple Fauna, en remplaçant le module **faunadb** par [apollo-server-lambda](https://www.npmjs.com/package/apollo-server-lambda), afin de pouvoir écrire ma propre API GraphQL et mes résolveurs.

L'une des améliorations [que j'ai dû apporter](https://github.com/netlify/netlify-lambda/issues/112) a été de déplacer toutes mes dépendances de fonction Netlify vers le dossier /functions dans mon projet (séparé et au même niveau que le dossier /src qui contient mon client React). Pour ce faire, j'ai exécuté `npm init` dans le dossier functions, j'ai déplacé un ensemble de dépendances du fichier package.json de niveau supérieur vers le nouveau /functions/package.json, j'ai ajouté un [webpack.functions.js](https://github.com/netlify/netlify-lambda/issues/112#issuecomment-488644361), puis j'ai exécuté `yarn install` pour extraire les packages dans un nouveau dossier node_modules.

Le résultat était le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-18-at-1.06.47-PM.png)

Je parlerai des sous-dossiers plus tard ; la principale chose à remarquer est qu'il y a des fichiers yarn, plus package.json, un dossier node_modules, un dossier schema, et quelques fichiers .js pour les tests.

Le projet original utilisait [netlify_lambda](https://github.com/netlify/netlify-lambda) pour construire, qui utilise webpack et babel. J'ai rencontré [certains problèmes](https://github.com/netlify/netlify-lambda/issues/183), je les ai résolus, puis je les ai rencontrés à nouveau plus tard.

Frustré, j'ai décidé de ne pas utiliser netlify-lambda et j'ai choisi [Netlify Dev](https://www.netlify.com/products/dev/) pour construire et déployer depuis la ligne de commande. L'inconvénient était que je n'avais pas la possibilité de lancer un serveur local, mais je pouvais déployer des candidats sur Netlify et les tester sans d'abord vérifier la source dans github ou déployer directement en production.

Il y avait moins de pièces mobiles puisque webpack et babel n'étaient plus nécessaires. En empruntant cette voie, vous définissez probablement la variable d'environnement **AWS_LAMBDA_JS_RUNTIME** sur **nodejs10.x** dans les paramètres _Build & deploy_ pour vos fonctions.

# Les choses ne sont pas toujours ce qu'elles semblent être

Plus familier avec les clients et serveurs GraphQL qu'avec les fonctions lambda dans le cloud, j'avais quelques hypothèses naïves sur la manière dont les choses étaient déployées dans Netlify. Je pensais que les fonctions étaient plus ou moins copiées et que les scripts de construction étaient exécutés sur le serveur, où tout serait heureux et mes fonctions seraient appelables via des URLs.

Ce n'est pas du tout ce qui se passe.

Lorsque j'ai commencé avec netlify_lambda, il utilisait webpack pour créer un fichier de sortie functions_build. Ma configuration netlify.toml avait cela comme emplacement des **fonctions**.

```
[build]
  functions = "functions-build"
  # Cela sera exécuté lors de la construction du site
  command = "yarn build"
  # Ce répertoire est publié sur le CDN de Netlify
  publish = "build"

```

Lorsque je suis passé à l'utilisation de [Netlify Dev](https://www.netlify.com/products/dev/), j'ai abandonné le dossier de sortie et j'ai simplement déployé la source "non regroupée" /**functions**. Ce n'est pas la fin de l'histoire, cependant.

# Problèmes d'authentification

Dans le projet FaunaDB, l'authentification se faisait via une variable d'environnement dont la valeur était un simple jeton. Un mécanisme similaire est utilisé par Firebase, mais au lieu d'un jeton, la valeur de la variable est un chemin vers un fichier d'identifiants que vous générez via la console FireBase. Les fonctions lambda créent une instance Firebase, et cette instance recherche la variable d'environnement pour localiser le fichier d'identifiants pour l'authentification.

Il semble que, peu importe où je plaçais ce fichier d'identifiants ou quel chemin j'utilisais, le client Firebase ne parvenait pas à le trouver. Au cours de mes recherches, je suis tombé sur une mention de l'utilitaire [zip-it-and-ship-it](https://github.com/netlify/zip-it-and-ship-it) de Netlify, que d'autres personnes avec d'autres problèmes recommandaient pour regrouper les fonctions dans des fichiers zip.

Je l'ai essayé, en modifiant le processus de construction pour appeler un script NodeJS qui compressait mes fonctions dans un dossier **functions-dist** (en modifiant la configuration **netlify.toml** pour qu'elle ne pointe pas vers ce dossier au lieu du dossier source **functions**). Bien que cela n'ait pas immédiatement résolu mes problèmes avec le fichier d'identifiants, j'ai remarqué certaines choses.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-18-at-1.58.30-PM.png)

J'ai commencé à réaliser que, lorsque chaque fichier .js de fonction lambda était regroupé dans un fichier zip, il contenait également son propre dossier **node_modules**. De plus, le dossier node_modules était "personnalisé" pour contenir uniquement les dépendances explicitement requises par chaque fonction.

## Astucieux, mais pas assez

Cela a nécessité quelques réflexions, mais j'ai décidé que si j'ajoutais mon fichier .json dans un projet local, puis en faisais une dépendance pour chaque fonction lambda, il serait intégré dans le dossier node_modules. À ce moment-là, j'aurais un chemin : **./creds/mycred.json**. Hourra !

Cela n'a pas tout à fait fonctionné—lorsque j'ai examiné les fichiers zip, les fichiers d'identifiants étaient là dans chaque archive zip, mais le client Firebase ne pouvait toujours pas y accéder.

J'ai avoué mon échec total sur le forum de support de Netlify, disant que je prévoyais de rejoindre une commune pour apprendre à tisser des [hamacs](https://www.twinoakshammocks.com/).

# À l'aide !

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-213.png)
_Photo par [Unsplash](https://unsplash.com/@jonnysplsh?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Jonny Caspari</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

J'ai dû évoquer quelque pitié, car Dennis de Netlify a bientôt répondu et m'a fait savoir que les fonctions lambda ne peuvent pas réellement accéder au système de fichiers. Ce que je tentais (charger les identifiants via un chemin de fichier) était impossible. Il a suggéré d'importer le fichier dans chaque lambda .js (ce que j'avais déjà fait). Il ne semble pas, cependant, que le client Firebase vous permette de charger les identifiants via une importation.

Mis à part cela, Dennis a plus ou moins suggéré que ce n'était peut-être pas vraiment l'approche que je devrais prendre, de toute façon. Il avait raison. La seule raison pour laquelle je suis passé par cette voie était que je suivais l'un des exemples de Netlify, mais remplacer le package **faunadb** par **apollo-server-lambda** _aurait peut-être_ ajouté beaucoup plus de poids aux fonctions lambda ; si c'est le cas, cela aurait probablement un impact sur les temps de démarrage lors des [démarrages à froid](https://hackernoon.com/im-afraid-you-re-thinking-about-aws-lambda-cold-starts-all-wrong-7d907f278a4f).

# Abandonner les fonctions lambda

Les fonctions lambda ne sont [pas une solution pour tout](https://hackernoon.com/developer-challenges-of-serverless-and-aws-lambda-8b8d5e299a34). Dans mon cas, je voulais simplement un magasin de données simple avec une interface GraphQL, sans exposer les requêtes GraphQL dans la console du navigateur.

Je peux atteindre les mêmes objectifs en ayant un processus Node héberger à la fois un client React et un serveur GraphQL. Je suis (presque) certain que je ne rencontrerai aucun problème d'accès au système de fichiers, et si c'est le cas, je passerai à [une autre méthode d'authentification](https://cloud.google.com/docs/authentication/production).