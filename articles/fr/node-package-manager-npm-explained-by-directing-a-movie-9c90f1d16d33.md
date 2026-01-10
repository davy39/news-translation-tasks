---
title: Node Package Manager (NPM) expliqué en dirigeant un film
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-24T01:45:53.000Z'
originalURL: https://freecodecamp.org/news/node-package-manager-npm-explained-by-directing-a-movie-9c90f1d16d33
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Sqqu9cwZB7zXj00ULQ5Eg.jpeg
tags:
- name: education
  slug: education
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Node Package Manager (NPM) expliqué en dirigeant un film
seo_desc: 'By Kevin Kononenko

  If you understand the general way that Hollywood movies are made, then you can understand
  Node Package Manager (NPM).

  Did you know that the initial version of Node.js was written by just one programmer,
  Ryan Dahl, in 2009?

  Today, i...'
---

Par Kevin Kononenko

**Si vous comprenez la manière générale dont les films hollywoodiens sont réalisés, alors vous pouvez comprendre Node Package Manager (NPM).**

Saviez-vous que la version initiale de Node.js a été écrite par un seul programmeur, Ryan Dahl, en 2009 ?

Aujourd'hui, en 2018, des millions de développeurs ont utilisé Node.js pour créer le back-end de leurs applications web. Mais Node s'est appuyé sur une communauté open-source active pour développer de nombreux packages spécialisés dans le Node Package Manager, ou NPM.

Il y a deux raisons pour lesquelles Ryan Dahl n'a pas développé toutes ces fonctions spécialisées lui-même :

1. Les développeurs ne voudraient pas utiliser un framework massif et encombrant écrit pour couvrir des centaines de cas d'utilisation.
2. Cela prendrait trop de temps pour créer tous les packages spécialisés vous-même.

Au lieu de cela, Ryan savait que si Node devenait populaire, les développeurs seraient prêts à contribuer. Il a donc lancé NPM en 2010 pour organiser tous ces packages créés par la communauté.

Cependant, en tant que développeur web débutant, il peut être difficile de comprendre tout cet écosystème et comment y accéder sur votre ordinateur local.

Après y avoir réfléchi un moment, j'ai réalisé que l'utilisation de NPM ressemble un peu à être le réalisateur d'un film hollywoodien. C'est à vous de jongler avec un groupe de personnes (ou de packages) ayant des fonctions spécialisées sans rendre tout le monde fou (ou rendre impossible la construction de votre application).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_h-Af2amJ-W_85YYY.jpeg)

Voici donc le guide complet de NPM. Pour comprendre ce tutoriel, vous devez simplement connaître [la différence entre front-end et back-end](https://blog.codeanalogies.com/2018/04/07/front-end-v-back-end-explained-by-waiting-tables-at-a-restaurant/).

# Qu'est-ce que NPM ?

Imaginez que vous êtes le réalisateur d'un nouveau film hollywoodien. Après avoir accepté le rôle, vous devez immédiatement commencer à engager des acteurs et d'autres exécutifs pour créer le film avec vous.

Bien sûr, cela soulève la question immédiate : quels acteurs/actrices allez-vous engager ? Comment allez-vous vous assurer qu'ils peuvent tous travailler ensemble ? Comment allez-vous respecter le budget ?

Ou bien, allez-vous prendre une direction complètement différente et essayer de construire l'équipe parfaite à partir de zéro avec des acteurs relativement inconnus ?

Si vous voulez engager une équipe, vous devrez consulter un type de répertoire pour trouver les bonnes personnes. Je ne sais pas si Hollywood a un répertoire interne, mais [IMDB](http://imdb.com/) en est un qui vient à l'esprit. Ou, dans le temps, avant Internet, il y avait probablement même un répertoire physique.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_OfNzoFOA9Scop-hQ.png)

Tout comme IMDB contient des informations sur des milliers d'acteurs que vous pouvez utiliser pour prendre une décision d'embauche, NPM contient des centaines de milliers de "packages" qui offrent des fonctions spécialisées. Ils sont tous écrits en JavaScript, donc TECHNIQUEMENT vous pourriez les réécrire... mais ce n'est pas le but. Ils sont censés faciliter votre vie en rendant de nouvelles fonctionnalités instantanément disponibles.

C'est un peu comme engager un acteur/actrice connu(e) — cette personne est spécialiste de certains types de rôles grâce à son expérience passée.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_gYvhN0Ws1rlLL6uo.jpeg)

_Nous connaissons tous la spécialité de Liam Neeson…_

Ainsi, en tant que développeur, vous accédez au registre NPM pour ajouter des packages spécifiques à votre application web, ce qui devrait faciliter votre vie. Et tout comme tous les acteurs/actrices ont construit leur propre carrière, tous les packages NPM ont été construits par des développeurs individuels ou des équipes et contribués au registre.

Dans votre code, tous ces packages sont suivis dans le fichier package.json. Ce fichier est donc un peu comme la liste des personnes impliquées dans le film. Voici un exemple de cette liste :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_94FQCRZXv3NGz2W8.png)

Nous aborderons les versions plus tard dans ce tutoriel.

# Explication des packages

Imaginons que votre film a 100 rôles à pourvoir. Si vous aviez un budget illimité, voudriez-vous pourvoir tous ces rôles avec des acteurs/actrices célèbres ayant joué des rôles similaires par le passé ?

Probablement pas.

Tout le monde voudrait être la star du spectacle et plier les règles pour s'adapter à son personnage. Ce serait un cauchemar. Mais si vous n'engagez que des acteurs inconnus, il sera assez difficile de réaliser un excellent film !

Il faut des années d'expérience pour devenir un grand acteur, après tout.

De même, lorsque vous construisez une application web, vous êtes constamment confronté à un choix — puis-je développer cette fonctionnalité moi-même, ou devrais-je utiliser un package pour accomplir la tâche ?

Connaissez-vous le film « [Super Troopers](https://en.wikipedia.org/wiki/Super_Troopers) » ? C'est un classique de la comédie, et le budget était de seulement 3 millions de dollars. Cependant, la plupart des excellents films coûtent entre 10 et 100 millions de dollars. Vous pouvez construire une application web incroyable à partir de zéro, mais vous voulez probablement utiliser des packages.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_H1HOGMdz6Swfae3H.jpeg)

Supposons que vous engagiez Mark Wahlberg, un acteur américain célèbre, pour votre film. Lorsque Mark rejoint votre film, ce n'est pas seulement lui. Il a une équipe de personnes qui le soutiennent et le rendent successful. Un chef, un entraîneur, un agent.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_si4-ybeeHo_o6Sx1.png)

De même, chaque package individuel ne fonctionne pas indépendamment. Les auteurs de packages ont utilisé d'autres packages NPM pour faciliter leur vie également. En fait, leur package partagera certaines dépendances avec d'autres packages, tout comme Mark Wahlberg pourrait partager un chef privé avec d'autres acteurs et actrices.

Voici la liste des dépendances pour [request](https://www.npmjs.com/package/request), un package populaire :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_aX2XcgXqhvH898m5.png)

Revenons donc à notre exemple de package.json ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_yzyTg-PLBa-Dyxsa.png)

Lorsque vous ajoutez le package « axios » à votre application, vous n'ajoutez pas seulement le fichier axios. Vous ajoutez également toutes les dépendances dont le fichier axios aura besoin, si vous ne les avez pas déjà ajoutées avec un autre package. Celles-ci ne sont pas explicitement indiquées, mais vous pouvez toujours les trouver dans le dossier node_modules.

C'est l'un des avantages de npm. Lorsque vous ajoutez un nouveau package, vous n'avez même pas besoin de vérifier si vous utilisez déjà tous les packages nécessaires qui supportent le package que vous utilisez. npm ajoutera automatiquement les nouveaux à votre répertoire.

# Explication des versions

Voyez-vous les trois séries de chiffres à côté de chaque package ci-dessus ? C'est le **numéro de version**. Comme les développeurs mettent constamment à jour leurs packages, vous pouvez choisir d'utiliser une version spécifique d'un package ou d'utiliser automatiquement la dernière version.

Ainsi, lorsque vous utilisez 40 packages différents dans votre projet, et qu'ils évoluent constamment, vous pouvez constater que des problèmes de compatibilité surviennent. Par exemple, lorsque ReactJS publie sa nouvelle version, votre application peut ne plus fonctionner comme vous l'attendez. C'est là que les tests entrent en jeu, mais c'est le sujet d'un autre tutoriel.

Pensez-y comme des acteurs/actrices à différentes étapes de leur carrière. Certains peuvent jouer des rôles similaires tout au long de leur carrière, tandis que d'autres peuvent changer radicalement.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_JZullYOFh6dTh7hd.jpeg)

_Jeune vs vieux Clint Eastwood_

# Utilisation de la ligne de commande

Lorsque vous téléchargez Node et NPM sur votre machine locale, vous pouvez instantanément utiliser une variété de commandes pour travailler avec le répertoire NPM. Une commande courante est :

_npm install_

Si vous souhaitez installer le package express, vous taperiez dans la ligne de commande :

_npm install express_

Ensuite, NPM téléchargerait le code express et ses dépendances sur votre ordinateur local. C'est un peu comme l'acte d'engager un nouvel acteur. Ou bien —

_npm uninstall express_

C'est comme « licencier » le package express de votre application.

Vous pouvez ajouter de nouvelles commandes dans la section « scripts » de votre fichier package.json. Une commande courante est « start », qui signifie « commencer à exécuter le serveur node ». Cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_Z9ZoMm3vSFGk-Mud.png)

Un peu comme un réalisateur criant « Action ! »

# Explication des dépendances

Jusqu'à présent, nous n'avons fait qu'effleurer le concept de dépendances. Votre application aura probablement quelques packages qui ne s'exécutent que sur la version locale, comme les outils de test et de transpilation. En d'autres termes, vous devriez avoir quelques outils que vous n'utilisez que dans votre environnement local, et non sur la version de production.

Si vous avez besoin d'un rappel sur la différence entre localhost et production, [consultez ce guide](https://blog.codeanalogies.com/2018/02/02/localhost-explained-by-trying-to-start-a-microbrewery/).

Pensez à tout le temps et l'énergie qui vont dans la réalisation d'un film. Seule une petite fraction de celui-ci se produit sur le plateau officiel avec les caméras en marche. Derrière la scène, il y a des heures de travail sur la mémorisation des lignes, la musculation à la salle de sport et l'apprentissage de nouveaux accents. Pour rendre l'équipe plus efficace, le réalisateur pourrait engager des entraîneurs spécialisés pour chacune de ces fonctions.

Ainsi, lorsque nous regardons tous les packages utilisés par une application Node, nous pouvons en fait les diviser en deux catégories :

1. Packages utilisés à la fois en production et en local
2. Packages utilisés uniquement en local

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0__kdSnu3_r0xpRRtu.png)

[Grunt](https://gruntjs.com/) est un exécuteur de tâches qui automatise les commandes répétitives sur la ligne de commande. [Nodemon](https://github.com/remy/nodemon) redémarre automatiquement votre serveur lors de tout changement dans votre code serveur.

Dans votre fichier package.json, ceux-ci sont séparés en deux sections : dependencies et devDependencies. Voici à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_tu-qbY_hG7z-qKzl.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_z4Y9LhCYX96HPGYL.png)