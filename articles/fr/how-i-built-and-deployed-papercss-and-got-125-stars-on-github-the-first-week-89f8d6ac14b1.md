---
title: Comment j'ai construit et déployé PaperCSS — et obtenu 125+ étoiles sur GitHub
  la première semaine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-19T09:54:55.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-and-deployed-papercss-and-got-125-stars-on-github-the-first-week-89f8d6ac14b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mxL8G7PSiKvz4-PN2CKN7A.png
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit et déployé PaperCSS — et obtenu 125+ étoiles sur
  GitHub la première semaine
seo_desc: 'By Rhyne Vlaservich

  Background

  I had just finished up a summer internship in New York working as a software engineer.
  During my exit interview, I asked for some feedback about any areas where I could
  improve. Since I’m very interested in a career in ...'
---

Par Rhyne Vlaservich

#### Contexte

Je venais de terminer un stage d'été à New York en tant qu'ingénieur logiciel. Lors de mon entretien de départ, j'ai demandé des retours sur les domaines où je pourrais m'améliorer. Comme je m'intéresse beaucoup à une carrière dans le développement web front-end, le principal enseignement que j'ai tiré de cette conversation était de mieux maîtriser CSS.

J'ai décidé que la meilleure façon d'apprendre CSS (et comment le construire avec [LESS](http://lesscss.org/)) était de créer mon propre framework CSS. Au lieu d'utiliser aveuglément [Bootstrap](http://getbootstrap.com/), je voulais comprendre pleinement tout ce qui se cache derrière. En bonus, ce framework CSS pourrait servir de base à tous mes futurs projets.

![Image](https://cdn-media-1.freecodecamp.org/images/cu32-J1e6RXBGNwtKKl2rv0ywDZv994a40g2)

Je savais maintenant que je voulais construire un framework CSS, mais je n'avais pas beaucoup de direction jusqu'à ce que je tombe sur [les boutons imparfaits de Tiffany Rayside sur Codepen](https://codepen.io/tmrDevelops/pen/VeRvKX). J'ai adoré le fait que les bordures n'étaient pas droites et que c'était, eh bien, imparfait. J'ai pensé que ce concept serait vraiment cool s'il était appliqué à tous les autres types d'éléments HTML. Et ainsi est né PaperCSS.

#### Construction de PaperCSS

J'ai passé les semaines suivantes à construire les classes pour le framework. J'ai commencé par le Flexgrid, car je voulais vraiment en apprendre davantage sur la façon dont flexbox peut être utilisé et appliqué. Je savais aussi que ce serait utile d'avoir un système de positionnement des éléments pour le site de documentation. J'ai ensuite ajouté plus de fonctionnalités et de styles au fur et à mesure que j'avais du temps.

![Image](https://cdn-media-1.freecodecamp.org/images/shjuneClw3a35ebAr1DF4LPsJpcy-Z57QAwp)
_Exemple de fonctionnalité, les bordures !_

J'ai passé du temps à apprendre [Gulp](https://gulpjs.com/) pour automatiser la construction du CSS. Tout ce que je devais faire était d'ajouter des styles dans un fichier .less et de laisser Gulp construire le CSS pour moi. Je pouvais ensuite le visualiser instantanément sur le site de documentation/démonstration. J'ai utilisé le module [gulp-watch-less](https://www.npmjs.com/package/gulp-watch-less) pour ne même pas avoir à recharger le site pour voir les changements.

C'était amusant d'apprendre comment fonctionne Gulp et de jouer avec tous les différents modules qui existent pour lui. On a l'impression qu'il y a un package Gulp pour tout ce dont vous avez besoin.

Dans l'ensemble, la construction de ce framework a été assez simple. Je voulais le garder aussi simple que possible pour que les gens puissent contribuer plus facilement. Mais j'y reviendrai plus tard.

#### Déploiement de PaperCSS

J'ai fini par déployer le framework sur [Netlify](https://www.netlify.com/). Tout ce que vous avez à faire est de connecter votre dépôt Git, votre commande de construction et votre nom de domaine (si vous en avez un). Ils vous permettent même d'ajouter https en seulement deux clics. J'adore leur service (et je ne suis pas payé pour le dire).

À partir de là, toute poussée vers votre branche master déclenche automatiquement une reconstruction et un redéploiement de votre site.

![Image](https://cdn-media-1.freecodecamp.org/images/UB-6KDtt0N3buA5Kf-dosuAWcjN2LK0cN8Vj)
_Une autre fonctionnalité, les boutons radio et les cases personnalisés_

Honêtement, la partie la plus difficile (jusqu'à présent) de ce déploiement a été de choisir le nom de domaine. papercss.com était déjà pris, donc j'ai dû faire preuve de créativité. J'ai fini par choisir getpapercss.com, puisque d'autres frameworks ont mis « get » avant leur nom réel (ahem, Bootstrap). D'autres options que j'aimais étaient papercss.style et papercss.org.

#### Lancement de PaperCSS

Après avoir obtenu des retours de la part d'amis et d'anciens collègues, j'ai décidé de partager PaperCSS sur Internet. Je l'ai posté sur [Hacker News](https://news.ycombinator.com/item?id=15584262) et [r/web_design](https://www.reddit.com/r/web_design/comments/79n3qh/papercss_the_less_formal_css_framework/). J'avais créé ce framework pour les développeurs web, donc je pensais que ces deux audiences seraient idéales.

J'ai fait quelques recherches rapides et j'ai découvert que le meilleur moment pour poster sur Reddit était [le dimanche et le lundi matin](http://maxcandocia.com/article/2017/Jul/29/what-time-to-post-to-reddit/). Comme mes recherches Google ont eu lieu un dimanche soir, j'ai choisi de poster sur ces deux canaux le lundi matin.

Hacker News a obtenu un peu de traction et de très bons retours dans les commentaires.

![Image](https://cdn-media-1.freecodecamp.org/images/1yEXAikrgOGFGVGz-VJskC8PBkf7wuXlKMnO)
_[Soumission Hacker News](https://news.ycombinator.com/item?id=15584262" rel="noopener" target="_blank" title=")_

Mais c'est **vraiment** décollé sur Reddit. Normalement, lorsque je lance une petite application ou une extension Chrome, j'obtiens trois votes positifs et peut-être un commentaire disant « meh ». Mais PaperCSS a somehow atteint le sommet de r/web_design et est resté dans la position du post le plus populaire pendant près de deux jours.

![Image](https://cdn-media-1.freecodecamp.org/images/WAwNPDt7HKubLBJyD04aQ1-P-gxAbDCoryqE)
_[Soumission r/web_design](https://www.reddit.com/r/web_design/comments/79n3qh/papercss_the_less_formal_css_framework/" rel="noopener" target="_blank" title=") après le jour 1_

Mais la meilleure partie du lancement a été l'intérêt immédiat pour contribuer. Il y avait trois pull requests au moment où j'ai ouvert mon email cet après-midi-là !

J'ai soudainement ressenti un sentiment de responsabilité. Ce n'était plus un projet aléatoire que je pouvais oublier et laisser derrière moi. Les gens étaient suffisamment intéressés pour vouloir l'améliorer. J'ai eu l'impression que je leur devais, ainsi qu'à tous ceux qui utilisent PaperCSS, de m'assurer que leurs contributions étaient incluses. Le projet doit vivre !

#### La première semaine

Voici un bref résumé de la première semaine de PaperCSS :

* 500+ nouvelles lignes de code
* 125+ étoiles sur GitHub
* 13 problèmes
* 12 pull requests
* 6 nouvelles fonctionnalités (infobulles, cartes, alertes, badges, styles de bordure, boutons désactivés)
* Et une richesse de soutien et de retours !

![Image](https://cdn-media-1.freecodecamp.org/images/3s2IP155-gYnJov1tOBxeDP2WfZq4SMfVhvw)
_Nouvelle fonctionnalité d'alertes_

Voulez-vous savoir la partie la plus folle de toute cette histoire ? Je n'ai personnellement ajouté aucune de ces nouvelles fonctionnalités. Cela a été une semaine chargée, donc j'ai simplement passé mon temps avec PaperCSS à commenter les problèmes et les pull requests et à les fusionner tous.

C'est très étrange d'être de l'autre côté de la pull request. Merci à **TotomInc**, **Fraham** et **joelwallis** pour leurs contributions jusqu'à présent ! Et merci à tous les autres pour les retours sur Hacker News, Reddit et via les problèmes sur GitHub.

#### L'avenir de PaperCSS

L'avenir de ce projet dépend de là où tout le monde veut l'emmener. J'adore la petite communauté qui s'est formée autour, et je veux que ce soit un framework qui grandit organiquement. J'adorerais continuer à ajouter des fonctionnalités, nettoyer la base de code et en faire un projet simple auquel il est facile de contribuer.

Quelques points concrets que je veux vraiment régler dès que possible :

* Mettre PaperCSS sur un CDN. Ainsi, les utilisateurs n'auront pas besoin de le télécharger — il pourra simplement être lié externement.
* Mettre PaperCSS sur NPM pour un facile `npm install`
* Trouver la meilleure façon de s'assurer que la documentation correspond à la dernière version
* Ajouter des pages d'exemples
* Diviser le fichier index.html monolithique en morceaux plus petits, tout en le gardant simple à comprendre et à contribuer.

En parlant de ce dernier point : beaucoup de projets sur GitHub sont intimidants à configurer localement — mais PaperCSS ne l'est pas. Il est relativement facile à comprendre et à ajouter des fonctionnalités, puisque les seules parties mobiles sont les fichiers .less et le fichier index.html. J'aimerais continuer à le garder simple et maintenir la barrière à l'entrée (pour contribuer) basse.

Pour toute personne qui veut commencer avec un projet open source, ce serait un excellent endroit pour le faire. Si vous n'avez jamais ouvert de pull request auparavant, je serais ravi de vous guider à travers ce processus.

#### Conclusion

Pour résumer, cela a été une semaine folle. PaperCSS a dépassé mes attentes de 1 000 % et je suis ravi de la façon dont il se développe. J'apprends encore beaucoup sur la façon de gérer le framework et les contributions, et j'apprécierais tout conseil à ce sujet. De plus, veuillez envisager d'utiliser PaperCSS pour votre prochain projet et envoyez-moi un lien avec le résultat :)

![Image](https://cdn-media-1.freecodecamp.org/images/gHe1ZHOCfGNzFeuhVmHtOWFFz9Y7GyPG5-nn)

![Image](https://cdn-media-1.freecodecamp.org/images/z1CusRkCJOcb0DhPrR1656oj46kBR8V9Qh0O)

![Image](https://cdn-media-1.freecodecamp.org/images/Cq6oayKGNMVYGGJhE7Gu65S9WvM9dlirNMZ8)