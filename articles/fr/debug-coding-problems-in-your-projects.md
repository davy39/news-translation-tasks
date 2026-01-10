---
title: Comment déboguer les problèmes de codage lors de la création de vos propres
  projets
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2024-02-20T21:47:09.000Z'
originalURL: https://freecodecamp.org/news/debug-coding-problems-in-your-projects
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-pixabay-144243--1-.jpg
tags:
- name: debugging
  slug: debugging
- name: logging
  slug: logging
- name: 'self-improvement '
  slug: self-improvement
seo_title: Comment déboguer les problèmes de codage lors de la création de vos propres
  projets
seo_desc: 'Ah, the joy of coding! There you are, cruising through your project, when
  suddenly – bam! – you hit a bug. It''s like hitting a wall in a maze.

  But fear not, fellow coder, for I bring you the trusty map to navigate the treacherous
  bug-infested waters ...'
---

Ah, la joie du codage ! Vous êtes là, en train de naviguer dans votre projet, quand soudain - bam ! - vous tombez sur un bug. C'est comme heurter un mur dans un labyrinthe.

Mais ne craignez rien, cher collègue codeur, car je vous apporte la carte fiable pour naviguer dans les eaux infestées de bugs de la programmation. Que vous soyez un autodidacte visant à décrocher ce job de rêve dans la tech ou simplement en train de bricoler pour le plaisir, voici comment devenir un ninja du débogage.

## Rechercher les erreurs dans votre IDE

Votre Environnement de Développement Intégré (IDE) n'est pas seulement un éditeur de texte sophistiqué - c'est votre première ligne de défense contre les bugs.

TypeScript, par exemple, est comme cet ami qui vous signale le nid-de-poule dans lequel vous êtes sur le point de marcher - il aide à attraper les erreurs tôt grâce à ses compétences de vérification de type.

Imaginez que vous essayez accidentellement d'ajouter un nombre à une chaîne de caractères. TypeScript agite un grand drapeau rouge, vous évitant un moment de facepalm plus tard. C'est l'une des nombreuses raisons pour lesquelles nous adorons TS.

**Exemple** : Vous déclarez `let age: number = 'twenty';`. TypeScript va désapprouver cela, vous disant que 'twenty' n'est pas un nombre. C'est comme avoir un ange gardien pour votre code.

## Essayez et isolez la zone

Avant de commencer à vous arracher les cheveux, essayez de jouer au détective et isolez l'endroit où se trouve la scène de crime.

Le bug se cache-t-il dans le backend, se dissimule-t-il dans le frontend, complote-t-il dans la base de données, ou se détend-il dans l'infrastructure ?

Lorsque vous travaillez localement, c'est généralement l'un des trois premiers suspects. Et voici un conseil chaud : l'onglet réseau dans les outils de développement de votre navigateur est comme votre scanner de police, vous aidant à localiser l'emplacement de l'appel de détresse.

**Exemple** : Supposons que vous envoyez une requête pour GET /users et qu'elle retourne un statut 500. C'est le serveur qui vous dit, "Mon pote, j'ai des problèmes." C'est un problème de backend. Mais si l'appel revient avec un statut 200 et que votre UI joue toujours à cache-cache avec les données, alors le bug organise une fête dans votre frontend. L'onglet réseau vient de vous donner l'adresse.

En réduisant la localisation de votre problème, vous pouvez concentrer vos efforts de débogage plus efficacement. C'est comme savoir s'il faut attaquer le château, le repaire du dragon ou la forêt sombre. Bonne chasse !

## Rechercher les erreurs dans la console du navigateur

La console du navigateur est votre loupe Sherlock Holmes pour les projets web. Elle découvre des indices cachés en pleine vue. L'onglet console, quant à lui, est comme suivre où le méchant est passé, vous aidant à repérer ces erreurs de code ennuyeuses.

**Exemple** : Votre application React ne récupère pas les données. Un rapide coup d'œil dans l'onglet console montre une erreur "undefined", et un numéro de ligne. C'est là que se trouve votre problème. Élémentaire, mon cher Watson !

## Ajouter `console.log()` à différentes fonctions

Ah, le humble `console.log()`, la déclaration print qui pourrait. En cas de doute, loggez-le. C'est comme laisser des miettes de pain dans votre code pour voir jusqu'où le Petit Chaperon Rouge arrive avant de rencontrer le Grand Méchant Bug.

**Exemple** : Vous n'êtes pas sûr que votre fonction reçoive les données attendues ? `console.log('Data:', data)` au début de la fonction. Pas de données ? Maintenant vous savez où le problème commence.

## Utiliser les blocs Try-Catch

Les blocs try-catch sont votre filet de sécurité, permettant à votre code d'effectuer des exploits audacieux sans planter votre application. Ils vous permettent de gérer élégamment les erreurs en les attrapant avant qu'elles ne causent des ravages. Ils vous permettent également de spécifier vos propres messages d'erreur personnalisés pour un bloc de code donné, vous aidant à trouver la zone problématique.

**Exemple** : Enveloppez votre appel API dans un try-catch. Si l'appel échoue, le bloc catch attrape l'erreur, vous permettant de la console.log ou d'afficher un message convivial à l'utilisateur.

Voici à quoi ressemble un bloc try catch en JS :

```javascript
  function displayUsers() {
    try {
      const users = getUsers();
    } catch (error) {
      console.log("oh crap");
    }
  }
```

## Rechercher sur Google ou utiliser ChatGPT pour aider avec les messages d'erreur

Bloqué sur un message d'erreur ? Google et ChatGPT sont votre bibliothèque et votre bibliothécaire. Il suffit de copier et coller l'erreur dans la barre de recherche et de regarder une pléthore de solutions se dérouler. C'est comme demander à l'esprit de la ruche : quelqu'un, quelque part, a déjà eu votre problème.

**Exemple** : Vous obtenez un "TypeError: Cannot read property 'map' of undefined" ? Une rapide recherche révèle que vous essayez peut-être d'utiliser `.map()` sur quelque chose qui n'est pas un tableau. Oups !

## Tester souvent

Le mantra "tester tôt, tester souvent" vous fera économiser beaucoup de temps. En testant de petits morceaux de code au fur et à mesure, vous attrapez les bugs tôt, quand ils sont plus faciles à écraser. C'est comme nettoyer en cuisinant - cela rend le nettoyage final beaucoup plus facile.

**Exemple** : Vous venez d'ajouter une nouvelle fonctionnalité ? Testez-la avant de continuer. Fonctionne-t-elle comme prévu ? Super ! Non ? Il est temps de déboguer pendant que le code est encore frais dans votre esprit.

## Essayer une approche différente

Si vous vous cognez la tête contre un mur avec un problème, peut-être est-il temps de l'escalader au lieu de le traverser. Ne vous attachez pas trop à votre code. Soyez prêt à refactoriser ou même à recommencer de zéro si cela signifie une solution plus propre et plus élégante.

**Exemple** : Si votre code est plus emmêlé qu'un bol de spaghetti, faire un pas en arrière et repenser votre approche pourrait révéler un chemin plus simple et plus efficace.

Le débogage est en partie un art, en partie une science, et entièrement un test de patience. Mais avec ces stratégies dans votre boîte à outils, vous écraserez les bugs avec les meilleurs. Bon codage, et que vos chasses aux bugs soient courtes et votre code propre !

## Scénario de la vie réelle

Prenons un scénario de la vie réelle. J'ai une application React, Node, Postgres qui affiche les utilisateurs dans le navigateur. Le code, autant que je sache, devrait fonctionner mais je ne vois pas les utilisateurs affichés sur le frontend.

### Étape 1 - Vérifier la console

Jetons un coup d'œil à la console des outils de développement Chrome et voyons ce qui se passe.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/step1.PNG)
_"Regarde maman, des erreurs !"_

Ah, l'intrigue s'épaissit dans la saga de "Pourquoi ce truc ne fonctionne-t-il pas ?". Plongeons dans le drame qui se déroule dans votre console et décomposons les miettes de pain laissées par notre ami malicieux, le bug.

Tout d'abord, nous avons notre indice principal : `GET http://localhost:3000/api/users 500 (Internal Server Error)`. Cette ligne est l'équivalent d'un cri dans la nuit dans notre histoire de détective. Elle nous dit que notre backend est en détresse, peut-être lié à une requête SQL néfaste ou à un morceau de logique voyou dans notre route API.

Le cri d'aide du serveur est clair : "Internal Server Error." Un classique du backend, vraiment.

Maintenant, notre casting de soutien fait son entrée avec `ResponseError: Response returned an error code`. C'est la grande révélation. Le problème n'est pas seulement un serveur qui passe une mauvaise journée - c'est un ResponseError pris la main dans le sac par `UsersApi.request`, et il nous dit même où se trouve la ligne d'erreur (UserApi.ts:83).

### Étape 2 - Vérifier le terminal backend

Notre voyage dans l'investigation du bug nous a conduit au backend, où nous sommes accueillis avec ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/step2.PNG)

Si vous voyez cela et que votre premier instinct est de fuir et de vous cacher, ne vous inquiétez pas - c'était aussi le mien. Mais ne craignez rien ! Il y a beaucoup d'indices qui nous pointent vers le problème.

Lorsque une erreur backend se produit, ceci est ce qu'on appelle une **stack trace** - essentiellement toutes les erreurs, infos, numéros de ligne, etc. que le compilateur a rencontrés dans un grand bloc de texte. Merci le compilateur !

Ce que nous faisons ici, c'est rechercher des mots clés, des fichiers reconnaissables, ou tout ce qui est lisible par les humains. Avez-vous repéré quelque chose ? Plongeons plus profondément :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/step2-1.PNG)
_En creusant plus profondément dans les erreurs_

Les parties surlignées en **jaune** indiquent qu'il y a eu une erreur dans `userController.ts`, spécifiquement dans la fonction `getAllUsers()`. Si nous lisons plus loin, les parties surlignées en **rouge** nous pointent vers le message d'erreur :

```bash
Authentication failed against database server at `dpg-cn9kr28l6cac73a1a7eg-a.frankfurt-postgres.render.com`, 
the provided database credentials for `dmin` are not valid.\n\nPlease make sure to provide valid database credentials for the database server 
```

Hourra ! Maintenant nous connaissons l'erreur. Nous avons mal orthographié "admin" dans notre chaîne de connexion à la base de données, ce qui signifie que la connexion a échoué. Doh ! Après avoir corrigé cela, l'erreur est résolue :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/step4.PNG)
_Erreur résolue_

### Étape 3 : Vérifier la correction

Maintenant que nous avons ajouté une correction, nous pouvons vérifier en consultant le navigateur pour voir si tout fonctionne. Dans ce cas, vérifier l'UI suffit pour vérifier, mais pour des flux plus complexes, vous pouvez vérifier que l'API retourne le bon code de statut (dans ce cas, 200).

## Conclusion

J'espère que cet article a jeté quelque lumière sur la façon dont vous pouvez déboguer vos projets.

Si vous cherchez plus d'informations sur le débogage et des projets de niveau industriel à construire, vous pouvez consulter ma chaîne YouTube où nous construisons et déployons des applications full stack en utilisant React, Node et d'autres technologies cool. J'espère vous y voir !


%[https://www.youtube.com/@ChrisBlakely]