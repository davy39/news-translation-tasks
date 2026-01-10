---
title: Comment j'ai utilisé mes compétences en programmation pour faire remplacer
  ma poussette perdue par une compagnie aérienne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-02T20:40:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-my-programming-skills-to-buy-a-stroller-2778cb85e8b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0Q8RiaA1CbA_klX1UWy6rw.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai utilisé mes compétences en programmation pour faire remplacer
  ma poussette perdue par une compagnie aérienne
seo_desc: 'By Kristóf Litavecz

  Last summer my wife and our two children flew from Hungary to California to visit
  friends. Among other complications, our airline lost our little one’s stroller on
  the way.

  After numerous unsuccessful attempts to contact the airli...'
---

Par Kristóf Litavecz

L'été dernier, ma femme et nos deux enfants avons volé de la Hongrie vers la Californie pour rendre visite à des amis. Parmi d'autres complications, la compagnie aérienne a perdu la poussette de notre petit en chemin.

Après de nombreuses tentatives infructueuses pour contacter la compagnie aérienne par e-mails, tweets, appels téléphoniques amicaux — puis en colère — pour couvrir nos frais, j'en avais assez. J'ai décidé de passer à l'étape suivante.

J'ai donc créé un **Twitter Bot** qui répondait à chaque tweet du compte de la compagnie aérienne pour leur rappeler notre cas, qui était en attente depuis plus de trois mois à ce moment-là.

En aucun cas je n'ai fait cela pour me venger ou extorquer de l'argent. Tout ce que je voulais, c'était qu'ils nous traitent équitablement et couvrent les frais d'une poussette perdue pour enfant.

J'apprenais à programmer depuis environ un an, et j'utilisais beaucoup la [communauté freeCodeCamp](https://medium.freecodecamp.org/) pour le soutien et l'inspiration.

Voici donc ce que j'ai fait :

1. J'ai créé un nouvel environnement de développement **Cloud9**
2. J'ai créé un compte **Twitter**
3. J'ai créé un simple Twitter Bot en utilisant Node.js
4. Je l'ai configuré pour qu'il tweete aléatoirement l'un des dix messages de rappel chaque heure
5. Ensuite, j'ai lancé le bot

Une semaine et demie plus tard, l'argent est arrivé sur mon compte, et j'ai acheté une nouvelle poussette.

J'ai mis tout mon code sur [ce dépôt GitHub](https://github.com/krizsoo/twitterbot) au cas où vous vous retrouveriez dans une situation similaire. Et voici comment j'ai fait tout cela.

### Étape #1 : Créer un nouvel environnement Cloud9 IDE

Rendez-vous sur [Cloud9](http://c9.io) et créez un nouvel espace de travail.

![Image](https://cdn-media-1.freecodecamp.org/images/L58T39ZkxkR9bwgGR7CGfoBwi7p5x9pAeGkN)
_Créer un nouvel espace de travail en utilisant et sélectionner le modèle Node.js_

Si vous souhaitez répliquer mon bot, clonez simplement mon dépôt en entrant la ligne suivante dans votre terminal :

`git clone [https://github.com/krizsoo/twitterbot](https://github.com/krizsoo/twitterbot)`

### Étape #2 : Créer un compte Twitter et une application Twitter

Si vous n'avez pas encore de compte Twitter, [allez-y et créez-en un](https://twitter.com/signup). Une fois inscrit, vous pouvez créer une nouvelle application, qui vous permettra d'accéder à l'API de Twitter et de générer des tweets de manière programmatique.

![Image](https://cdn-media-1.freecodecamp.org/images/lZ541M5OVVDR7jFixIpXnvW6k681gFHNSOJa)

Dès que mon application a été configurée, j'ai récupéré **quatre clés de sécurité** nécessaires pour accéder à l'API :

![Image](https://cdn-media-1.freecodecamp.org/images/7h1aJxOUcTLt6v4NkoauztnOEhyUNcEPazcA)

* Consumer Key (API Key)
* Consumer Secret (API Secret)
* Access Token
* Access Token Secret

Toutes les clés ci-dessus doivent être ajoutées au fichier config.js de la manière suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/3w9dpLtnLgKPxHMQhsptfTQxK-YdhE651Xs-)

### Étape #3 : Configurer le Twitter bot

J'ai dû faire une configuration initiale pour m'assurer que le bot fasse ce qu'il est censé faire.

#### **1. Installer les dépendances Node.js**

```
npm install --save twitter
```

#### **2. Configurer la requête de recherche**

C'était une étape importante pour définir une requête de recherche à laquelle le Bot répondait. Je suis allé dans le fichier "app.js" et j'ai mis à jour les paramètres de recherche.

* `q` représente les mots-clés.
* `count` représente le nombre de tweets que la requête doit retourner.
* `result_type` représente la logique de tri, dans notre cas, il montre le plus récent en premier.
* `lang` signifie la langue (par exemple, l'anglais).

La configuration ci-dessous répondrait automatiquement au tweet le plus récent contenant "@freecodecamp"

```
// Configurer vos paramètres de recherchevar params = {  q: '@freecodecamp',  count: 1,  result_type: 'recent',  lang: 'en'}
```

### **Étape #4 : Configurer les tweets**

Puisque le Bot fonctionnait toutes les heures, je ne voulais pas qu'il tweete le même message encore et encore. J'ai donc créé un tableau de dix tweets environ et le Bot en sélectionnait un aléatoirement à chaque fois.

```
// configurer un tableau de tweets qui peuvent être sélectionnés aléatoirementvar TWEETS_TO_REPLY = [    "Ceci est la première version de mes tweets",    "Ceci est la deuxième",    "Tweet 3 où est ma poussette ?"];
```

> **ÉDITION :** Comme [Jonny Asmar](https://www.freecodecamp.org/news/how-i-used-my-programming-skills-to-buy-a-stroller-2778cb85e8b2/undefined) l'a souligné ci-dessous, assurez-vous de ne pas mentionner de personnes dans vos réponses, car cela est contraire aux conditions d'utilisation de Twitter.

![Image](https://cdn-media-1.freecodecamp.org/images/HZVT7WnpRFyQrbQL-gxNb79sZiqZKvtKF0F3)

### **Étape #5 : Configurer la fréquence des tweets**

Enfin, j'ai configuré le Bot pour qu'il fonctionne toutes les heures.

J'ai d'abord créé une variable représentant une heure en millisecondes :

```
// configurer l'intervalle de temps des tweetsvar INTERVAL = 1*60*60*1000;
```

Ensuite, je me suis assuré de lancer le Bot en conséquence :

```
// Démarrer le bot et le minuteurBotStart();setInterval(BotStart, INTERVAL);
```

### Étape #6 : Lancer le bot

Dès que tout a été configuré, j'ai lancé le Bot et j'ai attendu patiemment.

```
npm run serve
```

### Ce que j'ai appris de tout cela

À ma grande surprise, environ 24 heures plus tard, un représentant du service client m'a enfin répondu. Ils m'ont informé qu'ils avaient initié le virement d'argent.

Il y a un an, je n'aurais pas pu faire tout cela. Même si c'est une petite chose, ce triomphe comptait beaucoup pour moi.

Cette histoire parle de la façon dont j'ai appris à coder en 2017, et comment j'ai trouvé une inspiration supplémentaire dans ce projet parallèle. Je n'ai pas commencé une nouvelle carrière en tant que développeur (pas encore), mais il existe de nombreuses autres façons d'utiliser vos compétences en programmation dans votre vie quotidienne. Certains soutiennent même que [le codage est devenu la 4ème compétence fondamentale](http://code.org).

Espérons que pour tous ceux qui commencent à apprendre à coder, vous trouverez un peu d'inspiration dans mon histoire également. Pendant toutes ces nuits tardives où vous luttez avec un défi de programmation, gardez à l'esprit que, que vous commenciez ou non une nouvelle carrière en tant que développeur, comprendre le langage des ordinateurs portera ses fruits un jour.

### Remerciements

Cet article n'aurait pas pu voir le jour sans la communauté freeCodeCamp, ni l'équipe CS50. Je leur suis reconnaissant pour leur soutien.

Je suis également reconnaissant envers [Brandon Morelli](https://www.freecodecamp.org/news/how-i-used-my-programming-skills-to-buy-a-stroller-2778cb85e8b2/undefined) et [Scott Spence](https://www.freecodecamp.org/news/how-i-used-my-programming-skills-to-buy-a-stroller-2778cb85e8b2/undefined) pour avoir écrit ces guides détaillés sur les Twitter Bots :

[**Créer un simple Twitter Bot avec Node.js en seulement 38 lignes de code**](https://codeburst.io/build-a-simple-twitter-bot-with-node-js-in-just-38-lines-of-code-ed92db9eb078)
[_Les tutoriels n'ont pas à être compliqués. Ensemble, nous allons créer un simple bot Twitter favoris avec Node.js en seulement 38 lignes de code..._codeburst.io](https://codeburst.io/build-a-simple-twitter-bot-with-node-js-in-just-38-lines-of-code-ed92db9eb078)
[**Pourquoi vous devriez avoir votre propre Twitter bot, et comment en créer un en moins de 30 minutes**](https://medium.freecodecamp.org/easily-set-up-your-own-twitter-bot-4aeed5e61f7f)
[_MISE À JOUR 20171102 : Depuis que cette histoire a été publiée pour la première fois en janvier 2017, il y a eu quelques changements..._medium.freecodecamp.org](https://medium.freecodecamp.org/easily-set-up-your-own-twitter-bot-4aeed5e61f7f)