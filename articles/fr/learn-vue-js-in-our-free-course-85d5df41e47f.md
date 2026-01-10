---
title: Apprenez Vue.js dans ce cours gratuit ! ✨
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-10T21:03:18.000Z'
originalURL: https://freecodecamp.org/news/learn-vue-js-in-our-free-course-85d5df41e47f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G1PUKcevhmpXSKUeX9XnLA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: Apprenez Vue.js dans ce cours gratuit ! ✨
seo_desc: 'By ZAYDEK

  Let’s make something Vueseful

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers. I created
  a short questionnaire to check out before...'
---

Par ZAYDEK

#### Faisons quelque chose d'utile avec Vue

Avant de commencer l'article, je souhaite partager que je développe un produit et que j'aimerais collecter des données pour mieux servir les développeurs web. J'ai créé un [court questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) à consulter avant ou après la lecture de cet article. Merci de votre participation ! Et maintenant, revenons à notre programme habituel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G1PUKcevhmpXSKUeX9XnLA.png)

### Bonjour Internet !

Vous ne savez peut-être pas ce qu'est Vue — et c'est tout à fait normal — et, en fait, vous ne savez peut-être pas non plus qui je suis ! Je suis [Zaydek](http://twitter.com/username_ZAYDEK), un graphiste et programmeur expérimenté. [Je viens de lancer un cours gratuit](https://scrimba.com/g/glearnvue) pour aider les développeurs à apprendre Vue ! Je suis ici pour vous éclairer sur toutes les possibilités que présente l'apprentissage et l'utilisation de ce framework open-source incroyable.

Dans cet article, je détaille comment aborder Vue. Je passe également en revue les éléments de base nécessaires pour commencer à programmer des sites web statiques et dynamiques avec une facilité d'un ordre de grandeur supérieur à celle de JavaScript vanilla. 💡 Vue est à la fois un paradigme pour écrire des applications web et un guide idiomatique pour apprendre et programmer en JavaScript.

#### J'enseigne également le JavaScript 💡✨ nécessaire pour commencer dans le cours Vue que je viens de lancer. Apprenez Vue depuis les bases, et comment construire quelques projets. [Cliquez ici pour vous inscrire gratuitement !](https://scrimba.com/g/glearnvue)

![Image](https://cdn-media-1.freecodecamp.org/images/1*q-pzfW25_QfFrGQg2T3FOA.png)
_Cliquez pour vous inscrire à mon cours gratuit sur Vue !_

Le cours est dispensé sur [Scrimba.com](https://scrimba.com/g/glearnvue), qui est un **nouveau site web interactif pour apprendre et partager comment coder**. Les screencasts peuvent être interrompus et modifiés, ce qui rend l'apprentissage actif et amusant à expérimenter.

### Vue n'est pas une seule chose

Un framework peut être considéré comme une boîte à outils polyvalente, équipée d'outils qui résolvent différents problèmes mais qui, ensemble, aident à accomplir une tâche. Cette tâche, en ce qui concerne Vue, est de construire des applications web maintenables et idiomatiques avec facilité — vraiment — et de s'amuser en le faisant !

Mettons les choses en perspective. Vue peut être aussi simple qu'une balise script que nous pouvons inclure dans nos sites web pour les transformer en applications web. Mais il peut aussi être un écosystème entier qui repose sur un processus de construction pour faciliter l'ingénierie d'applications web complexes et puissantes.

Dans cet article et dans le cours, je me concentre sur l'apprentissage des concepts de base que présente Vue, et je ne suppose aucune connaissance de la ligne de commande ou de ce qu'est un processus de construction.

### Ce que couvre le cours

![Image](https://cdn-media-1.freecodecamp.org/images/1*ixssvvdIf64KQONR4Ugn7Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*spoAQtMm1OBMU1iciAZmzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_mu96vH6fakViESA8XOmQg.png)

Le cours est divisé en trois parties :

1. apprendre le minimum de JavaScript nécessaire pour commencer avec Vue
2. apprendre les concepts de base de Vue, et
3. un aperçu de deux exemples plus avancés (deux applications web mignonnes et amusantes que j'ai créées : le Div de Schrödinger 🐱 et un Sélecteur de Couleurs 🎨).

Ce que j'aime dans Vue, c'est qu'il propose des idées intéressantes sur la façon de penser et de construire des applications web. Il y a quelques idées que je trouve particulièrement intéressantes — bien que cela ne représente pas tout ce que Vue peut faire :

* séparer les données du DOM
* JavaScript idiomatique
* templating et HTML basé sur les composants
* gestion des événements

Mais avant d'aborder cela, couvrons d'abord comment connecter Vue via une simple balise script à un site web :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5FJnYPPjV1EKLtk4xk5r2w.png)

Vous pouvez penser à une application web comme étant à l'intérieur ou au-dessus d'un site web. Ainsi, une application web commence sa vie à la `<div id="app">`, où, depuis l'intérieur de la balise script, elle est connectée via `new Vue({ el: "#app" })`. C'est ainsi que nous créons une relation entre le JavaScript et le HTML (où `el` est l'abréviation de element).

Ceci est la première des options connues, et Vue supporte de nombreuses options, telles que `data` et `methods`. Celles-ci sont analogues aux variables et fonctions de notre application web.

**Note :** Vue existe en deux versions : 💡 il y a à la fois la version [développement](https://cdn.jsdelivr.net/npm/vue/dist/vue.js) et la version [production](https://cdn.jsdelivr.net/npm/vue). La version développement émet des messages d'erreur et des avertissements détaillés pour soutenir les développeurs travaillant avec Vue. La version production est optimisée pour la vitesse et la taille.

En plus de tout cela, [il existe une extension officielle Chrome](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd) qui facilite la gestion de l'état de l'application et le débogage.

### Séparer les données du DOM

![Image](https://cdn-media-1.freecodecamp.org/images/1*h6PJeo6PHIpzinqCLkjYCw.jpeg)
_Crédit [Daniel Cheung](https://unsplash.com/photos/bO4UR1VzQu8" rel="noopener" target="_blank" title=")_

Comme mentionné précédemment, une excellente suggestion que propose Vue est de séparer les données du DOM. DOM signifie Document Object Model, qui peut être considéré comme l'arbre des éléments qui composent notre site web. Le texte entre les balises d'ouverture et de fermeture est ce que j'appelle les données. Dans Vue, nous ne les codons pas en dur — nous les séparons et les plaçons dans l'objet `data` mentionné précédemment, à l'intérieur de notre instance Vue.

Cette idée est également appelée le Virtual DOM. Cela peut sembler insignifiant, mais la vérité est que le fait d'avoir les données à un seul endroit signifie que nous savons comment et où les mettre à jour. Et parce que Vue est réactif, chaque fois que nous mettons à jour ces données, ce changement se propage dans toute notre application web. Grâce à cette relation, les données peuvent être considérées comme beaucoup plus vivantes dans Vue que dans le HTML vanilla.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s961WYdfXbFGEVR6bkGtdg.png)

[Ces idées sont explorées dans le troisième screencast.](https://scrimba.com/g/glearnvue)

### JavaScript idiomatique

![Image](https://cdn-media-1.freecodecamp.org/images/1*uJNE1s0MwUXnlRlA7hly8Q.jpeg)
_Crédit [Daniel Cheung](https://unsplash.com/photos/ZqqlOZyGG7g" rel="noopener" target="_blank" title=")_

Pour moi, Vue fait de JavaScript une langue qui vaut la peine d'être apprise, car il donne un sens à JavaScript. Ce que je veux dire, c'est que depuis l'intérieur d'un `new Vue({ ... })` est la façon et l'endroit où nous apprenons à maîtriser JavaScript. Les variables sont des paires clé-valeur attachées à l'objet `data` comme montré ci-dessus, et les fonctions sont attachées comme des paires clé-valeur à un deuxième objet : `methods`. Et les deux objets, data et methods, sont optionnels — rappelez-vous, ce sont les options de notre application web.

Mais Vue va beaucoup plus loin : Vue propose de nombreuses options qui se présentent sous la forme d'objets que nous intégrons dans notre instance Vue. Ensemble, cela ressemble à un guide idiomatique et à une approche de la programmation en JavaScript. Par conséquent, peu de décisions architecturales sont laissées au programmeur. Cela signifie que l'écriture et la lecture de Vue ont une sorte de cohérence et d'élégance qui le rendent plus facile à apprendre que de déconstruire le fonctionnement d'une application JavaScript vanilla.

[Ces idées sont explorées dans le quatrième screencast.](https://scrimba.com/g/glearnvue)

### Templating HTML

![Image](https://cdn-media-1.freecodecamp.org/images/1*OqJU7uN6drj41M8LTMzH_w.jpeg)
_Crédit [Daniel Cheung](https://unsplash.com/photos/dDppsuM_UpE" rel="noopener" target="_blank" title=")_

La plupart des gens ne considèrent pas [HTML comme un langage de programmation](https://www.youtube.com/watch?v=4A2mWqLUpzw). Mais je pense qu'une définition raisonnable du but d'un langage de programmation est la suivante : interpréter et transformer des données, comme la lecture et la compilation de code source.

Étant donné les attributs de Vue, tels que `v-for`, `v-if`, et ainsi de suite, pour moi, HTML commence à ressembler à un langage de programmation avec un contrôle de flux. Cela signifie que nous pouvons mieux contrôler le flux des données de notre programme (par exemple, le contenu de notre site web ou ce que je continue d'appeler les données).

À ce titre, les frameworks de templating, comme [Jekyll](https://jekyllrb.com/) et [Hugo](https://gohugo.io/), ont été créés pour aider les développeurs à créer des sites web statiques en utilisant une sorte de contrôle de flux. Bien que ce soit agréable, cela est limité aux sites web statiques, car ces frameworks compilent en HTML plutôt que d'interpréter le HTML.

Avoir accès à un contrôle de flux en temps réel, comme les boucles for et les instructions if, signifie que Vue peut faire beaucoup plus et le faire en temps réel. C'est l'une des grandes différences entre les sites web et les applications web (contenu statique versus dynamique).

[Ces idées sont explorées dans le cinquième screencast.](https://scrimba.com/g/glearnvue)

### Composants et props

![Image](https://cdn-media-1.freecodecamp.org/images/1*po1kpbyVVzwXrxtKC6A7Bw.jpeg)
_Crédit [James Pond](https://unsplash.com/photos/jnL0gfo_5Rg" rel="noopener" target="_blank" title=")_

Quelque chose qui m'a pris beaucoup trop de temps à apprécier est la différence entre les variables et les propriétés. Les variables stockent des données, tandis que les propriétés sont des variables attachées à un objet en JavaScript. Ainsi, les composants peuvent être considérés comme des mixins HTML. Un quoi ? Un mixin est comme une fonction, mais au lieu de retourner des données, il mélange les données dans le document. Par exemple, il écrit du HTML pour nous afin que nous n'ayons pas à nous répéter !

Et ce n'est pas une petite chose. Le bénéfice des composants et des props dans Vue signifie que nous pouvons refactoriser des blocs de code HTML entiers en lignes uniques qui peuvent être personnalisées via des props. Cela signifie que nous pouvons maintenant créer des éléments personnalisés qui exposent l'accès à leurs éléments internes sans surcompliquer le HTML public. C'est une grande victoire pour un code maintenable et lisible.

[Ces idées sont explorées dans le sixième screencast.](https://scrimba.com/g/glearnvue)

### Gestion des événements

![Image](https://cdn-media-1.freecodecamp.org/images/1*7qN47N73nxf62SJem67Txw.jpeg)
_Crédit [James Pond](https://unsplash.com/photos/gQ-h3k7vHjc" rel="noopener" target="_blank" title=")_

Bien que tout ce dont nous avons parlé jusqu'à présent soit fascinant, cela ne traite pas de l'interaction avec l'utilisateur, qui est l'une des principales différences entre un site web et une application web. Un site web signifie conventionnellement quelque chose qui est plus ou moins statique et qui n'est pas conçu ou destiné à interagir beaucoup avec l'utilisateur, en dehors de la collecte de données. Dans une véritable application web, quelque chose qui rappelle une application native, l'interaction est primordiale. 💡 Cette idée est également appelée un site web dynamique ou une application web.

Puisque Vue est à la fois un framework et un écosystème, il propose également des solutions idiomatiques pour cela. La plus simple que j'enseigne dans le cours est le gestionnaire `@click="function()"` que nous intégrons à un élément en tant qu'attribut HTML. Ce simple extrait nous donne un moyen d'interagir avec nos données, aussi simple qu'un attribut que nous intégrons à un élément. Cela signifie que nous pouvons nous appuyer sur JavaScript et non sur HTML ou CSS pour une interaction riche avec l'utilisateur.

[Ces idées sont explorées dans le septième screencast.](https://scrimba.com/g/glearnvue)

#### Il y a beaucoup plus à apprendre sur Vue, donc j'ai écrit deux autres articles sur le sujet. Après cet article, n'hésitez pas à les consulter !

![Image](https://cdn-media-1.freecodecamp.org/images/1*spoAQtMm1OBMU1iciAZmzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_mu96vH6fakViESA8XOmQg.png)
_Gauche : « [Comment créer un sélecteur de couleurs 🎨 avec Vue !](https://medium.freecodecamp.org/building-schr%C3%B6dingers-div-with-vue-4068f6423830" rel="noopener" target="_blank" title="">Construire le div de Schrödinger 🐱 avec Vue ! » Droite : « [Comment créer un sélecteur de couleurs avec Vue](https://medium.freecodecamp.org/how-to-make-a-color-picker-with-vue-9640043b6c82" rel="noopener" target="_blank" title=") »_

### Vue donne un sens au web

Avant Vue, je connaissais HTML et CSS. J'étais suffisamment à l'aise pour créer des sites web attrayants, mais rien de plus. J'ai exploré quelques frameworks (comme ceux dont j'ai discuté dans cet article concernant la compilation statique), et j'ai jeté un coup d'œil à Angular et React, mais je n'ai pas eu la bonne sensation en explorant ceux-ci. Ce que je voulais, c'était quelque chose de léger et intuitif, et je crois avoir trouvé cela avec Vue.

En fin de compte, peu importe les outils que nous utilisons si nous pouvons créer ce que nous avons l'intention de construire. Mais le problème, c'est qu'il est difficile de séparer les outils de la réflexion utilisée pour construire un produit ou un service. C'est à la fois une bonne et une mauvaise chose. D'une part, cela peut nous rendre étroits d'esprit. Mais à l'autre extrémité du spectre, les outils que nous utilisons peuvent également servir d'instrument d'enseignement pour apprendre de nouvelles idées intéressantes. J'aime les outils qui ne peuvent s'empêcher de m'enseigner en même temps, et je ne pourrais recommander Vue plus pour cette raison !

Alors, s'il vous plaît, allez dans le monde magnifique et apprenez Vue ! Vous pouvez (!) créer des choses incroyables et même changer la vie des gens, même la vôtre. **Et si cela aide, [essayez le cours gratuit](https://scrimba.com/g/glearnvue) !**

![Image](https://cdn-media-1.freecodecamp.org/images/1*q-pzfW25_QfFrGQg2T3FOA.png)