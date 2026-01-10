---
title: Comment créer un sélecteur de couleurs avec Vue !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T19:40:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-color-picker-with-vue-9640043b6c82
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_mu96vH6fakViESA8XOmQg.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Comment créer un sélecteur de couleurs avec Vue !
seo_desc: 'By ZAYDEK

  Caution: colors may appear cuter than they are!

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers. I created
  a short questionnaire t...'
---

Par ZAYDEK

#### Attention : les couleurs peuvent paraître plus mignonnes qu'elles ne le sont !

Avant de commencer l'article, je souhaite partager que je développe un produit et que j'aimerais collecter des données pour mieux servir les développeurs web. J'ai créé un [court questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) à consulter avant ou après la lecture de cet article. Merci de le consulter ! Et maintenant, revenons à notre programme habituel.

![Image](https://cdn-media-1.freecodecamp.org/images/V-DOiGlgMR2tBo5RNps7uY2WwC9tbEX9e6uF)

### Bonjour Internet !

Je suis [Zaydek](https://twitter.com/username_ZAYDEK) et je suis relativement nouveau dans le développement web. Je viens d'un milieu de design graphique et de programmation, donc l'apprentissage du frontend a été fascinant pour moi.

Le web est comme l'enfant d'un designer graphique et d'un programmeur — il est à la fois visuel et programmatique. Aujourd'hui, je vais vous présenter [Vue.js](https://vuejs.org/) et le design web basé sur les composants, c'est-à-dire le développement web moderne. Je vais vous transformer d'un développeur web débutant en un développeur web tout-puissant et omniscient !

> _Comment pouvez-vous faire de telles affirmations, monsieur ?_

> — Vous, avec élégance

Eh bien, le fait est que la plupart des gens ont appris à utiliser Internet avant que nous (en tant que communauté) comprenions comment utiliser Internet ! Moi y compris ! ? Ce qui, pour être honnête, est probablement la raison pour laquelle j'ai refusé d'apprendre le développement web pendant si longtemps. Cela semblait simplement brisé !

Mais les temps changent et le développement web n'a jamais été aussi accessible ou rationalisé. C'est donc un grand honneur et un privilège pour moi de vous montrer comment utiliser Internet en 2018, et peut-être même au-delà !

#### J'enseigne également comment cela fonctionne ? et bien plus encore dans le cours Vue que je viens de publier. Apprenez Vue dès les bases et comment construire quelques choses aussi ! [Cliquez ici pour vous inscrire gratuitement !](https://scrimba.com/g/glearnvue)

![Image](https://cdn-media-1.freecodecamp.org/images/nehx34-E7AQRjhDTfRXmz0fTCXevirAjWeOf)
_[Cliquez pour vous inscrire à mon cours gratuit sur Vue](https://scrimba.com/g/glearnvue" rel="noopener" target="_blank" title=")_

#### [Scrimba.com](https://scrimba.com/g/glearnvue) est un nouveau site interactif pour apprendre et partager comment coder. Les screencasts peuvent être interrompus et modifiés, rendant l'apprentissage actif et amusant à expérimenter !

### Alors, quel est l'avantage de Vue ?

Alors pourquoi [Vue](https://vuejs.org/) ? C'est une excellente et juste question que vous devriez vous poser. Certaines personnes protestent et méprisent l'idée d'utiliser un framework, et je pense que c'est une idée dangereuse. Je suggère cependant que, quel que soit l'outil que vous utilisez, soyez très délibéré et réfléchissez à pourquoi vous l'utilisez.

J'ai choisi Vue parce que je veux utiliser des outils plus récents qui ne sont pas trop grand public. Je voulais qu'ils aient appris des outils qui les ont précédés (ou en d'autres termes, qu'ils ne soient pas trop pionniers). Ils devraient avoir une [documentation de classe mondiale](https://vuejs.org/v2/guide/), et avoir une masse critique d'utilisateurs.

Puisque Vue, ces dernières semaines, a [dépassé React en étoiles sur GitHub](https://hasvuepassedreactyet.surge.sh/), c'est pour moi la preuve que Vue a une masse critique. ?

![Image](https://cdn-media-1.freecodecamp.org/images/vCpg0aDDKpn7wSPw4iEbuE0eK9fHyAIF41aE)
_En passant, [ce site web](https://hasvuepassedreactyet.surge.sh" rel="noopener" target="_blank" title=") a été créé en utilisant Vue.js ! ?_

De plus, [Vue est un projet open-source extraordinaire](https://github.com/vuejs/vue), [est financé publiquement](https://www.patreon.com/evanyou), et offre une excellente expérience développeur ! Comme l'expérience utilisateur, mais pour les développeurs. Cela a la merveilleuse conséquence que le développeur moyen peut maintenant créer des sites web interactifs de manière intuitive. Et Vue s'appuie sur l'une des idées les plus réussies des guerres Angular-React, qui est le Virtual DOM. Alors parlons-en maintenant.

> _Virtual WUT ?_

> — Vous, Internet

Virtual DOM, yo. LOL désolé. Alors faisons un pas en arrière — DOM est l'abréviation de document-object-model. Je considère le DOM comme un paradigme pour la façon dont nous pensons au texte comme des structures de données pour composer ce que nous appelons des pages web. Et un DOM virtuel est une abstraction ingénieuse pour traiter le texte qui va entre les éléments, comme `<p>bonjour, monde</p>`. Dans un site web idiomatique basé sur Vue, c'est quelque chose comme `<p>{{ message }}</p>`, où les données sont stockées à l'intérieur du JavaScript au lieu !

> _Pourquoi dépendre de JavaScript pour un simple site web ?_

> — Vous, innocent

C'est un excellent (et juste) point. Mais il y a un avantage significatif à dépendre de JavaScript pour composer des sites web, statiques ou dynamiques. Nous pouvons écrire et construire des sites web de manière programmatique au lieu de copier-coller des données. Une fois que les données sont séparées du HTML, tout comme avoir le CSS séparé du HTML, c'est là que des choses magiques peuvent commencer à se produire. ?

La bonne nouvelle est que, puisque nous en sommes venus à attendre tellement des sites web, il est juste de supposer que la majorité des gens auront JavaScript activé par défaut. Nous n'avons donc aucune raison de le désactiver. J'aurais peut-être été en désaccord avec cela il y a quelques années, mais je peux maintenant apprécier à quel point les avantages de l'utilisation de JavaScript l'emportent largement sur les préoccupations possibles qui pourraient survenir.

### Alors… qu'en est-il de ce sélecteur de couleurs, hein ?

![Image](https://cdn-media-1.freecodecamp.org/images/VNZfvY7c9sYl-1JCG5tll3QJPgWjXNTYgD8z)

![Image](https://cdn-media-1.freecodecamp.org/images/rBvQ8vNQMBafRf3hmnV8-cyALn5xd01lh81P)

![Image](https://cdn-media-1.freecodecamp.org/images/jkR1hOGbO8JVeb6T-Z7KXc7aPDgHPFNyWBSC)
_Cliquez pour choisir une couleur, n'importe laquelle !_

Désolé pour le bavardage ! Il est difficile pour moi de ne pas parler de cela longuement, en partie parce que c'est si excitant. Et aussi en partie à cause de la gamme de possibilités qui se présentent lorsqu'un seul développeur peut être responsable de la création de belles applications web interactives/entreprises. Des entreprises, dites-vous ? Oui — [Suivez-moi sur Twitter](https://twitter.com/username_ZAYDEK) et je m'assurerai de suivre ! ?

Sans plus attendre, voici le HTML pour le site web :

![Image](https://cdn-media-1.freecodecamp.org/images/AVS2iaAAgowtEcDXSlKWV6dPHUldlCE8EvCV)

Psst… le code complet est disponible dans le [neuvième screencast](https://scrimba.com/p/pZ45Hz/crVeyTd).

Vous êtes choqué ? Le fait est, réfléchissons à la complexité inhérente du site web que je vous ai montré. Ce n'est vraiment qu'une boîte avec deux cellules, une avec un emoji et une avec du texte, répétée 12 fois. Oui, il y a un peu de remplissage, il y a quelques dégradés, mais le design fondamental est inchangé. Alors, et si la complexité du code était proportionnelle à la complexité du design ?

![Image](https://cdn-media-1.freecodecamp.org/images/zhdMTMFVhE-GWzYCcw9lhK90NVViglhCJqn2)

![Image](https://cdn-media-1.freecodecamp.org/images/wHs5kNPsPAY3xGrQTbbqUFWr2iN4-OfWXu45)
_C'est ce que j'appelle un débogueur CSS. Vous pouvez en apprendre plus à ce sujet (et comment l'utiliser) en [cliquant ici](https://gist.github.com/zaydek/6b2e55258734deabbd2b4a284321d6f6" rel="noopener" target="_blank" title=")._

Ici, j'ai appliqué un [débogueur CSS](https://gist.github.com/zaydek/6b2e55258734deabbd2b4a284321d6f6) pour désambiguïser le design, mais cela ne va que jusqu'au CSS. Ce qui est plus important ici, la véritable signification de Vue, est la façon dont nous pouvons penser à notre site web en termes de données et non en termes d'éléments HTML.

Alors regardez à nouveau ces images. Si nous pensons à notre site web purement en termes de données, combien de données y a-t-il ?

Permettez-moi maintenant de partager la structure de données sous-jacente utilisée :

![Image](https://cdn-media-1.freecodecamp.org/images/7b0uUS6QZGfjM3FEpeh6z-j4rQqHggb7kole)
_emojify() est une fonction auxiliaire_

La phrase suivante est peut-être la plus importante : **Vue nous libère pour penser à notre site web en termes de données, séparées du HTML ; c'est une révolution pour la façon dont nous pouvons construire pour le web !**

Pour être explicite, ce que je vous montre est un tableau d'objets anonymes chacun avec deux clés : `emoji`, et `color`. Maintenant que nous pouvons représenter le site web en termes de données, nous itérons simplement sur les données en utilisant `v-for` de Vue et un composant personnalisé.

### Oui, c'est ça. Alors, qu'en est-il des composants ?

Les composants — oui ! Après la séparation des données du HTML, l'une des choses les plus cool que Vue offre est le design basé sur les composants. Les composants peuvent nous aider à abstraire des blocs de HTML/CSS/JS en une unité réutilisable : un composant.

**Une note rapide** : J'ai décidé qu'il serait préférable d'apprendre d'abord à utiliser Vue sans processus de construction, ce qui signifie que je n'utilise pas de composants à fichier unique. Mais j'utilise des composants via `Vue.component()`.

Vous vous souvenez de l'élément `<swatch>` que j'ai démontré plus tôt dans le code source ? C'est un composant personnalisé que j'ai conçu en utilisant Vue pour abstraire l'élément de l'implémentation. C'est un concept significatif, car cela signifie que nous pouvons commencer à penser de manière plus fonctionnelle qu'impérative.

Quelle est la différence ? Le design fonctionnel se soucie du résultat, tandis que le design impératif se soucie du résultat **et** de l'implémentation. Concevoir un composant est un processus impératif, tandis que l'utiliser est fonctionnel. ?

![Image](https://cdn-media-1.freecodecamp.org/images/Aix-LCVU5Ffx7zQfjKXdoFQKFcYHkHWtKqkR)

C'est l'implémentation de l'élément `swatch` montré précédemment. Comment cela fonctionne, c'est que Vue scanne le DOM pour les instances de `swatch` et les remplace par le HTML cité à l'intérieur de la valeur `template` du composant. Cela signifie que nous pouvons faire des refactorisations majeures pour mieux comprendre notre site web en termes de concepts, plutôt que de nous soucier de la façon dont quelque chose devrait être conçu tout le temps.

#### Il y a beaucoup plus à apprendre sur Vue, alors j'ai écrit deux autres articles sur le sujet. S'il vous plaît, après cet article, jetez un coup d'œil !

![Image](https://cdn-media-1.freecodecamp.org/images/ozARrBWWUuMdflw5O99w8TL9fpmXkq-IrWxz)

![Image](https://cdn-media-1.freecodecamp.org/images/Bjc0ppEmnmqc5KQKLRIHCXPHnOTVdTpmf0Lj)
_Gauche : « [Apprendre Vue.js dans ce cours gratuit ! ?✨](https://medium.freecodecamp.org/learn-vue-js-in-our-free-course-85d5df41e47f" rel="noopener" target="_blank" title=") » Droite : « [Construire le div de Schrödinger avec Vue !](https://medium.freecodecamp.org/building-schr%C3%B6dingers-div-with-vue-4068f6423830" rel="noopener" target="_blank" title=") »_

### Eh bien, vous avez changé mon avis..

Je sais que cela peut être beaucoup à assimiler, surtout pour quelque chose d'aussi anodin qu'un sélecteur de couleurs ?. Mais ce que je vous ai montré est (à part le CSS) 90 % de la base de code. Il y a au moins quelques fonctions auxiliaires que j'omets, mais le point est que les techniques et les idéologies discutées s'additionnent à bien plus qu'une application web mignonne. Cela signifie qu'un individu seul peut créer de beaux produits et services web fonctionnels pour les autres.

Je suggère également que Vue est bien plus qu'un framework. Si associé au bon langage backend (faisons un coup de projecteur pour [Go](https://golang.org/) !), apprendre et utiliser Vue s'additionne à bien plus. Vue idiomatique peut également enseigner ce que signifie le développement logiciel moderne, et comment accéder aux milliards (!) d'entre nous qui sont maintenant connectés, sans les mêmes barrières techniques qui accompagnent le développement d'applications.

#### Alors s'il vous plaît, allez dans le monde magnifique et apprenez Vue ! Vous pouvez (!) créer des choses incroyables et même changer la vie des gens, même la vôtre. Et si cela aide, [essayez le cours gratuit](https://scrimba.com/g/glearnvue) !

![Image](https://cdn-media-1.freecodecamp.org/images/xdrJi-5Z3EID6sEgh8dvUk7u335SFakRO4SX)