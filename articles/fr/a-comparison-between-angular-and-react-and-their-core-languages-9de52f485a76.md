---
title: Une comparaison entre Angular et React et leurs langages principaux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T22:47:25.000Z'
originalURL: https://freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2FNo1Wxk0kZX0QoH.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Une comparaison entre Angular et React et leurs langages principaux
seo_desc: 'By Dler Ari

  In this article, we will compare two of the most popular web technologies in 2019,
  and also address their history, key differences, core languages recommended (TypeScript
  and JavaScript) and so forth. Overall, these technologies have made...'
---

Par Dler Ari

Dans cet article, nous allons comparer deux des technologies web les plus populaires en 2019, et aborder également leur histoire, leurs différences clés, les langages principaux recommandés (TypeScript et JavaScript) et ainsi de suite. Globalement, ces technologies ont grandement facilité la tâche des développeurs pour réutiliser, refactoriser et maintenir le code en divisant les choses en modules/composants.

Le but de cet article n'est pas de trouver la meilleure technologie, mais de comparer, de mettre en lumière et de clarifier quelques idées reçues. Nous nous concentrerons également sur ce qui est important plutôt que sur des détails mineurs qui n'ont pas vraiment d'importance à long terme.

Vous devez être conscient que la comparaison entre ces deux technologies ne peut pas être entièrement couverte. Angular est un framework complet (MVC), tandis que React est une bibliothèque frontale avec de nombreux packages open-source à intégrer.

> Si vous souhaitez devenir un meilleur développeur web, créer votre propre entreprise, enseigner aux autres ou simplement améliorer vos compétences en développement, abonnez-vous à ma newsletter pour obtenir les dernières nouvelles et mises à jour du web.

### Questions à aborder

* Quelles sont les différences clés entre Angular et React ?
* Qu'est-ce qui rend TypeScript si spécial ?
* À quel point ces technologies sont-elles populaires ?
* Quel est l'état actuel de l'open-source ?
* Quelle technologie les entreprises utilisent-elles le plus ?
* Les langages à typage statique influencent-ils la qualité du code et le temps de développement ?

Les sections futures seront ajoutées en fonction de la demande dans les commentaires.

### Comparaisons clés

Voici une comparaison rapide entre Angular (à gauche) et React (à droite).

![Image](https://cdn-media-1.freecodecamp.org/images/1*w9DLq-pSxDGabNxUzawN_w.png)
_Angular et React_

Une chose vraiment géniale à propos de React en termes de performance est le Virtual DOM, dont vous avez probablement entendu parler plusieurs fois. Si ce n'est pas le cas, ne vous inquiétez pas, je vais l'expliquer !

**Problème**  
Supposons que vous souhaitiez mettre à jour la date de naissance d'un utilisateur dans un bloc de balises HTML.

**Virtual DOM**  
Il ne met à jour que la partie nécessaire en voyant les différences entre les versions HTML précédente et actuelle. C'est une approche similaire à la manière dont GitHub fonctionne lorsqu'il détecte des changements dans le fichier.

**Regular DOM**  
Il mettra à jour toute la structure arborescente des balises HTML jusqu'à atteindre la date de naissance.

#### Pourquoi est-ce important ?

Cela peut ne pas être important pour le problème décrit ci-dessus. Cependant, si nous traitons 20 à 30 requêtes de données asynchrones sur la même page (et pour chaque requête de page, nous remplaçons tout le bloc HTML), cela influencera les performances ainsi que l'expérience utilisateur.

Besoin de plus de contexte ? Consultez l'article de [Dace](https://www.freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76/undefined) !

Mais d'abord, revenons au début...

### Histoire

Nous devons connaître un peu d'histoire (contexte) car cela donne un aperçu de la manière dont les choses pourraient se façonner à l'avenir.

> _Je ne vais pas entrer dans les détails de ce qui s'est exactement passé entre Angular et AngularJS, et je suis sûr qu'il existe de nombreuses ressources disponibles qui [le couvrent](https://www.angularjswiki.com/angularjs/history-of-angularjs/). Mais en bref, Google a remplacé AngularJS par Angular, et JavaScript par TypeScript._

D'accord, donc à l'époque avec ES4/ES5, la courbe d'apprentissage pour JavaScript était vraiment élevée. Si vous veniez du monde de Java, C# ou C++, un monde de programmation orientée objet (POO), alors apprendre JavaScript n'était tout simplement pas très intuitif. En d'autres termes, c'était une vraie galère.

Ce n'est pas parce que le langage était mal écrit, mais parce qu'il a un but différent. Il a été conçu pour gérer la nature asynchrone du web, telle que l'interaction utilisateur, la liaison d'événements, les transitions/animations, et ainsi de suite. C'est un animal différent avec des instincts différents.

### Popularité

Comme le révèle Google Trends, Angular et React sont deux des technologies web les plus populaires en 2019.

Angular a plus de recherches que React, cependant, cela ne signifie pas nécessairement qu'un est meilleur que l'autre. Mais cela indique ce que les gens trouvent intéressant, quelle qu'en soit la raison. Il est important de savoir que les gens peuvent confondre les mots-clés tels que AngularJS ou Angular, ce qui conduit à un plus grand nombre de recherches.

Une chose est sûre — les deux technologies sont en croissance, et l'avenir semble prometteur. Cela signifie que vous n'avez pas à vous inquiéter si une technologie va échouer et vous laisser derrière.

Il est important de ne pas négliger l'histoire en termes de ce qui s'est passé entre AngularJS et Angular, car l'histoire est une forme d'indication de ce qui peut se passer à l'avenir. Mais si vous avez une certaine expérience avec Angular et AngularJS, alors vous verrez probablement pourquoi les décisions ont été prises pour le mieux. Juste pour mentionner, de telles choses peuvent arriver à n'importe quel framework, y compris React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QHPY_nB9Gvx0pNNPtPqUiQ.png)
_Google Trends Angular vs React_

#### Open-source

React a plus de 100 000 étoiles, ainsi que 1200 contributeurs et près de 300 problèmes en attente de résolution.

React a un avantage en termes de temps de mise sur le marché, puisqu'il a été publié 3 ans avant Angular. Et cela signifie qu'il a été confronté à de nombreux problèmes réels, a subi des tests critiques et s'est globalement développé en une bibliothèque frontale adaptable et flexible que beaucoup aiment.

En ce qui concerne Angular, à première vue, nous pouvons clairement voir qu'Angular a 6 fois plus de problèmes que React (ce qui n'est pas bon). Cependant, nous ne devons pas oublier qu'Angular est un framework beaucoup plus grand, et a également moins de développeurs qui l'utilisent (actuellement) car il a été publié en 2016.

![Image](https://cdn-media-1.freecodecamp.org/images/1*peSbHEIzoh41XzjjEcyaOQ.png)
_Angular et React — Popularité sur GitHub_

> Statistiques prises des pages GitHub d'[Angular](https://github.com/angular/angular) et de [React](https://github.com/facebook/react).

### Quelles entreprises utilisent ces technologies

React a été initialement développé chez Facebook pour Facebook afin d'optimiser et de faciliter le développement de composants. Un article écrit par [Chris Cordle](https://www.freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76/undefined) souligne que React a une utilisation plus élevée chez Facebook que Angular chez Google.

Alors, qui utilise quelle technologie ?

#### [# React](https://github.com/facebook/react/wiki/Sites-Using-React)

* Facebook
* AirBnb
* Uber
* Netflix
* Instagram
* Whatsapp
* Dropbox

#### [# Angular](https://www.madewithangular.com/categories/angular)

* Eat24
* CVS shop
* onefootball
* Google Express
* NBA
* Delta
* wix.com

> _Si vous connaissez des entreprises (bien connues) utilisant Angular, veuillez les partager avec un lien._

### TypeScript et JavaScript (ES6+)

Comme je l'ai mentionné, il peut être trompeur de comparer uniquement Angular et React sans se concentrer sur le langage principal que chacun met en avant (selon leur documentation).

> Note ! Le but de cette section n'est pas de décider si nous allons choisir Angular ou React. Mais de clarifier quelques idées reçues entre les langages à typage statique et dynamique qui existent depuis un certain temps, soutenues par des recherches.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VgrihKGD-D8TdfX1CTAB-A.png)
_TypeScript (à gauche) vs JavaScript (à droite)_

En termes de base d'utilisateurs, JavaScript est supérieur. Mais TypeScript est en augmentation rapide, alors qui sait ce que les 10 à 15 prochaines années nous réserveront.

#### Popularité de TypeScript au cours des 5 dernières années

![Image](https://cdn-media-1.freecodecamp.org/images/1*cRXezTFmwhdPEmXX7eMCQA.png)
_Google Trends — Popularité de TypeScript_

#### Popularité de JavaScript au cours des 5 dernières années

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ga66wSTNP6w1MT6JRbfYjA.png)
_Google Trends — Popularité de JavaScript_

#### Popularité de JavaScript vs TypeScript au cours des 5 dernières années

![Image](https://cdn-media-1.freecodecamp.org/images/1*axNBATWdEu5lNC9zcL2Fug.png)
_Google Trends — Popularité de TypeScript et JavaScript_

TypeScript a été initialement développé par Microsoft pour rendre JavaScript plus facile (en d'autres termes, pour rendre ES5 plus facile). Il a été publié en octobre 2012. Et il s'agit simplement d'un transpileur qui compile TypeScript en code JavaScript, ce qui signifie également que vous pouvez écrire du code ES5 dans un fichier TypeScript. TypeScript est considéré comme un sur-ensemble de JavaScript.

En général, TypeScript offre une transition en douceur pour les programmeurs ayant un passé en programmation orientée objet (POO). Il est important de noter que TypeScript a été publié à l'époque de ES5, et à cette époque, ES5 n'était pas un langage POO basé sur les classes.

En bref, la chose la plus proche que vous pouviez avoir des classes et des objets à l'époque était l'héritage par prototype. Et comme nous le savons, cela a été une transition difficile pour la plupart des développeurs ayant un passé en POO. Donc la décision idéale était bien sûr de choisir quelque chose avec lequel vous vous sentiez à l'aise et familier, ce qui était probablement TypeScript.

Cependant, ces dernières années, JavaScript a évolué et mis en œuvre de nombreux grands changements tels que les modules, les classes, les opérateurs de propagation, les fonctions fléchées, les littéraux de gabarit et ainsi de suite. Globalement, il permet aux développeurs d'écrire du code déclaratif, tout en supportant les caractéristiques d'un vrai langage POO (c'est-à-dire, incluant une structure basée sur les classes).

#### Langages à typage statique et dynamique

Un langage à typage statique signifie essentiellement que vous pouvez définir le type de variable (chaîne, nombre, tableau, etc.). Vous pouvez vous demander pourquoi cela est important. Voici une analogie du monde réel que j'ai mise en place (créativité à son meilleur).

Supposons que vous souhaitiez faire le plein de votre voiture avec de l'essence. Une chose importante est de faire le plein avec le bon carburant — essence ou diesel. Et si vous ne savez pas, vous devrez peut-être acheter une nouvelle voiture.

Bien sûr, la gravité n'est pas la même avec le codage, cependant, dans certains cas, elle peut l'être. Réfléchissez-y. Si vous travaillez avec une grande application, vous aimeriez connaître le type d'argument et de propriété qui est passé, sinon vous pourriez casser le code.

D'accord, donc si vous êtes toujours confus sur ce que signifie le typage statique, regardez ceci :

#### Propriété à typage statique

![Image](https://cdn-media-1.freecodecamp.org/images/1*mY3mIKr4VVX2Dfdd44klqA.png)
_Comparaison de propriété à typage statique entre JavaScript et TypeScript_

#### Argument à typage statique

![Image](https://cdn-media-1.freecodecamp.org/images/1*wp-KxiqHmsplvH9R9jf84g.png)
_Comparaison d'argument à typage statique entre JavaScript et TypeScript_

J'ai appris que beaucoup de gens croient qu'un langage à typage statique signifie un code fiable, et est le plus souvent utilisé comme un argument gagnant sur les langages à typage dynamique. Et franchement, il est assez difficile de réfuter cette affirmation car elle repose fondamentalement sur l'environnement de développement, l'expérience des programmeurs et bien sûr les exigences du projet.

Heureusement, une [recherche](https://courses.cs.washington.edu/courses/cse590n/10au/hanenberg-oopsla2010.pdf) (tl;dr [vidéo](https://vimeo.com/74354480)) a pris cela au sérieux et a mis ce mythe à l'épreuve avec 49 sujets.

#### Les observations de la recherche sont :

* Les langages à typage statique nécessitent plus de temps en raison de la correction des erreurs de frappe
* Les langages à typage dynamique sont lisibles et plus faciles à écrire (code déclaratif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*bshGBQgntp2lz78ZZENNLA.png)

La figure 5 montre que, en moyenne, les développeurs réduisent leur temps de développement d'un facteur de deux lorsqu'ils écrivent dans un langage à typage dynamique.

Si vous souhaitez approfondir ce sujet, je vous suggère de lire cet article d'[Eric Elliott](https://www.freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76/undefined) qui indique que vous n'avez peut-être pas besoin de TypeScript (ou de langages à typage statique).

#### Que choisir

Donc, la question n'est pas seulement de savoir ce qu'Angular ou React offre, mais aussi quel langage principal vous devriez investir du temps. Et cela n'a pas vraiment d'importance tant que vous choisissez quelque chose qui correspond à vos exigences et à votre complexité.

Si vous n'êtes pas un fan des types, alors il n'y a rien qui vous empêche d'écrire du code ES6 dans TypeScript. C'est juste que si vous en avez besoin, alors il est là.

Mais si vous construisez une application frontale assez grande avec Angular traitant de nombreuses requêtes HTTP, alors avoir des types aide vraiment avec des questions telles que « Quel type d'objet est-ce, quels champs puis-je utiliser, et quel type est ce champ, etc. ». C'est idéal pour la collaboration et pour clarifier les petites choses.

Voici une comparaison simple entre une classe-objet TS et JS (ES6).

![Image](https://cdn-media-1.freecodecamp.org/images/1*hlNk4pSA_NOAyUclRxAkFw.png)
_TypeScript_

![Image](https://cdn-media-1.freecodecamp.org/images/1*AqwhtWGVeDmOqf_J0_vCGg.png)
_JavaScript (ES6)_

#### Mon avis

Le typage statique semble structuré, sécurisé, lisible et facile à collaborer avec les autres (empêche les gens de passer des valeurs inattendues). Cependant, lorsque je travaille avec du typage dynamique, j'ai la flexibilité et la créativité de me concentrer davantage sur la création que de trop penser aux types, interfaces et génériques, etc.

Et d'après les applications web que j'ai construites dans le passé, je n'ai pas vraiment eu de gros problèmes à ne pas avoir de typage statique. Cela ne signifie pas que je ne l'aime pas — je n'en ai tout simplement pas besoin, mais peut-être que j'en aurai besoin à l'avenir.

Voici une mise à jour — actuellement, je travaille avec quelques développeurs Microsoft pour construire une application en utilisant le framework Angular. La raison pour laquelle nous avons sélectionné Angular est que la plupart des packages sont déjà définis, et la documentation pour tout est au même endroit. Il met également l'accent sur TypeScript, ce qui est un choix parfait car la majorité des développeurs ont déjà beaucoup d'expérience avec la programmation orientée objet.

D'un autre côté, j'ai vu des applications similaires à celles sur lesquelles nous travaillons construites avec React. Donc, en général, les deux sont des outils puissants, et cela dépend surtout de la manière dont vous configurez l'architecture.

### Notes à retenir

* TypeScript est simplement un transpileur, il peut être utilisé avec React ou tout autre framework JS
* React gère la gestion de la mémoire efficacement (Virtual DOM)
* React utilise JavaScript (ES6), un langage web reconnu depuis 1995
* Angular utilise TypeScript, publié en 2012
* Le langage à typage statique est génial, mais ce n'est pas une obligation
* Les langages à typage dynamique nécessitent moins de temps pour écrire et offrent plus de flexibilité pour utiliser la créativité
* L'apprentissage d'un langage à typage statique peut être un défi, surtout si vous n'avez travaillé qu'avec des langages à typage dynamique
* ES6 a mis en œuvre de nombreuses fonctionnalités géniales telles que les modules, les classes, l'opérateur de propagation, les fonctions fléchées, les littéraux de gabarit qui vous permettent d'écrire moins, un code plus propre et plus structuré (sucre syntaxique)
* TS est simplement ES6+ avec des types et bien plus

### Conclusion

Le framework/bibliothèque de composants que vous choisissez peut influencer le temps que vous passez à programmer et votre budget. Si vous avez une équipe de développeurs C#, Java ou C++, alors je choisirais probablement Angular, puisque TypeScript partage de nombreuses similitudes avec ces langages.

La meilleure recommandation que je puisse offrir est de configurer une application de base à la fois en Angular et en React, puis d'évaluer le langage et le flux de travail avant de prendre une décision.

Comme mentionné précédemment, les deux technologies ont leur propre ensemble d'avantages et de similitudes, et cela dépend vraiment du **type d'exigences que l'application offre, de la complexité et du niveau d'expérience des développeurs.**

Voici quelques articles que j'ai écrits sur l'écosystème web ainsi que des conseils et astuces de programmation personnels.

* [Un esprit chaotique conduit à un code chaotique](https://medium.freecodecamp.org/a-chaotic-mind-leads-to-chaotic-code-e7d6962777c0)
* [Les développeurs qui veulent constamment apprendre de nouvelles choses](https://codeburst.io/developers-that-constantly-want-to-learn-new-things-heres-a-tip-7a16e42302e4)
* [Un guide pratique des modules ES6](https://medium.freecodecamp.org/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773)
* [Apprenez ces concepts principaux du Web](https://medium.freecodecamp.org/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0?gi=6274e9c4d599)
* [Améliorez vos compétences avec ces méthodes JavaScript importantes](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)
* [Programmez plus vite en créant des commandes bash personnalisées](https://codeburst.io/learn-how-to-create-custom-bash-commands-in-less-than-4-minutes-6d4ceadd9590)

Vous pouvez me trouver sur Medium où je publie sur une base hebdomadaire. Ou vous pouvez me suivre sur [Twitter](http://twitter.com/dleroari), où je poste des conseils et astuces de développement web pertinents ainsi que des histoires personnelles.

_P.S. Si vous avez aimé cet article et en voulez plus, veuillez applaudir 💙 et partager avec des amis qui pourraient en avoir besoin, c'est du bon karma._