---
title: Comment améliorer et automatiser votre flux de travail de développement web
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-11-01T15:47:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-web-development-workflow
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/freeCodeCamp-Cover-1.png
tags:
- name: automation
  slug: automation
- name: Web Development
  slug: web-development
- name: workflow
  slug: workflow
seo_title: Comment améliorer et automatiser votre flux de travail de développement
  web
seo_desc: 'The modern age of Web Development is incredible. We have a plethora of
  frameworks and libraries to help us work more efficiently, tons of quality resources
  to learn from, and numerous projects to inspire us.

  My decade-long journey as a web developer ...'
---

L'ère moderne du développement web est incroyable. Nous disposons d'une pléthore de frameworks et de bibliothèques pour nous aider à travailler plus efficacement, de nombreuses ressources de qualité pour apprendre et de nombreux projets pour nous inspirer.

Mon parcours de dix ans en tant que développeur web n'est peut-être pas très différent du vôtre. Mais dernièrement, je me suis davantage concentré sur la réalisation rapide des choses avec qualité. Il ne s'agit pas seulement de ce que nous codons et de la manière dont nous le faisons. Il s'agit également de la manière dont nous testons, déboguons et enfin livrons/déployons l'application.

Dans cet article, vous apprendrez quelques flux de travail de développement web qui peuvent vous aider à développer, tester, construire et déployer plus rapidement.

## Console du navigateur – Le meilleur ami d'un développeur web

Dans mes premiers jours de développement, la console du navigateur était mon meilleur ami (et elle l'est toujours aujourd'hui).

Vous pouvez essayer toute votre logique JavaScript, vos extraits de code et vos idées de code directement dans la console. Cela fonctionne à merveille lorsque vous souhaitez essayer des preuves de concept de votre logique dans la console avant de mettre le code dans l'application.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-83.png)
_Programme JavaScript dans la console du navigateur_

Vous pouvez lancer les DevTools (pour Chrome, et disponibles dans d'autres navigateurs également) en utilisant la touche `F12` de votre navigateur préféré. Ensuite, vous pouvez naviguer vers l'onglet `console` pour commencer à écrire et à expérimenter avec le code.

## Cela dit, c'est pour la logique JavaScript...

La console du navigateur est un excellent moyen d'essayer la partie logique, mais elle n'est pas suffisante pour construire et tester une application web en cours de route.

Si vous commencez avec un framework ou une bibliothèque populaire comme `Angular`, `React`, `Vue` ou `Svelte`, ils vous couvrent. Vous aurez une infrastructure complète pour développer, tester, exécuter et voir les changements presque en temps réel.

Cependant, supposons que vous réalisiez un projet avec du JavaScript simple, HTML5 et CSS (j'adore cette combinaison). Dans ce cas, vous n'aurez peut-être pas besoin d'une infrastructure particulière.

Voici quelques options pour vous lancer.

### VS Code + Live Server ou tout équivalent

Supposons que vous utilisiez Visual Studio Code comme éditeur/IDE préféré pour le développement web. Dans ce cas, vous pouvez installer une extension appelée `Live Server`. Elle lance un serveur de développement local avec une fonctionnalité de rechargement en direct pour les pages statiques et dynamiques.

%[https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer]

Une fois installée, vous pouvez faire un clic droit sur le fichier HTML d'entrée (généralement un fichier `index.html`) de l'application et l'ouvrir avec Live Server.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-85.png)
_Lancer l'application en utilisant Live Server_

Alternativement, vous pouvez essayer l'option `Go Live` depuis la barre d'état de VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-86.png)
_Autre façon de lancer Go Live_

Ce flux de travail fonctionne vraiment bien pour développer et tester votre application web de manière incrémentielle. Il fournit un rechargement à chaud, donc vous n'avez pas besoin de rafraîchir le navigateur pour voir les dernières modifications. Cela se fait automatiquement.

Au cas où vous n'utiliseriez pas VS Code, il pourrait y avoir d'autres alternatives pour votre IDE préféré.

### Avec la commande npx serve

`npx` signifie Node Package Execute. Il vient avec `npm` pour exécuter n'importe quel package que vous souhaitez depuis le registre npm sans l'installer localement. [serve](https://www.npmjs.com/package/serve) est un utilitaire pour vous aider à servir un site statique, une application monopage localement.

Pour l'utiliser, ouvrez une invite de commande à la racine du dossier du projet et tapez ceci :

```shell
npx serve
```

Vous obtiendrez une URL pour accéder à l'application localement.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-84.png)
_Utilisation de npx serve_

Ces deux méthodologies sont très utiles pour exécuter et tester l'application `localement`. Mais vous pourriez avoir besoin d'un flux de travail un peu plus sophistiqué pour construire et déployer l'application afin de tester la version de production simultanément.

## Un flux de travail plus sophistiqué

La dernière chose que vous souhaitez, c'est que votre application ne se comporte pas de la même manière en production qu'en local. Cela pourrait être un cauchemar si vous le découvrez près de la date limite.

Une meilleure approche serait de développer des fonctionnalités, de les tester localement, puis de les déployer et de les prévisualiser sur une infrastructure de type production. Si tout se passe bien, vous pouvez alors les lancer en production. Vous pouvez faire tout cela de manière entièrement automatisée en quelques minutes.

J'ai commencé à suivre un flux de travail qui m'aide à accomplir ces tâches :

%[https://twitter.com/tapasadhikary/status/1451041822285783040]

Certains services d'hébergement basés sur le cloud fantastiques sont disponibles pour vous aider à éliminer de nombreuses complexités liées à la construction, au déploiement et à l'hébergement de vos applications web. En voici quelques-uns que vous pouvez consulter (mes préférés sont Vercel et Netlify) :

* [Heroku](https://heroku.com/)
* [Netlify](https://netlify.com/)
* [Vercel](https://vercel.com/)
* [Surge](https://surge.sh/)
* [Firebase](https://firebase.com/)
* [Fly](https://fly.io/)

Il est courant de gérer et de suivre les modifications de votre code source à l'aide d'un système de contrôle de version comme Git et une application comme GitHub. Si vous n'avez pas de compte sur [GitHub](http://github.com/), vous pouvez en créer un maintenant.

Si vous cherchez un guide pour les dépôts GitHub afin d'augmenter l'engagement sur vos dépôts publics, vous pouvez lire cet article que j'ai écrit :

%[https://www.freecodecamp.org/news/increase-engagement-on-your-public-github-repositories/]

Très bien, revenons à notre sujet. Les services d'hébergement mentionnés ci-dessus ont des intégrations avec GitHub. Cela signifie que vous pouvez connecter un dépôt particulier dans GitHub pour construire le code source à partir de celui-ci et le déployer sur un CDN par les services d'hébergement.

Le meilleur, c'est que tout cela se fait automatiquement chaque fois que vous poussez vos commits vers une branche de dépôt. Pour chaque pull request, vous obtenez une URL de prévisualisation pour tester vos modifications dans une infrastructure de type production. N'est-ce pas génial ?

Une fois que vous êtes satisfait des tests, vous fusionnez simplement la pull request vers la branche master (ou main) pour construire et déployer votre application/site à partir de là.

Alors, à quoi ressemble le flux de travail à un niveau élevé ? Jetez un coup d'œil à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/workflow-1.png)
_Un flux de travail automatisé_

* En tant que développeurs, nous créons un dépôt GitHub pour notre code source et committons, poussons le code initial vers celui-ci.
* Nous effectuons quelques étapes simples avec le fournisseur d'hébergement (comme Vercel, Netlify) pour intégrer le dépôt GitHub.
* Ensuite, nous créons des branches dans le dépôt pour implémenter des fonctionnalités ou corriger des bugs. Netlify, Vercel ou d'autres services créeront une version déployable, la déployeront sur un CDN et nous fourniront une URL de prévisualisation pour chaque branche.
* Nous utilisons ensuite cette URL pour tester la fonctionnalité. Nous pouvons également partager cette URL publiquement avec nos parties prenantes.
* Une fois que nous avons terminé, nous fusionnons la PR, et les modifications dans la branche master ou main sont également construites et déployées automatiquement.

Ce flux de travail m'aide le plus avec mon développement web. Je me concentre simplement sur la livraison de mes modifications de code à GitHub, et le reste se fait automatiquement.

Passons maintenant aux étapes rapides de déploiement d'une application web simple sur Vercel. C'est assez similaire aux autres plateformes que je vous laisse explorer.

### Comment déployer une application web sur Vercel

* Inscrivez-vous avec [Vercel](https://vercel.com/) et connectez-vous. Ensuite, cliquez sur le bouton `New Project` :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-95.png)
_Sélectionner un nouveau projet_

* Ensuite, configurez et importez un dépôt GitHub :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-96.png)
_Configurer le dépôt GitHub_

* Maintenant, installez Vercel sur votre organisation GitHub où ce dépôt existe.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-97.png)
_Installer Vercel sur GitHub_

* Vous devrez fournir l'accès à tous les dépôts ou sélectionner ceux que vous souhaitez que Vercel gère. Ensuite, sauvegardez les modifications.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-98.png)
_Sélectionner le dépôt_

* Maintenant, le contrôle revient à l'interface de Vercel et vous pouvez importer le dépôt à partir de là.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-99.png)
_Importer le dépôt sélectionné pour le déploiement_

* Vous pouvez sélectionner le point d'entrée du répertoire racine du projet et déployer.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-100.png)
_Une configuration de base_

* Le déploiement peut prendre un certain temps en fonction du type de votre projet web. Une fois terminé, vous obtiendrez un écran comme ci-dessous pour le confirmer.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-101.png)
_Terminé !_

Super, j'espère que c'était facile. Veuillez explorer davantage, et je suis sûr que vous allez adorer.

## Avant de terminer...

J'espère que vous avez trouvé l'article perspicace et informatif. Mes DM sont ouverts sur Twitter si vous souhaitez discuter davantage.

Restons en contact. Je partage mes apprentissages sur JavaScript, le développement web et le blogging sur ces plateformes également :

* [Suivez-moi sur Twitter](https://twitter.com/tapasadhikary)
* [Abonnez-vous à ma chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1)
* [Projets secondaires sur GitHub](https://github.com/atapas)