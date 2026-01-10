---
title: Un Plan d'Étude Pour Guérir la Fatigue JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-31T07:19:05.000Z'
originalURL: https://freecodecamp.org/news/a-study-plan-to-cure-javascript-fatigue-8ad3a54f2eb1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9aqEe1RQXAh77hA07VZN0w.png
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un Plan d'Étude Pour Guérir la Fatigue JavaScript
seo_desc: 'By Sacha Greif

  Like everybody else, I recently came across Jose Aguinaga’s post “How it feels to
  learn JavaScript in 2016”.

  It’s clear that this post hit a nerve: I saw it reaching the top spot on Hacker
  News not once but twice. It was the most popul...'
---

Par Sacha Greif

Comme tout le monde, j'ai récemment découvert le post de Jose Aguinaga « [Comment on se sent en apprenant JavaScript en 2016](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f#.5wjpn7svo) ».

Il est clair que ce post a touché une corde sensible : je l'ai vu atteindre la première place sur [Hacker News](http://news.ycombinator.com) non pas une, mais deux fois. C'était le post le plus populaire sur [/r/javascript](http://reddit.com/r/javascript/), et à l'heure actuelle, il a plus de 10k likes sur Medium — ce qui est probablement plus que tous mes propres posts réunis. Mais qui compte ?

Cela n'a pas été une surprise : je savais depuis longtemps que l'écosystème JavaScript peut être déroutant. En fait, la raison même pour laquelle j'ai mené l'enquête [State Of JavaScript](http://stateofjs.com) était de découvrir quelles bibliothèques étaient réellement populaires, et enfin de séparer le bon grain de l'ivraie.

Mais aujourd'hui, je veux aller plus loin. Au lieu de simplement me plaindre de l'état des choses, je vais vous donner un plan d'étude concret, étape par étape, pour maîtriser l'écosystème JavaScript.

### À Qui Ce Plan S'Adresse

Ce plan d'étude est pour vous si :

* Vous êtes déjà familier avec les concepts de base de la programmation comme les variables et les fonctions.
* Vous avez peut-être déjà fait du travail back-end avec des langages comme PHP et Python, et peut-être utilisé des bibliothèques front-end comme jQuery pour quelques hacks simples.
* Vous souhaitez maintenant vous lancer dans un développement front-end plus sérieux mais vous êtes submergé par les frameworks et les bibliothèques avant même d'avoir commencé.

### Ce Que Nous Allons Couvrir

* À quoi ressemble une application web JavaScript moderne
* Pourquoi vous ne pouvez pas simplement utiliser jQuery
* Pourquoi React est le choix le plus sûr
* Pourquoi vous n'avez peut-être pas besoin d'« apprendre JavaScript correctement » d'abord
* Comment apprendre la syntaxe ES6
* Pourquoi et comment apprendre Redux
* Qu'est-ce que GraphQL et pourquoi c'est une grosse affaire
* Où aller ensuite

### Ressources Mentionnées Ici

Avertissement : ce post inclura quelques liens d'affiliation vers des cours de [Wes Bos](http://wesbos.com/), mais le matériel est recommandé parce que je pense sincèrement qu'il est bon, et pas seulement à cause du programme d'affiliation.

Si vous préférez trouver d'autres ressources, Mark Erikson maintient une excellente liste de liens sur [React, ES6, et Redux](https://github.com/markerikson/react-redux-links).

### JavaScript vs JavaScript

Avant de commencer, nous devons nous assurer que nous parlons de la même chose. Si vous recherchez « Apprendre JavaScript » ou « Plan d'étude JavaScript », vous trouverez une tonne de ressources qui vous enseignent comment apprendre le langage JavaScript.

Mais c'est en fait la partie facile. Bien que vous puissiez certainement creuser profondément et apprendre les subtilités du langage, la vérité est que la plupart des applications web utilisent un code relativement simple. En d'autres termes, 80 % de ce dont vous aurez besoin pour écrire des applications web est généralement couvert dans les premiers chapitres de votre livre JavaScript typique.

Non, le problème difficile est de maîtriser l'écosystème JavaScript, avec ses innombrables frameworks et bibliothèques en compétition. La bonne nouvelle, c'est que c'est exactement sur quoi ce plan d'étude se concentre.

### Les Briques de Base des Applications JavaScript

Pour comprendre pourquoi les applications JavaScript modernes semblent si complexes, vous devez d'abord comprendre comment elles fonctionnent.

Pour commencer, regardons une application web « traditionnelle » vers 2008 :

![Image](https://cdn-media-1.freecodecamp.org/images/a5vRMwjVXfM5uDwt6Kepza-Tt92DmZogq1KJ)

1. La base de données envoie des données à votre back-end (par exemple, votre application PHP ou Rails).
2. Le back-end lit ces données et génère du HTML.
3. Le HTML est envoyé au navigateur, qui l'affiche sous forme de DOM (basiquement, une page web).

Beaucoup de ces applications ajoutaient également du code JavaScript côté client pour ajouter de l'interactivité, comme des onglets et des fenêtres modales. Mais fondamentalement, le navigateur recevait toujours du HTML et partait de là.

Comparez maintenant cela avec une application web « moderne » de 2016 (également connue sous le nom d'« Application Monopage ») :

![Image](https://cdn-media-1.freecodecamp.org/images/XkXQGT4yHkgkpBojIYxqwAXIhUCeKHtBjs12)

Remarquez la différence ? Au lieu d'envoyer du HTML, le serveur envoie maintenant des données, et l'étape de conversion « données vers HTML » se produit côté client (c'est pourquoi vous envoyez également le code qui indique au client comment effectuer ladite conversion).

Cela a de nombreuses implications. D'abord, le bon :

* Pour un contenu donné, envoyer uniquement des données est plus rapide que d'envoyer des pages HTML entières.
* Le client peut échanger du contenu instantanément sans avoir à rafraîchir la fenêtre du navigateur (d'où le terme « Application Monopage »).

Le mauvais :

* Le chargement initial prend plus de temps puisque la base de code « données vers HTML » peut devenir assez grande.
* Vous avez maintenant besoin d'un endroit pour stocker et gérer les données côté client, au cas où vous souhaiteriez les mettre en cache ou les inspecter.

Et le laid :

* Félicitations — vous devez maintenant gérer une pile côté client, qui peut devenir aussi complexe que votre pile côté serveur.

### Le Spectre Client-Serveur

Alors pourquoi passer par tous ces tracas s'il y a tant d'inconvénients ? Pourquoi ne pas simplement rester avec les bonnes vieilles applications PHP ?

Eh bien, imaginez que vous construisez une calculatrice. Si l'utilisateur veut savoir ce que 2 + 2 fait, cela n'a pas de sens de revenir au serveur pour effectuer l'opération lorsque le navigateur est parfaitement capable de le faire.

D'un autre côté, si vous construisez un site purement statique comme un blog, il est parfaitement acceptable de générer le HTML final sur le serveur et d'en rester là.

La vérité est que la plupart des applications web se situent quelque part au milieu du spectre. Le problème est de savoir où.

Mais la chose clé est que le spectre n'est pas continu : vous ne pouvez pas commencer avec une application purement côté serveur et lentement évoluer vers une application purement côté client. À un moment donné (la Divide), vous serez forcé de vous arrêter et de tout refactoriser, sinon vous finirez avec un désordre de code spaghetti inmaintenable.

![Image](https://cdn-media-1.freecodecamp.org/images/EaPbfy1YtKtMalzoM-e0foWtXQ8xJfakOgqJ)

C'est pourquoi vous ne devriez pas « simplement utiliser jQuery » pour tout. Vous pouvez penser à jQuery comme du ruban adhésif. Il est incroyablement pratique pour les petites réparations autour de la maison, mais si vous continuez à en ajouter, les choses commenceront à avoir l'air moche.

D'un autre côté, les frameworks JavaScript modernes sont plus comme l'impression 3D d'une pièce de rechange : cela prend plus de temps, mais le résultat est beaucoup plus propre et plus solide.

En d'autres termes, maîtriser la pile JavaScript moderne est un pari que, peu importe où elles commencent, la plupart des applications web finiront probablement du bon côté de la divide tôt ou tard. Donc oui, c'est plus de travail, mais mieux vaut prévenir que guérir.

### Semaine 0 : Les Bases de JavaScript

Sauf si vous êtes un développeur purement back-end, vous connaissez probablement un peu de JavaScript. Et même si ce n'est pas le cas, la syntaxe de JavaScript, similaire à celle du C, vous semblera quelque peu familière si vous êtes un développeur PHP ou Java.

Mais si JavaScript est un mystère complet pour vous, ne désespérez pas. Il existe de nombreuses ressources gratuites qui vous mettront rapidement à niveau. Par exemple, un bon point de départ est [les leçons JavaScript de Codecademy](https://www.codecademy.com/learn/javascript).

### Semaine 1 : Commencez avec React

Maintenant que vous connaissez la syntaxe de base de JavaScript et que vous comprenez pourquoi les applications JavaScript peuvent sembler si complexes, parlons des détails. Par où devriez-vous commencer ?

Je crois que la réponse est [React](https://facebook.github.io/react/).

![Image](https://cdn-media-1.freecodecamp.org/images/W8VzkiwWwoiWCUbFMA7CGeaft2OiDaSeOXk3)

React est une bibliothèque d'interface utilisateur créée et open-sourcée par Facebook. En d'autres termes, elle s'occupe de cette étape de conversion « données vers HTML » (la couche de vue).

Maintenant, ne vous méprenez pas : je ne vous dis pas de choisir React parce que c'est la meilleure bibliothèque (car c'est très subjectif), mais parce qu'elle est assez bonne.

* React n'est peut-être pas la bibliothèque la plus populaire, mais elle est assez populaire.
* React n'est peut-être pas la bibliothèque la plus légère, mais elle est assez légère.
* React n'est peut-être pas la plus facile à apprendre, mais elle est assez facile à apprendre.
* React n'est peut-être pas la bibliothèque la plus élégante, mais elle est assez élégante.

En d'autres termes, React n'est peut-être pas le meilleur choix dans toutes les situations, mais je crois que c'est le plus sûr. Et croyez-moi, « juste quand vous commencez » n'est pas le bon moment pour prendre des risques avec vos choix technologiques.

React vous présentera également des concepts utiles comme les composants, l'état de l'application et les fonctions sans état qui vous seront utiles, quel que soit le framework ou les bibliothèques que vous finirez par utiliser au cours de votre carrière.

Enfin, React dispose d'un large écosystème d'autres packages et bibliothèques qui fonctionnent bien avec lui. Et sa popularité signifie que vous pourrez trouver beaucoup d'aide sur des sites comme Stack Overflow.

Je recommande personnellement le cours [React for Beginners](https://reactforbeginners.com/friend/STATEOFJS) de Wes Bos. C'est comme ça que j'ai appris React moi-même, et il vient d'être entièrement refondu avec les meilleures pratiques React les plus récentes.

### Devriez-vous « Apprendre JavaScript Correctement » D'abord ?

Si vous êtes un apprenant très méthodique, vous voudrez peut-être bien comprendre les fondamentaux de JavaScript avant de faire autre chose.

Mais pour d'autres, cela ressemble à apprendre à nager en étudiant l'anatomie humaine et la dynamique des fluides. Bien sûr, ils jouent tous les deux un rôle énorme dans la natation, mais c'est plus amusant de simplement sauter dans la piscine !

Il n'y a pas de bonne ou de mauvaise réponse ici, tout dépend de votre style d'apprentissage. La vérité est que la plupart des tutoriels React de base n'utiliseront probablement qu'un petit sous-ensemble de JavaScript de toute façon, il est donc parfaitement acceptable de se concentrer uniquement sur ce dont vous avez besoin maintenant et de laisser le reste pour plus tard.

Cela s'applique également à l'écosystème JavaScript dans son ensemble. Ne vous inquiétez pas trop de comprendre les tenants et les aboutissants de choses comme Webpack ou Babel pour l'instant. En fait, React a récemment sorti son propre petit [utilitaire en ligne de commande](https://github.com/facebookincubator/create-react-app) qui vous permet de créer des applications sans aucune configuration de build.

### Semaine 2 : Votre Premier Projet React

Supposons que vous venez de terminer un cours React. Si vous êtes comme moi, deux choses sont probablement vraies :

* Vous avez déjà oublié la moitié de ce que vous venez d'apprendre.
* Vous ne pouvez pas attendre pour mettre en pratique la moitié que vous vous souvenez.

Je crois que la meilleure façon d'apprendre un framework ou un langage est de simplement l'utiliser. Et les projets personnels sont l'occasion parfaite pour essayer de nouvelles technologies.

Un projet personnel peut être n'importe quoi, d'une seule page à une application web complexe, mais je pense que la refonte de votre propre site personnel peut être un bon compromis. De plus, je sais que vous l'avez probablement reporté depuis des années !

Maintenant, j'ai dit plus tôt que l'utilisation d'applications monopages pour du contenu statique était souvent excessive, mais React a en fait une arme secrète : [Gatsby](https://github.com/gatsbyjs/gatsby), un générateur de site statique React qui vous permet de « tricher » et d'obtenir tous les avantages de React sans aucun des inconvénients.

![Image](https://cdn-media-1.freecodecamp.org/images/8Y20yyMExUv3c79wf9jBUtDlosGtaM8zGLCM)

Voici pourquoi Gatsby est un excellent moyen de commencer avec React :

* Un Webpack préconfiguré, ce qui signifie que vous obtenez tous les avantages sans aucun des maux de tête.
* Un routage automatique basé sur votre structure de répertoires.
* Tout le contenu HTML est également généré côté serveur, vous obtenez donc le meilleur des deux mondes.
* Le contenu statique signifie pas de serveur et un hébergement super facile sur [GitHub Pages](https://pages.github.com/).

J'ai utilisé Gatsby pour le site [State Of JavaScript](http://stateofjs.com), et ne pas avoir à m'inquiéter du routage, de la configuration des outils de build, ou du rendu côté serveur m'a fait gagner beaucoup de temps.

### Semaine 3 : Maîtriser ES6

Dans ma propre quête pour apprendre React, j'ai rapidement atteint un point où je pouvais me débrouiller en copiant-collant des exemples de code, mais il y avait encore beaucoup de choses que je ne comprenais pas.

Plus précisément, je n'étais pas familier avec toutes les nouvelles fonctionnalités introduites par [ES6](http://es6-features.org/#Constants), telles que :

* Les fonctions fléchées
* La déstructuration d'objets
* Les classes
* L'opérateur de décomposition

Si vous êtes dans le même bateau, il est peut-être temps de prendre quelques jours et d'apprendre ES6 correctement. Si vous avez aimé le cours React for Beginners, vous voudrez peut-être consulter les excellentes vidéos [ES6 for Everybody](https://es6.io/friend/stateofjs) de Wes.

Ou si vous préférez les ressources gratuites, consultez [le livre de Nicolas Bevacqua, Practical ES6](https://ponyfoo.com/books/practical-es6/chapters).

Un bon exercice pour maîtriser ES6 est de parcourir un ancien code (comme celui que vous venez de créer dans la Semaine 2 !) et de convertir votre code en syntaxe ES6, plus courte et plus concise, chaque fois que possible.

### Semaine 4 : Prendre en Charge la Gestion d'État

À ce stade, vous devriez être capable de construire un front-end React simple soutenu par du contenu statique.

Mais les vraies applications web ne sont pas statiques : elles doivent obtenir leurs données de quelque part, généralement une base de données.

Maintenant, vous pourriez simplement envoyer des données à vos composants individuels, mais cela devient rapidement désordonné. Par exemple, que se passe-t-il si deux composants doivent afficher la même pièce de données ? Ou doivent communiquer entre eux ?

C'est là que la **Gestion d'État** entre en jeu. Au lieu de stocker votre état (en d'autres termes, vos données) bit par bit dans chaque composant, vous le stockez dans un seul **magasin global** qui le distribue ensuite à vos composants React :

![Image](https://cdn-media-1.freecodecamp.org/images/K0M0mRxQv3iHLtpp6dSrdDhJyf4ShwO3zBNo)

Dans le monde React, la bibliothèque de gestion d'état la plus populaire est Redux. Redux non seulement aide à centraliser vos données, mais il impose également des protocoles stricts pour manipuler ces données.

![Image](https://cdn-media-1.freecodecamp.org/images/0PpfZoG5IXx7Z0nQDLtY0hOA38UuTPtQGGTW)

Vous pouvez penser à Redux comme à une banque : vous ne pouvez pas aller à votre agence locale et modifier manuellement le solde de votre compte (« tiens, laissez-moi juste ajouter quelques zéros en plus ! »). Au lieu de cela, vous remplissez un formulaire de dépôt, puis vous le donnez à un employé de banque autorisé à effectuer l'action.

De même, Redux ne vous permettra pas de modifier votre état global directement. Au lieu de cela, vous passez des _actions_ à des _réducteurs_, des fonctions spéciales qui effectuent l'opération et retournent le nouvel état mis à jour en résultat.

Le résultat de tout ce travail supplémentaire est un flux de données hautement standardisé et maintenable dans toute votre application, et l'accès à des outils tels que les [Redux Devtools](https://github.com/gaearon/redux-devtools) pour vous aider à le visualiser :

![Image](https://cdn-media-1.freecodecamp.org/images/DhG9IaSZIgdYiNbh-TdRsTzl5qU4-gQvkoC7)

Une fois de plus, vous pouvez rester avec notre ami Wes et apprendre Redux avec [son cours Redux](https://learnredux.com/), qui est en fait complètement gratuit !

Ou, vous pouvez consulter la série de vidéos du créateur de Redux, Dan Abramov, sur [egghead.io](https://egghead.io/courses/getting-started-with-redux), qui est également gratuite.

### Semaine Bonus 5 : Construire des API avec GraphQL

Jusqu'à présent, nous avons principalement parlé du client, et ce n'est que la moitié de l'équation. Et même sans entrer dans tout l'écosystème Node, il est important d'aborder un aspect clé de toute application web : comment les données passent du serveur au client.

Il ne sera pas surprenant que cela aussi change rapidement, avec [GraphQL](http://graphql.org) (un autre projet open-source de Facebook) émergent comme une alternative sérieuse aux API REST traditionnelles.

![Image](https://cdn-media-1.freecodecamp.org/images/6WMbmm3Dc4ERuTJZypPfP6g4YpeGXA1SYtZI)

Alors qu'une API REST expose plusieurs routes REST qui vous donnent chacune accès à un ensemble de données prédéfinies (par exemple, /api/posts, /api/comments, etc.), GraphQL expose un seul point de terminaison qui permet au client de demander les données dont il a besoin.

Pensez à cela comme à faire plusieurs voyages à la boucherie, à la boulangerie et à l'épicerie, contre donner à quelqu'un une liste de courses et l'envoyer dans les trois.

Cette nouvelle stratégie devient particulièrement significative lorsque vous devez interroger plusieurs sources de données. Tout comme avec notre exemple de liste de courses, vous pouvez maintenant obtenir des données de toutes ces sources avec une seule requête.

GraphQL a pris de l'ampleur au cours de l'année écoulée, avec de nombreux projets (comme [Gatsby](https://github.com/gatsbyjs/gatsby/), que nous avons utilisé dans la Semaine 2) prévoyant de l'adopter.

GraphQL lui-même n'est qu'un protocole, mais sa meilleure implémentation à l'heure actuelle est probablement la bibliothèque [Apollo](http://apollostack.com), qui fonctionne bien avec Redux. Il manque encore de matériel pédagogique autour de GraphQL et Apollo, mais espérons que la [documentation Apollo](http://dev.apollodata.com/) puisse vous aider à commencer.

### Au-delà de React et Cie

Je vous ai recommandé de commencer avec l'écosystème React parce que c'est un choix sûr, mais ce n'est en aucun cas la seule pile front-end valide. Si vous voulez continuer à explorer, voici deux recommandations :

#### Vue

[Vue](http://vuejs.org/) est une bibliothèque relativement nouvelle, mais elle croît à des vitesses record et a déjà été adoptée par de grandes entreprises, surtout en Chine où elle est utilisée par des entreprises comme Baidu et Alibaba (pensez à Google chinois et Amazon chinois). Et c'est également la couche front-end officielle du framework PHP [Laravel](https://laravel.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/Baeyi33ETMymHnmWEkv9IlaxRG--zEPKBSkY)

Comparé à React, certains de ses principaux arguments de vente sont :

* Des bibliothèques de routage et de gestion d'état maintenues officiellement.
* Un accent sur la performance.
* Une courbe d'apprentissage plus faible grâce à l'utilisation de modèles basés sur HTML.
* Moins de code boilerplate.

À l'heure actuelle, les deux principales choses qui donnent encore à React un avantage sur Vue sont la taille de l'écosystème React et [React Native](https://facebook.github.io/react-native/) (plus sur cela plus tard). Mais je ne serais pas surpris de voir Vue rattraper son retard bientôt !

#### Elm

Si Vue est l'option la plus accessible, [Elm](http://elm-lang.org/) est celle la plus à la pointe. Elm n'est pas seulement un framework, mais un tout nouveau langage qui se compile en JavaScript.

Cela apporte de multiples avantages, tels qu'une performance améliorée, une version sémantique imposée et aucune exception d'exécution.

Je n'ai pas essayé Elm personnellement, mais il m'a été chaudement recommandé par des amis et les utilisateurs d'Elm semblent généralement très satisfaits (comme le montre son [taux de satisfaction de 84 %](http://stateofjs.com/2016/flavors/) dans l'enquête State Of JavaScript).

### Prochaines Étapes

À ce stade, vous devriez avoir une assez bonne compréhension de toute la pile front-end React et, espérons-le, être raisonnablement productif avec elle.

Cela ne signifie pas que vous avez terminé ! Ce n'est que le début de votre voyage à travers l'écosystème JavaScript. Certains des autres sujets que vous rencontrerez éventuellement incluent :

* JavaScript sur le serveur (Node, [Express](https://expressjs.com/)...)
* Tests JavaScript ([Jest](https://facebook.github.io/jest/), [Enzyme](https://github.com/airbnb/enzyme)...)
* Outils de build ([Webpack](https://webpack.github.io/)...)
* Systèmes de typage ([TypeScript](https://www.typescriptlang.org/), [Flow](https://flowtype.org/)...)
* Gestion du CSS dans vos applications JavaScript ([CSS Modules](https://github.com/css-modules/css-modules), [Styled Components](https://github.com/styled-components/styled-components)...)
* JavaScript pour les applications mobiles ([React Native](https://facebook.github.io/react-native/)...)
* JavaScript pour les applications de bureau ([Electron](http://electron.atom.io/)...)

Je ne peux pas tout couvrir ici, mais ne désespérez pas ! La première étape est toujours la plus difficile, et devinez quoi : vous venez de la franchir en lisant ce plan d'étude.

Et maintenant que vous comprenez comment les différentes pièces de l'écosystème s'emboîtent, il ne s'agit que d'aligner ce que vous voulez apprendre ensuite et de maîtriser une nouvelle technologie chaque mois.

### Restez en Contact

Avez-vous trouvé ce plan d'étude utile ? Quel domaine de JavaScript aimeriez-vous que j'aborde ensuite ? Laissez un commentaire ou [tweetez](http://twitter.com/sachagreif) pour me le faire savoir !

Et si vous voulez savoir la prochaine fois que je publie un post, vous pouvez également [vous inscrire à la liste de diffusion State Of JavaScript](http://eepurl.com/ccyxCn).