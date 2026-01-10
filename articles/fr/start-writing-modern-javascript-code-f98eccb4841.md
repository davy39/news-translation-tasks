---
title: ES2015 est déjà là — il n'est simplement pas très uniformément distribué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-10T20:36:22.000Z'
originalURL: https://freecodecamp.org/news/start-writing-modern-javascript-code-f98eccb4841
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EXorOYogh19X_PA08uKODQ.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: ES2015 est déjà là — il n'est simplement pas très uniformément distribué
seo_desc: 'By Alex Moldovan

  In 2015, ECMA International finalized the ECMAScript 6 specifications and renamed
  it to ECMAScript 2015 (ES 2015). This means is that we have a new standard in writing
  JavaScript code.

  Sounds cool, can I use it?

  ES2015 comes with a b...'
---

Par Alex Moldovan

En 2015, ECMA International a finalisé les [spécifications ECMAScript 6](http://www.ecma-international.org/ecma-262/6.0/) et l'a renommé **ECMAScript 2015 (ES 2015)**. Cela signifie que nous avons une nouvelle norme pour écrire du code **JavaScript**.

#### Cela semble cool, puis-je l'utiliser ?

ES2015 arrive avec un ensemble de nouvelles fonctionnalités cool que nous discuterons brièvement plus tard. Maintenant que ces fonctionnalités sont essentiellement figées pour cette itération, il est sûr de commencer à travailler avec elles dans des applications de production à grande échelle.

De plus, je vous encourage à migrer votre ancien code dès que possible vers la nouvelle norme, car _toute ligne de code que vous écrivez en utilisant l'ancienne norme ES5 est obsolète dès le premier jour_.

> « Le futur est déjà là — il n'est simplement pas très uniformément distribué. » — William Gibson

Comme vous pouvez le voir dans [le tableau de compatibilité](https://kangax.github.io/compat-table/es6/), ES2015 est adopté à un rythme rapide par tous les navigateurs, même [Safari](https://kangax.github.io/compat-table/es6/#safari9) et [Microsoft Edge](https://kangax.github.io/compat-table/es6/#edge13) (le nom fantaisiste qu'ils ont inventé pour la nouvelle version d'IE). Toutes les fonctionnalités ne sont pas encore implémentées, mais vous pouvez déjà utiliser une bonne partie des nouvelles fonctionnalités directement dans le navigateur.

Cependant, je ne vous conseille pas d'écrire du code ES2015 et de l'exécuter directement dans le navigateur. [Dites bonjour à **babel**](https://babeljs.io/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*XmHUL5DeySv_dGmvbPqdDQ.png)

**Babel.js** est un [**transpileur**](https://en.wikipedia.org/wiki/Source-to-source_compiler) que vous pouvez très facilement intégrer dans votre processus de build JavaScript.

Si vous souhaitez en savoir plus sur l'utilisation de babel pour toutes vos applications JavaScript — ou sur la mise en place d'un processus de build — je vous encourage à lire [cet article](https://medium.com/javascript-scene/how-to-use-es6-for-isomorphic-javascript-apps-2a9c3abe5ea2#.xps7gn6up). Ensuite, familiarisez-vous avec des outils comme [grunt](http://gruntjs.com/) et [gulp](http://gulpjs.com/), et avec des bundlers de modules comme [webpack](https://webpack.github.io/) et [Browserify](http://browserify.org/), car ils deviennent lentement mais sûrement des standards de l'industrie.

Ainsi, nous écrivons du code ES2015 aujourd'hui, le code est transpilé en ES5, qui est presque 100 % supporté dans la plupart des navigateurs modernes. Une fois que la plupart des fonctionnalités majeures offertes par ES2015 sont implémentées dans les navigateurs modernes, nous nous débarrassons simplement du transpileur babel de notre processus de build. Ainsi, en une seule étape, nous faisons passer notre code en production à la norme ES2015.

### Qu'y a-t-il de nouveau ?

Je me souviens avoir été fasciné par la quantité de nouvelles fonctionnalités que ES6 promettait d'apporter, donc si vous voulez un guide complet des nouvelles fonctionnalités, je peux vous conseiller de suivre ces « tutoriels » :

* [http://es6-features.org/](http://es6-features.org/)
* [https://github.com/lukehoban/es6features](https://github.com/lukehoban/es6features)
* [https://babeljs.io/docs/learn-es2015/](https://babeljs.io/docs/learn-es2015/)

Maintenant, discutons de certaines de mes nouvelles fonctionnalités préférées.

#### Fonctions fléchées

Les fonctions fléchées vous permettent d'écrire des fonctions anonymes de manière beaucoup plus compacte, en supprimant beaucoup de code boilerplate. Cela ouvre la voie à la programmation de style fonctionnel et permet aux programmeurs de garder leur santé mentale tout en lisant du code fonctionnel écrit par d'autres.

Le côté cool des fonctions fléchées est que vous n'avez jamais à écrire le mot **_function_** — sauf dans les cas où vous avez réellement besoin d'une fonction nommée. Ensuite, vous lisez à propos de la nouvelle [notation littérale d'objet améliorée](https://github.com/lukehoban/es6features#enhanced-object-literals) et vous réalisez que le mot **_function_** va probablement être oublié bientôt.

#### Variables à portée de bloc

Le comportement des variables à portée de fonction a longtemps été le point culminant de tout entretien JavaScript. ES2015 facilite la vie de ceux qui viennent de langages de programmation basés sur C, dans lesquels une variable est à portée du bloc de code dans lequel elle est déclarée. Avec « **let** » et « **const** », votre code est beaucoup plus expressif. Regardons quelques exemples :

Comme vous l'avez probablement compris maintenant, « **let** » est équivalent à « **var** », mais il est à portée de bloc. Cela signifie qu'il n'existe pas en dehors du bloc dans lequel il est défini.

D'autre part, « **const** » vous permet de définir une variable avec une valeur fixe. Elle ne peut recevoir une valeur que lors de sa création, et toute affectation ultérieure à une « **const** » n'a aucun effet. Cela est très important en termes d'expressivité car vous pouvez déclarer toutes les variables que vous ne modifiez pas dans votre code avec « **const** » et toutes les autres avec « **let** ». De cette façon, toute valeur qui a le potentiel de muter dans votre code est facilement traçable dès le début. Si toutes vos variables sont des constantes (sans jeu de mots), vous n'avez pas à vous soucier des effets secondaires ou des mutations d'état non désirées.

#### Déstructuration

En parlant d'expressivité, la déstructuration offre des tonnes de façons de dire plus avec moins de lignes de code. Cette fonctionnalité fait essentiellement de la **correspondance de motifs** sur les objets et les tableaux, vous permettant d'accéder rapidement à des parties de ceux-ci.

Avec la déstructuration, vous n'avez plus besoin de créer des variables qui pointent vers certaines propriétés ou sous-objets du paramètre de fonction, comme dans l'exemple _fullName()_ ci-dessus. Il est également plus facile de retourner plusieurs valeurs d'une fonction sans écrire trop de lignes de code. La déstructuration est amusante lorsqu'elle est combinée avec les nouvelles façons de gérer les paramètres de fonction : paramètres par défaut et opérateurs rest et spread.

#### Paramètres de fonction — Défaut, Rest, Spread

Les paramètres par défaut sont assez simples et sont déjà présents dans de nombreux langages de programmation, donc rien d'extraordinaire ici. Cependant, les opérateurs **rest** et **spread** vous permettent de gérer les paramètres de fonction de la manière que vous souhaitez.

#### Générateurs

D'accord, nous avons joué avec la syntaxe, nous avons fait quelques extraits de programmation de style fonctionnel cool, creusons profondément dans l'une des fonctionnalités les plus intéressantes offertes par ES2015, à savoir les **générateurs**. Très brièvement expliqué, les générateurs sont des fonctions d'usine pour les **itérateurs**. Toujours confus ? Moi aussi, mais regardons un exemple.

Alors, que se passe-t-il ici ? Un générateur est essentiellement une fonction qui peut être arrêtée à tout moment et reprise ensuite. Le générateur est arrêté lorsque l'instruction **yield** est exécutée et il retourne la valeur que nous plaçons à côté de l'instruction yield. Nous utilisons l'appel de fonction **next()** pour avancer étape par étape, en collectant la valeur produite par le générateur.

En tant que fonctionnalité supplémentaire, vous pouvez passer un paramètre à la fonction next() et ce paramètre est considéré comme le retour de l'instruction yield dans le générateur. Ainsi, nous avons essentiellement une communication bidirectionnelle entre la fonction générateur et le monde extérieur.

Le gros avantage des générateurs est leur potentiel à être utilisés dans les parties du code qui gèrent les appels asynchrones. Imaginez la situation dans laquelle vous devez effectuer 3 appels d'API distincts dans un ordre particulier, en utilisant toujours le résultat d'un appel comme paramètre pour l'appel suivant. Imaginez à quoi ressemblerait ce code avec des callbacks ou même avec des promesses.

Et si nous pouvions faire quelque chose comme ceci à la place ?

Il existe déjà des solutions fonctionnelles qui vous permettent d'écrire des appels asynchrones séquentiels avec des générateurs et des promesses. Par exemple, vous pouvez consulter cet [article qui montre une solution similaire](http://blog.mgechev.com/2014/12/21/handling-asynchronous-calls-with-es6-javascript-generators/).

Bien sûr, il y a beaucoup d'autres fonctionnalités cool comme les modèles de chaînes, les promesses natives, les modules de style AMD, de nouvelles fonctions ajoutées aux prototypes de Number, String, Array et Object, et bien plus encore. Mais j'ai présenté ici celles que je considère les plus utiles dans les tâches de codage régulières. Cependant, il y a un côté sombre avec l'une des nouvelles fonctionnalités que je veux discuter.

#### Classes

Je parie que 50 % des personnes qui ont lu les spécifications attendaient cela avec impatience, tandis que les 50 % autres disaient : « Mais… pourquoi ??? » Je fais partie de la deuxième catégorie.

ES2015 apporte une syntaxe sucrée qui utilise la création d'objets prototypaux en arrière-plan. Voici un exemple :

Sortez cela de votre tête, JavaScript n'a **PAS** de classes. JavaScript n'implémente pas la programmation orientée objet basée sur les classes et ne le fera jamais. Le modèle d'héritage en JavaScript est prototypal, les objets sont créés sur la base des prototypes d'autres objets. Tous ces éléments de syntaxe que vous voyez dans l'extrait de classe comme : constructor, get, set, static sont simplement implémentés en arrière-plan comme des fonctions régulières ou des valeurs simples ajoutées aux prototypes.

Ajouter des classes en JavaScript est probablement la pire erreur à venir. Pensez au nombre de personnes qui interprètent mal la signification de « **this** ». Multipliez cela par 10 et vous obtenez le nombre de personnes qui interpréteront mal la signification de « **class** ».

Toutes ces constructions viennent du monde de l'orientation objet basée sur les classes. Les gens doivent simplement abandonner ces pratiques, car elles ne correspondent pas aux paradigmes implémentés en JavaScript. De plus, elles confondent les nouveaux venus plus que jamais.

> Venir à JavaScript et demander comment faire de l'héritage classique, c'est comme prendre un téléphone mobile à écran tactile et demander où se trouve le cadran rotatif. Bien sûr, les gens seront amusés lorsque la prochaine chose qui sortira de votre bouche sera : « Si cela n'a pas de cadran rotatif, ce n'est pas un téléphone ! » — _Eric Elliott, Programming JavaScript Applications_

Mon entretien standard contient le jeu de questions suivantes que je pose en succession :

* « Les classes sont-elles obligatoires en POO ? »
* « JavaScript est-il un langage POO ? »
* « A-t-il des classes ? »

Imaginez combien de temps je vais potentiellement perdre à essayer d'expliquer aux gens que les « classes » qu'ils voient en JavaScript ne sont en réalité PAS des classes.

### Adoptez la programmation fonctionnelle

Du côté positif, avec ES2015, nous avons toutes ces nouvelles fonctionnalités qui nous permettent d'écrire un meilleur code, plus propre et, dans une certaine mesure, plus rapide. Je pense que maintenant est le moment d'adopter la programmation fonctionnelle comme paradigme fondamental en JavaScript. De préférence, vous n'aurez plus jamais à écrire une seule instruction de boucle, sauf dans certaines situations rares.

Avec **const** et **let**, vous êtes en mesure d'ajouter un autre niveau d'expressivité à toutes vos variables. Vous éviterez probablement d'utiliser **var** à partir de ce moment. Les fonctions fléchées combinées avec les fonctions itératrices classiques vous permettent d'écrire de la programmation réactive fonctionnelle, créant essentiellement des flux de fonctionnalités.

Votre code devient plus succinct, plus fonctionnel et moins étatique. Cela signifie également que votre code est plus facile à tester et à maintenir, et également beaucoup moins sujet aux bugs, et présente des fonctions pures, des données immuables. Il y a beaucoup de contenu là-bas sur les avantages de la programmation fonctionnelle, et je pense qu'itérer à nouveau sur ces points n'a pas de sens dans le cadre de cet article.

Travailler avec Babel n'est pas si difficile, et je vous encourage à commencer dès aujourd'hui. Souvenez-vous, le code que vous écrivez aujourd'hui en utilisant la syntaxe ES5 est obsolète. Juste et simple.

### Qu'est-ce qui suit ?

ES2015 était une version majeure avec beaucoup de changements. Le comité TC39 a commencé avec une approche différente et ils standardiseront de nouvelles fonctionnalités chaque année, divisant essentiellement ce qui était initialement prévu pour être implémenté comme ES7 en morceaux plus petits.

Certaines des futures fonctionnalités de JavaScript incluront : les fonctions asynchrones, les décorateurs d'objets/fonctions et des choses comme les opérations SIMD (single instruction, multiple data).

Habituellement, toutes les futures fonctionnalités sont appelées génériquement ESnext, au cas où vous verriez cela quelque part. Avec Babel, vous pouvez même jouer avec certaines de ces futures fonctionnalités aujourd'hui !

Voici quelques articles que je recommande de lire concernant les fonctionnalités ESnext :

* [http://www.2ality.com/2015/11/tc39-process.html](http://www.2ality.com/2015/11/tc39-process.html)
* [https://medium.com/google-developers/exploring-es7-decorators-76ecb65fb841#.hrg2xk5q1](https://medium.com/google-developers/exploring-es7-decorators-76ecb65fb841#.hrg2xk5q1)
* [https://www.twilio.com/blog/2015/10/asyncawait-the-hero-javascript-deserved.html](https://www.twilio.com/blog/2015/10/asyncawait-the-hero-javascript-deserved.html)
* [https://github.com/tc39/ecma262](https://github.com/tc39/ecma262) (statut officiel des fonctionnalités)