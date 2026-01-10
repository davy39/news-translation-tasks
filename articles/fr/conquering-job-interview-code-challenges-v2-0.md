---
title: 'Comment maîtriser les défis de code en entretien d''embauche v2.0 : créer
  une application web front-end'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-19T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/conquering-job-interview-code-challenges-v2-0
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/lou-levit-B4op5oZ4x5Q-unsplash.jpg
tags:
- name: challenge
  slug: challenge
- name: code challenge
  slug: code-challenge
- name: coding challenge
  slug: coding-challenge
- name: coding interview
  slug: coding-interview
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: Job Hunting
  slug: job-hunting
- name: Job Interview
  slug: job-interview
- name: learn to code
  slug: learn-to-code
- name: learning to code
  slug: learning-to-code
seo_title: 'Comment maîtriser les défis de code en entretien d''embauche v2.0 : créer
  une application web front-end'
seo_desc: 'By Jonathan Sexton

  As many of you know, I landed my first developer job at the end of June and I thought
  it would be great to use the challenge I was given as the subject of today''s article.

  It is important to note that I used React to build my proje...'
---

Par Jonathan Sexton

Comme beaucoup d'entre vous le savent, j'ai [décroché mon premier emploi de développeur](https://jonathansexton.me/blog/landing-my-first-development-job-what-a-crazy-journey/) à la fin du mois de juin et j'ai pensé qu'il serait intéressant d'utiliser le défi qui m'a été donné comme sujet de l'article d'aujourd'hui.

Il est important de noter que j'ai utilisé React pour construire mon projet, mais cela aurait pu être réalisé avec n'importe quel framework front-end ou du 'vanilla JavaScript'.

Voici une liste des sujets que nous allons aborder :

* Accéder à l'[API Quip Automation](https://quip.com/dev/automation/documentation#token-endpoint)
* Créer des feuilles de calcul/documents avec l'API Quip
* Installer et utiliser la bibliothèque [Axios](https://github.com/axios/axios) (ceci est optionnel et vous pouvez faire des requêtes API sans elle, mais j'aime la syntaxe)
* Utiliser le [package qs](https://www.npmjs.com/package/qs) pour stringifier les requêtes (ceci n'est pas une exigence, mais je voulais essayer quelque chose de nouveau et si cela ne fonctionnait pas, j'avais toujours la solution de repli de savoir qu'Axios stringifiera mes requêtes par défaut)
* Faire des requêtes [POST](https://en.wikipedia.org/wiki/POST_(HTTP)) et [GET](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods)

Pour contexte, voici un extrait des exigences telles que je les ai reçues :

"_Créez une application web front-end qui interagit avec l'API Quip de la manière suivante :_"

* _Créez une feuille de calcul (points bonus pour importer des données dans la nouvelle feuille de calcul créée)._
* _Par importer des données, je veux dire télécharger une feuille de calcul Excel, ou copier et coller des données dans une feuille de calcul Quip._
* _Exporter une feuille de calcul Quip vers .xlsx_
* _Télécharger (sauvegarder) un dossier/multiples documents._

_Créez l'interface utilisateur de la page de la manière qui vous semble appropriée (boutons, boîtes de dialogue, etc.)._"

J'étais un peu inquiet lorsque j'ai lu les exigences, car je n'étais pas exactement sûr par où commencer. Alors, j'ai plongé dans la documentation de l'API et j'ai commencé à absorber des informations. Heureusement, aucune limite de temps ne m'a été donnée, mais je voulais terminer cela le plus rapidement possible pour voir où j'en étais dans le processus d'entretien.

Pour commencer, j'ai conçu un prototype du produit fini dans Figma afin d'avoir une feuille de route à suivre. Ce n'est pas une étape obligatoire, mais cela rend l'expérience de construction de votre projet beaucoup plus fluide.

Très bien, plongeons-nous dedans !

## Installation

J'ai construit mes composants Nav, Footer et Content afin d'avoir une base solide pour mon application.

Chacun de ces composants retourne du JSX basique et il n'y a pas grand-chose à dire à leur sujet (si vous souhaitez voir le code de chacun, vous pouvez consulter le [dépôt GitHub](https://github.com/JS-goose/gibson-code-challenge) du projet).

J'ai décidé que la majorité des requêtes serait répartie entre les fichiers _`App.js`_ et _`CenterContent.js`_.

Pour référence, voici la structure de mon projet :

![code react montrant une structure de projet](https://jonathansexton.me/blog/wp-content/uploads/2019/08/image.png)
_Ma structure de projet_

Vous me verrez faire référence aux requêtes POST et GET tout au long de cet article. Si vous n'êtes pas familier avec celles-ci, c'est le moment de faire quelques recherches à leur sujet. Je vais être honnête en disant que je n'étais pas à 100% sûr d'elles lorsque j'ai commencé ce projet et que j'ai dû consulter quelques ressources moi-même.

En résumé, une requête POST est lorsque nous demandons au serveur d'**_accepter_** certaines données entrantes (que nous envoyons) - dans notre cas, ces données se présentent sous la forme de la création d'un nouveau fichier de feuille de calcul.

Une requête GET est lorsque nous demandons au serveur de nous **_envoyer_** des données à partir d'une ressource spécifiée sur le serveur.

J'ai utilisé le [client REST Insomnia](https://insomnia.rest/) pour m'aider à déboguer les problèmes avec mes requêtes. Je travaille sur un guide pour débutants à ce sujet, alors restez à l'écoute !

## Utilisation de l'API Quip

Si vous êtes comme moi, vous n'avez jamais entendu parler de l'API Quip et vous ne savez pas ce qu'elle fait. À sa base, Quip est un outil d'automatisation qui vous permet de vous intégrer avec des outils comme [SalesForce](https://www.salesforce.com/) pour rendre votre équipe commerciale plus collaborative.

Pour nos besoins, nous allons l'utiliser pour créer des feuilles de calcul Excel sur mon compte Quip (si vous souhaitez reproduire ce projet, vous devrez créer un compte Quip - c'est gratuit).

Vous devrez également créer un jeton de développeur personnel afin de faire des requêtes. Vous pouvez le faire [ici](https://quip.com/dev/token) (nécessite un compte). Une fois que vous avez votre jeton, gardez-le dans un endroit sûr car nous allons l'utiliser bientôt.

Pour commencer, j'ai installé Axios dans mon projet en exécutant `npm install axios`, puis je l'ai importé dans les fichiers où j'avais besoin de faire mes requêtes avec `import axios from "axios";`

![un extrait de code montrant les instructions d'importation de react](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-1.png)
_Mes instructions d'importation pour les packages requis_

## Authentification

Avant de faire des requêtes au serveur, je devais m'authentifier avec mes identifiants. J'ai décidé de mettre cela dans le fichier `App.js` à l'intérieur d'une méthode de cycle de vie `componentDidMount` afin qu'il se charge à chaque fois que la page se charge :

![un code react montrant un appel d'authentification à une API externe](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-4.png)
_Ma fonction d'authentification_

J'ai donc construit ma fonction, j'ai appelé ma fonction et pendant un moment, j'ai pensé que tout allait bien, jusqu'à ce que je tombe sur cette erreur redoutée :

```
"Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at $websiteName"
```

Non !!! Le monstre CORS redouté lève sa tête puissante ! (CORS est en fait un intermédiaire utile entre moi et le serveur, mais peut être ennuyeux à gérer si vous n'avez jamais vu cette erreur auparavant).

_*Note de côté - si vous n'avez jamais vu cette erreur auparavant, ne vous inquiétez pas ! Je ne la comprends toujours pas complètement, mais je sais assez pour la déboguer. Si vous êtes bloqué, consultez le lien ci-dessus pour des informations utiles ou regardez ci-dessous pour une solution rapide.*_

Un moyen facile de contourner cela est d'utiliser un proxy comme la ressource gratuite [CORS Anywhere](https://cors-anywhere.herokuapp.com/). Essentiellement, placez ce lien `https://cors-anywhere.herokuapp.com/` devant votre URL de point de terminaison et cela résoudra le problème, pour l'instant.

Cet outil pratique vous permettra de faire vos requêtes **_pendant le développement sur localhost_** . Si j'étais vous, je ferais quelques recherches avant d'utiliser cette approche en production. Avertissement complet, je ne sais pas assez sur ce petit truc pour vous dire s'il est sûr de l'utiliser en production ou non.

Ainsi, après quelques ajustements de la fonction d'authentification, j'ai obtenu le résultat souhaité pour le journal de la console. Il est temps de passer à la réalisation de requêtes !

## Réalisation de requêtes

Maintenant que mon authentification fonctionne, nous sommes prêts à faire quelques requêtes. Je savais que j'allais faire une requête POST chaque fois que je voulais créer un nouveau document et que je voulais également lier cette action au clic d'un bouton. Voici donc ma fonction POST :

![un appel de fonction POST à une API externe](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-3.png)
_Ma fonction POST_

Vous remarquerez que c'est ici que notre package `qs` que j'ai mentionné au début de cet article entre en jeu. Je ne suis pas un expert, mais d'après ce que j'ai compris après avoir lu la documentation à ce sujet, ce package transforme ma requête en une chaîne à envoyer au serveur. Si vous préférez ne pas utiliser ce package, ce n'est pas un problème, car `Axios` le fera par défaut. Je sais que `qs` offre plus que la simple transformation de données en chaîne, mais je ne suis pas familier avec toute la gamme de ses capacités.

Maintenant, je veux que cette fonction se déclenche lors du clic sur un bouton. Ainsi, un bouton basique est né !

![un code react pour un bouton simple](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-5-1024x96.png)
_Un bouton React simple avec une méthode de clic_

Ma fonction POST a été construite, mon bouton a été construit, et la méthode qui y est liée. Il est temps de croiser les doigts et de voir ce que ma fonction a renvoyé dans la console :

![une instruction de journalisation de la console à partir d'un appel d'API externe](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-6.png)
_Le résultat de ma requête serveur - ça marche !_

À ce stade, je suis aux anges ! Je suis au-delà de l'excitation que cet appel d'API non seulement fonctionne, mais retourne également quelque chose. Maintenant, le vrai test... cela apparaît-il comme une nouvelle feuille de calcul sur mon compte Quip ?

![un compte quip montrant la création d'une feuille de calcul](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-7.png)

J'ai l'instruction de la console et la confirmation de mon compte Quip montrant que j'ai réussi à créer une nouvelle feuille de calcul - c'est génial ! Je suis extatique et j'ai littéralement bondi de ma chaise et crié "YEEEEEEESSSSSS !!!" une fois que j'ai obtenu les deux.

Ce sentiment de faire fonctionner quelque chose après avoir lutté avec est comme rien d'autre que j'ai connu dans ma vie professionnelle. Je me dis que je dois continuer à surfer sur cette vague d'enthousiasme et d'exaltation, alors je passe à l'élément suivant de la liste.

## Importer des données dans la nouvelle feuille de calcul créée

J'avais de grandes idées pour cette section de l'"assignment", mais à ce stade, cela fait presque deux semaines que j'ai commencé ce projet et je suis anxieux que l'intervieweur m'ait oublié (c'est-à-dire moi) ou soit impatient avec moi.

Alors, j'ai abandonné ces grands plans et opté pour quelque chose de plus simple afin de pouvoir rendre ce projet le plus rapidement possible.

J'ai construit une petite fonction pour au moins attacher au bouton de téléchargement afin d'avoir un type de fonctionnalité pour celui-ci. À sa base, cette fonction attend qu'un fichier soit téléchargé, définit l'état au premier élément du tableau de la cible de l'événement, puis crée des en-têtes basés sur ces informations, avec pour objectif final de les publier sur mon compte Quip avec ces informations.

Cependant, vous pouvez voir par le commentaire en haut de ce bloc de fonction que je n'ai pas réussi à le faire fonctionner correctement. Cependant, je n'avais pas le temps (du moins je pensais ne pas en avoir) de creuser profondément dans ce problème et de le résoudre.

![un extrait de code react montrant une fonction de téléchargement](https://jonathansexton.me/blog/wp-content/uploads/2019/08/image-3.png)
_Ma fonction d'importation qui n'a jamais tout à fait fonctionné correctement :)_

À ce stade, je travaille sur ce projet après le travail et la nuit depuis plus de deux semaines. Je décide qu'il est temps de le rendre sans que les autres parties fonctionnent (importation, exportation et téléchargement de données).

## Les dernières touches

Je sais que mon projet est inachevé et je me fais des reproches assez durs à ce sujet. Mais, en bonus, je décide que je vais concevoir quelque chose dans [Figma](https://www.figma.com/) comme touche supplémentaire pour aider mes chances d'obtenir un retour d'appel.

Voici le produit fini modélisé d'après leurs couleurs actuelles/police/thème :

![une application react montrant les données d'une table de base de données](https://jonathansexton.me/blog/wp-content/uploads/2019/08/image-4-1024x731.png)

## Et c'est tout

Avec mon projet non terminé mais à un point d'arrêt, je ne me sens pas très bien à propos de mes progrès et de mon timing, mais je mets tout en paquets et je le mets sur GitHub. J'ajoute l'image ci-dessus et je planifie un e-mail à envoyer le lendemain matin à 9h à l'intervieweur.

J'ai attendu près de 2 jours avec impatience en espérant obtenir un retour d'appel - quelque chose. Il est finalement arrivé alors que je conduisais pour aller au travail. L'intervieweur avait reçu mon projet et voulait que je vienne pour une autre réunion avec son développeur principal.

J'étais terrifié et excité en même temps parce que je pensais qu'ils voulaient me faire venir pour se moquer de mon code ou pour me demander ce que je pensais en construisant ce monstre. Mais ce n'était pas du tout le cas. J'ai fini par obtenir une offre d'emploi grâce à ce projet !

Si vous voulez toute l'histoire à ce sujet, vous pouvez la trouver dans mon précédent article de blog [sur l'obtention de mon premier emploi de développeur](https://jonathansexton.me/blog/landing-my-first-development-job-what-a-crazy-journey/).

J'espère que vous avez trouvé de la valeur dans cet article. Si c'est le cas, faites-le moi savoir sur [Twitter](https://twitter.com/jj_goose) ou sur l'une des autres plateformes où je poste :D

De plus, je publie la plupart de mes articles sur de grandes plateformes comme [Dev.to](https://dev.to/jsgoose) et [Medium](https://medium.com/@joncsexton), donc vous pouvez trouver mon travail là aussi !

Pendant que vous êtes ici, pourquoi ne pas vous inscrire à ma **Newsletter** - vous pouvez le faire en haut à droite de la page sur mon [blog](https://jonathansexton.me/blog). Je promets de ne jamais spammer votre boîte de réception et vos informations ne seront pas partagées avec qui que ce soit/site. J'aime occasionnellement envoyer des ressources intéressantes que je trouve, des articles sur le développement web et une liste de mes derniers articles.

Passez une journée géniale remplie d'amour, de joie et de codage !