---
title: Psst ! Voici pourquoi ReasonReact est la meilleure façon d'écrire React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T17:10:34.000Z'
originalURL: https://freecodecamp.org/news/psst-heres-why-reasonreact-is-the-best-way-to-write-react-5088d434d035
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jU57ThAZc50pyAG1INey3g.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: reasonml
  slug: reasonml
- name: Web Development
  slug: web-development
seo_title: Psst ! Voici pourquoi ReasonReact est la meilleure façon d'écrire React
seo_desc: 'By David Kopal

  Are you using React to build user interfaces? Well, I am too. And now, you’ll learn
  why you should write your React applications using ReasonML.

  React is a pretty cool way to write user interfaces. But, could we make it even
  cooler? Be...'
---

Par David Kopal

Utilisez-vous [React](https://reactjs.org/) pour construire des interfaces utilisateur ? Moi aussi. Et maintenant, vous allez apprendre pourquoi vous devriez écrire vos applications React [en utilisant ReasonML](https://medium.freecodecamp.org/learn-reasonml-by-building-tic-tac-toe-in-react-334203dd513c).

React est une façon assez cool d'écrire des interfaces utilisateur. Mais, pourrait-on le rendre encore plus cool ? Meilleur ?

Pour l'améliorer, nous devons d'abord identifier ses problèmes. Alors, quel est le principal problème de React en tant que bibliothèque JavaScript ?

### **React n'a pas été initialement développé pour JavaScript**

Si vous regardez React de plus près, vous verrez que certains de ses principes principaux sont étrangers à JavaScript. Parlons de l'immutabilité, des principes de la programmation fonctionnelle et du système de types en particulier.

L'immutabilité est l'un des principes fondamentaux de React. Vous ne voulez pas muter vos props ou votre état, car si vous le faites, vous pourriez rencontrer des conséquences imprévisibles. En JavaScript, nous n'avons pas l'immutabilité par défaut. Nous gardons nos structures de données immutables par convention, ou nous utilisons des bibliothèques telles que [immutableJS](https://facebook.github.io/immutable-js/) pour l'atteindre.

React est basé sur les principes de la programmation fonctionnelle puisque ses applications sont des compositions de fonctions. Bien que JavaScript possède certaines de ces fonctionnalités, comme les fonctions de première classe, ce n'est pas un langage de programmation fonctionnelle. Lorsque nous voulons écrire du code déclaratif, nous devons utiliser des bibliothèques externes comme [Lodash/fp](https://github.com/lodash/lodash/wiki/FP-Guide) ou [Ramda](https://ramdajs.com/).

Alors, qu'en est-il du système de types ? Dans React, nous avions [PropTypes](https://reactjs.org/docs/typechecking-with-proptypes.html). Nous les avons utilisés pour imiter les types en JavaScript, puisque ce n'est pas un langage typé statiquement. Pour tirer parti du typage statique avancé, nous devons à nouveau utiliser des dépendances externes, telles que [Flow](https://flow.org/) et [TypeScript](https://www.typescriptlang.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/MBTOborji3cqg5Fulhsv9cA3tiEoSi8fu3l4)
_Comparaison entre React et JavaScript_

Comme vous pouvez le voir, **JavaScript n'est pas compatible avec les principes fondamentaux de React.**

Existe-t-il un autre langage de programmation qui serait plus compatible avec React que JavaScript ?

Heureusement, nous avons [ReasonML](https://reasonml.github.io/).

Avec Reason, nous obtenons l'immutabilité par défaut. Puisqu'il est basé sur [OCaml](https://ocaml.org/), le langage de programmation fonctionnelle, nous avons également ces fonctionnalités intégrées dans le langage lui-même. Reason nous fournit également un système de types solide.

![Image](https://cdn-media-1.freecodecamp.org/images/QHbj6LVoIlCNOKjfeZdBDkRBClnsL1qnz5kr)
_Comparaison entre React, JavaScript et Reason_

Reason est compatible avec les principes fondamentaux de React.

### Reason

Ce n'est pas un nouveau langage. C'est une syntaxe alternative similaire à JavaScript et une chaîne d'outils pour OCaml, un langage de programmation fonctionnelle qui existe depuis plus de 20 ans. Reason a été créé par des développeurs de Facebook qui utilisaient déjà OCaml dans leurs projets ([Flow,](https://github.com/facebook/flow) [Infer](https://github.com/facebook/infer)).

![Image](https://cdn-media-1.freecodecamp.org/images/iZOPlVop1OKOO36dranfKTTg9P0b0PGtCR6x)

Reason, avec sa syntaxe de type C, rend OCaml accessible aux personnes venant de langages grand public tels que JavaScript ou Java. Il vous fournit une meilleure documentation (comparée à OCaml) et une [communauté grandissante](https://reasonml.github.io/docs/en/community) autour de lui. De plus, il facilite l'intégration avec votre base de code JavaScript existante.

![Image](https://cdn-media-1.freecodecamp.org/images/FeHSk51tA2kwbv2sVbu-QinVHCzYipvQUMWp)

OCaml sert de langage de support pour Reason. Reason a la même sémantique que OCaml — seule la syntaxe est différente. Cela signifie que vous pouvez écrire OCaml en utilisant la syntaxe de type JavaScript de Reason. En conséquence, vous pouvez tirer parti des fonctionnalités impressionnantes de OCaml, telles que son système de types solide et la correspondance de motifs.

Prenons un exemple de la syntaxe de Reason.

```js
let fizzbuzz = (i) =>
  switch (i mod 3, i mod 5) {
  | (0, 0) => "FizzBuzz"
  | (0, _) => "Fizz"
  | (_, 0) => "Buzz"
  | _ => string_of_int(i)
  };
for (i in 1 to 100) {
  Js.log(fizzbuzz(i))
};
```

Bien que nous utilisions la correspondance de motifs dans cet exemple, cela reste assez similaire à JavaScript, n'est-ce pas ?

Cependant, le seul langage utilisable pour les navigateurs est toujours JavaScript, ce qui signifie que nous devons le compiler.

#### BuckleScript

![Image](https://cdn-media-1.freecodecamp.org/images/X36FEoHL7z2YWiiLNhNWbOy0Wx5O7FTEerBX)

L'une des fonctionnalités puissantes de Reason est le [compilateur BuckleScript](https://bucklescript.github.io/), qui prend votre code Reason et le compile en JavaScript lisible et performant avec une excellente élimination du code mort. Vous apprécierez la lisibilité si vous travaillez dans une équipe où tout le monde ne connaît pas Reason, car ils pourront toujours lire le code JavaScript compilé.

La similarité avec JavaScript est si proche que certaines parties du code de Reason n'ont pas besoin d'être modifiées par le compilateur. Ainsi, vous pouvez profiter des avantages du langage typé statiquement sans aucun changement dans le code.

```
let add = (a, b) => a + b;add(6, 9);
```

Ce code est valide à la fois en Reason et en JavaScript.

BuckleScript est livré avec quatre bibliothèques : la bibliothèque standard appelée [Belt](https://bucklescript.github.io/bucklescript/api/Belt.html) ([la bibliothèque standard OCaml est insuffisante](https://discuss.ocaml.org/t/what-is-the-preferable-solution-for-the-role-of-standard-library/1092)), et des liaisons avec JavaScript, Node.js et les API DOM.

Puisque BuckleScript est basé sur le compilateur OCaml, vous obtiendrez [une compilation ultra-rapide](https://bucklescript.github.io/docs/en/build-performance) qui est beaucoup plus rapide que Babel et plusieurs fois plus rapide que TypeScript.

Compilons notre algorithme FizzBuzz écrit en Reason en JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/IQVd0AQHgI7i26a21uf9kALk6xi2CzpGcoiM)
_Compilation du code Reason en JavaScript via BuckleScript_

Comme vous pouvez le voir, le code JavaScript résultant est assez lisible. Il semble qu'il ait été écrit par un développeur JavaScript.

Non seulement Reason compile en JavaScript, mais aussi en natif et en bytecode. Ainsi, vous pouvez écrire une seule application en utilisant la syntaxe Reason et être en mesure de l'exécuter dans le navigateur sur MacOS, Android et iOS. Il existe un jeu appelé [Gravitron](https://github.com/jaredly/gravitron) par Jared Forsyth qui est écrit en Reason et peut être exécuté sur toutes les plateformes que je viens de mentionner.

#### Interopérabilité JavaScript

BuckleScript nous fournit également l'[interopérabilité](https://en.wikipedia.org/wiki/Interoperability) avec JavaScript. Non seulement vous pouvez coller votre code JavaScript fonctionnel dans votre base de code Reason, mais votre code Reason peut également interagir avec ce code JavaScript. Cela signifie que vous pouvez facilement intégrer le code Reason dans votre base de code JavaScript existante. De plus, vous pouvez utiliser tous les packages JavaScript de l'écosystème NPM dans votre code Reason. Par exemple, vous pouvez combiner Flow, TypeScript et Reason ensemble dans un seul projet.

Cependant, ce n'est pas si simple. Pour utiliser des bibliothèques ou du code JavaScript dans Reason, vous devez d'abord les porter vers Reason via des liaisons Reason. En d'autres termes, vous avez besoin de types pour votre code JavaScript non typé afin de pouvoir tirer parti du système de types solide de Reason.

Chaque fois que vous avez besoin d'utiliser une bibliothèque JavaScript dans votre code Reason, vérifiez si la bibliothèque a déjà été portée vers Reason en parcourant la base de données de l'index des packages Reason ([Redex](https://redex.github.io/)). C'est un site qui agrège différentes bibliothèques et outils écrits en Reason et des bibliothèques JavaScript avec des liaisons Reason. Si vous avez trouvé votre bibliothèque là-bas, vous pouvez simplement l'installer en tant que dépendance et l'utiliser dans votre application Reason.

Cependant, si vous n'avez pas trouvé votre bibliothèque, vous devrez écrire les liaisons Reason vous-même. Si vous commencez tout juste avec Reason, gardez à l'esprit que l'écriture de liaisons n'est pas quelque chose que vous voulez commencer, car c'est l'une des choses les plus difficiles dans l'écosystème de Reason.

Heureusement, je suis en train d'écrire un article sur l'écriture de liaisons Reason, alors restez à l'écoute !

Lorsque vous avez besoin d'une fonctionnalité d'une bibliothèque JavaScript, vous n'avez pas besoin d'écrire les liaisons Reason pour toute la bibliothèque. Vous pouvez le faire uniquement pour les fonctions ou composants que vous devez utiliser.

### ReasonReact

Cet article parle de l'écriture de React en Reason, ce que vous pouvez faire grâce à la [bibliothèque ReasonReact](https://reasonml.github.io/reason-react/).

Peut-être pensez-vous maintenant « Je ne sais toujours pas pourquoi je devrais utiliser React en Reason. »

Nous avons déjà mentionné la principale raison de le faire — Reason est plus compatible avec React que JavaScript. Pourquoi est-il plus compatible ? Parce que React a été développé pour Reason, ou plus précisément, pour OCaml.

#### Le chemin vers ReasonReact

![Image](https://cdn-media-1.freecodecamp.org/images/biX58BUYBBeSlVU4t3h4n-wBYAqi8oFUXReH)

Le premier prototype de React a été développé par Facebook et a été écrit en Standard Meta Language ([StandardML](https://en.wikipedia.org/wiki/Standard_ML)), un cousin de OCaml. Ensuite, il a été porté vers OCaml. React a également été transcrit en JavaScript.

C'était parce que tout le web utilisait JavaScript, et il n'était probablement pas intelligent de dire, « Maintenant, nous allons construire des interfaces utilisateur en OCaml. » Et cela a fonctionné — React en JavaScript a été largement adopté.

Ainsi, nous nous sommes habitués à React en tant que bibliothèque JavaScript. React, ainsi que d'autres bibliothèques et langages — [Elm](https://elm-lang.org/), [Redux](https://redux.js.org/), [Recompose](https://github.com/acdlite/recompose), [Ramda](https://ramdajs.com/), et [PureScript](http://www.purescript.org/) — ont rendu la programmation fonctionnelle en JavaScript populaire. Et avec l'essor de [Flow](https://flow.org/) et [TypeScript](https://www.typescriptlang.org/), le typage statique est également devenu populaire. En conséquence, le paradigme de la programmation fonctionnelle avec des types statiques est devenu courant dans le monde du front-end.

En 2016, [Bloomberg](https://www.bloomberg.com/company/announcements/open-source-at-bloomberg-introducing-bucklescript/) a développé et open-sourcé BuckleScript, le compilateur qui transforme OCaml en JavaScript. Cela leur a permis d'écrire du code sûr sur le front-end en utilisant le système de types solide de OCaml. Ils ont pris le compilateur OCaml optimisé et ultra-rapide et ont échangé son back-end générant du code natif pour un générateur de code JavaScript.

La popularité de la **programmation fonctionnelle** ainsi que la sortie de BuckleScript ont généré le climat idéal pour que Facebook revienne à l'idée originale de React, qui a été initialement écrit dans un [langage ML](https://en.wikipedia.org/wiki/ML_(programming_language)).

![Image](https://cdn-media-1.freecodecamp.org/images/XrSsanYlN4ilFGc7k97yqreJTWjNx0IQrOHl)
_ReasonReact_

Ils ont pris la sémantique de OCaml et la syntaxe de JavaScript, et créé Reason. Ils ont également créé l'enveloppe Reason autour de React — la bibliothèque ReasonReact — avec des fonctionnalités supplémentaires telles que l'encapsulation des principes de Redux dans des composants avec état. En faisant cela, ils ont ramené [React à ses racines originales](https://news.ycombinator.com/item?id=15209704).

#### La puissance de React dans Reason

Lorsque React est arrivé dans JavaScript, nous avons ajusté JavaScript aux besoins de React en introduisant diverses bibliothèques et outils. Cela a également signifié plus de dépendances pour nos projets. Sans parler du fait que ces bibliothèques sont encore en développement et que des changements majeurs sont introduits régulièrement. Vous devez donc maintenir ces dépendances avec soin dans vos projets.

Cela a ajouté une autre couche de complexité au développement JavaScript.

Votre application React typique aura au moins ces dépendances :

![Image](https://cdn-media-1.freecodecamp.org/images/AAN8F1esKaCoYudXoz90QfiWd40IrF8B4IRc)

* typage statique — Flow/TypeScript
* immutabilité — immutableJS
* routage — ReactRouter
* formatage — Prettier
* linting — ESLint
* fonctions d'aide — Ramda/Lodash

Remplaçons maintenant React JavaScript par ReasonReact.

Avons-nous encore besoin de toutes ces dépendances ?

![Image](https://cdn-media-1.freecodecamp.org/images/tMqUDBPlT3UvrGwf9UqaBTXanS6QgUqEmOSi)

* typage statique — **intégré**
* immutabilité — **intégré**
* routage — **intégré**
* formatage — **intégré**
* linting — **intégré**
* fonctions d'aide — **intégré**

Vous pouvez en apprendre plus sur [ces fonctionnalités intégrées dans mon autre article.](https://www.codinglawyer.io/posts/why-building-stuff-in-reason)

Dans une application ReasonReact, vous n'avez pas besoin de ces dépendances et de nombreuses autres, car de nombreuses fonctionnalités cruciales qui facilitent votre développement sont déjà incluses dans le langage lui-même. Ainsi, la maintenance de vos packages deviendra plus facile et vous n'aurez pas d'augmentation de la complexité au fil du temps.

Cela est grâce à OCaml, qui a plus de 20 ans. C'est un langage mature avec tous ses principes fondamentaux en place et stables.

### Conclusion

Au début, les créateurs de Reason avaient deux options. Prendre JavaScript et somehow l'améliorer. En faisant cela, ils devraient également traiter ses fardeaux historiques.

Cependant, ils ont pris un chemin différent. Ils ont pris OCaml comme un langage mature avec de grandes performances et l'ont modifié pour qu'il ressemble à JavaScript.

React est également basé sur les principes de OCaml. C'est pourquoi vous obtiendrez une bien meilleure expérience de développement lorsque vous l'utiliserez avec Reason. React dans Reason représente une façon plus sûre de construire des composants React, puisque le système de types solide vous soutient et vous n'avez pas à traiter la plupart des problèmes de JavaScript (héritage).

### Qu'est-ce qui suit ?

![Image](https://cdn-media-1.freecodecamp.org/images/yD9SkLowMRhycLIc0Zz4X0VjYig9qDQb7EjK)

Si vous venez du monde de JavaScript, il vous sera plus facile de commencer avec Reason, grâce à sa similarité syntaxique avec JavaScript. Si vous avez programmé en React, ce sera encore plus facile pour vous, car vous pouvez utiliser toutes vos connaissances React, puisque ReasonReact a le même modèle mental que React et un flux de travail très similaire. Cela signifie que vous n'avez pas besoin de commencer à partir de zéro. Vous apprendrez Reason au fur et à mesure que vous développerez.

La meilleure façon de commencer à utiliser Reason dans vos projets est de le faire de manière incrémentielle. J'ai déjà mentionné que vous pouvez prendre du code Reason et l'utiliser en JavaScript, et vice versa. Vous pouvez faire la même chose avec ReasonReact. Vous prenez votre composant ReasonReact et l'utilisez dans votre application React JavaScript, et inversement.

Cette approche incrémentielle a été choisie par les développeurs de Facebook qui utilisent Reason de manière extensive dans le développement de [l'application Facebook Messenger](https://reasonml.github.io/blog/2017/09/08/messenger-50-reason.html).

Si vous voulez construire une application en utilisant React dans Reason et apprendre les bases de Reason de manière pratique, consultez mon autre article où [nous construirons ensemble un jeu de Tic Tac Toe.](https://medium.freecodecamp.org/learn-reasonml-by-building-tic-tac-toe-in-react-334203dd513c)

Si vous avez des questions, des critiques, des observations ou des conseils pour l'amélioration, n'hésitez pas à écrire un commentaire ci-dessous ou à me contacter via [Twitter](https://twitter.com/coding_lawyer) ou [mon blog](https://www.codinglawyer.io/).